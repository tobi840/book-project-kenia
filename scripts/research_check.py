#!/usr/bin/env python3
"""Kapitel gegen das Research-Doc pruefen, soweit sich das mechanisch geht.

Der Regel-Check zaehlt nur. Er liest den Text nicht gegen die Quelle und hat
darum im Pilot fuenf von fuenf Kapiteln gruen gemeldet, von denen drei
faktisch rot waren. Dieses Skript schliesst die drei Luecken, die im Pilot
zusammen 19 von 30 Befunden ausmachten:

  1. Zahlen, die im Kapitel stehen und im Research-Doc nicht vorkommen
  2. Alltagsvergleiche, die das Research-Doc nicht hergibt
  3. Lateinische Namen: erfunden, oder vorhanden und nicht kursiv
  4. Zuspitzung: eine Aufzaehlung, die im Doc ein Vorbehaltswort traegt
     und im Kapitel keins

Alles wird als "pruefen" gemeldet, nicht als Urteil. Das Skript kann nicht
wissen, ob eine Zahl umgerechnet oder ein Vergleich sinngemaess uebernommen
wurde. Es zeigt die Stelle, entschieden wird in der QS.

    python3 scripts/research_check.py chapters/001-x.html --research research/001-x.txt
    python3 scripts/research_check.py chapters/001-x.html --research research/001-x.txt --json

Exit-Code 0 = keine Befunde, sonst 1.
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from regel_check import Builder, saetze, LUECKE_RE, OFFEN_RE  # noqa: E402


# ----------------------------------------------------------------- Konstanten

# Brennweiten aus unserem Set. Die stehen in keinem Research-Doc und sollen
# auch nicht drinstehen, es ist unsere Ausruestung.
BRENNWEITEN_ZAHLEN = {"100", "400", "150", "600", "45", "26", "60"}

# Zahlwoerter, damit "zwoelf Menschen" und "12 Menschen" sich finden.
ZAHLWORT = {
    "null": 0, "ein": 1, "eine": 1, "einer": 1, "eines": 1, "zwei": 2,
    "drei": 3, "vier": 4, "fuenf": 5, "fünf": 5, "sechs": 6, "sieben": 7,
    "acht": 8, "neun": 9, "zehn": 10, "elf": 11, "zwoelf": 12, "zwölf": 12,
    "dreizehn": 13, "vierzehn": 14, "fuenfzehn": 15, "fünfzehn": 15,
    "sechzehn": 16, "siebzehn": 17, "achtzehn": 18, "neunzehn": 19,
    "zwanzig": 20, "dreissig": 30, "dreißig": 30, "vierzig": 40,
    "fuenfzig": 50, "fünfzig": 50, "sechzig": 60, "siebzig": 70,
    "achtzig": 80, "neunzig": 90, "hundert": 100, "tausend": 1000,
}

# Alltagsvergleiche. Jeder einzelne ist eine Tatsachenbehauptung ueber eine
# Groesse und muss im Research-Doc stehen (E2). Im Pilot liefen sechs
# erfundene Vergleiche durch, drei davon durch zwei QS-Runden.
VERGLEICH_RE = [
    re.compile(r"\bso\s+(?:gross|groß|lang|hoch|breit|dick|schwer|schmal|weit|tief)\s+wie\b", re.I),
    re.compile(r"\b\w+(?:gross|groß|lang|hoch|dick|schwer|breit|tief|schmal)\b", re.I),
    re.compile(r"\bkaum\s+(?:groesser|größer|laenger|länger|dicker|hoeher|höher)\s+als\b", re.I),
    re.compile(r"\b(?:Armlaenge|Armlänge|Fingerkuppe|Handflaeche|Handfläche|Handteller|"
               r"Daumennagel|Fingernagel|Streichholz|Fussballfeld|Fußballfeld|Tennisplatz|"
               r"Ellenbogen|Unterarm|Handruecken|Handrücken)\w*", re.I),
]
# Zusammensetzungen auf -gross/-lang, die keine Alltagsvergleiche sind.
VERGLEICH_STOPP = re.compile(
    r"^(?:jahrelang|lebenslang|stundenlang|tagelang|wochenlang|monatelang|"
    r"ewiglang|langlang|entlang|zeitlebenslang|meterlang|zentimeterlang|"
    r"millimeterlang|kilometerlang|gleichlang|dabeilang|solang|genauso\w*|"
    r"hochhoch|einlang)$", re.I)

# Vorbehaltswoerter. Steht eins davon im Quellsatz und keins im Kapitelsatz,
# ist die Aufzaehlung im Kapitel geschlossen, im Doc war sie offen.
VORBEHALT = [
    "darunter", "unter anderem", "u. a.", "u.a.", "zum Beispiel",
    "z. B.", "z.B.", "beispielsweise", "vor allem", "primär", "primäre",
    "überwiegend", "hauptsächlich", "meist", "in der Regel",
    "verschiedene", "unter ihnen", "wie etwa", "typischerweise",
    "in erster Linie", "insbesondere", "vorwiegend", "vornehmlich",
]

# Endungen, an denen eine Familie oder eine hoehere Gruppe zu erkennen ist.
TAXON_ENDUNG = re.compile(r"\b([A-Z][a-z]{3,}(?:aceae|idae|inae|ales|oideae|ini))\b")

# Endungen lateinischer Artepitheta. Die alte Heuristik im Regel-Check suchte
# nur Wortpaare und liess Trigona, Podocarpaceae und Podocarpus durch.
LAT_EPITHET = (
    "us", "um", "ii", "ensis", "ata", "osa", "ica", "ana", "oides", "folia",
    "ior", "iana", "alis", "aris", "orum", "arum", "atum", "era", "ifera",
    "ina", "inum", "eae", "ea", "iensis", "ella", "illa", "ata", "ata",
)
# Deutsche Woerter, die zufaellig so enden.
LAT_EPITHET_STOPP = set("""
herum darum warum ringsum worum wiederum ringsherum drumherum
datum album museum zentrum publikum minimum maximum optimum
virus zirkus fokus modus status bonus kaktus
hinaus heraus voraus daraus woraus hieraus durchaus zuhaus
""".split())


# Grosse Woerter, die wie eine Gattung aussehen und keine sind.
GATTUNG_STOPP = set("""
Afrika Ostafrika Westafrika Kenia Kenias Uganda Tansania Nairobi Mombasa
Europa Amerika Mexiko Asien Indien China Japan Deutschland England Kew
Januar Februar Maerz April Juni Juli August September Oktober November
Dezember Montag Dienstag Mittwoch Donnerstag Freitag Samstag Sonntag
Swahili Kikuyu Kamba Luo Luhya Maasai Maa Meru Embu Samburu Pokot Turkana
Works Where This These Eine Diese Dieser Der Die Das Ein Und Als Von Mit
""".split())


# Lateinische Wortpaare, die keine Artnamen sind. Krankheiten, Fachbegriffe.
KEIN_ARTNAME = set([
    "Malaria tropica", "Diabetes mellitus", "Delirium tremens",
    "Malaria", "Diabetes", "Delirium", "Status", "Habitus", "Modus",
])


def ist_epithet(w):
    if any(c in w for c in "äöüß"):
        return False
    if w in LAT_EPITHET_STOPP:
        return False
    return len(w) >= 4 and w.endswith(LAT_EPITHET)


def binomen_aus(text):
    """Artnamen, die im Text wirklich als Binomen auftauchen."""
    treffer = set()
    for m in re.finditer(r"\b([A-Z][a-z]{3,})\s+([a-z]{4,})\b", text):
        if m.group(1) in GATTUNG_STOPP:
            continue
        if not ist_epithet(m.group(2)):
            continue
        treffer.add((m.group(1), m.group(2)))
    return treffer


def normzahl(s):
    """1.200 und 1200 sind dieselbe Zahl, 1,5 und 1.5 auch."""
    s = s.replace(".", "").replace(",", ".")
    try:
        f = float(s)
    except ValueError:
        return None
    return str(int(f)) if f == int(f) else str(f)


def zahlformen(n):
    """Alle Schreibweisen, unter denen eine Zahl im Doc stehen kann."""
    formen = {n}
    if "." not in n:
        i = int(n)
        if i >= 1000:
            formen.add("{:,}".format(i).replace(",", "."))
            formen.add("{:,}".format(i))
            formen.add("{:,}".format(i).replace(",", " "))
        for wort, wert in ZAHLWORT.items():
            if wert == i:
                formen.add(wort)
    else:
        formen.add(n.replace(".", ","))
    return formen


def zahlen_aus(text):
    """Zahlen mit ihrer Umgebung, ohne Marker und ohne URLs."""
    text = OFFEN_RE.sub(" ", LUECKE_RE.sub(" ", text))
    text = re.sub(r"https?://\S+", " ", text)
    out = []
    for m in re.finditer(r"(?<![\w.,])(\d{1,3}(?:[.\s]\d{3})+|\d+(?:,\d+)?)(?![\w])", text):
        roh = m.group(1).replace(" ", ".")
        n = normzahl(roh)
        if n is None:
            continue
        links = text[max(0, m.start() - 45):m.start()].strip()
        rechts = text[m.end():m.end() + 45].strip()
        out.append((roh, n, (links + " [" + m.group(1) + "] " + rechts).strip()))
    return out


def doc_saetze(doc):
    return [" ".join(s.split()) for s in re.split(r"(?<=[.!?:;])\s+|\n+", doc) if s.strip()]


def hat_vorbehalt(satz):
    low = satz.lower()
    return [v for v in VORBEHALT if v.lower() in low]


def aufzaehlungen(satz):
    """Aufzaehlungen ab drei Gliedern, als Liste der Inhaltswoerter."""
    if satz.count(",") < 2:
        return []
    if not re.search(r",\s*[^,]{2,60}\s+(?:und|oder|sowie)\s+", satz):
        return []
    teile = re.split(r",|\s+und\s+|\s+oder\s+|\s+sowie\s+", satz)
    glieder = []
    for t in teile:
        woerter = [w.strip(".,;:()„“\"'") for w in t.split()]
        woerter = [w for w in woerter if len(w) > 4 and re.match(r"^[A-ZÄÖÜ]", w)]
        if woerter:
            glieder.append(woerter[0])
    return glieder if len(glieder) >= 3 else []


def pruefe(kapitel_pfad, research_pfad):
    with open(kapitel_pfad, encoding="utf-8") as fh:
        html = fh.read()
    with open(research_pfad, encoding="utf-8") as fh:
        doc = fh.read()
    doc_low = doc.lower()
    d_saetze = doc_saetze(doc)

    b = Builder()
    b.feed(html)
    art = b.root.find("article") or b.root

    befunde = []

    def fund(art_, text, zitat=""):
        befunde.append({"art": art_, "text": text, "zitat": zitat})

    sektionen = {}
    for s in art.find_all("section"):
        for c in s.cls().split():
            sektionen[c] = s

    gesch = sektionen.get("geschichte")
    muk = sektionen.get("menschen-kultur")
    linse = sektionen.get("vor-der-linse")

    prosa_knoten = [n for n in (gesch, muk) if n is not None]
    prosa = " ".join(n.text() for n in prosa_knoten)

    # --- 1. Zahlen -------------------------------------------------------
    zahl_quellen = list(prosa_knoten)
    if linse is not None:
        zahl_quellen.append(linse)
    gesehen = set()
    for knoten in zahl_quellen:
        ist_linse = knoten is linse
        for roh, n, umgebung in zahlen_aus(knoten.text()):
            if n in gesehen:
                continue
            if ist_linse and roh in BRENNWEITEN_ZAHLEN:
                continue
            if any(f in doc for f in zahlformen(n)):
                gesehen.add(n)
                continue
            if any(f.lower() in doc_low for f in zahlformen(n)):
                gesehen.add(n)
                continue
            gesehen.add(n)
            fund("zahl", "Zahl " + roh + " steht so nicht im Research-Doc", umgebung)

    # --- 2. Alltagsvergleiche --------------------------------------------
    for satz in saetze(prosa):
        for rx in VERGLEICH_RE:
            for m in rx.finditer(satz):
                treffer = m.group(0)
                if VERGLEICH_STOPP.match(treffer):
                    continue
                kern = treffer.lower()
                if kern in doc_low:
                    continue
                # Auch das Bezugswort pruefen: "so gross wie eine Faust".
                # Das Doc formuliert den Vergleich oft anders und flektiert
                # anders ("entspricht der Hoehe eines einstoeckigen Gebaeudes"
                # gegen "so hoch wie ein einstoeckiges Gebaeude"). Deshalb
                # nicht auf das ganze Wort pruefen, sondern auf den Stamm,
                # und nicht nur auf das erste Wort nach dem Vergleich.
                nach = satz[m.end():m.end() + 60]
                bezug = re.findall(r"[A-Za-zÄÖÜäöüß]{5,}", nach)[:3]
                if any(w.lower()[:6] in doc_low for w in bezug):
                    continue
                fund("vergleich",
                     'Alltagsvergleich "' + treffer + '" steht nicht im Research-Doc (E2)',
                     satz[:140])

    # --- 3. Lateinische Namen --------------------------------------------
    # Zwei Signale, die kaum falsch anschlagen. Erstens der Widerspruch im
    # Kapitel selbst: was einmal kursiv steht, gehoert ueberall kursiv.
    # Zweitens die im Research-Doc belegten Binomen.
    ohne_em = " ".join(n.text_ohne("em") for n in prosa_knoten)
    kursiv_gesetzt = set()
    for n in prosa_knoten:
        for em in n.find_all("em"):
            t = " ".join(em.text().split()).strip(".,;:()„“\"")
            if not t:
                continue
            kursiv_gesetzt.add(t)
            erstes = t.split()[0]
            if erstes[:1].isupper():
                kursiv_gesetzt.add(erstes)

    doc_binomen = binomen_aus(doc)
    doc_gattungen = set(g for g, _ in doc_binomen)
    for m in TAXON_ENDUNG.finditer(doc):
        doc_gattungen.add(m.group(1))

    gemeldet = set()

    def kursiv_fund(begriff, grund):
        if begriff in gemeldet or begriff in KEIN_ARTNAME:
            return
        if not re.search(r"\b" + re.escape(begriff) + r"\b", ohne_em):
            return
        gemeldet.add(begriff)
        stelle = re.search(r".{0,45}\b" + re.escape(begriff) + r"\b.{0,45}", ohne_em)
        fund("kursiv", grund + ': "' + begriff + '"',
             " ".join(stelle.group(0).split()) if stelle else "")

    for t in sorted(kursiv_gesetzt, key=len, reverse=True):
        kursiv_fund(t, "Steht im Kapitel einmal kursiv und hier aufrecht")
    for g, e in sorted(doc_binomen):
        kursiv_fund(g + " " + e, "Artname aus dem Research-Doc, hier aufrecht")
    for g in sorted(doc_gattungen):
        kursiv_fund(g, "Gattung oder Familie aus dem Research-Doc, hier aufrecht")
    for m in TAXON_ENDUNG.finditer(ohne_em):
        kursiv_fund(m.group(1), "Taxon-Endung ausserhalb von <em>")

    # Erfundene Artnamen: kursiv gesetzt, im Research-Doc nicht vorhanden
    for t in sorted(kursiv_gesetzt):
        if " " not in t:
            continue
        g, _, e = t.partition(" ")
        e = e.split()[0] if e.split() else ""
        if not (g[:1].isupper() and ist_epithet(e)):
            continue
        if (g, e) not in doc_binomen and (g + " " + e) not in doc:
            fund("artname", "Lateinischer Name steht nicht im Research-Doc", t[:60])

    # --- 4. Zuspitzung ----------------------------------------------------
    for satz in saetze(prosa):
        glieder = aufzaehlungen(satz)
        if not glieder:
            continue
        if hat_vorbehalt(satz):
            continue
        noetig = max(2, int(len(glieder) * 0.6 + 0.999))
        for ds in d_saetze:
            treffer = [g for g in glieder if g in ds]
            if len(treffer) < noetig:
                continue
            # Zahlenbereiche sind keine Aufzaehlung von Dingen. "von 2,3 bis
            # zu 5,1 Metern" und "zwischen 2,3 und 5,1 Metern" sind dasselbe.
            if len(re.findall(r"\d", satz)) > 6 and len(re.findall(r"\d", ds)) > 4:
                continue
            vorbehalte = hat_vorbehalt(ds)
            if vorbehalte:
                fund("zuspitzung",
                     "Aufzaehlung geschlossen, Quellsatz traegt " + ", ".join(
                         '"' + v + '"' for v in vorbehalte[:3]),
                     "KAPITEL: " + satz[:120] + "  ||  DOC: " + ds[:140])
                break

    return {
        "kapitel": kapitel_pfad,
        "research": research_pfad,
        "anzahl": len(befunde),
        "befunde": befunde,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kapitel")
    ap.add_argument("--research", required=True)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    e = pruefe(a.kapitel, a.research)
    if a.json:
        print(json.dumps(e, ensure_ascii=False, indent=2))
    else:
        print("Research-Check: " + e["kapitel"])
        print("Befunde: " + str(e["anzahl"]) + "  (alle zum Pruefen, keine Urteile)")
        print()
        for f in e["befunde"]:
            print("  [" + f["art"].upper() + "] " + f["text"])
            if f["zitat"]:
                print("      " + f["zitat"])
    return 1 if e["anzahl"] else 0


if __name__ == "__main__":
    sys.exit(main())
