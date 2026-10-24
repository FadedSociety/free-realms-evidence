"""event_packs.py: one evidence pack per Free Realms live event, for the events-calendar pass (lead, 2026-10-23).

Events are the article facts with topic "event" (references/articles/facts.json), grouped by name with years and
filler words dropped. Each pack: the event's facts (statement, numbers, era, quote, article, date), those articles'
summaries, the wiki pages in a category of the same name (seasonal items, NPCs), and the quest answers whose title,
line or objectives mention it. Writes references/quest-lines/event-packs/<key>.json and event-keys.json.
"""
import json
import re
import sqlite3
from pathlib import Path

LAB = Path(r"C:\Users\Bryce\Documents\Projects\CartoonMMO\lab")
OUT = LAB / "references" / "quest-lines"
norm = lambda s: re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()  # noqa: E731


def key_of(name):
    k = re.sub(r"\b(20\d\d|event|events|the|annual|celebration|community)\b", "", norm(name))
    return re.sub(r"\s+", " ", k).strip()


def main():
    facts = json.load(open(LAB / "references" / "articles" / "facts.json", encoding="utf-8"))
    articles = {a["id"]: a for a in json.load(open(LAB / "references" / "articles" / "articles.json", encoding="utf-8"))}
    quests = json.load(open(OUT / "quests.json", encoding="utf-8"))
    wiki = sqlite3.connect(f"file:{LAB / 'references' / 'freerealms-wiki' / 'harvest' / 'harvest.sqlite'}?mode=ro",
                           uri=True)
    cats = {}
    for title, cat in wiki.execute("SELECT p.title, c.category FROM page_categories c JOIN pages p USING(page_id) "
                                   "WHERE p.ns = 0"):
        cats.setdefault(key_of(cat), []).append(title)
    groups = {}
    for f in facts:
        if f.get("topic") == "event" and f.get("name") and key_of(f["name"]):
            groups.setdefault(key_of(f["name"]), []).append(f)
    (OUT / "event-packs").mkdir(exist_ok=True)
    keys = []
    for k, fs in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        names = sorted({f["name"] for f in fs})
        ids = list(dict.fromkeys(f["article"]["id"] for f in fs))
        words = k.split()
        related = []
        for r in quests:
            a = r.get("answer") or {}
            text = norm(" ".join([str((a.get("quest") or {}).get("title")), str((a.get("line") or {}).get("name"))]))
            if words and all(w in text for w in words):
                related.append(f"{(a.get('quest') or {}).get('title')} ({r['status']}, live {a.get('live')})")
        key = "v" + re.sub(r"[^a-z0-9]+", "-", k)[:60]
        pack = {"title": names[0], "names_seen": names[:8],
                "facts": [{k2: f.get(k2) for k2 in ("statement", "numbers", "era", "quote")} |
                          {"article": f["article"]["url"], "date": f["article"]["date"]} for f in fs[:30]],
                "article_summaries": [{"url": articles[i].get("url"), "date": articles[i].get("date"),
                                       "title": articles[i].get("title"), "summary": articles[i].get("summary")}
                                      for i in ids[:6] if i in articles],
                "wiki_category_members": cats.get(k, [])[:60], "quest_answers_mentioning_it": related[:15]}
        (OUT / "event-packs" / f"{key}.json").write_text(json.dumps(pack, indent=1, ensure_ascii=False),
                                                         encoding="utf-8")
        keys.append(key)
    (OUT / "event-keys.json").write_text(json.dumps(keys), encoding="utf-8")
    print(json.dumps({"events": len(keys), "with_wiki_category": sum(1 for k in groups if cats.get(k)),
                      "with_quests": None}))


if __name__ == "__main__":
    main()
