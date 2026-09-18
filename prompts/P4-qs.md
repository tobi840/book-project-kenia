# P4: QS pro Kapitel

Lokale Arbeitsfassung des Drive-Prompts "P4_QS pro Kapitel", mit den Entscheidungen vom 18.09.2026 eingebaut.

Ein Durchgang, fünf Prüfungen. Ausgabe ist eine Fundstellenliste, kein stiller Umbau. Tobi entscheidet, was übernommen wird.

## Auftrag

Prüfe das Kapitel `{NR}_{TRIVIALNAME}` gegen sein Research-Doc und den Text-Styleguide V2. **Ändere nichts am Text.**

Du schreibst dieses Kapitel nicht und hast es nicht geschrieben. Du prüfst es. Wenn dir eine bessere Formulierung einfällt, notiere sie als Fundstelle, setze sie nicht ein.

## Prüfung 1: Fakten

Jede Zahl, jedes Datum, jeder Name, jeder lokale Name gegen das Research-Doc.

Kategorien:
- `FALSCH`: steht anders im Research-Doc
- `UNBELEGT`: steht gar nicht im Research-Doc
- `STATUSFEHLER`: Überliefertes als gesichert dargestellt oder umgekehrt
- `VERZERRT`: Zahl stimmt, Kontext verschiebt die Bedeutung

Format je Fundstelle: `Zitatanfang | Kategorie | was im Text steht | was im Research-Doc steht`

Drei Fehlertypen sind im Pilot am häufigsten durchgerutscht. Prüfe sie gezielt, sie sehen harmlos aus:

- **Zuspitzung.** Der Text ist stärker als seine Quelle. "Primär in der Rinde" wurde zu "nicht im Holz, nicht in den Blättern". Ein Tonnageverhältnis wurde zu "auf jeden Baum kamen fünfzehn". Eine Aufzählung mit "darunter" wurde zu einer abgeschlossenen Liste. Ein einschränkender Nebensatz fiel weg. Das ist `VERZERRT`, bei abgeschlossenen Listen `FALSCH`. 14 der 19 Faktenbefunde des Piloten waren von dieser Art.
- **Körpermaße und Alltagsvergleiche.** Jeder Vergleich ("kleiner als eine Fingerkuppe", "erbsengroß", "eine Armlänge") muss im Research-Doc stehen. Steht er nicht dort, ist er `UNBELEGT`, auch wenn er stimmt. Die Docs führen Alltagsvergleiche als eigenen Punkt und sagen hin, wenn keiner ableitbar ist. Im Pilot liefen drei erfundene Vergleiche durch Erst- und Nachprüfung.
- **Erklärungen von Fachbegriffen.** Jede Umschreibung ist eine Tatsachenbehauptung und wird wie eine Zahl gegen das Doc geprüft. Ein Kürzel auszuschreiben ist keine Erklärung. "AFLP vergleicht die Länge vervielfältigter Bruchstücke des Erbguts" ist eine, und sie stand in keinem Doc.

## Prüfung 2: Stil

- Gedankenstriche ("–", "—"): verboten
- Verbotene Wörter: majestätisch, faszinierend, wunderschön, ikonisch, atemberaubend, Wunder der Natur
- Adjektivketten (drei oder mehr)
- Fazit-Sätze, Moral, Appelle
- Rhetorische Fragen ohne Rätsel-Setup
- Mehr als zwei Humor-Einwürfe
- Ende-Check: kehrt der letzte Absatz zum Anfangsbild zurück?
- Längen: Geschichte 900 bis 1.500 Wörter (gelb bis 1.800, rot darüber; weiche Untergrenze 700, harte 600), kein Absatz über 200 Wörter, erster Satz unter 25, letzter Absatz unter 80. **Nenne die tatsächlichen Werte.**
- Unerklärte Fachbegriffe. Erklärte Fachbegriffe gehören in Prüfung 1, nicht hierher.

