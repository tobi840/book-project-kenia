#!/usr/bin/env python3
# ABOUTME: Runs the P7 read-aloud pass with Codex writers, three chapters per worker, and re-checks each chapter.
# ABOUTME: A chapter that turns red or gains an unbacked number is restored from git and listed for hand review.
"""Usage: vorlesen_batch.py [--parallel N] NNN [NNN ...]   (chapter numbers, grouped in threes)"""

import argparse
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

import codex_batch as b


def prompt(group):
    jobs = "\n".join(f"- Kapitel {c['nr']} {c['name']}: research/{c['nr']}.txt, chapters/{c['stem']}.html" for c in group)
    return f"""Du bist der Schreiber im Vorlese-Durchgang eines Kenia-Vorlesebuchs. Arbeite nur in diesem Ordner.
Lies zuerst styleguide/01-text-styleguide.md und prompts/P7-vorlesen.md. Folge P7 vollständig.
Dann überarbeite nacheinander diese Kapitel, jedes nur mit seinem eigenen Research-Doc:
{jobs}
Lies sonst keine Dateien, durchsuche den Ordner nicht, ruf kein Skript auf, keine Websuche, kein git.
Antworte am Ende nur mit einer Zeile je Kapitel: Nummer und Wortzahl der Geschichte."""


def findings(c):
    out = b.script("research_check.py", "--json", "--research", f"research/{c['nr']}.txt", f"chapters/{c['stem']}.html")
    return {json.dumps(f, sort_keys=True) for f in json.loads(out)["befunde"]}


def run_group(group):
    label = f"{group[0]['nr']}-{group[-1]['nr']}"
    before = {c["nr"]: findings(c) for c in group}
    tokens = b.codex(prompt(group), f"vorlesen-{label}")
    for c in group:
        path = f"chapters/{c['stem']}.html"
        check = b.rule_check(c)
        new = findings(c) - before[c["nr"]]
        if check["rot"] > 0 or new:
            subprocess.run(["git", "checkout", "--", path], cwd=b.ROOT, check=True)
            reason = "rot im Regel-Check" if check["rot"] > 0 else "neue Befunde: " + "; ".join(sorted(new))
            print(f"{c['stem']}: ZURUECKGESETZT, {reason}", flush=True)
        else:
            print(f"{c['stem']}: {check['ampel_regelcheck']} {check['masse']['geschichte_woerter']} Wörter", flush=True)
    print(f"{label}: {tokens:,} tokens", flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--parallel", type=int, default=4)
    parser.add_argument("numbers", nargs="+")
    args = parser.parse_args()
    chapters = b.load_chapters()
    todo = [chapters[nr] for nr in args.numbers]
    groups = [todo[i:i + b.GROUP_SIZE] for i in range(0, len(todo), b.GROUP_SIZE)]
    (b.ROOT / "logs").mkdir(exist_ok=True)
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
