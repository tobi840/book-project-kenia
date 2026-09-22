#!/usr/bin/env python3
"""Deterministischer Regel-Check fuer die Einleitungen (P6).

regel_check.py prueft die Kapitelstruktur und passt hier nicht: eine Einleitung
hat keine Kopfzeile mit Namen, keinen Block "Menschen und Kultur", keine
Illustration. Geprueft wird hier nur, was P6 fuer Einleitungen festlegt.

    python3 scripts/einleitung_check.py einleitungen/01-nairobi.html
    python3 scripts/einleitung_check.py einleitungen/*.html
"""

import re
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from regel_check import (saubere_woerter, wortzahl, saetze,
                         VERBOTENE_WOERTER, HALBGEVIERT, GEVIERT)

ABSATZ_NORM_MIN, ABSATZ_NORM_MAX, ABSATZ_HART = 80, 180, 200
ERSTER_SATZ_MAX = 25
LETZTER_ABSATZ_MAX = 80
SATZ_LANG = 40
KETTE = re.compile(r"\b[a-zäöüß]+(?:e|en|er|es|em)\s*,\s*[a-zäöüß]+(?:e|en|er|es|em)\s*,\s*"
                   r"[a-zäöüß]+(?:e|en|er|es|em)\b")

# Lateinische Namen prueft research_check.py gegen das Research-Doc. Ein
# zweiter, unabhaengiger Test hier meldete jeden Satzanfang als Binomen.


def zone(nr):
    return (1200, 1500) if nr == "00" else (400, 600)


def absaetze(rumpf):
    """Alle <p> ausserhalb des <header>."""
    ohne_kopf = re.sub(r"(?s)<header.*?</header>", "", rumpf)
    roh = re.findall(r"(?s)<p[^>]*>(.*?)</p>", ohne_kopf)
    return [re.sub(r"<[^>]+>", "", p).strip() for p in roh]


def pruefe(pfad):
    text = open(pfad, encoding="utf-8").read()
    kopf = re.search(r"(?s)<!--(.*?)-->", text)
    felder = {}
    if kopf:
        for zeile in kopf.group(1).strip().splitlines():
            if ":" in zeile:
                k, v = zeile.split(":", 1)
                felder[k.strip()] = v.strip()
    rumpf = re.sub(r"(?s)<!--.*?-->", "", text)
    nr = felder.get("abschnitt", "??")
    befunde = []

    for feld in ("typ", "abschnitt", "titel", "quelle", "status"):
        if feld not in felder:
            befunde.append(("rot", "Kopfzeile: Feld %s fehlt" % feld))

    ps = absaetze(rumpf)
    if not ps:
        befunde.append(("rot", "kein Absatz gefunden"))
        return nr, 0, befunde, felder

    gesamt = sum(wortzahl(p) for p in ps)
    umin, umax = zone(nr)
    if gesamt < umin:
        befunde.append(("rot", "Wortzahl %d unter %d" % (gesamt, umin)))
    elif gesamt > umax:
        schwere = "gelb" if nr != "00" and gesamt <= umax + 150 else "rot"
        befunde.append((schwere, "Wortzahl %d ueber %d" % (gesamt, umax)))

    for i, p in enumerate(ps, 1):
        w = wortzahl(p)
        letzter = (i == len(ps))
        if w > ABSATZ_HART:
            befunde.append(("rot", "Absatz %d hat %d Woerter, ueber %d" % (i, w, ABSATZ_HART)))
        elif w > ABSATZ_NORM_MAX:
            befunde.append(("gelb", "Absatz %d hat %d Woerter, ueber %d" % (i, w, ABSATZ_NORM_MAX)))
        elif w < ABSATZ_NORM_MIN and not letzter:
            befunde.append(("gelb", "Absatz %d hat %d Woerter, unter %d" % (i, w, ABSATZ_NORM_MIN)))
        if letzter and w >= LETZTER_ABSATZ_MAX:
            befunde.append(("rot", "letzter Absatz hat %d Woerter, nicht unter %d" % (w, LETZTER_ABSATZ_MAX)))

    erste = saetze(ps[0])
    if erste and wortzahl(erste[0]) >= ERSTER_SATZ_MAX:
        befunde.append(("rot", "erster Satz hat %d Woerter, nicht unter %d"
                        % (wortzahl(erste[0]), ERSTER_SATZ_MAX)))

    ganz = " ".join(ps)
    for z, name in ((HALBGEVIERT, "Halbgeviertstrich"), (GEVIERT, "Geviertstrich")):
        if z in ganz:
            befunde.append(("rot", "%s im Text" % name))
    for w in VERBOTENE_WOERTER:
        if w.lower() in ganz.lower():
            befunde.append(("rot", "verbotenes Wort: %s" % w))
    for i, p in enumerate(ps, 1):
        for s in saetze(p):
            if wortzahl(s) > SATZ_LANG:
                befunde.append(("gelb", "Absatz %d: Satz mit %d Woertern" % (i, wortzahl(s))))
        if KETTE.search(p):
            befunde.append(("gelb", "Absatz %d: Dreierkette %s"
                            % (i, KETTE.search(p).group(0))))

    return nr, gesamt, befunde, felder


def main():
    schlimm = 0
    for pfad in sys.argv[1:]:
        nr, gesamt, befunde, felder = pruefe(pfad)
        rot = [b for b in befunde if b[0] == "rot"]
        gelb = [b for b in befunde if b[0] == "gelb"]
        ampel = "rot" if rot else ("gelb" if gelb else "gruen")
        print("%s  %s  %d Woerter  %s" % (pfad, ampel, gesamt, felder.get("titel", "")))
        for schwere, text in befunde:
            print("   [%s] %s" % (schwere, text))
        if rot:
            schlimm = 1
    return schlimm


if __name__ == "__main__":
    sys.exit(main())
