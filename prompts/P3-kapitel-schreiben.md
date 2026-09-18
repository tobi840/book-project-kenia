# P3: Kapitel schreiben

Lokale Arbeitsfassung des Drive-Prompts "P3_Kapitel schreiben", mit den Entscheidungen vom 18.09.2026 eingebaut. Abweichungen gegenüber Drive stehen unten unter "Was gegenüber Drive geändert ist".

## Grundlagen

- `styleguide/01-text-styleguide.md` (Text-Styleguide V2)
- `styleguide/02-kapitel-template.md` (Kapitel-Template, HTML)
- Das Research-Doc der Art. Es ist Gesetz.
- `research/namen-bedeutungen.md`. Geschlossener Vermerk, wird nicht fortgeführt. Enthält die wenigen Namensbedeutungen, die vor dem Abbruch der Recherche belegt wurden. Für diese Namen ist er verbindlich wie das Research-Doc.

## Vorgehen

1. Lies das Research-Doc vollständig, bevor du schreibst.
2. Entscheide, welches der vier Elemente das Kapitel trägt: These, Name, Mechanismus oder Menschen. Gewichte danach.
3. Wähle das Anfangsbild und notiere es dir, der letzte Absatz kehrt dorthin zurück.
4. Schreib.

## Harte Vorgaben

- **Der gegebene Kontext ist Gesetz.** Jede Zahl, jedes Datum, jeder Name, jeder lokale Name, jede URL steht im Research-Doc. Nichts aus Modellwissen ergänzen, auch nicht, wenn du es sicher weißt.
- **Nicht nachrecherchieren.** Keine Websuche, kein Abruf externer Quellen. Was fehlt, fehlt. Ohne Ausnahme. Es gibt keine gesammelte Nachrecherche mehr, auch nicht für Namensbedeutungen und nicht für die Fotografie.
- **Vorbehaltswörter wandern mit.** Steht im Quellsatz eines dieser Wörter, steht in deinem Satz auch eins:

  > darunter, unter anderem, vor allem, primär, überwiegend, hauptsächlich, meist, in der Regel, verschiedene, typischerweise, insbesondere, zum Beispiel

  Das ist keine Stilfrage, sondern die einzige Fassung der Zuspitzungsregel, die man beim Schreiben befolgen kann. "Spitze nicht zu" hilft nicht, weil du beim Schreiben nicht siehst, welcher Satz zugespitzt ist. "Nimm das Wort mit" siehst du.

  Konkret aus dem Pilot: das Doc schrieb "Die **primäre** Pollenübertragung erfolgt durch Wind, Vögel, Insekten und kletternde Säugetiere", das Kapitel schrieb "Den Pollen tragen Wind, Vögel, Insekten und kletternde Säugetiere". Ein Wort weg, aus einer Hauptursache eine vollständige Liste. Zwei QS-Runden haben es nicht gefunden.

