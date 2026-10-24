"""world_lines.py: NPCs and enemies pieced together the way quest_lines.py does quests (lead, 2026-10-23).

Run with lab/tools/wiki-env/Scripts/python.exe after quest_lines.py (its quest answers are evidence here).

  python world_lines.py prepare --domain npc|enemy|dialog
  python world_lines.py run --domain npc --concurrency 120      (enemy: Bryce asked for under 100 agents)
  python world_lines.py report --domain npc|enemy|dialog

npc: one record per NPC row (data/content/npcs, pure enemies left to the enemy domain).
enemy: one record per distinct enemy name across enemies, enemies_unresolved, field_enemies, field_battles,
encounters, dungeons and enemy-role NPC rows.
Each pack: our data, the client's text for the name and the client lines tagged to it (FLAGs shown), the wiki
page, transcribed images, reviewed video frames, article facts, and the quest answers that name it. Rounds rotate
the critic lenses evidence -> world (fleet/jobs/<domain>-infer.md, <domain>-critic.md); a pass means true as far as
it goes, `wireable` says whether a builder can use it now. Writes references/quest-lines/<domain>s.json.
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))  # -I leaves the script's own folder off sys.path
from quest_lines import CONTENT, FLEET, LAB, OUT, norm, records, rounds  # noqa: E402

LENSES = ("evidence", "world")
WIKI_DB = LAB / "references" / "freerealms-wiki" / "harvest" / "harvest.sqlite"


class Evidence:
    """The sources every pack draws on, loaded once."""

    def __init__(self):
        self.locale = {r["id"]: r["text"] for r in json.load(open(LAB / "reports" / "locale-id-to-text.json",
                                                                  encoding="utf-8"))}
        self.idx = sqlite3.connect(f"file:{OUT / 'index.sqlite'}?mode=ro", uri=True)
        self.tags = {i: (t, z, h, f) for i, t, z, h, f in self.idx.execute(
            "SELECT id, type, zone, hint, flag FROM strings")}
        self.by_text = {}
        for i, t in self.locale.items():
            self.by_text.setdefault(norm(t), []).append(i)
        self.wiki = sqlite3.connect(f"file:{WIKI_DB}?mode=ro", uri=True)
        self.video = sqlite3.connect(f"file:{OUT / 'video.sqlite'}?mode=ro", uri=True)
        self.arts = sqlite3.connect(f"file:{LAB / 'references' / 'articles' / 'articles.sqlite'}?mode=ro", uri=True)
        self.quests = json.load(open(OUT / "quests.json", encoding="utf-8"))

    def line(self, i):
        t, z, h, f = self.tags.get(i, ("?", None, None, None))
        return f"locale:{i} [{t} | {z or '-'} | {h or '-'}{' | FLAG ' + f if f else ''}] {self.locale.get(i, '')[:160]!r}"

    def name_ids(self, name):
        return self.by_text.get(norm(name), [])[:8]

    def tagged_to(self, name, limit=30):
        rows = self.idx.execute("SELECT id FROM strings WHERE hint = ? COLLATE NOCASE LIMIT ?", (name, limit))
        return [self.line(i) for (i,) in rows]

    def cluster(self, i, span=12):
        return [self.line(j) for j in range(i - span, i + span + 1) if j in self.locale and j in self.tags]

    def wiki_page(self, name):
        import mwparserfromhell as mw
        for title in (name, name.rstrip("s"), name + "s"):
            row = self.wiki.execute("SELECT wikitext FROM pages WHERE ns = 0 AND title = ? COLLATE NOCASE "
                                    "AND redirect_to IS NULL", (title,)).fetchone()
            if row:
                return {"title": title, "text": mw.parse(row[0] or "").strip_code()[:1800]}
        return None

    def fts(self, con, sql, name, limit):
        try:
            return con.execute(sql, ('"' + name.replace('"', "") + '"', limit)).fetchall()
        except sqlite3.Error:
            return []

    def images(self, name, limit=3):
        return [f"image ({k}): {t[:300]}" for k, t in self.fts(self.wiki, "SELECT kind, body FROM search WHERE "
                "search MATCH ? AND kind LIKE 'image:%' ORDER BY rank LIMIT ?", name, limit)]

    def frames(self, name, limit=5):
        return [f"video:{k} ({z or '-'}): {b[:280]}" for k, z, b in self.fts(self.video, "SELECT key, zone, body "
                "FROM frames WHERE frames MATCH ? ORDER BY rank LIMIT ?", name, limit)]

    def facts(self, name, limit=4):
        return [f"{k}: {b[:260]} ({u})" for k, b, u in self.fts(self.arts, "SELECT kind, body, url FROM search "
                "WHERE search MATCH ? ORDER BY rank LIMIT ?", name, limit)]

    def quests_naming(self, name):
        """Quest answers (from quest_lines) that name this NPC/enemy as giver or objective target."""
        n, out = norm(name), []
        for r in self.quests:
            a = r.get("answer") or {}
            title = (a.get("quest") or {}).get("title")
            if n and norm((a.get("giver") or {}).get("name")) == n:
                out.append(f"giver of '{title}' ({r['status']}, zone {a.get('zone')})")
            for o in a.get("objectives") or []:
                if n and n in norm(o.get("target")):
                    out.append(f"{o.get('kind')} target in '{title}' ({r['status']}): {str(o.get('text'))[:120]}")
        return out[:20]


def npc_packs(ev):
    packs = {}
    keep = ("npc_id", "name", "name_string_id", "zone", "roles", "title_or_role", "location_evidence",
            "quests_given_text", "quest_ids_given", "services", "position", "placement", "placement_confidence")
    for r in records(CONTENT / "npcs"):
        if set(r.get("roles") or []) == {"enemy"}:
            continue
        name = r.get("name") or ""
        sid = int(r["name_string_id"]) if str(r.get("name_string_id") or "").isdigit() else None
        dossier = FLEET / "out" / "quest-dossier" / f"{r['npc_id']}.md"
        packs[f"n{r['npc_id']}"] = {
            "title": name, "record": {k: r.get(k) for k in keep},
            "record_vendor_stock": str(r.get("vendor_stock"))[:500], "record_file": r["_file"],
            "placement_candidates": (r.get("placement_candidates") or [])[:2],
            "record_sources": [s.get("evidence", "")[:200] for s in r.get("source") or []][:3],
            "client_name": ev.line(sid) if sid else None, "client_name_matches": [ev.line(i) for i in ev.name_ids(name)],
            "client_lines_tagged_to_name": ev.tagged_to(name), "client_cluster": ev.cluster(sid) if sid else [],
            "wiki": ev.wiki_page(name), "images": ev.images(name), "video": ev.frames(name),
            "article_facts": ev.facts(name), "quest_answers_naming_it": ev.quests_naming(name),
            "quest_dossier": dossier.read_text(encoding="utf-8").split("\n", 1)[-1][:1800] if dossier.exists() else None}
    return packs


def enemy_packs(ev):
    found = {}

    def walk(node, where):
        if isinstance(node, dict):
            if isinstance(node.get("name"), str) and any(k in node for k in ("name_id", "definition_id", "model_id",
                                                                               "max_health", "enemy_kind")):
                summary = {k: node.get(k) for k in ("name_id", "definition_id", "model_id", "max_health", "damage",
                                                    "boss", "zone", "region", "level_band", "enemy_kind",
                                                    "location_evidence") if node.get(k) not in (None, "", [])}
                found.setdefault(node["name"].strip(), []).append({"file": where, **summary})
            for v in node.values():
                walk(v, where)
        elif isinstance(node, list):
            for v in node:
                walk(v, where)

    files = ["enemies.json", "enemies_unresolved.json", "field_enemies.json", "field_battles.json", "encounters.json"]
    files += [str(p.relative_to(CONTENT)) for p in sorted((CONTENT / "dungeons").glob("*.json"))]
    for f in files:
        walk(json.load(open(CONTENT / f, encoding="utf-8")), f)
    for r in records(CONTENT / "npcs"):
        if "enemy" in (r.get("roles") or []):
            found.setdefault(r["name"].strip(), []).append(
                {"file": f"npcs/{r['_file']}", "npc_id": r["npc_id"], "zone": r.get("zone"),
                 "enemy_kind": r.get("enemy_kind"), "location_evidence": r.get("location_evidence")})
    packs = {}
    for name, entries in found.items():
        ids = ev.name_ids(name) or [e["name_id"] for e in entries if isinstance(e.get("name_id"), int)][:3]
        packs["e" + re.sub(r"[^a-z0-9]+", "-", norm(name))[:60]] = {
            "title": name, "our_entries": entries[:14], "entry_count": len(entries),
            "client_name_matches": [ev.line(i) for i in ids if i in ev.locale],
            "client_lines_tagged_to_name": ev.tagged_to(name), "client_cluster": ev.cluster(ids[0], 8) if ids else [],
            "wiki": ev.wiki_page(name), "images": ev.images(name), "video": ev.frames(name),
            "article_facts": ev.facts(name), "quest_answers_naming_it": ev.quests_naming(name)}
    return packs


def dialog_packs(ev):
    """One pack per answered, not-dead quest: its answer, the client lines tagged to it or written next to its title,
    and the NPC answers (npcs.json) of the giver and anyone it names."""
    npcs = {}
    for r in json.load(open(OUT / "npcs.json", encoding="utf-8")):
        a = r.get("answer") or {}
        npcs.setdefault(norm((a.get("npc") or {}).get("name")), []).append(
            {"status": r["status"], "zone": a.get("zone"), "place": a.get("place"),
             "quests_given": a.get("quests_given"), "dialog": a.get("dialog")})
    packs = {}
    for r in ev.quests:
        a = r.get("answer") or {}
        if not a or a.get("live") == "no":
            continue
        q = a.get("quest") or {}
        title, tid = q.get("title") or "", q.get("title_locale_id")
        people = {norm((a.get("giver") or {}).get("name"))} | {norm(o.get("target")) for o in a.get("objectives") or []}
        packs[r["key"]] = {
            "title": title,
            "quest_answer": {k: a.get(k) for k in ("quest", "live", "zone", "giver", "line", "objectives", "dialog",
                                                   "rewards", "open")},
            "client_lines_tagged_to_quest": ev.tagged_to(title, 40) if title else [],
            "client_cluster_around_title": ev.cluster(tid, 30) if isinstance(tid, int) else [],
            "npc_answers": {p: npcs[p] for p in people if p in npcs}}
    return packs


def answers(name):
    path = OUT / name
    if not path.exists():
        return []
    data = json.load(open(path, encoding="utf-8"))
    if isinstance(data, dict):  # a rounds() state file
        return [{"key": k, "status": "final" if s.get("final") else "open", "answer": s.get("answer")}
                for k, s in data.items()]
    return data


def vendor_stock():
    vendors = json.load(open(CONTENT / "vendors.json", encoding="utf-8"))
    stock = {}
    for v in vendors.get("vendors", vendors if isinstance(vendors, list) else []):
        for row in v.get("stock", []) if isinstance(v, dict) else []:
            if row.get("item_name"):
                stock.setdefault(norm(row["item_name"]), []).append(
                    {"vendor_npc": v.get("npc_name") or v.get("npc_id"), "zone": v.get("zone"),
                     "price": row.get("purchase_price_coins") or row.get("price")})
    return stock


def answer_mentions():
    """norm(item name) -> lines from quest rewards, enemy drops and event items that name it."""
    mentions = {}
    for domain, file, fields in (("quest", "quests.json", ("rewards",)), ("enemy", "enemies.json", ("drops",)),
                                 ("event", "event-state.json", ("items", "rewards"))):
        for r in answers(file):
            a = r.get("answer") or {}
            head = next((a[k] for k in ("quest", "enemy", "event") if isinstance(a.get(k), dict)), {})
            title = head.get("title") or head.get("name") or r.get("key")
            for f in fields:
                for x in a.get(f) or []:
                    text = json.dumps(x, ensure_ascii=False)
                    for word in re.findall(r'"(?:item|value|name)": "([^"]{3,60})"', text) or [text[:60]]:
                        mentions.setdefault(norm(word), []).append(f"{domain} '{title}' ({r.get('status')}): {text[:200]}")
    return mentions


def item_packs(ev):
    """One pack per wiki item article (catalog.json): its prices, description and categories, the client name, and
    every other answer that mentions it (quest rewards, enemy drops, event items, vendor stock)."""
    catalog = json.load(open(LAB / "references" / "freerealms-wiki" / "harvest" / "lists" / "catalog.json",
                             encoding="utf-8"))
    stock, mentions = vendor_stock(), answer_mentions()
    packs = {}
    for c in catalog:
        n = norm(c["name"])
        packs["i" + re.sub(r"[^a-z0-9]+", "-", n)[:60]] = {
            "title": c["name"], "wiki": {k: c.get(k) for k in ("url", "rev_id", "coins", "station_cash", "igd",
                                                                "categories")},
            "wiki_infobox": c.get("infobox")[:1] if c.get("infobox") else None,
            "wiki_page": ev.wiki_page(c["name"]), "client_name_matches": [ev.line(i) for i in ev.name_ids(c["name"])],
            "images": ev.images(c["name"], 2), "article_facts": ev.facts(c["name"], 3),
            "vendor_stock": stock.get(n, [])[:6], "mentioned_by_other_answers": mentions.get(n, [])[:10]}
    return packs


def citem_packs(ev):
    """One pack per client item name the wiki item pass did not answer and Jev calls live (item_catalogue.py
    survivors). A name with no evidence beyond itself (no coin price, store row, wiki, image, article, video,
    tagged client line or other answer) gets no agent: an agent could only guess. Those go to citem-nofind.json
    with Jev's tag."""
    con = sqlite3.connect(f"file:{OUT / 'catalogue.sqlite'}?mode=ro", uri=True)
    rows = {k: (json.loads(p), (live, kind, src, flag)) for k, p, live, kind, src, flag in con.execute(
        "SELECT n.key, n.payload, j.live, j.kind, j.source, j.flag FROM names n JOIN jev j USING(key)")}
    stock, mentions = vendor_stock(), answer_mentions()
    packs, nofind = {}, []
    for key in json.load(open(OUT / "citem-keys.json", encoding="utf-8")):
        d, (live, kind, src, flag) = rows[key]
        name, n = d["name"], norm(d["name"])
        ev_ = {"wiki_page": ev.wiki_page(name), "images": ev.images(name, 2), "article_facts": ev.facts(name, 3),
               "video": ev.frames(name, 3), "client_lines_tagged_to_name": ev.tagged_to(name, 12),
               "vendor_stock": stock.get(n, [])[:6], "mentioned_by_other_answers": mentions.get(n, [])[:10]}
        if not d["coin_store_prices"] and not any(ev_.values()):
            nofind.append({"key": key, "name": name, "jev": {"live": live, "kind": kind, "source": src}})
            continue
        sid = d["name_locale_id"]
        packs[key] = {"title": name, "client_definition": d, "jev_first_pass": {"live": live, "kind": kind,
                                                                               "source_guess": src, "flag": flag},
                      "client_name": ev.line(sid), "client_cluster": ev.cluster(sid, 5), **ev_}
    (OUT / "citem-nofind.json").write_text(json.dumps(nofind, indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"packs": len(packs), "no_evidence_kept_as_jev_tag": len(nofind)}))
    return packs


