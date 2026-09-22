#!/usr/bin/env python3
"""Baut buch/kenia-vorgelesen.epub aus denselben Quellen wie buch_bauen.py.

Unterschiede zum HTML-Buch, und warum:

* Jedes Kapitel wird eine eigene XHTML-Datei. Reader blaettern damit sauber,
  und ein Fehler in einem Kapitel reisst nicht das ganze Buch mit.
* Die Kapitel sind gueltiges HTML5, aber kein gueltiges XML: <img> steht ohne
  Schraegstrich, und in drei alt-Texten steckt ein <em>-Tag, das in XML in einem
  Attribut nicht erlaubt ist. EPUB verlangt XHTML, deshalb laeuft der Block hier
  durch einen Parser und wird neu geschrieben. Inhaltlich aendert sich nichts.
* Die Illustrationen liegen als PNG mit zusammen rund 300 MB im Repo. Als EPUB
  waere das unlesbar, also werden sie beim Bauen zu JPEG gerechnet. Die
  Quelldateien bleiben unberuehrt.

Aufruf:
    python3 scripts/epub_bauen.py
    python3 scripts/epub_bauen.py --nur 5        # kleines Testbuch
    python3 scripts/epub_bauen.py --breite 900 --qualitaet 85

Geprueft wird mit epubcheck, nicht nach Augenmass:
    java -jar epubcheck.jar buch/kenia-vorgelesen.epub
"""

import argparse
import datetime
import glob
import html
import io
import os
import re
import sys
import uuid
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import buch_bauen as bb
from PIL import Image

WURZEL = bb.WURZEL
ZIEL = bb.pfad("buch", "kenia-vorgelesen.epub")

# Feste Kennung des Buches. Bleibt ueber alle Neubauten gleich, damit ein
# Reader eine neue Fassung als dasselbe Buch erkennt und die Lesezeichen
# behaelt, statt eine zweite Kopie anzulegen.
BUCH_ID = "urn:uuid:" + str(
    uuid.uuid5(uuid.NAMESPACE_URL, "https://github.com/tobi840/book-project-kenia")
)

CSS = """
@charset "utf-8";

html { font-size: 100%; }
body {
  margin: 0 5%;
  color: #1f1c18;
  background: #fbf9f4;
  font-family: "Iowan Old Style", Palatino, Georgia, serif;
  line-height: 1.6;
  widows: 2;
  orphans: 2;
}
p { margin: 0 0 .75em; text-align: justify; hyphens: auto; -epub-hyphens: auto; }

/* Cover: ein Bild, sonst nichts */
body.cover { margin: 0; text-align: center; }
body.cover img { max-width: 100%; max-height: 100%; }

/* Titelseite */
.titelseite { text-align: center; margin-top: 25%; }
.titelseite h1 { font-size: 2.2em; margin: 0 0 .2em; font-weight: normal; }
.titelseite .untertitel { font-style: italic; color: #6b6355; margin: 0 0 2em; }
.titelseite .autor { letter-spacing: .1em; text-transform: uppercase;
                     font-size: .9em; }
.titelseite .reise { color: #6b6355; font-size: .85em; margin-top: 3em; }

/* Inhalt */
nav ol { list-style: none; margin: 0; padding: 0 0 0 .5em; }
nav > ol > li { margin: 1.2em 0 0; font-weight: bold; }
nav ol ol { font-weight: normal; padding-left: 1em; }
nav ol ol li { margin: .15em 0; font-size: .95em; }
nav a { color: #1f1c18; text-decoration: none; }

/* Abschnittseinleitung */
.abschnitt-nr { color: #8a3b1e; letter-spacing: .12em; text-transform: uppercase;
                font-size: .75em; margin: 0 0 .3em; text-align: left; }
.einleitung-kopf { border-bottom: 2px solid #8a3b1e; padding-bottom: .8em;
                   margin-bottom: 1.5em; }
.einleitung-kopf h1 { font-size: 1.9em; margin: 0; line-height: 1.15;
                      font-weight: normal; }
.einleitung-kopf .untertitel { color: #6b6355; font-style: italic;
                               margin: .3em 0 0; text-align: left; }

/* Kapitel */
.kapitel-kopf { margin-bottom: 1.2em; }
.lebensraum { color: #8a3b1e; letter-spacing: .12em; text-transform: uppercase;
              font-size: .7em; margin: 0 0 .3em; text-align: left; }
.kapitel-kopf h1 { font-size: 1.7em; margin: 0; line-height: 1.2;
                   font-weight: normal; }
.lateinisch { margin: .2em 0 0; color: #6b6355; text-align: left; }
.namen { margin: .4em 0 0; font-size: .85em; color: #6b6355; text-align: left; }

figure.illustration { margin: 1.2em 0; padding: 0; page-break-inside: avoid;
                      break-inside: avoid; text-align: center; }
figure.illustration img { max-width: 100%; }
figure.illustration figcaption { font-size: .8em; color: #6b6355;
                                 font-style: italic; margin-top: .4em;
                                 text-align: left; }

h2 { font-size: .95em; letter-spacing: .06em; text-transform: uppercase;
     color: #8a3b1e; margin: 1.8em 0 .5em; font-weight: bold;
     page-break-after: avoid; break-after: avoid; }
/* Die Ueberschrift "Geschichte" steht nur fuer Vorleseprogramme in der Datei.
   display:none wuerde sie auch denen nehmen, deshalb wird sie weggeschoben. */
.geschichte > h2 { position: absolute; left: -9999px; height: 1px;
                   width: 1px; overflow: hidden; }
.menschen-kultur, .vor-der-linse { border-left: 3px solid #ddd5c6;
                                   padding-left: 1em; margin-top: 1.5em; }
"""


