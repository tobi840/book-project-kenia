#!/usr/bin/env python3
"""Deterministischer Regel-Check fuer ein Kapitel des Kenia-Vorlesebuchs.

Prueft alles, was sich zaehlen oder mit einer Wortliste erschlagen laesst:
Struktur, Laengen, Absaetze, Saetze, verbotene Zeichen und Woerter,
Lueckenmarker. Alles andere ist Sache der QS.

    python3 scripts/regel_check.py chapters/001-wuergefeige.html
    python3 scripts/regel_check.py chapters/001-wuergefeige.html --json
    python3 scripts/regel_check.py chapters/001-wuergefeige.html --research-duenn

Exit-Code 0 = keine Befunde der Schwere "rot", sonst 1.
"""

import argparse
import json
import re
import sys
from html.parser import HTMLParser

# ---------------------------------------------------------------- Konstanten

# Laengenzonen, gesenkt am 18.09.2026 (E18). Der Pilot hat gezeigt, dass jede
# zusaetzliche Behauptung eine zusaetzliche Fehlerquelle ist und dass die alte
# Untergrenze von 900 Woertern Texte ins Auffuellen treibt. Drori liegt bei
# 700 bis 900. Wir bleiben knapp darueber.
NORM_MIN, NORM_MAX = 800, 1300
GELB_MAX = 1600
WEICHE_UNTERGRENZE = 650
HARTE_UNTERGRENZE = 550

ABSATZ_MAX = 200
ERSTER_SATZ_MAX = 25          # unter 25 Woertern, also 24 ist ok
LETZTER_ABSATZ_MAX = 80       # unter 80 Woertern
SATZ_LANG = 40
ABSAETZE_MIN, ABSAETZE_MAX = 5, 9

MUK_MIN, MUK_MAX = 150, 250   # Menschen und Kultur
LINSE_MIN, LINSE_MAX = 100, 200

HALBGEVIERT = chr(0x2013)
GEVIERT = chr(0x2014)
MITTELPUNKT = chr(0xB7)
MARK_A = chr(1)
MARK_B = chr(2)

VERBOTENE_WOERTER = [
    "majestätisch", "faszinierend", "wunderschön", "ikonisch",
    "atemberaubend", "Wunder der Natur",
    # Zeitliche Zuspitzung. Zweimal in zwei Kapiteln als Fehler bestaetigt:
    # 007 ("und er geht den ganzen Tag", das Doc nennt Ruhe im Schatten ueber
    # Mittag) und 008 ("den ganzen Tag senkrecht springt", das Doc schreibt
    # "tagtaeglich" und nennt die hoechste Aktivitaet am fruehen Morgen).
    # Kein Research-Doc formuliert so. Steht es doch woertlich im Doc, ist der
    # Befund gelb und damit ein Verdacht, kein Urteil.
    "den ganzen Tag", "rund um die Uhr", "unermüdlich",
]

# Adjektivketten ab drei Gliedern. Deutsche Substantive sind gross, eine Reihe
# kleingeschriebener Woerter mit Adjektivendung, durch Komma getrennt, ist
# darum fast immer eine Adjektivkette. Styleguide Abschnitt 8.
# Praedikative Adjektive tragen im Deutschen gar keine Endung (flach, rau,
# dick). Eine Endungsliste filtert darum falsch. Was zaehlt, ist die Form:
# drei oder mehr kleingeschriebene Woerter, durch Komma und "und" verbunden.
# Substantive sind gross, also bleibt fast nur die Adjektivkette uebrig.
ADJ_VERBENDUNG = ("ieren", "ieren.", "eln", "ern")
ADJ_KETTE_RE = re.compile(
    r"\b([a-zäöüß]{3,}), ([a-zäöüß]{3,})(?:, ([a-zäöüß]{3,}))? (?:und|oder|sowie) ([a-zäöüß]{3,})\b")
