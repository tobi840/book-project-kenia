#!/usr/bin/env python3
"""Baut buch/kenia-vorgelesen.pdf aus denselben Quellen wie buch_bauen.py.

Warum ein eigenes Skript und nicht der Druck-Abschnitt aus buch_bauen.py:
Die Bildschirmseite ist eine einzige lange Bahn. Ein Buch ist ein Stapel
Blaetter. Das braucht anderen Satz, nicht nur andere Schriftgroessen:
Kolumnentitel, Seitenzahlen, ein Inhaltsverzeichnis mit echten Seitenzahlen,
Silbentrennung, Schusterjungen und Hurenkinder.

Drei Entscheidungen, die man kennen sollte:

* Gesetzt wird mit WeasyPrint, nicht mit einem Browser. Nur so gibt es
  target-counter(), also ein Inhaltsverzeichnis, das die Seitenzahl kennt,
  auf der das Kapitel wirklich steht.
* Die Schrift ist Literata (SIL Open Font License, liegt unter schriften/).
  Die Bildschirmschrift des Buches, Iowan Old Style, ist nicht frei. Was auf
  diesem Rechner sonst da ist, hat keinen echten Kursivschnitt, und bei rund
  hundert lateinischen Artnamen faellt ein schraeg gestellter Normalschnitt
  auf.
* Gezaehlt wird ab dem Cover durch. Die Seitenzahl im Inhaltsverzeichnis ist
  damit dieselbe Zahl, die der PDF-Betrachter anzeigt. Auf Cover, Titel und
  Inhalt steht sie nur nicht gedruckt.

Aufruf:
    python3 scripts/pdf_bauen.py
    python3 scripts/pdf_bauen.py --nur 5              # kleines Testbuch
    python3 scripts/pdf_bauen.py --format buch        # 165 mal 240 mm
    python3 scripts/pdf_bauen.py --druck              # Bundsteg, Kapitel rechts
"""

import argparse
import datetime
import glob
import html
import os
import re
import shutil
import string
import sys
import tempfile
import uuid

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import buch_bauen as bb
import epub_bauen as eb

ZIEL = ("buch", "kenia-vorgelesen.pdf")
REISE = "Kenia, 24. September bis 12. Oktober 2026"

# Seitengroesse, Rand oben, unten, aussen, innen, Grundschrift, Bildbreite.
# Die Bildbreite ist kein Geschmack, sondern Arithmetik: Die Illustrationen
# sind 3:4 hoch. Volle Satzbreite ergaebe ein Bild, das allein hoeher ist als
# der Satzspiegel. Die Werte hier lassen unter jedem Bild noch Text stehen.
FORMATE = {
    "a4": dict(groesse="210mm 297mm", oben="25mm", unten="22mm",
               aussen="30mm", innen="30mm", schrift="12pt", bild="118mm"),
    "a5": dict(groesse="148mm 210mm", oben="15mm", unten="14mm",
               aussen="14mm", innen="16mm", schrift="10pt", bild="88mm"),
    "buch": dict(groesse="165mm 240mm", oben="18mm", unten="16mm",
                 aussen="16mm", innen="19mm", schrift="10.5pt", bild="100mm"),
}

