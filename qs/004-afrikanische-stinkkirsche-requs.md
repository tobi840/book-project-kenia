# Nachprüfung 004: Afrikanische Stinkkirsche (Prunus africana)

Erreichbarkeit: gesammelter Lauf steht aus.

Geprüft: `chapters/004-afrikanische-stinkkirsche.html` gegen `research/004-afrikanische-stinkkirsche.txt`, `styleguide/01-text-styleguide.md` und `research/namen-bedeutungen.md` (Status `belegt`). Kapiteldatei für diese Prüfung nicht verändert. Beide vorangegangenen Durchgänge (Korrekturlauf laut `berichte/KORREKTURLAUF-001-005.md` und die Kürzung der Namensabsätze nach E13) waren zuvor von keinem prüfenden Modell gesehen worden.

Werkzeugausgaben (übernommen, nicht selbst gezählt):
- `regel_check.py`: Ampel grün, rot 0, gelb 0. Geschichte 1010 Wörter, 9 Absätze, erster Satz 14 Wörter, letzter Absatz 47 Wörter, Sätze über 40 Wörter 0, rhetorische Fragen 1, Kursivverdacht 0, lateinisch im Fließtext 1, Links 6, Lücken 0, Offen 3.
- `check_links.py`: 6 Links, 0 nicht im Research-Doc, 0 tot, 0 nicht prüfbar. Alle 6 URLs mit Herkunft „im-research".

## Teil 1: Umgesetzte Punkte aus Erstprüfung und Korrekturlauf

Geprüft, jeweils erneut mit dem Research-Doc abgeglichen, nicht nur die Änderungsbeschreibung im Korrekturbericht gelesen. Alle bestätigt korrekt umgesetzt, kein Zitat wiederholt:

- Herbarium-Angabe „Kew Gardens" zu „K Herbarium" korrigiert
- Sprachbezeichnung „Maa" statt „Maasai" im Kopf
- Zuspitzung „nicht im Holz, nicht in den Blättern" gestrichen
- „fünfzehn Bäume" zu einer Tonnage-Aussage (5.000 t gegen 330 t, Faktor rund fünfzehn) umformuliert
- Länderliste 2007 mit „unter anderem" als Beispiel statt als vollständige Liste markiert
- Phloem-Funktionsbehauptung (Zuckertransport) gestrichen, nur noch die belegte mikroskopische Beschreibung
- Tageszeitangabe „am frühen Morgen" entfernt, Research-Doc nennt nur „tief stehende Sonne"
- Bezugswort „Er" durch „Dieser Geruch" ersetzt, Referenz jetzt eindeutig
- Die beiden lateinischen Artnamen im Karura-Satz durch deutschen Zwischentext getrennt
- <em>Nuxia congesta</em>, <em>Elaeodendron paniculata</em>, <em>Croton megalocarpus</em> kursiv gesetzt
- Querverweis-Satz mit dem „(S. XX)"-Platzhalter vollständig entfernt (nicht nur der Platzhalter), kein `<p class="querverweis">` mehr im Kapitel, kein Rest-Marker dafür
- Ordnungszahl „dieser zweite Name" korrekt an die gekürzte Namensliste angepasst (vorher „dritter Name" bei drei genannten Kikuyu-Namen, jetzt zwei genannt: Muiri, Muchorowe). Eigens gegengeprüft, weil genau diese Art von Zählfehler beim Kürzen entsteht

Ergebnis: Kein FALSCH, UNBELEGT, STATUSFEHLER oder VERZERRT aus der Erstprüfung ist noch offen.

## Teil 2: Nachzählung der Namenszeile (E13)

„sieben Sprachen, fünfzehn Wörter" (Geschichte, Absatz 3) nachgezählt gegen die Namenszeile im Kopf:

Swahili (2: Kiburabura, Mfuwate), Kikuyu (3: Muiri, Mwiria, Muchorowe), Kalenjin (4: Tenduet, Chebitet, Yemit, Remit), Maa (1: Olkojuk), Samburu (2: Lcheni, Lkeni), Kamba (2: Mumbaume, Mutimailu), Bukusu (1: Kumutura).

7 Sprachen, 2+3+4+1+2+2+1 = 15 Wörter. Beide Zahlen stimmen mit der Namenszeile und dem Research-Doc überein. Kein Befund.

## Teil 3: Neue Befunde Prüfung 1 (Fakten)

1. „die Mittelader wie mit dem Daumennagel eingedrückt" | UNBELEGT | Text vergleicht die Einsenkung der Blattmittelader mit einem Daumennagel-Abdruck | Research-Doc beschreibt die Mittelader nur als „auf der Oberseite markant eingesenkt (depressed)", ohne Alltagsvergleich. Kein Fund im Doc für „Daumennagel". Gehört zur Kategorie Körpermaße/Alltagsvergleiche aus P4: nur zulässig, wenn das Doc den Vergleich liefert. Bestand schon vor dem Korrekturlauf, der an dieser Stelle zwei andere erfundene Vergleiche im selben Kapitel strich (Armlänge, erbsengroß), diesen aber nicht. In der Erstprüfung nicht gefunden.

2. „Zwei Meter höher, an einem Zweig mit unversehrter Rinde, schwellen in den Blattachseln die Knospen der nächsten Blütentrauben." | UNBELEGT | Text gibt für die Position des unversehrten Zweigs im Schlussbild eine Höhenangabe von zwei Metern an | Research-Doc nennt für das Wachstumsverhalten nur „frische Wachstumsschübe (Flushing) an den Zweigenden" ohne jede Höhen- oder Entfernungsangabe. Auch dieser Satz war schon vor dem Korrekturlauf vorhanden und ist in der Erstprüfung nicht aufgefallen.

