"""apply_objfix.py: merge the objective fix pass into builder-ready specs (lead, 2026-10-25).

Reads objective-specs.json (drafts with the client-id overlay) and objfixs.json (world_lines.py --domain objfix);
writes references/quest-lines/objective-specs-fixed.json. A quest with a final fix answer takes its fixed objectives;
every id is checked against our tables (NPC rows, enemy actor kinds, the item catalogue, POIs, MiniGameData) and an
id that is not there downgrades the objective ("needs_npc_row", "unknown"), because the critic missed invented ids.
  spec_complete     every objective settled (a builder can wire it now)
  after_placement   every objective settled or needs_placement on a real NPC row (wire after placing talk-spawns)
Run with lab/tools/wiki-env/Scripts/python.exe.
"""
import json
import re
import sqlite3
from collections import Counter

from npc_match import CONTENT, norm
from quest_lines import LAB, OUT

FIELD_TABLE = {"npc_id": "npc", "actor_kind_id": "actor", "item_id": "item", "resource_id": "item",
               "definition_id": "item", "poi_id": "poi", "minigame_id": "minigame"}


def tables():
    load = lambda p: json.load(open(p, encoding="utf-8"))  # noqa: E731
    npc = {r["npc_id"] for f in (CONTENT / "npcs").glob("*.json") for r in load(f)["records"]}
    npc |= {r.get("spawn_guid") for r in load(CONTENT / "npc_spawns_extra.json")["records"]}
    actor = {r["actor_kind_id"] for f in ("enemies.json", "field_enemies.json")
             for r in (lambda d: d.get("definitions") or d.get("records") or [])(load(CONTENT / f)) if isinstance(r, dict)}
    item = {d["id"] for d in load(LAB / "reports" / "native-20261024T0455Z-new" / "content" / "item-catalogue.json")["definitions"]}
    poi = {p["Id"] for p in load(LAB / "references" / "FreeRealms-Legacy" / "src" / "Resources" / "PointOfInterests.json")}
    mg_file = LAB / "working" / "OSFR.Client" / "OSFR Client" / "Resources" / "MiniGameData.txt"
    minigame = {int(x.split("^")[0]) for x in mg_file.read_text(encoding="utf-8", errors="replace").splitlines() if x[:1].isdigit()}
    return {"npc": npc, "actor": actor, "item": item, "poi": poi, "minigame": minigame}


def names():
    """Client names for the draft ids a name check can restore: minigame id and item id -> normalized name."""
    loc = {r["id"]: r["text"] for r in json.load(open(LAB / "reports" / "locale-id-to-text.json", encoding="utf-8"))}
    clean = lambda s: norm(re.sub(r"\{[^}]*\}", "", s or ""))  # noqa: E731
    mg = {}
    mg_file = LAB / "working" / "OSFR.Client" / "OSFR Client" / "Resources" / "MiniGameData.txt"
    for line in mg_file.read_text(encoding="utf-8", errors="replace").splitlines():
        f = line.split("^")
        if f[0].isdigit() and len(f) > 2 and f[2].isdigit():
            mg[int(f[0])] = clean(loc.get(int(f[2])))
    item = {}
    for d in json.load(open(LAB / "reports" / "native-20261024T0455Z-new" / "content" / "item-catalogue.json",
                            encoding="utf-8"))["definitions"]:
        hx = d.get("serialized_hex") or ""
        if len(hx) >= 16:
            item[d["id"]] = clean(loc.get(int.from_bytes(bytes.fromhex(hx[8:16]), "little")))
    return {"finish_minigame": ("minigame_id", mg), "gather_resource": ("resource_id", item)}


def name_match(name, target):
    """Every target word is in the table name ("Rainleaf" in "bundle of rainleaf"), plurals folded."""
    fold = lambda s: {w.rstrip("s") for w in norm(s or "").split() if len(w) > 2}  # noqa: E731
    t = fold(target)
    return bool(t) and t <= fold(name)


