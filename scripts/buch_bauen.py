#!/usr/bin/env python3
"""Baut buch/buch.html aus Cover, Inhaltsverzeichnis, Einleitungen und Kapiteln.

Reihenfolge: die fuenf Lebensraeume in der Reihenfolge der Reise, innerhalb
eines Abschnitts nach Kapitelnummer. Die Nummer ist eine Kennung, keine
Seitenzahl: 081 bis 100 sind nachtraeglich dazugekommen und verteilen sich
auf alle fuenf Abschnitte.

Aufruf: python3 scripts/buch_bauen.py
"""

import glob
import html
import os
import re
import sys

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Lebensraum in chapters.tsv -> (Nummer des Abschnitts, Titel im Buch)
ABSCHNITTE = [
    ("Nairobi", "01", "Nairobi und Umgebung"),
    ("Rift Valley", "02", "Rift Valley"),
    ("Laikipia / Mt. Kenya", "03", "Laikipia und Mount Kenya"),
    ("Küste Mombasa", "04", "Die Küste bei Mombasa"),
    ("Tsavo / Amboseli", "05", "Tsavo und Amboseli"),
]

TITEL = "Kenia, vorgelesen"
UNTERTITEL = "Hundert Arten zwischen Riff und Gipfel"


def pfad(*teile):
    return os.path.join(WURZEL, *teile)


def kopfdaten(text):
    """Liest das Frontmatter aus dem HTML-Kommentar am Dateianfang."""
    m = re.match(r"\s*<!--(.*?)-->", text, re.S)
    daten = {}
    if not m:
        return daten
    for zeile in m.group(1).strip().split("\n"):
        if ":" in zeile:
            k, _, v = zeile.partition(":")
            daten[k.strip()] = v.strip()
    return daten


def artikel(text):
    """Schneidet den article-Block heraus, ohne Frontmatter."""
    m = re.search(r"<article\b.*?</article>", text, re.S)
    if not m:
        raise ValueError("kein article-Block")
    return m.group(0)


def lies_tsv():
    zeilen = []
    with open(pfad("chapters.tsv"), encoding="utf-8") as f:
        for zeile in f:
            zeile = zeile.rstrip("\n")
            if not zeile.strip():
                continue
            teile = zeile.split("\t")
            zeilen.append((teile[0], teile[1], teile[2]))
    return zeilen


def kapiteldatei(nr):
    treffer = sorted(glob.glob(pfad("chapters", nr + "-*.html")))
    if not treffer:
        return None
    return treffer[0]


