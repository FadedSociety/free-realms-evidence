"""fleet.py: run one job's items through Claude Haiku 5.5 agents that can only read (lead, 2026-10-22).

usage: python -I fleet.py JOB [--limit N] [--only ID,ID] [--concurrency C] [--cap USD] [--redo]

Each item gets its own agent. The job prompt (jobs/JOB.md) is the system prompt, identical for every agent of the
job, so with the tool list it is a cached prefix they share; the item is the first user message. Tools read an
allow-list of roots, the client function database (read-only SQL) and the client locale text; nothing can write
except `submit`, whose result goes to out/JOB/ID.md and out/JOB/index.jsonl.

Spend: each response is priced from its usage (Haiku 5.5: $0.10 in, $0.125 cache write, $0.01 cache read, $0.50
out per MTok; 5x when the prompt passes 100k tokens) and every item is booked in claude-api/spend.tsv, so the
helm's budget sees it. No agent starts once fleet spend plus the caps of running agents reaches --cap. An agent
past its own cap, near the 100k price step or out of turns is told to submit.
The API key comes from claude-api/key-helper.ps1 (DPAPI) and is never printed or logged.
"""
import argparse
import asyncio
import base64
import json
import re
import sqlite3
import subprocess
import sys
import threading
import time
from pathlib import Path

import anthropic

sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I drops the script's folder from sys.path
import jobs  # noqa: E402

CMMO = Path(r"C:\Users\Bryce\Documents\Projects\CartoonMMO")
LAB = CMMO / "lab"
FLEET = LAB / "fleet"
CAPI = LAB / "autopilot" / "claude-api"
SPEND = CAPI / "spend.tsv"
RG = LAB / "tools" / "cargo" / "bin" / "rg.exe"
DB = LAB / "native-map" / "run" / "map.sqlite"
LOCALE = LAB / "reports" / "locale-id-to-text.json"
MODEL = "claude-haiku-5-5"
ROOTS = {  # alias -> directory the agents may read
    "repo": CMMO / "fleet-ro",
    "refs": LAB / "references",
    "client": LAB / "working" / "OSFR.Client" / "OSFR Client",
    "ui": LAB / "decompiled" / "client-ui",
    "briefs": LAB / "autopilot" / "queue",
}
PRICE = {"in": 0.10, "write": 0.125, "read": 0.01, "out": 0.50}  # USD per MTok, prompt <= 100k tokens
PROMPT_GUARD = 90_000   # tokens: ask for submit before the 100k price step
MAX_TURNS = 40
OUT_CHARS = 12_000      # cap on any one tool result