- **Zuspitzung ist Erfindung.** Aus einem Beispiel wird keine Liste, aus "primär" kein "nur", aus "in Kenia" kein "in Ostafrika", aus "häufig" kein Superlativ, aus einem Verhältnis zwischen Mengen keine Aussage über einzelne Stücke. Wenn ein Satz stärker klingt als seine Quelle, ist er falsch. Das war im Pilot der häufigste Fehler, in 5 von 5 Kapiteln, 19 von 30 Befunden.
- **Kein Alltagsvergleich, den das Research-Doc nicht wörtlich liefert.** Nicht "mannshoch", nicht "erbsengroß", nicht "so hoch wie ein einstöckiges Gebäude", nicht "wie mit dem Daumennagel eingedrückt". Die Docs führen Alltagsvergleiche als eigenen Punkt und schreiben hin, wenn sich keiner ableiten lässt. Liefert das Doc keinen, steht die Zahl allein, und der Satz bleibt kürzer. Ein erfundener Vergleich ist ein Faktenfehler, kein Stilmittel. Der Styleguide zitiert Droris Körpermaße als Vorbild, das gilt für seine Arten, nicht für unsere (E16).
- **Eine Erklärung ist eine Tatsachenbehauptung.** Erklär einen Fachbegriff nur mit dem, was das Research-Doc über ihn sagt. Reicht das nicht, benutz den Begriff nicht, sondern ein Alltagswort. Ein Kürzel auszuschreiben ist keine Erklärung und bleibt erlaubt, wenn die Langform im Doc steht.
- **Status übernehmen:** gesichert, vermutet, beobachtet, überliefert. Das Research-Doc markiert das, der Text auch.
- Geschichte: 800 bis 1.300 Wörter, 5 bis 9 Absätze. **Ziel sind 880, nicht 800.** Das untere Ende ist kein Notfall. Ein Kapitel mit 880 belegten Wörtern ist besser als eines mit 1.150, von denen 300 Nebel sind.

  Der Grund für die 880 ist die Patch-Reserve. Ein Patch kann nur streichen. Kapitel 008 kam mit 804 Wörtern aus dem Schreiben, die QS strich drei zugespitzte Sätze, danach standen 776 da: unter der Norm, ohne dass jemand einen Fehler gemacht hätte. Im Batch sitzt kein Schreiber mehr daneben, der auffüllt, und ein zweiter Schreiberlauf ist nur bei **rotem** Regel-Check vorgesehen. Also liefert der Schreiber die Reserve gleich mit. Sie besteht aus belegter Substanz, nicht aus Nebel: Nebel ist genau das, was die QS anschließend herausstreicht.

- Keine zeitliche Zuspitzung. „Den ganzen Tag", „rund um die Uhr", „unermüdlich" steht in keinem Research-Doc, und zweimal in zwei Kapiteln stand im Doc etwas anderes: der Sekretär ruht mittags im Schatten, Jacksons Wida springt „tagtäglich", nicht den ganzen Tag. `regel_check.py` meldet die drei Wendungen jetzt gelb.
- Kein Absatz über 200 Wörter.
- Erster Satz der Geschichte unter 25 Wörtern.
- Letzter Absatz der Geschichte unter 80 Wörtern.
- Keine Gedankenstriche, weder Halbgeviertstrich (U+2013) noch Geviertstrich (U+2014). Punkt, Komma, Doppelpunkt, Klammer.
- Das Ende kehrt zum Anfangsbild zurück. Kein Fazit, keine Moral, kein Allgemeinplatz.
- Höchstens zwei Humor-Einwürfe, höchstens zwei rhetorische Fragen und die nur als Rätsel-Setup.
- **Jeder lateinische Name steht kursiv, Gattung wie Art**, auch der von Nebenarten, Wirtspflanzen, Erregern, Bestäubern und Synonymen, und auch der allein stehende Gattungsname. Kein Ermessen. Nicht kursiv sind Handels- und Drogennamen, auch wenn sie wie ein Taxon aussehen. Die Regel "höchstens einmal im Fließtext" gilt nur für die Art des Kapitels.
- **Tempus:** Wissenschaftsgeschichte im Präteritum, auch bei Inversion am Satzanfang. Nicht "Aufgedeckt hat das X", sondern "Das deckte X auf".
- "Menschen und Kultur" ergänzt Block 1, wiederholt ihn nicht.
- "Vor der Linse" nennt einen konkreten Ort auf unserer Route, eine Tageszeit und eine Brennweite aus unserem Set (100 bis 400, 150 bis 600, 45 mm, 26 bis 60).

## Die Kopfzeile

In die Namenszeile kommen nur lokale Namen mit Sprachangabe, im Format `Sprache: „Name"`. Mehrere Namen einer Sprache durch Komma.

- Handelsnamen auf Englisch oder Deutsch gehören nicht dorthin. Das sind keine lokalen Namen.
- Die Sprachbezeichnung ist buchweit einheitlich: **Maa** für die Sprache, **Maasai** nur für Menschen. Also "Maa: „Oretiti"", nicht "Maasai: „Oretiti"".
- Der lateinische Name steht kursiv im Kopf.

### Im Fließtext höchstens drei Namen

Die Namenszeile trägt die vollständige Liste. Der Fließtext wiederholt sie **nicht**.
Im Pilot stand jeder Name zweimal im Kapitel, Kapitel 004 zählte vierzehn Namen auf.
Vorgelesen ist das eine Litanei aus Wörtern, die niemand behält.

