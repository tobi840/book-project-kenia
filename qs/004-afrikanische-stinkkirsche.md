# QS 004: Afrikanische Stinkkirsche (Prunus africana)

## Ampel Prüfung 1: ROT

Werkzeugausgaben (übernommen, nicht selbst gezählt):
- `regel_check.py`: Ampel gelb, rot: 0, gelb: 4 (alles offene [[LÜCKE]]-Marker). Geschichte 1064 Wörter, 9 Absätze, erster Satz 14 Wörter, letzter Absatz 47 Wörter, Sätze über 40 Wörter: 0, rhetorische Fragen: 1, lateinisch im Fließtext: 1, Links: 6, Lücken: 4.
- `check_links.py`: 6 Links, erfundene_urls: 0, tote_links: 0, nicht_pruefbar: 6 (alle Hosts von der Egress-Policy gesperrt, daher ungeprüft, nicht tot). Alle 6 URLs mit Herkunft "im-research".

## Prüfung 1: Fakten

1. „im Herbarium der Kew Gardens liegt, unter der Nummer K000107419“ | UNBELEGT | Text benennt „Kew Gardens“ als Aufbewahrungsort des Typusexemplars | Research-Doc nennt nur „heute im K Herbarium, K000107419“. „Kew Gardens“ taucht im Research-Doc nur im Zusammenhang mit dem Briefwechsel Mann/Hooker auf, nicht als expliziter Name des Herbariums.

2. „Maa: „Olkojuk““ | FALSCH | Text ordnet den Namen „Olkojuk“ der Sprache/Ethnie „Maa“ zu | Research-Doc-Tabelle listet die Ethnie durchgehend als „Maasai“, nicht als „Maa“.

3. „Alle diese Stoffe sind fettlöslich, und alle sitzen vor allem an einer Stelle: in der Rinde. Nicht im Holz, nicht in den Blättern.“ | VERZERRT | Text behauptet Ausschließlichkeit: die Wirkstoffe seien nicht im Holz und nicht in den Blättern vorhanden | Research-Doc: „Da die Wirkstoffe primär in der Rinde sitzen“. „Primär“ ist keine Exklusivitätsaussage zu Holz oder Blättern.

4. „Auf jeden Baum, den diese Rechnung erlaubte, kamen also fünfzehn.“ | VERZERRT | Text verwandelt ein Tonnage-Verhältnis in eine Aussage über einzelne Bäume | Research-Doc nennt nur Tonnenzahlen: „über 5.000 Tonnen Rinde“ exportiert gegen „330 Tonnen“ nachhaltig. Kein Beleg für eine Umrechnung in Baum-Stückzahlen oder das Verhältnis „fünfzehn“ pro Baum.

5. „2007 wurde der Handel für Madagaskar, Uganda, Kamerun und Burundi zeitweise ganz ausgesetzt.“ | VERZERRT | Text stellt die vier genannten Länder als vollständige Liste dar | Research-Doc: „wurde der Handel für zahlreiche Länder, darunter Madagaskar, Uganda, Kamerun und Burundi, zeitweise komplett suspendiert“. Die vier sind laut Research-Doc nur Beispiele aus einer größeren, nicht näher bezifferten Gruppe von Ländern.

6. „Unter der Borke liegt das Phloem, die Leitung, die den Zucker aus den Blättern nach unten bringt.“ | UNBELEGT | Text beschreibt die Transportfunktion des Phloems (Zucker aus den Blättern nach unten) | Research-Doc beschreibt an dieser Stelle nur die mikroskopische Faserstruktur des Phloems (lange, dünnwandige, nicht verholzte Fasern in tangentialen Gruppen). Die Zuckertransport-Funktion steht dort nicht.

7. „Tief stehende Sonne am frühen Morgen, sonst verschluckt das Kronendach den Kontrast.“ | UNBELEGT | Text legt die Tageszeit auf den frühen Morgen fest | Research-Doc nennt für den Kontrast nur „tief stehende Sonne“, ohne Tageszeit zu spezifizieren. Ob Morgen oder Abend gemeint ist, steht dort nicht.

## Prüfung 2: Stil

Keine Fundstellen. Keine Gedankenstriche, keine verbotenen Wörter, keine Adjektivketten ab drei, ein Humor-Einwurf: keiner, rhetorische Fragen: 1 von maximal 2 (als Rätsel-Setup verwendet). Längenwerte siehe Werkzeugausgabe oben, alle im grünen Bereich.

