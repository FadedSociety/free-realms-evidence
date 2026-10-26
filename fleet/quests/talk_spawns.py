"""talk_spawns.py: reference spawn candidates for NPCs the server cannot draw yet (lead, 2026-10-25).

Our NPC rows with placement poi_anchor/unanchored are not drawn by world.rs, so quests that give from or talk to them
cannot run. The earlier legacy join matched spawns only by our row's name_string_id; many rows carry other locale
tables, so this joins by name instead:
  name   the spawn's Npcs.json NameId resolves (client locale) to the row's name
  model  the spawn's character model file names the NPC (fairy_darkthorne_f.adr), character models only
Sources: FreeRealms-Legacy and Sanctuary-main FabledRealms.lua spawns + Npcs.json (read as data, cited by file:line).
Also covers unresolved talk targets with no NPC row at all. Writes references/quest-lines/wiring/talk-spawns.json;
`unique` means every candidate spawn sits within 5 m of the first, else the zone briefs choose (or the fix pass).
Run with lab/tools/wiki-env/Scripts/python.exe.
"""
import json
import re
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path

from npc_match import CONTENT, norm

LAB = Path(r"C:\Users\Bryce\Documents\Projects\CartoonMMO\lab")
QL = LAB / "references" / "quest-lines"
SOURCES = ("FreeRealms-Legacy", "Sanctuary-main-20261019")
TITLES = {"queen", "king", "mayor", "assistant", "master", "archer", "farmer", "guard", "captain", "sir", "lady",
          "chef", "professor", "the", "of", "doctor", "general", "elder", "princess", "prince", "coach"}
NOT_CHARACTER = re.compile(r"^(evnt|sg|eng|bw|prop|veh|fx|ui|pet|mnt)_")
SPAWN = re.compile(r"spawnNpc\w*\((\d+),\s*(?:\d+,\s*)?(-?[\d.]+),\s*(-?[\d.]+),\s*(-?[\d.]+),\s*(-?[\d.]+)")


def spawns():
    """Reference npc id -> its spawns, each {source, line, position, heading, model, name_id}."""
    out = defaultdict(list)
    for src in SOURCES:
        base = LAB / "references" / src / "src"
        npcs = {x["Id"]: x for x in json.load(open(base / "Resources" / "Npcs.json", encoding="utf-8"))}
        lua = base / "Scripts" / "Zone" / "FabledRealms.lua"
        for ln, line in enumerate(open(lua, encoding="utf-8", errors="replace"), 1):
            m = SPAWN.search(line)
            if not m:
                continue
            ref = int(m.group(1))
            x = npcs.get(ref, {})
            pos = [float(m.group(k)) for k in (2, 3, 4)]
            if any(s["position"] == pos for s in out[ref]):
                continue  # the same spawn in both sources: keep the first citation
            out[ref].append({"ref_id": ref, "source": f"lab/references/{src}/src/Scripts/Zone/FabledRealms.lua:{ln}",
                             "position": pos, "heading": float(m.group(5)), "model": x.get("ModelFileName"),
                             "model_id": x.get("ModelId"), "name_id": x.get("NameId")})
    return out


def indexes(sp, locale):
    by_name, by_token = defaultdict(set), defaultdict(set)
    for ref, rows in sp.items():
        nid, model = rows[0]["name_id"], (rows[0]["model"] or "").lower()
        if nid and locale.get(nid):
            by_name[norm(locale[nid])].add(ref)
        if model and not NOT_CHARACTER.match(model):
            for t in re.split(r"[_.\d]+", model):
                if len(t) >= 3:
                    by_token[t].add(ref)
    return by_name, by_token


