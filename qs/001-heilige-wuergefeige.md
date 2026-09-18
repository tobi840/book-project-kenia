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

## Nachprüfung

Geprüft: Kapiteldatei nach Korrektur, unverändert von diesem Lauf. Research-Doc und Spiegel wie oben. Kapiteldatei wurde für diese Nachprüfung nicht angefasst.

### Teil 1: Sitzt jede Anweisung des Korrekturauftrags

1. Erdwall ohne Höhenangabe. Umgesetzt. Neue Stelle: "In Thika legte die britische Kolonialverwaltung einen eisernen Ring um einen Baum. Dazu einen Erdwall." Die Höhenangabe "bis an die grauen Wülste der Rinde" ist gestrichen, kein Ersatz eingefügt. Deckt sich mit Research-Doc ("einem Erdwall und einem massiven eisernen Ring").

2. Superlativ ersetzt. Umgesetzt. Neue Stelle: "Wer Ende September unter einem Mugumo steht, steht unter einer Krone, die in diesen Wochen zum Magneten für fruchtfressende Tiere wird." Kein Vergleich zu anderen Bäumen mehr, "Magnet für fruchtfressende Tiere" entspricht Research-Doc Zeile 115 ("wird die Baumkrone ein Magnet für Frugivore sein").

3. Statusmarker ergänzt. Umgesetzt. Neue Stelle: "Am 12. Dezember 1963, dem Tag der kenianischen Unabhängigkeit, sackte das Geflecht in sich zusammen (überliefert)." Markiert wie im Research-Doc.

4. IUCN-Datenjahr korrigiert. Umgesetzt. Neue Stelle: "Die IUCN führt die Art als „Least Concern“, die Einstufung trägt in aktuellen Fassungen meist das Datenjahr 2020." Gibt Research-Doc Zeile 108 wieder ("Datenjahr der Erfassung in aktuellen Derivaten oft 2020"), keine Verschiebung mehr Richtung "davor".

5. Höhenlagen und Niederschlag getrennt. Umgesetzt. Neue Stelle: "Der Baum verträgt Höhen zwischen 1.000 und 2.500 Metern, Nairobi liegt bei etwa 1.795 Metern. An Jahresniederschlag verträgt er 750 bis 2.000 Millimeter." Zwei Sätze statt einem, alle drei Zahlen erhalten.

6. Wespensatz geteilt. Umgesetzt. Neue Stelle: "In einer Stichprobe von 50 Feigen enthielten 28 genau eine Wespenart. In 19 Feigen waren es zwei Arten, in zwei Feigen drei." Zwei Sätze, Zahlenreihe entzerrt.

7. Highways-Satz entschachtelt. Umgesetzt. Neue Stelle: "Die Kenya National Highways Authority kündigte an, einen jahrhundertealten Mugumo am Waiyaki Way in Westlands zu versetzen oder zu fällen, einen Baum von vier Stockwerken Höhe. Er stand im Weg des von China finanzierten Nairobi Expressway (gesichert)." Nairobi Expressway steht jetzt in eigenem Satz, wie im Auftrag als Beispiel genannt.

8. "Phylogenetisch" erklärt. Umgesetzt. Neue Stelle: "Phylogenetische Arbeiten, also Arbeiten zur Verwandtschaft der Arten, unter anderem von Compton und Kollegen 2009 und Cornille und Kollegen 2011, haben dieses Bild für diesen Artenkomplex widerlegt (gesichert)." Erklärung sitzt direkt im Satz.

9. "Formenkreis" ersetzt. Umgesetzt. Neue Stelle: "Als einzige Art ihrer Verwandtschaftsgruppe bildet sie Stilbene, darunter Resveratrol, die der Baum gegen Krankheitserreger und UV-Strahlung produziert ..." Allgemeinverständliches Wort wie im Auftrag vorgeschlagen.

10. Fehlendes Verb ergänzt. Umgesetzt. Neue Stelle: "ein Sykonium von 7 bis 14 Millimetern, kleiner als eine Fingerkuppe, die Blüten liegen vollständig im Inneren." Apposition jetzt vollständiger Satzteil.

Ergebnis Teil 1: Alle zehn Anweisungen sitzen, jede korrekt gegen das Research-Doc geprüft.

### Teil 2: Hat die Korrektur etwas kaputt gemacht

