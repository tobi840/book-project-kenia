# Kenia-Vorlesebuch: Kapitel-Pipeline

Rund 100 Kapitel, Reise 24.09. bis 12.10.2026, Fertigstellungstermin 23.09.2026.
Dieses Repo enthält die Arbeitsfassungen der Prompts, die deterministischen
Prüfskripte und die erzeugten Kapitel.

## Der Ablauf pro Kapitel

Seit dem 18.09.2026 fünf Schritte statt acht (E20). Der Korrekturschritt ist
weggefallen, weil ein Skript die Patches anwendet.

| # | Schritt | Wer | Was passiert |
|---|---------|-----|--------------|
| 1 | Substanz-Check | Sonnet 5 | Research-Doc aus Drive holen, nach `research/` spiegeln, messen: Zeichen, belegte Zahlen, URLs. Urteil: trägt das Doc ein volles Kapitel oder ist es dünn? |
| 2 | Schreiben | Opus | Kapitel nach `prompts/P3-kapitel-schreiben.md` als HTML, danach Selbstprüfung gegen die Skripte, höchstens zwei Runden |
| 3 | Skripte | Skript | `regel_check.py` (zählt), `research_check.py` (liest gegen das Research-Doc). Kostenlos, deterministisch, sofort |
| 4 | QS | Sonnet 5 | Zwei Prüfungen nach `prompts/P4-qs.md`, sieht Kapitel und Research-Doc, ändert nichts. Ausgabe sind **Patches**, keine Prosa |
| 5 | Patch | Skript | `patch_anwenden.py` wendet an, was die drei Patch-Regeln besteht, und lehnt jede Umformulierung ab |

Der Schreiber sieht seine eigene Prüfung nie: Opus schreibt, Sonnet 5 prüft.
Was sich zählen lässt, zählt ein Skript und kein Modell.

**Höchstens zwei QS-Runden je Kapitel, angestrebt ist eine (E22).** Was die
zweite Runde nicht findet, bleibt im Buch. Das ist eine bewusste Entscheidung
zugunsten von Tempo: 95 Kapitel in fünf Tagen bei bewusst etwas niedrigerer
Qualität pro Kapitel. Runde 3 im Pilot fand noch ein echtes `FALSCH`, also
kostet die Regel etwas. Sie wurde trotzdem so gesetzt.

**Das QS-Dokument ist Patch-Block plus höchstens fünf Zeilen (E23).** Es ist
Arbeitsmaterial für `patch_anwenden.py`, nicht für Tobi. Im Normalfall steht
unter `## Für Tobi` genau ein Wort: `Nichts.`

### Die QS-Datei ist die Wahrheit, nicht die Rückmeldung des Prüfers

`patch_anwenden.py` liest `qs/{nr}-{slug}.md`. Was ein QS-Lauf sonst noch über
sich selbst meldet, Ampel, Zahl der Patches, Zusammenfassung, ist nicht
maßgeblich und darf nie als Gate dienen.

In Runde 3 hat ein Prüfer vier Patches und ein `UNBELEGT` in seine Datei
geschrieben und gleichzeitig "grün, null Patches" gemeldet. Ein Automat, der
der Meldung folgt statt der Datei, hätte den Fehler verloren, ohne dass es
jemand bemerkt. Über 95 Kapitel ist das der teuerste denkbare Ausfall, weil er
lautlos ist.

### Warum der Korrekturschritt weg ist

Im Pilot sind in 2 von 5 Kapiteln beim Korrigieren neue Fehler entstanden, in
einem weiteren ein neuer unbelegter Satz, der erst in der dritten Runde auffiel.
Jeder dieser Fehler entstand beim **Umformulieren**. Keiner beim Streichen.

Also formuliert nichts mehr um. Ein Patch darf nur streichen, wörtlich aus dem
Research-Doc übernehmen oder ein Vorbehaltswort ergänzen. `patch_anwenden.py`
prüft das mechanisch und lehnt alles andere ab.

## Die drei Prüfskripte