Kein FALSCH, kein STATUSFEHLER, kein VERZERRT gefunden. Ampel Prüfung 1: GELB (zwei UNBELEGT, kein FALSCH).

## Prüfung 2: Stil

Keine Befunde. Keine Gedankenstriche, keine verbotenen Wörter, keine Adjektivketten ab drei, eine rhetorische Frage als Rätsel-Setup (im Rahmen), Längenwerte alle im grünen Bereich laut Werkzeug.

## Prüfung 3: Vorlesbarkeit

1. „Die unscheinbaren Blüten bestäuben Insekten, die Früchte fressen Vögel und Säugetiere." | Geringfügig. Bei wörtlicher Subjekt-Verb-Objekt-Lesart stünde da, die Blüten bestäuben die Insekten, umgekehrt zum Research-Doc („werden durch verschiedene Insektenarten bestäubt"). Die Weltwissen-Plausibilität und der parallele zweite Halbsatz (der auf dieselbe Art gebaut ist und dort eindeutig nur „Vögel und Säugetiere fressen die Früchte" bedeuten kann) lösen das beim Lesen wahrscheinlich richtig auf. Kein Änderungsvorschlag, nur notiert, da grenzwertig.

## Prüfung 4: Struktur, Marker und Links

Alle fünf Blöcke vorhanden. Kopfzeile: nur lokale Namen, Format „Sprache: „Name"", Sprachbezeichnung „Maa" korrekt. Kein `<p class="querverweis">`. Links 6, alle mit Kontextsatz, 0 erfunden laut Werkzeug. Marker: 0 `[[LÜCKE]]`, 3 `[[OFFEN]]`, alle drei weiterhin korrekt als vom Research-Doc selbst nicht klärbar ausgewiesen (Kikuyu-Schreibung „Mueri", Blühzeitpunkt im Reisefenster, Kakamega-Variante in Nairobi). Keine Seitenzahl in einem Marker.

Offener Punkt zur Zählung der lokalen Namen im Fließtext (E13, höchstens drei): Im Fließtext direkt lesbar (außerhalb von Markern) stehen „Muiri", „Muchorowe" und „Lcheni", macht drei. Innerhalb des ersten `[[OFFEN]]`-Markers wird zusätzlich „Mueri" genannt (im Vergleich mit „Muiri"). Ob das mitzählt, hängt davon ab, ob Marker-Inhalt als Fließtext gilt. Nach der im Korrekturbericht festgehaltenen Regel „ein Marker ist keine Prosa und wird nicht vorgelesen" zählt er nach meiner Lesart nicht mit, dann bleibt es bei drei. Die E13-Regel nennt „eine Zuordnungsfrage" aber ausdrücklich als Aufnahmegrund, und genau das ist der Mueri-Fall, was auch für eine Zählung sprechen könnte. Beide Lesarten sind vertretbar, die Regel selbst entscheidet es nicht. Da E13 erst nach der Erstprüfung entschieden wurde, ist das eine neue Frage, kein durchgerutschter Fehler.

## Prüfung 5: Sprachrichtigkeit

Kursivierung: alle lateinischen Artnamen im Fließtext und in den Links kursiv, auch die drei zuvor aufrecht stehenden. Bare Gattungsnamen ohne Art-Epitheton („Gattung Prunus", „Prunus-Extrakte", „dicht mit Prunus bestanden") stehen aufrecht, das ist buchweit einheitlich so (auch „Gattung Trigona" in 003 und „Gattung Tithonia" in 005 stehen aufrecht), kein Einzelfall von 004 und kein neuer Befund.

Weiterhin offen: Namenszeilen-Format im Kopf. Styleguide Abschnitt 5 schreibt „Name" (Sprache), das Kapitel nutzt wie alle fünf Kapitel und wie das Kapitel-Template „Sprache: „Name"". Unverändert seit der letzten Prüfung, bewusst nicht angefasst, braucht weiterhin eine Konventionsentscheidung, kein Fehler im Kapitel.

Tempus durchgehend korrekt (Präsens für Biologie und für weiterhin gültige Fakten wie „Rindenextrakte laufen bis heute als Pygeum", Präteritum für abgeschlossene historische Ereignisse). Keine Rechtschreib- oder Zeichensetzungsfehler gefunden.

## Die drei wichtigsten Punkte

1. Alle Befunde aus Erstprüfung und Korrekturlauf sind korrekt behoben. Die Ampel steht trotzdem nicht auf Grün: Zwei neue UNBELEGT-Befunde (Daumennagel-Vergleich, Zwei-Meter-Höhenangabe) waren schon vor dem Korrekturlauf im Text und sind erst jetzt aufgefallen, färben Prüfung 1 gelb.
2. Ungeklärt, ob die Namensliste im Fließtext mit vier statt drei lokalen Namen gegen E13 verstößt, je nachdem, ob der nur im `[[OFFEN]]`-Marker genannte Name „Mueri" mitzählt. Die Regel selbst entscheidet die Frage nicht, das ist eine Entscheidung für Tobi.
3. Zwei ältere, sachlich unveränderte offene Punkte bleiben: das Namenszeilen-Format (Styleguide gegen gelebte Praxis) und die drei `[[OFFEN]]`-Marker, die laut E11/E12 nicht mehr nachrecherchiert werden.