CSS = string.Template("""
@font-face { font-family: Buch; src: url(schriften/Literata.ttf);
             font-weight: 200 900; font-style: normal; }
@font-face { font-family: Buch; src: url(schriften/Literata-Italic.ttf);
             font-weight: 200 900; font-style: italic; }

@page {
  size: $groesse;
  margin: $oben $aussen $unten $innen;
  @top-left { content: none; }
  @top-right { content: none; }
}
@page :left {
  margin-left: $aussen; margin-right: $innen;
  @top-left { content: string(verso, first-except); font-family: Buch; font-size: 8pt;
              color: #6b6355; letter-spacing: .06em; padding-bottom: 4mm; }
  @bottom-left { content: counter(page); font-family: Buch; font-size: 9pt;
                 color: #6b6355; padding-top: 4mm; }
}
@page :right {
  margin-left: $innen; margin-right: $aussen;
  @top-right { content: string(kolumne, first-except); font-family: Buch; font-size: 8pt;
               color: #6b6355; letter-spacing: .06em; padding-bottom: 4mm; }
  @bottom-right { content: counter(page); font-family: Buch; font-size: 9pt;
                  color: #6b6355; padding-top: 4mm; }
}
/* Vorspann laeuft im Seitenzaehler mit, traegt aber nichts im Kopf und Fuss. */
@page stumm {
  @top-left { content: none; } @top-right { content: none; }
  @bottom-left { content: none; } @bottom-right { content: none; }
}
@page cover { margin: 0;
  @top-left { content: none; } @top-right { content: none; }
  @bottom-left { content: none; } @bottom-right { content: none; }
}

html {
  font-family: Buch, serif;
  font-size: $schrift;
  line-height: 1.46;
  color: #1f1c18;
  hyphens: auto;
}
body { margin: 0; }
em { font-style: italic; }
a { color: inherit; text-decoration: none; }

/* Fliesstext im Buchsatz: kein Abstand zwischen Absaetzen, dafuer Einzug.
   Der erste Absatz nach einer Ueberschrift bleibt stumpf. */
section p, .einleitung > p {
  margin: 0;
  text-indent: 1.3em;
  text-align: justify;
  orphans: 2;
  widows: 2;
}
section > h2 + p, .einleitung-kopf + p { text-indent: 0; }

/* Cover */
.cover { page: cover; break-after: page; }
.cover img { width: 100%; height: 100%; object-fit: contain; display: block; }
.nur-vorlesen { display: none; }

/* Titelseite */
.titel { page: stumm; break-after: page; text-align: center;
         padding-top: 55mm; }
.titel h1 { font-size: 26pt; font-weight: 600; margin: 0 0 3mm;
            line-height: 1.15; bookmark-level: 1; bookmark-label: "Titel"; }
.titel .untertitel { font-size: 12pt; color: #6b6355; font-style: italic;
                     margin: 0 0 22mm; }
.titel .autor { font-size: 12pt; margin: 0 0 3mm; }
.titel .reise { font-size: 8.5pt; color: #6b6355; letter-spacing: .1em;
                text-transform: uppercase; margin: 0; }

/* Inhaltsverzeichnis */
.inhalt { page: stumm; break-after: page; }
.inhalt h1 { font-size: 20pt; font-weight: 600; margin: 0 0 8mm;
             bookmark-level: 1; bookmark-label: "Inhalt"; }
.inhalt h2 { font-size: 10pt; font-weight: 600; color: #8a3b1e;
             letter-spacing: .1em; text-transform: uppercase;
             margin: 7mm 0 2mm; bookmark-level: none; break-after: avoid; }
.inhalt ol { list-style: none; margin: 0; padding: 0; }
.inhalt li { margin: 0 0 .9mm; font-size: 9.5pt; }
.inhalt li .nr { color: #6b6355; font-variant-numeric: tabular-nums;
                 margin-right: 2.5mm; }
.inhalt a::after { content: leader('.') ' ' target-counter(attr(href), page);
                   color: #6b6355; }
.inhalt .ohne-nr a::after { content: ''; }

/* Einleitung und Abschnittseinleitungen */
/* Kein string-set auf dem Artikel selbst: WeasyPrint wertet die
   Zuweisung auf jeder Seite aus, ueber die der Block laeuft, und
   first-except unterdrueckt den Kolumnentitel dann ueberall. Den
   Titel setzt allein die Ueberschrift. */
.einleitung { break-before: page; }
.einleitung-kopf { margin: 0 0 7mm; border-bottom: 1.5pt solid #8a3b1e;
                   padding-bottom: 3mm; }
.einleitung-kopf h1 { font-size: 22pt; font-weight: 600; margin: 0;
                      line-height: 1.15; bookmark-level: 1;
                      string-set: kolumne content(), verso "$buchtitel"; }
.abschnitt-nr { color: #8a3b1e; letter-spacing: .12em; text-transform: uppercase;
                font-size: 8pt; margin: 0 0 1.5mm; }
.einleitung-kopf .untertitel { color: #6b6355; margin: 2mm 0 0;
                               font-style: italic; font-size: 11pt; }

/* Kapitel */
.kapitel { break-before: page; }
.kapitel-kopf { margin: 0 0 6mm; }
.lebensraum { color: #8a3b1e; letter-spacing: .12em; text-transform: uppercase;
              font-size: 7.5pt; margin: 0 0 1.5mm; }
.kapitel-kopf h1 { font-size: 19pt; font-weight: 600; margin: 0;
                   line-height: 1.18; bookmark-level: 2;
                   string-set: kolumne content(), verso "$buchtitel"; }
.lateinisch { margin: 1mm 0 0; color: #6b6355; font-size: 10.5pt; }
.namen { margin: 2.5mm 0 0; font-size: 8.5pt; color: #6b6355; line-height: 1.35; }

.illustration { break-inside: avoid; margin: 0 0 6mm; text-align: center; }
.illustration img { width: $bild; height: auto; display: block; margin: 0 auto; }
.illustration figcaption { font-size: 8pt; color: #6b6355; font-style: italic;
                           margin: 2.5mm auto 0; text-align: left;
                           max-width: $bild; line-height: 1.35; }

/* Die Ueberschrift "Geschichte" steht schon auf dem Bildschirm nur fuer
   Vorleseprogramme da. Im Buch waere sie ueber dem ersten Absatz doppelt. */
.geschichte h2 { display: none; }
.kapitel h2 { font-size: 9pt; letter-spacing: .1em; text-transform: uppercase;
              color: #8a3b1e; margin: 6mm 0 2mm; font-weight: 600;
              bookmark-level: none; break-after: avoid; }
.menschen-kultur, .vor-der-linse { border-left: 1.5pt solid #ddd5c6;
                                   padding-left: 4mm; }
.querverweis { color: #6b6355; }
""")


