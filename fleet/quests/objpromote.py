"""objpromote.py: the "unknown" objectives whose ids are all filled (lead, 2026-10-26; NEXT-PASSES.md step 3).

objective-specs-fixed.json keeps 244 objectives "unknown". 118 of them have every id their kind needs; what holds
them back is a note: often only a reasoned count ("some cray" -> 1 (R)), which Bryce's rules allow as tunable data
(memory tunable-over-locked, coworker-pushback: flag (R), then build), sometimes a real doubt (an id that is only a
candidate, a proxy position, an unproven quest link). Each pack carries the objective and local checks of its ids
against our content (NPC row and whether world.rs draws it, enemy definition, client item, recipe row, a minigame id
other content already uses); the job objpromote-judge decides settled_r or keep.

  python objpromote.py          -> references/quest-lines/round/objpromote-judge.json
  python objpromote.py apply    -> promotes the settled_r answers in objective-specs-fixed.json
"""
import json
import re
import sys
from pathlib import Path

CMMO = Path(r"C:\Users\Bryce\Documents\Projects\CartoonMMO")
LAB = CMMO / "lab"
QL = LAB / "references" / "quest-lines"
CONTENT = CMMO / "autopilot-int" / "prototype" / "osfr-tools" / "data" / "content"
OUT = LAB / "fleet" / "out" / "objpromote-judge"
REQ = {"talk_to_npc": ["npc_id"], "interact_npc": ["npc_id"], "kill_actor_kind": ["actor_kind_id"],
       "collect_item": ["item_id"], "gather_resource": ["resource_id"], "craft_recipe": ["recipe_id"],
       "finish_minigame": ["minigame_id"], "visit_position": ["position", "zone_id"], "use_item": ["item_id"]}
DRAWN = {"legacy_data", "capture", "reference", "authored", "playtest"}


def ints_under(node, key, out):
    if isinstance(node, dict):
        for k, v in node.items():
            if k == key and isinstance(v, int):
                out.add(v)
            ints_under(v, key, out)
    elif isinstance(node, list):
        for v in node:
            ints_under(v, key, out)
    return out


def tables():
    npcs = {}
    for f in (CONTENT / "npcs").glob("*.json"):
        for r in json.load(open(f, encoding="utf-8")).get("records", []):
            npcs[int(r["npc_id"])] = (r.get("name"), r.get("placement"), f.name)
    enemies = {d.get(k) for d in json.load(open(CONTENT / "enemies.json", encoding="utf-8"))["definitions"]
               for k in ("definition_id", "actor_kind_id")}
    enemies |= {r.get("definition_id") for r in json.load(open(CONTENT / "field_enemies.json", encoding="utf-8"))["enemies"]}
    items = {x["Id"] for x in json.load(open(LAB / "references" / "FreeRealms-Legacy" / "src" / "Resources" /
                                              "ClientItemDefinitions.json", encoding="utf-8-sig"))}
    recipes = set()
    for r in json.load(open(CONTENT / "recipes.json", encoding="utf-8"))["records"]:
        recipes |= {r.get("recipe_id"), r.get("candidate_recipe_id")} - {None}
    minigames = set()
    for f in CONTENT.rglob("*.json"):
        try:
            ints_under(json.load(open(f, encoding="utf-8")), "minigame_id", minigames)
        except (json.JSONDecodeError, UnicodeDecodeError):
            pass
    return npcs, enemies, items, recipes, minigames


def check(kind, fields, t):
    npcs, enemies, items, recipes, minigames = t
    f = fields or {}
    if kind in ("talk_to_npc", "interact_npc"):
        row = npcs.get(int(f["npc_id"]))
        return (f"npc row {f['npc_id']}: {row[0]!r} in npcs/{row[2]}, placement {row[1]} "
                f"({'drawn by world.rs' if row[1] in DRAWN else 'NOT drawn'})") if row else f"npc {f['npc_id']}: no row"
    if kind == "kill_actor_kind":
        return f"actor_kind_id {f['actor_kind_id']}: {'an enemy definition we ship' if f['actor_kind_id'] in enemies else 'NOT in enemies.json/field_enemies.json'}"
    if kind in ("collect_item", "gather_resource", "use_item"):
        i = f.get("item_id") or f.get("resource_id")
        return f"item {i}: {'a client item definition' if i in items else 'NOT a client item definition'}"
    if kind == "craft_recipe":
        return f"recipe_id {f['recipe_id']}: {'a recipe row' if f['recipe_id'] in recipes else 'NOT in recipes.json'}"
    if kind == "finish_minigame":
        return f"minigame_id {f['minigame_id']}: {'used by other content' if f['minigame_id'] in minigames else 'no other content uses it'}"
    return "position given (check the note for its source)"


def build():
    t = tables()
    locale = {r["id"]: r["text"] for r in json.load(open(LAB / "reports" / "locale-id-to-text.json", encoding="utf-8"))}
    items = []
    for q in json.load(open(QL / "objective-specs-fixed.json", encoding="utf-8")):
        for o in q["objectives"]:
            req = REQ.get(str(o.get("kind")))
            f = o.get("fields") or {}
            if o.get("status") != "unknown" or not req or any(f.get(x) in (None, "", []) for x in req):
                continue
            pack = {"quest": q["quest"], "title": q["title"], "live": q.get("live"), "index": o.get("index"),
                    "objective_text": locale.get(o.get("text_string_id")), "kind": o["kind"], "fields": f,
                    "evidence": o.get("evidence"), "note": o.get("note"), "local_check": check(o["kind"], f, t)}
            items.append({"id": f"{q['quest']}-o{o.get('index')}", "title": f"{q['title']} objective {o.get('index')}",
                          "prompt": "Pack:\n" + json.dumps(pack, ensure_ascii=False, indent=1) +
                                    "\n\nJudge it and submit the JSON result."})
    return items


def apply():
    verdicts = {}
    for p in OUT.glob("*.md"):
        m = re.search(r"\{.*\}", p.read_text(encoding="utf-8"), re.S)
        try:
            r = json.loads(m.group(0)) if m else {}
        except json.JSONDecodeError:
            continue
        if r.get("verdict") == "settled_r":
            verdicts[p.stem] = r
    path = QL / "objective-specs-fixed.json"
    specs = json.load(open(path, encoding="utf-8"))
    n = 0
    for q in specs:
        for o in q["objectives"]:
            r = verdicts.get(f"{q['quest']}-o{o.get('index')}")
            if r and o.get("status") == "unknown":
                o["status"], o["r_values"] = "settled_r", r.get("r_values", [])
                o.setdefault("evidence", []).append({"claim": r.get("reason", ""),
                                                     "source": "objpromote-judge (Haiku), lead rule 2026-10-26"})
                n += 1
    path.write_text(json.dumps(specs, indent=1, ensure_ascii=False), encoding="utf-8")
    print(n, "objectives -> settled_r")


if __name__ == "__main__":
    if sys.argv[1:] == ["apply"]:
        apply()
    else:
        items = build()
        (QL / "round" / "objpromote-judge.json").write_text(json.dumps(items, ensure_ascii=False), encoding="utf-8")
        print(len(items), "packs")
