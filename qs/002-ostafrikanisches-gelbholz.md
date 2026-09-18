# QS 002: Ostafrikanisches Gelbholz (Podo)

## Ampel

Gesamtampel Prüfung 1: **rot** (ein FALSCH Befund)

Regelcheck (Skript): gelb, 0 rot, 3 gelb (ausschließlich die drei offenen Lücken)
Linkcheck (Skript): 4 Links, 0 erfundene URLs, 0 tote Links, 4 nicht prüfbar (Egress Policy sperrt die Hosts, das ist kein toter Link)

## Prüfung 1: Fakten

Format: Zitatanfang | Kategorie | was im Text steht | was im Research Doc steht

1. „Im selben Zeitfenster schiebt der Baum neue Blätter, blaugrau und hell gegen das dunkle Grün darunter.“ | FALSCH | Der Blattaustrieb wird an das Zeitfenster Dezember/Januar gehängt, denselben Satzabschnitt wie die Fruchtreife („Reif sind die Früchte meist im Dezember und Januar. Im selben Zeitfenster...“) | Das Research Doc verortet den Blattaustrieb ausdrücklich im Reisezeitraum 24.09. bis 12.10.: „Im festgelegten Reisezeitraum (24.09. bis 12.10.2026)... ist dokumentiert, dass Afrocarpus falcatus einen neuen Blattaustrieb (Flush) ausbildet.“ Das ist ein anderes Zeitfenster als Dezember/Januar, nicht dasselbe.

2. „und unter diesem Handelsnamen ging sein Holz um die Welt“ | UNBELEGT | Weltweiter Handel unter dem Namen „Podo“ | Das Research Doc belegt nur: „gehandelt unter dem Namen Podo oder Yellowwood“, dazu eine Liste industrieller Verwendungen (Schiffsbau, Eisenbahnschwellen, Möbel, Furniere, Instrumentenbau). Eine weltweite Verbreitung des Holzes steht nicht im Dokument.

3. „oft in einem Stück Wald, in dem noch kein Podo steht“ | UNBELEGT | Der Same lande oft dort, wo noch kein Podo wächst | Das Research Doc sagt nur: „Der unversehrte Samen wird durch den Kot (Endozoochorie) in großer Entfernung zum Mutterbaum in einem neuen Habitat ausgeschieden.“ Die Spezifizierung „noch kein Podo“ steht dort nicht.

Geprüft und in Ordnung (keine Fundstelle, zur Dokumentation der Prüftiefe): alle Höhen, Durchmesser, Blatt und Samenmaße, Rindenwerte, das Perm/Gondwana Alter, die Malapa/Sterkfontein Angabe, die Karura Chronologie (1902, 1932, 25 Prozent, 1998, Januar 1999, 2009, 2011, 15 Hektar, 100.000 Setzlinge, 70 Arten), die Tannin Spanne 3 bis 6 Prozent, die IUCN Einstufung 2013, das äthiopische Fällverbot 1994, alle lokalen Namen samt Sprachen, sowie die Statusmarkierungen „überliefert“ (Kikuyu Präfix Mũ, Pufferzone 18. Jahrhundert) und „wird vermutet“ (Pollenfreisetzung Ende September im Karura Forest) stimmen mit dem Research Doc überein.

## Prüfung 2: Stil

Gemessene Werte (aus regel_check.py): Geschichte 1085 Wörter, 9 Absätze, erster Satz 13 Wörter, letzter Absatz 44 Wörter, keine Sätze über 40 Wörter, 2 rhetorische Fragen, 1 lateinischer Name im Fließtext.

1. „Zwölf bis achtzehn Millimeter lang, glatt, fleischig, im schrägen Morgenlicht fast wie lackiert.“ | Adjektivkette: drei Merkmale hintereinander (lang, glatt, fleischig) vor demselben Bezugswort.

2. „Aus seinen Blättern wurde Podolid isoliert, ein Norditerpenlacton, das insektizid wirkt und im Reagenzglas gegen Leukämiezellen.“ | Unerklärter Fachbegriff: „Norditerpenlacton“ wird genannt, aber nicht erklärt, was diese Stoffklasse ist. Erklärt wird nur die Wirkung von Podolid, nicht der Fachbegriff selbst.

