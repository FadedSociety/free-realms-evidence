"""quest_lines.py: piece together Free Realms quest lines with the Haiku fleet, critiqued in rotating rounds (lead, 2026-10-23).

Run with lab/tools/wiki-env/Scripts/python.exe after locale_index.py built references/quest-lines/index.sqlite.

  prepare   one evidence pack per quest: our 660 quest records plus the wiki quests we have no record for. Each pack
            holds the record, the client's text for it, the client text authored next to it (tagged, FLAGs shown),
            the wiki entry, article facts and the giver's dossier.
  run       round 0: fleet job quest-infer answers every quest (prompt fleet/jobs/quest-infer.md).
            rounds 1..N: fleet job quest-critic judges every unfinished answer through one lens, rotating evidence ->
            lines -> evidence ... (fleet/jobs/quest-critic.md). A failed answer is redone by a fresh quest-infer agent
            with the critique. A quest is final once its CURRENT answer has passed both lenses; any revision resets
            its passes. Between rounds a deterministic pass checks every previous/next link against the other
            quests' answers and hands each quest its conflicts.
  report    references/quest-lines/quests.json (every quest: final answer, status, rounds, last critiques) and
            quest_lines.json (lines assembled from the final answers' links).

Writes references/quest-lines/{packs.json, state.json, round/<job>.json, quests.json, quest_lines.json}.
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import subprocess
import sys
from pathlib import Path

CMMO = Path(r"C:\Users\Bryce\Documents\Projects\CartoonMMO")
LAB = CMMO / "lab"
OUT = LAB / "references" / "quest-lines"
CONTENT = CMMO / "autopilot-int" / "prototype" / "osfr-tools" / "data" / "content"
FLEET = LAB / "fleet"
LENSES = ("evidence", "lines")
norm = lambda s: re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()  # noqa: E731


def records(folder):
    out = []
    for p in sorted(folder.glob("*.json")):
        d = json.load(open(p, encoding="utf-8"))
        out += [dict(r, _file=p.name) for r in (d.get("records", []) if isinstance(d, dict) else d)]
    return out


def prepare(args):
    locale = {r["id"]: r["text"] for r in json.load(open(LAB / "reports" / "locale-id-to-text.json", encoding="utf-8"))}
    idx = sqlite3.connect(f"file:{OUT / 'index.sqlite'}?mode=ro", uri=True)
    tagged = {i: (typ, zone, hint, flag) for i, typ, zone, hint, flag in
              idx.execute("SELECT id, type, zone, hint, flag FROM strings")}
    npcs = {str(r["npc_id"]): r for r in records(CONTENT / "npcs")}
    wiki = {norm(q["name"]): q for q in json.load(open(LAB / "references" / "freerealms-wiki" / "harvest" / "lists" /
                                                       "quests.json", encoding="utf-8"))}
    art_quests = {}
    for q in json.load(open(LAB / "references" / "articles" / "quests.json", encoding="utf-8")):
        art_quests.setdefault(norm(q.get("name")), []).append(q)
    arts = sqlite3.connect(f"file:{LAB / 'references' / 'articles' / 'articles.sqlite'}?mode=ro", uri=True)

    def text(i):
        return f"locale:{i} {locale.get(i, '(no such id)')!r}" if i else None

    def cluster(i, span=30):
        rows = []
        for j in range(i - span, i + span + 1):
            if j in tagged and j in locale:
                typ, zone, hint, flag = tagged[j]
                rows.append(f"locale:{j} [{typ} | {zone or '-'} | {hint or '-'}{' | FLAG ' + flag if flag else ''}] "
                            f"{locale[j][:160]!r}")
        return rows[:45]

    def facts(title):
        q = '"' + title.replace('"', "") + '"'
        try:
            return [f"{kind}: {body[:300]} ({url})" for kind, body, url in arts.execute(
                "SELECT kind, body, url FROM search WHERE search MATCH ? ORDER BY rank LIMIT 5", (q,))]
        except sqlite3.Error:
            return []

    def dossier(npc_id):
        p = FLEET / "out" / "quest-dossier" / f"{npc_id}.md"
        return p.read_text(encoding="utf-8").split("\n", 1)[-1][:2500] if p.exists() else None

    def wiki_entry(title):
        w = wiki.get(norm(title))
        if not w:
            return None
        page = w.get("page") or {}
        return {"givers": w["givers"][:6], "appearances": w["appearances"][:6], "quest2": page.get("quest2"),
                "questprog": page.get("questprog"),
                "sections": {k: v[:900] for k, v in (page.get("sections") or {}).items()}}

    quests = records(CONTENT / "quests")
    by_giver, followers = {}, {}
    for q in quests:
        by_giver.setdefault(str(q.get("giver_npc_id")), []).append(q)
        for p in q.get("prerequisite_quest_ids") or []:
            followers.setdefault(p, []).append(q)
    by_id = {q["id"]: q for q in quests}
    name = lambda q: f"{q['id']}: {locale.get(q.get('title_string_id') or 0, '?')!r}"  # noqa: E731
    packs, seen_titles = {}, set()
    for q in quests:
        title = locale.get(q.get("title_string_id") or 0, "")
        seen_titles.add(norm(title))
        giver = npcs.get(str(q.get("giver_npc_id")), {})
        siblings = [f"{s['id']}: {locale.get(s.get('title_string_id') or 0, '?')!r}" for s in
                    by_giver.get(str(q.get("giver_npc_id")), []) if s["id"] != q["id"]][:15]
        packs[f"q{q['id']}"] = {
            "record": {k: q.get(k) for k in ("id", "title_string_id", "giver_npc_id", "prerequisite_quest_ids",
                                             "objectives", "rewards", "enabled", "job", "min_level", "live_event",
                                             "_file")},
            "record_sources": [s.get("evidence", "")[:240] for s in q.get("source", [])][:5],
            "texts": {k: text(q.get(k)) for k in ("title_string_id", "description_string_id",
                                                   "intro_text_string_id", "end_text_string_id") if q.get(k)},
            "giver": {"npc_id": str(q.get("giver_npc_id")), "name": giver.get("name"), "zone": giver.get("zone"),
                      "roles": giver.get("roles"), "quests_given_text": giver.get("quests_given_text")},
            "same_giver_quests": siblings,
            "our_records_say": {"previous": [name(by_id[p]) for p in q.get("prerequisite_quest_ids") or [] if p in by_id],
                                "next": [name(f) for f in followers.get(q["id"], [])]},
            "client_cluster": cluster(q["title_string_id"]) if q.get("title_string_id") else [],
            "wiki": wiki_entry(title), "articles_quests": art_quests.get(norm(title), [])[:3],
            "article_facts": facts(title) if title else [], "giver_dossier": dossier(q.get("giver_npc_id")),
            "title": title}
    titles = {}
    for i, typ, *_ in idx.execute("SELECT id, type FROM strings WHERE type='quest_title'"):
        titles.setdefault(norm(locale.get(i, "")), i)
    for key, w in wiki.items():
        if key in seen_titles:
            continue
        title_id = titles.get(key)
        packs["w" + re.sub(r"[^a-z0-9]+", "-", key)[:60]] = {
            "record": None, "title": w["name"], "texts": {"title_string_id": text(title_id)} if title_id else {},
            "client_cluster": cluster(title_id) if title_id else [], "wiki": wiki_entry(w["name"]),
            "articles_quests": art_quests.get(key, [])[:3], "article_facts": facts(w["name"]),
            "note": "We have no quest record for this wiki quest; work out what it is so a record can be made."}
    (OUT / "packs.json").write_text(json.dumps(packs, indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"packs": len(packs), "records": len(quests), "wiki_only": len(packs) - len(quests)}))


def answers_of(job):
    out = {}
    for path in (FLEET / "out" / job).glob("*.md"):
        body = path.read_text(encoding="utf-8").partition("\n")[2]
        body = body.split("\n", 2)[-1].strip() if body.startswith("# ") else body.strip()
        body = re.sub(r"^```(?:json)?\s*|\s*```$", "", body)
        try:
            out[path.stem] = json.loads(body)
        except json.JSONDecodeError:
            pass
    return out


def fleet(job, items, args):
    (OUT / "round").mkdir(parents=True, exist_ok=True)
    (OUT / "round" / f"{job}.json").write_text(json.dumps(items, ensure_ascii=False), encoding="utf-8")
    if items:
        subprocess.run([str(LAB / "tools" / "fleet-venv" / "Scripts" / "python.exe"), "-I", "fleet.py", job,
                        "--concurrency", str(args.concurrency), "--cap", str(args.cap)], cwd=FLEET, check=False)
    return answers_of(job)


def chain_notes(state):
    """For each quest, the previous/next links that other quests' current answers contradict or never confirm."""
    current = {qid: s["answer"] for qid, s in state.items() if s.get("answer")}
    by_title = {norm((a.get("quest") or {}).get("title")): qid for qid, a in current.items()}
    notes = {qid: [] for qid in current}
    for qid, a in current.items():
        title = (a.get("quest") or {}).get("title")
        line = a.get("line") or {}
        for rel, back in (("next", "previous"), ("previous", "next")):
            for other in line.get(rel) or []:
                oid = by_title.get(norm(other))
                if not oid:
                    notes[qid].append(f"{rel} '{other}' matches no quest answer (wrong title, or a quest we lack)")
                    continue
                theirs = [norm(t) for t in (current[oid].get("line") or {}).get(back) or []]
                if norm(title) not in theirs:
                    notes[qid].append(f"you say {rel} is '{other}', but its answer lists {back}: "
                                      f"{(current[oid].get('line') or {}).get(back) or 'nothing'}")
    return notes


