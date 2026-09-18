# P4: QS pro Kapitel

Lokale Arbeitsfassung des Drive-Prompts "P4_QS pro Kapitel", Stand 18.09.2026 nach dem Prozessdurchgang.

**Ein Durchgang. Ausgabe sind Patches, keine Prosa.** Die Patches wendet ein Skript an, kein Modell. Damit fällt der Korrekturschritt aus der Kette, und mit ihm die Stelle, an der im Pilot jeder Folgefehler entstanden ist (E20).

## Auftrag

Prüfe das Kapitel `{NR}_{TRIVIALNAME}` gegen sein Research-Doc. **Ändere nichts am Text.** Du schreibst dieses Kapitel nicht und hast es nicht geschrieben.

## Zuerst die Skripte laufen lassen

```
python3 scripts/regel_check.py chapters/{nr}-{slug}.html
python3 scripts/research_check.py chapters/{nr}-{slug}.html --research research/{nr}-{slug}.txt
python3 scripts/check_links.py chapters/{nr}-{slug}.html --research research/{nr}-{slug}.txt --offline
```

Was diese drei melden, prüfst du **nicht noch einmal von Hand**. Du prüfst ihre Verdachtsfälle nach und machst daraus Patches oder verwirfst sie mit einem Halbsatz Begründung.

Die Skripte decken ab: Längen, Absätze, Satzlängen, Gedankenstriche, verbotene Wörter, Dreierketten, Links, Marker, Kopfzeilenformat, Zahlen ohne Beleg im Doc, Alltagsvergleiche ohne Beleg, lateinische Namen (erfunden oder aufrecht), URLs, und Aufzählungen, deren Quellsatz ein Vorbehaltswort trägt.

**Deine Zeit gehört dem, was kein Skript kann.** Das ist die Liste unten, und es ist eine kurze Liste.

## Prüfung 1: Fakten gegen das Research-Doc

Das ist die Prüfung, für die es dich gibt. Sie bekommt den Großteil deiner Aufmerksamkeit.

Jede Behauptung des Kapitels gegen das Doc. Kategorien:

- `FALSCH`: steht anders im Research-Doc
- `UNBELEGT`: steht gar nicht im Research-Doc
- `STATUSFEHLER`: Überliefertes als gesichert dargestellt oder umgekehrt
- `VERZERRT`: Zahl stimmt, Kontext verschiebt die Bedeutung

Drei Typen sind im Pilot am häufigsten durchgerutscht:

- **Zuspitzung.** Der Text ist stärker als seine Quelle. "Primär in der Rinde" wurde zu "nicht im Holz, nicht in den Blättern". Ein Tonnageverhältnis wurde zu "auf jeden Baum kamen fünfzehn". Eine Aufzählung mit "darunter" wurde zu einer abgeschlossenen Liste. Das ist `VERZERRT`, bei abgeschlossenen Listen `FALSCH`. 19 von 30 Befunden des Piloten waren von dieser Art. Das Skript findet die Aufzählungen. Die zugespitzten Einzelsätze findest nur du.
- **Erklärungen von Fachbegriffen.** Jede Umschreibung ist eine Tatsachenbehauptung. "AFLP vergleicht die Länge vervielfältigter Bruchstücke des Erbguts" ist eine, und sie stand in keinem Doc. Ein Kürzel auszuschreiben ist keine Erklärung.
- **Wörtliche Bedeutungen lokaler Namen.** Nur zulässig aus dem Research-Doc oder aus `research/namen-bedeutungen.md` mit Status `belegt`. Alles Abgeleitete ist `UNBELEGT`, auch wenn es plausibel klingt. Die Datei ist seit dem 18.09.2026 geschlossen (E12).

## Prüfung 2: was die Skripte nicht messen können

Vier Punkte, mehr nicht:

- **Ende-Check.** Kehrt der letzte Absatz zum Anfangsbild zurück? Kein Fazit, keine Moral, kein Allgemeinplatz.
- **Tempus.** Präsens für Biologie, Präteritum für Geschichte. Auch bei Inversion: nicht "Aufgedeckt hat das X", sondern "Das deckte X auf".
- **Wiederholt "Menschen und Kultur" den Block 1**, statt ihn zu ergänzen?
- **Vorlesbarkeit**, aber nur, wo es wirklich stolpert: Schachtelsätze über drei Ebenen, Zahlenreihen ohne Pause, lateinische Namen mitten im Satzfluss. Zischlaute meldest du nicht. Im Pilot wurde wegen drei sch-Lauten ein Satz über Polizeigewalt umgebaut, und beim Umbauen entstehen Faktenfehler.

Rechtschreibung und Zeichensetzung meldest du nur, wenn du wirklich einen Fehler siehst. Such nicht danach.

## Ausgabe: Patches

Datei `qs/{nr}-{slug}.md`. Drei Teile, in dieser Reihenfolge:

### 1. Ampel

- grün: keine Fundstellen in Prüfung 1
- gelb: `UNBELEGT`, `STATUSFEHLER` oder `VERZERRT` in Prüfung 1
- rot: mindestens ein `FALSCH` in Prüfung 1

