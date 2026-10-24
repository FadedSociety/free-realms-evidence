# Free Realms articles (official site + Ten Ton Hammer)

Wayback Machine copies of the official freerealms.com (SOE news, patch notes, events, guides, error-code help,
2009-2013) and Ten Ton Hammer's Free Realms section (news, previews, interviews, guides, 2008-2014), read by the
Haiku fleet into sourced facts. Content evidence: client evidence wins where they disagree.

| Step | Script | Output |
|---|---|---|
| Crawl official site | `fleet/wiki/wayback_frcom.py crawl` (needs `references/freerealms-com/cdx-urls.json`) | `references/freerealms-com/frcom.sqlite` (948 pages) |
| Crawl Ten Ton Hammer | `fleet/wiki/wayback_tth.py crawl` | `references/tentonhammer/tth.sqlite` |
| Read every page | `fleet.py frcom-structure`, `fleet.py tth-structure`, prompt `fleet/jobs/article-structure.md` | `fleet/out/<job>/<id>.md` |
| Build lists | `fleet/wiki/articles.py` | this folder |

Both crawlers run one request per 4.5 s (the archive refuses connections above ~15 a minute), resume where they
stopped, and must not run at the same time. All scripts run with `lab/tools/wiki-env` (fleet with `fleet-venv`).

## Files

| File | What |
|---|---|
| `articles.json` | one row per page: source, url, capture date, title, type (news/event/patch_notes/guide/...), date, summary |
| `facts.json` | every fact: topic, name (+ client locale id when found), statement, numbers, era, verbatim quote, article |
| `quests.json` | quests the articles describe: giver, location, steps, rewards |
| `articles.sqlite` | the same as tables plus FTS5 `search`: `SELECT kind, title, body, url FROM search WHERE search MATCH 'hall pass'` |

`era` separates `live` facts from `pre_launch_plan` (previews before the April 2009 launch, which may not have
shipped). Pages in French, Spanish, Portuguese and German are summarised in English with the original-language quote.
