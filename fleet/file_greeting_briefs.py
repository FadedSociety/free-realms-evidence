"""file_greeting_briefs.py: check the greeting sweep's proposals and write one binding brief per zone (lead, 2026-10-22).

A proposal survives when its locale id exists, its quoted text equals the client's string exactly (whitespace
folded), the NPC record exists without a greeting, and no NPC already uses that string as its greeting. Survivors go
to lab/autopilot/incoming/fleet-greetings-<zone>.md (the tick numbers them); everything else is listed with its reason.
"""
import json
import re
from collections import defaultdict
from pathlib import Path

CMMO = Path(r"C:\Users\Bryce\Documents\Projects\CartoonMMO")
FLEET = CMMO / "lab" / "fleet"
NPCS = CMMO / "fleet-ro" / "prototype" / "osfr-tools" / "data" / "content" / "npcs"
INCOMING = CMMO / "lab" / "autopilot" / "incoming"
LOCALE = {r["id"]: r["text"] for r in json.load(open(CMMO / "lab" / "reports" / "locale-id-to-text.json", encoding="utf-8"))}


def fold(text):
    return re.sub(r"\s+", " ", (text or "").replace("\u2019", "'")).strip()


records, used = {}, set()
for path in NPCS.glob("*.json"):
    for r in json.load(open(path, encoding="utf-8")).get("records", []):
        records[str(r["npc_id"])] = (path.name, r)
        if r.get("greeting_string_id"):
            used.add(int(r["greeting_string_id"]))

by_zone, rejected, claimed = defaultdict(list), [], {}
for out in sorted((FLEET / "out" / "greeting-sweep").glob("*.md")):
    text = out.read_text(encoding="utf-8")
    if "status=done" not in text.split("\n")[0]:
        continue
    m = re.search(r"\*\*Greeting:\*\*\s*`?locale\s*(\d+)`?\s*:?\s*[\"\u201c](.+?)[\"\u201d]\s*$", text, re.M)
    if not m:
        rejected.append((out.stem, "no parseable Greeting line"))
        continue
    sid, quote = int(m.group(1)), m.group(2)
    if out.stem not in records:
        rejected.append((out.stem, "npc id not found"))
        continue
    zone_file, rec = records[out.stem]
    if rec.get("greeting_string_id"):
        rejected.append((out.stem, "already has a greeting"))
    elif sid not in LOCALE:
        rejected.append((out.stem, f"locale {sid} does not exist"))
    elif fold(LOCALE[sid]).rstrip(".!?") != fold(quote).rstrip(".!?") and fold(quote) not in fold(LOCALE[sid]):
        rejected.append((out.stem, f"quote does not match locale {sid}"))
    elif sid in used:
        rejected.append((out.stem, f"locale {sid} is already another NPC's greeting"))
    elif sid in claimed:
        rejected.append((out.stem, f"locale {sid} also proposed for {claimed[sid]}"))
    else:
        claimed[sid] = out.stem
        by_zone[zone_file].append((out.stem, rec.get("name"), sid, LOCALE[sid]))

for zone_file, rows in sorted(by_zone.items()):
    zone = zone_file[:-5]
    lines = "\n".join(f"- `{npc}` {name}: locale {sid} \"{text[:140]}\" (proof: `lab/fleet/out/greeting-sweep/{npc}.md`)"
                      for npc, name, sid, text in rows)
    (INCOMING / f"fleet-greetings-{zone.replace('_', '-')}.md").write_text(
        f"title: Bind {len(rows)} proven NPC greetings in {zone} (fleet greeting sweep)\n---\n\n## Why\n\n"
        "The greeting table (who says which line) was server-side and is lost; a line may be bound only with proof "
        "(a guide/wiki quote attributing it, a line naming its speaker, or a quest intro of that giver). A read-only "
        "Claude Haiku agent searched each NPC; a script checked the locale id exists, the quote matches, and no NPC "
        "already uses the line. Each proof file says which rule it used.\n\n## Proposed bindings\n\n"
        f"{lines}\n\n## Work\n\nOpen each proof file and re-check the attribution yourself; drop any whose proof is "
        "only proximity or guesswork, and say so. Bind the rest as `greeting_string_id` with a `field_sources` entry "
        f"citing the proof, in `prototype/osfr-tools/data/content/npcs/{zone_file}` (keep its line endings), and extend "
        "the zone's greeting test (follow `tests/npc_greetings_*.rs` and the T316 speaker-proof rule).\n",
        encoding="utf-8", newline="\n")
    print(f"brief {zone}: {len(rows)}")
print("rejected", len(rejected))
for stem, why in rejected[:15]:
    print("  ", stem, why)
