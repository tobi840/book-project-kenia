# Prozessdurchgang 18.09.2026: wo gekürzt wird

Auftrag: einmal durch den ganzen Ablauf gehen, Tokens pro Kapitel senken, die
Ersterstellung richtiger machen, Komplexität aus den Texten nehmen. 100 Kapitel
bleiben 100.

## Der Befund, der alles andere erklärt

**Der Styleguide hat den Schreiber zu genau den Fehlern angewiesen, die die QS
danach gefunden hat.** Drei Stellen, alle seit heute repariert:

| Stelle im Styleguide | Wortlaut | Erzeugte Fehlerklasse | Befunde im Pilot |
|---|---|---|---|
| Abschnitt 1, Körpermaße | "Regel: Jede wichtige Zahl bekommt ein Körpermaß daneben oder wird durch eines ersetzt." | erfundene Alltagsvergleiche | 6 |
| Abschnitt 3, Wörter als Fundstücke | "Wir übernehmen das doppelt: lateinische Wortherkunft plus Swahili-, Maa- oder Kikuyu-Name mit wörtlicher Bedeutung." | abgeleitete Namensbedeutungen | 4 |
| Abschnitt 7, letzter Punkt | "Einzige Ausnahme vom Nachrecherche-Verbot: die wörtliche Bedeutung lokaler Namen" | seit E12 schlicht falsch | (Regelwiderspruch) |

P3 verbot beides, der Styleguide verlangte es, und der Styleguide formulierte es
als "Regel". Der Schreiber liest beide. Zehn Befunde des Piloten stammen aus
einer Anweisung, die wir selbst geschrieben haben.

Das ist die Antwort auf die Frage, ob sich in der Ersterstellung etwas verbessern
lässt: ja, und es kostet nichts. Ein Widerspruch im Regelwerk kostet je Kapitel
einen QS-Befund, eine Korrekturrunde und eine Nachprüfung, hundertmal.

## Was geschnitten wird

### E15: `[[OFFEN]]` ist abgeschafft

Der Marker hatte zwei Abnehmer: die gesammelte Nachrecherche und den
Entscheidungsstapel. Die Nachrecherche ist seit E11 und E12 eingestellt,
ampelrelevant war der Marker nie. Damit hat er null Abnehmer.

Im Pilot standen fünfzehn davon in fünf Kapiteln. Einer lautete "typische
fotografische Fehler und artspezifische Verschlusszeiten, vom Research-Doc als
nicht thematisiert ausgewiesen". Bezahlt wurde er fünfmal: beim Schreiben, im
Regel-Check, in der QS-Liste, in der Nachprüfung und beim Löschen vor dem Satz.

Neue Regel: Was das Research-Doc nicht hergibt, steht nicht im Kapitel. Fehlt die
Fluchtdistanz, steht in "Vor der Linse" nichts über Fluchtdistanz. Das ist kein
Mangel, sondern ein kürzerer Text.

Ausnahme: eine Zuordnungsfrage, die den Text trägt (ob „Mueri" und „Muiri"
dasselbe Wort sind), gehört als Satz in den Fließtext, mit Status "ungeklärt".
Als Sprache, nicht als Marker.

### E16: kein Alltagsvergleich ohne wörtlichen Beleg

Sechs erfundene Vergleiche in fünf Kapiteln, drei davon haben zwei vollständige
QS-Runden überlebt: "mannshoch", "wie mit dem Daumennagel eingedrückt", "zwei
Meter höher". Keiner stand in einer Quelle, alle drei klangen gut.

Dieselbe Logik wie bei den Namen: eine Anforderung, die das Research-Doc
regelmäßig nicht erfüllen kann, erzeugt Erfindung statt Lücke. Also fällt die
Anforderung weg, nicht die Sorgfalt.

### E18: Längenzonen gesenkt, Norm 800 bis 1.300

Vorher 900 bis 1.500. Die alte Untergrenze hat Texte ins Auffüllen getrieben, und
aufgefüllt wird mit dem, was nicht belegt ist. Drori liegt bei 700 bis 900.

Über 100 Kapitel sind das rund 15.000 Wörter weniger, entsprechend weniger
Behauptungen, die stimmen müssen, und entsprechend weniger Prüfarbeit. Nebenbei
löst es das Problem, dass Kapitel 003 nach der Namenskürzung sechs Wörter über
der alten grünen Linie lag.

### E19: 3 bis 4 Links statt 3 bis 6

Erfundene URLs sind laut P4 der häufigste Einzelfehlertyp. Jede zusätzliche URL
ist eine zusätzliche Gelegenheit dazu und eine zusätzliche Zeile Prüfarbeit. Zwei
Links weniger je Kapitel sind 200 Links weniger im Buch.

### E20: die QS liefert Patches, das Korrekturmodell fällt weg

Der größte Schnitt. Bisher: QS schreibt Prosa, ein Korrekturmodell liest die
Prosa und baut den Text um. **Jeder Fehler, der im Pilot nach dem Erstentwurf
entstanden ist, entstand in diesem Schritt, und zwar immer beim Umformulieren.
Keiner beim Streichen.**

Neu: die QS liefert einen Patch-Block. Zwei Aktionen, Tabulator-getrennt:

```patch
STREICHEN	exakter Wortlaut aus dem Kapitel
ERSETZEN	exakter Wortlaut	neuer Wortlaut
```

`scripts/patch_anwenden.py` wendet an und prüft dabei mechanisch drei Regeln:
der zitierte Wortlaut muss genau einmal vorkommen, und ein Ersatz darf nur
streichen, wörtlich aus dem Research-Doc übernehmen oder ein Vorbehaltswort
ergänzen. Alles andere wird abgelehnt und gemeldet.