def plan_bauen(nur):
    """Kapitel nach Abschnitten gruppieren, genau wie buch_bauen.bau()."""
    tsv = bb.lies_tsv()
    if nur:
        tsv = tsv[:nur]
    nach_lebensraum = {}
    for nr, name, lebensraum in tsv:
        nach_lebensraum.setdefault(lebensraum, []).append((nr, name))
    unbekannt = set(nach_lebensraum) - {a[0] for a in bb.ABSCHNITTE}
    if unbekannt:
        sys.exit("Lebensraum ohne Abschnitt: %s" % ", ".join(sorted(unbekannt)))

    plan, fehlend = [], []
    for lebensraum, anr, titel in bb.ABSCHNITTE:
        kapitel = []
        for nr, name in nach_lebensraum.get(lebensraum, []):
            datei = bb.kapiteldatei(nr)
            if datei:
                kapitel.append((nr, name, datei))
            else:
                fehlend.append("Kapitel %s" % nr)
        plan.append((lebensraum, anr, titel, kapitel))
    return plan, fehlend


def block_holen(quelle, kennung, bildnamen):
    """Article-Block einer Datei, mit id und umgebogenen Bildpfaden."""
    roh = open(quelle, encoding="utf-8").read()
    block = bb.artikel(roh)
    if block is None:
        raise ValueError("Kein <article> in %s" % quelle)
    block = eb.nach_xhtml(block, bildnamen)
    return block.replace("<article ", '<article id="%s" ' % kennung, 1)