CSS = """
:root {
  --papier: #fbf9f4;
  --tinte: #1f1c18;
  --grau: #6b6355;
  --linie: #ddd5c6;
  --akzent: #8a3b1e;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--papier);
  color: var(--tinte);
  font-family: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
  font-size: 19px;
  line-height: 1.65;
}
.seite { max-width: 40rem; margin: 0 auto; padding: 0 1rem; }

/* Cover */
.nur-vorlesen { position: absolute; width: 1px; height: 1px; overflow: hidden;
  clip: rect(0 0 0 0); white-space: nowrap; }
.cover { min-height: 100vh; display: flex; flex-direction: column;
         align-items: center; justify-content: center; text-align: center;
         padding: 3rem 1rem; }
.cover img { max-width: min(34rem, 92vw); width: 100%; height: auto;
             border-radius: 2px; box-shadow: 0 2px 30px rgba(0,0,0,.18); }
.cover h1 { font-size: clamp(2.2rem, 7vw, 3.4rem); margin: 2rem 0 .3rem;
            letter-spacing: .01em; font-weight: 600; }
.cover p.untertitel { color: var(--grau); font-size: 1.1rem; margin: 0 0 1.5rem; }
.cover p.reise { color: var(--grau); font-size: .95rem; letter-spacing: .08em;
                 text-transform: uppercase; }

/* Inhaltsverzeichnis */
.inhalt h2 { font-size: 1.9rem; margin: 3rem 0 1.5rem; }
.inhalt h3 { font-size: 1.15rem; margin: 2.2rem 0 .2rem; color: var(--akzent); }
.inhalt h3 span { color: var(--grau); font-weight: 400; font-size: .85rem;
                  display: block; letter-spacing: .06em; text-transform: uppercase; }
.inhalt ol { list-style: none; margin: .6rem 0 0; padding: 0;
             columns: 2; column-gap: 2rem; }
.inhalt li { margin: 0 0 .3rem; break-inside: avoid; font-size: .95rem; }
.inhalt a { color: var(--tinte); text-decoration: none;
            border-bottom: 1px solid var(--linie); }
.inhalt a:hover { border-bottom-color: var(--akzent); color: var(--akzent); }
.inhalt .nr { color: var(--grau); font-variant-numeric: tabular-nums;
              margin-right: .45rem; font-size: .85rem; }
@media (max-width: 34rem) { .inhalt ol { columns: 1; } }

/* Abschnittstrenner und Einleitungen */
.einleitung { padding: 3rem 0 2rem; }
.einleitung-kopf { margin-bottom: 2rem; border-bottom: 2px solid var(--akzent);
                   padding-bottom: 1rem; }
.abschnitt-nr { color: var(--akzent); letter-spacing: .12em;
                text-transform: uppercase; font-size: .8rem; margin: 0 0 .4rem; }
.einleitung-kopf h1 { font-size: 2.3rem; margin: 0; line-height: 1.15; }
.einleitung-kopf .untertitel { color: var(--grau); margin: .4rem 0 0;
                               font-style: italic; }

/* Kapitel */
.kapitel { padding: 2.5rem 0 1rem; }
.kapitel-kopf { margin-bottom: 1.5rem; }
.lebensraum { color: var(--akzent); letter-spacing: .12em;
              text-transform: uppercase; font-size: .75rem; margin: 0 0 .4rem; }
.kapitel-kopf h1 { font-size: 2rem; margin: 0; line-height: 1.2; }
.lateinisch { margin: .2rem 0 0; color: var(--grau); }
.namen { margin: .5rem 0 0; font-size: .92rem; color: var(--grau); }
.illustration { margin: 1.6rem 0; }
.illustration img { width: 100%; height: auto; border-radius: 2px;
                    display: block; }
.illustration figcaption { font-size: .82rem; color: var(--grau);
                           margin-top: .5rem; font-style: italic; }
.kapitel h2 { font-size: 1.1rem; letter-spacing: .06em;
              text-transform: uppercase; color: var(--akzent);
              margin: 2.2rem 0 .6rem; }
.geschichte h2 { position: absolute; left: -9999px; }
.querverweis { color: var(--grau); }
.menschen-kultur, .vor-der-linse { border-left: 3px solid var(--linie);
                                   padding-left: 1.1rem; }
.vor-der-linse p { margin: .4rem 0; }

.zurueck { display: block; margin: 2rem 0 0; font-size: .8rem;
           letter-spacing: .08em; text-transform: uppercase;
           color: var(--grau); text-decoration: none; }
.zurueck:hover { color: var(--akzent); }
hr.trenner { border: 0; border-top: 1px solid var(--linie); margin: 3rem 0 0; }

@media print {
  body { font-size: 11pt; background: #fff; }
  .seite { max-width: none; }
  .cover, .inhalt, .einleitung, .kapitel { break-after: page; }
  .zurueck, hr.trenner { display: none; }
  a { color: inherit; text-decoration: none; }
}
"""


