# QS 005 Nachprüfung: Mexikanische Sonnenblume (Tithonia diversifolia)

Erreichbarkeit: gesammelter Lauf steht aus.

Geprüfter Stand: chapters/005-mexikanische-sonnenblume.html nach Korrekturlauf 001 bis 005 (Commit 3384d17) und E11 bis E14 (Commit d4b9808). Beide Durchgänge waren vor diesem Lauf ungeprüft.

## Ampel

**Prüfung 1 (Fakten): rot.** Ein FALSCH Befund (Namensbedeutung Luhya und Luo, siehe unten), dazu ein UNBELEGT Befund (Körpermaß Vergleich).

Regelcheck (regel_check.py): Ampel grün (0 rot, 0 gelb). Geschichte 1.067 Wörter, 9 Absätze, erster Satz 9 Wörter, letzter Absatz 49 Wörter, 0 Sätze über 40 Wörter, 1 rhetorische Frage, 1 lateinischer Name im Fließtext, 0 Kursivverdacht, 0 Lücken, 3 Offen.

Linkcheck (check_links.py): 5 Links, 0 nicht im Research Doc, 0 tot, 0 nicht prüfbar.

## Umgesetzt seit der Erstprüfung, geprüft und in Ordnung

- Höhe und Kronenbreite entkoppelt, kein gemeinsames Exemplar mehr.
- Körpermaß Vergleiche „Handfläche" und „Handspanne" gestrichen.
- Einschränkung „sofern die klimatischen Rahmenbedingungen dies zulassen" an beiden Blühstellen vorhanden.
- Tempus bei „quantifizierte" durchgängig Präteritum.
- Querverweis Absatz vollständig entfernt, kein `<p class="querverweis">` mehr im Kapitel.
- Handelsnamen (Deutsch, Englisch) aus der Kopfzeile entfernt, nur noch „Sprache: „Name"".
- Kursivsetzung nachgezogen: „Mirasolia diversifolia" und die Artnamen in der Linkliste jetzt kursiv, „Tithonia diversifolia" weiterhin genau einmal im Fließtext kursiv.
- Alle drei verbleibenden Marker einzeln gegen Research Doc Abschnitt 10 geprüft, korrekt als OFFEN eingeordnet (Gewicht, Bestandszahlen, Mythen), keine LÜCKE mehr.
- Fließtext auf höchstens drei lokale Namen gekürzt (Maruru, Maua amalulu, Maua makech). Die Zählangabe „vier Sprachen" in der Namenszeile stimmt (Kikuyu, Luo, Luhya, Kamba, dazu Swahili).

## Prüfung 1: Fakten, neu und vollständig geprüft

1. „Dieselbe Auskunft geben die Nachbarsprachen. Das Luhya „Maua amalulu" und das Luo „Maua makech" benennen ebenfalls den bitteren Geschmack (gesichert). Drei Sprachen, dieselbe Beobachtung" | FALSCH | Text stellt die Bedeutung von „Maua amalulu" (Luhya) und „Maua makech" (Luo) als gesichert bitteren Geschmack dar | Research Doc 005, Abschnitt 1, Tabelle: „Maua makech, Akech, Maua madungo, Otech / Luo / Wörtliche Bedeutung ist unbekannt" und „Maua amalulu, Amatwele / Luhya / Wörtliche Bedeutung ist unbekannt". research/namen-bedeutungen.md führt für Luo und Luhya gar keinen Eintrag, beide stehen dort ausdrücklich auf der Liste „Nie geprüft". Einzige Stütze ist ein Nebensatz in der Maruru Dokumentation, der eine Quelle zur Nachbarsprache zitiert, genau das schließt dieselbe Datei aus: „Kein Modell leitet eine Bedeutung selbst ab. Nicht aus dem Wortstamm, nicht aus einer Nachbarsprache, nicht aus einem Präfix." Entstanden im Korrekturlauf (Commit 3384d17, „Dieselbe Auskunft geben die Namen der Nachbarsprachen ... (gesichert)"), durch die Kürzung E13 (Commit d4b9808) mit dem Satz „Drei Sprachen, dieselbe Beobachtung" noch verstärkt. Färbt rot.

