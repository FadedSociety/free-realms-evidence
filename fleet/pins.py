"""pins.py: find tests that pin tunable gameplay numbers, Jev first (lead, 2026-10-24).

Bryce's rule (memory tunable-over-locked): gameplay values live in data and stay retunable; tests check sanity
bounds or read the value from the data, never pin the number. The T639 review found tests pinning combat numbers.

Run with lab/tools/wiki-env/Scripts/python.exe:
  python pins.py collect [--repo DIR]   -> out/pin-audit/pins.sqlite: every assert comparing against a number >= 2
  python pins.py jev [--budget 1]       -> Jev tags each: pins a tunable value from data? (jobs/pin-jev.md)
  python pins.py survivors              -> out/pin-audit/survivors.json, grouped per file for the Haiku job
  (lab/fleet) fleet.py pin-audit        -> Haiku confirms per file against the code and data (jobs/pin-audit.md)
  python pins.py status
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import subprocess
import sys
import threading
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "quests"))  # -I leaves the script's own folder off sys.path
from locale_index import NO_FLAG, ask_jev  # noqa: E402

FLEET = Path(__file__).parent
OUT = FLEET / "out" / "pin-audit"
RG = FLEET.parent / "tools" / "cargo" / "bin" / "rg.exe"
KINDS = ("damage", "health", "price", "reward", "xp", "timer", "rate", "count", "id", "layout", "other")
TUNABLE = {"damage", "health", "price", "reward", "xp", "timer", "rate"}
lock = threading.Lock()


def db():
    OUT.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(OUT / "pins.sqlite", check_same_thread=False)
    con.executescript("""
    CREATE TABLE IF NOT EXISTS lines(key TEXT PRIMARY KEY, file TEXT, line INTEGER, text TEXT);
    CREATE TABLE IF NOT EXISTS jev(key TEXT PRIMARY KEY, pinned TEXT, kind TEXT, data TEXT, batch INTEGER);
    CREATE TABLE IF NOT EXISTS jev_spend(batch INTEGER PRIMARY KEY, usd REAL, model TEXT, ok INTEGER);
    """)
    return con


def collect(con, repo):
    root = Path(repo) / "prototype" / "osfr-tools"
    out = subprocess.run([str(RG), "-n", "--no-heading", r"assert(_eq|_ne)?!.*\b([2-9]|[1-9][0-9]+)(\.[0-9]+)?\b",
                          "tests", "src", "-g", "*.rs"], cwd=root, capture_output=True, text=True, encoding="utf-8")
    con.execute("DELETE FROM lines")
    n = 0
    for ln in out.stdout.splitlines():
        path, num, text = ln.split(":", 2)
        path = path.replace("\\", "/")
        con.execute("INSERT OR REPLACE INTO lines VALUES(?,?,?,?)", (f"p{n}", path, int(num), text.strip()[:240]))
        n += 1
    con.commit()
    print(json.dumps({"candidates": n}))


def batches(con, size=25):
    rows = [(k, f"{f}:{l} {t}") for k, f, l, t in con.execute("SELECT key, file, line, text FROM lines ORDER BY file, line")]
    return [(i // size, rows[i:i + size]) for i in range(0, len(rows), size)]


def parse(text, lines):
    want, got = {k for k, _ in lines}, {}
    for ln in text.splitlines():
        p = [x.strip() for x in ln.strip().strip("`").split("|")]
        if len(p) >= 4 and p[0] in want:
            data = "|".join(x for x in p[3:] if not NO_FLAG.fullmatch(x))
            got[p[0]] = (p[1].lower() if p[1].lower() in ("yes", "no", "unsure") else "unsure",
                         p[2].lower() if p[2].lower() in KINDS else "other", data[:80] or None)
    return got


def jev(con, budget, threads):
    prompt = (FLEET / "jobs" / "pin-jev.md").read_text(encoding="utf-8")
    done = {b for (b,) in con.execute("SELECT batch FROM jev_spend WHERE ok=1")}
    todo = [(b, lines) for b, lines in batches(con) if b not in done]
    spent = [con.execute("SELECT coalesce(sum(usd),0) FROM jev_spend").fetchone()[0]]

    def work(b, lines):
        if spent[0] >= budget:
            return
        text, usd, model = ask_jev(lines, prompt)
        got = parse(text, lines)
        ok = len(got) >= 0.9 * len(lines)
        with lock:
            spent[0] += usd
            con.execute("INSERT OR REPLACE INTO jev_spend VALUES(?,?,?,?)", (b, usd, model, int(ok)))
            if ok:
                con.executemany("INSERT OR REPLACE INTO jev VALUES(?,?,?,?,?)",
                                [(k, *got.get(k, ("unsure", "other", None)), b) for k, _ in lines])
            con.commit()

    if todo:
        ask_jev(todo[0][1][:2], prompt)  # fail fast on a refused key
    with ThreadPoolExecutor(threads) as pool:
        for b, lines in todo:
            pool.submit(work, b, lines)
    print(json.dumps({"batches": len(todo), "jev_spent_usd": round(spent[0], 3)}))


def survivors(con):
    files = defaultdict(list)
    for f, l, t, kind, data in con.execute("SELECT l.file, l.line, l.text, j.kind, j.data FROM lines l JOIN jev j "
                                           "USING(key) WHERE j.pinned != 'no' ORDER BY l.file, l.line"):
        if kind in TUNABLE:
            files[f].append(f"{l}: {t}  [jev: {kind}{', ' + data if data else ''}]")
    items = [{"file": f, "lines": ls} for f, ls in sorted(files.items())]
    (OUT / "survivors.json").write_text(json.dumps(items, indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"files": len(items), "lines": sum(len(i["lines"]) for i in items)}))


def status(con):
    q = lambda sql: con.execute(sql).fetchall()  # noqa: E731
    print(json.dumps({"candidates": q("SELECT count(*) FROM lines")[0][0], "jev_tagged": q("SELECT count(*) FROM jev")[0][0],
                      "pinned": dict(q("SELECT pinned, count(*) FROM jev GROUP BY pinned")),
                      "kinds": dict(q("SELECT kind, count(*) FROM jev WHERE pinned != 'no' GROUP BY kind ORDER BY 2 DESC")),
                      "jev_spent_usd": q("SELECT round(coalesce(sum(usd),0),3) FROM jev_spend")[0][0],
                      "batches_failed": q("SELECT count(*) FROM jev_spend WHERE ok=0")[0][0]}, indent=1))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=["collect", "jev", "survivors", "status"])
    ap.add_argument("--repo", default=str(FLEET.parent.parent / "autopilot-int"))
    ap.add_argument("--budget", type=float, default=float("inf"))  # Jev runs uncapped (Bryce, 2026-10-24)
    ap.add_argument("--threads", type=int, default=16)
    args = ap.parse_args()
    con = db()
    {"collect": lambda: collect(con, args.repo), "jev": lambda: jev(con, args.budget, args.threads),
     "survivors": lambda: survivors(con), "status": lambda: status(con)}[args.step]()


if __name__ == "__main__":
    sys.exit(main())
