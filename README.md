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
| 5 | Linkcheck | Skript | `scripts/check_links.py`, Herkunft jeder URL gegen das Research-Doc, Erreichbarkeit soweit das Netz es zulässt |
| 6 | Gesamtampel | Workflow | rechnet Regel-Check, QS und Linkcheck zusammen |
| 7 | Korrigieren | Opus | nur bei gelb oder rot, nur die gemeldeten Fundstellen, eine Runde |
| 8 | Re-QS | Sonnet 5 | prüft die Korrektur nach, setzt die finale Ampel |

Der Schreiber sieht seine eigene Prüfung nie: Opus schreibt, Sonnet 5 prüft.
Was sich zählen lässt, zählt ein Skript und kein Modell.

## Gesamtampel

- **rot**: mindestens ein `FALSCH` in QS-Prüfung 1, oder eine erfundene URL, oder
  ein toter Link, oder ein roter Befund im Regel-Check (fehlender Block, harte
  Längenuntergrenze unterschritten, Gedankenstrich)
- **gelb**: nur `UNBELEGT` oder `STATUSFEHLER`, gelbe Befunde im Regel-Check,
  offene `[[LÜCKE]]`-Marker
- **grün**: nichts davon

Grün heißt: geht ohne Tobi weiter. Gelb und rot landen im Entscheidungsstapel.

## Längenzonen (Geschichte)

| Wörter | Zone |
|--------|------|
| unter 600 | rot, harte Untergrenze, kein Kapitel |
| 600 bis 699 | gelb bei dünnem Research, sonst rot |
| 700 bis 899 | gelb, zulässig bei dünnem Research |
| 900 bis 1.500 | grün, Norm |
| 1.500 bis 1.800 | gelb, kürzen |
| über 1.800 | rot |

Nachrecherche läuft nie automatisch. Sie braucht die aktive Freigabe von Tobi.

## Verzeichnisse

```
styleguide/   Text-Styleguide V2 und Kapitel-Template (HTML)
prompts/      Arbeitsfassungen von P3 (Schreiben) und P4 (QS)
research/     Spiegel der Deep-Research-Docs aus Drive, plus Substanz-Messung
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
verursachen. Ob die vom Deep Research gelieferten URLs live erreichbar sind,
muss in einer Umgebung mit offenem Netz nachgeholt werden.