def xhtml(titel, koerper, koerperklasse=None, epub_ns=False):
    ns = ' xmlns:epub="http://www.idpf.org/2007/ops"' if epub_ns else ""
    kl = ' class="%s"' % koerperklasse if koerperklasse else ""
    return (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<!DOCTYPE html>\n'
        '<html xmlns="http://www.w3.org/1999/xhtml"%s xml:lang="de" lang="de">\n'
        '<head>\n'
        '<meta charset="utf-8"/>\n'
        '<title>%s</title>\n'
        '<link rel="stylesheet" type="text/css" href="stil.css"/>\n'
        '</head>\n'
        '<body%s>\n%s\n</body>\n</html>\n'
        % (ns, html.escape(titel), kl, koerper)
    )


LEERE_TAGS = frozenset(
    ["area", "base", "br", "col", "embed", "hr", "img", "input", "link",
     "meta", "param", "source", "track", "wbr"]
)


def attr_maskieren(wert):
    """Attributwert XML-sicher machen.

    Tags im Wert werden gestrichen. In drei alt-Texten steht ein <em>-Tag,
    und XML verbietet ein < im Attribut. Maskiert saehe der Vorleser die
    spitzen Klammern, gestrichen liest er den Satz.
    """
    if wert is None:
        return ""
    wert = re.sub(r"</?[A-Za-z][^>]*>", "", wert)
    return (
        wert.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def text_maskieren(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class XhtmlSchreiber(HTMLParser):
    """Liest den HTML-Block und schreibt ihn als wohlgeformtes XHTML neu.

    Kein Regex auf dem Markup: leere Elemente werden geschlossen, Text und
    Attribute maskiert, Kommentare fallen weg (in 009 und 014 stehen dort
    Notizen zum gestrichenen Querverweis-Durchlauf). Falsch geschachtelte
    Tags werfen, statt still ein kaputtes Buch zu bauen.
    """

    def __init__(self, bildnamen):
        HTMLParser.__init__(self, convert_charrefs=True)
        self.bildnamen = bildnamen
        self.teile = []
        self.offen = []

    def bildpfad(self, quelle):
        name = os.path.basename(quelle or "")
        neu = self.bildnamen.get(name)
        if neu is None:
            raise ValueError("Bild nicht vorbereitet: %s" % quelle)
        return "bilder/" + neu

    def tag_schreiben(self, tag, attrs, leer):
        stuecke = ["<" + tag]
        for name, wert in attrs:
            if tag == "img" and name == "src":
                wert = self.bildpfad(wert)
            stuecke.append(' %s="%s"' % (name, attr_maskieren(wert)))
        stuecke.append("/>" if leer else ">")
        return "".join(stuecke)

    def handle_starttag(self, tag, attrs):
        leer = tag in LEERE_TAGS
        self.teile.append(self.tag_schreiben(tag, attrs, leer))
        if not leer:
            self.offen.append(tag)

    def handle_startendtag(self, tag, attrs):
        self.teile.append(self.tag_schreiben(tag, attrs, True))

    def handle_endtag(self, tag):
        if tag in LEERE_TAGS:
            return
        if not self.offen or self.offen[-1] != tag:
            raise ValueError(
                "Tag nicht sauber geschachtelt: </%s>, offen war %s"
                % (tag, self.offen[-1] if self.offen else "nichts")
            )
        self.offen.pop()
        self.teile.append("</%s>" % tag)

    def handle_data(self, daten):
        self.teile.append(text_maskieren(daten))

    def ergebnis(self):
        if self.offen:
            raise ValueError("Tag nicht geschlossen: <%s>" % self.offen[-1])
        return "".join(self.teile)


def nach_xhtml(block, bildnamen):
    """Macht aus dem article-Block gueltiges XHTML."""
    schreiber = XhtmlSchreiber(bildnamen)
    schreiber.feed(block)
    schreiber.close()
    return schreiber.ergebnis()


def bilder_umrechnen(quellen, breite, qualitaet):
    """PNG zu JPEG. Gibt {Quelldateiname: Name im EPUB} und die Bytes zurueck."""
    namen, daten = {}, {}
    for pfad_quelle in quellen:
        name = os.path.basename(pfad_quelle)
        ziel = re.sub(r"[^A-Za-z0-9_.-]", "_", os.path.splitext(name)[0]) + ".jpg"
        bild = Image.open(pfad_quelle).convert("RGB")
        if bild.width > breite:
            hoehe = round(bild.height * breite / bild.width)
            bild = bild.resize((breite, hoehe), Image.LANCZOS)
        puffer = io.BytesIO()
        bild.save(puffer, "JPEG", quality=qualitaet, optimize=True, progressive=True)
        namen[name] = ziel
        daten[ziel] = puffer.getvalue()
    return namen, daten


def bau(nur=0, breite=1000, qualitaet=80):
    tsv = bb.lies_tsv()
    nach_lebensraum = {}
    for nr, name, lebensraum in tsv:
        nach_lebensraum.setdefault(lebensraum, []).append((nr, name))

    unbekannt = set(nach_lebensraum) - {a[0] for a in bb.ABSCHNITTE}
    if unbekannt:
        sys.exit("Lebensraum ohne Abschnitt: %s" % ", ".join(sorted(unbekannt)))

    # Welche Kapitel kommen ins Buch
    plan = []          # [(abschnitt, [(nr, name, datei), ...])]
    gezaehlt = 0
    fehlend = []
    for lebensraum, anr, titel in bb.ABSCHNITTE:
        kapitel = []
        for nr, name in nach_lebensraum.get(lebensraum, []):
            if nur and gezaehlt >= nur:
                break
            datei = bb.kapiteldatei(nr)
            if not datei:
                fehlend.append("Kapitel %s" % nr)
                continue
            kapitel.append((nr, name, datei))
            gezaehlt += 1
        plan.append((lebensraum, anr, titel, kapitel))

    # Bilder sammeln und umrechnen
    quellen = [bb.pfad("buch", "cover.png")]
    for _, _, _, kapitel in plan:
        for nr, name, datei in kapitel:
            text = open(datei, encoding="utf-8").read()
            for src in re.findall(r'<img[^>]*src="([^"]+)"', text):
                quellen.append(os.path.normpath(os.path.join(os.path.dirname(datei), src)))
    quellen = [q for q in quellen if os.path.exists(q)]
    print("Bilder werden umgerechnet: %d Stueck" % len(quellen))
    bildnamen, bilddaten = bilder_umrechnen(quellen, breite, qualitaet)

    dateien = {}       # Name im EPUB -> Bytes oder Text
    spine = []         # [(id, datei)]
    inhalt = []        # fuer nav und ncx: [(ebene, titel, ziel)]

    dateien["stil.css"] = CSS

    # Cover
    cover_da = "cover.png" in bildnamen
    if cover_da:
        dateien["cover.xhtml"] = xhtml(
            "Cover",
            '<div><img src="bilder/%s" alt="%s. %s. %s"/></div>'
            % (bildnamen["cover.png"], html.escape(bb.TITEL),
               html.escape(bb.UNTERTITEL), html.escape(bb.AUTOR)),
            koerperklasse="cover",
        )
        spine.append(("cover", "cover.xhtml"))

    # Titelseite
    dateien["titel.xhtml"] = xhtml(
        bb.TITEL,
        '<div class="titelseite">\n'
        '<h1>%s</h1>\n<p class="untertitel">%s</p>\n'
        '<p class="autor">%s</p>\n'
        '<p class="reise">Kenia, 24. September bis 12. Oktober 2026</p>\n</div>'
        % (html.escape(bb.TITEL), html.escape(bb.UNTERTITEL), html.escape(bb.AUTOR)),
    )
    spine.append(("titel", "titel.xhtml"))
    spine.append(("nav", "nav.xhtml"))

    # Allgemeine Einleitung
    quelle = bb.pfad("einleitungen", "00-einleitung.html")
    if os.path.exists(quelle):
        block = nach_xhtml(bb.artikel(open(quelle, encoding="utf-8").read()), bildnamen)
        dateien["einleitung.xhtml"] = xhtml("Einleitung", block)
        spine.append(("einleitung", "einleitung.xhtml"))
        inhalt.append((1, "Einleitung", "einleitung.xhtml"))
    else:
        fehlend.append("Einleitung 00")

    # Abschnitte und Kapitel
    for lebensraum, anr, titel, kapitel in plan:
        if not kapitel:
            continue
        quelle = sorted(glob.glob(bb.pfad("einleitungen", anr + "-*.html")))
        ziel = "abschnitt-%s.xhtml" % anr
        if quelle:
            block = nach_xhtml(
                bb.artikel(open(quelle[0], encoding="utf-8").read()), bildnamen
            )
            dateien[ziel] = xhtml(titel, block)
            spine.append(("abschnitt%s" % anr, ziel))
            inhalt.append((1, titel, ziel))
        else:
            fehlend.append("Einleitung %s" % anr)
            inhalt.append((1, titel, "k%s.xhtml" % kapitel[0][0]))

        for nr, name, datei in kapitel:
            block = nach_xhtml(
                bb.artikel(open(datei, encoding="utf-8").read()), bildnamen
            )
            ziel = "k%s.xhtml" % nr
            dateien[ziel] = xhtml("%s. %s" % (nr.lstrip("0"), name), block)
            spine.append(("k%s" % nr, ziel))
            inhalt.append((2, "%s  %s" % (nr.lstrip("0"), name), ziel))

    dateien["nav.xhtml"] = nav_bauen(inhalt, cover_da)
    dateien["toc.ncx"] = ncx_bauen(inhalt)
    dateien["content.opf"] = opf_bauen(spine, dateien, bilddaten, cover_da,
                                       bildnamen.get("cover.png"))

    # Pruefen, bevor irgendetwas gepackt wird
    kaputt = []
    for name, text in sorted(dateien.items()):
        if not name.endswith((".xhtml", ".opf", ".ncx")):
            continue
        try:
            ET.fromstring(text.encode("utf-8"))
        except ET.ParseError as e:
            kaputt.append((name, str(e)))
    if kaputt:
        for name, fehler in kaputt:
            print("  KAPUTT %s: %s" % (name, fehler))
        sys.exit("%d Datei(en) sind kein gueltiges XML. Nichts geschrieben." % len(kaputt))

    schreiben(dateien, bilddaten)

    groesse = os.path.getsize(ZIEL)
    print("%s geschrieben" % os.path.relpath(ZIEL, WURZEL))
    print("  Kapitel:      %d" % sum(len(k) for _, _, _, k in plan))
    print("  Dokumente:    %d" % len(spine))
    print("  Bilder:       %d, %.1f MB als JPEG (%d px, q%d)"
          % (len(bilddaten), sum(len(b) for b in bilddaten.values()) / 1e6,
             breite, qualitaet))
    print("  Datei:        %.1f MB" % (groesse / 1e6))
    if fehlend:
        print("  Fehlt:        %s" % ", ".join(fehlend))
    return 0


def nav_bauen(inhalt, cover_da):
    zeilen = ['<nav epub:type="toc" id="toc"><h1>Inhalt</h1>', "<ol>"]
    offen = False   # ein Eintrag der ersten Ebene ist offen
    liste = False   # darin steht schon eine Unterliste
    for ebene, titel, ziel in inhalt:
        if ebene == 1:
            if offen:
                zeilen.append("</ol></li>" if liste else "</li>")
            zeilen.append('<li><a href="%s">%s</a>' % (ziel, html.escape(titel)))
            offen, liste = True, False
        else:
            # Die Unterliste wird erst beim ersten Kind geoeffnet. Die
            # Einleitung hat keine Kinder, und ein leeres <ol> ist in EPUB
            # ein Fehler, kein Schoenheitsfehler.
            if offen and not liste:
                zeilen.append("<ol>")
                liste = True
            zeilen.append('<li><a href="%s">%s</a></li>' % (ziel, html.escape(titel)))
    if offen:
        zeilen.append("</ol></li>" if liste else "</li>")
    zeilen.append("</ol></nav>")

    marken = ['<nav epub:type="landmarks" class="versteckt"><h2>Wegmarken</h2><ol>']
    if cover_da:
        marken.append('<li><a epub:type="cover" href="cover.xhtml">Cover</a></li>')
    marken.append('<li><a epub:type="toc" href="nav.xhtml">Inhalt</a></li>')
    erstes = inhalt[0][2] if inhalt else "titel.xhtml"
    marken.append('<li><a epub:type="bodymatter" href="%s">Anfang</a></li>' % erstes)
    marken.append("</ol></nav>")

    return xhtml("Inhalt", "\n".join(zeilen) + "\n" + "\n".join(marken), epub_ns=True)


def ncx_bauen(inhalt):
    """Alte Inhaltsangabe. Braucht Kindle, EPUB 3 allein genuegt ihm nicht."""
    punkte = []
    zaehler = 0
    i = 0
    while i < len(inhalt):
        ebene, titel, ziel = inhalt[i]
        zaehler += 1
        kinder = []
        j = i + 1
        while j < len(inhalt) and inhalt[j][0] == 2:
            zaehler += 1
            kinder.append(
                '<navPoint id="n%d" playOrder="%d"><navLabel><text>%s</text>'
                '</navLabel><content src="%s"/></navPoint>'
                % (zaehler, zaehler, html.escape(inhalt[j][1]), inhalt[j][2])
            )
            j += 1
        punkte.append(
            '<navPoint id="n%d" playOrder="%d"><navLabel><text>%s</text></navLabel>'
            '<content src="%s"/>%s</navPoint>'
            % (zaehler - len(kinder), zaehler - len(kinder), html.escape(titel),
               ziel, "".join(kinder))
        )
        i = j
    return (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1" '
        'xml:lang="de">\n'
        '<head><meta name="dtb:uid" content="%s"/>'
        '<meta name="dtb:depth" content="2"/>'
        '<meta name="dtb:totalPageCount" content="0"/>'
        '<meta name="dtb:maxPageNumber" content="0"/></head>\n'
        '<docTitle><text>%s</text></docTitle>\n'
        '<navMap>%s</navMap>\n</ncx>\n'
        % (BUCH_ID, html.escape(bb.TITEL), "\n".join(punkte))
    )


def opf_bauen(spine, dateien, bilddaten, cover_da, cover_name):
    jetzt = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    m = [
        '<dc:identifier id="buch-id">%s</dc:identifier>' % BUCH_ID,
        '<dc:title id="t1">%s</dc:title>' % html.escape(bb.TITEL),
        '<meta refines="#t1" property="title-type">main</meta>',
        '<dc:title id="t2">%s</dc:title>' % html.escape(bb.UNTERTITEL),
        '<meta refines="#t2" property="title-type">subtitle</meta>',
        '<dc:creator id="autor">%s</dc:creator>' % html.escape(bb.AUTOR),
        '<meta refines="#autor" property="role" scheme="marc:relators">aut</meta>',
        "<dc:language>de</dc:language>",
        '<meta property="dcterms:modified">%s</meta>' % jetzt,
    ]
    if cover_da:
        m.append('<meta name="cover" content="cover-bild"/>')

    eintraege = [
        '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" '
        'properties="nav"/>',
        '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
        '<item id="css" href="stil.css" media-type="text/css"/>',
    ]
    for kennung, datei in spine:
        if datei == "nav.xhtml":
            continue
        eintraege.append(
            '<item id="%s" href="%s" media-type="application/xhtml+xml"/>'
            % (kennung, datei)
        )
    for name in sorted(bilddaten):
        kennung = "cover-bild" if name == cover_name else "b-" + name[:-4]
        zusatz = ' properties="cover-image"' if name == cover_name else ""
        eintraege.append(
            '<item id="%s" href="bilder/%s" media-type="image/jpeg"%s/>'
            % (kennung, name, zusatz)
        )

    ruecken = []
    for kennung, datei in spine:
        ruecken.append('<itemref idref="%s"/>' % kennung)

    return (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" '
        'unique-identifier="buch-id" xml:lang="de">\n'
        '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">\n%s\n</metadata>\n'
        '<manifest>\n%s\n</manifest>\n'
        '<spine toc="ncx">\n%s\n</spine>\n</package>\n'
        % ("\n".join(m), "\n".join(eintraege), "\n".join(ruecken))
    )


def schreiben(dateien, bilddaten):
    os.makedirs(os.path.dirname(ZIEL), exist_ok=True)
    with zipfile.ZipFile(ZIEL, "w") as z:
        # Die Datei mimetype muss die erste im Archiv sein und ungepackt.
        z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip",
                   compress_type=zipfile.ZIP_STORED)
        z.writestr(
            "META-INF/container.xml",
            '<?xml version="1.0" encoding="utf-8"?>\n'
            '<container version="1.0" '
            'xmlns="urn:oasis:names:tc:opendocument:xmlns:container">\n'
            '<rootfiles><rootfile full-path="OEBPS/content.opf" '
            'media-type="application/oebps-package+xml"/></rootfiles>\n'
            '</container>\n',
            compress_type=zipfile.ZIP_DEFLATED,
        )
        for name, text in sorted(dateien.items()):
            z.writestr("OEBPS/" + name, text.encode("utf-8"),
                       compress_type=zipfile.ZIP_DEFLATED)
        for name, roh in sorted(bilddaten.items()):
            z.writestr("OEBPS/bilder/" + name, roh,
                       compress_type=zipfile.ZIP_STORED)


def main():
    p = argparse.ArgumentParser(description="Baut das EPUB.")
    p.add_argument("--nur", type=int, default=0,
                   help="nur die ersten N Kapitel, fuer einen schnellen Test")
    p.add_argument("--breite", type=int, default=1000,
                   help="maximale Bildbreite in Pixeln (Standard 1000)")
    p.add_argument("--qualitaet", type=int, default=80,
                   help="JPEG-Qualitaet (Standard 80)")
    a = p.parse_args()
    return bau(nur=a.nur, breite=a.breite, qualitaet=a.qualitaet)


if __name__ == "__main__":
    sys.exit(main())
