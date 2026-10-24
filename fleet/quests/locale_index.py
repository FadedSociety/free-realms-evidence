"""locale_index.py: a tagged, searchable index of every client locale string for quest-line work (lead, 2026-10-23).

Run with lab/tools/wiki-env/Scripts/python.exe. The tagging prompt is fleet/jobs/locale-tag.md: each request gets one
run of ~40 consecutive strings (consecutive ids are authored together) and answers id|type|zone|hint|flag.

  1. Haiku tags everything:  (lab/fleet) fleet.py locale-tag           -> fleet/out/locale-tag/
  2. python locale_index.py ingest     -> strings table, deterministic flags added, FTS rebuilt
  3. Jev (TypeSafe router via OpenRouter) tags everything a second time, independently, once Bryce refreshes the
     OpenRouter key (`codex-router setup`):  python locale_index.py jev [--budget 12]   -> jev table
     Lines where Jev and Haiku disagree on type, or where either flags them, are flagged for review.
  4. python locale_index.py flags      -> references/quest-lines/flags.json + flags.tsv (the human review list)
  python locale_index.py status

Writes lab/references/quest-lines/index.sqlite: strings(id, text, type, zone, hint, flag, batch), jev(...),
FTS5 strings_fts(id, text, type, zone, hint, flag).
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

LAB = Path(r"C:\Users\Bryce\Documents\Projects\CartoonMMO\lab")
OUT = LAB / "references" / "quest-lines"
FLEET_OUT = LAB / "fleet" / "out" / "locale-tag"
PROMPT_FILE = LAB / "fleet" / "jobs" / "locale-tag.md"
JEV_MODEL = "openrouter/typesafe/jev-router"
TYPES = ("quest_title", "quest_objective", "quest_dialog", "quest_reward", "npc_name", "npc_dialog", "item",
         "place", "ability", "ui", "other")
# Markers in the text itself: these lines are never trusted as live quest content without a human look.
# Upper-case markers only: ordinary dialog says "cut the grass" and "test your skills".
MARKERS = [(re.compile(r"\bNOT LIVE\b|\bNOT_LIVE\b|\bUNUSED\b|\bCUT\b|\(old\)|\bOLD -"), "not_live: marker in text"),
           (re.compile(r"(?i:placeholder|lorem ipsum)|\bTBD\b|\bTODO\b|\bXXX\b|\bTEST\b|^Sample (Bundle|Name|Desc)"),
            "placeholder: marker in text"),
           (re.compile(r"\bDO NOT USE\b|\bFIXME\b|(?i:\bdebug\b)"), "dev_note: marker in text")]
NO_FLAG = re.compile(r"[-|\s]*|flag|none", re.I)  # model output that means "no flag"
lock = threading.Lock()


def db():
    OUT.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(OUT / "index.sqlite", check_same_thread=False)
    con.executescript("""
    CREATE TABLE IF NOT EXISTS strings(id INTEGER PRIMARY KEY, text TEXT, type TEXT, zone TEXT, hint TEXT, flag TEXT,
        batch INTEGER);
    CREATE TABLE IF NOT EXISTS jev(id INTEGER PRIMARY KEY, type TEXT, zone TEXT, hint TEXT, flag TEXT, batch INTEGER);
    CREATE TABLE IF NOT EXISTS jev_spend(batch INTEGER PRIMARY KEY, usd REAL, model TEXT, ok INTEGER);
    """)
    return con


def batches(size=40, max_chars=3000):
    """[(batch_no, [(id, text), ...]), ...] over every non-empty locale string in id order."""
    rows = sorted((r["id"], r["text"]) for r in json.load(open(LAB / "reports" / "locale-id-to-text.json",
                                                              encoding="utf-8")) if r["text"].strip())
    out, cur, n = [], [], 0
    for i, t in rows:
        t = re.sub(r"\s+", " ", t)[:300]
        if cur and (len(cur) >= size or n + len(t) > max_chars):
            out.append(cur)
            cur, n = [], 0
        cur.append((i, t))
        n += len(t) + 10
    return list(enumerate(out + ([cur] if cur else [])))


def parse(text, lines):
    want = {i for i, _ in lines}
    got = {}
    for ln in text.splitlines():
        parts = [p.strip() for p in ln.strip().strip("`").split("|")]
        if len(parts) >= 5 and parts[0].isdigit() and int(parts[0]) in want:
            val = lambda v, n: None if NO_FLAG.fullmatch(v) else v[:n]  # noqa: E731
            flag = "|".join(p for p in parts[4:] if not NO_FLAG.fullmatch(p))
            got[int(parts[0])] = (parts[1] if parts[1] in TYPES else "other", val(parts[2], 40), val(parts[3], 120),
                                  val(flag, 120))
    return got


def marker_flag(text):
    return next((why for rx, why in MARKERS if rx.search(text)), None)


def rebuild_fts(con):
    con.executescript("DROP TABLE IF EXISTS strings_fts; CREATE VIRTUAL TABLE strings_fts USING fts5(id UNINDEXED, "
                      "text, type, zone, hint, flag); INSERT INTO strings_fts SELECT id, text, type, zone, hint, "
                      "coalesce(flag, '') FROM strings;")


def ingest(con):
    all_batches = dict(batches())
    n = 0
    for path in FLEET_OUT.glob("batch-*.md"):
        k = int(path.stem.split("-")[1])
        body = path.read_text(encoding="utf-8")
        got = parse(body, all_batches[k])
        if len(got) < 0.9 * len(all_batches[k]):
            continue
        for i, t in all_batches[k]:
            typ, zone, hint, flag = got.get(i, ("other", None, None, None))
            con.execute("INSERT OR REPLACE INTO strings VALUES(?,?,?,?,?,?,?)",
                        (i, t, typ, zone, hint, flag or marker_flag(t), k))
        n += 1
    con.commit()
    rebuild_fts(con)
    print(json.dumps({"batches_ingested": n, "of": len(all_batches)}))


def ask_jev(lines, prompt):
    import requests
    sec = Path.home().joinpath(".codex/codex-router/caller-secret").read_text().strip()
    url = f"http://127.0.0.1:4202/_codex-router/{sec}/v1/responses"
    body = prompt + "\n\n" + "\n".join(f"{i}: {t}" for i, t in lines)
    for attempt in range(4):
        try:
            r = requests.post(url, json={"model": JEV_MODEL, "input": [{"role": "user", "content": body}],
                                         "stream": False}, timeout=300)
            if r.status_code == 200:
                j = r.json()
                text = " ".join(c.get("text", "") for o in j.get("output", []) if o.get("type") == "message"
                                for c in o.get("content", []))
                return text, (j.get("usage") or {}).get("cost") or 0, j.get("model")
            if r.status_code in (401, 402):
                raise SystemExit(f"Jev refused: {r.status_code} {r.text[:200]} (refresh with codex-router setup)")
        except Exception as e:  # network trouble: retry
            if isinstance(e, SystemExit):
                raise
        time.sleep(5 * (attempt + 1))
    return "", 0, None


def jev(con, budget, threads):
    prompt = PROMPT_FILE.read_text(encoding="utf-8").rsplit("When you are finished", 1)[0].strip()
    done = {b for (b,) in con.execute("SELECT batch FROM jev_spend WHERE ok=1")}
    todo = [(k, b) for k, b in batches() if k not in done]
    spent = [con.execute("SELECT coalesce(sum(usd),0) FROM jev_spend").fetchone()[0]]

    def work(k, lines):
        if spent[0] >= budget:
            return
        text, usd, model = ask_jev(lines, prompt)
        got = parse(text, lines)
        ok = len(got) >= 0.9 * len(lines)
        with lock:
            spent[0] += usd
            con.execute("INSERT OR REPLACE INTO jev_spend VALUES(?,?,?,?)", (k, usd, model, int(ok)))
            if ok:
                con.executemany("INSERT OR REPLACE INTO jev VALUES(?,?,?,?,?,?)",
                                [(i, *got.get(i, ("other", None, None, None)), k) for i, _ in lines])
            con.commit()

    ask_jev(todo[0][1][:2], prompt)  # fail fast on a refused key
    with ThreadPoolExecutor(threads) as pool:
        for k, lines in todo:
            pool.submit(work, k, lines)
    print(json.dumps({"jev_spent_usd": round(spent[0], 3)}))


REASONS = re.compile(r"(not_live|placeholder|dev_note|joke|duplicate|fragment)\b")  # Jev's flag counts only with a code


def write_tsv(path, rows, cols):
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("\t".join(cols) + "\n")
        for r in rows:
            f.write("\t".join(str(r[k] or "").replace("\t", " ") for k in cols) + "\n")


def flags(con):
    """Two human review lists. flags: every line Haiku, Jev or a text marker says is probably not live content
    ("ooga booga is probably not a quest"), quest-typed lines first. disagreements: quest-typed lines the two models
    tag differently (a weaker signal: often genuinely ambiguous lines)."""
    rows = con.execute("SELECT s.id, s.text, s.type, j.type, s.zone, s.hint, s.flag, j.flag FROM strings s "
                       "LEFT JOIN jev j USING(id) ORDER BY s.id").fetchall()
    flagged, disagree = [], []
    for i, t, st, jt, z, h, sf, jf in rows:
        jf = jf if jf and REASONS.match(jf) else None
        row = {"id": i, "text": t, "type": st, "jev_type": jt, "zone": z, "hint": h, "flag": sf or jf,
               "by": "+".join(n for n, v in (("haiku", sf), ("jev", jf)) if v)}
        if sf or jf:
            flagged.append(row)
        elif jt and jt != st and (st.startswith("quest") or jt.startswith("quest")):
            disagree.append(row)
    flagged.sort(key=lambda r: (not r["type"].startswith("quest"), r["id"]))
    (OUT / "flags.json").write_text(json.dumps(flagged, indent=1, ensure_ascii=False), encoding="utf-8")
    write_tsv(OUT / "flags.tsv", flagged, ("id", "flag", "by", "type", "jev_type", "zone", "hint", "text"))
    write_tsv(OUT / "disagreements.tsv", disagree, ("id", "type", "jev_type", "zone", "hint", "text"))
    kinds = {}
    for r in flagged:
        k = (REASONS.match(r["flag"]) or re.match(r"\S+", r["flag"])).group(0)
        kinds[k] = kinds.get(k, 0) + 1
    print(json.dumps({"flagged": len(flagged), "quest_typed_flagged": sum(r["type"].startswith("quest") for r in flagged),
                      "flagged_by_both": sum(r["by"] == "haiku+jev" for r in flagged),
                      "by_reason": dict(sorted(kinds.items(), key=lambda kv: -kv[1])[:8]),
                      "quest_type_disagreements": len(disagree)}))


def status(con):
    print(json.dumps({"tagged": con.execute("SELECT count(*) FROM strings").fetchone()[0],
                      "types": dict(con.execute("SELECT type, count(*) FROM strings GROUP BY type").fetchall()),
                      "flagged": con.execute("SELECT count(*) FROM strings WHERE flag IS NOT NULL").fetchone()[0],
                      "jev_tagged": con.execute("SELECT count(*) FROM jev").fetchone()[0],
                      "jev_spent_usd": con.execute("SELECT round(coalesce(sum(usd),0),3) FROM jev_spend").fetchone()[0]},
                     indent=1))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=["ingest", "jev", "flags", "status"])
    # Bryce, 2026-10-24: Jev needs no cap; --budget stays for a deliberate limit.
    ap.add_argument("--budget", type=float, default=float("inf"), help="Jev: stop spending at this many USD")
    ap.add_argument("--threads", type=int, default=16)
    args = ap.parse_args()
    con = db()
    {"ingest": lambda: ingest(con), "jev": lambda: jev(con, args.budget, args.threads),
     "flags": lambda: flags(con), "status": lambda: status(con)}[args.step]()


if __name__ == "__main__":
    sys.exit(main())
