"""round3_lists.py: quests wireable now after the placement (T695-T698) and enemy-row (T699) briefs (lead, 2026-10-26).

A quest is listed when its fixed spec (objective-specs-fixed.json) has every objective "settled", or
"needs_placement" on an NPC row that the tip now draws, and the quest is still disabled at the tip. Grouped by
the zone lists in wiring/zone-quests/; zones whose round-1 brief is still queued are skipped (that brief covers
them). Writes wiring/round3/<zone>.json.
Run with lab/tools/wiki-env/Scripts/python.exe.
"""
import json
from collections import defaultdict

from npc_match import CONTENT
from quest_lines import OUT

DRAWN = {"legacy_data", "capture", "reference", "authored", "playtest", "reference_data"}
PENDING_ROUND1 = {"blackspore", "lakeshore", "greenwood-forest", "snowhill", "dartmoor", "sunstone-valley",
                  "shrouded-glade", "wilds"}


def main():
    load = lambda p: json.load(open(p, encoding="utf-8"))  # noqa: E731
    drawn = {r["npc_id"] for f in (CONTENT / "npcs").glob("*.json") for r in load(f)["records"]
             if r.get("placement") in DRAWN}
    drawn |= {r.get("spawn_guid") for r in load(CONTENT / "npc_spawns_extra.json")["records"]}
    enabled = {r["id"]: bool(r.get("enabled")) for f in (CONTENT / "quests").glob("*.json") for r in load(f)["records"]}
    zone_of = {}
    for f in (OUT / "wiring" / "zone-quests").glob("*.json"):
        for q in load(f)["quests"]:
            zone_of[q["quest_id"]] = f.stem
    out = defaultdict(list)
    for q in load(OUT / "objective-specs-fixed.json"):
        qid = int(q["quest"].lstrip("q"))
        objs = q.get("objectives") or []
        ok = bool(objs) and all(o.get("status", "settled" if o.get("resolved") else "x") == "settled"
                                or (o.get("status") == "needs_placement"
                                    and (o.get("fields") or {}).get("npc_id") in drawn) for o in objs)
        zone = zone_of.get(qid)
        if ok and qid in enabled and not enabled[qid] and zone and zone not in PENDING_ROUND1:
            out[zone].append({"quest_id": qid, "title": q["title"], "record": q["record"],
                              "source": q.get("source"), "objectives": objs})
    (OUT / "wiring" / "round3").mkdir(exist_ok=True)
    for zone, rows in out.items():
        (OUT / "wiring" / "round3" / f"{zone}.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False),
                                                                 encoding="utf-8")
    print({z: len(r) for z, r in sorted(out.items(), key=lambda x: -len(x[1]))})


if __name__ == "__main__":
    main()