Damit ist die Umformulierung nicht mehr verboten, sondern unmöglich.

## Was dazukommt, weil es Fehler verhindert statt findet

### E17: Vorbehaltswörter wandern mit

Zuspitzung war mit 19 von 30 Befunden die mit Abstand größte Fehlerklasse. Die
bisherige Regel lautete "spitze nicht zu". Die kann man nicht befolgen, weil man
beim Schreiben nicht sieht, welcher Satz zugespitzt ist.

Die neue Regel ist die positive Fassung: steht im Quellsatz "darunter", "vor
allem", "primär", "überwiegend", "meist", "verschiedene", "typischerweise" oder
"insbesondere", steht in deinem Satz auch eins. Das sieht man.

### `scripts/research_check.py`

Der Regel-Check zählt nur, er liest nicht gegen die Quelle. Deshalb hat er fünf
von fünf Pilotkapiteln grün gemeldet, von denen drei faktisch rot waren.

Das neue Skript liest gegen das Research-Doc und findet vier Klassen: Zahlen, die
dort nicht vorkommen; Alltagsvergleiche ohne Beleg; lateinische Namen, erfunden
oder aufrecht; Aufzählungen, deren Quellsatz ein Vorbehaltswort trägt und der
Kapitelsatz nicht.

**Am fertig korrigierten Pilot, nach zwei vollständigen QS-Runden, fand es in
Sekunden drei echte Fehler:**

1. 002: das Doc schreibt "Die **primäre** Pollenübertragung erfolgt durch Wind,
   Vögel, Insekten und kletternde Säugetiere", das Kapitel schreibt "Den Pollen
   tragen Wind, Vögel, Insekten und kletternde Säugetiere". Ein Wort weg, aus
   einer Hauptursache eine vollständige Liste.
2. 005: das Doc schreibt "**typischerweise** mit 3 bis 7 Lappen", das Kapitel
   schreibt "tragen drei bis sieben Lappen".
3. 005: "im Höchstfall so hoch wie ein einstöckiges Gebäude" steht in keiner
   Quelle. Das war meine eigene Korrektur aus der Re-QS-Runde, eingesetzt als
   Ersatz für das ebenfalls erfundene "mannshoch".

Dazu vier aufrechte Taxa (*Ficus*, *Prunus*, *Pygeum*, *Tithonia*) und eine
Viererkette aus Adjektiven, alle ebenfalls durch zwei QS-Runden gelaufen.

Genauigkeit etwa zwei von drei. Der Rest sind Fehlalarme, die eine QS in einem
Satz verwirft. Der Lauf kostet nichts und dauert eine Sekunde.

## Der neue Ablauf

| # | Schritt | Wer | Kosten |
|---|---------|-----|--------|
| 1 | Substanz-Check | Sonnet 5 | klein |
| 2 | Schreiben | Opus | groß |
| 3 | drei Skripte | Skript | null |
| 4 | QS mit Patch-Ausgabe | Sonnet 5 | mittel |
| 5 | Patch anwenden | Skript | null |

Acht Schritte werden fünf. Weggefallen sind Korrigieren und Re-QS pro Kapitel.
Die Nachprüfung läuft nur noch auf Stichprobe.

## Rechnung

Gemessen: die Re-QS-Runde kostete 969.818 Tokens für fünf Kapitel, also rund
194.000 je Kapitel für **einen** QS-Durchgang. Der alte Ablauf hatte zwei davon
plus eine Korrekturrunde.

Geschätzt, nicht gemessen:

| | alt | neu |
|---|---|---|
| Schreiben | ~150k | ~120k (kürzere Texte) |
| Skripte | 0 | 0 |
| QS | ~194k | ~120k (kürzerer Prompt, kürzere Ausgabe) |
| Korrigieren | ~100k | 0 |
| Re-QS | ~194k | ~40k (nur Stichprobe) |
| **je Kapitel** | **~640k** | **~280k** |
| **95 Kapitel** | **~61M** | **~27M** |

Die Ausgabelänge ist der größte einzelne Hebel: im Pilot waren drei von fünf
QS-Dokumenten länger als das Kapitel, das sie prüfen. P4 deckelt sie jetzt auf
400 Wörter plus Patch-Block.

## Was bewusst nicht geschnitten wurde

- **Der Block "Menschen und Kultur"**, 150 bis 250 Wörter je Kapitel. Er ist
  streichbar und würde 20.000 Wörter sparen. Das ist eine Buchentscheidung, keine
  Prozessentscheidung, und gehört Tobi.
- **Die Trennung Schreiber und Prüfer.** Ein Modell, das sich selbst prüft, ist
  billiger und blind. Die drei Fehler oben zeigen, dass schon zwei getrennte
  Läufe nicht reichen.
- **Der Substanz-Check.** Kostet wenig und entscheidet, ob ein dünnes Doc
  überhaupt in die Schreibphase geht.

## Was offen bleibt

Fertigstellungstermin ist der 23.09.2026, heute ist der 18.09. Das sind fünf Tage
für 95 Kapitel, also 19 pro Tag. Der Prozess ist jetzt so schlank, wie er ohne
Qualitätsverlust wird. Die Rechnung geht damit rechnerisch auf, aber ohne
Spielraum für eine zweite Runde.

Dazu kommt: das Wochenlimit des Accounts läuft erst am 21.09. um 4 Uhr UTC zurück.
