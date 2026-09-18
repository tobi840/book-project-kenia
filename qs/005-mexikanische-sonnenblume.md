# QS 005: Mexikanische Sonnenblume (Tithonia diversifolia)

## Ampel

**Prüfung 1 (Fakten): gelb.** Kein FALSCH, kein UNBELEGT, kein STATUSFEHLER. Vier VERZERRT-Stellen (siehe unten).

Regelcheck (Skript, `regel_check.py`): rot 0, gelb 5 (alle fünf gelben Befunde sind die offenen LÜCKE-Marker). Geschichte 1.058 Wörter, 9 Absätze, erster Satz 9 Wörter, letzter Absatz 49 Wörter, 0 Sätze über 40 Wörter, 1 rhetorische Frage, 1 lateinischer Name im Fließtext.

Linkcheck (Skript, `check_links.py`): 5 Links, 0 erfundene URLs, 0 tote Links, 5 nicht-prüfbar (Egress-Policy sperrt die Hosts, alle 5 Herkunft "im-research").

## Prüfung 1: Fakten

1. „Ein Exemplar am oberen Ende dieser Reihe reicht an ein einstöckiges Gebäude heran und dehnt seine Krone bis zu 4,0 Meter in die Breite.“ | VERZERRT | Text verknüpft Maximalhöhe (5,0 m, verglichen mit einem einstöckigen Gebäude) und maximale Kronenbreite (4,0 m) als Eigenschaften ein und desselben Exemplars („Ein Exemplar am oberen Ende dieser Reihe“) | Research-Doc führt beide Werte in getrennten Tabellenzeilen ohne Verknüpfung: „Höhe: 1.2 m bis 5.0 m [...] Ein Alltagsvergleich für die Maximalhöhe von 5.0 m entspricht der Höhe eines einstöckigen Gebäudes“ und „Breite (Krone): Bis zu 4.0 m Ausdehnung pro Pflanze“ (Abschnitt 2). Keine Aussage, dass es sich um dieselbe Pflanze handelt.

2. „Die Blütenstände messen 5,0 bis 15,0 Zentimeter im Querschnitt, der größte füllt eine Handfläche“ | VERZERRT | Körpermaß „Handfläche“ für den Maximalwert von 15 cm steht nicht im Research-Doc, eine durchschnittliche Handfläche ist deutlich kleiner als 15 cm | Research-Doc nennt nur „Blütenstand (Durchmesser): 5.0 cm bis 15.0 cm im Querschnitt“ (Abschnitt 2), keinen Körpermaß-Vergleich.

3. „mit 10,0 bis 40,0 Zentimetern werden die größten länger als eine Handspanne“ | VERZERRT | Körpermaß „Handspanne“ (ca. 20 cm) für den Maximalwert 40 cm steht nicht im Research-Doc und untertreibt die Größe (40 cm ist etwa doppelt so lang wie eine Handspanne) | Research-Doc nennt nur „Blattlänge: 10.0 cm bis 40.0 cm“ (Abschnitt 2), keinen Körpermaß-Vergleich.

4. „Sie ist mannshoch bis doppelt mannshoch, sie blüht das ganze Jahr“ (Absatz 1) und „Sie blüht und fruchtet ganzjährig“ (Absatz 8) | VERZERRT | Text stellt das ganzjährige Blühen als uneingeschränkte Tatsache dar | Research-Doc: „Die Lebensweise der autotrophen Pflanze ist polykarpisch; sie blüht und produziert Samen ganzjährig, sofern die klimatischen Rahmenbedingungen dies zulassen“ (Abschnitt 4). Die Bedingung fehlt im Kapiteltext an beiden Stellen.

## Prüfung 2: Stil

Keine Fundstellen. Keine Gedankenstriche, keine verbotenen Wörter, keine Adjektivketten ab drei, keine Fazit-Sätze oder Appelle. Letzter Absatz kehrt zum Anfangsbild zurück („Die gelbe Wand am Straßenrand steht noch“ zu „Vor Nairobi steht [...] eine gelbe Wand“). Eine rhetorische Frage („Warum also steht dieser Strauch mit vollen Blättern auf Böden, auf denen der Mais hungert?“) als Rätsel-Setup, innerhalb des Limits. Ein Humor-Einwurf in Klammern, innerhalb des Limits. Längen laut Skript alle im grünen bis gelben Bereich (siehe Ampel).

