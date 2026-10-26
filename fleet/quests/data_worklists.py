"""data_worklists.py: builder worklists from the fixed objective specs (lead, 2026-10-25).

Writes under references/quest-lines/wiring/:
  placements/<npc file>.json  unplaced NPC rows with ONE reference spawn location matched by the spawn's client
                              name (talk-spawns.json, match "name", unique), and the quests whose talk objectives
                              wait on them (objective-specs-fixed.json, needs_placement)
  enemy-rows-needed.json      kill objectives with no enemy definition row (needs_enemy_row): target, model id,
                              the reference Npcs.json definitions sharing the model and our enemy rows that do
Run with lab/tools/wiki-env/Scripts/python.exe.
"""
import json
import re
from collections import defaultdict

from npc_match import CONTENT
from quest_lines import LAB, OUT
from talk_spawns import spawns as spawns_by_ref

W = OUT / "wiring"


def main():
    spawns = json.load(open(W / "talk-spawns.json", encoding="utf-8"))["rows"]
    specs = json.load(open(OUT / "objective-specs-fixed.json", encoding="utf-8"))
    waiting = defaultdict(list)
    for q in specs:
        for o in q.get("objectives", []):
            npc = (o.get("fields") or {}).get("npc_id")
            if o.get("status") == "needs_placement" and npc:
                waiting[npc].append(f"{q['quest']} objective {o.get('index')}")
    per_file = defaultdict(list)
    for r in spawns:
        if r["match"] == "name" and r["unique"]:
            c = r["candidates"][0]
            per_file[r["file"]].append({"npc_id": r["npc_id"], "name": r["name"], "zone": r["zone"],
                                        "position": c["position"], "heading": c["heading"], "model": c["model"],
                                        "model_id": c["model_id"], "source": c["source"], "near_zone": c["near_zone"],
                                        "quests_waiting": waiting.get(r["npc_id"], [])})
    (W / "placements").mkdir(exist_ok=True)
    for f, rows in per_file.items():
        (W / "placements" / Path(f).name).write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
    print({Path(f).name: len(v) for f, v in sorted(per_file.items(), key=lambda x: -len(x[1]))})

    ref = json.load(open(LAB / "references" / "FreeRealms-Legacy" / "src" / "Resources" / "Npcs.json", encoding="utf-8"))
    loc = {r["id"]: r["text"] for r in json.load(open(LAB / "reports" / "locale-id-to-text.json", encoding="utf-8"))}
    ours = defaultdict(list)
    for name in ("enemies.json", "field_enemies.json"):
        d = json.load(open(CONTENT / name, encoding="utf-8"))
        for r in d.get("definitions") or d.get("records") or []:
            if isinstance(r, dict) and r.get("model_id"):
                ours[r["model_id"]].append({"actor_kind_id": r.get("actor_kind_id"), "name": r.get("kind") or r.get("name"),
                                            "file": name})
    draft = {q["quest"]: q for q in json.load(open(OUT / "objective-specs.json", encoding="utf-8"))}
    sp = spawns_by_ref()
    need = []
    for q in specs:
        for o in q.get("objectives", []):
            if o.get("status") != "needs_enemy_row":
                continue
            d = next((x for x in draft[q["quest"]]["objectives"]
                      if int(x["from"].split(":")[0].split()[1]) == o.get("index")), {})
            models = {d.get("model_id")} | {int(m) for m in re.findall(r"model[_ ]id (\d+)", o.get("note") or "")}
            models.discard(None)
            need.append({"quest": q["quest"], "title": q["title"], "objective": o.get("index"), "part": o.get("part"),
                         "client_text": d.get("from", "").split(": ", 1)[-1], "count": (o.get("fields") or {}).get("count"),
                         "model_ids": sorted(models), "fixer_note": o.get("note"),
                         "reference_definitions": [{"id": x["Id"], "model": x.get("ModelFileName"), "name": loc.get(x.get("NameId")),
                                                    "spawns": [{k: s[k] for k in ("source", "position", "heading")}
                                                               for s in sp.get(x["Id"], [])][:6]}
                                                   for x in ref if x.get("ModelId") in models][:8],
                         "our_rows_with_model": [r for m in models for r in ours.get(m, [])]})
    (W / "enemy-rows-needed.json").write_text(json.dumps(need, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"enemy rows needed: {len(need)} objectives, {len({m for n in need for m in n['model_ids']})} models")


if __name__ == "__main__":
    from pathlib import Path
    main()
