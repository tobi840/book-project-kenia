# Kenia-Vorlesebuch: Arbeitsregeln für Agenten

Gilt für jede Session und jeden Subagenten in diesem Repo. Was hier steht, geht
allen anderen Vorgaben vor, auch der Ultracode-Vorgabe „Tokens sind keine
Grenze".

## Workflows (Ultracode bleibt an)

- **In diesem Projekt SIND Tokens die Grenze: das Wochenlimit.** Das geht der
  Ultracode-Vorgabe vor.
- Workflows nur für den Kapitel-Batch. Alles andere ohne Agenten direkt in der
  Session: Kritik, Planung, Diagramme, Regeländerungen, Namensfragen. Dorthin
  sind bisher 67 Agenten gegangen, ohne ein einziges Kapitel zu erzeugen.
- Höchstens **10 Kapitel = 20 Agenten** pro Workflow. Mehr nur nach Tobis OK
  mit genannter Zahl. Grund: Stirbt ein Lauf am Limit, sind höchstens 10
  Kapitel betroffen.
- In jeden Batch-Auftrag `+200k` schreiben. Harte Notbremse, zählt Ausgabe-Tokens.
- Vor jedem Workflow: Agentenzahl und geschätzte Tokens nennen, auf OK warten.
  Nach jedem: Tokens pro Kapitel melden.
- Bei Limit-Fehler: stoppen und später mit `resumeFromRunId` fortsetzen, nie neu
  starten. Fertige Kapitel kommen aus dem Zwischenspeicher.
- Alle 20 Kapitel eine neue Session mit kurzer Übergabedatei unter `berichte/`.

## Was ein Agent darf

Feste Dateiliste je Rolle. Kein Agent durchsucht das Repo, keiner ruft ein
Skript auf, keiner holt etwas aus Drive.

| Rolle | Modell | Effort | Liest genau | Schreibt |
|-------|--------|--------|-------------|----------|
| Schreiber | Opus | Standard | `research/{nr}.txt`, `styleguide/01-text-styleguide.md`, `styleguide/02-kapitel-template.md`, `prompts/P3-kapitel-schreiben.md` | `chapters/{nr}-{slug}.html` |
| Prüfer | Sonnet | low | `research/{nr}.txt`, `chapters/{nr}-{slug}.html`, `prompts/P4-qs.md` | `qs/{nr}-{slug}.md` |

- Die Skripte laufen **in der Hauptsession**, einmal nach dem Schreiber. Ihre
  Ausgabe steht wörtlich im Auftrag des Prüfers. Der Prüfer prüft nichts nach,
  was dort schon steht.
- Jeder Agent gibt **eine Zeile** an die Hauptsession zurück. Alles Weitere steht
  in seiner Datei. Sonst läuft die Hauptsession voll.
