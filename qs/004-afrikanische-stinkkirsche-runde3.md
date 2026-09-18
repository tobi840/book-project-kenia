# QS 004: Afrikanische Stinkkirsche — Runde 3

## Ampel: GELB

Werkzeugausgaben (übernommen, nicht selbst gezählt): `regel_check.py` gruen, 0 rot, 0 gelb, Geschichte 1007 Woerter, 4 Links, 0 Luecken, 0 Offen. `check_links.py`: 4 Links, 0 nicht im Research-Doc, 0 tot. `research_check.py`: 2 Verdachtsfaelle, beide KURSIV ("Prunus", "Pygeum" aufrecht statt kursiv). Beide einzeln geprueft und verworfen, keine Patches: bare Gattungsnamen ohne Art-Epitheton stehen buchweit einheitlich aufrecht (so bereits in der vorigen Nachpruefung dieses Kapitels entschieden, ebenso in 003 und 005), "Pygeum" steht hier als Handelsname parallel zu "Pygeum-Extrakt" im Research-Doc, nicht als Binomen. 2 von 2 Fehlalarme.

Erreichbarkeit: gesammelter Lauf steht aus.

## Pruefung 1: Fakten gegen das Research-Doc

1. "In Frankreich und Spanien wurde er dadurch zur ersten Wahl." | VERZERRT | Research-Doc: "weshalb PAE insbesondere in Frankreich und Spanien als primaere Behandlungsform etabliert wurde" (E17). Der Quellsatz traegt "insbesondere", der Kapitelsatz kein Vorbehaltswort mehr.

Alle uebrigen Behauptungen des Kapitels satzweise gegen das Research-Doc geprueft (Geschichte, Morphologie, Pharmakologie, Oekonomie, Oekologie, Menschen und Kultur, Vor der Linse): keine weiteren FALSCH-, UNBELEGT-, STATUSFEHLER- oder VERZERRT-Befunde. Die beiden UNBELEGT-Funde der vorigen Runde (Daumennagel-Vergleich, Zwei-Meter-Hoehenangabe) sind behoben. Namenszaehlung Fliesstext (E13): Muiri, Muchorowe, Lcheni, macht drei, keine vierte.

## Pruefung 2: was Skripte nicht messen

Ende-Check: letzter Absatz kehrt zur Narbe im Karura Forest zurueck, kein Fazit, keine Moral. Tempus durchgehend korrekt (Praesens Biologie, Praeteritum Geschichte). "Menschen und Kultur" ergaenzt Block 1, wiederholt ihn nicht. Keine Vorlesbarkeits-Stolperstellen. Keine Befunde.

```patch
ERSETZEN	In Frankreich und Spanien wurde er dadurch zur ersten Wahl.	In Frankreich und Spanien wurde er dadurch insbesondere zur ersten Wahl.
```

## Was nicht als Patch geht

Keine Eintraege.