2. „Sie ist mannshoch bis doppelt mannshoch" | UNBELEGT | Körpermaß Vergleich für die Wuchshöhe 1,2 bis 5,0 Meter | Research Doc nennt für die Maximalhöhe von 5,0 m nur den Vergleich „Höhe eines einstöckigen Gebäudes" (Abschnitt 2), keinen Körpermaß Vergleich, für die volle Spanne 1,2 bis 5,0 m gar keinen. Vorbestehend seit der ersten Fassung (Pilot Commit 890423b), unverändert durch beide geprüften Durchgänge, von der Erstprüfung nicht gefunden.

## Prüfung 2 und 3

Keine neuen Befunde gegenüber der Erstprüfung. Gedankenstriche weiterhin keine, verbotene Wörter keine, Adjektivketten keine, Schachtelsätze und Zahlenreihen ohne Befund.

## Prüfung 4: Struktur, Marker und Links

Kein `<p class="querverweis">` mehr vorhanden. Kopfzeile korrekt (Sprache: „Name", keine Handelsnamen). Drei lokale Namen im Fließtext, Grenze eingehalten. Links unverändert korrekt (siehe Linkcheck).

Ein Nebenbefund: Der Marker `[[OFFEN: wörtliche Bedeutung der übrigen lokalen Namen, siehe research/namen-bedeutungen.md]]`, den der Korrekturlauf gesetzt hatte, ist bei der Kürzung in E13 ersatzlos entfallen. Der Satz „Was die übrigen Wörter bedeuten, übersetzt keine Quelle" steht weiter im Text, die Lücke besteht unverändert, jetzt aber ohne Marker. Nicht ampelrelevant (OFFEN färbt ohnehin nicht), aber eine Fundstelle.

## Prüfung 5: Sprachrichtigkeit

„und sie hat Ende der 1990er Jahre den Blick auf die Pflanze gedreht" (Absatz 1) steht im Perfekt in einem historischen Zusammenhang mit Jahrzehntangabe. Dieselbe Inkonsistenz, die bei „Quantifiziert hat das zuerst ..." in der Erstprüfung gemeldet und im Korrekturlauf zu „quantifizierte" behoben wurde, steht hier unbehoben. Vorbestehend seit der Pilotfassung, von keiner bisherigen Prüfung gemeldet. Styleguide Abschnitt 5: „Präteritum für Geschichte."

Kursivsetzung im Übrigen korrekt, lateinische Namen wie gemeldet.

## Die drei wichtigsten Punkte

1. FALSCH in Prüfung 1, Ampel rot: Die im Korrekturlauf ergänzte und in E13 verstärkte Aussage, Luhya „Maua amalulu" und Luo „Maua makech" bedeuteten gesichert „bitterer Geschmack", widerspricht dem Research Doc 005 (dort ausdrücklich „unbekannt") und der Statusregel aus namen-bedeutungen.md (Luo und Luhya nie geprüft, keine Ableitung aus Nachbarsprachen erlaubt). Das ist der Fehler, den diese Nachprüfung finden sollte.
2. Ein zweiter, vorbestehender Fundpunkt kam beim erneuten vollständigen Abgleich aller Zahlen hinzu: der erfundene Körpermaß Vergleich „mannshoch bis doppelt mannshoch" im ersten Satz, unbelegt und von keiner bisherigen Prüfung gefunden.
3. Alle prüfbaren Änderungen aus Korrekturlauf und E13 (Kursivsetzung, Kopfzeile, Querverweis Entfernung, Markerzuordnung, Drei Namen Grenze, die fünf ursprünglichen Korrekturpunkte) sind korrekt umgesetzt. Einzige strukturelle Nebenwirkung: ein OFFEN Marker ist beim Kürzen ohne Ersatz verschwunden, nicht ampelrelevant.