TOOLS = [
    {"name": "search", "description": "ripgrep a regex under one root. Returns up to 60 matching lines as path:line:text. "
     "Roots: repo (our server code and notes at the current tip), refs (community servers Sanctuary, "
     "Lxzxrus-Free-Realms-Server, FreeRealms-Legacy, TCG-Files, cached wiki pages), client (the shipped client's files and "
     "Resources tables), ui (the client's decompiled Lua UI, ScriptsBase.lua), briefs (queued build briefs).",
     "input_schema": {"type": "object", "properties": {
         "root": {"type": "string", "enum": list(ROOTS)},
         "pattern": {"type": "string", "description": "Rust-regex pattern"},
         "path": {"type": "string", "description": "optional sub-path inside the root, e.g. prototype/osfr-tools/src"},
         "glob": {"type": "string", "description": "optional file glob, e.g. *.rs"},
         "ignore_case": {"type": "boolean"}},
         "required": ["root", "pattern"], "additionalProperties": False}},
    {"name": "read", "description": "Read lines of one file under a root, numbered. At most 300 lines per call.",
     "input_schema": {"type": "object", "properties": {
         "root": {"type": "string", "enum": list(ROOTS)},
         "path": {"type": "string"},
         "start": {"type": "integer", "minimum": 1},
         "end": {"type": "integer", "minimum": 1}},
         "required": ["root", "path"], "additionalProperties": False}},
    {"name": "list", "description": "List one directory under a root (at most 300 entries; directories end with /).",
     "input_schema": {"type": "object", "properties": {
         "root": {"type": "string", "enum": list(ROOTS)},
         "path": {"type": "string"}},
         "required": ["root"], "additionalProperties": False}},
    {"name": "client_sql", "description": "Read-only SQL (SELECT only) on the decompiled client database. Tables: "
     "fn(addr TEXT hex like '00aa0920', name, namespace, signature, bytes, thunk_of, callees, callers, strings, vtables, "
     "data, decompiled (0/1 flag), c TEXT (the pseudocode), rule_kind); label(addr, shard, record JSON with the mapped "
     "meaning: name, subsystem, does, ...; status, pass); command(class_id, class, family, version, vtable, read, write, "
     "handler, routing, shard, read_label_conf). At most 40 rows; long cells are cut at 4000 characters. Example: "
     "SELECT f.addr, substr(l.record,1,600), substr(f.c,1,3500) FROM fn f LEFT JOIN label l USING(addr) WHERE "
     "f.addr='00aa0920'.",
     "input_schema": {"type": "object", "properties": {"query": {"type": "string"}},
                      "required": ["query"], "additionalProperties": False}},
    {"name": "locale", "description": "Look up the client's English text table (every string the game shipped). "
     "Give a number for one string id, or a regex to find strings (first 30 hits as id: text).",
     "input_schema": {"type": "object", "properties": {"query": {"type": "string"}},
                      "required": ["query"], "additionalProperties": False}},
    {"name": "lookup", "description": "Full-text search (SQLite FTS5: words, \"exact phrase\", OR, NEAR) over four "
     "indexes. client: every client text line, tagged type (quest_title, quest_objective, quest_dialog, npc_name, ...), "
     "zone, hint (the quest or NPC it belongs to) and FLAG (not_live, placeholder, joke, ...: not trusted as live "
     "content); refs look like locale:12345. wiki: the Free Realms wiki's pages and every image's transcribed text. "
     "articles: sourced facts from the official site, Ten Ton Hammer and the fan forum. video: reviewed frames of "
     "gameplay videos (NPCs, dialog, zone, landmarks seen on screen; refs look like video:<id>/<frame>). Up to `limit` "
     "hits per source.",
     "input_schema": {"type": "object", "properties": {
         "query": {"type": "string"},
         "sources": {"type": "array", "items": {"type": "string", "enum": ["client", "wiki", "articles", "video"]}},
         "limit": {"type": "integer", "minimum": 1, "maximum": 20}},
         "required": ["query"], "additionalProperties": False}},
    {"name": "submit", "description": "Finish: hand in your result. Call it exactly once, as your last action.",
     "input_schema": {"type": "object", "properties": {
         "status": {"type": "string", "enum": ["done", "nothing_found", "blocked"]},
         "result": {"type": "string", "description": "the job's result, in Markdown"}},
         "required": ["status", "result"], "additionalProperties": False}},
]


def resolve(root, path=""):
    if root not in ROOTS:
        raise ValueError(f"unknown root {root!r}; use one of {', '.join(ROOTS)}")
    base = ROOTS[root].resolve()
    target = (base / (path or "")).resolve()
    if target != base and base not in target.parents:
        raise ValueError("path leaves the root")
    return base, target


def cut(text):
    return text if len(text) <= OUT_CHARS else text[:OUT_CHARS] + f"\n[... cut at {OUT_CHARS} characters]"


def tool_search(root, pattern, path="", glob="", ignore_case=False):
    base, target = resolve(root, path)
    cmd = [str(RG), "-n", "--no-heading", "-m", "20", "--max-columns", "300", "--max-columns-preview"]
    if ignore_case:
        cmd.append("-i")
    if glob:
        cmd += ["-g", glob]
    cmd += ["-e", pattern, str(target)]
    run = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    lines = [ln.replace(str(base) + "\\", "").replace("\\", "/") for ln in run.stdout.splitlines()[:60]]
    if run.returncode == 2 and not lines:
        return "search error: " + run.stderr.strip()[:500]
    return cut("\n".join(lines)) if lines else "no matches"


def tool_read(root, path, start=1, end=None):
    _, target = resolve(root, path)
    if not target.is_file():
        return "not a file"
    lines = target.read_text(encoding="utf-8", errors="replace").splitlines()
    end = min(end or start + 199, start + 299, len(lines))
    body = "\n".join(f"{n}: {lines[n - 1]}" for n in range(start, end + 1))
    return cut(f"{path} lines {start}-{end} of {len(lines)}\n{body}")


