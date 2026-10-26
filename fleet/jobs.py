"""jobs.py: the fleet's jobs (lead, 2026-10-22). Each job names its system prompt (jobs/<prompt>.md), its effort,
a per-item spend cap in USD, and how to list its items: {id, title, prompt}. Item ids are file-name safe."""
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

CMMO = Path(r"C:\Users\Bryce\Documents\Projects\CartoonMMO")
AP = CMMO / "lab" / "autopilot"
REPO = CMMO / "fleet-ro"
TOOLS = REPO / "prototype" / "osfr-tools"


@dataclass
class Job:
    name: str
    prompt: str
    effort: str
    item_cap: float
    items: Callable[[], list]
    tools: tuple = ()   # tool names the agents get; empty = all


def slug(text):
    return re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-")[:90]


def brief_items():
    """Job 1: one research pack per queued build brief."""
    items = []
    for path in sorted((AP / "queue").glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        title = next((ln[7:].strip() for ln in text.splitlines() if ln.startswith("title: ")), path.stem)
        brief_id = re.match(r"[TF]\d+", path.name).group(0)
        items.append({"id": brief_id, "title": f"{brief_id}: {title}",
                      "prompt": f"Queued brief `briefs/{path.name}` (full text below).\n\n" + text[:20_000]})
    return items


def unrouted_items():
    """Job 2: one re-check per row of notes/Research/Unrouted Client Requests.md (survey of 2026-10-16)."""
    note = REPO / "notes" / "Research" / "Unrouted Client Requests.md"
    items, area = [], ""
    for n, line in enumerate(note.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("## "):
            area = line[3:].strip()
        m = re.match(r"\| (R\d+) ", line)
        if m:
            items.append({"id": m.group(1), "title": f"{m.group(1)} ({area})",
                          "prompt": f"Survey row `repo:notes/Research/Unrouted Client Requests.md:{n}`, section "
                                    f"\"{area}\" (survey written 2026-10-16):\n\n{line[:6000]}"})
    return items


def window_items(folder, size):
    """One item per window of `size` lines of each .rs file under `folder`."""
    items = []
    for path in sorted(folder.rglob("*.rs")):
        rel = path.relative_to(REPO).as_posix()
        lines = sum(1 for _ in open(path, encoding="utf-8", errors="replace"))
        for start in range(1, max(lines, 1) + 1, size):
            end = min(start + size - 1, lines)
            tag = f"{slug(path.relative_to(TOOLS).as_posix())}-L{start}"
            items.append({"id": tag, "title": f"{rel} lines {start}-{end} of {lines}",
                          "prompt": f"Your window: `repo:{rel}` lines {start}-{end} (the file has {lines} lines). "
                                    "Read the window in full; read anything outside it only as needed."})
    return items


def doc_items(folder, max_bytes):
    items = []
    for path in sorted(folder.rglob("*.md")):
        if path.stat().st_size > max_bytes:
            continue
        rel = path.relative_to(REPO).as_posix()
        items.append({"id": slug(path.relative_to(folder).as_posix()[:-3]), "title": rel,
                      "prompt": f"Your note: `repo:{rel}` ({path.stat().st_size} bytes). Check it against the code "
                                "at the current tip."})
    return items


def greeting_items():
    """Job 8: one search per talkable NPC record (not an enemy) that has no greeting yet."""
    import json
    items = []
    for path in sorted((TOOLS / "data" / "content" / "npcs").glob("*.json")):
        for r in json.load(open(path, encoding="utf-8")).get("records", []):
            roles = r.get("roles") or []
            if r.get("greeting_string_id") or not roles or "enemy" in roles:
                continue
            facts = {k: r.get(k) for k in ("npc_id", "name", "name_string_id", "zone", "roles", "title_or_role",
                                            "quests_given_text", "services")}
            items.append({"id": str(r["npc_id"]), "title": f"{r.get('name')} ({r.get('zone')})",
                          "prompt": f"NPC record in `repo:prototype/osfr-tools/data/content/npcs/{path.name}`:\n\n"
                                    + json.dumps(facts, ensure_ascii=False, indent=1)[:4000]})
    return items


def quest_giver_items():
    """Job 6: one dossier per quest-giving NPC whose record names quests."""
    import json
    items = []
    for path in sorted((TOOLS / "data" / "content" / "npcs").glob("*.json")):
        for r in json.load(open(path, encoding="utf-8")).get("records", []):
            given = [q for q in (r.get("quests_given_text") or []) if "none found" not in q.lower()]
            if "quest_giver" not in (r.get("roles") or []) or not given:
                continue
            facts = {k: r.get(k) for k in ("npc_id", "name", "name_string_id", "zone", "roles", "title_or_role",
                                            "quests_given_text", "quest_ids_given")}
            items.append({"id": str(r["npc_id"]), "title": f"Quests of {r.get('name')} ({r.get('zone')})",
                          "prompt": f"Quest giver record in `repo:prototype/osfr-tools/data/content/npcs/{path.name}`:"
                                    "\n\n" + json.dumps(facts, ensure_ascii=False, indent=1)[:6000]})
    return items


def bug_finding_items(source="bug-hunt", levels="high|medium"):
    """Verify pass: one skeptic per finding of the given levels in a finding job's outputs."""
    out = CMMO / "lab" / "fleet" / "out" / source
    items = []
    for path in sorted(out.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        blocks = re.split(r"(?m)^(?=- \*\*\[(?:high|medium|low)\])", text)
        n = 0
        for block in blocks:
            m = re.match(rf"- \*\*\[({levels})\] ([^ ]+)", block)
            if not m:
                continue
            n += 1
            items.append({"id": f"{path.stem}-f{n}", "title": f"{m.group(1)}: {m.group(2)}",
                          "prompt": "Claimed defect (from a first-pass reviewer):\n\n" + block.strip()[:6000]})
    return items


HARVEST = CMMO / "lab" / "references" / "freerealms-wiki" / "harvest"


def wiki_image_items():
    """Job: read the text out of every raster image on the Fandom wiki (harvest.py prepare made the vision copies).
    One item per unique image (sha1); its names, the pages that use it and its file-page categories go in the prompt.
    Images used on item, weapon and job pages come first."""
    import sqlite3
    con = sqlite3.connect(f"file:{HARVEST / 'harvest.sqlite'}?mode=ro", uri=True)
    files = {}
    for name, sha1, vision in con.execute("SELECT name, sha1, vision FROM files WHERE vision LIKE 'vision%'"):
        files.setdefault(sha1, {"names": [], "vision": vision})["names"].append(name)
    used = {}
    for title, f in con.execute("SELECT p.title, i.file FROM page_images i JOIN pages p USING(page_id)"):
        used.setdefault(f.replace("_", " "), []).append(title)
    cats = {}
    for title, c in con.execute("SELECT p.title, c.category FROM page_categories c JOIN pages p USING(page_id) "
                                "WHERE p.ns = 6"):
        cats.setdefault(title.split(":", 1)[1], []).append(c)
    hot = re.compile(r"weapon|sword|bow|wand|staff|blade|hammer|axe|fist|gauntlet|scythe|item|armor|armour|"
                     r"equipment|stat|tooltip|power|job|pet|mount|ride|collection|vendor|shop|price", re.I)
    items = []
    for sha1, f in files.items():
        pages = sorted({p for n in f["names"] for p in used.get(n, [])})
        fcats = sorted({c for n in f["names"] for c in cats.get(n, [])})
        context = " ".join(f["names"] + pages + fcats)
        prompt = (f"Wiki file name(s): {'; '.join(f['names'])}\n"
                  f"Used on wiki page(s): {'; '.join(pages[:40]) or '(none)'}\n"
                  f"File categories: {'; '.join(fcats) or '(none)'}\n\n"
                  "Read the image and submit the JSON result.")
        items.append({"id": sha1, "title": f["names"][0], "prompt": prompt, "image": str(HARVEST / f["vision"]),
                      "_hot": 0 if hot.search(context) else 1})
    items.sort(key=lambda i: (i["_hot"], i["title"]))
    return items


def tth_items():
    """Job: structure every Free Realms article the Ten Ton Hammer crawler (wiki/wayback_tth.py) stored. An article's
    ?page=N continuations are joined to it in page order."""
    import sqlite3
    db = CMMO / "lab" / "references" / "tentonhammer" / "tth.sqlite"
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    arts = {}
    for url, ts, title, text in con.execute("SELECT url, ts, title, text FROM pages WHERE kind != 'listing'"):
        base, _, query = url.partition("?")
        page = int(m.group(1)) if (m := re.search(r"page=(\d+)", query)) else 0
        arts.setdefault(base.rstrip("/"), []).append((page, ts, title, text))
    items = []
    for base, parts in sorted(arts.items()):
        parts.sort()
        _, ts, title, _ = parts[0]
        body = "\n\n".join(p[3] for p in parts)[:40000]
        items.append({"id": slug(base.split("://", 1)[-1]), "title": title,
                      "prompt": f"URL: {base}\nCaptured: {ts[:8]}\nTitle: {title}\n\nText:\n{body}"})
    return items


def frcom_items(db=CMMO / "lab" / "references" / "freerealms-com" / "frcom.sqlite"):
    """Job: structure every page a site crawler stored (wiki/wayback_frcom.py; wayback_forum.py shares the schema)."""
    import sqlite3
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    return [{"id": slug(f"{kind}-{key}"), "title": title or key,
             "prompt": f"URL: {url}\nCaptured: {ts[:8]}\nTitle: {title}\n\nText:\n{text[:40000]}"}
            for kind, key, url, ts, title, text in con.execute(
                "SELECT kind, key, url, ts, title, text FROM pages WHERE length(text) > 200 ORDER BY kind, key")]


def locale_tag_items():
    """Job: tag every client locale string (quests/locale_index.py batches: ~40 consecutive ids each)."""
    import sys
    sys.path.insert(0, str(CMMO / "lab" / "fleet" / "quests"))
    import locale_index
    return [{"id": f"batch-{k:05d}", "title": f"locale {lines[0][0]}-{lines[-1][0]}",
             "prompt": "\n".join(f"{i}: {t}" for i, t in lines)} for k, lines in locale_index.batches()]


def pin_items():
    """Job: one item per test file whose assertions Jev says may pin a tunable value (pins.py survivors)."""
    import json
    path = CMMO / "lab" / "fleet" / "out" / "pin-audit" / "survivors.json"
    return [{"id": slug(it["file"]), "title": it["file"],
             "prompt": f"Your file: `repo:prototype/osfr-tools/{it['file']}`. Screened lines:\n" + "\n".join(it["lines"])}
            for it in json.load(open(path, encoding="utf-8"))] if path.exists() else []


def round_items(job):
    """Items the quest-lines driver (quests/quest_lines.py) wrote for this round of `job`."""
    import json
    path = CMMO / "lab" / "references" / "quest-lines" / "round" / f"{job}.json"
    return json.load(open(path, encoding="utf-8")) if path.exists() else []


def hp_frame_items():
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent / "quests"))
    import enemy_hp_video
    return enemy_hp_video.frame_items()


QUEST_TOOLS = ("lookup", "locale", "search", "read", "submit")

JOBS = {
    "quest-infer": Job("quest-infer", "quest-infer", "low", 0.08, lambda: round_items("quest-infer"), tools=QUEST_TOOLS),
    "quest-critic": Job("quest-critic", "quest-critic", "low", 0.06, lambda: round_items("quest-critic"),
                        tools=QUEST_TOOLS),
    "npc-infer": Job("npc-infer", "npc-infer", "low", 0.08, lambda: round_items("npc-infer"), tools=QUEST_TOOLS),
    "npc-critic": Job("npc-critic", "npc-critic", "low", 0.06, lambda: round_items("npc-critic"), tools=QUEST_TOOLS),
    "enemy-infer": Job("enemy-infer", "enemy-infer", "low", 0.08, lambda: round_items("enemy-infer"),
                       tools=QUEST_TOOLS),
    "item-infer": Job("item-infer", "item-infer", "low", 0.06, lambda: round_items("item-infer"), tools=QUEST_TOOLS),
    "item-critic": Job("item-critic", "item-critic", "low", 0.05, lambda: round_items("item-critic"),
                       tools=QUEST_TOOLS),
    "citem-infer": Job("citem-infer", "citem-infer", "low", 0.05, lambda: round_items("citem-infer"),
                       tools=QUEST_TOOLS),
    "citem-critic": Job("citem-critic", "citem-critic", "low", 0.04, lambda: round_items("citem-critic"),
                        tools=QUEST_TOOLS),
    "schedule-infer": Job("schedule-infer", "schedule-infer", "low", 0.06, lambda: round_items("schedule-infer"),
                          tools=QUEST_TOOLS),
    "schedule-critic": Job("schedule-critic", "schedule-critic", "low", 0.05, lambda: round_items("schedule-critic"),
                           tools=QUEST_TOOLS),
    "objfix-infer": Job("objfix-infer", "objfix-infer", "low", 0.06, lambda: round_items("objfix-infer"),
                        tools=QUEST_TOOLS),
    "objfix-critic": Job("objfix-critic", "objfix-critic", "low", 0.05, lambda: round_items("objfix-critic"),
                         tools=QUEST_TOOLS),
    "testaudit-infer": Job("testaudit-infer", "testaudit-infer", "low", 0.06, lambda: round_items("testaudit-infer"),
                           tools=QUEST_TOOLS),
    "testaudit-critic": Job("testaudit-critic", "testaudit-critic", "low", 0.05, lambda: round_items("testaudit-critic"),
                            tools=QUEST_TOOLS),
    # The same fix prompts over the drafts that already resolved (counts, splits, actor kinds).
    "objcheck-infer": Job("objcheck-infer", "objfix-infer", "low", 0.06, lambda: round_items("objcheck-infer"),
                          tools=QUEST_TOOLS),
    "objcheck-critic": Job("objcheck-critic", "objfix-critic", "low", 0.05, lambda: round_items("objcheck-critic"),
                           tools=QUEST_TOOLS),
    # One gameplay-video frame around an enemy sighting (quests/enemy_hp_video.py picks them).
    "hp-frame": Job("hp-frame", "hp-frame", "low", 0.02, hp_frame_items, tools=("submit",)),
    # A reference spawn for each needs_spawn objective (quests/spawn_objects.py writes the packs).
    "spawnobj-infer": Job("spawnobj-infer", "spawnobj-infer", "low", 0.05, lambda: round_items("spawnobj-infer"),
                          tools=("locale", "submit")),
    # Unknown objectives with every id filled: settled with (R) values, or keep (quests/objpromote.py).
    "objpromote-judge": Job("objpromote-judge", "objpromote-judge", "low", 0.02, lambda: round_items("objpromote-judge"),
                            tools=("submit",)),
    "line-infer": Job("line-infer", "line-infer", "low", 0.06, lambda: round_items("line-infer"), tools=QUEST_TOOLS),
    "line-critic": Job("line-critic", "line-critic", "low", 0.05, lambda: round_items("line-critic"),
                       tools=QUEST_TOOLS),
    "event-infer": Job("event-infer", "event-infer", "low", 0.06, lambda: round_items("event-infer"),
                       tools=QUEST_TOOLS),
    "event-critic": Job("event-critic", "event-critic", "low", 0.05, lambda: round_items("event-critic"),
                        tools=QUEST_TOOLS),
    "dialog-infer": Job("dialog-infer", "dialog-infer", "low", 0.06, lambda: round_items("dialog-infer"),
                        tools=QUEST_TOOLS),
    "dialog-critic": Job("dialog-critic", "dialog-critic", "low", 0.05, lambda: round_items("dialog-critic"),
                         tools=QUEST_TOOLS),
    "enemy-critic": Job("enemy-critic", "enemy-critic", "low", 0.06, lambda: round_items("enemy-critic"),
                        tools=QUEST_TOOLS),
    "locale-tag": Job("locale-tag", "locale-tag", "low", 0.02, locale_tag_items, tools=("submit",)),
    "tth-structure": Job("tth-structure", "article-structure", "low", 0.10, tth_items, tools=("locale", "submit")),
    "frcom-structure": Job("frcom-structure", "article-structure", "low", 0.10, frcom_items,
                           tools=("locale", "submit")),
    "forum-structure": Job("forum-structure", "article-structure", "low", 0.10,
                           lambda: frcom_items(CMMO / "lab" / "references" / "freerealmsforums" / "forum.sqlite"),
                           tools=("locale", "submit")),
    "wiki-image-text": Job("wiki-image-text", "wiki-image-text", "low", 0.05, wiki_image_items,
                           tools=("locale", "submit")),
    "brief-research": Job("brief-research", "brief-research", "high", 0.60, brief_items),
    "unrouted-recheck": Job("unrouted-recheck", "unrouted-recheck", "high", 0.40, unrouted_items),
    "bug-hunt": Job("bug-hunt", "bug-hunt", "high", 0.50, lambda: window_items(TOOLS / "src", 800)),
    "test-audit": Job("test-audit", "test-audit", "medium", 0.30, lambda: window_items(TOOLS / "tests", 1200)),
    "pin-audit": Job("pin-audit", "pin-audit", "low", 0.12, pin_items, tools=("search", "read", "list", "submit")),
    "guide-refresh": Job("guide-refresh", "doc-refresh", "high", 0.60,
                         lambda: doc_items(REPO / "notes" / "Build Guides", 200_000)),
    "note-refresh": Job("note-refresh", "doc-refresh", "high", 0.60,
                        lambda: doc_items(REPO / "notes" / "Research", 200_000)),
    "quest-dossier": Job("quest-dossier", "quest-dossier", "high", 0.60, quest_giver_items),
    "greeting-sweep": Job("greeting-sweep", "greeting-sweep", "medium", 0.25, greeting_items),
    "bug-verify": Job("bug-verify", "bug-verify", "high", 0.40, bug_finding_items),
    "test-verify": Job("test-verify", "test-verify", "high", 0.30, lambda: bug_finding_items("test-audit", "high")),
}