def schedule_packs(ev):
    """One pack per live-or-unsure event answer (event-state.json): turn it into a schedule row the revival's
    world-event scheduler (T462: seasons in client_areas.json, wall-clock slots) can load. Packs carry the event
    answer, the seasons already defined, and the calendar facts, wiki page and video frames for the event name."""
    seasons = json.load(open(CONTENT / "client_areas.json", encoding="utf-8"))["seasons"]
    seasons = [{k: s.get(k) for k in ("name", "start_month", "start_day", "end_month", "end_day", "source")}
               for s in seasons]
    packs = {}
    for key, s in json.load(open(OUT / "event-state.json", encoding="utf-8")).items():
        a = s.get("answer") or {}
        parsed = {k: (json.loads(v) if isinstance(v, str) and v[:1] in "[{" else v) for k, v in a.items()}
        if not a or parsed.get("live") == "no":
            continue
        name = (parsed.get("event") or {}).get("name") if isinstance(parsed.get("event"), dict) else str(key)
        packs["s" + key.lstrip("e")] = {
            "title": name, "event_answer": parsed, "event_answer_final": bool(s.get("final")),
            "seasons_already_defined": seasons, "calendar_facts": ev.facts(name, 6), "wiki_page": ev.wiki_page(name),
            "video": ev.frames(name, 3), "client_name_matches": [ev.line(i) for i in ev.name_ids(name)]}
    return packs