def restored(o, d, target, nm):
    """A fixer that withdrew a draft minigame/item id only for want of a citation, when the id's own client name
    matches the target, gets the id back (Haiku was over-cautious on 42 of these, 2026-10-25)."""
    if o.get("status") != "unknown" or not d or d["kind"] not in nm or o.get("kind") not in (d["kind"], None):
        return o
    field, table = nm[d["kind"]]
    name = table.get(d.get(field))
    if not name or not name_match(name, target):
        return o
    fields = {**(o.get("fields") or {}), field: d[field]}
    if not isinstance(fields.get("count"), int):
        fields["count"] = d.get("count") or d.get("quantity") or 1
    return {**o, "kind": d["kind"], "fields": fields, "status": "settled",
            "note": f"(lead check) draft {field} {d[field]} is named '{name}', matching target '{target}'. "
                    + (o.get("note") or "")}


def checked(o, t):
    """The objective with its ids checked: an id missing from its table downgrades the status, with the reason."""
    o = dict(o)
    for field, table in FIELD_TABLE.items():
        v = (o.get("fields") or {}).get(field)
        if v is not None and v not in t[table]:
            o["status"] = "needs_npc_row" if field == "npc_id" else "unknown"
            o["note"] = f"(lead check) {field} {v} is not in our {table} data. " + (o.get("note") or "")
    return o


def main():
    t, nm = tables(), names()
    tags = {k: v for k, v in sqlite3.connect(OUT / "objectives.sqlite").execute("SELECT key, target FROM jev")}
    fixed = {}
    for name in ("objfixs.json", "objchecks.json"):  # incomplete drafts fixed; complete drafts checked
        path = OUT / name
        if path.exists():
            fixed.update({r["key"]: (name[:-6], r) for r in json.load(open(path, encoding="utf-8")) if r["status"] == "final"})
    out, stats, statuses = [], Counter(), Counter()
    for q in json.load(open(OUT / "objective-specs.json", encoding="utf-8")):
        tag = "draft complete" if q["spec_complete"] else "draft incomplete"
        if q["quest"] not in fixed:
            # An unchecked complete draft may still carry model ids for kills and count 1 defaults.
            out.append({**q, "source": f"{tag} (no final fix/check answer)", "after_placement": q["spec_complete"]})
            stats[f"{tag}, unchecked"] += 1
            continue
        domain, row = fixed[q["quest"]]
        drafts = {int(o["from"].split(":")[0].split()[1]): o for o in q["objectives"] if o.get("resolved")}
        objs = [checked(restored(o, drafts.get(o.get("index")), tags.get(f"{q['quest']}o{o.get('index')}") or "", nm), t)
                for o in (row["answer"] or {}).get("objectives") or []]
        statuses.update(o.get("status") for o in objs)
        complete = bool(objs) and all(o.get("status") == "settled" for o in objs)
        after = bool(objs) and all(o.get("status") in ("settled", "needs_placement") for o in objs)
        stats[f"{tag} -> " + ("complete" if complete else "after placement" if after else "blocked")] += 1
        out.append({"quest": q["quest"], "record": q["record"], "title": q["title"], "live": q["live"],
                    "spec_complete": complete, "after_placement": after, "source": f"{domain} (Haiku, critic-passed)",
                    "objectives": objs, "open": (row["answer"] or {}).get("open", [])})
    (OUT / "objective-specs-fixed.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"quests": stats, "spec_complete": sum(q["spec_complete"] for q in out),
                      "after_placement": sum(q["after_placement"] for q in out),
                      "fixed_objective_statuses": statuses}, indent=1))


if __name__ == "__main__":
    t0 = {"npc": {1}, "actor": set(), "item": set(), "poi": set(), "minigame": set()}
    assert checked({"fields": {"npc_id": 2}, "status": "needs_placement"}, t0)["status"] == "needs_npc_row"
    assert checked({"fields": {"npc_id": 1}, "status": "settled"}, t0)["status"] == "settled"
    nm0 = {"gather_resource": ("resource_id", {7: "bundle of rainleaf"})}
    d0 = {"kind": "gather_resource", "resource_id": 7, "quantity": 2}
    assert restored({"status": "unknown", "kind": "gather_resource", "fields": {}}, d0, "Rainleaf", nm0)["status"] == "settled"
    assert restored({"status": "unknown", "kind": "gather_resource", "fields": {}}, d0, "shark", nm0)["status"] == "unknown"
    main()