def bau(nur, format_name, druck, breite, qualitaet, ziel):
    try:
        from weasyprint import HTML
    except ImportError:
        sys.exit("WeasyPrint fehlt. Einmalig: python3 -m pip install weasyprint")

    masse = dict(FORMATE[format_name])
    masse["buchtitel"] = bb.TITEL
    if not druck:
        # Ohne Bundsteg sind beide Raender gleich. Sonst steht der Satzspiegel
        # im Bildschirm-PDF bei jedem Blaettern ein Stueck versetzt.
        masse["innen"] = masse["aussen"]

    schriften = bb.pfad("schriften")
    for datei in ("Literata.ttf", "Literata-Italic.ttf"):
        if not os.path.exists(os.path.join(schriften, datei)):
            sys.exit("Schrift fehlt: schriften/%s" % datei)

    plan, fehlend = plan_bauen(nur)

    # Bilder einsammeln und umrechnen. Dieselbe Umrechnung wie im EPUB, nur
    # mit mehr Reserve: gedruckt wird ein Bild nicht noch einmal skaliert.
    quellen = []
    cover = bb.pfad("buch", "cover.png")
    if os.path.exists(cover):
        quellen.append(cover)
    for _, _, _, kapitel in plan:
        for _, _, datei in kapitel:
            block = bb.artikel(open(datei, encoding="utf-8").read())
            for treffer in re.finditer(r'src="([^"]+)"', block or ""):
                pfad_bild = os.path.normpath(
                    os.path.join(os.path.dirname(datei), treffer.group(1))
                )
                if os.path.exists(pfad_bild):
                    quellen.append(pfad_bild)
                else:
                    fehlend.append("Bild %s" % treffer.group(1))
    quellen = sorted(set(quellen))
    print("Bilder werden umgerechnet: %d Stueck" % len(quellen))
    bildnamen, bilddaten = eb.bilder_umrechnen(quellen, breite, qualitaet)

    bauplatz = tempfile.mkdtemp(prefix="pdf-bau-")
    try:
        os.makedirs(os.path.join(bauplatz, "bilder"))
        for name, daten in bilddaten.items():
            with open(os.path.join(bauplatz, "bilder", name), "wb") as f:
                f.write(daten)
        os.symlink(schriften, os.path.join(bauplatz, "schriften"))

        teile = ["<!DOCTYPE html>", '<html lang="de">', "<head>",
                 '<meta charset="utf-8">',
                 "<title>%s</title>" % html.escape(bb.TITEL),
                 '<meta name="author" content="%s">' % html.escape(bb.AUTOR),
                 '<meta name="description" content="%s">' % html.escape(bb.UNTERTITEL),
                 "<style>%s</style>" % CSS.substitute(masse),
                 "</head>",
                 "<body>"]

        # Cover
        if os.path.exists(cover):
            teile.append('<div class="cover"><img src="bilder/%s" alt="%s">'
                         "</div>" % (bildnamen[os.path.basename(cover)],
                                     html.escape("%s. %s. %s" % (bb.TITEL, bb.UNTERTITEL, bb.AUTOR))))
        else:
            fehlend.append("Cover")

        # Titelseite
        teile.append('<div class="titel"><h1>%s</h1>'
                     '<p class="untertitel">%s</p>'
                     '<p class="autor">%s</p>'
                     '<p class="reise">%s</p></div>'
                     % (html.escape(bb.TITEL), html.escape(bb.UNTERTITEL),
                        html.escape(bb.AUTOR), html.escape(REISE)))

        # Inhaltsverzeichnis
        teile.append('<div class="inhalt"><h1>Inhalt</h1>')
        teile.append('<ol><li><a href="#einleitung">Einleitung</a></li></ol>')
        for _, anr, titel, kapitel in plan:
            if not kapitel:
                continue
            teile.append('<h2><a href="#abschnitt-%s">%s</a></h2>' % (anr, html.escape(titel)))
            teile.append("<ol>")
            for nr, name, _ in kapitel:
                teile.append('<li><a href="#k%s"><span class="nr">%s</span>%s</a></li>'
                             % (nr, nr, html.escape(name)))
            teile.append("</ol>")
        teile.append("</div>")

        # Einleitung
        quelle = bb.pfad("einleitungen", "00-einleitung.html")
        if os.path.exists(quelle):
            teile.append(block_holen(quelle, "einleitung", bildnamen))
        else:
            fehlend.append("Einleitung 00")

        # Abschnitte und Kapitel
        gebaut = 0
        for _, anr, titel, kapitel in plan:
            if not kapitel:
                continue
            quelle = sorted(glob.glob(bb.pfad("einleitungen", anr + "-*.html")))
            if quelle:
                teile.append(block_holen(quelle[0], "abschnitt-%s" % anr, bildnamen))
            else:
                fehlend.append("Einleitung %s" % anr)
            for nr, name, datei in kapitel:
                if druck:
                    # Im Druck beginnt ein Kapitel rechts. Das kostet leere
                    # Rueckseiten, ist aber die Konvention.
                    teile.append('<div style="break-before: right"></div>')
                teile.append(block_holen(datei, "k%s" % nr, bildnamen))
                gebaut += 1

        teile.append("</body></html>")

        quelldatei = os.path.join(bauplatz, "buch.html")
        with open(quelldatei, "w", encoding="utf-8") as f:
            f.write("\n".join(teile))

        kennung = uuid.uuid5(uuid.NAMESPACE_URL,
                             "https://github.com/tobi840/book-project-kenia#pdf")
        os.makedirs(bb.pfad("buch"), exist_ok=True)
        dokument = HTML(filename=quelldatei).render()
        dokument.write_pdf(ziel, pdf_identifier=kennung.bytes, uncompressed_pdf=False)
        seiten = len(dokument.pages)
    finally:
        shutil.rmtree(bauplatz, ignore_errors=True)

    groesse = os.path.getsize(ziel) / 1e6
    bildgroesse = sum(len(d) for d in bilddaten.values()) / 1e6
    print("%s geschrieben" % os.path.relpath(ziel, bb.WURZEL))
    print("  Format:       %s, %s" % (format_name, masse["groesse"]))
    print("  Seiten:       %d" % seiten)
    print("  Kapitel:      %d" % gebaut)
    print("  Bilder:       %d, %.1f MB als JPEG (%d px, q%d)"
          % (len(bilddaten), bildgroesse, breite, qualitaet))
    print("  Datei:        %.1f MB" % groesse)
    if fehlend:
        print("  Fehlt:        %s" % ", ".join(fehlend))
    return 0 if not fehlend else 1


def main():
    p = argparse.ArgumentParser(description="Baut das Buch als PDF.")
    p.add_argument("--nur", type=int, default=0,
                   help="nur die ersten N Kapitel, fuer einen schnellen Blick")
    p.add_argument("--format", default="a4", choices=sorted(FORMATE),
                   help="Seitenformat (Standard a4)")
    p.add_argument("--druck", action="store_true",
                   help="Bundsteg innen und Kapitelanfang immer rechts")
    p.add_argument("--breite", type=int, default=1086,
                   help="Bildbreite in Pixeln (Standard 1086, also die Quelle)")
    p.add_argument("--qualitaet", type=int, default=85,
                   help="JPEG-Qualitaet (Standard 85)")
    p.add_argument("--ziel", default=bb.pfad(*ZIEL))
    a = p.parse_args()
    return bau(a.nur, a.format, a.druck, a.breite, a.qualitaet, a.ziel)


if __name__ == "__main__":
    sys.exit(main())
