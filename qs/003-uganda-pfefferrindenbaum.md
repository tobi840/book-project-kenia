# QS Kapitel 003: Uganda-Pfefferrindenbaum (Warburgia ugandensis)

Research-Doc: 1C-HftgJiJucqcwcwW2KC0AmQm1ffMq_XYDHxp4QM1cs
Kapiteldatei: chapters/003-uganda-pfefferrindenbaum.html

## Ampel

**Prüfung 1 (Fakten): gelb.** Ein Fund in der Kategorie UNBELEGT, kein FALSCH, kein STATUSFEHLER, kein VERZERRT.

Werkzeug-Ergebnisse (übernommen, nicht selbst gezählt):
- `regel_check.py`: Ampel gelb, 0 rot, 8 gelb (alle 8 Befunde sind offene LÜCKE Marker), Geschichte 929 Wörter, 8 Absätze, erster Satz 14 Wörter, letzter Absatz 53 Wörter, keine Sätze über 40 Wörter, 1 rhetorische Frage, 1 lateinischer Name im Fließtext, 5 Links.
- `check_links.py`: 5 Links, 0 erfundene URLs, 0 tote Links, 5 nicht prüfbar (Egress-Policy sperrt die Hosts, alle 5 Herkunft „im-research“).

## Prüfung 1: Fakten

1. „Dass Rinde und Blätter in Kenia und Uganda seit Langem gegen Malaria abgekocht werden, bekommt damit einen Mechanismus.“ | UNBELEGT | Text nennt Kenia und Uganda als Anwendungsgebiet und „seit Langem“ als Zeitrahmen | Research-Doc, Abschnitt 5 („Menschen und Kultur in Kenia“): „Vor allem aber werden Rinde und Blätter in wässrigen Abkochungen konsumiert, um Malaria zu behandeln [gesichert]9.“ Die Praxis ist im Research-Doc nur für Kenia belegt, ein Ugandabezug für diese konkrete Anwendung fehlt, ebenso jede Zeitangabe wie „seit Langem“.

Keine weiteren Befunde in Prüfung 1. Alle geprüften Zahlen (Höhen 4,3 bis 15,0 m, Kronendurchmesser 2,3 bis 5,1 m, BHD 0,08 bis 0,26 m, Höhenlage 1.800 bis 2.500 m, Niederschlag 650 bis 1.500 mm, IC50 5,7 µg/ml, CC50 14,7 µg/ml, Selektivitätsindex 2,6, Darmepithel-Wert unter 50 µg/ml, umstrittene 7,6 und 6,4 µg/ml, Maus-Werte über 250 µg/ml und LD50 über 5.000 mg/kg, Zeitraum Januar 2003 bis Dezember 2021, 197 Pflanzenarten, 1.170 Tests, 223 AFLP-Bänder, H = 0,1278 bis 0,2892, 54/46 Prozent, Jahre 2008/2012, 1.620 Stecklinge, 7,5 cm, 10 Prozent Schattennetz, Holzdichte 1.010 kg/m³ bzw. umstrittene 500 bis 650 kg/m³, Erstbeschreibung 1906 durch Sprague, Brennweiten und Ortsangabe Karura Forest auf 1.700 m), alle lokalen Namen (mgurure, Mũthĩga, Olsokonoi, ol-mororoi, Soroko mit Unschärfe-Hinweis, Sinendet, Abasi, Mukuzanume, masuko, mukhungula, kagua) und alle Statusmarkierungen (gesichert, umstritten, überliefert, vermutlich) stimmen mit dem Research-Doc überein, einschließlich der korrekt übernommenen Unsicherheitsstatus bei den widersprüchlichen Toxizitätswerten und bei der Kikuyu-Überlieferung zu Zahnschmerzen.

## Prüfung 2: Stil

1. „Eine genetische Kartierung mit 223 polymorphen AFLP-Bändern brachte dann einen unerwarteten Befund.“ | Unerklärter Fachbegriff | „AFLP“ wird nicht aufgeschlüsselt oder umschrieben, anders als bei „Domatien“ oder „Aposematismus“ im Styleguide-Vorbild.

Keine Gedankenstriche, keine der verbotenen Wörter (majestätisch, faszinierend, wunderschön, ikonisch, atemberaubend, „Wunder der Natur“), keine Adjektivketten ab drei Gliedern, kein Fazit-Satz oder Appell, die eine Rhetorische Frage ist ein Rätsel-Setup mit sofortiger Auflösung, kein Humor-Einwurf über dem Limit, letzter Absatz kehrt zum Anfangsbild zurück (Rinde kauen, Zunge brennt, Pfeffergeschmack), Körpermaß (Unterarm) neben einer wichtigen Zahl (BHD) vorhanden. Längen laut `regel_check.py` durchgehend im grünen Bereich.

## Prüfung 3: Vorlesbarkeit

