# Kenia-Buch

- `chapters.tsv`: Nummer, Trivialname, Lebensraum (aus der Notion-Kapitel-Datenbank)
- `research/NNN.txt`: Detail-Research pro Kapitel (Textkopie der Docs aus Drive `03_Recherche Kapitel`)
- `styleguides/`: Bild-Styleguide
- `prompts/`: der Bildprompt, mit dem das jeweilige Bild erzeugt wurde
- `illustrationen/`: Hauptbild pro Kapitel, `NNN_Trivialname_haupt.png`

Bilder erzeugen (überspringt Kapitel, die schon ein Bild haben):

    python3 generate_images.py            # alle Kapitel mit Research
    python3 generate_images.py 036 079    # einzelne Kapitel

Ein Bild neu erzeugen: PNG löschen, Script erneut starten.
