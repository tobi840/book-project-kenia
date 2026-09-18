# P4: QS pro Kapitel

Lokale Arbeitsfassung des Drive-Prompts "P4_QS pro Kapitel", Stand 18.09.2026 nach dem zweiten Prozessdurchgang.

**Höchstens zwei Runden je Kapitel (E22), und Runde 2 gibt es nur, wenn Runde 1 rot war (E24).** Was Runde 1 bei grüner Ampel nicht findet, steht im Buch. Das ist eine bewusste Entscheidung von Tobi zugunsten von Tempo: 95 Kapitel in fünf Tagen. Dritte Runden gibt es nicht mehr.

**Ausgabe sind Patches, keine Prosa.** Die Patches wendet ein Skript an, kein Modell. Damit fällt der Korrekturschritt aus der Kette, und mit ihm die Stelle, an der im Pilot jeder Folgefehler entstanden ist (E20).

## Auftrag

Prüfe das Kapitel `{NR}_{TRIVIALNAME}` gegen sein Research-Doc. **Ändere nichts am Text.** Du schreibst dieses Kapitel nicht und hast es nicht geschrieben.

## Die Skriptausgabe steht in deinem Auftrag

Du rufst **kein Skript auf** und durchsuchst das Repo nicht. Du liest genau drei
Dateien: das Research-Doc, das Kapitel und diesen Prompt. Alles andere kostet
Tokens, die das Projekt nicht hat.

`regel_check.py` und `research_check.py` sind vorher einmal gelaufen. Ihre
Ausgabe steht wörtlich in deinem Auftrag. Was dort steht, prüfst du **nicht noch
einmal von Hand**. Du prüfst ihre Verdachtsfälle nach und machst daraus Patches
oder verwirfst sie.

Die Skripte decken ab: Längen, Absätze, Satzlängen, Gedankenstriche, verbotene Wörter, Dreierketten, Marker, Kopfzeilenformat, Struktur, Zahlen ohne Beleg im Doc, Alltagsvergleiche ohne Beleg, lateinische Namen (erfunden oder aufrecht), und Aufzählungen, deren Quellsatz ein Vorbehaltswort trägt.

`check_links.py` gibt es nicht mehr, weil es keine Links mehr gibt (E21).

**Deine Zeit gehört dem, was kein Skript kann.**

## Prüfung 1: Fakten gegen das Research-Doc

Das ist die Prüfung, für die es dich gibt. Sie bekommt fast deine ganze Aufmerksamkeit.

Jede Behauptung des Kapitels gegen das Doc. Kategorien:

- `FALSCH`: steht anders im Research-Doc
- `UNBELEGT`: steht gar nicht im Research-Doc
- `STATUSFEHLER`: Überliefertes als gesichert dargestellt oder umgekehrt
- `VERZERRT`: Zahl stimmt, Kontext verschiebt die Bedeutung

Vier Typen sind bisher am häufigsten durchgerutscht:

- **Zuspitzung.** Der Text ist stärker als seine Quelle. "Primär in der Rinde" wurde zu "nicht im Holz, nicht in den Blättern". Eine Aufzählung mit "darunter" wurde zu einer abgeschlossenen Liste. Das ist `VERZERRT`, bei abgeschlossenen Listen `FALSCH`. 19 von 30 Befunden der ersten Runde waren von dieser Art. Das Skript findet die Aufzählungen ab zwei Kommas. Dreierlisten mit nur einem Komma und die zugespitzten Einzelsätze findest nur du.
- **Nachzählbare Zahlen.** Kapitel 003 behauptete "sieben Sprachen, zusammen zehn Wörter". Es waren acht und elf. Zwei volle Runden haben das übersehen, weil niemand nachgezählt hat. **Wenn das Kapitel etwas zählt, zähl es im Doc nach.**
- **Erklärungen von Fachbegriffen.** Jede Umschreibung ist eine Tatsachenbehauptung. "AFLP vergleicht die Länge vervielfältigter Bruchstücke des Erbguts" ist eine, und sie stand in keinem Doc. Ein Kürzel auszuschreiben ist keine Erklärung.
- **Wörtliche Bedeutungen lokaler Namen.** Nur zulässig aus dem Research-Doc oder aus `research/namen-bedeutungen.md` mit Status `belegt`. Alles Abgeleitete ist `UNBELEGT`, auch wenn es plausibel klingt. Die Datei ist seit dem 18.09.2026 geschlossen (E12).

