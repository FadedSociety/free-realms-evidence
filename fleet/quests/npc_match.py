"""npc_match.py: resolve quest givers and objective targets to our NPC rows, to find more wireable quests (lead, 2026-10-24).

The quest packs held the giver's record but not the objective targets' rows, so answers often say "<NPC> has no npc id"
although data/content already places that NPC (e.g. q3040024: Ari the Fish is npcs/wilds.json 9500000869). This pass
matches names and locale ids (no model, no cost) for every final quest the critics did not mark wireable, and writes
references/quest-lines/wiring/zone-quests-matched/<zone>.json:
  wireable_by_match  every NPC the quest needs (giver and talk/deliver/defeat targets) resolves to a placed row and no
                     objective needs a mechanic we lack; empty rewards are allowed (the builder uses the job-quest
                     reward ladder, marked (R))
  still_blocked      the rest, each with the reasons
Run with lab/tools/wiki-env/Scripts/python.exe.
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))  # -I leaves the script's own folder off sys.path
from wiring_lists import CONTENT, OUT, slug, zone_of  # noqa: E402

PLACED = {"legacy_data", "capture", "reference", "authored", "playtest"}  # placements world.rs draws
NPC_KINDS = {"talk", "deliver", "defeat", "escort", "give"}
MECHANIC_KINDS = {"minigame", "craft", "fish", "harvest", "race", "duel"}


def norm(s):
    s = re.sub(r"'s\b", "", (s or "").lower())
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def npc_index():
    by_name, by_sid, rows = defaultdict(list), defaultdict(list), []
    for f in (CONTENT / "npcs").glob("*.json"):
        for r in json.load(open(f, encoding="utf-8")).get("records", []):
            row = {"npc_id": r.get("npc_id"), "name": r.get("name"), "file": f"npcs/{f.name}", "zone": r.get("zone"),
                   "placed": r.get("placement") in PLACED and bool(r.get("position")),
                   "placement": r.get("placement"), "confidence": r.get("placement_confidence")}
            rows.append(row)
            if r.get("name"):
                by_name[norm(r["name"])].append(row)
            for sid in [r.get("name_string_id")] + list(r.get("name_string_ids") or []):
                if isinstance(sid, int):
                    by_sid[sid].append(row)
    for r in json.load(open(CONTENT / "npc_spawns_extra.json", encoding="utf-8")).get("records", []):
        row = {"npc_id": r.get("spawn_guid"), "name": r.get("name"), "file": "npc_spawns_extra.json", "zone": None,
               "placed": bool(r.get("position")), "placement": "extra_spawn", "confidence": None}
        rows.append(row)
        if r.get("name"):
            by_name[norm(r["name"])].append(row)
        if isinstance(r.get("name_string_id"), int):
            by_sid[r["name_string_id"]].append(row)
    names = sorted(by_name, key=len, reverse=True)
    return by_name, by_sid, names


def resolve(text, sid, by_name, by_sid, names):
    """Best placed row for a name or target text: locale id first, then exact name, then the longest name inside it."""
    cands = list(by_sid.get(sid, [])) if isinstance(sid, int) else []
    n = norm(text)
    if not cands and n:
        cands = by_name.get(n, [])
    if not cands and n:
        hit = next((k for k in names if len(k) >= 5 and re.search(rf"\b{re.escape(k)}\b", n)), None)
        cands = by_name.get(hit, []) if hit else []
    placed = [c for c in cands if c["placed"]]
    return (placed or cands or [None])[0]


def main():
    by_name, by_sid, names = npc_index()
    shipped = {}
    for f in (CONTENT / "quests").glob("*.json"):
        for r in json.load(open(f, encoding="utf-8")).get("records", []):
            shipped[r["id"]] = (f.name, bool(r.get("enabled")))
    dialogs = {r["key"]: r for r in json.load(open(OUT / "dialogs.json", encoding="utf-8")) if r["status"] == "final"}
    out, stats, reasons = defaultdict(lambda: {"wireable_by_match": [], "still_blocked": []}), Counter(), Counter()
    for r in json.load(open(OUT / "quests.json", encoding="utf-8")):
        key = r["key"].lstrip("q")
        a = r["answer"] or {}
        if (r["status"] != "final" or not key.isdigit() or any(c.get("wireable") for c in r["last_critiques"])
                or a.get("live") not in ("yes", "unsure")):
            continue
        qid = int(key)
        if qid not in shipped:
            stats["no_shipped_record"] += 1
            continue
        if shipped[qid][1]:
            stats["already_enabled"] += 1
            continue
        why = []
        g = a.get("giver") or {}
        giver = resolve(g.get("name"), g.get("locale_id"), by_name, by_sid, names)
        if not giver:
            why.append(f"giver {g.get('name')!r} not in our NPC rows")
        elif not giver["placed"]:
            why.append(f"giver {g.get('name')!r} row {giver['npc_id']} not placed")
        objs = []
        for o in a.get("objectives") or []:
            kind = (o.get("kind") or "other").lower()
            row = None
            if kind in NPC_KINDS or (kind == "go" and o.get("target")):
                row = resolve(o.get("target"), o.get("target_locale_id"), by_name, by_sid, names)
                if kind in NPC_KINDS and not (row and row["placed"]):
                    why.append(f"{kind} target {o.get('target')!r} not placed in our rows")
            if kind in MECHANIC_KINDS:
                why.append(f"needs mechanic: {kind} ({o.get('target') or o.get('text')})"[:160])
            objs.append({**o, "resolved_npc": row})
        d = (dialogs.get(r["key"]) or {}).get("answer") or {}
        item = {"quest_id": qid, "record": f"quest-lines/quests.json {r['key']}", "quest_file": shipped[qid][0],
                "title": (a.get("quest") or {}).get("title"), "live": a.get("live"), "giver": g, "resolved_giver": giver,
                "objectives": objs, "rewards": a.get("rewards") or [], "rewards_missing": not a.get("rewards"),
                "dialog": {s: d.get(s) for s in ("offer", "progress", "complete")} if d else a.get("dialog"),
                "critic_problems": [f"{p.get('field')}: {p.get('issue', '')[:200]}" for c in r["last_critiques"]
                                    for p in c.get("problems") or []][:6]}
        z = zone_of(a.get("zone"))
        if why:
            item["blocked_by"] = why
            out[z]["still_blocked"].append(item)
            stats["still_blocked"] += 1
            for w in why:
                reasons[w.split(" ")[0] if w.startswith("needs") else re.sub(r"'.*?'|\d+", "", w)[:40]] += 1
        else:
            out[z]["wireable_by_match"].append(item)
            stats["wireable_by_match"] += 1
            stats["of_which_rewards_missing"] += item["rewards_missing"]
    target = OUT / "wiring" / "zone-quests-matched"
    target.mkdir(parents=True, exist_ok=True)
    for z, v in out.items():
        (target / f"{slug(z)}.json").write_text(json.dumps({"zone": z, **v}, indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"stats": stats, "by_zone": {z: len(v["wireable_by_match"]) for z, v in
                                                   sorted(out.items(), key=lambda kv: -len(kv[1]["wireable_by_match"]))},
                      "top_blockers": reasons.most_common(8)}, indent=1))


if __name__ == "__main__":
    main()
