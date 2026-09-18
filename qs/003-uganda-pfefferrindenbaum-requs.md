# QS Kapitel 003: Uganda-Pfefferrindenbaum, Nachprüfung nach Korrekturlauf und Namenskürzung (E13)

Research-Doc: 1C-HftgJiJucqcwcwW2KC0AmQm1ffMq_XYDHxp4QM1cs
Kapiteldatei: chapters/003-uganda-pfefferrindenbaum.html
Grundlage: research/003-uganda-pfefferrindenbaum.txt, styleguide/01-text-styleguide.md, research/namen-bedeutungen.md, prompts/P4-qs.md.
Erstprüfung, zuletzt von einem prüfenden Modell gesehen: qs/003-uganda-pfefferrindenbaum.md (Pilot, inklusive der dort schon eingebauten ersten Nachprüfung).

Seit dieser Fassung gab es zwei Durchgänge ohne prüfendes Modell: den Korrekturlauf 001 bis 005 (berichte/KORREKTURLAUF-001-005.md) und die Namenskürzung im Fließtext nach Entscheidung E13. Diese Nachprüfung arbeitet mit der vollen Tiefe der Erstprüfung, nicht nur entlang der beiden Änderungen, und prüft auch Stellen, die nie beanstandet wurden.

Erreichbarkeit: gesammelter Lauf steht aus.

## Ampel

**Ampel aus Prüfung 1: rot.** Ein Fund in der Kategorie FALSCH, ein Fund VERZERRT, kein UNBELEGT, kein STATUSFEHLER.

Werkzeug-Ergebnisse (übernommen, nicht selbst gezählt):
- `regel_check.py`: Ampel grün, 0 rot, 0 gelb. Geschichte 906 Wörter, 8 Absätze, erster Satz 14 Wörter, letzter Absatz 53 Wörter, 0 Sätze über 40 Wörter, 1 rhetorische Frage, 0 Kursiv-Verdacht, 1 Nennung des Kapitel-Artnamens im Fließtext, 6 OFFEN, 0 LÜCKE, 5 Links.
- `check_links.py`: 5 Links, 0 nicht im Research-Doc, 0 tot, 0 nicht prüfbar (alle 5 Herkunft „im-research").

## Umgesetzte Punkte, geprüft und in Ordnung

- AFLP: die unbelegte Erklärung „und vergleicht die Länge vervielfältigter Bruchstücke des Erbguts" ist raus, nur die Ausschreibung des Kürzels bleibt. Der bisher offene Punkt aus der Pilot-Nachprüfung ist damit erledigt.
- Kopfzeile: „Maasai" zu „Maa", englische und deutsche Handelsnamen aus der Namenszeile entfernt. Format durchgehend Sprache: „Name".
- Kursivsetzung der Binomen: *Warburgia ugandensis* und *Plasmodium falciparum* jetzt korrekt kursiv im Fließtext.
- Querverweis vollständig entfernt, keine Spur mehr im Kapitel.
- Marker: alle LÜCKE zu OFFEN korrigiert, zwei davon durch die Namenskürzung ganz entfallen. Die verbleibenden 6 OFFEN wurden einzeln gegen Abschnitt 10 des Research-Docs geprüft, alle korrekt zugeordnet, keiner müsste eigentlich LÜCKE sein.
- E13, Namenskürzung: Fließtext enthält jetzt genau drei Namensnennungen (Mũthĩga in zwei Schreibweisen, Soroko einmal), jede mit einem Grund nach der Regel (wiederkehrender Gebrauch bzw. Zuordnungsfrage). Die neue Zählangabe „sieben Sprachen, zusammen zehn Wörter" wurde gegen die Namenszeile nachgezählt: Swahili, Kikuyu, Maa, Nandi, Luganda, Luhya, Sukuma sind sieben Sprachen mit zusammen zehn Wörtern (1+1+2+1+3+1+1), „Soroko" korrekt als elftes, separates Wort geführt. Die Zahl stimmt.
- GBIF-Linktext weiterhin korrekt gekürzt, „und Fundpunkte der Art" bleibt draußen.

## Prüfung 1: Fakten, bei dieser Tiefe neu gefunden

1. „Getrocknete Rinde wird gekaut und der austretende Saft geschluckt, gegen Verstopfung, Magenschmerzen, Zahnschmerzen, Husten, Fieber, Muskel- und Gliederschmerzen." | FALSCH | Text listet sechs Beschwerden als abschließende Aufzählung mit „gegen" | Research-Doc, Abschnitt 5: „um ein breites Spektrum an Leiden zu behandeln, darunter Verstopfung, Magenschmerzen, Zahnschmerzen, Husten, Fieber, Muskelschmerzen und allgemeine Gliederschmerzen [gesichert]9." Das Doc markiert die Liste mit „darunter" ausdrücklich als Ausschnitt aus einem „breiten Spektrum", also offen. Im Kapitel wird daraus eine geschlossene Liste, genau das in P4 benannte Fehlermuster („Aufzählung mit darunter wird zu abgeschlossener Liste, bei abgeschlossenen Listen FALSCH"). Nicht neu durch Korrektur oder Kürzung: der Satz steht schon im allerersten Entwurf so da und wurde von keinem bisherigen Durchlauf gemeldet.