## Prüfung 3: Vorlesbarkeit

- Schachtelsätze über drei Ebenen
- Zahlenreihen ohne Pause
- Lateinische Namen mitten im Satzfluss
- Sätze über 40 Wörter

Zischlaut-Häufungen meldest du nur, wenn der Satz beim lauten Lesen wirklich stolpert. Im Pilot führte ein solcher Befund dazu, dass ein Satz über Polizeigewalt umgebaut wurde, um drei sch-Laute zu entzerren. Der Nutzen war klein, das Risiko eines neuen Faktenfehlers beim Umbauen ist real.

## Prüfung 4: Struktur, Marker und Links

- Alle fünf Blöcke vorhanden (Kopf, Geschichte, Menschen und Kultur, Vor der Linse, Weiterlesen und Sehen)
- Kopfzeile: nur lokale Namen im Format `Sprache: „Name"`. Kein Englisch, kein Deutsch. Sprachbezeichnung **Maa**, nicht Maasai.
- Wiederholt "Menschen und Kultur" den Block 1, statt ihn zu ergänzen?
- Nennt "Vor der Linse" konkreten Ort, Tageszeit und eine Brennweite aus unserem Set?
- 3 bis 6 Links, jeder mit einem Satz Kontext
- URLs vollständig und im Research-Doc vorhanden. Konstruierte oder abweichende URLs melden. **Deep Research erfindet gelegentlich URLs, das ist der häufigste Fehlertyp.**
- **Kein `<p class="querverweis">` im Kapitel.** Querverweise setzt ein eigener Durchlauf, wenn alle Kapitel stehen. Ein Querverweis im Entwurf ist eine Fundstelle.
- **Marker getrennt auflisten**, das ist ampelrelevant:
  - `[[LÜCKE: …]]`, Pflichtfeld unbelegt. Jede einzeln, mit Zitat der Umgebung. Färbt gelb.
  - `[[OFFEN: …]]`, vom Research-Doc selbst als nicht belegbar ausgewiesen. Jede einzeln. Färbt nicht, wird für die gesammelte Nachrecherche eingesammelt.
  - Prüfe die Zuordnung. Ein `[[OFFEN]]` an einem Pflichtfeld ist falsch einsortiert und gehört als Fundstelle gemeldet.
  - Eine Seitenzahl gehört in keinen Marker. Dort steht `(S. XX)`.

## Prüfung 5: Sprachrichtigkeit

- Rechtschreibung, Zeichensetzung, Kongruenz
- Tempus: Präsens für Biologie, Präteritum für Geschichte. Auch bei Inversion am Satzanfang: nicht "Aufgedeckt hat das X", sondern "Das deckte X auf".
- **Jeder lateinische Artname kursiv**, auch Nebenarten, Wirtspflanzen, Erreger, Bestäuber, Synonyme und Familiennamen. Im Pilot standen sieben fremde Artnamen aufrecht, in drei von fünf Kapiteln, und drei QS-Läufe haben es nicht gemeldet.

## Werkzeuge

```
python3 scripts/regel_check.py chapters/{nr}-{slug}.html
```

Liefert die gemessenen Längen, Absatz- und Satzwerte sowie die Markerzahlen. Nimm diese Zahlen, statt selbst zu zählen.

```
python3 scripts/check_links.py chapters/{nr}-{slug}.html --research research/{nr}-{slug}.txt --offline
```

Prüft offline, ob jede URL wörtlich im Research-Spiegel steht. Das ist der Teil, der hier zählt, weil er den Fehler findet, den wir selbst verursachen: eine erfundene oder umgeschriebene Adresse.

**Die Erreichbarkeit der Links prüfst du nicht.** Der Egress-Proxy dieser Umgebung sperrt alle allgemeinen Webhosts. Ein gesammelter Linkcheck läuft einmal für alle Kapitel in einer Umgebung mit offenem Netz, vor dem Satz. Schreib "Erreichbarkeit: gesammelter Lauf steht aus" einmal in die Kopfzeile deiner Ausgabe und nicht noch einmal pro Link. Im Pilot stand derselbe Hinweis 25 mal in den Fundstellenlisten und danach noch einmal in jeder Nachprüfung.