# Verben und Adverbien, die in Aufzaehlungen stehen und keine Adjektivkette sind.
ADJ_STOPP = set("""
oder aber denn sonst dann damit weil wenn dass ohne gegen durch unter ueber
werden wurden haben hatten sind waren wird kann koennen muss muessen
""".split())

BRENNWEITEN = ["100 bis 400", "150 bis 600", "45 mm", "26 bis 60"]
PFLICHT_SEKTIONEN = ["geschichte", "menschen-kultur", "vor-der-linse"]

ABKUERZUNGEN = [
    "z. B.", "z.B.", "u. a.", "u.a.", "ca.", "bzw.", "Nr.", "S.",
    "Abb.", "vgl.", "ggf.", "Dr.", "Prof.", "St.", "engl.", "lat.", "dt.",
]

LUECKE_RE = re.compile(r"\[\[LÜCKE:.*?\]\]", re.S)
OFFEN_RE = re.compile(r"\[\[OFFEN:.*?\]\]", re.S)

# Heuristik fuer nicht kursiv gesetzte lateinische Artnamen.
# Gattung gross, Art klein und mindestens 5 Zeichen mit lateinischer Endung.
LAT_ENDUNGEN = (
    "us", "um", "ii", "ensis", "ata", "osa", "ica", "ana", "oides",
    "folia", "ior", "iana", "alis", "aris", "orum", "arum", "atum",
)
LAT_PAAR_RE = re.compile(r"\b([A-ZÄÖÜ][a-zäöüß]{3,})\s+([a-zäöüß]{5,})\b")
LAT_STOPP = set([
    "herum", "darum", "warum", "ringsum", "rundum", "wiederum", "darunter",
    "worum", "hinaus", "heraus", "voraus", "zugleich", "zuvor",
])
# Lateinische Wortpaare, die keine Artnamen sind und darum aufrecht stehen.
# Krankheitsbezeichnungen, Fachbegriffe, Werktitel.
KEIN_ARTNAME = set([
    "Malaria tropica", "Diabetes mellitus", "Delirium tremens",
])

# ------------------------------------------------------------------- Parsing

VOID = {"br", "img", "hr", "meta", "link", "input"}


class Node:
    def __init__(self, tag, attrs=None):
        self.tag = tag
        self.attrs = dict(attrs or [])
        self.kids = []

    def cls(self):
        return self.attrs.get("class") or ""

    def find_all(self, tag=None, cls=None):
        out = []
        for kid in self.kids:
            if isinstance(kid, Node):
                if (tag is None or kid.tag == tag) and (cls is None or cls in kid.cls().split()):
                    out.append(kid)
                out.extend(kid.find_all(tag, cls))
        return out

    def find(self, tag=None, cls=None):
        hits = self.find_all(tag, cls)
        return hits[0] if hits else None

    def text(self):
        return "".join(k if isinstance(k, str) else k.text() for k in self.kids)

    def text_ohne(self, *tags):
        """Text des Knotens, aber ohne den Inhalt der genannten Tags.

        Gebraucht fuer die Kursiv-Heuristik: was in <em> steht, ist bereits
        kursiv und darf nicht als Verdachtsfall gemeldet werden.
        """
        teile = []
        for k in self.kids:
            if isinstance(k, str):
                teile.append(k)
            elif k.tag in tags:
                teile.append(" ")
            else:
                teile.append(k.text_ohne(*tags))
        return "".join(teile)


class Builder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root")
        self.stack = [self.root]
        self.comments = []

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].kids.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].kids.append(Node(tag, attrs))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        self.stack[-1].kids.append(data)

    def handle_comment(self, data):
        self.comments.append(data)


# --------------------------------------------------------------- Textmetrik


def saubere_woerter(text):
    text = OFFEN_RE.sub(" ", LUECKE_RE.sub(" ", text))
    return [w for w in re.findall(r"\S+", text) if re.search(r"[0-9A-Za-zÀ-ÿ]", w)]


def wortzahl(text):
    return len(saubere_woerter(text))


