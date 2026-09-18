# QS Kapitel 001: Heilige Würgefeige (Mugumo)

Research-Doc: 1KsGwquxBWy8lavum5HIa9B8NUxViL-N1U7HZABLA8ak
Geprüft gegen Spiegel: research/001-heilige-wuergefeige.txt
Kapiteldatei (nicht verändert): chapters/001-heilige-wuergefeige.html

## Werkzeug-Ausgaben (übernommen, nicht selbst gezählt)

`regel_check.py`: Ampel gelb, rot 0, gelb 3 (alle drei aus offenen Lücken). Geschichte 1.056 Wörter, 9 Absätze, erster Satz 12 Wörter, letzter Absatz 56 Wörter, Sätze über 40 Wörter 0, rhetorische Fragen 2, lateinischer Name im Fließtext 1x, Menschen und Kultur 203 Wörter, Vor der Linse 129 Wörter, Links 6, Lücken 3.

`check_links.py`: 6 Links, 0 erfundene URLs, 0 tote Links, 6 nicht prüfbar (Egress-Policy sperrt die Hosts), Herkunft aller 6 Links "im-research".

## Ampel Prüfung 1

**Gelb.** Kein FALSCH, aber UNBELEGT, STATUSFEHLER und VERZERRT vorhanden.

## Prüfung 1: Fakten

- "Dazu einen Erdwall, aufgeschüttet bis an die grauen Wülste der Rinde." | UNBELEGT | Text behauptet, der Erdwall sei bis zur Höhe der Rindenwülste aufgeschüttet worden | Research-Doc nennt nur "einem Erdwall und einem massiven eisernen Ring" ohne Angabe zur Höhe des Walls.

- "Wer Ende September unter einem Mugumo steht, steht unter dem am besten besuchten Baum der Umgebung." | UNBELEGT | Text behauptet, der Baum sei der meistbesuchte Baum der Umgebung | Research-Doc belegt nur, dass die Baumkrone in dieser Zeit "ein Magnet für Frugivore" wird und der Baum als Keystone-Species gilt, kein Vergleich zu anderen Bäumen der Umgebung.

- "Am 12. Dezember 1963, dem Tag der kenianischen Unabhängigkeit, sackte das Geflecht in sich zusammen." | STATUSFEHLER | Text stellt den Zusammensturz am 12.12.1963 ohne Statusmarker als gesicherte Tatsache dar | Research-Doc markiert genau dieses Ereignis explizit als überliefert: "Am 12. Dezember 1963 ... fiel der Baum in sich zusammen und erfüllte die Prophezeiung (überliefert)15."

- "Die IUCN führt die Art als „Least Concern“, die Einstufung beruht auf Daten von vor 2020." | VERZERRT | Text sagt, die Daten stammten von vor 2020 (impliziert: veraltet, älter als 2020) | Research-Doc: "Datenjahr der Erfassung in aktuellen Derivaten oft 2020" (also aus 2020, nicht davor). Die Zeitangabe verschiebt sich vom Doc zum Text.

## Prüfung 2: Stil

Keine Gedankenstriche gefunden, keine verbotenen Wörter, keine Adjektivketten ab drei, maximal zwei rhetorische Fragen (genau zwei, beide als Rätsel-Setup, im Rahmen), keine Fazit-Sätze oder Appelle, letzter Absatz kehrt zum Eisenring-Bild des Anfangs zurück. Längen unauffällig (siehe Werkzeug-Ausgabe oben).

- "Phylogenetische Arbeiten, unter anderem von Compton und Kollegen 2009 und Cornille und Kollegen 2011, haben dieses Bild für diesen Artenkomplex widerlegt (gesichert)." | Unerklärter Fachbegriff "Phylogenetisch" wird im Satz nicht erklärt.

- "Als einzige Art ihres Formenkreises bildet sie Stilbene, darunter Resveratrol, die der Baum gegen Krankheitserreger und UV-Strahlung produziert ..." | Unerklärter Fachbegriff "Formenkreis" wird im Satz nicht erklärt.

## Prüfung 3: Vorlesbarkeit

- "Der Baum verträgt Höhen zwischen 1.000 und 2.500 Metern, Nairobi liegt bei etwa 1.795 Metern, und Jahresniederschläge von 750 bis 2.000 Millimetern." | Zahlenreihe ohne Pause: drei Zahlenangaben in einem Satz ohne satzschließende Pause dazwischen.

- "In einer Stichprobe von 50 Feigen enthielten 28 genau eine Wespenart, 19 zwei Arten und zwei Feigen drei." | Zahlenreihe ohne Pause: vier Zahlen in einem Satz, beim Vorlesen schwer atembar.

- "Die Kenya National Highways Authority kündigte an, einen jahrhundertealten Mugumo am Waiyaki Way in Westlands zu versetzen oder zu fällen, einen Baum von vier Stockwerken Höhe, im Weg des von China finanzierten Nairobi Expressway (gesichert)." | Schachtelsatz: Infinitivkonstruktion plus zwei nachgestellte Apposition/Partizipialkonstruktionen in einem Satz.

## Prüfung 4: Struktur und Links

Alle fünf Blöcke vorhanden. "Menschen und Kultur" wiederholt Block 1 nicht, sondern ergänzt ihn (Futter, Medizin, Ritual, Tabu, Schutzstatus statt Mechanismus und Geschichte). "Vor der Linse" nennt konkreten Ort (Waiyaki Way, Westlands), Tageszeiten und mehrere Brennweiten aus dem Set. 6 Links, jeder mit einem Kontextsatz, alle 6 URLs laut Linkcheck im Research-Doc vorhanden, keine erfundene URL.

Offene [[LÜCKE]]-Marker (3, alle bereits korrekt als Lücke markiert, keine Änderung nötig):

- "Was diese Wörter wörtlich bedeuten, sagt keine der Quellen. [[LÜCKE: wörtliche Bedeutung der lokalen Namen Mũgumo, Kiumo, Oretiti, Koitab cheboiyet, Simotwo, Pocho, Seepei]]"
- "Für die Giriama an der Küste ist gar kein Name belegt. [[LÜCKE: lokaler Name der Giriama]]"
- "Für springende Tiere im Geäst genügen 1/500 s bis 1/1000 s. [[LÜCKE: Fluchtdistanz der frugivoren Tiere am Waiyaki-Way-Baum]]"

## Prüfung 5: Sprachrichtigkeit

- "ein Sykonium von 7 bis 14 Millimetern, kleiner als eine Fingerkuppe, die Blüten vollständig im Inneren." | Unvollständiger Satzteil: der letzten Apposition fehlt ein finites Verb (z. B. "liegen" oder "sind").

Tempus konsistent (Präsens für Biologie, Präteritum für historische Ereignisse wie Thika-Ring, Mugo wa Kibiru, Nairobi Expressway 2020, Unabhängigkeit 1963). Lateinischer Name korrekt kursiv, nur einmal im Fließtext plus im Kopf.

## Die drei wichtigsten Punkte

1. Der Schlussabsatz erzählt den Zusammensturz des Baumes am 12. Dezember 1963 ohne Statusmarker als gesicherte Tatsache, obwohl das Research-Doc dieses Ereignis explizit als überliefert markiert.
2. Zwei Detailbehauptungen (Höhe des Erdwalls bis zu den Rindenwülsten, "meistbesuchter Baum der Umgebung") stehen so nicht im Research-Doc.
3. Die IUCN-Einstufung wird zeitlich verzerrt wiedergegeben: Der Text macht aus "Datenjahr oft 2020" ein "Daten von vor 2020".
