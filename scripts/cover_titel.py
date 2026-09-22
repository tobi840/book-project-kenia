#!/usr/bin/env python3
"""Setzt Titel und Untertitel in das freie Mittelfeld des Covers.

Das Bild kommt ohne Text aus der Generierung, weil Bildmodelle deutsche
Schrift unzuverlaessig setzen. Die Typografie kommt hier dazu, in echter
Schrift und damit scharf, auch fuer EPUB und PDF.

Das Rohbild liegt als buch/cover-roh.png im Repo, damit sich das Cover
ohne einen neuen Generierungslauf wiederherstellen laesst.

    python3 scripts/cover_titel.py <roh.png> buch/cover.png
"""

import sys
from PIL import Image, ImageDraw, ImageFont

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
TITEL = ["KENIA,", "VORGELESEN"]
UNTERTITEL = ["Hundert Arten zwischen", "Riff und Gipfel"]
AUTOR = "Tobi Brockmann"
FARBE = (38, 32, 26)
SPERRUNG = 0.10          # Anteil der Schriftgroesse als Buchstabenabstand
RAND = 24                # Sicherheitsabstand zum Motivkranz


def hell(p):
    """Der freie Mittelgrund ist warmes Cremepapier, nicht Weiss. Die Schwelle
    muss den Gelbstich zulassen, sonst findet sie das Feld nicht."""
    r, g, b = p[:3]
    return r > 238 and g > 230 and b > 203 and max(p[:3]) - min(p[:3]) < 44


def freies_feld(im):
    """Laengster heller Lauf je Zeile, als {y: (x_links, x_rechts)}."""
    w, h = im.size
    px = im.load()
    feld = {}
    for y in range(h):
        lauf, best = None, None
        for x in range(0, w, 2):
            if hell(px[x, y]):
                if lauf is None:
                    lauf = x
            else:
                if lauf is not None and (best is None or x - lauf > best[1] - best[0]):
                    best = (lauf, x)
                lauf = None
        if lauf is not None and (best is None or w - lauf > best[1] - best[0]):
            best = (lauf, w)
        if best and best[1] - best[0] > w * 0.25:
            feld[y] = best
    return feld


def breite_bei(feld, y, hoehe):
    """Engste Stelle im Band y bis y+hoehe."""
    werte = [feld[k][1] - feld[k][0] for k in feld if y <= k <= y + hoehe]
    return min(werte) if werte else 0


def gesperrt(draw, text, font, sperrung):
    return sum(draw.textlength(c, font=font) for c in text) + sperrung * (len(text) - 1)


def schreibe(draw, text, font, sperrung, mitte_x, y, farbe):
    breite = gesperrt(draw, text, font, sperrung)
    x = mitte_x - breite / 2
    for c in text:
        draw.text((x, y), c, font=font, fill=farbe)
        x += draw.textlength(c, font=font) + sperrung


def main():
    roh, ziel = sys.argv[1], sys.argv[2]
    im = Image.open(roh).convert("RGB")
    feld = freies_feld(im)
    ys = sorted(feld)
    oben, unten = ys[0], ys[-1]
    mitte_y = (oben + unten) / 2
    mitte_x = sum(feld[int(mitte_y)]) / 2
    draw = ImageDraw.Draw(im)

    for gross in range(64, 20, -2):
        klein = max(14, int(gross * 0.42))
        ft = ImageFont.truetype(SERIF, gross)
        fu = ImageFont.truetype(SERIF, klein)
        zeilen = ([(t, ft, gross * SPERRUNG, gross * 1.30) for t in TITEL]
                  + [(None, None, 0, gross * 0.75)]
                  + [(u, fu, klein * SPERRUNG, klein * 1.45) for u in UNTERTITEL]
                  + [("", None, 0, klein * 1.1)]
                  + [(AUTOR, fu, klein * SPERRUNG, klein * 1.45)])
        hoehe = sum(z[3] for z in zeilen)
        y = mitte_y - hoehe / 2
        passt = y > oben + RAND and y + hoehe < unten - RAND
        if passt:
            pruef_y = y
            for text, font, sp, zh in zeilen:
                if text:
                    b = gesperrt(draw, text, font, sp)
                    if b > breite_bei(feld, int(pruef_y), int(zh)) - 2 * RAND:
                        passt = False
                        break
                pruef_y += zh
        if passt:
            break

    y = mitte_y - hoehe / 2
    for text, font, sp, zh in zeilen:
        if text == "":
            pass                       # nur Abstand, keine Linie
        elif text is None:
            linie = gross * 1.1
            mitte_zeile = y + zh / 2
            draw.line([(mitte_x - linie, mitte_zeile), (mitte_x + linie, mitte_zeile)],
                      fill=FARBE, width=max(1, gross // 32))
        else:
            schreibe(draw, text, font, sp, mitte_x, y, FARBE)
        y += zh

    im.save(ziel)
    print("%s geschrieben, Titelgroesse %d px" % (ziel, gross))


if __name__ == "__main__":
    main()