## Prüfung 3: Vorlesbarkeit

Keine Fundstellen. Keine Schachtelsätze über drei Ebenen, keine auffälligen Zischlaut-Häufungen, keine unpausierten Zahlenreihen, keine lateinischen Namen mitten im Satzfluss über die eine erlaubte Stelle hinaus, 0 Sätze über 40 Wörter (Skriptwert).

## Prüfung 4: Struktur und Links

- Alle fünf Blöcke vorhanden: Kopf, Geschichte, Menschen und Kultur, Vor der Linse, Weiterlesen und Sehen.
- „Menschen und Kultur“ wiederholt Block 1 nicht, ergänzt eigenständigen Inhalt (Medizin, Toxikologie, Termitenschutz).
- „Vor der Linse“ nennt konkreten Ort (Nairobi, Wegesränder, Brachflächen, Lebendzäune), Tageszeit (6:30 bis 8:30 Uhr, ab 16:30 Uhr) und Brennweiten aus dem Set (100 bis 400 / 150 bis 600 mm; 26 bis 60 mm / 45 mm). Keine Fundstelle.
- 5 Links, jeder mit einem Satz Kontext. Keine Fundstelle.
- Keine erfundenen oder abweichenden URLs (Skript: erfundene_urls 0, tote_links 0). Alle 5 Links Herkunft „im-research“, davon 5 nicht-prüfbar wegen Egress-Sperre (nicht tot, ungeprüft).
- Offene LÜCKE-Marker (5), einzeln mit Zitat der Umgebung:
  1. „Was die Wörter wörtlich bedeuten, übersetzt keine der Quellen. [[LÜCKE: wörtliche Bedeutung der lokalen Namen, etwa „Maua makech“ (Luo) und „Maruru“ (Kikuyu)]]“
  2. „Für Maa, Samburu und Giriama ist überhaupt kein Name dokumentiert. [[LÜCKE: lokale Bezeichnungen bei Maa, Samburu und Giriama]]“
  3. „Ein Gesamtgewicht verzeichnet keine Quelle. [[LÜCKE: Gewicht einer einzelnen Pflanze]]“
  4. „Wie viele Pflanzen so in Kenia stehen, zählt niemand. [[LÜCKE: quantitative Bestandszahlen für Kenia]]“
  5. „Überliefert ist lediglich, dass verwandte Tithonia-Arten in Westafrika für spirituelle Waschungen verwendet werden. [[LÜCKE: kenianische Mythen, Sprichwörter oder Legenden]]“

## Prüfung 5: Sprachrichtigkeit

1. „Quantifiziert hat das zuerst das International Centre for Research in Agroforestry in Nairobi.“ | Tempus-Inkonsistenz: Perfekt in einem sonst durchgängig im Präteritum erzählten historischen Absatz (unmittelbar folgender Satz: „Bashir Jama, Roland J. Buresh, Cheryl A. Palm und A. Niang veröffentlichten zwischen 1997 und 2000 [...]“) | Styleguide Abschnitt 5: „Präteritum für Geschichte“.

Keine weiteren Rechtschreib-, Zeichensetzungs- oder Kongruenzfehler gefunden. Lateinische Namen korrekt geschrieben; „Tithonia diversifolia“ genau einmal im Fließtext kursiv, „Mirasolia diversifolia“ bewusst nicht kursiv (steht im Einklang mit der Regel „höchstens einmal im Text“).

## Die drei wichtigsten Punkte