| Skript | Braucht | Findet |
|--------|---------|--------|
| `regel_check.py` | nur das Kapitel | Längen, Absätze, Satzlängen, Gedankenstriche, verbotene Wörter, Dreierketten, Marker, Kopfzeilenformat, Struktur |
| `research_check.py` | Kapitel und Research-Doc | Zahlen ohne Beleg, Alltagsvergleiche ohne Beleg, lateinische Namen (erfunden oder aufrecht), Aufzählungen ohne das Vorbehaltswort der Quelle |

`research_check.py` ist am 18.09.2026 dazugekommen. Der Grund: der Regel-Check
zählt nur, er liest nicht gegen die Quelle, und hat darum fünf von fünf
Pilotkapiteln grün gemeldet, von denen drei faktisch rot waren. Am fertig
korrigierten Pilot fand das neue Skript in Sekunden drei Fehler, die zwei
vollständige QS-Runden übersehen hatten.

Seine Befunde sind **Verdachtsfälle, keine Urteile**. Etwa jeder dritte ist ein
Fehlalarm. Das ist der Preis dafür, dass er nichts kostet.

## Gesamtampel

Rechnet der Workflow aus, nicht ein Modell.

- **rot**: mindestens ein `FALSCH` in QS-Prüfung 1, oder eine erfundene URL, oder
  ein fehlender Block, oder die harte Längenuntergrenze unterschritten, oder ein
  Gedankenstrich
- **gelb**: `UNBELEGT`, `STATUSFEHLER` oder `VERZERRT` in Prüfung 1, gelbe
  Befunde im Regel-Check, gelbe Längenzone, offene `[[LÜCKE]]`-Marker
- **grün**: nichts davon

Grün heißt: geht ohne Tobi weiter. Gelb und rot landen im Entscheidungsstapel,
der einmal am Tag gebündelt vorgelegt wird, nicht kapitelweise.

### Nur noch ein Marker

| Marker | Bedeutung | Ampel |
|--------|-----------|-------|
| `[[LÜCKE: …]]` | Pflichtfeld des Templates unbelegt | gelb |

`[[OFFEN]]` ist seit E15 abgeschafft. Was das Research-Doc als nicht belegbar
ausweist, steht im Kapitel gar nicht, auch nicht als Marker.

Der Marker hatte zwei Abnehmer: die gesammelte Nachrecherche und den
Entscheidungsstapel. Die Nachrecherche ist seit E11 und E12 eingestellt,
ampelrelevant war er nie. Im Pilot standen fünfzehn davon in fünf Kapiteln, einer
lautete „typische fotografische Fehler, vom Research-Doc als nicht thematisiert
ausgewiesen". Niemand wird das je bearbeiten. Geschrieben, geprüft, aufgelistet,
nachgeprüft und am Ende von Hand gelöscht wird es trotzdem.

Wenn das Doc eine Frage offen lässt, hat das Kapitel diese Frage nicht. Eine
Seitenzahl gehört ohnehin in keinen Marker, dort steht `(S. XX)` bis zum Satz.

### Nicht mehr vorhanden

Der Block "Weiterlesen und Sehen" und mit ihm jede Link-Prüfung (E21,
Entscheidung Tobi vom 18.09.2026). Wer nachschlagen will, googelt, Vogelrufe
laufen über eBird und Merlin. Die Quellen bleiben im Research-Doc, sie stehen nur
nicht mehr im Buch.

Damit fallen weg: `check_links.py`, der nie gelaufene Erreichbarkeitslauf, die
Ampelzeile dazu in jedem QS-Dokument, und die erfundene URL als häufigste
Einzelfehlerquelle der Kette.

## Querverweise

Entstehen nicht beim Schreiben. Wer nur sein eigenes Kapitel kennt, nimmt den
schwächsten verfügbaren Zusammenhang: im Pilot zeigten drei von fünf Verweisen
auf dasselbe Kapitel, zwei begründeten sich mit „wächst auch in Nairobi".