Sonst kein Befund: keine Gedankenstriche im Text, keine der verbotenen Wörter (majestätisch, faszinierend, wunderschön, ikonisch, atemberaubend, Wunder der Natur), rhetorische Fragen (2) beide als Rätsel Setup und innerhalb des Maximums, ein Humor Einwurf („Ein Baum, der seine eigenen Attrappen finanziert.“) innerhalb des Maximums von zwei, letzter Absatz kehrt zum Anfangsbild zurück (graugrüne Kugel im schrägen Morgenlicht), Körpermaß neben Zahl vorhanden (Stammdurchmesser neben Zimmertürhöhe).

## Prüfung 3: Vorlesbarkeit

1. „Sicherheitskräfte schlugen die Demonstranten nieder, doch die internationale Empörung stoppte die Bebauung.“ | Zischlaut Häufung: Sicherheitskräfte, schlugen, stoppte kurz hintereinander, beim lauten Vorlesen stolpert man hier.

Sonst kein Befund: keine Sätze über 40 Wörter (Skriptwert 0), keine Schachtelsätze über drei Ebenen aufgefallen, Zahlenreihen jeweils mit Komma oder Wortpause getrennt, lateinischer Name nur einmal im Fließtext (Skriptwert 1).

## Prüfung 4: Struktur und Links

- Alle fünf Blöcke vorhanden: Kopf, Geschichte, Menschen und Kultur, Vor der Linse, Weiterlesen und Sehen.
- „Menschen und Kultur“ wiederholt Block 1 nicht, sondern ergänzt Nutzung, Medizin, Ritual, IUCN Status.
- „Vor der Linse“ nennt konkreten Ort (Karura Forest, farbcodierte Wege, Amani Garden, KFEET Zentrum), Tageszeit (07:00 bis 10:00 Uhr, 15:30 bis 17:30 Uhr) und Brennweiten (150 bis 600, 45 mm).
- 4 Links, jeweils mit einem Satz Kontext (im Rahmen von 3 bis 6).
- Linkcheck: alle 4 URLs stehen im Research Doc (Herkunft „im-research“), 0 erfundene URLs, 0 tote Links. Alle 4 sind „nicht prüfbar“, weil die Egress Policy die Hosts sperrt, das zählt nicht als toter Link.

Offene [[LÜCKE]] Marker (3), einzeln mit Zitat der Umgebung:

1. „...bei den Kipsigis „Saptet“. [[LÜCKE: wörtliche Bedeutung dieser lokalen Namen, im Research-Doc nicht belegt]]“
2. „...aus Respekt vor den Ahnen kein Baum gefällt oder beschädigt werden darf. [[LÜCKE: überlieferte Legenden oder Sprichwörter zu dieser Baumart, im Research-Doc nicht belegt]]“
3. „Einen fruchtenden weiblichen Baum finden die FKF Ranger schneller als wir. [[LÜCKE: gemessene Fluchtdistanz der Mantelaffen gegenüber Fotografen, im Research-Doc nur als geschätzte 10 bis 20 Meter nahe dem KFEET-Zentrum]]“

Alle drei Lücken sind korrekt gesetzt: Das Research Doc markiert exakt diese drei Punkte selbst als „nicht belegt werden konnte“ beziehungsweise als Näherungswert.

## Prüfung 5: Sprachrichtigkeit

Kein Befund. Rechtschreibung, Zeichensetzung und Kongruenz unauffällig. Tempus korrekt verteilt: Präsens in den biologischen Passagen, Präteritum in den historischen Passagen (Wissenschaftsgeschichte, Karura Konflikt). Der lateinische Name ist korrekt geschrieben und kursiv gesetzt, im Kopf und einmal im Fließtext.

## Die drei wichtigsten Punkte

