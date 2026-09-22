# Übergabe 22.09.2026: Kapitel 028 bis 100

Alle 100 Kapitel liegen in `chapters/`. 028 bis 100 hat Codex (Modell
gpt-5.6-luna, Effort high) geschrieben, geprüft und gepatcht, mit Tobis
Pipeline (P3, Skripte, P4, `patch_anwenden.py`). Branch
`claude/exciting-wozniak-h93njf`, alles gepusht.

## Was gelaufen ist

1. **Schreiben und QS** (`scripts/codex_batch.py`): drei Kapitel je Worker,
   QS-Runde 2 nur bei rot. Ergebnis je Kapitel in `berichte/codex-batch.tsv`.
   Rund 63k Tokens je Kapitel.
2. **Nachpatch und Glättung**: 43 abgelehnte QS-Patches waren
   Umformulierungen. Ein zweiter Prüferlauf hat sie als Streichung oder
   wörtliches Zitat neu gefasst (`qs/*-nachpatch.md`). Danach ein Lauf, der
   eingeklebte Research-Sätze wieder gekürzt hat (`qs/*-glaettung.md`).
3. **Vorlese-Durchgang** (`prompts/P7-vorlesen.md`,
   `scripts/vorlesen_batch.py`): ein Schreiber streicht Laborzahlen,
   Studiensprache und lange Aufzählungen, erfindet nichts. Jedes Kapitel wird
   danach mit `regel_check.py` und `research_check.py` gegen den Stand davor
   geprüft; wird es rot, kommt ein neuer Befund dazu oder steht ein Satz
   doppelt, wird die geprüfte Fassung wiederhergestellt. 72 von 73 Kapiteln
   sind so überarbeitet, 050 blieb auf der geprüften Fassung (der Check hält
   "Antilope" für einen lateinischen Namen).

## Stand

- Regel-Check: 0 rot. Geschichten 793 bis 1.000 Wörter, drei knapp unter 800
  (041, 075, 077), der Check meldet sie gelb.
- Von den 73 neuen Kapiteln habe ich 5 ganz gelesen (029, 055, 065, 095, 100)
  und Stichproben in den Diffs. Die übrigen 68 sind nur maschinell geprüft.

## Was Tobi wissen muss

- **Lesen bleibt nötig.** Die Skripte finden Zahlen ohne Beleg, keine
  Stilfehler und keine erfundenen Bilder. Ein Durchgang beim Vorlesen findet
  mehr als jede weitere QS-Runde.
- `patch_anwenden.py` hat zwei Erweiterungen: Vorbehaltswort am Satzanfang,
  und wörtliche Zitate trotz Fußnotenziffern im Doc.
- `research/076–078.txt`, `080–100.txt` sind neu aus Drive gespiegelt.
- Offen: Illustrationen für 077 bis 100 (76 liegen unter `illustrationen/`),
  Einleitungen (P6a), Satz als EPUB und PDF (P6b), Merge nach `main`.
- Die rohen Session-Logs gehören nicht in dieses öffentliche Repo.

## Kosten

Codex 4ED1-Konto, Wochenlimit: 87 % vor dem Start, 89 % nach allen Läufen.
Vorlese-Durchgang: rund 3,3 Mio. Tokens für 73 Kapitel, etwa 45k je Kapitel.