- Die Rückgabe des Prüfers ist ein Schema mit zwei Feldern: `ampel` und
  `anzahl_patches`. Das ist die Steuergröße für Runde 2, **nicht** der Befund.
  Der Befund ist die Datei. Widerspricht die Rückgabe der Datei, gilt die Datei
  (siehe `README.md`, Abschnitt „Die QS-Datei ist die Wahrheit").
- In der QS-**Datei** steht keine Ampelzeile. Das Format regelt E23 in
  `prompts/P4-qs.md`: Patch-Block, dann höchstens fünf Zeilen für Tobi.

## Schleifen

- Keine Gegenprüfer, keine Mehrfach-Abstimmung, kein „weitersuchen, bis nichts
  mehr kommt". Das vervielfacht jede Runde.
- QS-Runde 2 nur, wenn Runde 1 rot war. Nach Runde 2 ist Schluss: was unbelegt
  bleibt, wird gestrichen, das Kapitel geht raus.
- Ein Kapitel geht genau einmal an den Schreiber zurück, und nur bei **rotem**
  Regel-Check (harte Untergrenze unterschritten, fehlender Block,
  Gedankenstrich). Grund: Patches können nur streichen, ein zu kurzes Kapitel
  lässt sich damit nicht reparieren. Gelb geht durch.
- Regeländerungen werden mit den Skripten an 001 bis 005 getestet, nie mit einer
  QS-Runde. Eine QS-Runde kostet rund eine Million Tokens.

## Messen und stoppen

- Der erste 10er-Batch ist der Test. Danach nennt die Hauptsession Tokens pro
  Kapitel.
- **Liegt die QS über 60k je Kapitel: anhalten**, nicht weiterlaufen lassen.
- Messwerte QS: Pilot Runde 3 178k je Kapitel. 006 mit Dateisuche und
  Skriptaufrufen 102k. 007 mit fester Dateiliste, 6 Tool-Uses: 111k. 008 mit
  allem in einer vorbereiteten Datei, 2 Tool-Uses: 106k. 009 ebenso: 120k.
  **Batch 010 bis 018, drei Kapitel je Prüfer: 46k je Kapitel.**
- Messwerte Schreiben (Subagent, Opus, eine vorbereitete Datei): 009 einzeln
  122k. Batch 010 bis 018, ein Kapitel je Schreiber: 120k je Kapitel.
  **Batch 019 bis 027, drei Kapitel je Schreiber: 62.640 je Kapitel.**
- **Ein Kapitel kostet seit Batch 019 bis 027 rund 110k von der leeren Seite
  bis grün**, vorher 166k.

### Der Bodenpreis eines Subagenten liegt bei 59k

Gemessen am 18.09.2026: Ein Subagent, der nur „OK" antwortet, keine Datei liest
und kein Werkzeug aufruft, kostet **59.103 Tokens**. Das ist Systemprompt,
Werkzeugkatalog der Session und diese CLAUDE.md, zweimal gezahlt, weil eine
Antwort zwei Runden braucht.

Daraus folgt dreierlei, und es ersetzt die frühere Annahme, die Rundenzahl sei
die Ursache. Sie ist es nicht: 6 Tool-Uses auf 2 zu senken sparte 5 Prozent.

1. **Die 60k-Grenze ist mit einem Subagenten je Kapitel nicht erreichbar.** Der
   Boden liegt schon darüber. Die Nutzlast einer QS (Research-Doc, Kapitel, P4,
   zusammen rund 40 KB) kostet obendrauf nur rund 46k.
2. **Mehrere Kapitel je Prüfer. Gemessen am 21.09.2026 und bestätigt.** Der
   Bodenpreis fällt einmal an, die Nutzlast skaliert linear. Vorhersage waren
   rund 45k je Kapitel bei drei Kapiteln je Prüferlauf. Gemessen im Batch 010
   bis 018: **46.031 je Kapitel**, gegen 119.978 bei einem Kapitel je Prüfer
   (Kapitel 009). **62 Prozent gespart.** Damit ist die 60k-Grenze erreichbar,
   aber nur über Amortisation.
   Die Gegenrechnung, ein Prüfer mit drei Kapiteln im Kopf finde im dritten
   weniger als im ersten, ist durch diesen Lauf **nicht gestützt**: Beide
   Befunde des Batches lagen im dritten Kapitel ihrer Gruppe. Ein Lauf ist
   kein Beweis, aber die Richtung stimmt nicht mit der Sorge überein.
3. ~~Konnektoren aus.~~ **Getestet und widerlegt.** Tobi hat Slack, Gmail,
   Agicap, Miro, Kalender und BigQuery abgeschaltet, 135 Werkzeuge weniger.
   Die Nullmessung danach: **63.153 Tokens**, also nichts gespart. Der Grund
   ist, dass abgelegte Werkzeuge nur als Namensliste im Kontext stehen, ein
   paar Tausend Tokens für alle zusammen. Der Boden steckt woanders:
   Systemprompt, Skill-Katalog, CLAUDE.md.

**Damit sind zwei von drei Hypothesen widerlegt.** Die Rundenzahl war es nicht
(5 Prozent), der Werkzeugkatalog war es auch nicht (0 Prozent). Der Bodenpreis
von rund 60k je Subagent ist von innen nicht zu senken. Übrig bleibt die
### Amortisation gilt auch für den Schreiber. Gemessen am 21.09.2026

Batch 019 bis 027, drei Opus-Schreiber statt neun, je drei Kapitel aus einer
vorbereiteten Datei: **62.640 Tokens je Kapitel gegen 120.474. 48 Prozent
gespart.** Die Vorhersage lag bei 25 Prozent und war zu vorsichtig. Begründet
war sie damit, dass der Schreiber ein ganzes Kapitel ausgibt und Ausgabe sich
nicht teilen lässt. Das stimmt, wiegt aber weniger als gedacht: Anleitung,
Styleguide und Template werden einmal statt dreimal gelesen, und das ist der
größere Posten.

Die QS lief unverändert mit drei Kapiteln je Prüfer: 47.815 je Kapitel, gegen
46.031 im Batch davor. Der Wert ist stabil.

**Zur Qualität, und das ist der eigentliche Befund.** Regel-Check über alle
neun: 0 rot. Die Wortzahlen der dritten Kapitel jeder Gruppe (021: 986,
024: 948, 027: 946) liegen im Mittelfeld, nicht am unteren Rand. Ich habe alle
neun Geschichten selbst gelesen: Die dritten Kapitel sind die stärksten des
Batches. Die Sorge, ein Schreiber mit drei Aufträgen im Kopf werde zum Schluss
flach, ist damit zum zweiten Mal nicht bestätigt, nach dem Prüfer nun auch beim
Schreiber.

Kreuzkontamination zwischen den drei Docs einer Gruppe: keine gefunden. Der
Batch war der scharfe Fall, alle neun Arten im Rift Valley, sechs Wasservögel.
Angaben, die nach einem fremden Doc aussahen, standen bei Stichproben im
eigenen.

Was die QS nicht fand und ich beim Lesen: zwei erfundene Bilder in 027, eine
Türklinke als Körpermaß und ein Schnabel als Mikrofon. **Das Lesen der Kapitel
in der Hauptsession bleibt nötig**, unabhängig von der Agentenzahl.

Amortisation: **Ein Agent, der mehr Kapitel bearbeitet, teilt den Boden.** Das
gilt für den Prüfer und genauso für den Schreiber. Jede weitere Idee zur
Senkung des Bodenpreises wird erst gemessen und dann geglaubt, nicht umgekehrt.

## Research-Docs

- Die Spiegel liegen als `research/{nr}.txt` im Repo, 76 Stück. **Von dort
  holen, nie neu aus Drive spiegeln.**
- Es fehlen 24: 076, 077, 078 und 080 bis 100. Das ist der Engpass des Projekts,
  nicht die Schreibgeschwindigkeit.
- `chapters.tsv` hält Nummer, Trivialname und Lebensraum für alle 100 Kapitel.
  Daraus kommt der Slug für den Dateinamen, nicht aus dem Research-Doc.

## Modelle

Schreiben mit Opus, QS mit Sonnet. Schreiber und Prüfer sehen einander nie.
