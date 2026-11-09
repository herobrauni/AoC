#!/usr/bin/env python3
"""Regenerate the star tables in README.md from adventofcode.com.

Reads AOC_SESSION (session cookie) and AOC_USER_AGENT from the environment and
rewrites everything between the two `<!--- advent_readme_stars table --->` markers.

Only the standard library is used, so CI can run it with a plain interpreter:
    AOC_SESSION=... AOC_USER_AGENT=... python tools/update_readme_stars.py [--dry-run]
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

MARKER = "<!--- advent_readme_stars table --->"
FIRST_YEAR = 2015
BASE = "https://adventofcode.com"
DAY_LINK = re.compile(r'<a\b[^>]*href="/(\d{4})/day/(\d{1,2})"[^>]*>')
LABEL = re.compile(r'aria-label="([^"]*)"')
STAR_WORDS = {"two stars": 2, "one star": 1}


def fetch_calendar(year: int, session: str, user_agent: str) -> dict[int, int]:
    """Return {day: stars 0..2} for every day shown on that year's calendar."""
    request = urllib.request.Request(
        f"{BASE}/{year}",
        headers={"Cookie": f"session={session}", "User-Agent": user_agent},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        html = response.read().decode("utf-8", "replace")

    days: dict[int, int] = {}
    for tag in DAY_LINK.finditer(html):
        if int(tag.group(1)) != year:
            continue
        label = LABEL.search(tag.group(0))
        text = label.group(1) if label else ""
        days[int(tag.group(2))] = next((stars for word, stars in STAR_WORDS.items() if word in text), 0)
    return days


def grid(days: dict[int, int]) -> str:
    cells = {0: "·", 1: "☆", 2: "★"}
    return "".join(cells[days.get(day, 0)] for day in range(1, 26))


def render(all_days: dict[int, dict[int, int]]) -> str:
    years = sorted(all_days)
    total_stars = sum(sum(days.values()) for days in all_days.values())
    total_days = sum(1 for days in all_days.values() for stars in days.values() if stars == 2)
    max_stars = 50 * len(years)

    out = [
        "## Results",
        "",
        f"**{total_stars}/{max_stars} ⭐** · **{total_days}/{25 * len(years)} days**",
        "",
        "| Year | Stars | Days | Progress |",
        "| :--- | ---: | :---: | :--- |",
    ]
    for year in years:
        days = all_days[year]
        stars = sum(days.values())
        solved = sum(1 for value in days.values() if value == 2)
        out.append(f"| [{year}]({BASE}/{year}) | {stars}/50 | {solved}/25 | `{grid(days)}` |")
    out.append(f"| **Total** | **{total_stars}** | **{total_days}** | |")
    out.append("")
    out.append("`★` both parts · `☆` part 1 only · `·` unsolved")
    out.append("")

    for year in years:
        days = all_days[year]
        stars = sum(days.values())
        solved = sum(1 for value in days.values() if value == 2)
        if not stars:
            continue
        out += [
            "<details>",
            f"<summary><strong>{year}</strong> — {stars}/50 ⭐ · {solved}/25 days</summary>",
            "",
            "| Day | Part 1 | Part 2 |",
            "| :---: | :---: | :---: |",
        ]
        for day in sorted(days):
            stars_today = days[day]
            part_1 = "⭐" if stars_today >= 1 else ""
            part_2 = "⭐" if stars_today == 2 else ""
            out.append(f"| [Day {day}]({BASE}/{year}/day/{day}) | {part_1} | {part_2} |")
        out += ["", "</details>", ""]

    return "\n".join(out).rstrip() + "\n"


def replace_block(readme: str, block: str) -> str:
    start = readme.find(MARKER)
    if start == -1:
        sys.exit(f"error: marker {MARKER!r} not found in README.md")
    end = readme.find(MARKER, start + len(MARKER))
    if end == -1:
        sys.exit("error: closing marker not found in README.md (need the marker twice)")
    return readme[: start + len(MARKER)] + "\n" + block + readme[end:]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="print the generated block, do not write")
    args = parser.parse_args()

    session = os.environ.get("AOC_SESSION", "").strip()
    if not session:
        sys.exit("error: AOC_SESSION is not set")
    user_agent = os.environ.get("AOC_USER_AGENT", "aoc@brauni.dev")

    current_year = dt.date.today().year
    all_days: dict[int, dict[int, int]] = {}
    for year in range(FIRST_YEAR, current_year + 1):
        days = fetch_calendar(year, session, user_agent)
        if not days:
            print(f"{year}: no puzzles published yet, skipping", file=sys.stderr)
            continue
        all_days[year] = days
        print(f"{year}: {sum(days.values())}/50 stars", file=sys.stderr)
        time.sleep(1)  # be polite to adventofcode.com

    block = render(all_days)
    if args.dry_run:
        print(block)
        return

    readme_path = Path(__file__).resolve().parents[1] / "README.md"
    readme_path.write_text(replace_block(readme_path.read_text(encoding="utf-8"), block), encoding="utf-8")
    print(f"wrote {readme_path}")


if __name__ == "__main__":
    main()