## Prüfung 2: was die Skripte nicht messen können

Vier Punkte, mehr nicht:

- **Ende-Check.** Kehrt der letzte Absatz zum Anfangsbild zurück? Kein Fazit, keine Moral, kein Allgemeinplatz.
- **Tempus.** Präsens für Biologie, Präteritum für Geschichte. Auch bei Inversion: nicht "Aufgedeckt hat das X", sondern "Das deckte X auf".
- **Wiederholt "Menschen und Kultur" den Block 1**, statt ihn zu ergänzen?
- **Vorlesbarkeit**, aber nur, wo es wirklich stolpert: Schachtelsätze über drei Ebenen, Zahlenreihen ohne Pause. Zischlaute meldest du nicht. Im Pilot wurde wegen drei sch-Lauten ein Satz über Polizeigewalt umgebaut, und beim Umbauen entstehen Faktenfehler.

Rechtschreibung und Zeichensetzung meldest du nur, wenn du wirklich einen Fehler siehst. Such nicht danach.

## Ausgabe

Datei `qs/{nr}-{slug}.md`. **Zwei Teile, sonst nichts (E23).**

Das QS-Dokument ist Arbeitsmaterial für ein Skript, nicht für Tobi. Er soll davon höchstens den zweiten Teil lesen müssen, und der ist im Normalfall leer. Jede Zeile, die weder Patch noch Entscheidungsvorlage ist, kostet ihn Lesezeit und bringt nichts.

**Verboten sind:** eine Ampelzeile, eine Zusammenfassung der Skriptausgaben, Sätze der Form "alles Übrige geprüft, keine Abweichung", ein Bericht über Prüfung 2 ohne Befund, Lob, eine Inhaltsangabe des Kapitels, Vorschläge über die Fundstellen hinaus. Nichts davon wird gelesen.

### 1. Der Patch-Block

Genau ein Codeblock, ausgezeichnet als `patch`. Eine Zeile je Patch, Felder durch **Tabulator** getrennt:

```patch
STREICHEN	exakter Wortlaut aus dem Kapitel
ERSETZEN	exakter Wortlaut aus dem Kapitel	neuer Wortlaut
```

Keine Fundstellenliste daneben. Wenn du erklären musst, warum ein Patch nötig ist, gehört er in Teil 2.

Fünf harte Regeln für jeden Patch:

1. **Der zitierte Wortlaut muss zeichengenau und genau einmal im Kapitel vorkommen.** Kopier ihn, tipp ihn nicht ab. Kommt er zweimal vor, nimm mehr Kontext dazu, bis er eindeutig ist.
2. **Ein Ersatz darf nur streichen oder wörtlich aus dem Research-Doc übernehmen.** Er darf nicht umformulieren. Das ist die Kernregel: jeder Fehler, der im Pilot nach dem Erstentwurf entstanden ist, entstand beim Umformulieren, keiner beim Streichen.
3. **Erlaubt sind genau drei Formen von Ersatz:**
   - der alte Wortlaut ohne einzelne Wörter (Streichung im Satz)
   - der alte Wortlaut plus ein Vorbehaltswort, das im Quellsatz des Docs steht
   - eine Wortfolge, die wörtlich im Research-Doc steht
   Alles andere lehnt das Patch-Skript ab.
4. **Ein Vorbehaltswort gehört an die Stelle, an der es im Quellsatz steht.** Das Doc schreibt "insbesondere in Frankreich und Spanien". Dann heißt der Patch "Insbesondere in Frankreich und Spanien wurde er", nicht "wurde er dadurch insbesondere". Das Skript prüft nur, **ob** das Wort dazugekommen ist, nicht **wo**. An der falschen Stelle schwächt es das falsche Satzglied ab und der Satz behauptet etwas Neues.
5. **Im Zweifel STREICHEN.** Ein Satz weniger ist ein Kapitel ohne diesen Fehler. Ein umformulierter Satz ist ein Kapitel mit einem neuen, den niemand mehr sucht.

Kursivsetzungen sind der einzige Fall, in dem du HTML in den Ersatz schreibst: `ERSETZEN\tdie Gattung Prunus\tdie Gattung <em>Prunus</em>`.

