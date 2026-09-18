# Korrekturlauf 001 bis 005

18.09.2026. Ein Durchgang über alle fünf Pilotkapitel, mit den Entscheidungen
E1 bis E10 und der Querverweis-Regel. Kein neuer QS-Lauf: Schreiber und Prüfer
sind verschiedene Modelle, die Nachprüfung steht aus.

## Was geändert wurde

**Querverweise, alle fünf.** Die fünf `<p class="querverweis">` sind raus. Drei
zeigten auf dasselbe Kapitel, zwei begründeten sich mit einem gemeinsamen Ort.
Verweise setzt ein eigener Durchlauf, wenn alle Kapitel stehen.

**Erfundene Körpermaße, 001 und 004.** Vier Vergleiche gestrichen, keiner stand
im Research-Doc:

| Kapitel | raus | Grund |
|---|---|---|
| 001 | „kleiner als eine Fingerkuppe" (2x) | Doc führt nur 15 Fuß, 14,35 m Umfang, „vier Stockwerke" |
| 004 | „eine Armlänge quer durch das Holz" | Doc: „Durchmesser, die oft einen Meter überschreiten", kein Vergleich |
| 004 | „erbsengroß" | Doc: „etwa 10 mm im Durchmesser", kein Vergleich |

Das Schlussbild von 001 hing an einem davon und heißt jetzt: „In einer Kugel von
höchstens 14 Millimetern wohnt eine Belegschaft."

**Unbelegte Erklärungen, 001 und 003.**

- 001: die Glosse „also Arbeiten zur Verwandtschaft der Arten" ist raus. Der
  Fachbegriff davor auch, der Satz beginnt jetzt direkt mit „Arbeiten zur
  Verwandtschaft der Arten". Kein Jargon, keine Erklärung, nichts erfunden.
- 003: „und vergleicht die Länge vervielfältigter Bruchstücke des Erbguts" ist
  raus. Das Kürzel auszuschreiben bleibt, das steht im Doc.

**Kopfzeilen, 003, 004, 005.** `Maasai:` zu `Maa:` in der Namenszeile und in den
Metadaten (im Fließtext bleibt „bei den Maasai", dort sind Menschen gemeint).
Die englischen und deutschen Handelsnamen sind aus 003 und 005 raus.

**Kursivsetzung, alle fünf.** 17 Stellen standen aufrecht, 8 im Fließtext und 9 in
den Linklisten, zusammen 12 verschiedene Artnamen: *Elisabethiella stuckenbergi*, *Alfonsiella
brongersmai*, *Podocarpus falcatus*, *Taxus falcata*, *Afrocarpus gracilior*,
*Afrocarpus falcatus*, *Plasmodium falciparum*, *Warburgia ugandensis*, *Pygeum
africanum*, *Mirasolia diversifolia*, *Prunus africana*, *Tithonia diversifolia*.
Aufrecht bleibt „Malaria tropica", das ist ein Krankheitsname, kein Artname.

**Marker, alle fünf.** 25 Marker geprüft, jeder einzeln gegen den Abschnitt „Was
nicht belegt werden konnte" seines Research-Docs:

- 23 sind `[[OFFEN]]` geworden: das Doc weist die Angabe selbst als nicht
  belegbar aus. Jeder Marker sagt jetzt dazu, wo das steht.
- 1 ist mit dem Querverweis verschwunden (die fehlende Seitenzahl in 004).
- 1 war schlicht falsch: 004 meldete „Tageszeit nicht spezifiziert", das Doc sagt
  „bei tief stehender Sonne", und genau das steht auch im Kapitel.

Es bleibt **keine einzige `[[LÜCKE]]`** über alle fünf Kapitel.

**Namensbedeutung, 005.** „Maruru" heißt im Kikuyu die Bitteren. Beide blinden
Läufe der Namensrecherche kamen unabhängig auf dieselbe Quelle. Steht jetzt im
Kapitel, mitsamt den gleichbedeutenden Namen der Nachbarsprachen.

## Was der Regel-Check danach sagt

| Kapitel | Ampel | Wörter | LÜCKE | OFFEN | Kursivverdacht |
|---|---|---|---|---|---|
| 001 | grün | 1.059 | 0 | 3 | 0 |
| 002 | grün | 1.095 | 0 | 3 | 0 |
| 003 | grün | 943 | 0 | 8 | 0 |
| 004 | grün | 1.044 | 0 | 4 | 0 |
| 005 | grün | 1.101 | 0 | 5 | 0 |

Alle fünf in der Normzone 900 bis 1.500. Linkcheck: 26 Links, 0 außerhalb des
Research-Docs, 0 erfunden. Erreichbarkeit: gesammelter Lauf steht aus.

Vor dem Lauf waren alle fünf gelb, alle aus demselben Grund. Das war der Befund,
der E1 ausgelöst hat.

## Zwei Korrekturen am Prüfskript

- `[[OFFEN]]` wurde bei Wort- und Satzlänge mitgezählt. Ein Marker ist keine
  Prosa und wird nicht vorgelesen. 004 war dadurch gelb wegen eines „Satzes" mit
  67 Wörtern, der zur Hälfte aus einem Marker bestand.
- Neue Liste `KEIN_ARTNAME` für lateinische Wortpaare, die keine Artnamen sind
  (Malaria tropica, Diabetes mellitus, Delirium tremens). Die Kursiv-Heuristik
  ließ sie sonst als Befund stehen.

## Was offen bleibt

- **Re-QS.** Der Korrekturlauf hat im Pilot in 2 von 5 Kapiteln neue Fehler
  gebaut. Dieser hier ist ungeprüft. Der Status der Kapitel steht auf
  `korrigiert`, die Ampel auf `re-qs ausstehend`.
- **Namensrecherche.** 9 von 11 Sprachgruppen fehlen, der Lauf ist am Spend-Limit
  abgebrochen. Details in `research/namen-bedeutungen.md`.
- **Erreichbarkeit der 26 Links.** Braucht eine Umgebung mit offenem Netz.
- **E5, zweite Hälfte.** Die gesammelte Nachrecherche zur Fotografie
  (Fluchtdistanz, Tageszeit, Phänologie im Reisefenster) ist nicht entschieden.
  7 der 23 offenen Punkte hängen daran.