2. „mit dem Handwerker Werkzeugstiele in den Metallfassungen von Hacken festsetzen" | VERZERRT | Hacken erscheinen als alleiniger Verwendungszweck des Harzleims | Research-Doc, Abschnitt 5: „Handwerker verwenden es, um Werkzeugstiele (etwa bei landwirtschaftlichen Hacken) in Metallfassungen zu fixieren [gesichert]9." Das Doc nennt Hacken als ein Beispiel („etwa"), der Kapitelsatz lässt das Beispielhafte weg. Nicht neu, seit dem Entwurf unverändert.

Alle übrigen Zahlen, Daten, Statusmarkierungen und Namen im Kapitel wurden erneut einzeln gegen das Research-Doc geprüft (Maße und Standortwerte, Toxizitätswerte samt Status umstritten, AFLP-Zahlen, Stecklingsversuche, Publikationsdaten, alle lokalen Namen samt der neuen Zählangabe, alle fünf Links) und stimmen überein.

## Prüfung 2 bis 4

Keine neuen Befunde. Stil, Vorlesbarkeit und Struktur wie in der Erstprüfung bewertet bzw. durch den Korrekturlauf korrigiert: keine Gedankenstriche, keine verbotenen Wörter, keine Adjektivketten, Längen durchgehend grün, letzter Absatz kehrt zum Anfangsbild zurück, alle fünf Blöcke vorhanden, kein Querverweis, Links vollständig und im Research-Doc belegt.

## Prüfung 5: Sprachrichtigkeit, neu gefunden

1. Die Gattung *Trigona* (Bestäuber) steht an allen vier Stellen im Kapitel aufrecht statt kursiv: „Bienen der Gattung Trigona" (Geschichte), „die bestäubenden Trigona-Bienen" (Vor der Linse, Wo und wann), „Eine Trigona-Biene" (Vor der Linse, Bild-Idee) und „eine Trigona-Biene sammelt" (Illustrations-Figcaption). Der Styleguide verlangt Kursivsetzung auch für Bestäuber. Der Korrekturlauf hat genau diese Fehlerklasse bearbeitet (17 Stellen, 12 Artnamen), einwortige Gattungsnamen ohne Artepitheton aber nicht erfasst, ebenso wenig wie die automatische Kursiv-Heuristik in `regel_check.py`, die auf zweiteilige Gattung-Art-Muster zielt. Nicht neu durch Korrektur oder Kürzung: seit dem Entwurf unverändert und von keinem bisherigen Durchlauf gemeldet, auch nicht vom auf Kursivsetzung spezialisierten Korrekturlauf.

Tempus weiterhin konsistent (Präteritum für die Wissenschaftsgeschichte, Präsens für Biologie), keine weiteren Befunde.

## Die drei wichtigsten Punkte

1. Ampel Prüfung 1 kippt auf rot: Die Heilanwendungen in „Menschen und Kultur" waren im Research-Doc ausdrücklich eine offene Beispielliste mit „darunter", im Kapitel stehen sie als geschlossene Aufzählung. Der Fehler ist so alt wie der erste Entwurf und lief durch Pilot-Erst- und Nachprüfung sowie den Korrekturlauf unbemerkt durch.
2. Die Gattung *Trigona* steht an vier Stellen aufrecht statt kursiv, obwohl der Korrekturlauf gezielt auf nicht kursiv gesetzte Artnamen geprüft hat. Einwortige Gattungsnamen ohne Artepitheton fielen offenbar durchs Raster, sowohl beim Korrekturlauf als auch bei der Skript-Heuristik.
3. Beide geprüften Eingriffe selbst sind sauber umgesetzt: Korrekturlauf (AFLP, Kopfzeile, Kursivsetzung der Binomen, Marker, Querverweis) und Namenskürzung nach E13 samt neuer Zählangabe „sieben Sprachen, zehn Wörter", die exakt mit der Namenszeile übereinstimmt. Keine falsche Zahl durch die Kürzung entstanden, die beiden neuen Befunde sind ältere, bisher unentdeckte Fehler.
