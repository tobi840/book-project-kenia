# QS Kapitel 001 – Heilige Würgefeige (Mugumo), Runde 3

## Ampel

**Gelb.** Zwei VERZERRT-Befunde in Prüfung 1 (E17, Vorbehaltswort fehlt), kein FALSCH, kein UNBELEGT, kein STATUSFEHLER.

Erreichbarkeit: gesammelter Lauf steht aus.

Konvergenz: Alle Befunde der Vorrunde (drei FALSCH bei gekürzten Aufzählungen: Pilzfolgen, Wirkstoffgruppen, Stilbenwirkungen; ein UNBELEGT bei „Handelswörter") sind im aktuellen Text behoben, geprüft, kein Rückfall. `research_check.py` meldete 2 Verdachtsfälle, beide bestätigt (0 Fehlalarme). `regel_check.py` meldete 1 Verdachtsfall, geprüft und verworfen (unten).

## Fakten gegen das Research-Doc

- „bis zu 21 Arten in ein und demselben Sykonium" | VERZERRT | Quellsatz trägt „verschiedene" (bis zu 21 verschiedene Arten), Kapitelsatz nicht (E17).
- „tragen im Gegenzug die Samen in die nächste Astgabel" | VERZERRT | Doc: Fledermäuse „fungieren im Gegenzug als **primäre** Vektoren für die Samenverbreitung". Kapitel lässt das Vorbehaltswort weg und macht aus dem primären den alleinigen Vektor (E17).
- „Ficus" (zweites Vorkommen, aufrecht) | Kursivsetzung (E9) | Erstes Vorkommen „Ficus thonningii" korrekt kursiv, das isolierte „Ficus" im Etymologie-Satz steht aufrecht in Anführungszeichen. Gleiches Wort, uneinheitlich gesetzt.

Alles Weitere im Fließtext erneut gegen das Doc gelesen (Thika-Maße, Blume/Thonning, Wuchshöhe, Sykoniengröße, Wespenmechanismus, 50/28/19/2-Stichprobe, Phänologie, Höhenlage/Niederschlag, Mugo-wa-Kibiru-Prophezeiung, Waiyaki-Way-Fall 2020, Futter-/Medizinnutzung, IUCN-Status, alle vier Links): keine weitere Abweichung gefunden.

## Patch-Block

```patch
ERSETZEN	„Ficus“	„<em>Ficus</em>“
ERSETZEN	bis zu 21 Arten in ein und demselben Sykonium	bis zu 21 verschiedene Arten in ein und demselben Sykonium
ERSETZEN	Fledermäuse hängen obligatorisch von den Feigen ab und tragen im Gegenzug die Samen in die nächste Astgabel.	Fledermäuse hängen obligatorisch von den Feigen ab und tragen im Gegenzug primär die Samen in die nächste Astgabel.
```

## Was nicht als Patch geht

- Adjektivkette „entzündungshemmend, schmerzstillend, antioxidativ und antimikrobiell" (regel_check-Verdacht) | kein Patch, kein Fehler | Vierkette entspricht wörtlich der vierteiligen Liste im Research-Doc; die Vorrunde hatte hier ein fehlendes Glied als FALSCH korrigiert. Kürzen würde diesen bereits behobenen Fehler wieder einführen. Reine Stilfrage, keine Aufzählung mit Vorbehaltswort im Quellsatz.
