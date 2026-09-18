# P3: Kapitel schreiben

Lokale Arbeitsfassung des Drive-Prompts "P3_Kapitel schreiben", mit den Entscheidungen vom 18.09.2026 eingebaut. Abweichungen gegenüber Drive sind unten unter "Was gegenüber Drive geändert ist" aufgeführt.

## Grundlagen

- `styleguide/01-text-styleguide.md` (Text-Styleguide V2)
- `styleguide/02-kapitel-template.md` (Kapitel-Template, HTML)
- Das Research-Doc der Art. Es ist Gesetz.

## Vorgehen

1. Lies das Research-Doc vollständig, bevor du schreibst.
2. Entscheide, welches der vier Elemente das Kapitel trägt: These, Name, Mechanismus oder Menschen. Gewichte danach.
3. Wähle das Anfangsbild und notiere es dir, der letzte Absatz kehrt dorthin zurück.
4. Schreib.

## Harte Vorgaben

- **Der gegebene Kontext ist Gesetz.** Jede Zahl, jedes Datum, jeder Name, jeder lokale Name, jede URL steht im Research-Doc. Nichts aus Modellwissen ergänzen, auch nicht, wenn du es sicher weißt.
- **Nicht nachrecherchieren.** Keine Websuche, kein Abruf externer Quellen. Was fehlt, fehlt.
- **Lücken markieren, nicht füllen:** `[[LÜCKE: was fehlt]]` im Fließtext an der Stelle, an der die Information hingehört.
- **Status übernehmen:** gesichert, vermutet, beobachtet, überliefert. Das Research-Doc markiert das, der Text auch.
- Geschichte: 900 bis 1.500 Wörter, 6 bis 9 Absätze.
- Kein Absatz über 200 Wörter.
- Erster Satz der Geschichte unter 25 Wörtern.
- Letzter Absatz der Geschichte unter 80 Wörtern.
- Keine Gedankenstriche, weder "–" noch "—". Punkt, Komma, Doppelpunkt, Klammer.
- Das Ende kehrt zum Anfangsbild zurück. Kein Fazit, keine Moral, kein Allgemeinplatz.
- Mindestens eine wichtige Zahl bekommt ein Körpermaß daneben.
- Höchstens zwei Humor-Einwürfe, höchstens zwei rhetorische Fragen und die nur als Rätsel-Setup.
- Lateinischer Name kursiv, im Kopf und höchstens einmal im Fließtext.
- "Menschen und Kultur" ergänzt Block 1, wiederholt ihn nicht.
- "Vor der Linse" nennt einen konkreten Ort auf unserer Route, eine Tageszeit und eine Brennweite aus unserem Set (100 bis 400, 150 bis 600, 45 mm, 26 bis 60).
- "Weiterlesen und Sehen": 3 bis 6 Links, jeder mit einem Satz Kontext. Nur URLs, die vollständig im Research-Doc stehen. Keine konstruierten oder zusammengesetzten Adressen.

## Wenn das Research-Doc dünn ist

Der Text darf kürzer werden. Lieber 780 belegte Wörter als 1.200 mit Nebel. Atmosphäre ist kein Ersatz für Substanz.

- 900 bis 1.500 Wörter: Norm.
- 700 bis 899 Wörter: zulässig, wenn der Substanz-Check das Research-Doc als dünn markiert hat. Sonst nachschärfen.
- 600 bis 699 Wörter: weiche Untergrenze unterschritten. Geht nur mit dünnem Research-Doc durch und landet im Entscheidungsstapel.
- Unter 600 Wörtern: harte Untergrenze. Das ist kein Kapitel mehr. Nicht mit Füllmaterial strecken, sondern als "zu dünn" melden.
- 1.500 bis 1.800 Wörter: gelb, kürzen.
- Über 1.800 Wörter: rot.

Nachrecherche läuft nie automatisch. Sie braucht die aktive Freigabe von Tobi.

## Ausgabe

Eine Datei `chapters/{nr}-{slug}.html` nach `styleguide/02-kapitel-template.md`. Danach, außerhalb der Datei, in deiner Antwort:

1. Alle `[[LÜCKE]]`-Marker auflisten.
2. In einem Satz nennen, welches Element das Kapitel trägt und warum.
3. Das Ergebnis von `python3 scripts/regel_check.py chapters/{nr}-{slug}.html`.

## Selbstprüfung vor der Abgabe

Führe `python3 scripts/regel_check.py <datei>` aus und behebe, was das Skript meldet. Höchstens zwei Runden. Bleibt danach etwas offen, melde es, statt es zu verstecken.

## Was gegenüber Drive geändert ist

- Ausgabeformat HTML statt Markdown, Frontmatter als HTML-Kommentar (Entscheidung Tobi).
- Längenzonen präzisiert: Norm 900 bis 1.500, gelb 1.500 bis 1.800, rot über 1.800, weiche Untergrenze 700, harte Untergrenze 600 (Entscheidung Tobi).
- Explizites Verbot der Nachrecherche, mit dem Freigabeweg über Tobi (Entscheidung Tobi).
- Selbstprüfung gegen `scripts/regel_check.py` ergänzt, damit deterministisch Prüfbares nicht in der QS landet.
- Die Drive-Regel "höchstens drei bis fünf Kapitel pro Chat, dann neuer Chat, sonst driftet der Stil" ist hier strukturell gelöst: jedes Kapitel bekommt einen eigenen Agenten mit eigenem Kontext.