def tool_list(root, path=""):
    _, target = resolve(root, path)
    if not target.is_dir():
        return "not a directory"
    names = sorted(p.name + ("/" if p.is_dir() else "") for p in target.iterdir())
    return "\n".join(names[:300]) + (f"\n[{len(names) - 300} more]" if len(names) > 300 else "")


def tool_client_sql(query):
    if not re.match(r"\s*(select|with)\b", query, re.I) or ";" in query.strip().rstrip(";"):
        return "only one SELECT statement is allowed"
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    deadline = time.monotonic() + 20
    con.set_progress_handler(lambda: 1 if time.monotonic() > deadline else 0, 100_000)
    try:
        cur = con.execute(query)
        cols = [d[0] for d in cur.description or []]
        rows = cur.fetchmany(40)
    except sqlite3.Error as e:
        return f"sql error: {e}"
    finally:
        con.close()
    out = [" | ".join(cols)]
    for row in rows:
        out.append(" | ".join(str(v)[:4000] for v in row))
    return cut("\n".join(out)) if rows else "no rows"


_locale, _locale_lock = None, threading.Lock()


def tool_locale(query):
    global _locale
    with _locale_lock:
        if _locale is None:
            _locale = {row["id"]: row["text"] for row in json.load(open(LOCALE, encoding="utf-8"))}
    if query.strip().isdigit():
        return f"{query.strip()}: {_locale.get(int(query.strip()), '(no such id)')}"
    try:
        rx = re.compile(query, re.I)
    except re.error as e:
        return f"regex error: {e}"
    hits = [f"{i}: {t[:300]}" for i, t in _locale.items() if rx.search(t or "")][:30]
    return "\n".join(hits) if hits else "no matches"


LOOKUP_DBS = {  # source -> (sqlite file under lab/references, FTS query returning (ref, label, text))
    "client": ("quest-lines/index.sqlite", "SELECT 'locale:' || id, type || ' ' || coalesce(zone,'-') || ' ' || "
               "coalesce(hint,'-') || coalesce(' FLAG ' || nullif(flag,''),''), text FROM strings_fts "
               "WHERE strings_fts MATCH ? ORDER BY rank LIMIT ?"),
    "wiki": ("freerealms-wiki/harvest/harvest.sqlite", "SELECT kind, title, snippet(search, 2, '[', ']', '..', 40) "
             "FROM search WHERE search MATCH ? ORDER BY rank LIMIT ?"),
    "articles": ("articles/articles.sqlite", "SELECT kind, coalesce(url,''), snippet(search, 2, '[', ']', '..', 40) "
                 "FROM search WHERE search MATCH ? ORDER BY rank LIMIT ?"),
    "video": ("quest-lines/video.sqlite", "SELECT 'video:' || key, screen || ' ' || coalesce(zone,'-'), "
              "snippet(frames, 3, '[', ']', '..', 40) FROM frames WHERE frames MATCH ? ORDER BY rank LIMIT ?"),
}


def tool_lookup(query, sources=None, limit=8):
    """Full-text search (SQLite FTS5) over the tagged client text, the wiki (pages + image text) and the archived
    articles/forum facts."""
    out = []
    for source in sources or list(LOOKUP_DBS):
        if source not in LOOKUP_DBS:
            continue
        path, sql = LOOKUP_DBS[source]
        try:
            con = sqlite3.connect(f"file:{CMMO / 'lab' / 'references' / path}?mode=ro", uri=True)
            rows = con.execute(sql, (query, max(1, min(int(limit), 20)))).fetchall()
        except sqlite3.Error as e:
            out.append(f"[{source}] query error: {e} (FTS5 syntax: words, \"exact phrase\", OR, NEAR)")
            continue
        out += [f"[{source}] {ref} | {label} | {text[:400]}" for ref, label, text in rows]
    return "\n".join(out) or "no matches"


RUNNERS = {"search": tool_search, "read": tool_read, "list": tool_list, "client_sql": tool_client_sql,
           "locale": tool_locale, "lookup": tool_lookup}


