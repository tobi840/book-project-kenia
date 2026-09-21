#!/usr/bin/env python3
# ABOUTME: Runs the chapter pipeline (write, rule scripts, QS, patch) with Codex workers, three chapters per worker.
# ABOUTME: Skips finished chapters, so a stopped run continues where it ended; results go to berichte/codex-batch.tsv.
"""Usage: codex_batch.py [--parallel N] NNN [NNN ...]   (chapter numbers, grouped in threes in the given order)"""

import argparse
import json
import re
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODEL = "gpt-5.6-luna"
EFFORT = "high"
GROUP_SIZE = 3
CODEX_TIMEOUT_SECONDS = 3600
UMLAUTS = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"})
RESULTS = ROOT / "berichte" / "codex-batch.tsv"
results_lock = threading.Lock()


def load_chapters():
    chapters = {}
    for line in (ROOT / "chapters.tsv").read_text().splitlines():
        nr, name, habitat = line.split("\t")
        slug = re.sub(r"[^a-z0-9]+", "-", name.lower().translate(UMLAUTS)).strip("-")
        chapters[nr] = {"nr": nr, "name": name, "habitat": habitat, "stem": f"{nr}-{slug}"}
    return chapters


def codex(prompt, log_name):
    """Runs one Codex worker in the repo root and returns the tokens it used."""
    log = ROOT / "logs" / f"{log_name}.log"
    with log.open("w") as out:
        subprocess.run(
            ["codex", "exec", "--sandbox", "danger-full-access", "-m", MODEL,
             "-c", f"model_reasoning_effort={EFFORT}", prompt],
            cwd=ROOT, stdin=subprocess.DEVNULL, stdout=out, stderr=subprocess.STDOUT,
            timeout=CODEX_TIMEOUT_SECONDS,
        )
    text = log.read_text()
    if "usage limit" in text:
        raise RuntimeError(f"Codex usage limit reached, see {log.relative_to(ROOT)}")
    used = re.findall(r"tokens used\s+([\d,.]+)", text)
    return int(re.sub(r"\D", "", used[-1])) if used else 0


def script(name, *args):
    return subprocess.run([sys.executable, str(ROOT / "scripts" / name), *args],
                          cwd=ROOT, capture_output=True, text=True).stdout


def rule_check(ch):
    return json.loads(script("regel_check.py", "--json", f"chapters/{ch['stem']}.html"))


def write_prompt(group, redo_notes=""):
    jobs = "\n".join(
        f"- Kapitel {c['nr']} {c['name']} (Lebensraum: {c['habitat']}): lies research/{c['nr']}.txt, "
        f"schreib chapters/{c['stem']}.html" for c in group)
    return f"""Du schreibst Kapitel für ein Kenia-Vorlesebuch. Arbeite nur in diesem Ordner.
Lies zuerst genau diese Dateien: prompts/P3-kapitel-schreiben.md, styleguide/01-text-styleguide.md,
styleguide/02-kapitel-template.md, research/namen-bedeutungen.md. Folge P3 vollständig.
Dann schreib nacheinander, jedes Kapitel nur aus seinem eigenen Research-Doc:
{jobs}
Lies sonst keine Dateien, durchsuche den Ordner nicht, ruf kein Skript auf, keine Websuche, kein git.
Nichts aus dem Research-Doc eines anderen Kapitels übernehmen.
Längen, die ein Skript danach zählt: Geschichte 900 bis 1.000 Wörter, "Menschen und Kultur" 150 bis 250 Wörter.
Zähl vor dem Speichern nach und fülle nur mit belegter Substanz aus dem Research-Doc auf.
{redo_notes}Antworte am Ende nur mit einer Zeile je Kapitel: Nummer und Wortzahl der Geschichte."""