Keine Befunde. Keine Schachtelsätze über drei Ebenen, keine auffälligen Zischlaut-Häufungen, Zahlenreihen sind durch Satzgrenzen unterbrochen, der einzige Fließtext-Beleg des lateinischen Namens steht am Satzende und unterbricht den Redefluss nicht, laut `regel_check.py` kein Satz über 40 Wörter.

## Prüfung 4: Struktur und Links

Alle fünf Blöcke sind vorhanden (Kopf, Geschichte, Menschen und Kultur, Vor der Linse, Weiterlesen und Sehen). „Menschen und Kultur“ ergänzt Block 1 (Nutzung, Material, Überlieferung) statt ihn zu wiederholen. „Vor der Linse“ nennt einen konkreten Ort (Karura Forest, 1.700 m), begründet das Fehlen einer Tageszeitangabe und nennt mehrere Brennweiten aus dem Set (100 bis 400, 150 bis 600, 45 mm, 26 bis 60 mm).

1. „GBIF: Warburgia ugandensis · Taxonomische Einordnung, Synonyme, umgangssprachliche Namen und Fundpunkte der Art.“ | Kontextsatz erweitert | Das Research-Doc beschreibt den GBIF-Eintrag nur als „taxonomische Klassifizierung, Synonyme und umgangssprachliche Namen“ (Abschnitt 8). „Fundpunkte der Art“ steht so nicht im Research-Doc.

Links insgesamt: 5, jeder mit einem Satz Kontext, alle URLs laut `check_links.py` vollständig, im Research-Doc vorhanden und nicht erfunden. Erreichbarkeit bei allen 5 „nicht-prüfbar“ (Egress-Policy), das ist kein toter Link.

Offene `[[LÜCKE]]`-Marker, einzeln mit Zitat der Umgebung (8, wie von `regel_check.py` gezählt):

1. „Woher der Gattungsname stammt, steht in den Quellen nicht. [[LÜCKE: Herkunft und Bedeutung des Gattungsnamens Warburgia]]“
2. „Was diese Wörter wörtlich bedeuten, ist nirgends übersetzt. [[LÜCKE: wörtliche Bedeutung der lokalen Namen, etwa „Sinendet“ und „Mũthĩga“]]“
3. „Für Kamba, Samburu und Giriama liegen gar keine geprüften Namen vor. [[LÜCKE: verifizierte Bezeichnungen bei Kamba, Samburu und Giriama]]“
4. „Den Pollen tragen kleine Insekten, vor allem Bienen der Gattung Trigona. [[LÜCKE: Maße für Blätter, Früchte und Samen]]“
5. „[[LÜCKE: Unterschiede zwischen Geschlechtern und Altersstufen]]“ (unmittelbar im Anschluss an Punkt 4, gleiche Textstelle)
6. „…verwertbare Exemplare sind in freier Wildbahn zunehmend schwer zu finden. [[LÜCKE: absolute Bestandszahlen mit Jahresangabe]]“
7. „Eine Tageszeit nennt die Literatur nicht, doch weil die bestäubenden Trigona-Bienen tagaktiv sind, bleibt vermutlich nur das Tageslicht. [[LÜCKE: Blattaustrieb, Blüte und Fruchtreife für Ende September bis Anfang Oktober]]“
8. „Ruhiger: die frische Schnittstelle in der Rinde, heller Splint gegen dunkles Grau, daneben ein erstarrter Harztropfen. [[LÜCKE: typische fotografische Fehler und artspezifische Verschlusszeiten]]“

## Prüfung 5: Sprachrichtigkeit

1. „Benannt hat die Art der schottische Botaniker Thomas Archibald Sprague, 1906, im Journal of the Linnean Society, Botany und im Kew Bulletin.“ und „Aufgedeckt hat das der Forscher Kubo in den späten 1970er Jahren.“ | Tempus-Inkonsistenz | Beide Sätze stehen im Perfekt, während die übrige Wissenschaftsgeschichte im Präteritum steht: „Muchugi und Kollegen legten diese Arbeiten 2008 und 2012 vor.“ Der Styleguide verlangt Präteritum für Geschichte.

Rechtschreibung, Zeichensetzung und Kongruenz unauffällig. Lateinischer Name durchgehend korrekt geschrieben und kursiv (Kopf und die eine Nennung im Fließtext). Diakritische Zeichen bei „Mũthĩga“ konsistent mit dem Research-Doc.

## Die drei wichtigsten Punkte

1. Der Text hält die Statusmarkierungen (gesichert, umstritten, überliefert, vermutlich) fast durchgängig exakt so wie im Research-Doc, das ist der stärkste Befund dieser QS.
2. Ein Satz weitet eine nur für Kenia belegte Aussage (Malariabehandlung durch Abkochung) unbelegt auf Uganda aus und ergänzt eine nicht belegte Zeitangabe.
3. Acht offene `[[LÜCKE]]`-Marker sind korrekt gesetzt und nicht heimlich gefüllt, das Kapitel ist trotz dünner Quellenlage an mehreren Stellen ehrlich offen.
