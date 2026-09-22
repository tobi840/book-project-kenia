#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Nummeriert die Kapitel auf die Lesereihenfolge des Buches um.

Bis zum 22.09.2026 war die Kapitelnummer eine reine Kennung aus der
Entstehungsreihenfolge. 081 bis 100 kamen nachtraeglich dazu und verteilten
sich ueber alle fuenf Lebensraeume, deshalb standen Marabu (086) und
Dorfweber (090) im Abschnitt Nairobi hinter Kapitel 017. Im gesetzten Buch
sieht man die Nummer, und dort ist ein Sprung von 017 auf 086 ein Fehler.

Die neue Nummer ist die Position in der Lesereihenfolge. Die alte bleibt als
`alt_nr` im Kopfkommentar stehen, weil die Deep-Research-Docs in Drive nach
den alten Nummern heissen und sonst nicht mehr auffindbar waeren.

Umbenannt wird in zwei Durchgaengen ueber ein Zwischenpraefix. Ein Durchgang
wuerde Dateien ueberschreiben, weil sich alte und neue Nummern ueberlappen
(016 wird 018, und 018 gibt es schon).

    python3 scripts/umnummerieren.py --probe   # nur rechnen und zeigen
    python3 scripts/umnummerieren.py           # ausfuehren
"""

import csv
import glob
import os
import re
import subprocess
import sys

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Die Reihenfolge der Abschnitte im Buch. Sie steht genauso in
# scripts/buch_bauen.py und in prompts/P6-einleitungen.md.
ABSCHNITTE = [
    "Nairobi",
    "Rift Valley",
    "Laikipia / Mt. Kenya",
    "Küste Mombasa",
    "Tsavo / Amboseli",
]

# Im Kopfkommentar der Kapitel stehen zwei Schreibweisen fuer denselben
# Abschnitt. Der Buchbau nimmt die Zuordnung aus chapters.tsv und merkt es
# deshalb nicht. Bei der Gelegenheit wird es gerade gezogen.
LEBENSRAUM_NORM = {"Laikipia / Mount Kenya": "Laikipia / Mt. Kenya"}

ZWISCHEN = "zz"


def pfad(*teile):
    return os.path.join(WURZEL, *teile)


def abbildung():
    """Liest chapters.tsv und gibt [(alt, neu, name, lebensraum)] zurueck."""
    zeilen = [
        z for z in csv.reader(open(pfad("chapters.tsv"), encoding="utf-8"), delimiter="\t")
        if z and z[0].strip()
    ]
    gruppen = {a: [] for a in ABSCHNITTE}
    for nr, name, leb in zeilen:
        leb = LEBENSRAUM_NORM.get(leb.strip(), leb.strip())
        if leb not in gruppen:
            sys.exit("Lebensraum ohne Abschnitt: %r" % leb)
        gruppen[leb].append((nr.strip(), name.strip()))

    aus, lauf = [], 0
    for a in ABSCHNITTE:
        for alt, name in gruppen[a]:
            lauf += 1
            aus.append((alt, "%03d" % lauf, name, a))
    if lauf != 100:
        sys.exit("Erwartet werden 100 Kapitel, gezaehlt wurden %d." % lauf)
    return aus


def dateien(nr):
    """Alle Dateien, die an einer Kapitelnummer haengen."""
    treffer = []
    treffer += glob.glob(pfad("chapters", nr + "-*.html"))
    treffer += glob.glob(pfad("qs", nr + "-*.md"))
    treffer += glob.glob(pfad("illustrationen", nr + "_*"))
    doc = pfad("research", nr + ".txt")
    if os.path.exists(doc):
        treffer.append(doc)
    return sorted(treffer)


def neuer_name(weg, alt, neu):
    """Ersetzt das Nummernpraefix im Dateinamen, sonst nichts."""
    ordner, name = os.path.split(weg)
    if not name.startswith(alt):
        sys.exit("Datei ohne erwartetes Praefix: %s" % weg)
    return os.path.join(ordner, neu + name[len(alt):])


def git_mv(quelle, ziel):
    subprocess.run(["git", "mv", quelle, ziel], cwd=WURZEL, check=True)


def kapitel_anpassen(weg, alt, neu, lebensraum):
    """Zieht Nummer, Research-Verweis und Bildpfad im Kapitel nach."""
    text = open(weg, encoding="utf-8").read()
    kopf_ende = text.index("-->")
    kopf, rest = text[:kopf_ende], text[kopf_ende:]

    kopf = re.sub(r"^nr: .*$", "nr: " + neu, kopf, flags=re.M)
    kopf = re.sub(r"^research_doc: .*$", "research_doc: research/%s.txt" % neu,
                  kopf, flags=re.M)
    kopf = re.sub(r"^lebensraum: .*$", "lebensraum: " + lebensraum, kopf, flags=re.M)
    if "alt_nr:" not in kopf:
        kopf = re.sub(r"^(nr: .*)$", r"\1\nalt_nr: " + alt, kopf, flags=re.M)

    rest = rest.replace('data-nr="%s"' % alt, 'data-nr="%s"' % neu)
    rest = re.sub(r'(\.\./illustrationen/)%s_' % alt, r"\g<1>%s_" % neu, rest)
    open(weg, "w", encoding="utf-8").write(kopf + rest)


def tsv_schreiben(abb):
    with open(pfad("chapters.tsv"), "w", encoding="utf-8", newline="") as f:
        for _, neu, name, leb in abb:
            f.write("%s\t%s\t%s\n" % (neu, name, leb))


def main():
    probe = "--probe" in sys.argv
    abb = abbildung()

    fehlt = [alt for alt, _, _, _ in abb if not glob.glob(pfad("chapters", alt + "-*.html"))]
    if fehlt:
        sys.exit("Kapiteldatei fehlt zu: %s" % ", ".join(fehlt))

    wechsel = [x for x in abb if x[0] != x[1]]
    print("Kapitel gesamt: %d, Nummer aendert sich bei %d." % (len(abb), len(wechsel)))
    for a in ABSCHNITTE:
        teil = [x for x in abb if x[3] == a]
        print("  %-24s %s bis %s (%d)" % (a, teil[0][1], teil[-1][1], len(teil)))
    if probe:
        for alt, neu, name, _ in wechsel:
            print("  %s -> %s  %s" % (alt, neu, name))
        return

    # Durchgang 1: alles auf ein Zwischenpraefix, damit sich nichts ueberschreibt.
    for alt, neu, _, _ in abb:
        for weg in dateien(alt):
            git_mv(weg, neuer_name(weg, alt, ZWISCHEN + neu))

    # Durchgang 2: Zwischenpraefix entfernen, Inhalte nachziehen.
    for alt, neu, _, leb in abb:
        for weg in dateien(ZWISCHEN + neu):
            ziel = neuer_name(weg, ZWISCHEN + neu, neu)
            git_mv(weg, ziel)
            if ziel.endswith(".html") and "/chapters/" in ziel:
                kapitel_anpassen(ziel, alt, neu, leb)

    tsv_schreiben(abb)
    print("Umbenannt. chapters.tsv neu geschrieben.")


if __name__ == "__main__":
    main()
