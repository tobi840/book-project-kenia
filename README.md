# Kenia-Vorlesebuch: Kapitel-Pipeline

Rund 100 Kapitel, Reise 24.09. bis 12.10.2026, Fertigstellungstermin 23.09.2026.
Dieses Repo enthält die Arbeitsfassungen der Prompts, die deterministischen
Prüfskripte und die erzeugten Kapitel.

## Der Ablauf pro Kapitel

| # | Schritt | Wer | Was passiert |
|---|---------|-----|--------------|
| 1 | Substanz-Check | Sonnet 5 | Research-Doc aus Drive holen, nach `research/` spiegeln, messen: Zeichen, belegte Zahlen, URLs, offene Lücken. Urteil: trägt das Doc ein volles Kapitel oder ist es dünn? |
| 2 | Schreiben | Opus | Kapitel nach `prompts/P3-kapitel-schreiben.md` als HTML, danach Selbstprüfung gegen `scripts/regel_check.py`, höchstens zwei Runden |
| 3 | Regel-Check | Skript | `scripts/regel_check.py`, zählt Längen, Absätze, Sätze, Zeichen, Struktur, Lücken |
| 4 | QS | Sonnet 5 | Fünf Prüfungen nach `prompts/P4-qs.md`, sieht nur Kapitel, Research-Doc und Styleguide, ändert nichts |
| 5 | Linkcheck | Skript | `scripts/check_links.py --offline`, Herkunft jeder URL gegen das Research-Doc. Erreichbarkeit erst im gesammelten Lauf vor dem Satz |
| 6 | Gesamtampel | Workflow | rechnet Regel-Check, QS und Linkcheck zusammen |
| 7 | Korrigieren | Opus | nur bei gelb oder rot, nur die gemeldeten Fundstellen, eine Runde |
| 8 | Re-QS | Sonnet 5 | prüft die Korrektur nach, setzt die finale Ampel |

Der Schreiber sieht seine eigene Prüfung nie: Opus schreibt, Sonnet 5 prüft.
Was sich zählen lässt, zählt ein Skript und kein Modell.

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

### Zwei Sorten Marker

| Marker | Bedeutung | Ampel |
|--------|-----------|-------|
| `[[LÜCKE: …]]` | Pflichtfeld des Templates unbelegt | gelb |
| `[[OFFEN: …]]` | das Research-Doc selbst weist die Angabe als nicht belegbar aus | keine |

Der Unterschied ist der Grund, warum nicht jedes Kapitel gelb wird. Ein
Research-Doc, das eine Angabe ehrlich offenlässt, ist kein Mangel des Kapitels.
Ein Pflichtfeld ohne Beleg schon. Eine Seitenzahl gehört in keinen Marker, dort
steht `(S. XX)` bis zum Satz.

`[[OFFEN]]` ist seit dem 18.09.2026 ein Endzustand. Es gibt keine Nachrecherche
mehr, die diese Marker später auflöst. Sie halten fest, wo die Quellenlage endet.

### Nicht ampelrelevant

Die Erreichbarkeit der Links. Nachrangig, kein Gate vor dem Satz (E14). Ein
gesammelter Lauf kann sie irgendwann prüfen, muss aber nicht. Pro Kapitel wird nur
geprüft, ob jede URL wörtlich im Research-Doc steht. Das fängt den Fehlertyp ab,
den wir selbst verursachen.

## Querverweise

Entstehen nicht beim Schreiben. Wer nur sein eigenes Kapitel kennt, nimmt den
schwächsten verfügbaren Zusammenhang: im Pilot zeigten drei von fünf Verweisen
auf dasselbe Kapitel, zwei begründeten sich mit „wächst auch in Nairobi".

Stattdessen ein eigener Durchlauf, wenn alle Kapitel stehen: 20 bis 30 Verweise
auf 100 Kapitel, kein Kapitel häufiger als zweimal Ziel, der Zusammenhang muss
sachlich sein (derselbe Mechanismus, dasselbe Molekül, dieselbe Geschichte,
derselbe Konflikt). Ein gemeinsamer Ort reicht nicht.

## Längenzonen (Geschichte)

| Wörter | Zone |
|--------|------|
| unter 600 | rot, harte Untergrenze, kein Kapitel |
| 600 bis 699 | gelb bei dünnem Research, sonst rot |
| 700 bis 899 | gelb, zulässig bei dünnem Research |
| 900 bis 1.500 | grün, Norm |
| 1.500 bis 1.800 | gelb, kürzen |
| über 1.800 | rot |

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
              namen-bedeutungen.md (einzige erlaubte Nachrecherche)
chapters/     {nr}-{slug}.html, das Ergebnis
qs/           {nr}-{slug}.md, die Fundstellenlisten
berichte/     Pilotbericht und was daraus für P3 und P4 folgt
scripts/      regel_check.py, check_links.py
```

## Bekannte Einschränkung

Die Egress-Policy dieser Umgebung sperrt allgemeine Web-Hosts. Die
Erreichbarkeitsprüfung in `check_links.py` meldet solche Links als
`nicht-pruefbar`, nicht als tot. Die Herkunftsprüfung (steht die URL wörtlich im
Research-Doc?) läuft offline und fängt den Fehlertyp ab, den wir selbst
verursachen: eine erfundene oder umgeschriebene Adresse.

Ob die vom Deep Research gelieferten URLs live erreichbar sind, bleibt damit offen.
Das ist hingenommen (E14). In jeder QS-Ausgabe steht dazu einmal ein Satz, nicht
einmal pro Link. Im Pilot stand derselbe Satz 25 mal in den Fundstellenlisten.

Dieselbe Sperre hat die Namensrecherche daran gehindert, eine Quelle im Original zu
lesen. Beleg war dort der Ausschnitt aus der Suchtrefferliste. Was das wert ist und
was nicht, steht in `research/namen-bedeutungen.md`.