## Prüfung 3: Vorlesbarkeit

1. „Er hat dem Baum im Holzhandel den Namen „Red Stinkwood“ eingetragen, Rotes Stinkholz, und der deutsche Trivialname übersetzt ihn mit.“ | Das Bezugswort von „Er“ ist beim Vorlesen nicht eindeutig zu klären: das vorangehende Subjekt im Satzverlauf ist „den Geruch von Blausäure“, nicht der Baum und keine Person.

2. „wo Elaeodendron paniculata mit 214 Zählungen und Croton megalocarpus die Bestände prägen“ | Zwei lateinische Artnamen folgen unmittelbar aufeinander mitten im Satzfluss, ohne deutschen Zwischentext oder Sprechpause.

## Prüfung 4: Struktur und Links

Alle fünf Blöcke vorhanden (Kopf, Geschichte, Menschen und Kultur, Vor der Linse, Weiterlesen und Sehen). „Menschen und Kultur“ ergänzt Block 1, statt ihn zu wiederholen. „Vor der Linse“ nennt Ort (Karura Forest, City Park), Tageszeit und zwei Brennweiten. Links: 6, alle mit Kontextsatz, keine erfundene URL laut `check_links.py`, alle sechs Hosts nicht prüfbar wegen Egress-Sperre.

Strukturbefund:
1. „Auch das Ostafrikanische Gelbholz (S. XX) steht im Karura Forest und wurde für das, was in seinem Stamm steckt, eingeschlagen.“ | Der Platzhalter „S. XX“ für die Seitenzahl ist keine Lücke, die dem Format [[LÜCKE: ...]] folgt, sondern ein unmarkierter Platzhalter.

Offene [[LÜCKE]]-Marker (aus `regel_check.py`, einzeln mit Umgebung):
1. „... wobei dieser dritte Name teils auch für eine andere Art verwendet wird, für Nuxia congesta. [[LÜCKE: ob die Kikuyu-Schreibung „Mueri“ eine orthografische Variante von „Muiri“ ist, einen Ort in den Aberdares bezeichnet oder einen heiligen Waldhain, ist aus den Quellen nicht zu klären]] Bei den Kalenjin im Rift Valley heißt er ...“
2. „... Im Swahili laufen die Handelsnamen „Kiburabura“ und „Mfuwate“. [[LÜCKE: wörtliche Bedeutung dieser lokalen Namen, im Research-Doc nicht belegt]]“
3. „... Zu suchen sind frische Austriebe an den Zweigenden und die 3 bis 8 Zentimeter langen Blütentrauben in den Blattachseln. Reife purpurrote Früchte sind in diesem Fenster ausgeschlossen. [[LÜCKE: ob am konkreten Reisedatum bereits geöffnete Blüten zu erwarten sind, hängt am Einsetzen der Regen und ist nicht vorhersagbar]] [[LÜCKE: ob im Raum Nairobi Setzlinge der abweichenden Kakamega-Variante ausgepflanzt wurden, was die Bestimmung erschweren würde, ist ungeklärt]]“ (zwei Marker in derselben Umgebung)

## Prüfung 5: Sprachrichtigkeit

1. „für eine andere Art verwendet wird, für Nuxia congesta“ / „wo Elaeodendron paniculata mit 214 Zählungen und Croton megalocarpus die Bestände prägen“ | Die lateinischen Artnamen Nuxia congesta, Elaeodendron paniculata und Croton megalocarpus stehen nicht kursiv, obwohl Prüfung 5 kursive Schreibung für lateinische Namen verlangt.

2. „Swahili: „Kiburabura“, „Mfuwate“. Kikuyu: „Muiri“, „Mwiria“, „Muchorowe“. ...“ | Format weicht vom Styleguide ab. Styleguide-Vorgabe: „Lokale Namen in Anführungszeichen mit Sprache: „Mbuyu“ (Swahili)“, also Name zuerst, Sprache in Klammern danach. Das Kapitel nutzt stattdessen „Sprache: „Name““.

Tempus: Präsens für Biologie-Absätze, Präteritum für Geschichtsabsätze durchgehend korrekt eingehalten. Keine weiteren Rechtschreib- oder Zeichensetzungsfehler gefunden.