**Prüfung 1 (Fakten), erneut vollständig durchgeführt:** Alle vier ursprünglichen Befunde (UNBELEGT Erdwall, UNBELEGT meistbesuchter Baum, STATUSFEHLER 12.12.1963, VERZERRT IUCN-Datenjahr) sind behoben, siehe Teil 1. Restlicher Fließtext erneut gegen Research-Doc gelesen (Thika-Ring und Maße, Namensliste, Anastomose-Mechanismus, Feigenwespen-Biologie, Compton/Cornille-Referenz, Fruchtzeit und Höhenlagen, Cege wa Kibiru/Mugo wa Kibiru, Waiyaki-Way-Fall, Nutzung als Futter und Medizin, Tabu Migiro, IUCN/NatureServe): keine neuen FALSCH, UNBELEGT, STATUSFEHLER oder VERZERRT gefunden. Kein neuer Befund durch die Umformulierungen selbst, da sie ausschließlich Sätze aufteilen oder Fachbegriffe erklären, ohne neue Behauptungen einzuführen.

**Ampel Prüfung 1: Grün.** Kein FALSCH, kein UNBELEGT, kein STATUSFEHLER, kein VERZERRT mehr offen.

**Prüfung 2 (Stil), erneut vollständig durchgeführt:** Die beiden gemeldeten unerklärten Fachbegriffe ("Phylogenetisch", "Formenkreis") sind behoben (Punkte 8 und 9). Keine Gedankenstriche im gesamten Kapitel. Keine verbotenen Wörter. Keine Adjektivketten ab drei. Rhetorische Fragen weiterhin genau zwei (Rätsel-Setup, im Rahmen). Keine Fazit-Sätze oder Appelle. Letzter Absatz kehrt weiterhin zum Eisenring-Bild des Anfangs zurück, jetzt mit korrektem Statusmarker. Keine neuen Stil-Befunde durch die Korrektur.

**Skript `regel_check.py --json`:** Ampel gelb, rot 0, gelb 3. Alle drei Gelb-Befunde sind die bereits bekannten, korrekt markierten [[LÜCKE]]-Marker (wörtliche Bedeutung der lokalen Namen, Giriama-Name, Fluchtdistanz), keine neuen Regelverstöße. Maße: Geschichte 1.068 Wörter (vorher 1.056, Anstieg durch die Erklärungen "also Arbeiten zur Verwandtschaft der Arten" und "Verwandtschaftsgruppe" statt "Formenkreis"), 9 Absätze (unverändert), erster Satz 12 Wörter, letzter Absatz 57 Wörter (vorher 56, im Rahmen, Grenze 80), Sätze über 40 Wörter weiterhin 0, rhetorische Fragen 2, lateinischer Name im Fließtext 1x, Menschen und Kultur 205 Wörter, Vor der Linse 129 Wörter, Links 6, Lücken 3. Alle Werte innerhalb der Normgrenzen, keine neue Rot- oder Gelb-Ursache durch die Korrektur.

**Skript `check_links.py --json`:** 6 Links, 0 erfundene URLs, 0 tote Links, 6 nicht prüfbar (Egress-Policy sperrt die Hosts, das ist ungeprüft, nicht tot), Herkunft aller 6 Links weiterhin "im-research". Unverändert gegenüber der ersten QS, die Korrektur hat den Abschnitt "Weiterlesen und Sehen" nicht berührt.

Ergebnis Teil 2: Keine neuen Befunde in Fakten, Stil, Regelcheck oder Linkcheck. Die drei offenen [[LÜCKE]]-Marker sind unverändert und weiterhin korrekt als Lücke markiert, sie sind kein neuer Schaden, sondern derselbe bereits bekannte, ungefüllte Bestand. Für ihre Füllung bleibt eine Nachrecherche nötig, die laut Grundgesetz die aktive Freigabe von Tobi braucht und in diesem Lauf nicht stattfand.

### Ampel nach Korrektur

**Grün.** Alle zehn Korrekturen sitzen und korrekt gegen das Research-Doc geprüft, keine neuen Fakten, Stil, Regel oder Link-Befunde, `regel_check.py` rot 0 (gelb 3 ausschließlich aus den drei offenen, bereits korrekt markierten Lücken), `check_links.py` rot 0.

### Die drei wichtigsten Punkte der Nachprüfung

1. Alle zehn Anweisungen des Korrekturauftrags sind umgesetzt und stimmen mit dem Research-Doc überein, keine davon führt eine neue unbelegte Behauptung ein.
2. Prüfung 1 (Fakten) steht jetzt auf Grün, die vier ursprünglichen Befunde (Erdwall-Höhe, meistbesuchter Baum, fehlender Statusmarker, verzerrtes IUCN-Datenjahr) sind behoben.
3. Beide Skripte laufen unverändert sauber durch (rot 0 bei beiden), die einzigen verbliebenen Gelb-Befunde sind die drei bereits vor der Korrektur bekannten und korrekt markierten [[LÜCKE]]-Stellen, für die weiterhin Tobis Freigabe zur Nachrecherche aussteht.
