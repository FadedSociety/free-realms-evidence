"""spawn_objects.py: reference spawns for the needs_spawn objectives (lead, 2026-10-26; NEXT-PASSES.md step 2).

94 objectives in objective-specs-fixed.json need a clickable object or NPC the server does not place. Most targets
are props ("the pail of water next to Guard Reli"), which the name/model join of talk_spawns.py rarely finds, but
their text or quest names an NPC to stand near. So each pack pre-joins:
  direct   reference spawns whose client name or model matches the target (talk_spawns.match)
  nearby   every reference spawn within RADIUS m of an anchor (the giver, NPCs named in the objective text, the
           quest's talk targets), with its client name, model file and distance
and the job spawnobj-infer picks the spawn(s) or says none fits.

  python spawn_objects.py           -> references/quest-lines/round/spawnobj-infer.json (the job's items)
  python spawn_objects.py apply     -> references/quest-lines/wiring/spawn-objects.json
Run with lab/tools/wiki-env/Scripts/python.exe.
"""
import json
import math
import re
import sqlite3
import sys
from collections import defaultdict

from npc_match import CONTENT, norm
from talk_spawns import LAB, QL, indexes, match, spawns

RADIUS, NEARBY = 60.0, 60
OUT = LAB / "fleet" / "out" / "spawnobj-infer"


def anchors_index(sp, locale):
    """norm(name) -> [position]: reference spawns by client name, then our own placed NPC rows."""
    at = defaultdict(list)
    for rows in sp.values():
        nid = rows[0]["name_id"]
        if nid and locale.get(nid):
            at[norm(locale[nid])] += [r["position"] for r in rows]
    for f in sorted((CONTENT / "npcs").glob("*.json")):
        for r in json.load(open(f, encoding="utf-8")).get("records", []):
            if r.get("position") and r.get("name"):
                at[norm(r["name"])].append(r["position"])
    return at


def dist(a, b):
    return math.hypot(a[0] - b[0], a[2] - b[2])


def build():
    locale = {r["id"]: r["text"] for r in json.load(open(LAB / "reports" / "locale-id-to-text.json", encoding="utf-8"))}
    sp = spawns()
    by_name, by_token = indexes(sp, locale)
    by_any = defaultdict(set)
    for ref, rows in sp.items():
        for t in re.split(r"[_.\d]+", (rows[0]["model"] or "").lower()):
            if len(t) >= 3:
                by_any[t].add(ref)
    at = anchors_index(sp, locale)
    flat = [s for rows in sp.values() for s in rows]
    tags = {k: t for k, t in sqlite3.connect(QL / "objectives.sqlite").execute("SELECT key, target FROM jev")}
    quests = {q["key"]: q.get("answer") or {} for q in json.load(open(QL / "quests.json", encoding="utf-8"))}
    items = []
    for q in json.load(open(QL / "objective-specs-fixed.json", encoding="utf-8")):
        a = quests.get(q["quest"], {})
        for o in q["objectives"]:
            if o.get("status") != "needs_spawn":
                continue
            target = tags.get(f"{q['quest']}o{o['index']}")
            text = locale.get(o.get("text_string_id"), "")
            how, refs = match(target or "", by_name, by_token)
            if not refs and target:
                how, refs = match(target, by_name, by_any)
            direct = [s for r in sorted(refs) for s in sp[r]][:12]
            # Anchors: the giver, any known NPC name inside the objective text, the quest's other targets.
            names = {(a.get("giver") or {}).get("name") or ""}
            names |= {x.get("target") or "" for x in a.get("objectives") or []}
            low = norm(text)
            names |= {n for n in at if len(n) > 6 and f" {n} " in f" {low} "}
            anchors = [{"name": n, "positions": at[norm(n)][:4]} for n in sorted(names) if n and at.get(norm(n))]
            near = []
            for s in flat:
                d = min((dist(s["position"], p) for an in anchors for p in an["positions"]), default=None)
                if d is not None and d <= RADIUS:
                    near.append({**{k: s[k] for k in ("ref_id", "model", "position", "source")},
                                 "name": locale.get(s["name_id"]), "metres_to_anchor": round(d, 1)})
            near.sort(key=lambda s: s["metres_to_anchor"])
            pack = {"quest": q["quest"], "title": q["title"], "zone": a.get("zone"), "index": o["index"],
                    "kind": o["kind"], "fields": o.get("fields"), "objective_text": text, "target": target,
                    "earlier_note": o.get("note"), "direct_matches": {"how": how, "spawns": direct},
                    "anchors": anchors, "nearby_spawns": near[:NEARBY]}
            rid = f"{q['quest']}-o{o['index']}"
            items.append({"id": rid, "title": f"{q['title']} objective {o['index']}: {target or text[:40]}",
                          "prompt": "Pack:\n" + json.dumps(pack, ensure_ascii=False, indent=1) +
                                    "\n\nChoose the spawn(s) and submit the JSON result."})
    return items


def apply():
    rows = []
    for p in sorted(OUT.glob("*.md")):
        m = re.search(r"\{.*\}", p.read_text(encoding="utf-8"), re.S)
        try:
            rows.append(json.loads(m.group(0)) if m else {"id": p.stem, "status": "no_result"})
        except json.JSONDecodeError:
            rows.append({"id": p.stem, "status": "bad_json"})
    out = QL / "wiring" / "spawn-objects.json"
    out.write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
    from collections import Counter
    print(json.dumps(Counter(r.get("status") for r in rows)))


if __name__ == "__main__":
    if sys.argv[1:] == ["apply"]:
        apply()
    else:
        items = build()
        (QL / "round").mkdir(exist_ok=True)
        (QL / "round" / "spawnobj-infer.json").write_text(json.dumps(items, ensure_ascii=False), encoding="utf-8")
        n = [json.loads(i["prompt"][6:].rsplit("\n\nChoose", 1)[0]) for i in items]
        print(json.dumps({"items": len(items), "with_direct": sum(1 for x in n if x["direct_matches"]["spawns"]),
                          "with_anchor": sum(1 for x in n if x["anchors"]),
                          "with_nearby": sum(1 for x in n if x["nearby_spawns"])}))
