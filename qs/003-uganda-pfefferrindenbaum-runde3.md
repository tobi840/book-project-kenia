# QS Kapitel 003: Uganda-Pfefferrindenbaum, Runde 3

Research-Doc: research/003-uganda-pfefferrindenbaum.txt
Kapiteldatei: chapters/003-uganda-pfefferrindenbaum.html

## Ampel

**Prüfung 1 (Fakten): rot.** Ein Fund FALSCH, ein Fund VERZERRT, kein UNBELEGT, kein STATUSFEHLER.

Erreichbarkeit: gesammelter Lauf steht aus.

Skript-Ergebnisse (übernommen): `regel_check.py` grün, 0 rot, 0 gelb, Geschichte 906 Wörter, 4 Links. `research_check.py`: 0 Befunde, also 0 zu prüfende Verdachtsfälle und 0 Fehlalarme in diesem Lauf. `check_links.py --offline`: 4 Links, 0 nicht im Doc, 0 tot.

## Prüfung 1: Fakten

1. „sieben Sprachen, zusammen zehn Wörter, und übersetzt ist keines davon“ | FALSCH | Research-Doc Abschnitt 1 führt zusätzlich zu Swahili, Kikuyu, Maa (Olsokonoi/ol-mororoi), Nandi, Luganda, Luhya und Sukuma noch eine achte Sprache mit gesichertem Namen: „mhw / Makokothi [gesichert]2“. Die Zahlen sieben und zehn treffen nicht zu, es sind acht Sprachen mit gesichertem Namen und elf Wörter (vor dem separat behandelten „Soroko“). Da keine belegte Ersatzzahl wörtlich im Doc steht, wird gestrichen statt neu gezählt.

2. „Isoliert und strukturell beschrieben sind Muzigadial, Warburganal und das Driman-Sesquiterpenoid Ugandenial A“ | VERZERRT (E17) | Research-Doc: „Zu den **primären** isolierten und strukturell charakterisierten Molekülen dieses Typs zählen Muzigadial, Warburganal sowie das Driman-Sesquiterpenoid Ugandenial A“. Das Vorbehaltswort „primär“ fehlt im Kapitelsatz, aus einer möglicherweise nicht abschließenden Auswahl wird eine geschlossene Liste. `research_check.py` fängt das nicht ab, weil der Satz nur ein Komma trägt, seine Aufzählungsheuristik verlangt zwei.

Alle übrigen Zahlen, Statusmarkierungen, Namen und Links wurden gegen das Doc geprüft und stimmen überein, einschließlich der bereits in Runde 2 korrigierten Stellen (Malaria nur Kenia, „etwa bei Hacken“, „darunter“ vor den Beschwerden, *Trigona* durchgehend kursiv).

## Prüfung 2

Ende-Check: letzter Absatz kehrt zum Kau-/Geschmacksbild des Anfangs zurück, kein Fazit. Tempus: Wissenschaftsgeschichte durchgehend Präteritum, Biologie Präsens, konsistent. „Menschen und Kultur“ ergänzt Block 1, keine Wiederholung. Vorlesbarkeit unauffällig, ein Rätselsatz mit sofortiger Auflösung. E13: genau drei lokale Namen im Fließtext (Mũthĩga, Soroko, Muthiga), Grenze eingehalten.

```patch
STREICHEN	sieben Sprachen, zusammen zehn Wörter, und 
STREICHEN	elftes 
ERSETZEN	Isoliert und strukturell beschrieben sind Muzigadial, Warburganal und das Driman-Sesquiterpenoid Ugandenial A.	Isoliert und strukturell beschrieben sind primär Muzigadial, Warburganal und das Driman-Sesquiterpenoid Ugandenial A.
```

## Was nicht als Patch geht

- Die richtige Zahl für die Sprachen/Wörter-Stelle (acht Sprachen, elf Wörter) steht in keiner Formulierung wörtlich im Research-Doc und wäre eine Umformulierung, keine Streichung oder wörtliche Übernahme. Ob die Zeile mit korrekter Zahl neu geschrieben oder so knapp bleibt, ist eine Entscheidung von Tobi.