def match(name, by_name, by_token):
    n = norm(name)
    if not n:
        return None, set()
    if by_name.get(n):
        return "name", by_name[n]
    words = n.split()
    if len(words) >= 2 and by_token.get(words[-2] + words[-1]):
        return "model", by_token[words[-2] + words[-1]]       # "queen valerian" -> queenvalerian
    toks = [w for w in words if w not in TITLES and len(w) >= 3]   # every name word must be in the model
    hits = [by_token.get(w, set()) for w in toks]
    if toks and all(hits):
        both = set.intersection(*hits)
        if both and (len(toks) >= 2 or len(both) <= 2):     # one bare token must be nearly unique
            return "model", both
    return None, set()


def entry(how, refs, sp, placed):
    cands = [s for r in sorted(refs) for s in sp[r]]
    first = cands[0]["position"]
    unique = all(sum((a - b) ** 2 for a, b in zip(c["position"], first)) <= 25 for c in cands)
    for c in cands:  # zone of the nearest NPC we already draw, as a check on the row's own zone (sub-regions differ)
        c["near_zone"] = min(placed, key=lambda p: (p[0][0] - c["position"][0]) ** 2
                             + (p[0][2] - c["position"][2]) ** 2)[1]
    return {"match": how, "unique": unique, "candidates": cands[:8], "more": max(0, len(cands) - 8)}


def main():
    locale = {r["id"]: r["text"] for r in json.load(open(LAB / "reports" / "locale-id-to-text.json", encoding="utf-8"))}
    sp = spawns()
    by_name, by_token = indexes(sp, locale)
    npc_rows = [(f, r) for f in sorted((CONTENT / "npcs").glob("*.json"))
                for r in json.load(open(f, encoding="utf-8")).get("records", [])]
    placed = [(r["position"], r.get("zone")) for _, r in npc_rows if r.get("placement") == "legacy_data" and r.get("position")]
    rows, stats = [], Counter()
    for f, r in npc_rows:
        if r.get("placement") not in ("poi_anchor", "unanchored"):
            continue
        how, refs = match(r.get("name"), by_name, by_token)
        stats[f"row {r['placement']} {'hit' if refs else 'miss'}"] += 1
        if refs:
            rows.append({"npc_id": r["npc_id"], "name": r["name"], "file": f"npcs/{f.name}", "zone": r.get("zone"),
                         "placement": r["placement"], **entry(how, refs, sp, placed)})
    # Talk targets with no NPC row at all (the objective drafts' gaps).
    con = sqlite3.connect(QL / "objectives.sqlite")
    tags = {k: t for k, t in con.execute("SELECT key, target FROM jev")}
    have = {norm(x["name"]) for x in rows}
    known = {norm(r.get("name") or "") for _, r in npc_rows}
    targets = []
    for q in json.load(open(QL / "objective-specs.json", encoding="utf-8")):
        for o in q["objectives"]:
            if o["kind"] != "talk_to_npc" or o.get("resolved"):
                continue
            i = int(re.match(r"objective (\d+)", o["from"]).group(1))
            t = tags.get(f"{q['quest']}o{i}")
            if t and norm(t) not in have and norm(t) not in known and t not in {x["name"] for x in targets}:
                how, refs = match(t, by_name, by_token)
                stats[f"no-row target {'hit' if refs else 'miss'}"] += 1
                targets.append({"name": t, "quest": q["quest"],
                                **(entry(how, refs, sp, placed) if refs else {"match": None})})
    out = QL / "wiring" / "talk-spawns.json"
    out.write_text(json.dumps({"rows": rows, "no_row_targets": targets, "stats": dict(stats)}, indent=1,
                              ensure_ascii=False), encoding="utf-8")
    print(json.dumps(dict(stats), indent=1), f"\nunique: {sum(r['unique'] for r in rows)} of {len(rows)} rows")


if __name__ == "__main__":
    assert match("Queen Valerian", {}, {"queenvalerian": {1}}) == ("model", {1})
    assert match("Farmer Chug", {}, {"chug": {1, 2, 3, 4}}) == (None, set()), "a bare common token is not a match"
    assert match("Mai Redline", {}, {"redline": {1}, "linx": {1}}) == (None, set()), "every name word must be in the model"
    main()
