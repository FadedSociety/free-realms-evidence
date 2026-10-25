"""wiring_lists.py: per-topic work lists from the inferred answers, for wiring briefs (lead, 2026-10-24).

Run with lab/tools/wiki-env/Scripts/python.exe after wiring_coverage.py. Writes references/quest-lines/wiring/:
  zone-quests/<zone>.json  shipped-but-disabled quests the answers call live: giver, objectives, dialog ids, rewards
  prize-wheel.json, collection.json, drop.json, marketplace.json, quest-reward.json, event-item.json
                           items whose final answer gives that source (with the source rows and evidence)
  seasons.json             yearly season windows from the schedule rows, grouped by season name
"""
import json
import re
from collections import defaultdict
from pathlib import Path

LAB = Path(r"C:\Users\Bryce\Documents\Projects\CartoonMMO\lab")
OUT = LAB / "references" / "quest-lines"
W = OUT / "wiring"
CONTENT = LAB.parent / "autopilot-int" / "prototype" / "osfr-tools" / "data" / "content"


def load(name):
    return json.load(open(OUT / name, encoding="utf-8"))


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", (s or "unknown").lower()).strip("-") or "unknown"


# The answers' zone fields are free text ("Briarwood (giver); Briarheart Palace, Blackspore (objectives)"): a quest goes
# to the first canonical zone its text names (the giver's zone comes first in nearly every answer).
ZONES = ["Sanctuary", "Briarwood", "Snowhill", "Blackspore", "Seaside", "Southvale", "Merry Vale", "Cobblestone",
         "Greenwood", "Wugachug", "Sunstone", "Highroad", "Lakeshore", "Shrouded Glade", "Farnum", "Dartmoor", "Wilds",
         "Stillwater", "Sacred Grove", "Wildwood", "Durango", "Thunder Falls", "Speedway", "Briarheart", "Nettleseed",
         "Darklit Lagoon", "Forest Troll Fort"]
CANON = {"Briarheart": "Blackspore", "Darklit Lagoon": "Briarwood", "Speedway": "Speedways", "Cobblestone": "Cobblestone Village",
         "Greenwood": "Greenwood Forest", "Sunstone": "Sunstone Valley", "Highroad": "Highroad Junction",
         "Farnum": "Farnum Farmstead", "Stillwater": "Stillwater Crossing", "Durango": "Durango Zoo",
         "Nettleseed": "Sanctuary", "Forest Troll Fort": "Wilds"}


def zone_of(text):
    text = text or ""
    hits = [(text.find(z), z) for z in ZONES if z in text]
    if not hits:
        return "unknown"
    z = min(hits)[1]
    return CANON.get(z, z)


def main():
    (W / "zone-quests").mkdir(parents=True, exist_ok=True)
    # Shipped-but-disabled quests whose final answer says live "yes" or "unsure" (Bryce 2026-10-24: wire them all; an
    # "unsure" row is enabled as (R) unless the flag list marks it not live).
    disabled = set()
    for f in (CONTENT / "quests").glob("*.json"):
        disabled |= {r["id"] for r in json.load(open(f, encoding="utf-8")).get("records", []) if not r.get("enabled")}
    dialogs = {r["key"]: r for r in load("dialogs.json") if r["status"] == "final"}
    zones = defaultdict(list)
    for r in load("quests.json"):
        key = r["key"].lstrip("q")
        if r["status"] != "final" or not key.isdigit() or int(key) not in disabled:
            continue
        a = r["answer"] or {}
        if a.get("live") not in ("yes", "unsure"):
            continue
        d = (dialogs.get(r["key"]) or {}).get("answer") or {}
        zones[zone_of(a.get("zone"))].append({
            "quest_id": int(key), "record": f"quest-lines/quests.json {r['key']}",
            "title": (a.get("quest") or {}).get("title"), "giver": a.get("giver"), "objectives": a.get("objectives"),
            "rewards": a.get("rewards"), "line": a.get("line"), "live": a.get("live"),
            "dialog": {s: d.get(s) for s in ("offer", "progress", "complete")} if d else None,
            "wireable": any(c.get("wireable") for c in r.get("last_critiques") or [])})
    for z, rows in zones.items():
        (W / "zone-quests" / f"{slug(z)}.json").write_text(json.dumps({"zone": z, "quests": rows}, indent=1,
                                                                     ensure_ascii=False), encoding="utf-8")
    stores = {r["item_id"]: r for r in json.load(open(CONTENT / "stores.json", encoding="utf-8"))["items"]}
    by_type = defaultdict(list)
    for name in ("items.json", "citems.json"):
        for r in load(name):
            if r["status"] != "final":
                continue
            a = r["answer"] or {}
            item = a.get("item") or {}
            for s in a.get("sources") or []:
                t = (s.get("type") or "other").replace(" ", "_")
                by_type[t].append({"item": item.get("name"), "item_locale_id": item.get("locale_id"),
                                   "record": f"quest-lines/{name} {r['key']}", "source": s,
                                   "store_row": stores.get(item.get("id")) if isinstance(item.get("id"), int) else None})
    picks = {"prize_wheel": "prize-wheel", "collection": "collection", "drop": "drop", "marketplace": "marketplace",
             "quest_reward": "quest-reward", "event": "event-item"}
    for t, f in picks.items():
        (W / f"{f}.json").write_text(json.dumps(by_type.get(t, []), indent=1, ensure_ascii=False), encoding="utf-8")
    seasons = defaultdict(list)
    for r in load("schedules.json"):
        a = r["answer"] or {}
        s = a.get("season")
        if r["status"] == "final" and s and (a.get("revival") or {}).get("recurrence") == "yearly_season":
            seasons[s.get("name")].append({"event": (a.get("event") or {}).get("name"), "record": f"quest-lines/schedules.json {r['key']}",
                                           "season": s, "zones": a.get("zones"), "runs": a.get("runs"),
                                           "original_dates": a.get("original_dates")})
    (W / "seasons.json").write_text(json.dumps(seasons, indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"zones": {z: len(v) for z, v in sorted(zones.items(), key=lambda kv: -len(kv[1]))},
                      "items": {t: len(by_type.get(t, [])) for t in picks}, "seasons": {k: len(v) for k, v in seasons.items()}}))


if __name__ == "__main__":
    main()
