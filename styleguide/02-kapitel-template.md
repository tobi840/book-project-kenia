# Kapitel-Template (HTML)

Jedes Kapitel folgt exakt dieser Struktur. Die Blöcke 3 bis 5 sind kurz und visuell abgesetzt, damit man sie beim Vorlesen überspringen oder gezielt aufschlagen kann.

Gegenüber der Drive-Fassung ist das Ausgabeformat von Markdown auf HTML umgestellt (Entscheidung Tobi, 18.09.2026), damit sich der Entwurf direkt im Browser ansehen lässt. Inhalt, Reihenfolge und Längen bleiben identisch. Das Frontmatter wandert in einen HTML-Kommentar am Dateianfang, die Überschriften werden zu `h2`, die Blöcke zu `section` mit festen Klassennamen. `scripts/regel_check.py` prüft gegen genau diese Klassennamen.

## Blöcke

**Kopf.** LEBENSRAUM in Versalien (z. B. RIFT VALLEY, LAIKIPIA, KÜSTE, TSAVO, AMBOSELI, NAIROBI), Trivialname (Deutsch), lateinischer Name kursiv, danach die belegten lokalen Namen im Format `Sprache: „Name"`, mehrere Namen einer Sprache durch Komma. Sprachbezeichnung buchweit einheitlich: **Maa** für die Sprache, **Maasai** nur für Menschen. Englische und deutsche Handelsnamen gehören nicht in die Namenszeile. Die Namenszeile trägt die vollständige Liste, der Fließtext höchstens drei Namen (E13).

**1. Geschichte.** 800 bis 1.300 Wörter nach Text-Styleguide (E18). Vier Bewegungen: These und Erscheinung, Herkunft und Name, Mechanismus, Menschen. Ende als Bild. **Kein Querverweis.** Den setzt ein eigener Durchlauf, wenn alle Kapitel stehen, 20 bis 30 auf 100 Kapitel. Siehe Text-Styleguide Abschnitt 9.

**2. Menschen und Kultur.** 150 bis 250 Wörter. Was die Art für Menschen in Kenia bedeutet oder bedeutet hat: Nutzung, Medizin, Mythos, Sprichwort, Konflikt, Schutzstatus, heutige Rolle (Tourismus, Landwirtschaft, Wilderei, Naturschutz). Nur Belegtes. Legenden als Legenden markiert. Wenn die Geschichte in Block 1 schon stark kulturell ist, wird dieser Block kürzer und ergänzt statt zu wiederholen.

**3. Vor der Linse.** 100 bis 200 Wörter, gegliedert in drei Zeilen.
- *Wo und wann:* Ort auf unserer Route, Tageszeit, Verhalten, das man abwarten sollte (z. B. Ansitz am Wasser, Flug zum Schlafbaum, Blütezeit im Oktober)
- *Brennweite:* Empfehlung aus unserem Set. 100 bis 400 oder 150 bis 600 für Vögel und scheue Säuger. 45 mm für Bäume im Kontext, Blätter, Rinde, Landschaft. 26 bis 60 für Pflanzen nah, Details, Umgebung. Bei Bäumen: Perspektive (von unten in die Krone, Silhouette bei Gegenlicht, Rinde als Fläche)
- *Bild-Idee:* Ein konkreter Bildvorschlag, der die Geschichte des Kapitels aufgreift. Startwerte nur, wenn sie aus dem Verhalten folgen (z. B. "Vogel im Flug: 1/2000 s oder schneller")

**4. Weiterlesen und Sehen.** 3 bis 4 Links, jeder mit einem Satz Kontext (E19). Typen: Quelle (Fachartikel, Kew, IUCN, Birds of the World, Feldführer), Fotos (iNaturalist, Flickr-Commons, Wikimedia), Ruf (bei Vögeln: xeno-canto, Macaulay Library), Verbreitungskarte (eBird, GBIF, IUCN), Kultur (Museum, Ethnobotanik-Datenbank, Dokumentation). Format: Linktext ist der Titel der Seite, danach ` · ` und ein Satz, was man dort findet. Im QS wird geprüft, ob jede URL wörtlich im Research-Doc steht. Die Erreichbarkeit ist nachrangig und kein Gate vor dem Satz (E14).

**5. Illustration.** Hauptbild oben unter dem Kopf, Hochformat. Optionales Detailbild neben Block 3 oder 4, quadratisch. Im Entwurf bleibt die `figure` leer und trägt `data-status="offen"`, gefüllt wird sie in Phase Illustration.

## Dateiformat

Datei: `chapters/{nr}-{slug}.html`, UTF-8, `nr` dreistellig, `slug` aus dem Trivialnamen (Kleinbuchstaben, Umlaute ausgeschrieben, Bindestriche).

```html
<!--
nr: 042
kategorie: Baum
lebensraum: Tsavo / Amboseli
trivialname: Affenbrotbaum
lateinisch: Adansonia digitata
swahili: Mbuyu
lokal:
status: entwurf
qs_ampel: offen
research_doc: <Google-Docs-ID>
-->
<article class="kapitel" data-nr="042">

  <header class="kapitel-kopf">
    <p class="lebensraum">TSAVO / AMBOSELI</p>
    <h1>Affenbrotbaum</h1>
    <p class="lateinisch"><em>Adansonia digitata</em></p>
    <p class="namen">Swahili: „Mbuyu“</p>
  </header>

  <figure class="illustration" data-status="offen">
    <figcaption>Bild-Idee in einem Satz, dient als Briefing für die Illustration.</figcaption>
  </figure>

  <section class="geschichte">
    <h2>Geschichte</h2>
    <p>…</p>
    <!-- Kein Querverweis beim Schreiben. Der Durchlauf am Ende setzt hier, falls dieses
         Kapitel einen bekommt, genau eine Zeile ein:
         <p class="querverweis"><em>Auch die Dum-Palme (S. XX) …</em></p> -->
  </section>

  <section class="menschen-kultur">
    <h2>Menschen und Kultur</h2>
    <p>…</p>
  </section>

  <section class="vor-der-linse">
    <h2>Vor der Linse</h2>
    <p><strong>Wo und wann:</strong> …</p>
    <p><strong>Brennweite:</strong> …</p>
    <p><strong>Bild-Idee:</strong> …</p>
  </section>

  <section class="weiterlesen">
    <h2>Weiterlesen und Sehen</h2>
    <ul>
      <li><a href="https://…">Titel der Seite</a> · Ein Satz, was man dort findet.</li>
    </ul>
  </section>

</article>
```

Offene Stellen werden im Fließtext als `[[LÜCKE: was fehlt]]` markiert und nie aus Modellwissen gefüllt.

## Marker im Text

Nur noch einer:

- `[[LÜCKE: was fehlt]]` steht für ein unbelegtes **Pflichtfeld**: Lebensraum, Trivialname, lateinischer Name, mindestens ein belegter lokaler Name, Ort in "Vor der Linse", Brennweite, Bild-Idee, drei bis vier Links. Färbt die Ampel gelb.

`[[OFFEN]]` ist seit E15 abgeschafft. Was das Research-Doc als nicht belegbar ausweist, steht im Kapitel gar nicht, auch nicht als Marker. Der Marker hatte zwei Abnehmer, die gesammelte Nachrecherche und den Entscheidungsstapel, und seit E11 und E12 keinen mehr.

Eine fehlende Seitenzahl ist keine Lücke. Dort steht `(S. XX)`.