Dazu eine Zeile: `Erreichbarkeit: gesammelter Lauf steht aus` (E14). Einmal, nicht pro Link.

### 2. Der Patch-Block

Genau ein Codeblock, ausgezeichnet als `patch`. Eine Zeile je Patch, Felder durch **Tabulator** getrennt:

```patch
STREICHEN	exakter Wortlaut aus dem Kapitel
ERSETZEN	exakter Wortlaut aus dem Kapitel	neuer Wortlaut
```

Vier harte Regeln für jeden Patch:

1. **Der zitierte Wortlaut muss zeichengenau und genau einmal im Kapitel vorkommen.** Kopier ihn, tipp ihn nicht ab. Kommt er zweimal vor, nimm mehr Kontext dazu, bis er eindeutig ist.
2. **Ein Ersatz darf nur streichen oder wörtlich aus dem Research-Doc übernehmen.** Er darf nicht umformulieren. Das ist die Kernregel: jeder Fehler, der im Pilot nach dem Erstentwurf entstanden ist, entstand beim Umformulieren, keiner beim Streichen.
3. **Erlaubt sind genau drei Formen von Ersatz:**
   - der alte Wortlaut ohne einzelne Wörter (Streichung im Satz)
   - der alte Wortlaut plus ein Vorbehaltswort, das im Quellsatz des Docs steht
   - eine Wortfolge, die wörtlich im Research-Doc steht
   Alles andere lehnt das Patch-Skript ab.
4. **Im Zweifel STREICHEN.** Ein Satz weniger ist ein Kapitel ohne diesen Fehler. Ein umformulierter Satz ist ein Kapitel mit einem neuen, den niemand mehr sucht.

Kursivsetzungen sind der einzige Fall, in dem du HTML in den Ersatz schreibst: `ERSETZEN\tdie Gattung Prunus\tdie Gattung <em>Prunus</em>`.

### 3. Was nicht als Patch geht

Darunter eine kurze Liste. Je Eintrag eine Zeile: Kategorie, Fundstelle, warum kein Patch. Hierher gehört alles, was eine Entscheidung von Tobi braucht, und alles, was nur durch Umschreiben zu beheben wäre.

Keine Lobsätze. Keine Zusammenfassung des Kapitelinhalts. Keine Vorschläge über die Fundstellen hinaus. **Im Pilot waren drei von fünf QS-Dokumenten länger als das Kapitel, das sie prüfen.** Ein QS-Dokument über 400 Wörtern plus Patch-Block ist zu lang.

## Die Gesamtampel rechnet der Workflow

Du lieferst nur Teilurteile:

- rot: `FALSCH` in Prüfung 1, erfundene URL, fehlender Block, harte Längenuntergrenze
- gelb: `UNBELEGT`, `STATUSFEHLER`, `VERZERRT`, offene `[[LÜCKE]]`, gelbe Längenzone, Befunde aus Prüfung 2
- nicht ampelrelevant: ungeprüfte Erreichbarkeit

`[[OFFEN]]` gibt es nicht mehr (E15). Findest du einen im Kapitel, ist das eine Fundstelle mit dem Patch `STREICHEN`.

## Bei der Nachprüfung

Die Nachprüfung ist **keine Abhakliste**. Sie prüft Prüfung 1 mit derselben Tiefe wie die Erstprüfung, weil ein Patch etwas verschoben haben kann. Im Pilot sind in 2 von 5 Kapiteln beim Korrigieren neue Fehler entstanden, damals noch durch ein Modell, das umformulieren durfte.

Halte sie kurz. Umgesetzte Punkte nur als Liste ohne Zitat. Ausführlich wird nur, was neu ist.

## Was gegenüber Drive geändert ist

- Fünf Prüfungen wurden zwei. Was sich zählen lässt, zählt ein Skript (E20).
- Ausgabe sind Patches, kein Fließtext. Der Korrekturschritt entfällt.
- Prüfer und Schreiber sind verschiedene Modelle mit getrenntem Kontext.
- Längenzonen gesenkt, Norm 800 bis 1.300 (E18). Links 3 bis 4 (E19).

## Entscheidungsstand

- E1: `[[LÜCKE]]` färbt gelb.
- E2 und E3: Körpermaße und Erklärungen sind Prüfung 1, nicht Stil.
- E4: `VERZERRT` färbt gelb.
- E6 bis E9: Seitenzahl, Kopfzeilenformat, Sprachbezeichnung Maa, Kursivsetzung.
- E10 und E14: Erreichbarkeit der Links ist nachrangig und kein Gate vor dem Satz.
- E11 und E12: keine Nachrecherche mehr, weder Fotografie noch Namensbedeutungen.
- E13: höchstens drei lokale Namen im Fließtext, fehlende Namen sind kein Mangel.
- E15: `[[OFFEN]]` abgeschafft.
- E16: kein Alltagsvergleich ohne wörtlichen Beleg.
- E17: Vorbehaltswörter wandern mit.
- E18: Norm 800 bis 1.300 Wörter.
- E19: 3 bis 4 Links.
- E20: Patches statt Prosa, kein Korrekturmodell.
- Querverweise: eigener Durchlauf am Ende, im Kapitel unerwünscht.