## Ausgabe

Datei `qs/{nr}-{slug}.md`:

1. **Ampel aus Prüfung 1**
   - grün: keine Fundstellen in Prüfung 1
   - gelb: `UNBELEGT`, `STATUSFEHLER` oder `VERZERRT` in Prüfung 1
   - rot: mindestens ein `FALSCH` in Prüfung 1
2. Fundstellenliste je Prüfung
3. Die drei wichtigsten Punkte

Keine Lobsätze. Keine Zusammenfassung des Kapitelinhalts. Keine Vorschläge, die über die Fundstellen hinausgehen.

Die Ampel aus Prüfung 1 ist nur ein Teil der Gesamtampel. Diese Teilurteile lieferst du, zusammenrechnen tut der Workflow:

- rot aus Prüfung 1 (`FALSCH`), erfundene URL, fehlender Block, harte Längenuntergrenze aus `regel_check.py`
- gelb aus Prüfung 1 (`UNBELEGT`, `STATUSFEHLER`, `VERZERRT`), offene `[[LÜCKE]]`, gelbe Längenzone, Befunde aus Prüfung 2, 3 und 5
- nicht ampelrelevant: `[[OFFEN]]`, ungeprüfte Erreichbarkeit

## Bei der Nachprüfung

Die Nachprüfung nach einer Korrekturrunde ist **keine Abhakliste**. Sie prüft mit derselben Tiefe wie die Erstprüfung, weil die Korrektur neue Fehler einbauen kann. Im Pilot ist genau das in 2 von 5 Kapiteln passiert, und in einem weiteren ist ein neuer unbelegter Satz entstanden und nicht gefunden worden.

Halte sie trotzdem kurz. Umgesetzte Punkte nur als Liste, ohne Wiederholung des vollen Zitats. Ausführlich wird nur, was neu ist oder offen bleibt. Im Pilot waren drei von fünf QS-Dokumenten länger als das Kapitel, das sie prüfen.

## Was gegenüber Drive geändert ist

- Fünf Prüfungen statt vier, Sprachrichtigkeit ist eigenständig (Entscheidung Tobi).
- Längenzonen präzisiert (Entscheidung Tobi).
- Prüfung 4 und die Längenuntergrenze haben jetzt eine Konsequenz für die Gesamtampel, vorher hatte nur Prüfung 1 eine.
- Marker werden explizit aufgelistet, damit kein löchriges Kapitel grün durchläuft.
- Prüfer und Schreiber sind verschiedene Modelle mit getrenntem Kontext.

## Was nach dem Pilot 001 bis 005 dazugekommen ist

Entscheidungen Tobi vom 18.09.2026, Nummern wie im Entscheidungsstapel des Pilotberichts.

- E1: `[[LÜCKE]]` färbt gelb, `[[OFFEN]]` nicht.
- E2 und E3: Körpermaße und Erklärungen sind Prüfung 1, nicht Prüfung 2.
- E4: `VERZERRT` färbt gelb. Es war die größte Einzelkategorie und hatte keine Regel.
- E6 bis E9: Seitenzahl, Kopfzeilenformat, Sprachbezeichnung und Kursivsetzung sind jetzt benannte Prüfpunkte.
- E10: Erreichbarkeit raus aus der Ampel und raus aus der Fundstellenliste, gesammelter Lauf vor dem Satz.
- Querverweise: im Kapitel unerwünscht, eigener Durchlauf am Ende (Entscheidung Tobi).
- Zuspitzung als benannter Fehlertyp in Prüfung 1, aus dem häufigsten Pilotbefund.
- Nachprüfung mit voller Tiefe, aber kurzer Form.