1. Keine FALSCH- oder UNBELEGT-Befunde in Prüfung 1, aber vier VERZERRT-Stellen: zwei erfundene Körpermaß-Vergleiche (Handfläche, Handspanne), eine Verknüpfung zweier getrennter Maximalwerte (Höhe, Breite) auf ein einzelnes Exemplar, und eine fehlende Einschränkung beim ganzjährigen Blühen.
2. Fünf offene LÜCKE-Marker sind korrekt gesetzt und stimmen mit den in Abschnitt 10 des Research-Docs aufgeführten Wissenslücken überein; das Kapitel bleibt mit 1.058 Wörtern in der grünen Längenzone trotz der Lücken.
3. Der Linkcheck findet keine erfundenen oder toten URLs; alle 5 Links sind im Research-Doc belegt, aber wegen der Egress-Sperre der Umgebung nicht live prüfbar (nicht-prüfbar, nicht tot).

## Nachprüfung

**Ampel Nachprüfung: grün.** Alle fünf Korrekturpunkte sind umgesetzt und korrekt. Kein neuer FALSCH, kein neues UNBELEGT, kein neuer STATUSFEHLER, kein neues VERZERRT. Regelcheck weiterhin rot 0, gelb 5 (unverändert die fünf offenen LÜCKE Marker). Linkcheck weiterhin 5 Links, 0 erfundene URLs, 0 tote Links, 5 nicht prüfbar.

### 1. Umsetzung der fünf Korrekturpunkte

1. Höhe und Breite entkoppelt. Neue Stelle: „Er wird 1,2 bis 5,0 Meter hoch, in landwirtschaftlichen Heckenpflanzungen im Schnitt 2,0 bis 3,0 Meter. Die Maximalhöhe von 5,0 Metern entspricht der Höhe eines einstöckigen Gebäudes. Die Krone einer Pflanze dehnt sich bis zu 4,0 Meter in die Breite.“ Der Gebäudevergleich hängt jetzt an der Maximalhöhe als Eigenschaft der Art, die Kronenbreite steht als eigener Satz mit „einer Pflanze“, ohne Verweis auf ein einzelnes Exemplar am oberen Ende der Höhenspanne. Deckt sich mit Research Doc Abschnitt 2 (Höhe und Breite in getrennten Tabellenzeilen). Korrekt umgesetzt.

2. Handfläche Vergleich gestrichen. Neue Stelle: „Die Blütenstände messen 5,0 bis 15,0 Zentimeter im Querschnitt: gelbe Zungenblüten von 4,0 bis 6,0 Zentimetern Länge um eine braunschwarze Scheibe aus Röhrenblüten von etwa 3,0 Zentimetern.“ Der Zusatz „der größte füllt eine Handfläche“ ist vollständig entfernt, der Maximalwert 15 cm steht jetzt ohne Verkleinerung durch einen Körpermaß Vergleich. Korrekt umgesetzt.

3. Handspanne Vergleich gestrichen. Neue Stelle: „Ältere Blätter sind tiefer gelappt als junge, und die Blattlänge reicht von 10,0 bis 40,0 Zentimetern.“ Der Zusatz „werden die größten länger als eine Handspanne“ ist entfernt, kein untertreibender Körpermaß Vergleich mehr vorhanden. Korrekt umgesetzt.

4. Einschränkung beim ganzjährigen Blühen ergänzt, an beiden Stellen. Absatz 1: „Sie ist mannshoch bis doppelt mannshoch, sie blüht das ganze Jahr, sofern die klimatischen Rahmenbedingungen dies zulassen, und wer hier Land bewirtschaftet, hat für sie selten ein gutes Wort.“ Absatz 8: „Sie blüht und fruchtet ganzjährig, sofern die klimatischen Rahmenbedingungen dies zulassen.“ Beide Stellen übernehmen die Einschränkung aus Research Doc Abschnitt 4 wörtlich sinngemäß („sofern die klimatischen Rahmenbedingungen dies zulassen“). Korrekt umgesetzt.