_ids = {}


def cited_ids(node, path=""):
    """(field, locale id, the text the answer claims it says) for every id an answer cites: any *_locale_id field
    (paired with its sibling title/text/target/name), quest dialog ids, and locale:N inside any string."""
    if isinstance(node, dict):
        for k, v in node.items():
            p = f"{path}.{k}" if path else k
            if k.endswith("locale_id") and isinstance(v, int):
                base = k[:-len("_locale_id")] or "name"
                yield p, v, node.get(base) if isinstance(node.get(base), str) else None
            elif k in ("offer", "progress", "complete") and isinstance(v, int):
                yield p, v, None
            else:
                yield from cited_ids(v, p)
    elif isinstance(node, list):
        for n, v in enumerate(node):
            yield from cited_ids(v, f"{path}[{n}]")
    elif isinstance(node, str):
        for i in re.findall(r"locale:(\d+)", node):
            yield path, int(i), None


def id_check(answer):
    """Every locale id an answer cites, checked without a model: does it exist, is it flagged (not live), and does
    an objective's quoted text match the client's? Haiku answers kept repeating wrong ids the critics had named."""
    if not _ids:
        locale = {r["id"]: r["text"] for r in json.load(open(LAB / "reports" / "locale-id-to-text.json",
                                                             encoding="utf-8"))}
        idx = sqlite3.connect(f"file:{OUT / 'index.sqlite'}?mode=ro", uri=True)
        flags = dict(idx.execute("SELECT id, flag FROM strings WHERE flag IS NOT NULL"))
        _ids.update(locale=locale, flags=flags)
    locale, flags = _ids["locale"], _ids["flags"]
    notes = []
    for field, i, claimed in cited_ids(answer):
        if not isinstance(i, int):
            continue
        if i not in locale:
            notes.append(f"{field}: locale:{i} does not exist")
            continue
        if i in flags:
            notes.append(f"{field}: locale:{i} is FLAGGED ({flags[i]}): not live evidence")
        if claimed and norm(claimed) not in norm(locale[i]) and norm(locale[i]) not in norm(claimed):
            words = set(norm(claimed).split())
            if len(words & set(norm(locale[i]).split())) < max(1, len(words) // 2):
                notes.append(f"{field}: locale:{i} is {locale[i][:90]!r}, not {claimed[:60]!r}")
    return sorted(set(notes))[:25]


def pack_text(packs, qid, extra=None):
    return json.dumps({**packs[qid], **(extra or {})}, ensure_ascii=False, indent=1)[:24000]


def run(args):
    rounds({"packs": OUT / "packs.json", "state": OUT / "state.json", "infer": "quest-infer",
            "critic": "quest-critic", "lenses": LENSES, "notes": chain_notes,
            "notes_label": "Chain notes from other quests' answers"}, args)
    report(args)


def rounds(cfg, args):
    """Round 0 answers every record with cfg['infer']; rounds args.start..args.rounds judge unfinished answers with
    cfg['critic'] through rotating cfg['lenses'] and redo failures. A record is final once its current answer passed
    every lens. cfg['notes'](state) gives each record its conflicts with the other records' answers."""
    packs = json.load(open(cfg["packs"], encoding="utf-8"))
    state_path, lenses = Path(cfg["state"]), cfg["lenses"]
    if args.only:  # a pilot keeps its own state; its fleet answers are reused by the full run
        packs = {k: packs[k] for k in args.only.split(",")}
        state_path = state_path.with_name(state_path.stem + "-pilot.json")
    state = json.load(open(state_path, encoding="utf-8")) if state_path.exists() else {
        qid: {"answer": None, "version": 0, "passed": [], "final": False, "critiques": [], "rounds": 0}
        for qid in packs}
    save = lambda: state_path.write_text(json.dumps(state, ensure_ascii=False), encoding="utf-8")  # noqa: E731
    title = lambda q: packs[q].get("title") or q  # noqa: E731
    todo = [q for q in state if state[q]["answer"] is None]
    if todo:  # round 0
        got = fleet(cfg["infer"], [{"id": f"{q}-v1", "title": title(q), "prompt": pack_text(packs, q)}
                                   for q in todo], args)
        for q in todo:
            if f"{q}-v1" in got:
                state[q].update(answer=got[f"{q}-v1"], version=1)
        save()
    for r in range(args.start, args.rounds + 1):
        lens = lenses[(r - 1) % len(lenses)]
        live = [q for q, s in state.items() if s["answer"] and not s["final"] and lens not in s["passed"]]
        if not live:
            continue
        notes = cfg["notes"](state)
        tag = f"r{r}"
        got = fleet(cfg["critic"], [{
            "id": f"{q}-v{state[q]['version']}-{lens}-{tag}", "title": title(q),
            "prompt": f"Lens: {lens}\n\nAnswer to judge:\n{json.dumps(state[q]['answer'], ensure_ascii=False)}\n\n"
                      f"{cfg['notes_label']}:\n{json.dumps(notes.get(q, []), ensure_ascii=False)}\n\n"
                      f"Automatic id check (no model; trust it):\n"
                      f"{json.dumps(id_check(state[q]['answer']), ensure_ascii=False)}\n\n"
                      f"Evidence pack:\n{pack_text(packs, q)}"} for q in live], args)
        failed = []
        for q in live:
            c = got.get(f"{q}-v{state[q]['version']}-{lens}-{tag}")
            if not c:
                continue
            state[q]["rounds"] = r
            state[q]["critiques"] = (state[q]["critiques"] + [c])[-4:]
            if c.get("pass"):
                state[q]["passed"].append(lens)
                state[q]["final"] = set(state[q]["passed"]) >= set(lenses)
            else:
                failed.append(q)
        save()
        if failed:
            got = fleet(cfg["infer"], [{
                "id": f"{q}-v{state[q]['version'] + 1}", "title": title(q),
                "prompt": pack_text(packs, q, {"previous_answer": state[q]["answer"],
                                               "critiques": state[q]["critiques"][-2:],
                                               "cross_notes": notes.get(q, []),
                                               "id_check": id_check(state[q]["answer"])})} for q in failed], args)
            for q in failed:
                new = got.get(f"{q}-v{state[q]['version'] + 1}")
                if new:
                    state[q].update(answer=new, version=state[q]["version"] + 1, passed=[])
            save()
        print(json.dumps({"round": r, "lens": lens, "judged": len(live), "failed": len(failed),
                          "final": sum(s["final"] for s in state.values())}), flush=True)
    return state_path


def report(args):
    state = json.load(open(OUT / ("state-pilot.json" if args.only else "state.json"), encoding="utf-8"))
    rows = [{"key": q, "status": "final" if s["final"] else ("unanswered" if not s["answer"] else "unresolved"),
             "version": s["version"], "rounds": s["rounds"], "passed": s["passed"], "answer": s["answer"],
             "last_critiques": s["critiques"][-2:]} for q, s in sorted(state.items())]
    (OUT / "quests.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
    final = {r["key"]: r["answer"] for r in rows if r["status"] == "final"}
    by_title = {norm((a.get("quest") or {}).get("title")): k for k, a in final.items()}
    nxt = {k: [by_title[norm(t)] for t in (a.get("line") or {}).get("next") or [] if norm(t) in by_title]
           for k, a in final.items()}
    has_prev = {v for vs in nxt.values() for v in vs}
    lines = []
    for start in sorted(k for k in final if k not in has_prev):
        chain, k = [], start
        while k and k not in chain and len(chain) < 60:
            chain.append(k)
            k = (nxt.get(k) or [None])[0]
        if len(chain) > 1 or (final[start].get("line") or {}).get("name"):
            lines.append({"name": (final[start].get("line") or {}).get("name"),
                          "quests": [{"key": c, "title": (final[c].get("quest") or {}).get("title"),
                                      "live": final[c].get("live")} for c in chain]})
    (OUT / "quest_lines.json").write_text(json.dumps(lines, indent=1, ensure_ascii=False), encoding="utf-8")
    counts = {}
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    live = {}
    for a in final.values():
        live[a.get("live")] = live.get(a.get("live"), 0) + 1
    wireable = sum(1 for r in rows if r["status"] == "final" and any(c.get("wireable") for c in r["last_critiques"]))
    print(json.dumps({"quests": counts, "final_live": live, "final_wireable": wireable, "lines": len(lines),
                      "lines_with_3plus": sum(1 for l in lines if len(l["quests"]) >= 3)}, indent=1))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=["prepare", "run", "report"])
    ap.add_argument("--rounds", type=int, default=6, help="last round to run")
    ap.add_argument("--start", type=int, default=1, help="first round, to continue an earlier run")
    ap.add_argument("--concurrency", type=int, default=200)
    ap.add_argument("--cap", type=float, default=175.0)
    ap.add_argument("--only", help="comma-separated pack keys (pilot)")
    args = ap.parse_args()
    {"prepare": prepare, "run": run, "report": report}[args.step](args)


if __name__ == "__main__":
    sys.exit(main())