def line_packs(ev):
    """One pack per authoring cluster of still-unbound live dialog lines (no speaker from the dialog or NPC passes):
    runs of nearby locale ids, with their neighbours and the NPC and quest answers they may belong to."""
    bound = set()
    for r in answers("dialogs.json"):
        a = r.get("answer") or {}
        bound |= {a[s]["locale_id"] for s in ("offer", "progress", "complete")
                  if isinstance(a.get(s), dict) and isinstance(a[s].get("locale_id"), int)}
        bound |= {o["locale_id"] for o in a.get("other_lines") or [] if isinstance(o.get("locale_id"), int)}
    for r in answers("npcs.json"):
        bound |= {d["locale_id"] for d in (r.get("answer") or {}).get("dialog") or []
                  if isinstance(d.get("locale_id"), int)}
    todo = sorted(i for i, (t, z, h, f) in ev.tags.items()
                  if t in ("quest_dialog", "npc_dialog") and not f and i not in bound)
    clusters, cur = [], []
    for i in todo:
        if cur and (i - cur[-1] > 6 or len(cur) >= 25):
            clusters.append(cur)
            cur = []
        cur.append(i)
    clusters += [cur] if cur else []
    npc_names = {norm((r.get("answer") or {}).get("npc", {}).get("name")): r for r in answers("npcs.json")
                 if (r.get("answer") or {}).get("npc")}
    quest_titles = {norm(((r.get("answer") or {}).get("quest") or {}).get("title")): r for r in answers("quests.json")}
    packs = {}
    for c in clusters:
        hints = {norm(ev.tags[i][2]) for i in c if ev.tags[i][2]}
        packs[f"l{c[0]}"] = {
            "title": f"dialog {c[0]}-{c[-1]}", "lines_to_bind": [ev.line(i) for i in c],
            "context_before": ev.cluster(c[0] - 6, 5)[:6], "context_after": ev.cluster(c[-1] + 6, 5)[-6:],
            "npc_answers": {h: {k: (npc_names[h].get("answer") or {}).get(k) for k in ("npc", "zone", "place", "roles",
                                                                                     "quests_given")}
                            for h in hints if h in npc_names},
            "quest_answers": {h: {k: (quest_titles[h].get("answer") or {}).get(k) for k in ("quest", "giver", "zone",
                                                                                          "line")}
                              for h in hints if h in quest_titles}}
    return packs


