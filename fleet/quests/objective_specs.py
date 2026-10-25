"""objective_specs.py: rebuild each final quest's objectives in the server's objective schema (lead, 2026-10-25).

The quest pass left objectives in loose form (kind words, text ids, target names); the server needs
talk_to_npc{npc_id} / visit_position{zone_id, position, radius} / defeat{model_id, count} / gather_resource{resource_id,
quantity} / craft_recipe{recipe_id, quantity} / complete_dungeon{encounter_id} / finish_minigame{minigame_id, count} /
job_level{profile_id, level} / client_reported. Run with lab/tools/wiki-env/Scripts/python.exe:
  python objective_specs.py jev      Jev classifies every objective: server kind, count, target name, job, level
  python objective_specs.py resolve  resolve targets to our ids -> references/quest-lines/objective-specs.json
  python objective_specs.py status
A quest is spec_complete when every objective resolves (narration lines are dropped); the rest name what is missing.
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
import threading
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))  # -I leaves the script's own folder off sys.path
from locale_index import NO_FLAG, ask_jev  # noqa: E402
from npc_match import norm, npc_index, resolve  # noqa: E402
from wiring_lists import CONTENT, LAB, OUT  # noqa: E402

KINDS = ("talk_to_npc", "visit_position", "defeat", "gather_resource", "craft_recipe", "complete_dungeon",
         "finish_minigame", "job_level", "client_reported", "narration")
PROMPT = """You convert quest objectives from the kids' MMO Free Realms into a game server's objective kinds.
Each line is "key: loose kind | objective text | target". For EVERY line answer exactly one line:
key|kind|count|target|job|level
- kind, one of: talk_to_npc (talk to, speak with, report to, deliver to, return to an NPC), visit_position (go to,
  find, reach, explore a place), defeat (defeat, beat, knock out, battle enemies), gather_resource (collect, gather,
  harvest, mine, find N items), craft_recipe (cook, forge, smelt, craft an item), complete_dungeon (clear, finish a
  dungeon or battle), finish_minigame (win, play, race, beat a minigame, card duel, kart race, fishing), job_level (reach
  level N as a job), client_reported (use an item, click, move, open a window), narration (not a task: story text).