1. Ein FALSCH Befund färbt die Ampel von Prüfung 1 rot: Der Satz zum Blattaustrieb verlegt ihn in das Zeitfenster Dezember/Januar, das Research Doc verortet ihn aber ausdrücklich im Reisezeitraum Ende September bis Anfang Oktober.
2. Zwei UNBELEGT Zusätze gehen über das Research Doc hinaus: der weltweite Handel mit Podoholz und die Behauptung, der Same lande oft in podofreiem Wald.
3. Ansonsten hohe Faktentreue: alle Zahlen, Daten, Namen, lokalen Namen und Statusmarkierungen (überliefert, vermutet, gesichert) stimmen mit dem Research Doc überein, der Linkcheck zeigt keine erfundenen oder toten URLs, und alle drei offenen Lücken sind korrekt und vollständig markiert.

## Nachprüfung

### 1. Sind die sechs Korrekturen umgesetzt, und richtig?

1. Blattaustrieb entkoppelt von Fruchtreife: UMGESETZT. Neue Stelle: „Reif sind die Früchte meist im Dezember und Januar. Neue Blätter schiebt er zu einer anderen Zeit, beim Übergang von der langen Trockenzeit in die kleine Regenzeit Ende September und Anfang Oktober, blaugrau und hell gegen das dunkle Grün darunter.“ Der Zeitbezug ist jetzt korrekt an den Reisezeitraum (24.09. bis 12.10.) gehängt, „zu einer anderen Zeit“ trennt ihn explizit von der Dezember/Januar Fruchtreife. Deckt sich mit dem Research Doc.

2. Handelssatz gekürzt: UMGESETZT. Neue Stelle: „Im Swahili heißt der Baum „Podo“ oder „Mpodo“, unter diesem Namen wird sein Holz gehandelt.“ Der Zusatz „ging sein Holz um die Welt“ ist gestrichen, es bleibt nur die belegte Aussage (gehandelt unter dem Namen Podo). Die im Research Doc genannten Verwendungen (Schiffsbau, Eisenbahnschwellen, Möbel, Furniere, Instrumentenbau) stehen bereits im Abschnitt „Menschen und Kultur“, keine Dopplung nötig.

3. Same/Habitat Satz gekürzt: UMGESETZT. Neue Stelle: „Der Same kommt unversehrt wieder heraus, mit dem Kot, weit vom Mutterbaum, in einem neuen Lebensraum.“ Der unbelegte Zusatz „oft in einem Stück Wald, in dem noch kein Podo steht“ ist gestrichen, „neuer Lebensraum“ entspricht dem Research Doc („in einem neuen Habitat“).

4. Adjektivkette gekürzt: UMGESETZT. Neue Stelle: „Zwölf bis achtzehn Millimeter lang, fleischig, im schrägen Morgenlicht fast wie lackiert.“ Aus der Dreierkette „lang, glatt, fleischig“ ist „glatt“ gestrichen, es bleiben zwei Merkmale.

5. Fachbegriff erklärt: UMGESETZT. Neue Stelle: „Aus seinen Blättern wurde Podolid isoliert, ein bioaktiver Pflanzenstoff, der insektizid wirkt und im Reagenzglas gegen Leukämiezellen.“ „Norditerpenlacton“ ist durch die allgemeinverständliche Umschreibung „ein bioaktiver Pflanzenstoff“ ersetzt, eine Formulierung, die sich sogar wörtlich an das Research Doc anlehnt („bioaktive sekundäre Pflanzenstoffe“).

6. Zischlaut Häufung entzerrt: UMGESETZT. Neue Stelle: „Sicherheitskräfte gingen mit Gewalt gegen die Demonstranten vor. Die internationale Verurteilung zwang die Regierung, die Bebauung aufzugeben.“ Der Satz ist in zwei Sätze aufgeteilt, „schlugen ... nieder“ und „stoppte“ (beide mit sch/st Anlaut) sind ersetzt durch „gingen ... vor“ und „aufzugeben“. Die Zischlaut Ballung ist deutlich reduziert, der Fakteninhalt (Gewalt gegen Demonstranten, internationaler Druck stoppt Bebauung) bleibt korrekt erhalten.

Alle sechs Anweisungen sind umgesetzt und inhaltlich korrekt am Research Doc ausgerichtet.

### 2. Hat die Korrektur etwas kaputt gemacht?