def cross_notes(domain):
    """Conflicts between an answer and the quest answers: a quest it claims that names someone else, or a quest that
    names it but the answer leaves out."""
    quests = json.load(open(OUT / "quests.json", encoding="utf-8"))
    givers, targets = {}, {}
    for r in quests:
        a = r.get("answer") or {}
        title = norm((a.get("quest") or {}).get("title"))
        givers[title] = norm((a.get("giver") or {}).get("name"))
        for o in a.get("objectives") or []:
            if o.get("kind") == "defeat":
                targets.setdefault(norm(o.get("target")), set()).add(title)

    def notes(state):
        out = {}
        for key, s in state.items():
            a, n = s.get("answer") or {}, []
            if domain == "npc":
                me = norm((a.get("npc") or {}).get("name"))
                for t in a.get("quests_given") or []:
                    if givers.get(norm(t)) and givers[norm(t)] != me:
                        n.append(f"you list '{t}' as given by you, but its quest answer names giver "
                                 f"'{givers[norm(t)]}'")
                mine = {t for t, g in givers.items() if g and g == me}
                missing = mine - {norm(t) for t in a.get("quests_given") or []}
                if missing:
                    n.append(f"quest answers name you as giver of: {sorted(missing)[:8]}")
            else:
                me = norm((a.get("enemy") or {}).get("name"))
                claimed = {norm(t) for t in a.get("quests_targeting_it") or []}
                known = {t for k, ts in targets.items() if me and (me in k or k in me) for t in ts}
                if claimed - known:
                    n.append(f"no quest answer has a defeat objective on you for: {sorted(claimed - known)[:6]}")
            out[key] = n
        return out
    return notes


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=["prepare", "run", "report"])
    ap.add_argument("--domain", choices=["npc", "enemy", "dialog", "event", "item", "line", "citem", "schedule"],
                    required=True)
    ap.add_argument("--rounds", type=int, default=8)
    ap.add_argument("--start", type=int, default=1)
    ap.add_argument("--concurrency", type=int, default=100)
    ap.add_argument("--cap", type=float, default=170.0)
    ap.add_argument("--only", help="comma-separated pack keys (pilot)")
    args = ap.parse_args()
    d = args.domain
    packs_path, state_path = OUT / f"{d}-packs.json", OUT / f"{d}-state.json"
    if args.step == "prepare":
        packs = {"npc": npc_packs, "enemy": enemy_packs, "dialog": dialog_packs, "item": item_packs,
                 "line": line_packs, "citem": citem_packs, "schedule": schedule_packs}[d](Evidence())
        packs_path.write_text(json.dumps(packs, indent=1, ensure_ascii=False), encoding="utf-8")
        print(json.dumps({"domain": d, "packs": len(packs)}))
        return
    if args.step == "run":
        state_path = rounds({"packs": packs_path, "state": state_path, "infer": f"{d}-infer", "critic": f"{d}-critic",
                             "lenses": {"dialog": ("evidence",), "line": ("evidence",), "event": ("evidence", "calendar"),
                                        "schedule": ("evidence", "calendar")}.get(d, LENSES),
                             "notes": cross_notes(d) if d in ("npc", "enemy") else (lambda state: {}),
                             "notes_label": "Cross notes against the quest answers"}, args)
    state = json.load(open(state_path, encoding="utf-8"))
    rows = [{"key": k, "status": "final" if s["final"] else ("unanswered" if not s["answer"] else "unresolved"),
             "version": s["version"], "rounds": s["rounds"], "answer": s["answer"],
             "last_critiques": s["critiques"][-2:]} for k, s in sorted(state.items())]
    (OUT / f"{d}s.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
    counts, live = {}, {}
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
        if r["status"] == "final":
            live[r["answer"].get("live")] = live.get(r["answer"].get("live"), 0) + 1
    print(json.dumps({"domain": d, "records": counts, "final_live": live,
                      "final_wireable": sum(1 for r in rows if r["status"] == "final" and
                                            any(c.get("wireable") for c in r["last_critiques"]))}, indent=1))


if __name__ == "__main__":
    sys.exit(main())
