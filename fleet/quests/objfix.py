"""objfix.py: evidence packs for the objective fix pass (lead, 2026-10-25; world_lines.py --domain objfix).

One pack per quest whose objective draft is incomplete (objective-specs.json). Everything a fixer needs is joined
in, so it should not have to explore (lesson of 2026-10-24, memory fleet-pack-joins):
  - each objective's client text, the draft spec, its gap and the DeepSeek client-id candidate (with why it was
    not accepted), plus the neighbouring client lines (offer, progress, turn-in text often names counts and items);
  - the quest's dialog answer;
  - candidates per objective target: our NPC rows (placed or not), reference spawns (talk-spawns.json), enemy
    actor kinds (enemies.json / field_enemies.json: actor_kind_id is the enemy definition id, NOT the model id;
    reference Npcs.json ids sharing a model), client items, points of interest, minigames;
  - the server's objective kinds and their fields (quest_engine.rs ObjectiveKind).
"""
import json
import re
import sqlite3
from collections import defaultdict

from npc_match import npc_index, resolve
from quest_lines import CONTENT, LAB, OUT, norm

KINDS = {  # quest_engine.rs ObjectiveKind, as the zone briefs write them in data/content/quests
    "talk_to_npc": "npc_id (an NPC row the server draws)", "interact_npc": "npc_id (a clickable actor: objects too)",
    "kill_actor_kind": "actor_kind_id (enemy definition id) + count", "collect_item": "item_id + count",
    "use_item": "item_id", "equip_item": "definition_id", "gather_resource": "resource_id (item definition) + count",
    "craft_recipe": "recipe_id + count", "finish_minigame": "minigame_id + count", "reach_poi": "poi_id",
    "enter_area": "area_id",
    "visit_position": "zone_id (0 = the open world, every outdoor zone: src/bin/osfr_gateway/admin_move.rs:10), "
                      "position [x,y,z], radius",
    "select_job": "profile_id",
    "job_level": "profile_id + level", "complete_dungeon": "encounter_id",
    "client_reported": "client_id (any unused id; the server registers it) + trigger: look_at{guid, offset_tenths, "
                       "range, angle_degrees} | ui_event{event} | first_movement{mouse}",
}
REF = LAB / "references" / "FreeRealms-Legacy" / "src" / "Resources"
RES = LAB / "working" / "OSFR.Client" / "OSFR Client" / "Resources"


def words(text):
    """Match words, singular ("grenades" and "Grenade" meet)."""
    out = []
    for w in norm(text or "").split():
        w = w[:-3] + "y" if w.endswith("ies") and len(w) > 5 else w   # berries -> berry
        w = w[:-1] if w.endswith("s") and not w.endswith("ss") and len(w) > 4 else w
        if len(w) >= 4:
            out.append(w)
    return out


class Names:
    """name -> rows indexes for the candidate kinds, matched by the target's words."""

    def __init__(self, locale):
        self.by = defaultdict(lambda: defaultdict(list))
        enemies = [r for f in ("enemies.json", "field_enemies.json") for r in
                   (lambda d: d.get("definitions") or d.get("records") or [])(json.load(open(CONTENT / f, encoding="utf-8")))
                   if isinstance(r, dict) and r.get("actor_kind_id")]
        self.by_model = defaultdict(list)
        for r in enemies:
            row = {"actor_kind_id": r["actor_kind_id"], "name": r.get("kind") or r.get("name"), "model_id": r.get("model_id"),
                   "source": "data/content/enemies"}
            self.add("enemy", row["name"], row)
            self.by_model[r.get("model_id")].append(row)
        for x in json.load(open(REF / "Npcs.json", encoding="utf-8")):
            row = {"reference_npc_id": x["Id"], "model_id": x.get("ModelId"), "model": x.get("ModelFileName"),
                   "name": locale.get(x.get("NameId")), "source": "FreeRealms-Legacy Npcs.json (R)"}
            self.by_model[x.get("ModelId")].append(row)
        cat = json.load(open(LAB / "reports" / "native-20261024T0455Z-new" / "content" / "item-catalogue.json",
                             encoding="utf-8"))["definitions"]
        for d in cat:
            hx = d.get("serialized_hex") or ""
            if len(hx) >= 16:
                name = locale.get(int.from_bytes(bytes.fromhex(hx[8:16]), "little"))
                if name:
                    self.add("item", re.sub(r"\{[^}]*\}", "", name), {"item_id": d["id"], "name": re.sub(r"\{[^}]*\}", "", name)})
        for p in json.load(open(REF / "PointOfInterests.json", encoding="utf-8")):
            self.add("poi", p.get("Comment"), {"poi_id": p["Id"], "name": p.get("Comment"), "position": p.get("Position"),
                                               "source": "FreeRealms-Legacy PointOfInterests.json (R)"})
        for line in (RES / "MiniGameData.txt").read_text(encoding="utf-8", errors="replace").splitlines():
            f = line.split("^")
            if f[0].isdigit() and len(f) > 2 and f[2].isdigit():
                name = locale.get(int(f[2]))
                self.add("minigame", name, {"minigame_id": int(f[0]), "type": int(f[1]), "name": name})

    def add(self, kind, name, row):
        for w in set(words(name)):
            self.by[kind][w].append(row)

    def find(self, kind, target, limit=6):
        score = defaultdict(int)
        rows = {}
        for w in words(target):
            for r in self.by[kind].get(w, [])[:400]:
                k = json.dumps(r, sort_keys=True)
                score[k] += 1
                rows[k] = r
        return [rows[k] for k in sorted(score, key=lambda k: -score[k])[:limit]]