def saetze(text):
    text = OFFEN_RE.sub(" ", LUECKE_RE.sub(" ", text)).strip()
    g = text
    for i, abk in enumerate(ABKUERZUNGEN):
        g = g.replace(abk, abk.replace(".", MARK_A + str(i) + MARK_A))
    g = re.sub(r"(\d)\.(\d)", r"\1" + MARK_B + r"\2", g)
    out = []
    for t in re.split(r"(?<=[.!?])\s+", g):
        for i, abk in enumerate(ABKUERZUNGEN):
            t = t.replace(MARK_A + str(i) + MARK_A, ".")
        t = t.replace(MARK_B, ".").strip()
        if t and re.search(r"[A-Za-zÀ-ÿ]", t):
            out.append(t)
    return out


def absaetze_von(section, ohne_klasse=None):
    out = []
    for p in section.find_all("p"):
        if ohne_klasse and ohne_klasse in p.cls().split():
            continue
        txt = " ".join(p.text().split())
        if txt:
            out.append(txt)
    return out


# ----------------------------------------------------------------- Pruefung


def pruefe(pfad, research_duenn=False):
    roh = open(pfad, encoding="utf-8").read()
    b = Builder()
    b.feed(roh)
    doc = b.root
    befunde = []

    def fund(schwere, regel, meldung, zitat=None):
        befunde.append({"schwere": schwere, "regel": regel, "meldung": meldung, "zitat": zitat})

    # --- Kopfkommentar ---------------------------------------------------
    meta = {}
    if b.comments:
        for zeile in b.comments[0].splitlines():
            if ":" in zeile:
                k, _, v = zeile.partition(":")
                meta[k.strip()] = v.strip()
    fehlend = [k for k in ["nr", "kategorie", "lebensraum", "trivialname", "lateinisch", "status"]
               if not meta.get(k)]
    if fehlend:
        fund("rot", "metadaten", "Metadaten fehlen oder sind leer: " + ", ".join(fehlend))

    # --- Struktur --------------------------------------------------------
    art = doc.find("article", "kapitel")
    if art is None:
        fund("rot", "struktur", 'Kein <article class="kapitel"> gefunden')
        art = doc

    kopf = art.find("header", "kapitel-kopf")
    if kopf is None:
        fund("rot", "struktur", 'Kopfblock <header class="kapitel-kopf"> fehlt')
    else:
        if kopf.find("h1") is None:
            fund("rot", "struktur", "Kopf ohne <h1> (Trivialname)")
        lr = kopf.find("p", "lebensraum")
        if lr is None:
            fund("rot", "struktur", "Kopf ohne Lebensraum-Zeile")
        elif lr.text().strip() != lr.text().strip().upper():
            fund("gelb", "struktur", "Lebensraum steht nicht in Versalien: " + lr.text().strip())
        lat = kopf.find("p", "lateinisch")
        if lat is None or lat.find("em") is None:
            fund("gelb", "struktur", "Lateinischer Name im Kopf fehlt oder ist nicht kursiv")

    sektionen = {}
    for name in PFLICHT_SEKTIONEN:
        s = art.find("section", name)
        if s is None:
            fund("rot", "struktur", 'Block <section class="' + name + '"> fehlt')
        else:
            sektionen[name] = s
            if s.find("h2") is None:
                fund("gelb", "struktur", 'Block "' + name + '" ohne <h2>')

    if art.find("figure", "illustration") is None:
        fund("gelb", "struktur", 'Platzhalter <figure class="illustration"> fehlt')

    volltext = art.text()

    # --- Gedankenstriche -------------------------------------------------
    for zeichen, name in ((HALBGEVIERT, "Halbgeviertstrich"), (GEVIERT, "Geviertstrich")):
        n = volltext.count(zeichen)
        if n:
            i = volltext.find(zeichen)
            fund("rot", "gedankenstrich", str(n) + " x " + name + " im Text",
                 " ".join(volltext[max(0, i - 60):i + 60].split()))

    # --- verbotene Woerter ----------------------------------------------
    klein = volltext.lower()
    for w in VERBOTENE_WOERTER:
        if w.lower() in klein:
            i = klein.find(w.lower())
            fund("gelb", "wortliste", 'Verbotenes Wort "' + w + '"',
                 " ".join(volltext[max(0, i - 60):i + 60].split()))

    ausrufe = volltext.count("!")
    if ausrufe > 2:
        fund("gelb", "ausrufezeichen", str(ausrufe) + " Ausrufezeichen, erlaubt sind hoechstens 2")

    # --- Adjektivketten --------------------------------------------------
    ketten = []
    for m in ADJ_KETTE_RE.finditer(volltext):
        glieder = [g for g in m.groups() if g]
        if any(g in ADJ_STOPP for g in glieder):
            continue
        if any(g.endswith(ADJ_VERBENDUNG) for g in glieder):
            continue
        ketten.append(m.group(0))
    for k in sorted(set(ketten)):
        fund("gelb", "adjektivkette",
             "Verdacht auf Dreierkette, Adjektive oder Verben, Styleguide Abschnitt 8", k)

    # --- Geschichte ------------------------------------------------------
    mass = {}
    gesch = sektionen.get("geschichte")
    if gesch is not None:
        texte = absaetze_von(gesch, ohne_klasse="querverweis")
        gesamt = " ".join(texte)
        wz = wortzahl(gesamt)
        mass["geschichte_woerter"] = wz
        mass["geschichte_absaetze"] = len(texte)

        if wz < HARTE_UNTERGRENZE:
            fund("rot", "laenge", "Geschichte hat " + str(wz) + " Woerter, harte Untergrenze ist "
                 + str(HARTE_UNTERGRENZE) + ". Das ist kein Kapitel mehr.")
        elif wz < WEICHE_UNTERGRENZE:
            fund("gelb" if research_duenn else "rot", "laenge",
                 "Geschichte hat " + str(wz) + " Woerter, unter der weichen Untergrenze "
                 + str(WEICHE_UNTERGRENZE)
                 + (". Research ist als duenn markiert, Fall fuer den Entscheidungsstapel."
                    if research_duenn else ". Research ist nicht als duenn markiert."))
        elif wz < NORM_MIN:
            fund("gelb", "laenge", "Geschichte hat " + str(wz) + " Woerter, die Norm beginnt bei "
                 + str(NORM_MIN)
                 + (". Research ist als duenn markiert, zulaessig." if research_duenn
                    else ". Research ist nicht als duenn markiert."))
        elif wz > GELB_MAX:
            fund("rot", "laenge", "Geschichte hat " + str(wz) + " Woerter, ueber der Obergrenze " + str(GELB_MAX))
        elif wz > NORM_MAX:
            fund("gelb", "laenge", "Geschichte hat " + str(wz) + " Woerter, die Norm endet bei " + str(NORM_MAX))

        if not (ABSAETZE_MIN <= len(texte) <= ABSAETZE_MAX):
            fund("gelb", "absaetze", "Geschichte hat " + str(len(texte)) + " Absaetze, vorgesehen sind "
                 + str(ABSAETZE_MIN) + " bis " + str(ABSAETZE_MAX))

        for idx, t in enumerate(texte, 1):
            n = wortzahl(t)
            if n > ABSATZ_MAX:
                fund("gelb", "absatzlaenge", "Absatz " + str(idx) + " hat " + str(n)
                     + " Woerter, erlaubt sind hoechstens " + str(ABSATZ_MAX),
                     " ".join(t.split()[:14]) + " ...")

        if texte:
            erste = saetze(texte[0])
            if erste:
                n = wortzahl(erste[0])
                mass["erster_satz_woerter"] = n
                if n >= ERSTER_SATZ_MAX:
                    fund("gelb", "erster-satz", "Erster Satz hat " + str(n)
                         + " Woerter, gefordert sind unter " + str(ERSTER_SATZ_MAX), erste[0])
            n_letzt = wortzahl(texte[-1])
            mass["letzter_absatz_woerter"] = n_letzt
            if n_letzt >= LETZTER_ABSATZ_MAX:
                fund("gelb", "letzter-absatz", "Letzter Absatz hat " + str(n_letzt)
                     + " Woerter, gefordert sind unter " + str(LETZTER_ABSATZ_MAX))

        lange = []
        for t in texte:
            for s in saetze(t):
                if wortzahl(s) > SATZ_LANG:
                    lange.append((wortzahl(s), s))
        mass["saetze_ueber_40"] = len(lange)
        for n, s in lange:
            fund("gelb", "satzlaenge", "Satz mit " + str(n) + " Woertern, Vorlesegrenze ist " + str(SATZ_LANG),
                 " ".join(s.split()[:16]) + " ...")

        fragen = gesamt.count("?")
        mass["rhetorische_fragen"] = fragen
        if fragen > 2:
            fund("gelb", "fragen", str(fragen) + " Fragezeichen in der Geschichte, erlaubt sind hoechstens 2")

        if gesch.find("p", "querverweis") is not None:
            fund("gelb", "querverweis",
                 'Querverweis im Entwurf. Querverweise setzt der eigene Durchlauf am Ende, '
                 'nicht der Schreiber.')

        # Lateinische Artnamen ausserhalb von <em>, Heuristik
        ausser_em = gesch.text_ohne("em")
        verdacht = []
        for m in LAT_PAAR_RE.finditer(ausser_em):
            art = m.group(2)
            if art in LAT_STOPP:
                continue
            if m.group(0) in KEIN_ARTNAME:
                continue
            if not art.endswith(LAT_ENDUNGEN):
                continue
            verdacht.append(m.group(0))
        mass["verdacht_kursiv"] = len(verdacht)
        for v in sorted(set(verdacht)):
            fund("gelb", "kursiv",
                 "Verdacht: lateinischer Artname nicht kursiv, bitte pruefen", v)

        lat_name = meta.get("lateinisch", "")
        if lat_name:
            n = gesamt.count(lat_name)
            mass["lateinisch_im_fliesstext"] = n
            if n > 1:
                fund("gelb", "lateinisch", "Lateinischer Name steht " + str(n)
                     + " x im Fliesstext, erlaubt ist hoechstens einmal")

    # --- Menschen und Kultur --------------------------------------------
    muk = sektionen.get("menschen-kultur")
    if muk is not None:
        n = wortzahl(" ".join(absaetze_von(muk)))
        mass["menschen_kultur_woerter"] = n
        if not (MUK_MIN <= n <= MUK_MAX):
            fund("gelb", "laenge-muk", '"Menschen und Kultur" hat ' + str(n) + " Woerter, vorgesehen sind "
                 + str(MUK_MIN) + " bis " + str(MUK_MAX))

    # --- Vor der Linse ---------------------------------------------------
    linse = sektionen.get("vor-der-linse")
    if linse is not None:
        txt = linse.text()
        n = wortzahl(txt)
        mass["vor_der_linse_woerter"] = n
        if not (LINSE_MIN <= n <= LINSE_MAX):
            fund("gelb", "laenge-linse", '"Vor der Linse" hat ' + str(n) + " Woerter, vorgesehen sind "
                 + str(LINSE_MIN) + " bis " + str(LINSE_MAX))
        for zeile in ("Wo und wann", "Brennweite", "Bild-Idee"):
            if zeile not in txt:
                fund("rot", "linse", 'Zeile "' + zeile + ':" fehlt in "Vor der Linse"')
        if not any(bw in txt for bw in BRENNWEITEN):
            fund("gelb", "linse", "Keine Brennweite aus unserem Set genannt (" + ", ".join(BRENNWEITEN) + ")")

    # --- Weiterlesen -----------------------------------------------------
    # Seit E21 gibt es den Block nicht mehr. Tobi googelt im Zweifel selbst,
    # Vogelrufe laufen ueber eBird und Merlin. Die Quellen bleiben im
    # Research-Doc, sie stehen nur nicht mehr im Buch.
    if sektionen.get("weiterlesen") is not None:
        fund("gelb", "weiterlesen",
             "Block \"Weiterlesen und Sehen\" ist seit E21 abgeschafft, bitte streichen")

    # --- Marker ----------------------------------------------------------
    # Zwei Sorten mit verschiedenen Folgen (Entscheidung E1 vom 18.09.2026):
    # [[LUECKE]] meint ein unbelegtes Pflichtfeld und faerbt gelb.
    # [[OFFEN]] meint, was das Research-Doc selbst als nicht belegbar ausweist,
    # und faerbt nicht.
    luecken = LUECKE_RE.findall(volltext)
    offene = OFFEN_RE.findall(volltext)
    mass["luecken"] = len(luecken)
    mass["offen"] = len(offene)
    for l in luecken:
        eine = " ".join(l.split())
        if "eitenzahl" in eine:
            fund("gelb", "seitenzahl",
                 "Seitenzahl gehoert in keinen Marker, dort steht (S. XX)", eine)
        else:
            fund("gelb", "luecke", "Offene Luecke im Pflichtfeld: " + eine)
    for o in offene:
        eine = " ".join(o.split())
        if "eitenzahl" in eine:
            fund("gelb", "seitenzahl",
                 "Seitenzahl gehoert in keinen Marker, dort steht (S. XX)", eine)
        else:
            fund("gelb", "offen",
                 "Marker [[OFFEN]] ist seit E15 abgeschafft. Was das Research-Doc nicht "
                 "hergibt, steht nicht im Kapitel, auch nicht als Marker: " + eine)

    # --- Kopfzeile -------------------------------------------------------
    namen_roh = meta.get("lokal", "") + " " + meta.get("swahili", "")
    if "Maasai" in namen_roh:
        fund("gelb", "kopfzeile",
             "Sprachbezeichnung Maasai in der Namenszeile, buchweit gilt Maa fuer die Sprache")
    kopf = doc.find("header", "kapitel-kopf")
    if kopf is not None:
        kopftext = kopf.text()
        for label in ("Englisch:", "Deutsch:", "English:"):
            if label in kopftext:
                fund("gelb", "kopfzeile",
                     "In der Namenszeile steht " + label
                     + " Dort gehoeren nur lokale Namen hin.")

    rot = sum(1 for f in befunde if f["schwere"] == "rot")
    gelb = sum(1 for f in befunde if f["schwere"] == "gelb")
    info = sum(1 for f in befunde if f["schwere"] == "info")

    return {
        "datei": pfad,
        "research_duenn": research_duenn,
        "ampel_regelcheck": "rot" if rot else ("gelb" if gelb else "gruen"),
        "rot": rot,
        "gelb": gelb,
        "info": info,
        "masse": mass,
        "metadaten": meta,
        "befunde": befunde,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("datei")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--research-duenn", action="store_true",
                    help="Research-Doc wurde im Substanz-Check als duenn markiert")
    a = ap.parse_args()

    e = pruefe(a.datei, research_duenn=a.research_duenn)

    if a.json:
        print(json.dumps(e, ensure_ascii=False, indent=2))
    else:
        print("Regel-Check: " + e["datei"])
        print("Ampel Regel-Check: " + e["ampel_regelcheck"]
              + " (" + str(e["rot"]) + " rot, " + str(e["gelb"]) + " gelb)")
        print("")
        print("Gemessen:")
        for k, v in e["masse"].items():
            print("  " + k.ljust(28) + " " + str(v))
        print("")
        if e["befunde"]:
            print("Befunde:")
            for f in e["befunde"]:
                print("  [" + f["schwere"].upper() + "] " + f["regel"] + ": " + f["meldung"])
                if f["zitat"]:
                    print("        > " + f["zitat"])
        else:
            print("Keine Befunde.")

    sys.exit(1 if e["rot"] else 0)


if __name__ == "__main__":
    main()
