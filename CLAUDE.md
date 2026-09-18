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
- Messwerte: QS-Runde 3 im Pilot 178k je Kapitel. Kapitel 006 mit Dateisuche und
  Skriptaufrufen 102k. Kapitel 007 mit fester Dateiliste, 6 Tool-Uses: 111k.
  Kapitel 008 mit allem in einer vorbereiteten Datei, 2 Tool-Uses: 106k.

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
2. **Mehrere Kapitel je Prüfer.** Der Bodenpreis fällt einmal an, die Nutzlast
   skaliert linear. Bei drei Kapiteln je Prüferlauf rund 45k je Kapitel.
   Gegenrechnung: Ein Prüfer mit drei Kapiteln im Kopf findet im dritten
   vermutlich weniger als im ersten. Beim ersten Batch messen.
3. ~~Konnektoren aus.~~ **Getestet und widerlegt.** Tobi hat Slack, Gmail,
   Agicap, Miro, Kalender und BigQuery abgeschaltet, 135 Werkzeuge weniger.
   Die Nullmessung danach: **63.153 Tokens**, also nichts gespart. Der Grund
   ist, dass abgelegte Werkzeuge nur als Namensliste im Kontext stehen, ein
   paar Tausend Tokens für alle zusammen. Der Boden steckt woanders:
   Systemprompt, Skill-Katalog, CLAUDE.md.

**Damit sind zwei von drei Hypothesen widerlegt.** Die Rundenzahl war es nicht
(5 Prozent), der Werkzeugkatalog war es auch nicht (0 Prozent). Der Bodenpreis
von rund 60k je Subagent ist von innen nicht zu senken. Übrig bleibt die
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