### 2. Für Tobi

Überschrift `## Für Tobi`. Darunter höchstens **fünf Zeilen**. Eine Zeile je Punkt, Form: Kategorie, Fundstelle in wenigen Wörtern, was er entscheiden muss.

Hierher gehört nur zweierlei:

- was eine Entscheidung von ihm braucht
- was ein `FALSCH` ist und sich weder streichen noch wörtlich ersetzen lässt

Gibt es nichts davon, schreibst du unter die Überschrift genau ein Wort: `Nichts.`

Das ist der Normalfall und ein gutes Ergebnis.

## Die Datei ist das Ergebnis, nicht dein Bericht

Du gibst zwei Felder zurück, `ampel` und `anzahl_patches`. Das ist die
Steuergröße für die Frage, ob eine zweite Runde nötig ist, und sonst nichts.
Gewertet wird `qs/{nr}-{slug}.md`, und nur die Datei geht in
`patch_anwenden.py`. Widerspricht deine Rückgabe deiner Datei, gilt die Datei.

Eine Ampelzeile **in** der Datei gibt es nicht (E23).

Das ist keine Formalie. In Runde 3 hat ein Prüfer vier Patches und ein
`UNBELEGT` in seine Datei geschrieben und in derselben Antwort "grün, null
Patches" zurückgemeldet. Wer dem Bericht geglaubt hätte, hätte den echten
Fehler verloren. Auf 95 Kapitel wäre das ein stiller Ausfall.

## Bei der zweiten Runde

Die zweite Runde ist die letzte (E22) und findet nur statt, wenn die erste rot
war (E24). Sie ist **keine Abhakliste**: sie prüft Prüfung 1 mit derselben Tiefe wie die erste, weil ein Patch etwas verschoben haben kann. Im Pilot sind in 2 von 5 Kapiteln beim Korrigieren neue Fehler entstanden, damals noch durch ein Modell, das umformulieren durfte.

Umgesetzte Punkte erwähnst du nicht. Das Kapitel ist der Beleg.

## Was gegenüber Drive geändert ist

- Fünf Prüfungen wurden zwei. Was sich zählen lässt, zählt ein Skript (E20).
- Ausgabe sind Patches, kein Fließtext. Der Korrekturschritt entfällt.
- Prüfer und Schreiber sind verschiedene Modelle mit getrenntem Kontext.
- Höchstens zwei Runden (E22), QS-Dokument auf Patches plus fünf Zeilen (E23).
- Der Link-Block ist gestrichen (E21). Kein `check_links.py`, keine Ampelzeile zur Erreichbarkeit.
- Längenzonen gesenkt, Norm 800 bis 1.300 (E18).

## Entscheidungsstand

- E1: `[[LÜCKE]]` färbt gelb.
- E2 und E3: Körpermaße und Erklärungen sind Prüfung 1, nicht Stil.
- E4: `VERZERRT` färbt gelb.
- E6 bis E9: Seitenzahl, Kopfzeilenformat, Sprachbezeichnung Maa, Kursivsetzung.
- E10 und E14: durch E21 gegenstandslos.
- E11 und E12: keine Nachrecherche mehr, weder Fotografie noch Namensbedeutungen.
- E13: höchstens drei lokale Namen im Fließtext, fehlende Namen sind kein Mangel.
- E15: `[[OFFEN]]` abgeschafft.
- E16: kein Alltagsvergleich ohne wörtlichen Beleg.
- E17: Vorbehaltswörter wandern mit, und zwar an ihre Stelle im Quellsatz.
- E18: Norm 800 bis 1.300 Wörter.
- E19: durch E21 gegenstandslos.
- E20: Patches statt Prosa, kein Korrekturmodell.
- E21: Block "Weiterlesen und Sehen" gestrichen.
- E22: höchstens zwei QS-Runden, angestrebt eine.
- E23: QS-Dokument ist Patch-Block plus höchstens fünf Zeilen für Tobi.
- E24: Runde 2 nur bei roter Runde 1. Der Prüfer ruft keine Skripte auf, liest
  nur drei Dateien und gibt zwei Felder zurück. Läuft als Sonnet mit Effort
  `low`.
- Querverweise: eigener Durchlauf am Ende, im Kapitel unerwünscht.
