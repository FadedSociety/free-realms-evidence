"""augment_open_quests.py: give the quests that never went final the evidence later passes produced (lead, 2026-10-24).

Run with lab/tools/wiki-env/Scripts/python.exe, then continue the rounds:
  python augment_open_quests.py          -> packs.json: open quests gain later_answers (NPC, dialog, item, event)
  python quest_lines.py run --start 13 --rounds 20
The quest pass ran before the NPC, dialog, item and event passes, so its critics never saw those answers.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))  # -I leaves the script's own folder off sys.path
from quest_lines import OUT, norm  # noqa: E402


def load(name):
    data = json.load(open(OUT / name, encoding="utf-8"))
    if isinstance(data, dict):
        return [{"key": k, "status": "final" if s.get("final") else "open", "answer": s.get("answer")}
                for k, s in data.items()]
    return data


def main():
    packs = json.load(open(OUT / "packs.json", encoding="utf-8"))
    state = json.load(open(OUT / "state.json", encoding="utf-8"))
    npcs = {}
    for r in load("npcs.json"):
        a = r.get("answer") or {}
        if r["status"] == "final":
            npcs[norm((a.get("npc") or {}).get("name"))] = {k: a.get(k) for k in ("npc", "zone", "place", "roles",
                                                                                 "quests_given")}
    dialogs = {r["key"]: r.get("answer") for r in load("dialogs.json") if r["status"] == "final"}
    items = {norm(((r.get("answer") or {}).get("item") or {}).get("name")): (r.get("answer") or {}).get("sources")
             for r in load("items.json") if r["status"] == "final"}
    events = []
    for r in load("event-state.json"):
        a = r.get("answer") or {}
        qs = a.get("quests")
        qs = json.loads(qs) if isinstance(qs, str) and qs.startswith("[") else (qs or [])
        name = a.get("event")
        name = json.loads(name).get("name") if isinstance(name, str) and name.startswith("{") else name
        events.append((name, {norm(q) for q in qs if isinstance(q, str)}, r["status"]))
    n = 0
    for key, s in state.items():
        if s.get("final") or key not in packs:
            continue
        a = s.get("answer") or {}
        title = norm((a.get("quest") or {}).get("title") or packs[key].get("title"))
        people = {norm((a.get("giver") or {}).get("name"))} | {norm(o.get("target")) for o in a.get("objectives") or []}
        rewards = {norm(x.get("item") or x.get("name") or x.get("value")) for x in a.get("rewards") or []
                   if isinstance(x, dict)}
        packs[key]["later_answers"] = {
            "npc_answers": {p: npcs[p] for p in people if p and p in npcs},
            "dialog_answer": dialogs.get(key),
            "reward_item_answers": {i: items[i] for i in rewards if i and i in items},
            "events_listing_this_quest": [f"{e} ({st})" for e, qs, st in events if title and title in qs]}
        n += 1
    (OUT / "packs.json").write_text(json.dumps(packs, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({"augmented": n}))


if __name__ == "__main__":
    sys.exit(main())