## Die drei wichtigsten Punkte

1. Ein FALSCH-Befund (Sprachname „Maa“ statt „Maasai“ im Kopf) färbt die Gesamtampel aus Prüfung 1 rot.
2. Drei VERZERRT-Befunde verschieben die Bedeutung korrekter Zahlen aus dem Research-Doc: Wirkstoff-Exklusivität in der Rinde, die „fünfzehn Bäume“-Rechnung und die Länderliste der Handelsaussetzung 2007.
3. Formatfehler bei lateinischen Namen (fehlende Kursivierung bei drei Fremdarten) und ein unmarkierter Seitenzahl-Platzhalter „(S. XX)“ statt eines [[LÜCKE]]-Markers.

## Nachprüfung (Korrektur vom Korrekturauftrag)

Geprüft: Kapiteldatei `chapters/004-afrikanische-stinkkirsche.html` nach Anwendung des Korrekturauftrags mit 12 Punkten, gegen Research-Doc `research/004-afrikanische-stinkkirsche.txt` und die anderen vier Kapitel/Templates im Arbeitsverzeichnis. Kapiteldatei wurde für diese Nachprüfung nicht verändert.

### Teil 1: Wurde jede Anweisung umgesetzt, und richtig?

1. „Maa: „Olkojuk““ → „Maasai“ | UMGESETZT, RICHTIG. Kopf jetzt: „... Kalenjin: „Tenduet“, „Chebitet“, „Yemit“, „Remit“. **Maasai**: „Olkojuk“. Samburu: ...“. Stimmt mit der Research-Doc-Tabelle überein, die durchgehend „Maasai“ listet.

2. „Kew Gardens“ → „K Herbarium“ | UMGESETZT, RICHTIG. Text jetzt: „... präparierte das Typusexemplar, das heute **im K Herbarium** liegt, unter der Nummer K000107419.“ Deckt sich mit Research-Doc: „heute im K Herbarium, K000107419“.

3. „Nicht im Holz, nicht in den Blättern.“ gestrichen | UMGESETZT, RICHTIG. Text jetzt: „Alle diese Stoffe sind fettlöslich, und alle sitzen vor allem an einer Stelle: in der Rinde. Wer sie haben will, muss schälen.“ Keine Exklusivitätsbehauptung zu Holz/Blättern mehr, deckt sich mit „primär in der Rinde“ im Research-Doc.

4. „Auf jeden Baum ... kamen also fünfzehn.“ umformuliert | UMGESETZT, RICHTIG. Text jetzt: „Nachhaltig wären nach wissenschaftlichen Analysen 330 Tonnen gewesen. **Geerntet wurde also fünfzehnmal so viel, wie nachhaltig gewesen wäre.**“ Bezieht sich jetzt auf Tonnage (5.000 t vs. 330 t ≈ Faktor 15), keine Baum-Stückzahlen mehr, exakt wie im Korrekturvorschlag vorgegeben.

5. Länderliste 2007 ergänzt | UMGESETZT, RICHTIG. Text jetzt: „2007 wurde der Handel **unter anderem** für Madagaskar, Uganda, Kamerun und Burundi zeitweise ganz ausgesetzt.“ Deckt sich mit Research-Doc: „für zahlreiche Länder, darunter Madagaskar, Uganda, Kamerun und Burundi“.

6. Phloem-Funktionsbeschreibung gestrichen | UMGESETZT, RICHTIG. Text jetzt: „Unter der Borke liegt das Phloem, **die Leitung des Baumes**. Unter dem Mikroskop besteht es aus langen, dünnwandigen, nicht verholzten Fasern, die in tangentialen Gruppen liegen und mit Siebgewebe abwechseln.“ Der Nebensatz zum Zuckertransport ist weg, der Rest deckt sich mit der mikroskopischen Beschreibung im Research-Doc.

7. Tageszeit „am frühen Morgen“ | UMGESETZT, RICHTIG (beide Optionen kombiniert). Text jetzt: „Tief stehende Sonne, sonst verschluckt das Kronendach den Kontrast. **[[LÜCKE: Tageszeit nicht im Research-Doc spezifiziert]]**“ Tageszeitangabe entfernt und zusätzlich als Lücke markiert, deckt sich mit Research-Doc, das nur „tief stehende Sonne“ ohne Tageszeit nennt.