Im Fließtext stehen deshalb höchstens **drei** lokale Namen, und nur solche, an denen
etwas hängt: eine belegte Bedeutung, eine Zuordnungsfrage, ein Gebrauch, der später im
Kapitel wieder vorkommt. Die Zahl der übrigen darf als Satz auftauchen ("Sieben Sprachen
haben einen eigenen Namen für ihn"), die Aufzählung nicht.

Fehlt für eine Sprache ein Name, ist das **kein Marker**. Die Liste hat keine Sollgröße.

## Nur noch ein Marker

**`[[LÜCKE: was fehlt]]`** setzt du, wenn ein **Pflichtfeld** des Templates unbelegt bleibt. Das färbt die Ampel gelb und landet im Entscheidungsstapel. Pflichtfelder sind: Lebensraum, Trivialname, lateinischer Name, mindestens ein belegter lokaler Name, Ort in "Vor der Linse", Brennweite, Bild-Idee.

**`[[OFFEN]]` gibt es nicht mehr (E15).** Was das Research-Doc als nicht belegbar ausweist, steht im Kapitel gar nicht, auch nicht als Marker. Kein Satz, keine Klammer, keine Notiz.

Der Grund ist rechnerisch. Der Marker hatte zwei Abnehmer: die gesammelte Nachrecherche und den Entscheidungsstapel. Die Nachrecherche ist seit E11 und E12 eingestellt, ampelrelevant war er nie. Im Pilot standen fünfzehn davon in fünf Kapiteln, einer lautete "typische fotografische Fehler, vom Research-Doc als nicht thematisiert ausgewiesen". Niemand wird das je bearbeiten. Geschrieben, geprüft, aufgelistet, nachgeprüft und am Ende von Hand gelöscht wird es trotzdem, fünfmal bezahlt für null Ertrag.

Wenn das Doc eine Frage offen lässt, hat das Kapitel diese Frage nicht. Fehlt die Fluchtdistanz, steht in "Vor der Linse" nichts über Fluchtdistanz. Das ist kein Mangel, sondern ein kürzerer Text.

Die Ausnahme ist die Zuordnungsfrage, die den Text trägt: dass unklar ist, ob „Mueri" und „Muiri" dasselbe Wort sind, ist eine Geschichte und gehört als Satz in den Fließtext, mit Status "ungeklärt". Nicht als Marker, sondern als Sprache.

Eine fehlende Seitenzahl ist auch keine Lücke. Dort steht `(S. XX)`, buchweit, so wie im Template. Die Seitenzahl entsteht im Satz.

## Querverweise: beim Schreiben keine

Du schreibst **keinen** Querverweis. Der Absatz `<p class="querverweis">` bleibt weg.

Der Grund: ein Schreiber, der nur sein eigenes Kapitel kennt und trotzdem einen Verweis liefern muss, nimmt den schwächsten verfügbaren Zusammenhang. Im Pilot zeigten drei von fünf Verweisen auf dasselbe Kapitel, und zwei von fünf begruendeten sich mit "wächst auch in Nairobi". Das ist kein Zusammenhang, das ist ein Zufall der Auswahl.

Die Verweise setzt ein eigener Durchlauf, wenn alle Kapitel stehen. Er sieht alle 100 auf einmal und findet deshalb bessere Paare, als du es kannst. Regeln dieses Durchlaufs, hier nur zur Kenntnis:

- 20 bis 30 Verweise auf 100 Kapitel, also etwa jedes vierte Kapitel.
- Kein Kapitel häufiger als zweimal Ziel.
- Der Verweis braucht einen sachlichen Zusammenhang: derselbe Mechanismus, dasselbe Molekül, dieselbe Geschichte, derselbe Konflikt. Ein gemeinsamer Ort reicht nicht.
- Seitenzahl als `(S. XX)`, im Satz aufgelöst.

## Namensbedeutungen

Die wörtliche Bedeutung eines lokalen Namens schreibst du nur, wenn eine von zwei
Quellen sie hergibt:

- das Research-Doc der Art, oder
- `research/namen-bedeutungen.md` mit Status `belegt`.

Sonst schreibst du keine. Kein Marker nötig, die Bedeutung ist kein Pflichtfeld.

**Du leitest nie selbst ab.** Nicht aus dem Wortstamm, nicht aus einer Nachbarsprache,
nicht aus einem Präfix. Dass "Mũ-" eine Nominalklasse markiert, ist keine Bedeutung.
Das ist die eine Regel, die von der eingestellten Namensrecherche übrig bleibt, und sie
gilt ohne Ausnahme.

Recherchiert wird dafür nichts mehr, weder von dir noch gesammelt.

## Wenn das Research-Doc dünn ist

Der Text darf kürzer werden. Lieber 780 belegte Wörter als 1.200 mit Nebel. Atmosphäre ist kein Ersatz für Substanz.

- 800 bis 1.300 Wörter: Norm.
- 650 bis 799 Wörter: zulässig, wenn der Substanz-Check das Research-Doc als dünn markiert hat. Sonst nachschärfen.
- 550 bis 649 Wörter: weiche Untergrenze unterschritten. Geht nur mit dünnem Research-Doc durch und landet im Entscheidungsstapel.
- Unter 550 Wörtern: harte Untergrenze. Das ist kein Kapitel mehr. Nicht mit Füllmaterial strecken, sondern als "zu dünn" melden.
- 1.300 bis 1.600 Wörter: gelb, kürzen.
- Über 1.600 Wörter: rot.

Nachrecherche gibt es nicht mehr, weder automatisch noch auf Freigabe (E11, E12).

## Ausgabe

Eine Datei `chapters/{nr}-{slug}.html` nach `styleguide/02-kapitel-template.md`. Danach, außerhalb der Datei, in deiner Antwort:

1. Alle `[[LÜCKE]]`-Marker auflisten.
2. In einem Satz nennen, welches Element das Kapitel trägt und warum.
3. Das Ergebnis beider Skripte.

## Selbstprüfung vor der Abgabe

**Du rufst kein Skript auf.** Die Hauptsession lässt `regel_check.py` und
`research_check.py` einmal über dein Kapitel laufen, sobald du fertig bist. Ihre
Ausgabe geht an den Prüfer, nicht an dich. Der Grund ist Geld: ein Agent, der
Skripte startet und ihre Ausgabe liest, kostete in der Messung das Vierfache
eines Agenten, der nur seine drei Dateien liest.

Was die Skripte finden, hast du also nicht mehr selbst in der Hand. Zurück
bekommst du ein Kapitel genau einmal, und nur bei **rotem** Regel-Check: harte
Untergrenze von 550 Wörtern unterschritten, fehlender Block, Gedankenstrich.
Gelbe Befunde gehen durch, korrigiert werden sie später als Patch.

Diese beiden prüfst du darum vor der Abgabe von Hand, weil ein Patch sie nicht
mehr reparieren kann:

- **Länge.** Zähl die Wörter der Geschichte. Unter 800 ist gelb, unter 550 ist
  kein Kapitel. Ein Patch darf nur streichen, also wird ein zu kurzes Kapitel
  nie länger.
- **Gedankenstriche.** Weder Halbgeviertstrich (U+2013) noch Geviertstrich (U+2014). Das färbt sofort rot.

Alles Übrige findest du nur, indem du deinen eigenen Text gegen das Research-Doc
liest: verschluckte Vorbehaltswörter, unbelegte Erklärungen von Fachbegriffen,
Statusfehler. In Kapitel 006 sind genau dort fünf Abweichungen entstanden, die
weder die Skripte noch die erste QS-Runde gefunden haben, zwei davon ein
weggelassenes „insbesondere".

Was kein Skript findet, findest du nur, indem du deinen eigenen Text noch einmal gegen das Research-Doc liest: unbelegte Erklärungen von Fachbegriffen und Statusfehler.

## Was gegenüber Drive geändert ist

- Ausgabeformat HTML statt Markdown, Frontmatter als HTML-Kommentar (Entscheidung Tobi).
- Längenzonen präzisiert und später gesenkt: Norm 800 bis 1.300, gelb bis 1.600, rot darüber, weiche Untergrenze 650, harte Untergrenze 550 (Entscheidung Tobi, zuletzt E18).
- Explizites Verbot der Nachrecherche, mit dem Freigabeweg über Tobi (Entscheidung Tobi).
- Selbstprüfung gegen `scripts/regel_check.py` ergänzt, damit deterministisch Prüfbares nicht in der QS landet.
- Die Drive-Regel "höchstens drei bis fünf Kapitel pro Chat, dann neuer Chat, sonst driftet der Stil" ist hier strukturell gelöst: jedes Kapitel bekommt einen eigenen Agenten mit eigenem Kontext.

## Was nach dem Pilot 001 bis 005 dazugekommen ist

Entscheidungen Tobi vom 18.09.2026, Nummern wie im Entscheidungsstapel des Pilotberichts.

- E1: `[[LÜCKE]]` ist ampelrelevant. Die zweite Markersorte ist seit E15 weg.
- E2: Körpermaße nur aus dem Research-Doc.
- E3: Fachbegriffserklärungen unterliegen dem Grundgesetz.
- E5: Namensbedeutungen nur aus Research-Doc oder belegtem Vermerk, nie selbst abgeleitet.
- E6: `(S. XX)` buchweit, kein Marker für Seitenzahlen.
- E7 und E8: Kopfzeile, Format `Sprache: „Name"`, Maa gegen Maasai, kein Englisch und Deutsch.
- E9: alle lateinischen Namen kursiv, Gattung wie Art.
- Querverweise: beim Schreiben keine, stattdessen ein Durchlauf am Ende mit 20 bis 30 Verweisen auf 100 Kapitel (Entscheidung Tobi, 18.09.2026).
- Dazu ohne Entscheidungsbedarf: Zuspitzungsregel und Tempusregel, beide aus gemessenen Pilotbefunden.

Entscheidungen Tobi vom 18.09.2026, zweite Runde, nach dem Korrekturlauf:

- E11: keine Fotografie-Nachrecherche. Fluchtdistanz, Blühzeitpunkt im Reisefenster und
  Aufnahmetechnik bleiben offen, wenn das Research-Doc sie nicht hergibt.
- E12: die gesammelte Namensrecherche ist eingestellt. Ein brauchbares Ergebnis aus
  sechzehn Namen rechtfertigt den Aufwand nicht. Das Verbot der Eigenableitung bleibt.
- E13: im Fließtext höchstens drei lokale Namen, die vollständige Liste nur in der
  Namenszeile. Fehlende Namen sind kein Mangel.

Entscheidungen Tobi vom 18.09.2026, dritte Runde, nach dem Prozessdurchgang:

- E15: `[[OFFEN]]` ist abgeschafft. Was das Research-Doc nicht hergibt, steht nicht
  im Kapitel, auch nicht als Marker.
- E16: kein Alltagsvergleich ohne wörtlichen Beleg. Die Styleguide-Regel "jede Zahl
  bekommt ein Körpermaß" ist gestrichen, sie hat die Fehler erzeugt.
- E17: Vorbehaltswörter wandern mit. Positive Fassung der Zuspitzungsregel.
- E18: Längenzonen gesenkt, Norm 800 bis 1.300 Wörter.
- E19: 3 bis 4 Links statt 3 bis 6. Seit E21 gegenstandslos.
- E20: die QS liefert Patches statt Prosa, das Korrekturmodell entfällt. Siehe P4.

- E21: Der Block "Weiterlesen und Sehen" entfällt ganz. Du schreibst keine Links
  mehr, weder Adresse noch Kontextsatz. Damit fällt die Fehlerklasse weg, die im
  Pilot am häufigsten auftrat.
- E22: Höchstens zwei QS-Runden je Kapitel, angestrebt ist eine. Was die zweite
  Runde nicht findet, bleibt im Buch. Schreib entsprechend vorsichtig: ein Satz,
  den du nicht aus dem Doc belegen kannst, wird nicht mehr von einer dritten
  Runde eingefangen.
- E23: QS-Dokumente sind Arbeitsmaterial für ein Skript, nicht für Tobi.