def bau():
    tsv = lies_tsv()
    nach_lebensraum = {}
    for nr, name, lebensraum in tsv:
        nach_lebensraum.setdefault(lebensraum, []).append((nr, name))

    unbekannt = set(nach_lebensraum) - {a[0] for a in ABSCHNITTE}
    if unbekannt:
        sys.exit("Lebensraum ohne Abschnitt: %s" % ", ".join(sorted(unbekannt)))

    teile = []
    teile.append("<!DOCTYPE html>")
    teile.append('<html lang="de">')
    teile.append("<head>")
    teile.append('<meta charset="utf-8">')
    teile.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
    teile.append("<title>%s</title>" % html.escape(TITEL))
    teile.append("<style>%s</style>" % CSS)
    teile.append("</head>")
    teile.append("<body>")

    # Cover
    cover = pfad("buch", "cover.png")
    teile.append('<div class="cover" id="cover">')
    if os.path.exists(cover):
        # Titel und Untertitel stehen seit dem 22.09.2026 im Bild selbst,
        # gesetzt von cover_titel.py. Hier stuenden sie sonst doppelt. Die
        # Ueberschrift bleibt fuer Vorleseprogramme und EPUB erhalten, aber
        # unsichtbar.
        teile.append('<img src="cover.png" alt="%s. %s">'
                     % (html.escape(TITEL), html.escape(UNTERTITEL)))
        teile.append('<h1 class="nur-vorlesen">%s</h1>' % html.escape(TITEL))
    else:
        teile.append("<h1>%s</h1>" % html.escape(TITEL))
        teile.append('<p class="untertitel">%s</p>' % html.escape(UNTERTITEL))
    teile.append('<p class="reise">Kenia, 24. September bis 12. Oktober 2026</p>')
    teile.append("</div>")

    # Inhaltsverzeichnis
    teile.append('<div class="seite inhalt" id="inhalt">')
    teile.append("<h2>Inhalt</h2>")
    teile.append('<p><a href="#einleitung">Einleitung</a></p>')
    for lebensraum, anr, titel in ABSCHNITTE:
        kapitel = nach_lebensraum.get(lebensraum, [])
        teile.append(
            '<h3><span>Abschnitt %s, %d Kapitel</span>'
            '<a href="#abschnitt-%s">%s</a></h3>'
            % (anr.lstrip("0"), len(kapitel), anr, html.escape(titel))
        )
        teile.append("<ol>")
        for nr, name in kapitel:
            teile.append(
                '<li><a href="#k%s"><span class="nr">%s</span>%s</a></li>'
                % (nr, nr, html.escape(name))
            )
        teile.append("</ol>")
    teile.append("</div>")

    # Allgemeine Einleitung
    quelle = pfad("einleitungen", "00-einleitung.html")
    if os.path.exists(quelle):
        text = open(quelle, encoding="utf-8").read()
        block = artikel(text).replace('<article ', '<article id="einleitung" ', 1)
        teile.append('<div class="seite">%s'
                     '<a class="zurueck" href="#inhalt">Zum Inhalt</a>'
                     '<hr class="trenner"></div>' % block)
    else:
        print("Hinweis: %s fehlt" % quelle)

    gebaut = 0
    fehlend = []
    for lebensraum, anr, titel in ABSCHNITTE:
        quelle = sorted(glob.glob(pfad("einleitungen", anr + "-*.html")))
        if quelle:
            text = open(quelle[0], encoding="utf-8").read()
            block = artikel(text).replace(
                "<article ", '<article id="abschnitt-%s" ' % anr, 1
            )
            teile.append('<div class="seite">%s'
                         '<a class="zurueck" href="#inhalt">Zum Inhalt</a>'
                         '<hr class="trenner"></div>' % block)
        else:
            fehlend.append("Einleitung %s" % anr)

        for nr, name in nach_lebensraum.get(lebensraum, []):
            datei = kapiteldatei(nr)
            if not datei:
                fehlend.append("Kapitel %s" % nr)
                continue
            text = open(datei, encoding="utf-8").read()
            block = artikel(text).replace("<article ", '<article id="k%s" ' % nr, 1)
            teile.append('<div class="seite">%s'
                         '<a class="zurueck" href="#inhalt">Zum Inhalt</a>'
                         '<hr class="trenner"></div>' % block)
            gebaut += 1

    teile.append("</body></html>")

    os.makedirs(pfad("buch"), exist_ok=True)
    ziel = pfad("buch", "buch.html")
    with open(ziel, "w", encoding="utf-8") as f:
        f.write("\n".join(teile))

    print("%s geschrieben" % os.path.relpath(ziel, WURZEL))
    print("  Kapitel:      %d von %d" % (gebaut, len(tsv)))
    print("  Abschnitte:   %d" % len(ABSCHNITTE))
    print("  Cover:        %s" % ("buch/cover.png" if os.path.exists(cover)
                                  else "fehlt, nur Typografie"))
    if fehlend:
        print("  Fehlt:        %s" % ", ".join(fehlend))
    return 0 if not fehlend else 1


if __name__ == "__main__":
    sys.exit(bau())