8. Kursivierung der lateinischen Fremdartnamen | UMGESETZT, RICHTIG. Alle drei jetzt kursiv: „für <em>Nuxia congesta</em>“ (Zeile 33), „wo <em>Elaeodendron paniculata</em> mit 214 Zählungen ... daneben <em>Croton megalocarpus</em>“ (Zeile 43). `<em>`/`</em>`-Tags sind paarig und ausgeglichen (6/6).

9. Platzhalter „(S. XX)“ im Querverweis → [[LÜCKE: Seitenzahl fehlt]] | UMGESETZT, RICHTIG IM WORTLAUT DER ANWEISUNG, ABER NEUES STRUKTURPROBLEM (siehe Teil 2, Punkt A). Text jetzt: „Auch das Ostafrikanische Gelbholz **[[LÜCKE: Seitenzahl fehlt]]** steht im Karura Forest ...“

10. Bezugswort von „Er“ geklärt | UMGESETZT, RICHTIG. Text jetzt: „**Dieser Geruch** hat dem Baum im Holzhandel den Namen „Red Stinkwood“ eingetragen, Rotes Stinkholz, und der deutsche Trivialname übersetzt ihn mit.“ Bezug ist jetzt eindeutig der zuvor beschriebene Blausäuregeruch, nicht mehr lesbar als Baum oder Person.

11. Latein-Namen entzerrt | UMGESETZT, RICHTIG. Text jetzt: „wo Elaeodendron paniculata mit 214 Zählungen **die Bestände prägt, daneben** Croton megalocarpus.“ Die beiden Artnamen sind durch deutschen Zwischentext getrennt, decken sich beim Vorlesen nicht mehr unmittelbar.

12. Namenszeilen-Format „Name“ (Sprache) vs. Sprache: „Name“ | GEPRÜFT, BEWUSST NICHT GEÄNDERT. Der Auftrag lautete „prüfen“, nicht „ändern“. Befund: Der Text-Styleguide (`styleguide/01-text-styleguide.md`, Abschnitt 5) schreibt „Lokale Namen in Anführungszeichen mit Sprache: „Mbuyu“ (Swahili)“, also Name zuerst. Das Kapitel-Template (`styleguide/02-kapitel-template.md`) zeigt im eigenen Beispiel jedoch „Swahili: „Mbuyu““, also Sprache zuerst, und genau dieses Format nutzen alle fünf Kapitel im Buch (001 bis 005) durchgängig, auch Kapitel 004 selbst. Eine Änderung nur in Kapitel 004 hätte das Kapitel gegen die restlichen vier Kapitel und gegen das Template inkonsistent gemacht. Nicht-Ändern war hier die richtige Entscheidung, siehe Teil 3.

### Teil 2: Hat die Korrektur etwas Neues kaputt gemacht?

**A. Neues Strukturproblem durch Punkt 9.** Kapitel 004 markiert den Seitenzahl-Platzhalter im Querverweis jetzt als `[[LÜCKE: Seitenzahl fehlt]]`. Alle anderen vier Kapitel nutzen weiterhin `(S. XX)`, exakt wie im Kapitel-Template vorgegeben:
- 001: „Auch das Ostafrikanische Gelbholz (S. XX) wächst in Nairobi ...“
- 002: „Auch die Heilige Würgefeige (S. XX) steht in Nairobi ...“
- 003: „Auch das Ostafrikanische Gelbholz (S. XX) verteidigt sich ...“
- 005: „Auch der Uganda-Pfefferrindenbaum (S. XX) trägt seine Abwehrchemie ...“

Kapitel 004 ist damit das einzige der fünf Kapitel mit abweichender Notation. Das ist kein Fakten- oder Recherchefehler, aber ein neuer Strukturbefund gegenüber Prüfung 4 (Struktur und Links), der vor der Korrektur nicht bestand (vorher nutzte auch Kapitel 004 „(S. XX)“, siehe ursprünglicher Struktur-Befund in Prüfung 4 oben, der genau diesen unmarkierten Platzhalter monierte).

