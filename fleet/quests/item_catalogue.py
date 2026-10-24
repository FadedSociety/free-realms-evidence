"""item_catalogue.py: every client item name the item pass has not answered, tagged by Jev first (lead, 2026-10-24).

Run with lab/tools/wiki-env/Scripts/python.exe. Bryce, 2026-10-24: "go for everything jev first". The client catalogue
(58,835 definitions) collapses to ~12,600 names; items.json answers ~2,200 of them (wiki articles). For the rest:

  python item_catalogue.py names            -> catalogue.sqlite names: one row per unanswered client item name
  python item_catalogue.py jev [--budget 6] -> Jev tags each name live / kind / likely source / flag (jobs/item-jev.md)
  python item_catalogue.py status
  python item_catalogue.py survivors        -> references/quest-lines/citem-keys.json: names Jev calls live (or unsure)
                                               and does not flag; world_lines.py --domain citem builds their packs.
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import struct
import sys
import threading
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))  # -I leaves the script's own folder off sys.path
from locale_index import NO_FLAG, ask_jev  # noqa: E402
from quest_lines import LAB, OUT, norm  # noqa: E402

CATALOGUE = LAB / "reports" / "native-20261024T0455Z-new" / "content" / "item-catalogue.json"
STORES = LAB.parent / "native" / "prototype" / "osfr-tools" / "data" / "content" / "stores.json"
PROMPT = LAB / "fleet" / "jobs" / "item-jev.md"
LIVE = ("yes", "no", "unsure")
SOURCES = ("vendor", "marketplace", "coin_shop", "quest_reward", "drop", "event", "prize_wheel", "crafting",
           "collection", "membership", "promotion", "npc_only", "unknown")
HARD_FLAGS = re.compile(r"(not_live|placeholder|dev_note|npc_only|internal|duplicate)\b")
lock = threading.Lock()


def db():
    con = sqlite3.connect(OUT / "catalogue.sqlite", check_same_thread=False)
    con.executescript("""
    CREATE TABLE IF NOT EXISTS names(key TEXT PRIMARY KEY, name TEXT, line TEXT, payload TEXT);
    CREATE TABLE IF NOT EXISTS jev(key TEXT PRIMARY KEY, live TEXT, kind TEXT, source TEXT, flag TEXT, batch INTEGER);
    CREATE TABLE IF NOT EXISTS jev_spend(batch INTEGER PRIMARY KEY, usd REAL, model TEXT, ok INTEGER);
    """)
    return con


def names(con):
    locale = {r["id"]: r["text"] for r in json.load(open(LAB / "reports" / "locale-id-to-text.json", encoding="utf-8"))}
    answered = {norm(((r.get("answer") or {}).get("item") or {}).get("name")) for r in
                json.load(open(OUT / "items.json", encoding="utf-8"))}
    price = {}
    for row in json.load(open(STORES, encoding="utf-8"))["items"]:
        if row.get("purchase_price_coins"):
            price[row["item_id"]] = row["purchase_price_coins"]
    groups = defaultdict(list)
    for d in json.load(open(CATALOGUE, encoding="utf-8"))["definitions"]:
        name_id, desc_id = struct.unpack("<ii", bytes.fromhex(d["serialized_hex"][8:24]))
        name = re.sub(r"\s+", " ", locale.get(name_id, "")).strip()
        if name and "NOT FOUND" not in name and norm(name) not in answered:
            groups[norm(name)].append((d, name, name_id, locale.get(desc_id, "")))
    con.execute("DELETE FROM names")
    for n, rows in groups.items():
        d0, name, name_id, desc = rows[0]
        ids = [d["id"] for d, *_ in rows]
        coins = sorted({price[i] for i in ids if i in price})
        payload = {"name": name, "name_locale_id": name_id, "description": re.sub(r"\s+", " ", desc)[:240],
                   "definition_ids": ids[:12], "definitions": len(ids),
                   "slots": sorted({d["slot"] for d, *_ in rows}), "class_ids": sorted({d["class_id"] for d, *_ in rows}),
                   "models": sorted({d["model"] for d, *_ in rows if d["model"]})[:3], "coin_store_prices": coins[:4]}
        line = (f"{name} | {payload['description'][:110] or '-'} | slot {payload['slots'][:3]} class "
                f"{payload['class_ids'][:3]} | {payload['models'][0][:50] if payload['models'] else '-'} | "
                f"{len(ids)} defs | coins {coins[:2] or '-'}")
        con.execute("INSERT INTO names VALUES(?,?,?,?)", ("c" + re.sub(r"[^a-z0-9]+", "-", n)[:60] + f"-{name_id}",
                                                         name, line, json.dumps(payload, ensure_ascii=False)))
    con.commit()
    print(json.dumps({"unanswered_names": len(groups), "answered_skipped": len(answered)}))


def batches(con, size=30):
    rows = con.execute("SELECT key, line FROM names ORDER BY key").fetchall()
    out = [(k // size, rows[k:k + size]) for k in range(0, len(rows), size)]
    # Batches Jev keeps failing are retried as batches of 6 (ids from 100000) once every first try is in.
    if con.execute("SELECT count(*) FROM jev_spend").fetchone()[0] >= len(out):
        left = con.execute("SELECT key, line FROM names WHERE key NOT IN (SELECT key FROM jev) ORDER BY key").fetchall()
        out += [(100000 + k // 6, left[k:k + 6]) for k in range(0, len(left), 6)]
    return out


def parse(text, lines):
    want, got = {k for k, _ in lines}, {}
    for ln in text.splitlines():
        p = [x.strip() for x in ln.strip().strip("`").split("|")]
        if len(p) >= 5 and p[0] in want:
            flag = "|".join(x for x in p[4:] if not NO_FLAG.fullmatch(x))
            got[p[0]] = (p[1].lower() if p[1].lower() in LIVE else "unsure", p[2][:30],
                         p[3].lower() if p[3].lower() in SOURCES else "unknown", flag[:120] or None)
    return got


def jev(con, budget, threads):
    prompt = PROMPT.read_text(encoding="utf-8")
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
                con.executemany("INSERT OR REPLACE INTO jev VALUES(?,?,?,?,?,?)",
                                [(k, *got.get(k, ("unsure", "other", "unknown", None)), b) for k, _ in lines])
            con.commit()

    if todo:
        ask_jev(todo[0][1][:2], prompt)  # fail fast on a refused key
    with ThreadPoolExecutor(threads) as pool:
        for b, lines in todo:
            pool.submit(work, b, lines)
    print(json.dumps({"batches": len(todo), "jev_spent_usd": round(spent[0], 3)}))


def survivors(con):
    rows = con.execute("SELECT n.key, j.live, j.source, j.flag FROM names n JOIN jev j USING(key)").fetchall()
    keep = [k for k, live, src, flag in rows if live != "no" and src != "npc_only" and not (flag and HARD_FLAGS.search(flag))]
    (OUT / "citem-keys.json").write_text(json.dumps(keep), encoding="utf-8")
    print(json.dumps({"tagged": len(rows), "survivors": len(keep)}))


def status(con):
    q = lambda sql: con.execute(sql).fetchall()  # noqa: E731
    print(json.dumps({"names": q("SELECT count(*) FROM names")[0][0], "jev_tagged": q("SELECT count(*) FROM jev")[0][0],
                      "live": dict(q("SELECT live, count(*) FROM jev GROUP BY live")),
                      "source": dict(q("SELECT source, count(*) FROM jev GROUP BY source ORDER BY 2 DESC")),
                      "flagged": q("SELECT count(*) FROM jev WHERE flag IS NOT NULL")[0][0],
                      "jev_spent_usd": q("SELECT round(coalesce(sum(usd),0),3) FROM jev_spend")[0][0],
                      "batches_failed": q("SELECT count(*) FROM jev_spend WHERE ok=0")[0][0]}, indent=1))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=["names", "jev", "survivors", "status"])
    # Bryce, 2026-10-24: Jev needs no cap ("let it run all the way through"); --budget stays for a deliberate limit.
    ap.add_argument("--budget", type=float, default=float("inf"), help="Jev: stop spending at this many USD")
    ap.add_argument("--threads", type=int, default=16)
    args = ap.parse_args()
    con = db()
    {"names": lambda: names(con), "jev": lambda: jev(con, args.budget, args.threads),
     "survivors": lambda: survivors(con), "status": lambda: status(con)}[args.step]()


if __name__ == "__main__":
    sys.exit(main())
