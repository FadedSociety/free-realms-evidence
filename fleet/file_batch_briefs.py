"""file_batch_briefs.py: turn verified fleet outputs into build briefs (lead, 2026-10-22).

- test-verify confirmed weak tests -> briefs of at most 12 findings each.
- guide-refresh / note-refresh corrections -> briefs of at most 20 notes each (the builder re-checks every correction).
- unrouted-recheck -> one brief to refresh notes/Research/Unrouted Client Requests.md.
Briefs go to lab/autopilot/incoming/ (the tick numbers them).
"""
import re
from pathlib import Path

FLEET = Path(__file__).resolve().parent
OUT = FLEET / "out"
INCOMING = FLEET.parent / "autopilot" / "incoming"
RULE = ("Every item below comes from a read-only Claude Haiku agent (lab/fleet). Re-check each one at the tip before "
        "acting; skip any that does not hold and say why in your report.")


def write(name, title, body):
    (INCOMING / name).write_text(f"title: {title}\n---\n\n{body}\n", encoding="utf-8", newline="\n")
    print("brief", name)


def chunks(rows, size):
    for i in range(0, len(rows), size):
        yield i // size + 1, rows[i:i + size]


# 1. weak tests confirmed by the skeptic
weak = []
for f in sorted((OUT / "test-verify").glob("*.md")):
    text = f.read_text(encoding="utf-8")
    if re.search(r"\*\*Verdict:\*\*\s*`?confirmed", text, re.I):
        weak.append(f"- {text.split(chr(10))[1][2:]} (`lab/fleet/out/test-verify/{f.name}`, first pass "
                    f"`lab/fleet/out/test-audit/{f.stem.rsplit('-f', 1)[0]}.md`)")
for n, rows in chunks(weak, 12):
    write(f"fleet-strengthen-tests-{n}.md", f"Strengthen {len(rows)} tests that cannot catch their regression (set {n})",
          "## Why\n\nEvery merge is gated on the full suite, so a test that cannot fail is a hole in the gate. A first "
          "pass flagged these as high and an independent skeptic confirmed each.\n\n## Tests\n\n" + "\n".join(rows) +
          f"\n\n## Work\n\n{RULE} For each: add the assertion or canary from the verification file (it must fail on "
          "the regression the file describes: show that by breaking the code locally, then restoring it), without "
          "weakening anything. Do not delete tests.")

# 2. doc corrections
for job, folder in (("guide-refresh", "notes/Build Guides"), ("note-refresh", "notes/Research")):
    notes = []
    for f in sorted((OUT / job).glob("*.md")):
        text = f.read_text(encoding="utf-8")
        if "status=done" in text.split("\n")[0] and re.search(r"(?m)^\s*-?\s*`?old:", text):
            notes.append(f"- `{text.split(chr(10))[1][2:]}` -> corrections in `lab/fleet/out/{job}/{f.name}`")
    for n, rows in chunks(notes, 20):
        write(f"fleet-{job}-{n}.md", f"Apply verified corrections to {len(rows)} notes under {folder} (set {n})",
              "## Why\n\nNotes were written over two weeks while the code moved; builders trust them. A read-only "
              "agent compared each note with the tip and proposed exact `old:` -> `new:` replacements with evidence."
              "\n\n## Notes\n\n" + "\n".join(rows) + f"\n\n## Work\n\n{RULE} Apply a correction only when its evidence "
              "holds at the tip and its `old:` text matches the note exactly; keep the note's voice and line endings. "
              "Notes only: change no code.")

# 3. unrouted survey refresh
done = sorted((OUT / "unrouted-recheck").glob("R*.md"))
write("fleet-refresh-unrouted-survey.md", "Refresh the Unrouted Client Requests survey from the fleet re-check",
      "## Why\n\n`notes/Research/Unrouted Client Requests.md` (2026-10-16) lists every client request and how we "
      f"handle it; many rows are stale. A read-only agent re-checked all {len(done)} rows against the tip "
      "(`lab/fleet/out/unrouted-recheck/R###.md`, each with Now C/P/I/X, handler and test, layout, gap, corrections)."
      f"\n\n## Work\n\n{RULE} Update each row's handling and evidence where the re-check holds, refresh the count "
      "summary and the Top 15 for playtest night, and add a dated note at the top. Notes only: change no code. List "
      "the P/I rows that have no queued brief in your report so the lead can queue them.")
