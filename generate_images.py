#!/usr/bin/env python3
# ABOUTME: Generates one main illustration per chapter with the Codex built-in image tool.
# ABOUTME: Reads research/NNN.txt (section 9) and the image styleguide; skips chapters that already have an image.
"""Usage: generate_images.py [--parallel N] [NNN ...]   (no numbers = every chapter with a research file)"""

import argparse
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STYLEGUIDE = ROOT / "styleguides" / "03_Bild-Styleguide.txt"
BACKGROUNDS = {
    "Nairobi": "dove blue",
    "Rift Valley": "pale sage",
    "Laikipia / Mt. Kenya": "cream",
    "Küste Mombasa": "light sand yellow",
    "Tsavo / Amboseli": "reddish ochre",
}
UMLAUTS = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "Ä": "Ae", "Ö": "Oe", "Ü": "Ue", "ß": "ss"})
CODEX_TIMEOUT_SECONDS = 900


def load_chapters():
    chapters = {}
    for line in (ROOT / "chapters.tsv").read_text().splitlines():
        nr, name, habitat = line.split("\t")
        chapters[nr] = (name, habitat)
    return chapters


def file_stem(nr, name):
    return f"{nr}_{name.translate(UMLAUTS).replace(' ', '_').replace('-', '_')}"


def instruction(nr, name, habitat, stem):
    return f"""Work only inside {ROOT}. Do not use any external API or API key.
Read {STYLEGUIDE.relative_to(ROOT)} and the English visual description for the illustration in research/{nr}.txt
(usually section 9 "Visuelle Beschreibung", sometimes under another heading near the end; called "section 9" below).
Build the main illustration prompt for chapter {nr} {name} exactly as section 3 of the styleguide prescribes:
the fixed style block, background colour "{BACKGROUNDS[habitat]}", the species description from section 9 taken over unchanged,
the three detail insets and the cultural vignette from section 9, and one accent colour that fits the species and stands out from the background.
If section 9 is missing or too thin to draw from, write the single line [[BESCHREIBUNG FEHLT]] to prompts/{stem}_haupt.txt, generate nothing and stop.
Otherwise save the prompt text to prompts/{stem}_haupt.txt, generate the image with your built-in image generation tool
and save it as illustrationen/{stem}_haupt.png.
Composition rules on top of the prompt: keep the real-world sizes from the description (a 2 to 3 m shrub must not look like a tall tree,
a 5 cm object stays small next to a staff); the vignette shows only the objects named, no added human figures.
Report only the saved file paths."""


def generate(job):
    nr, name, habitat = job
    stem = file_stem(nr, name)
    image = ROOT / "illustrationen" / f"{stem}_haupt.png"
    log = ROOT / "logs" / f"{stem}.log"
    with log.open("w") as out:
        result = subprocess.run(
            ["codex", "exec", "--skip-git-repo-check", "--sandbox", "danger-full-access",
             "-c", "model_reasoning_effort=medium", instruction(nr, name, habitat, stem)],
            cwd=ROOT, stdin=subprocess.DEVNULL, stdout=out, stderr=subprocess.STDOUT,
            timeout=CODEX_TIMEOUT_SECONDS,
        )
    status = "ok" if image.exists() else f"NO IMAGE (exit {result.returncode}, see {log.relative_to(ROOT)})"
    print(f"{stem}: {status}", flush=True)
    return image.exists()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--parallel", type=int, default=3)
    parser.add_argument("numbers", nargs="*")
    args = parser.parse_args()

    chapters = load_chapters()
    numbers = args.numbers or sorted(p.stem for p in (ROOT / "research").glob("*.txt"))
    jobs = []
    for nr in numbers:
        name, habitat = chapters[nr]
        if not (ROOT / "illustrationen" / f"{file_stem(nr, name)}_haupt.png").exists():
            jobs.append((nr, name, habitat))
    print(f"{len(jobs)} chapters to generate", flush=True)
    with ThreadPoolExecutor(max_workers=args.parallel) as pool:
        results = list(pool.map(generate, jobs))
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