5. Tempus vereinheitlicht. Neue Stelle: „Der Maisertrag stieg in Versuchen von 1,5 Megagramm je Hektar in der Kontrolle auf 5,4 bis 5,5 Megagramm. Zuerst quantifizierte das International Centre for Research in Agroforestry in Nairobi diesen Effekt. Bashir Jama, Roland J. Buresh, Cheryl A. Palm und A. Niang veröffentlichten zwischen 1997 und 2000 die agronomischen Datenreihen dazu. Damit kippte die Wahrnehmung der Art vom invasiven Unkraut zum Gründünger für Kleinbauern.“ Das Perfekt „Quantifiziert hat“ ist durch das Präteritum „quantifizierte“ ersetzt, der gesamte Absatz steht jetzt durchgängig im Präteritum (stieg, quantifizierte, veröffentlichten, kippte). Korrekt umgesetzt.

### 2. Prüfung auf neue Schäden

**Prüfung 1 (Fakten), erneut vollständig durchgeführt:** Kein FALSCH, kein UNBELEGT, kein STATUSFEHLER, keine erfundenen Werte. Die vier ursprünglich bemängelten VERZERRT Stellen sind behoben und durch keine neuen Verzerrungen ersetzt. Die restlichen Fakten und Zahlen im Kapitel sind unverändert und stimmen weiterhin mit dem Research Doc überein (unter anderem: Wuchshöhe 1,2 bis 5,0 m, Kronenbreite bis 4,0 m, Blattlänge 10,0 bis 40,0 cm, Blütenstand 5,0 bis 15,0 cm, Zungenblüten 4,0 bis 6,0 cm, Röhrenblüten etwa 3,0 cm, Phosphatase Aktivität 29,64 nmol MUB pro Minute und Gramm Boden, Maisertrag 1,5 auf 5,4 bis 5,5 Mg/ha, Nährstoffgehalt 4,2/1,2/5,6 Prozent). Die fünf offenen LÜCKE Marker sind unverändert vorhanden und weiterhin korrekt gesetzt.

**Prüfung 2 (Stil), erneut vollständig durchgeführt:** Keine Gedankenstriche, keine verbotenen Wörter, keine Adjektivketten ab drei. Die eingefügten Nebensätze („sofern die klimatischen Rahmenbedingungen dies zulassen“) und die neu formulierten Sätze zu Höhe und Breite fügen sich stilistisch unauffällig ein, keine neuen Schachtelsätze über dem Limit, keine neue rhetorische Frage, kein neuer Appell oder Fazit Satz. Letzter Absatz kehrt weiterhin zum Anfangsbild zurück. Längen weiterhin im grünen bis gelben Bereich.

**Skript regel_check.py:** rot 0, gelb 5 (identisch mit der ersten QS, ausschließlich die fünf LÜCKE Marker). Geschichte jetzt 1.062 Wörter (vorher 1.058), 9 Absätze, erster Satz 9 Wörter, letzter Absatz 49 Wörter, 0 Sätze über 40 Wörter, 1 rhetorische Frage, 1 lateinischer Name im Fließtext. Der leichte Wortzuwachs stammt aus den beiden ergänzten Einschränkungen und ist ohne Auswirkung auf die Längenampel.

**Skript check_links.py:** 5 Links, 0 erfundene URLs, 0 tote Links, 5 nicht prüfbar, alle Herkunft „im-research“. Unverändert gegenüber der ersten QS. Die fünf nicht prüfbaren Links sind wegen der Egress Sperre der Umgebung ungeprüft, nicht tot.

**Ergebnis:** Die Korrektur sitzt vollständig und sauber. Kein neuer Fehler, keine neue Lücke, kein Regressions Befund in Fakten, Stil oder den beiden Skripten.

## Die drei wichtigsten Punkte der Nachprüfung

1. Alle fünf Korrekturpunkte aus dem Auftrag sind an der jeweils richtigen Stelle korrekt umgesetzt, mit Zitat belegt.
2. Weder Prüfung 1 (Fakten) noch Prüfung 2 (Stil) noch die beiden Skripte (regel_check.py, check_links.py) finden neue Befunde. Regelcheck weiterhin rot 0 / gelb 5, Linkcheck weiterhin 0 erfundene und 0 tote Links.
3. Die fünf offenen LÜCKE Marker bleiben unverändert bestehen und sind weiterhin korrekt gesetzt, keine davon wurde durch die Korrektur berührt.