def objfix_packs(ev, complete=False):
    """Packs for the incomplete drafts, or (complete=True, domain objcheck) for the drafts that resolved, whose
    counts, splits and kill targets (model ids, not actor kinds) were never checked."""
    specs = json.load(open(OUT / "objective-specs.json", encoding="utf-8"))
    tags = {k: t for k, t in sqlite3.connect(OUT / "objectives.sqlite").execute("SELECT key, target FROM jev")}
    dialogs = {r["key"]: r["answer"] for r in json.load(open(OUT / "dialogs.json", encoding="utf-8")) if r.get("answer")}
    spawns = json.load(open(OUT / "wiring" / "talk-spawns.json", encoding="utf-8"))
    spawn_by = {norm(r["name"]): {k: r[k] for k in ("npc_id", "name", "zone", "match", "unique", "candidates")}
                for r in spawns["rows"]}
    spawn_by.update({norm(t["name"]): t for t in spawns["no_row_targets"] if t.get("match")})
    by_name, by_sid, names = npc_index()
    nm = Names(ev.locale)
    packs = {}
    for q in specs:
        if q["spec_complete"] != complete:
            continue
        objs, lines = [], []
        for o in q["objectives"]:
            i = int(re.match(r"objective (\d+)", o["from"]).group(1))
            target = tags.get(f"{q['quest']}o{i}")
            tid = o.get("text_string_id")
            if isinstance(tid, int):
                lines += [x for x in ev.cluster(tid, 8) if x not in lines]
            gap = next((g for g in q["gaps"] if g.startswith(f"objective {i}:")), None)
            row = {"index": i, "client_text": ev.locale.get(tid) if isinstance(tid, int) else o["from"],
                   "text_string_id": tid, "target": target,
                   "draft": {k: v for k, v in o.items() if k not in ("from", "resolved", "candidate")},
                   "resolved": o.get("resolved"), "gap": gap}
            if o.get("resolved") and not o.get("client_evidence"):
                row["draft_check"] = ("resolved by a local match of the target name to our tables (NPC rows; client "
                                      "MiniGameData.txt; the client item catalogue; enemy data; jobs; recipes): "
                                      "keep it if the candidate's name matches the target")
            if o.get("candidate"):
                row["client_id_candidate"] = o["candidate"]
            if target and (not o.get("resolved") or o["kind"] == "defeat"):
                npc = resolve(target, None, by_name, by_sid, names)
                model_ids = {o.get("model_id"), (o.get("candidate") or {}).get("fields", {}).get("model_id")
                             if isinstance((o.get("candidate") or {}).get("fields"), dict) else None} - {None}
                row["candidates"] = {k: v for k, v in {
                    "npc_row": npc and {k: npc[k] for k in ("npc_id", "name", "zone", "placed", "placement")},
                    "reference_spawn": spawn_by.get(norm(target)),
                    "enemy_actor_kinds": [r for m in model_ids for r in nm.by_model.get(m, [])][:6] + nm.find("enemy", target, 4),
                    "items": nm.find("item", target), "points_of_interest": nm.find("poi", target, 4),
                    "minigames": nm.find("minigame", target, 4)}.items() if v}
            objs.append(row)
        packs[q["quest"]] = {"title": q["title"], "live": q["live"], "objectives": objs,
                             "quest_lines": lines[:60], "dialog": dialogs.get(q["quest"]),
                             "server_objective_kinds": KINDS}
    return packs
