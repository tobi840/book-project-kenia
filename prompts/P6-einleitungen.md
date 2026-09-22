# P6: Allgemeine Einleitung und Abschnittseinleitungen

Nachgetragen am 22.09.2026. Es gab bis dahin keine Arbeitsfassung, nur den
Vermerk „Einleitungen (P6a)" in `berichte/UEBERGABE-028-100.md`. Die Längen und
der Zuschnitt stehen so, wie Tobi sie am 22.09.2026 vorgegeben hat.

## Was entsteht

| Datei | Umfang | Inhalt |
|-------|--------|--------|
| `einleitungen/00-einleitung.html` | 1.200 bis 1.500 Wörter | Das ganze Land: warum so viele Arten, wie der Graben entstand, welche Jahreszeit die Reise trifft, wie Naturschutz heute organisiert ist, wer die Namen vergeben hat |
| `einleitungen/0N-{slug}.html` | 400 bis 600 Wörter, etwas darüber ist zulässig | Je ein Abschnitt für die fünf Landschaften, in der Reihenfolge des Buches |

Die fünf Abschnitte und ihre Kapitelzahl:

| Nr | Abschnitt | Kapitel |
|----|-----------|---------|
| 01 | Nairobi und Umgebung | 17 |
| 02 | Rift Valley: Naivasha, Nakuru, Baringo | 24 |
| 03 | Laikipia und Mount Kenya | 22 |
| 04 | Die Küste bei Mombasa | 16 |
| 05 | Tsavo und Amboseli | 21 |

## Quelle

**Genau eine: `research/landschaften.txt`.** Das ist der Spiegel des
Deep-Research-Docs „XXX-2026-09-Book@Kenia-Detail-Research-LANDSCHAFTEN".
Abschnitt 1 trägt die allgemeine Einleitung, die Abschnitte 2 bis 6 je eine
Landschaft, Abschnitt 7 die Vergleichsmatrix.

Dazu `chapters.tsv` für die Kapitelzahl je Abschnitt. Sonst nichts. Keine
Kapitel lesen, keine Nachrecherche, kein Modellwissen (E11, E12).

## Regeln

Es gelten `styleguide/01-text-styleguide.md` und `README.md` unverändert, mit
drei Abweichungen:

1. **Keine Blöcke.** Eine Einleitung hat keine Kopfzeile mit lokalen Namen,
   kein „Menschen und Kultur", kein „Vor der Linse", keine Illustration.
2. **Keine Art steht im Mittelpunkt.** Arten kommen vor, aber als Beispiel für
   die Landschaft, nicht als Thema. Wer eine Art ausbreitet, nimmt dem Kapitel
   die Pointe weg.
3. **Keine Vorwegnahme.** Die Einleitung darf nicht erzählen, was ein Kapitel
   erzählt. Sie stellt den Raum auf, in dem die Kapitel spielen.

Sonst gilt alles: vier Bewegungen statt Katalog, Verben tragen den Satz, Status
jeder Aussage markieren, Zahlen nur mit Beleg, kein erfundener Alltagsvergleich
(E16), Vorbehaltswörter wandern mit (E17), **keine Gedankenstriche**, jeder
lateinische Name kursiv, Ende als Bild und nicht als Fazit.

Der erste Satz bleibt unter 25 Wörtern. Absätze 80 bis 180 Wörter, keiner über
200. Der letzte Absatz unter 80 Wörtern.

## Der Zuschnitt einer Abschnittseinleitung

Das Research-Doc gliedert jede Landschaft in acht Unterabschnitte. Sie sind
Material, keine Gliederung. Vier Bewegungen, wie beim Kapitel:

1. **Woran man diese Landschaft erkennt.** Ein Bild, kein Katalog. Das Doc
   liefert es in „Unterscheidungsmerkmale" und „Sinneseindrücke".
2. **Wie sie entstanden ist.** Geologie, Wasser, Boden. Nur so viel, wie den
   Rest erklärt.
3. **Wer darin lebt.** Die prägenden Lebensgemeinschaften, als Zusammenhang
   erzählt, nicht als Artenliste.
4. **Menschen.** Nutzung, Konflikt, eine belegte Geschichte aus dem Doc.

Dazu ein Absatz zur Phänologie Ende September bis Anfang Oktober, denn genau
dann sind wir dort. Er gehört an den Schluss der Bewegung 3 oder vor die
Bewegung 4, je nachdem, was besser trägt.

## Format

```html
<!--
typ: einleitung
abschnitt: 02
titel: Rift Valley
kapitel: 24
quelle: research/landschaften.txt
status: entwurf
-->
<article class="einleitung" data-abschnitt="02">
  <header class="einleitung-kopf">
    <p class="abschnitt-nr">Abschnitt 2</p>
    <h1>Rift Valley</h1>
    <p class="untertitel">Naivasha, Nakuru, Baringo</p>
  </header>
  <p>…</p>
</article>
```

Die allgemeine Einleitung trägt `abschnitt: 00`, `data-abschnitt="00"` und
keine `abschnitt-nr`.

## Prüfung

`regel_check.py` prüft gegen die Kapitelstruktur und passt hier nicht. Geprüft
wird von Hand auf: Gedankenstrich, Wortzahl, Absatzlänge, erster und letzter
Satz, jede Zahl gegen `research/landschaften.txt`. Eine QS-Runde mit Agenten
findet nicht statt, die Quelle ist eine einzige Datei und liegt vor.
