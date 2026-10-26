"""client_id_worklists.py: split the objective gaps that need client-side ids into DeepSeek worker lists (lead, 2026-10-25).

Reads references/quest-lines/objective-specs.json and writes references/quest-lines/client-ids/worklist-<group>-<n>.json:
  trigger   client_reported objectives (what the client sends when the objective is done; client_id is quest*10+n)
  minigame  finish_minigame objectives with no minigame_id (client MiniGameData.txt / MiniGameGroupData.txt)
  model     defeat objectives with no model_id (client Models.txt and enemy data)
  item      gather_resource objectives with no item id (client item tables)
  place     visit_position objectives with no position (client areas / map / POI data)
Talk targets (NPC placement) are not client ids and stay with the lead's spawn resolver.
Run with lab/tools/wiki-env/Scripts/python.exe [--chunk 40].
"""
import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

LAB = Path(r"C:\Users\Bryce\Documents\Projects\CartoonMMO\lab")
OUT = LAB / "references" / "quest-lines"
GROUP = {"client_reported": "trigger", "finish_minigame": "minigame", "defeat": "model", "gather_resource": "item",
         "visit_position": "place"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chunk", type=int, default=40)
    args = ap.parse_args()
    locale = {r["id"]: r["text"] for r in json.load(open(LAB / "reports" / "locale-id-to-text.json", encoding="utf-8"))}
    groups = defaultdict(list)
    for q in json.load(open(OUT / "objective-specs.json", encoding="utf-8")):
        qid = int(q["quest"].lstrip("q"))
        for o in q["objectives"]:
            g = GROUP.get(o["kind"])
            if not g or o.get("resolved"):
                continue
            idx = int(re.match(r"objective (\d+)", o["from"]).group(1))
            tid = o.get("text_string_id")
            groups[g].append({"quest_id": qid, "quest": q["quest"], "title": q["title"], "objective": idx,
                              "kind": o["kind"], "text_string_id": tid,
                              "text": locale.get(tid) if isinstance(tid, int) else o["from"].split(": ", 1)[-1],
                              "draft": {k: v for k, v in o.items() if k not in ("from", "resolved")},
                              "gap": next((x for x in q["gaps"] if x.startswith(f"objective {idx}:")), None)})
    out = OUT / "client-ids"
    out.mkdir(parents=True, exist_ok=True)
    made = {}
    for g, rows in groups.items():
        rows.sort(key=lambda r: (r["quest_id"], r["objective"]))
        for n in range(0, len(rows), args.chunk):
            f = out / f"worklist-{g}-{n // args.chunk + 1}.json"
            f.write_text(json.dumps(rows[n:n + args.chunk], indent=1, ensure_ascii=False), encoding="utf-8")
            made[f.name] = len(rows[n:n + args.chunk])
    print(json.dumps(made, indent=1))


if __name__ == "__main__":
    main()
