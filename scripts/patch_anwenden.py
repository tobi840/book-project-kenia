#!/usr/bin/env python3
"""Patches aus einer QS-Datei auf ein Kapitel anwenden.

Der Schritt, den bisher ein Modell gemacht hat. Im Pilot ist dabei in 2 von
5 Kapiteln ein neuer Fehler entstanden, jedes Mal beim Umformulieren, kein
einziges Mal beim Streichen. Also formuliert hier nichts mehr um.

Das Skript liest den ```patch-Block aus qs/{nr}-{slug}.md, prueft jeden
Patch gegen drei Regeln und wendet nur an, was durchkommt:

  1. Der zitierte Wortlaut kommt genau einmal im Kapitel vor.
  2. Bei ERSETZEN ist der Ersatz eine von drei erlaubten Formen:
     der alte Wortlaut ohne einzelne Woerter, oder eine Wortfolge, die
     woertlich im Research-Doc steht, oder der alte Wortlaut plus ein
     Vorbehaltswort aus dem Doc.
  3. Reine Kursivsetzung (<em>) ist immer erlaubt.

Was nicht durchkommt, wird gemeldet und nicht angewendet.

    python3 scripts/patch_anwenden.py chapters/001-x.html \\
        --qs qs/001-x.md --research research/001-x.txt
    ... --dry-run     nur zeigen, nichts schreiben

Exit-Code 0 = alle Patches angewendet, 1 = mindestens einer abgelehnt.
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from research_check import VORBEHALT  # noqa: E402

PATCH_BLOCK = re.compile(r"```patch\s*\n(.*?)```", re.S)


def norm(s):
    return " ".join(s.split())


def ohne_em(s):
    return norm(re.sub(r"</?em>", "", s))


def ist_streichung(alt, neu):
    """Ist neu der alte Wortlaut, aus dem nur Woerter entfernt wurden?"""
    a = ohne_em(alt).split()
    n = ohne_em(neu).split()
    if len(n) >= len(a):
        return False
    i = 0
    for w in a:
        if i < len(n) and n[i] == w:
            i += 1
    return i == len(n)


def ist_vorbehalt_ergaenzung(alt, neu):
    """Ist neu der alte Wortlaut plus genau ein Vorbehaltswort?"""
    a = ohne_em(alt)
    n = ohne_em(neu)
    for v in VORBEHALT:
        for kandidat in (v + " ", " " + v + " ", ", " + v + " "):
            if n.replace(kandidat, " ", 1).replace("  ", " ").strip() == a:
                return True
        # Am Satzanfang traegt das Vorbehaltswort den Grossbuchstaben, das alte erste Wort wird klein.
        anfang = v.capitalize() + " "
        if n.startswith(anfang):
            rest = n[len(anfang):]
            if rest[:1].upper() + rest[1:] == a:
                return True
    return False


def ist_nur_kursiv(alt, neu):
    return ohne_em(alt) == ohne_em(neu) and neu.count("<em>") > alt.count("<em>")


def patches_aus(qs_text):
    out = []
    for block in PATCH_BLOCK.findall(qs_text):
        for zeile in block.splitlines():
            if not zeile.strip():
                continue
            felder = zeile.split("\t")
            felder = [f for f in felder if f != ""]
            if not felder:
                continue
            aktion = felder[0].strip().upper()
            if aktion == "STREICHEN" and len(felder) >= 2:
                out.append(("STREICHEN", felder[1], ""))
            elif aktion == "ERSETZEN" and len(felder) >= 3:
                out.append(("ERSETZEN", felder[1], felder[2]))
            else:
                out.append(("UNGUELTIG", zeile.strip(), ""))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kapitel")
    ap.add_argument("--qs", required=True)
    ap.add_argument("--research", required=True)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    html = open(a.kapitel, encoding="utf-8").read()
    qs = open(a.qs, encoding="utf-8").read()
    doc_norm = norm(open(a.research, encoding="utf-8").read())
    # Fussnotenziffern kleben im Doc am Wort ("Hundekot4"), ein woertliches Zitat hat sie nicht.
    doc_ohne_fussnoten = re.sub(r"(?<=[A-Za-zäöüß)])\d{1,3}(?=[\s.,;:\[]|$)", "", doc_norm)

    patches = patches_aus(qs)
    if not patches:
        print("Kein ```patch-Block in " + a.qs + " gefunden.")
        return 1

    angewendet, abgelehnt = [], []
    for aktion, alt, neu in patches:
        if aktion == "UNGUELTIG":
            abgelehnt.append((alt, "Zeile passt in kein Patch-Format"))
            continue
        n = html.count(alt)
        if n == 0:
            abgelehnt.append((alt[:70], "Wortlaut kommt im Kapitel nicht vor"))
            continue
        if n > 1:
            abgelehnt.append((alt[:70], "Wortlaut kommt " + str(n) + " mal vor, nicht eindeutig"))
            continue
        if aktion == "ERSETZEN":
            erlaubt = (ist_nur_kursiv(alt, neu)
                       or ist_streichung(alt, neu)
                       or ohne_em(neu) in doc_norm
                       or ohne_em(neu).rstrip(".") in doc_ohne_fussnoten
                       or ist_vorbehalt_ergaenzung(alt, neu))
            if not erlaubt:
                abgelehnt.append(
                    (alt[:70], "Ersatz ist eine Umformulierung. Erlaubt sind nur "
                               "Streichung, woertliche Uebernahme aus dem Doc oder "
                               "ein ergaenztes Vorbehaltswort"))
                continue
        html = html.replace(alt, neu, 1)
        angewendet.append((aktion, alt[:70], neu[:70]))

    print("Patch-Lauf: " + a.kapitel)
    print("  angewendet: " + str(len(angewendet)) + "   abgelehnt: " + str(len(abgelehnt)))
    print()
    for aktion, alt, neu in angewendet:
        print("  [" + aktion + "] " + norm(alt))
        if neu:
            print("      -> " + norm(neu))
    if abgelehnt:
        print()
        print("  Abgelehnt, bitte von Hand entscheiden:")
        for alt, grund in abgelehnt:
            print("  [ABGELEHNT] " + norm(alt))
            print("      " + grund)

    if not a.dry_run and angewendet:
        with open(a.kapitel, "w", encoding="utf-8") as fh:
            fh.write(html)
        print()
        print("  " + a.kapitel + " geschrieben.")
    elif a.dry_run:
        print()
        print("  Probelauf, nichts geschrieben.")

    return 1 if abgelehnt else 0


if __name__ == "__main__":
    sys.exit(main())