def price(usage):
    prompt = usage.input_tokens + (usage.cache_read_input_tokens or 0) + (usage.cache_creation_input_tokens or 0)
    scale = 5 if prompt > 100_000 else 1
    usd = scale * (usage.input_tokens * PRICE["in"] + (usage.cache_creation_input_tokens or 0) * PRICE["write"]
                   + (usage.cache_read_input_tokens or 0) * PRICE["read"] + usage.output_tokens * PRICE["out"]) / 1e6
    return usd, prompt


def api_key():
    run = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File",
                          str(CAPI / "key-helper.ps1")], capture_output=True, text=True, timeout=60)
    key = run.stdout.strip()
    if not key.startswith("sk-ant-"):
        sys.exit("no API key from key-helper.ps1 (claude-api/set-key.ps1)")
    return key


def append_spend(line):
    """Several fleet processes book at once; without a cross-process lock their appends tore into fragments
    (2026-10-23: two rows read as $1,687 and $2,208). msvcrt.locking retries for ~10 s, then raises."""
    import msvcrt
    with open(SPEND.with_suffix(".lock"), "a+b") as lock:
        lock.seek(0)
        msvcrt.locking(lock.fileno(), msvcrt.LK_LOCK, 1)
        try:
            with open(SPEND, "a", encoding="utf-8", newline="\n") as f:
                f.write(line)
        finally:
            lock.seek(0)
            msvcrt.locking(lock.fileno(), msvcrt.LK_UNLCK, 1)


def fleet_spent():
    total = 0.0
    if SPEND.exists():
        for line in SPEND.read_text(encoding="utf-8").splitlines():
            cells = line.split("\t")
            if len(cells) >= 3 and cells[1].startswith("fleet-"):
                total += float(cells[2])
    return total