def qs_prompt(group, suffix):
    parts = []
    for c in group:
        chapter = f"chapters/{c['stem']}.html"
        research = f"research/{c['nr']}.txt"
        parts.append(
            f"### Kapitel {c['nr']} {c['name']}\nResearch-Doc: {research}\nKapitel: {chapter}\n"
            f"Ausgabe: qs/{c['stem']}{suffix}.md\n"
            f"Ausgabe regel_check.py:\n{script('regel_check.py', chapter)}\n"
            f"Ausgabe research_check.py:\n{script('research_check.py', '--research', research, chapter)}")
    round_note = "Dies ist die zweite und letzte Runde (siehe P4, Abschnitt zur zweiten Runde).\n" if suffix else ""
    return f"""Du prüfst Kapitel eines Kenia-Vorlesebuchs. Arbeite nur in diesem Ordner. Du hast diese Kapitel nicht geschrieben.
Lies zuerst prompts/P4-qs.md und folge ihm vollständig. {round_note}Prüfe jedes Kapitel nur gegen sein eigenes Research-Doc
und schreib je Kapitel genau die genannte Ausgabedatei. Ändere keine Kapiteldatei. Lies sonst keine Dateien,
durchsuche den Ordner nicht, ruf kein Skript auf, keine Websuche, kein git.
Gibt es für ein Kapitel keinen Patch, steht in seiner Datei statt des Codeblocks die Zeile KEINE PATCHES.

{chr(10).join(parts)}

Antworte am Ende nur mit einer Zeile je Kapitel in der Form: AMPEL <Nummer> <rot|gelb|gruen> <Anzahl Patches>"""


def apply_patches(c, suffix):
    out = script("patch_anwenden.py", "--qs", f"qs/{c['stem']}{suffix}.md",
                 "--research", f"research/{c['nr']}.txt", f"chapters/{c['stem']}.html")
    (ROOT / "logs" / f"patch-{c['stem']}{suffix}.log").write_text(out)


def is_red(c, suffix, worker_log):
    qs_text = (ROOT / "qs" / f"{c['stem']}{suffix}.md").read_text()
    reported = re.search(rf"AMPEL\s+{c['nr']}\s+rot", worker_log)
    return bool(reported) or "FALSCH" in qs_text


def run_group(group):
    label = f"{group[0]['nr']}-{group[-1]['nr']}"
    tokens = {"write": 0, "qs": 0}

    to_write = [c for c in group if not (ROOT / "chapters" / f"{c['stem']}.html").exists()]
    if to_write:
        tokens["write"] += codex(write_prompt(to_write), f"write-{label}")
    missing = [c["nr"] for c in group if not (ROOT / "chapters" / f"{c['stem']}.html").exists()]
    if missing:
        raise RuntimeError(f"no chapter file for {missing}")

    red = [c for c in group if rule_check(c)["rot"] > 0 and not (ROOT / "qs" / f"{c['stem']}.md").exists()]
    if red:
        notes = "Diese Kapitel gibt es schon, sie fallen im Regel-Check rot durch. Schreib sie neu und behebe genau das:\n" + \
            "\n".join(script("regel_check.py", f"chapters/{c['stem']}.html") for c in red) + "\n"
        tokens["write"] += codex(write_prompt(red, notes), f"rewrite-{label}")

    to_check = [c for c in group if not (ROOT / "qs" / f"{c['stem']}.md").exists()]
    if to_check:
        tokens["qs"] += codex(qs_prompt(to_check, ""), f"qs-{label}")
        worker_log = (ROOT / "logs" / f"qs-{label}.log").read_text()
        for c in to_check:
            apply_patches(c, "")
        second = [c for c in to_check if is_red(c, "", worker_log)]
        if second:
            tokens["qs"] += codex(qs_prompt(second, "-runde2"), f"qs2-{label}")
            for c in second:
                apply_patches(c, "-runde2")

    with results_lock, RESULTS.open("a") as out:
        for c in group:
            check = rule_check(c)
            out.write("\t".join([c["nr"], c["stem"], check["ampel_regelcheck"],
                                 str(check["masse"]["geschichte_woerter"]),
                                 str(tokens["write"] // len(group)), str(tokens["qs"] // len(group))]) + "\n")
    print(f"{label}: done, write {tokens['write']:,} qs {tokens['qs']:,} tokens", flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--parallel", type=int, default=4)
    parser.add_argument("numbers", nargs="+")
    args = parser.parse_args()

    chapters = load_chapters()
    todo = [chapters[nr] for nr in args.numbers]
    groups = [todo[i:i + GROUP_SIZE] for i in range(0, len(todo), GROUP_SIZE)]
    (ROOT / "logs").mkdir(exist_ok=True)
    if not RESULTS.exists():
        RESULTS.write_text("nr\tkapitel\tregelcheck\twoerter\ttokens_schreiben\ttokens_qs\n")

    failed = False
    with ThreadPoolExecutor(max_workers=args.parallel) as pool:
        for group, future in [(g, pool.submit(run_group, g)) for g in groups]:
            try:
                future.result()
            except Exception as error:
                failed = True
                print(f"{group[0]['nr']}-{group[-1]['nr']}: FAILED {error}", flush=True)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