- count: the number the text asks for (digits; "two" -> 2), or 1 when it asks for one thing, or empty.
- target: the NPC, place, enemy, item, recipe, dungeon or minigame named, cleaned to its proper name, or empty.
- job and level: only for job_level (e.g. Archer|5), else empty.
Answer only the lines, one per key, nothing else."""
NUM = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
       "twelve": 12, "fifteen": 15, "twenty": 20}
lock = threading.Lock()


def db():
    con = sqlite3.connect(OUT / "objectives.sqlite", check_same_thread=False)
    con.executescript("""
    CREATE TABLE IF NOT EXISTS obj(key TEXT PRIMARY KEY, quest TEXT, idx INTEGER, line TEXT, payload TEXT);
    CREATE TABLE IF NOT EXISTS jev(key TEXT PRIMARY KEY, kind TEXT, count INTEGER, target TEXT, job TEXT, level INTEGER,
        batch INTEGER);
    CREATE TABLE IF NOT EXISTS jev_spend(batch INTEGER PRIMARY KEY, usd REAL, model TEXT, ok INTEGER);
    """)
    return con


def final_quests():
    return [r for r in json.load(open(OUT / "quests.json", encoding="utf-8"))
            if r["status"] == "final" and r["key"].lstrip("q").isdigit()]


def fill(con):
    con.execute("DELETE FROM obj")
    for r in final_quests():
        for i, o in enumerate((r["answer"] or {}).get("objectives") or []):
            line = f"{o.get('kind') or '-'} | {str(o.get('text') or '-')[:180]} | {str(o.get('target') or '-')[:80]}"
            con.execute("INSERT INTO obj VALUES(?,?,?,?,?)", (f"{r['key']}o{i}", r["key"], i, line,
                                                             json.dumps(o, ensure_ascii=False)))
    con.commit()


def batches(con, size=25):
    rows = con.execute("SELECT key, line FROM obj ORDER BY key").fetchall()
    out = [(k // size, rows[k:k + size]) for k in range(0, len(rows), size)]
    if con.execute("SELECT count(*) FROM jev_spend").fetchone()[0] >= len(out):
        left = con.execute("SELECT key, line FROM obj WHERE key NOT IN (SELECT key FROM jev) ORDER BY key").fetchall()
        out += [(100000 + k // 5, left[k:k + 5]) for k in range(0, len(left), 5)]
    return out


def parse(text, lines):
    want, got = {k for k, _ in lines}, {}
    for ln in text.splitlines():
        p = [x.strip() for x in ln.strip().strip("`").split("|")]
        if len(p) >= 6 and p[0] in want:
            kind = p[1].lower() if p[1].lower() in KINDS else "narration"
            count = int(p[2]) if p[2].isdigit() else None
            level = int(p[5]) if p[5].isdigit() else None
            got[p[0]] = (kind, count, None if NO_FLAG.fullmatch(p[3]) else p[3][:100],
                         None if NO_FLAG.fullmatch(p[4]) else p[4][:40], level)
    return got


def jev(con, threads):
    if not con.execute("SELECT count(*) FROM obj").fetchone()[0]:
        fill(con)
    done = {b for (b,) in con.execute("SELECT batch FROM jev_spend WHERE ok=1")}
    todo = [(b, lines) for b, lines in batches(con) if b not in done]

    def work(b, lines):
        text, usd, model = ask_jev(lines, PROMPT)
        got = parse(text, lines)
        ok = len(got) >= 0.9 * len(lines)
        with lock:
            con.execute("INSERT OR REPLACE INTO jev_spend VALUES(?,?,?,?)", (b, usd, model, int(ok)))
            if ok:
                con.executemany("INSERT OR REPLACE INTO jev VALUES(?,?,?,?,?,?,?)",
                                [(k, *got[k], b) for k, _ in lines if k in got])
            con.commit()

    if todo:
        ask_jev(todo[0][1][:2], PROMPT)  # fail fast on a refused key
    with ThreadPoolExecutor(threads) as pool:
        for b, lines in todo:
            pool.submit(work, b, lines)
    print(json.dumps({"batches": len(todo), "tagged": con.execute("SELECT count(*) FROM jev").fetchone()[0],
                      "of": con.execute("SELECT count(*) FROM obj").fetchone()[0]}))


def name_maps():
    locale = {r["id"]: r["text"] for r in json.load(open(LAB / "reports" / "locale-id-to-text.json", encoding="utf-8"))}
    enemies = {}
    for d in json.load(open(CONTENT / "enemies.json", encoding="utf-8"))["definitions"]:
        n = locale.get(d.get("name_string_id"))
        if n:
            enemies.setdefault(norm(n), d.get("model_id"))
    enc = json.load(open(CONTENT / "encounters.json", encoding="utf-8"))
    for e in enc.get("world_enemies") or []:
        if e.get("name"):
            enemies.setdefault(norm(e["name"]), e.get("model_id"))
    dungeons = {}
    for d in enc.get("dungeons") or []:
        for k in ("name", "title"):
            if d.get(k):
                dungeons[norm(d[k])] = d.get("id")
        for e in d.get("enemies") or []:
            if e.get("name"):
                enemies.setdefault(norm(e["name"]), e.get("model_id"))
    for b in json.load(open(CONTENT / "field_battles.json", encoding="utf-8")).get("battles") or []:
        t = locale.get(b.get("title_id"))
        if t:
            dungeons.setdefault(norm(t), b.get("id"))
    recipes = {norm(r["name"]): r.get("recipe_id") for r in json.load(open(CONTENT / "recipes.json", encoding="utf-8"))["records"]
               if r.get("name") and r.get("recipe_id")}
    jobs = {norm(r["name"]): r.get("profile_id") for r in json.load(open(CONTENT / "jobs.json", encoding="utf-8"))["records"]
            if r.get("name")}
    # Client MiniGameData.txt: ID^TYPE^NAME_ID^... (minigame name -> minigame id); recipe names also name their minigame.
    minigames = {}
    client = LAB / "working" / "OSFR.Client" / "OSFR Client" / "Resources" / "MiniGameData.txt"
    for line in client.read_text(encoding="utf-8", errors="replace").splitlines():
        p = line.split("^")
        if len(p) > 2 and p[0].isdigit() and p[2].isdigit() and locale.get(int(p[2])):
            minigames.setdefault(norm(locale[int(p[2])]), int(p[0]))
    for r in json.load(open(CONTENT / "recipes.json", encoding="utf-8"))["records"]:
        if r.get("name") and r.get("minigame_id"):
            minigames.setdefault(norm(r["name"]), r["minigame_id"])
    # gather_resource counts an item: resource_id is the item definition id (gameplay/crafting.rs). Client item names.
    import struct
    resources = {}
    catalogue = LAB / "reports" / "native-20261024T0455Z-new" / "content" / "item-catalogue.json"
    for d in json.load(open(catalogue, encoding="utf-8"))["definitions"]:
        name_id = struct.unpack("<i", bytes.fromhex(d["serialized_hex"][8:16]))[0]
        if locale.get(name_id):
            resources.setdefault(norm(locale[name_id]), d["id"])
    # More enemies: NPC rows with an enemy role, field-enemy members, dungeon files, unresolved enemies.
    for f in (CONTENT / "npcs").glob("*.json"):
        for r in json.load(open(f, encoding="utf-8")).get("records", []):
            if "enemy" in (r.get("roles") or []) and r.get("name") and r.get("model_id"):
                enemies.setdefault(norm(r["name"]), r["model_id"])

    def walk(node):
        if isinstance(node, dict):
            sid = node.get("name_id") or node.get("name_string_id")
            n = node.get("name") or (locale.get(sid) if isinstance(sid, int) else None)
            if isinstance(n, str) and isinstance(node.get("model_id"), int):
                enemies.setdefault(norm(n), node["model_id"])
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)
    for f in ["field_enemies.json", "enemies_unresolved.json"] + [f"dungeons/{p.name}" for p in (CONTENT / "dungeons").glob("*.json")]:
        walk(json.load(open(CONTENT / f, encoding="utf-8")))
    return {"defeat": enemies, "complete_dungeon": dungeons, "craft_recipe": recipes, "job_level": jobs,
            "finish_minigame": minigames, "gather_resource": resources}


def lookup(table, name):
    n = norm(name)
    if not n:
        return None
    for v in (n, re.sub(r"es$", "", n), re.sub(r"s$", "", n)):  # "Robgoblins" -> "robgoblin"
        if v in table:
            return table[v]
    hit = next((k for k in sorted(table, key=len, reverse=True) if len(k) >= 4 and re.search(rf"\b{re.escape(k)}\b", n)), None)
    return table[hit] if hit else None


def count_of(text, jev_count):
    if jev_count:
        return jev_count
    m = re.search(r"\b(\d+)\b", text or "")
    if m:
        return int(m.group(1))
    w = next((NUM[x] for x in re.findall(r"[a-z]+", (text or "").lower()) if x in NUM), None)
    return w or 1


def resolve_all(con):
    by_name, by_sid, names = npc_index()
    maps = name_maps()
    tags = {k: (kind, c, t, j, lv) for k, kind, c, t, j, lv in con.execute("SELECT key, kind, count, target, job, level FROM jev")}
    quests, stats, missing = [], Counter(), Counter()
    for r in final_quests():
        a = r["answer"] or {}
        specs, gaps = [], []
        for i, o in enumerate(a.get("objectives") or []):
            kind, c, target, job, level = tags.get(f"{r['key']}o{i}", (None, None, None, None, None))
            target = target or o.get("target")
            text = o.get("text") or ""
            base = {"text_string_id": o.get("text_locale_id"), "from": f"objective {i}: {text[:120]}"}
            if kind in (None, "narration"):
                if kind is None:
                    gaps.append(f"objective {i}: not classified")
                continue
            spec, gap = {"kind": kind, **base}, None
            if kind == "talk_to_npc":
                row = resolve(target, o.get("target_locale_id"), by_name, by_sid, names)
                spec["npc_id"] = row["npc_id"] if row and row["placed"] else None
                gap = None if spec["npc_id"] else f"talk target {target!r} not placed in our NPC rows"
            elif kind == "visit_position":
                row = resolve(target, o.get("target_locale_id"), by_name, by_sid, names)
                if row and row["placed"]:
                    spec.update(npc_anchor=row["npc_id"], radius=8.0)
                else:
                    gap = f"place {target!r} has no position in our data"
            elif kind in ("defeat", "gather_resource", "craft_recipe", "finish_minigame", "complete_dungeon"):
                field = {"defeat": "model_id", "gather_resource": "resource_id", "craft_recipe": "recipe_id",
                         "finish_minigame": "minigame_id", "complete_dungeon": "encounter_id"}[kind]
                spec[field] = lookup(maps[kind], target)
                if kind in ("defeat", "gather_resource", "craft_recipe", "finish_minigame"):
                    spec["count" if kind in ("defeat", "finish_minigame") else "quantity"] = count_of(text, c)
                gap = None if spec[field] is not None else f"{kind} target {target!r} has no {field} in our data"
            elif kind == "job_level":
                spec.update(profile_id=lookup(maps["job_level"], job or target or text), level=level or count_of(text, None))
                gap = None if spec["profile_id"] else f"job {job or target!r} not in jobs.json"
            elif kind == "client_reported":
                gap = "client_reported trigger needs a client id from the decompile"
            if gap:
                gaps.append(f"objective {i}: {gap}")
                missing[gap.split(" ")[0] + " " + kind] += 1
            specs.append({**spec, "resolved": gap is None})
        complete = bool(specs) and not gaps
        stats["spec_complete" if complete else "incomplete"] += 1
        quests.append({"quest": r["key"], "record": f"quest-lines/quests.json {r['key']}",
                       "title": (a.get("quest") or {}).get("title"), "live": a.get("live"), "spec_complete": complete,
                       "objectives": specs, "gaps": gaps})
    (OUT / "objective-specs.json").write_text(json.dumps(quests, indent=1, ensure_ascii=False), encoding="utf-8")
    kinds = Counter(s["kind"] for q in quests for s in q["objectives"])
    resolved = Counter(s["kind"] for q in quests for s in q["objectives"] if s["resolved"])
    print(json.dumps({"quests": stats, "objectives_by_kind": {k: f"{resolved[k]}/{kinds[k]}" for k in kinds},
                      "top_gaps": missing.most_common(10)}, indent=1))


def status(con):
    q = lambda sql: con.execute(sql).fetchall()  # noqa: E731
    print(json.dumps({"objectives": q("SELECT count(*) FROM obj")[0][0], "jev_tagged": q("SELECT count(*) FROM jev")[0][0],
                      "kinds": dict(q("SELECT kind, count(*) FROM jev GROUP BY kind ORDER BY 2 DESC")),
                      "jev_usd": q("SELECT round(coalesce(sum(usd),0),3) FROM jev_spend")[0][0]}, indent=1))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=["jev", "resolve", "status"])
    ap.add_argument("--threads", type=int, default=16)
    args = ap.parse_args()
    con = db()
    {"jev": lambda: jev(con, args.threads), "resolve": lambda: resolve_all(con), "status": lambda: status(con)}[args.step]()


if __name__ == "__main__":
    main()