**B. Keine sonstigen neuen Fakten-, Stil- oder Vorlesbarkeitsprobleme gefunden.** Der gesamte Fließtext wurde erneut Satz für Satz gegen das Research-Doc geprüft (Namen, Zahlen, Daten, Prozesse). Keine neuen Abweichungen. Wortzahl Geschichte jetzt 1.051 (vorher 1.064), weiterhin innerhalb 900 bis 1.500. Absatzzahl unverändert 9. Kein Satz über 40 Wörter. Eine rhetorische Frage, wie vorher, im erlaubten Rahmen als Rätsel-Setup. Keine Gedankenstriche im Text (geprüft per Unicode-Scan auf U+2013/U+2014: keine Treffer). Keine Ausrufezeichen im Fließtext. Keine verbotenen Wörter (majestätisch, faszinierend, wunderschön, ikonisch, atemberaubend, „wahres Wunder“) gefunden. `<em>`-Tags paarig.

### Werkzeugausgaben (diese Nachprüfung)

`python3 scripts/regel_check.py chapters/004-afrikanische-stinkkirsche.html --json`:
- Ampel Regelcheck: gelb (unverändert gelb, ausschließlich wegen offener [[LÜCKE]]-Marker, keine roten Befunde)
- rot: 0, gelb: 6 (alle sechs Meldungen sind offene Lücken, keine neue über die erwarteten hinaus: die vier ursprünglichen plus die zwei durch Punkt 7 und Punkt 9 neu und korrekt gesetzten Lücken)
- Geschichte: 1.051 Wörter, 9 Absätze, erster Satz 14 Wörter, letzter Absatz 47 Wörter, Sätze über 40 Wörter: 0, rhetorische Fragen: 1, lateinisch im Fließtext (Hauptart): 1, Links: 6, Lücken: 6

`python3 scripts/check_links.py chapters/004-afrikanische-stinkkirsche.html --research research/004-afrikanische-stinkkirsche.txt --json`:
- Links: 6, erfundene_urls: 0, tote_links: 0, nicht_pruefbar: 6 (alle sechs Hosts weiterhin von der Egress-Policy gesperrt, daher ungeprüft, nicht tot, wie schon in der ersten QS)
- Alle 6 URLs unverändert mit Herkunft „im-research“

### Ampel Nachprüfung: GELB

Kein FALSCH-, VERZERRT- oder UNBELEGT-Befund mehr offen. Alle sieben ursprünglichen Prüfung-1-Befunde sind korrekt behoben, ebenso die Vorlesbarkeits- und Kursivierungs-Befunde. Nicht mehr rot. Gelb statt grün, weil zwei Punkte eine Entscheidung von Tobi brauchen (Seitenzahl-Platzhalter-Konvention und Namenszeilen-Format, siehe Teil 3), keiner davon ist aber ein Fehler im Sinne von falsch/erfunden/unbelegt.

### Teil 3: Was weiterhin offen ist beziehungsweise entschieden werden muss

1. Seitenzahl-Platzhalter buchweit uneinheitlich: Kapitel 004 nutzt `[[LÜCKE: Seitenzahl fehlt]]`, Kapitel 001, 002, 003 und 005 nutzen `(S. XX)` wie im Kapitel-Template vorgegeben. Muss entschieden werden: entweder wird `(S. XX)` in allen Kapiteln (und im Template) auf `[[LÜCKE: Seitenzahl fehlt]]` umgestellt, oder Kapitel 004 wird zur Konsistenz auf `(S. XX)` zurückgesetzt. Keine der beiden Optionen lässt sich aus dem Research-Doc ableiten, es ist eine Produktions-/Konventionsfrage.
2. Namenszeilen-Format im Kopf uneinheitlich zwischen Text-Styleguide (Abschnitt 5: „Name“ (Sprache)) und der tatsächlichen Praxis in Kapitel-Template und allen fünf Kapiteln (Sprache: „Name“). Muss entschieden werden: Styleguide-Text anpassen, um die etablierte Praxis zu kodifizieren, oder alle fünf Kapitel und das Template auf das im Styleguide beschriebene Format umstellen. Kapitel 004 wurde für diese Frage bewusst nicht verändert, um keine zusätzliche Inkonsistenz zu erzeugen.
3. Die bereits aus der ersten QS bekannten, unverändert offenen [[LÜCKE]]-Marker (Kikuyu „Mueri“, wörtliche Namensbedeutungen, Blühzeitpunkt am Reisedatum, Kakamega-Variante in Nairobi) bleiben zu Recht offen, sie sind keine neuen Befunde und werden hier nicht erneut aufgeführt.