class Fleet:
    def __init__(self, job, args):
        self.job, self.args = job, args
        self.client = anthropic.AsyncAnthropic(api_key=api_key(), max_retries=8)
        self.system = (FLEET / "jobs" / f"{job.prompt}.md").read_text(encoding="utf-8")
        self.tool_list = [t for t in TOOLS if not job.tools or t["name"] in job.tools]
        self.out = FLEET / "out" / job.name
        self.out.mkdir(parents=True, exist_ok=True)
        self.spent, self.reserved = fleet_spent(), 0.0
        self.lock = asyncio.Lock()
        self.tools = asyncio.Semaphore(24)   # bounds local rg/sqlite load, not the API
        self.log = open(FLEET / "logs" / f"{job.name}.log", "a", encoding="utf-8")

    def note(self, text):
        self.log.write(time.strftime("%Y-%m-%dT%H:%M:%SZ ", time.gmtime()) + text + "\n")
        self.log.flush()

    async def admit(self):
        async with self.lock:
            if self.spent + self.reserved + self.job.item_cap > self.args.cap:
                return False
            self.reserved += self.job.item_cap
            return True

    async def book(self, item_id, usd, tokens):
        async with self.lock:
            self.reserved -= self.job.item_cap
            self.spent += usd
            append_spend("\t".join([time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                                    f"fleet-{self.job.name}-{item_id}", f"{usd:.4f}", *map(str, tokens)]) + "\n")

    async def call_tool(self, name, args):
        if name not in RUNNERS:
            return f"unknown tool {name}"
        async with self.tools:
            try:
                return await asyncio.to_thread(RUNNERS[name], **args)
            except Exception as e:  # any tool failure goes back to the agent, never ends the run
                return f"tool error: {type(e).__name__}: {e}"[:1000]

    async def run_item(self, item):
        content = item["prompt"]
        if item.get("image"):  # vision items: the image, then the prompt
            path = Path(item["image"])
            media = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".gif": "image/gif",
                     ".webp": "image/webp"}[path.suffix.lower()]
            content = [{"type": "image", "source": {"type": "base64", "media_type": media,
                                                    "data": base64.b64encode(path.read_bytes()).decode()}},
                       {"type": "text", "text": item["prompt"]}]
        messages = [{"role": "user", "content": content}]
        usd, tokens, turns = 0.0, [0, 0, 0, 0], 0
        status, result, nudged = "no_submit", "", False
        try:
            while turns < MAX_TURNS:
                response = await self.client.messages.create(
                    model=MODEL, max_tokens=16000, system=self.system, tools=self.tool_list, messages=messages,
                    cache_control={"type": "ephemeral"}, output_config={"effort": self.job.effort})
                turns += 1
                cost, prompt = price(response.usage)
                usd += cost
                u = response.usage
                for i, v in enumerate((u.cache_read_input_tokens or 0, u.cache_creation_input_tokens or 0,
                                       u.input_tokens, u.output_tokens)):
                    tokens[i] += v
                messages.append({"role": "assistant", "content": response.content})
                if response.stop_reason == "refusal":
                    status = "refused"
                    break
                uses = [b for b in response.content if b.type == "tool_use"]
                submit = next((b for b in uses if b.name == "submit"), None)
                if submit:
                    status, result = submit.input.get("status", "done"), submit.input.get("result", "")
                    if not result:  # an agent that put its answer in other keys keeps it
                        rest = {k: v for k, v in submit.input.items() if k != "status"}
                        result = json.dumps(rest) if rest else ""
                    break
                if not uses:
                    result = "".join(b.text for b in response.content if b.type == "text")
                    break
                results = []
                for b in uses:
                    results.append({"type": "tool_result", "tool_use_id": b.id,
                                    "content": await self.call_tool(b.name, b.input)})
                if not nudged and (prompt > PROMPT_GUARD or usd > self.job.item_cap or turns >= MAX_TURNS - 3):
                    results.append({"type": "text", "text": "Budget reached: call submit now with your best result."})
                    nudged = True
                messages.append({"role": "user", "content": results})
        except anthropic.APIError as e:
            status, result = "api_error", f"{type(e).__name__}: {e}"[:500]
        except Exception as e:  # spend already made is booked below whatever went wrong
            status, result = "harness_error", f"{type(e).__name__}: {e}"[:500]
        await self.book(item["id"], usd, tokens)
        head = (f"<!-- fleet job={self.job.name} id={item['id']} status={status} turns={turns} usd={usd:.4f} "
                f"tokens(read,write,in,out)={tokens} model={MODEL} -->\n# {item['title']}\n\n")
        (self.out / f"{item['id']}.md").write_text(head + (result or "").strip() + "\n", encoding="utf-8")
        with open(self.out / "index.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps({"id": item["id"], "status": status, "turns": turns, "usd": round(usd, 4),
                                "tokens": tokens}) + "\n")
        self.note(f"{item['id']} {status} turns={turns} usd={usd:.4f} fleet={self.spent:.2f}")
        return status

    async def run(self, items):
        sem = asyncio.Semaphore(self.args.concurrency)
        stopped = []

        async def one(item):
            async with sem:
                if not await self.admit():
                    stopped.append(item["id"])
                    return "cap"
                return await self.run_item(item)

        self.note(f"start {len(items)} items, concurrency {self.args.concurrency}, cap ${self.args.cap}, "
                  f"fleet spent ${self.spent:.2f}")
        results = await asyncio.gather(*(one(i) for i in items), return_exceptions=True)
        results = [r if isinstance(r, str) else f"exception:{type(r).__name__}" for r in results]
        self.note(f"end: {dict((s, results.count(s)) for s in set(results))}; not started (cap): {len(stopped)}; "
                  f"fleet spent ${self.spent:.2f}")
        return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("job")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--only")
    ap.add_argument("--concurrency", type=int, default=50)
    ap.add_argument("--cap", type=float, default=175.0)
    ap.add_argument("--redo", action="store_true")
    args = ap.parse_args()
    job = jobs.JOBS[args.job]
    items = job.items()
    if args.only:
        wanted = set(args.only.split(","))
        items = [i for i in items if i["id"] in wanted]
    done_dir = FLEET / "out" / job.name
    if not args.redo:
        items = [i for i in items if not (done_dir / f"{i['id']}.md").exists()]
    if args.limit:
        items = items[: args.limit]
    results = asyncio.run(Fleet(job, args).run(items))
    print(json.dumps({s: results.count(s) for s in set(results)}), f"fleet spent ${fleet_spent():.2f}")


if __name__ == "__main__":
    main()