Stattdessen ein eigener Durchlauf, wenn alle Kapitel stehen: 20 bis 30 Verweise
auf 100 Kapitel, kein Kapitel häufiger als zweimal Ziel, der Zusammenhang muss
sachlich sein (derselbe Mechanismus, dasselbe Molekül, dieselbe Geschichte,
derselbe Konflikt). Ein gemeinsamer Ort reicht nicht.

## Längenzonen (Geschichte)

Gesenkt am 18.09.2026 (E18).

| Wörter | Zone |
|--------|------|
| unter 550 | rot, harte Untergrenze, kein Kapitel |
| 550 bis 649 | gelb bei dünnem Research, sonst rot |
| 650 bis 799 | gelb, zulässig bei dünnem Research |
| 800 bis 1.300 | grün, Norm |
| 1.300 bis 1.600 | gelb, kürzen |
| über 1.600 | rot |

Die Absenkung spart nicht am Buch, sondern am Fehler. Jeder zusätzliche Satz ist
eine zusätzliche Behauptung, die gegen das Research-Doc stimmen muss. Drori liegt
bei 700 bis 900 Wörtern. Die alte Untergrenze von 900 hat Texte ins Auffüllen
getrieben, und aufgefüllt wird mit dem, was nicht belegt ist. Über 100 Kapitel
gerechnet sind das rund 15.000 Wörter weniger und entsprechend weniger Prüfarbeit.

## Nachrecherche

Findet nicht statt. Weder für Namensbedeutungen noch für die Fotografie
(E11, E12, 18.09.2026).

Die Namensrecherche lief einmal und wurde eingestellt: ein brauchbares Ergebnis aus
sechzehn Namen, bei 31 Agenten Aufwand. Was sie fand, steht als geschlossener Vermerk
in `research/namen-bedeutungen.md` und gilt weiter. Neues kommt nicht dazu.

Die eine Regel, die bleibt: **kein Modell leitet eine Namensbedeutung selbst ab**,
nicht aus dem Wortstamm, nicht aus einer Nachbarsprache, nicht aus einem Präfix.
Eine Bedeutung steht im Research-Doc oder im Vermerk oder gar nicht im Kapitel.

## Lokale Namen im Kapitel

Die Namenszeile trägt die vollständige Liste, der Fließtext höchstens drei Namen (E13).
Aufgenommen wird, woran etwas hängt: eine belegte Bedeutung, eine Zuordnungsfrage, ein
Gebrauch, der im Kapitel wiederkommt. Der Rest darf als Zahl auftauchen, nicht als
Aufzählung.

Im Pilot stand jeder Name zweimal im selben Kapitel, einmal in der Zeile und einmal
ausgeschrieben im Text. Kapitel 004 zählte so vierzehn Namen auf. Vorgelesen ist das
eine Litanei. Fehlt für eine Sprache ein Name, ist das kein Mangel und kein Marker.

## Verzeichnisse

```
styleguide/   Text-Styleguide V2 und Kapitel-Template (HTML)
prompts/      Arbeitsfassungen von P3 (Schreiben) und P4 (QS)
research/     Spiegel der Deep-Research-Docs aus Drive, Substanz-Messung,
              namen-bedeutungen.md (geschlossener Vermerk, E12)
chapters/     {nr}-{slug}.html, das Ergebnis
qs/           {nr}-{slug}.md, Ampel plus Patch-Block
berichte/     Pilotbericht, Re-QS und der Prozessdurchgang
scripts/      regel_check.py, research_check.py, patch_anwenden.py
```

## Bekannte Einschränkung

Die Egress-Policy dieser Umgebung sperrt allgemeine Web-Hosts. Für die Kapitel
spielt das seit E21 keine Rolle mehr, weil dort keine URLs mehr stehen.

Dieselbe Sperre hat die Namensrecherche daran gehindert, eine Quelle im Original zu
lesen. Beleg war dort der Ausschnitt aus der Suchtrefferliste. Was das wert ist und
was nicht, steht in `research/namen-bedeutungen.md`.
