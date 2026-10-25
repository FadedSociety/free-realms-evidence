"""wiring_coverage.py: how much of each inferred answer set is already in the game's data/content (lead, 2026-10-24).

Run with lab/tools/wiki-env/Scripts/python.exe [content dir]. Prints one block per domain and writes
references/quest-lines/wiring-coverage.json (the gap lists the wiring briefs work from).
"""
import json
import sys
from collections import Counter
from pathlib import Path

LAB = Path(r"C:\Users\Bryce\Documents\Projects\CartoonMMO\lab")
OUT = LAB / "references" / "quest-lines"
CONTENT = Path(sys.argv[1]) if len(sys.argv) > 1 else LAB.parent / "autopilot-int" / "prototype" / "osfr-tools" / "data" / "content"


def load(name):
    return json.load(open(OUT / name, encoding="utf-8"))


def final(rows):
    return [r for r in rows if r.get("status") == "final"]


def wireable(r):
    return any(c.get("wireable") for c in r.get("last_critiques") or [])


def as_obj(v):
    return json.loads(v) if isinstance(v, str) and v[:1] in "[{" else v


report = {}
# Quests: final answers vs shipped quest records.
shipped = {}
for f in (CONTENT / "quests").glob("*.json"):
    for r in json.load(open(f, encoding="utf-8")).get("records", []):
        shipped[r["id"]] = (f.name, bool(r.get("enabled")), r)
qs = final(load("quests.json"))
miss, disabled, live_missing, wiki_only = [], [], [], []


def quest_id(r):
    key = r["key"].lstrip("q")
    if key.isdigit():
        return int(key)
    qid = ((r["answer"] or {}).get("quest") or {}).get("id")
    return int(qid) if str(qid or "").isdigit() else None


for r in qs:
    qid = quest_id(r)
    live = (r["answer"] or {}).get("live")
    if qid is None:
        wiki_only.append(r["key"])
    elif qid not in shipped:
        miss.append(qid)
        if live == "yes":
            live_missing.append(qid)
    elif not shipped[qid][1] and live == "yes":
        disabled.append(qid)
zones = Counter((r["answer"] or {}).get("zone") for r in qs if quest_id(r) in live_missing)
report["quests"] = {"final": len(qs), "shipped_records": len(shipped), "final_not_shipped": len(miss),
                    "final_live_yes_not_shipped": len(live_missing), "wiki_only_no_client_id": len(wiki_only), "shipped_but_disabled_live_yes": len(disabled),
                    "missing_live_by_zone": dict(zones.most_common(20)), "live_missing_ids": live_missing,
                    "disabled_live_ids": disabled}
# Dialogs: final dialog answers with offer/complete ids for enabled quests.
ds = final(load("dialogs.json"))
report["dialogs"] = {"final": len(ds), "wireable": sum(map(wireable, ds)),
                     "with_offer_and_complete": sum(1 for r in ds if (r["answer"] or {}).get("offer")
                                                   and (r["answer"] or {}).get("complete"))}
# Items: wiki items + client items, final sources by type, and which are already priced in stores.json.
stores = {r["item_id"]: r for r in json.load(open(CONTENT / "stores.json", encoding="utf-8"))["items"]}
src = Counter()
for name in ("items.json", "citems.json"):
    for r in final(load(name)):
        for s in (r["answer"] or {}).get("sources") or []:
            src[s.get("type")] += 1
cat = json.load(open(OUT / "catalogue.sqlite.json", encoding="utf-8")) if (OUT / "catalogue.sqlite.json").exists() else None
report["items"] = {"final_wiki": len(final(load("items.json"))), "final_client": len(final(load("citems.json"))),
                   "wireable_client": sum(map(wireable, final(load("citems.json")))), "sources": dict(src.most_common()),
                   "stores_rows": len(stores), "stores_coin_priced": sum(1 for r in stores.values() if r.get("purchase_price_coins")),
                   "stores_sc_priced": sum(1 for r in stores.values() if r.get("sc_price"))}
# Events: schedule rows vs world_events.json and seasons.
sch = final(load("schedules.json"))
we = json.load(open(CONTENT / "world_events.json", encoding="utf-8")).get("events", [])
seasons = [s["name"] for s in json.load(open(CONTENT / "client_areas.json", encoding="utf-8"))["seasons"]]
rec = Counter(((r["answer"] or {}).get("revival") or {}).get("recurrence") for r in sch)
yearly = [r for r in sch if ((r["answer"] or {}).get("revival") or {}).get("recurrence") == "yearly_season"
          and (r["answer"] or {}).get("season")]
season_names = Counter(((r["answer"] or {}).get("season") or {}).get("name") for r in yearly)
report["events"] = {"final_schedules": len(sch), "wireable": sum(map(wireable, sch)), "recurrence": dict(rec),
                    "yearly_with_season": len(yearly), "season_names": dict(season_names.most_common(25)),
                    "world_events_defined": len(we), "seasons_defined": seasons}
# NPCs: final NPC answers vs rows.
ns = final(load("npcs.json"))
report["npcs"] = {"final": len(ns), "wireable": sum(map(wireable, ns)),
                  "with_dialog": sum(1 for r in ns if (r["answer"] or {}).get("dialog"))}
(OUT / "wiring-coverage.json").write_text(json.dumps(report, indent=1), encoding="utf-8")
for k, v in report.items():
    print(k, json.dumps({a: b for a, b in v.items() if not a.endswith("_ids")}))