**Prüfung 1 (Fakten), erneut vollständig durchgeführt:** Keine neuen FALSCH oder UNBELEGT Befunde. Die sechs korrigierten Stellen sind jetzt research-treu (siehe oben). Alle übrigen Fakten wurden erneut gegen das Research Doc gehalten (Höhen, Durchmesser, Blatt- und Samenmaße, Rindenwerte, Perm/Gondwana Alter, Malapa/Sterkfontein, Karura Chronologie 1902/1932/25%/1998/Januar 1999/2009/2011/15 Hektar/100.000 Setzlinge/70 Arten, Tannin 3 bis 6%, IUCN 2013, äthiopisches Fällverbot 1994, alle lokalen Namen, Statusmarkierungen „überliefert“/„wird vermutet“) und stimmen unverändert mit dem Research Doc überein. Die drei offenen [[LÜCKE]] Marker sind unverändert vorhanden und weiterhin korrekt gesetzt.

**Prüfung 2 (Stil), erneut vollständig durchgeführt:** Die beiden vormals bemängelten Stellen (Adjektivkette, unerklärter Fachbegriff) sind behoben. Keine neuen Stilverstöße: keine Gedankenstriche im gesamten Dokument, keine verbotenen Wörter, 2 rhetorische Fragen (unverändert, im Rahmen), 1 Humor Einwurf (unverändert), letzter Absatz kehrt weiter zum Anfangsbild zurück (graugrüne Kugel im schrägen Morgenlicht), Körpermaß neben Zahl weiterhin vorhanden. Wortzahl Geschichte jetzt 1095 (vorher 1085), unauffällig.

**Skript regel_check.py (--json):** `ampel_regelcheck: gelb`, `rot: 0`, `gelb: 3`. Die drei gelben Befunde sind ausschließlich die drei bereits bekannten, korrekt gesetzten [[LÜCKE]] Marker. Keine neuen Regelverstöße.

**Skript check_links.py (--json):** 4 Links, 0 erfundene URLs, 0 tote Links, 4 nicht prüfbar (Egress Policy sperrt die Hosts, alle 4 URLs stammen laut Skript aus dem Research Doc, Herkunft „im-research“). Unverändert gegenüber der ersten Prüfung, keine Regression.

**Zischlautprobe (Vorlesbarkeit), erneut geprüft:** Der einzige vormals bemängelte Satz ist entzerrt (siehe Punkt 6 oben). Keine neue Zischlaut Häufung an anderer Stelle aufgefallen.

**Gedankenstriche (Grundgesetz 5):** Datei durchsucht, keine Gedankenstriche (kurz oder lang) außerhalb der HTML Kommentar-Randzeichen `-->` im Metadatenblock gefunden.

Die Korrektur hat nichts Neues kaputt gemacht. Ampel Prüfung 1 wechselt von rot auf grün.

### Ampel nach Nachprüfung

- Prüfung 1 (Fakten): **grün** (0 FALSCH, 0 UNBELEGT, keine neuen Befunde)
- Regelcheck (Skript): gelb, 0 rot, 3 gelb (weiterhin nur die drei offenen Lücken)
- Linkcheck (Skript): 4 Links, 0 erfundene URLs, 0 tote Links, 4 nicht prüfbar

### Weiterhin offen

- Drei [[LÜCKE]] Marker bleiben unverändert bestehen, da das Research Doc dazu explizit keine Angaben liefert: wörtliche Bedeutung der lokalen Namen (Maa, Samburu, Kamba, Kipsigis), überlieferte Legenden oder Sprichwörter zur Baumart, exakte gemessene Fluchtdistanz der Mantelaffen (nur Näherungswert 10 bis 20 Meter im Research Doc). Schließen dieser Lücken erfordert Nachrecherche, die laut Grundgesetz nur mit Freigabe von Tobi läuft.
- Die 4 Weiterlesen Links bleiben technisch nicht prüfbar (Egress Policy), das ist laut Vorgabe kein Fehlerbefund, sondern ein offener Prüfstatus, sollte aber nicht mit „geprüft und in Ordnung“ verwechselt werden.
