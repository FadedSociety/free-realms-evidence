# Free Realms wiki harvest

Everything on freerealms.fandom.com (2026-10-22): page text, categories, templates, tables, every image, and
what every image says (read by the Haiku fleet). Rebuild from scratch with the scripts in `lab/fleet/wiki/`.
Wiki facts are content evidence; client evidence wins where they disagree (memory: content-source-precedence).

| Step | Script | Output |
|---|---|---|
| Pages, links, files, download, parse | `harvest.py all` (wiki-env) | `harvest.sqlite`, `images/` (1.2 GB originals), `vision/` |
| Read every image | `fleet.py wiki-image-text` (fleet-venv), prompt `fleet/jobs/wiki-image-text.md` | `fleet/out/wiki-image-text/<sha1>.md` |
| Fold readings back, build lists | `merge.py` (wiki-env) | `lists/*.json`, `image_text` and FTS5 `search` tables |

## Lists (`lists/`)

| File | What |
|---|---|
| `weapons.json` | 653 weapon pages: level, jobs, power, coin/SC prices, acquisition, abilities with damage/heal; every tooltip image of the same weapon and `text_vs_image` checks |
| `attacks.json` | 259 attacks: damage and heal as a multiple of the tier base (`damage_x`), jobs, weapons, shape/effect tags |
| `catalog.json` | 2,217 articles with a price, in-game description (`{{IGD}}`), quote or infobox; 1,117 priced |
| `quests.json` | 408 quest names: the 52 Quest: pages (summary, coins, chain, requirements, steps) + NPC givers (273) + pages that mention them |
| `items.json`, `tooltips.json`, `abilities.json` | per item / per tooltip image / per ability, from the image readings |
| `image_text.json` | all 5,120 transcriptions (kind, verbatim text, tooltip fields) with file names and pages |
| `infobox_*.json`, `categories.json`, `tables.json` | raw structured wiki data (pets, rides, collections, locations, jobs...) |

Full-text lookup: `SELECT kind, title, snippet(search, 2, '[', ']', '..', 12) FROM search WHERE search MATCH 'sunstone'`.

## What the numbers show (derived, R)

- **Damage = tier base x attack multiplier.** Tier bases 889 / 1554 / 2716 / 4750 / 8302 for Power 1-5 (x1.75 a
  tier). Power tiers line up with level bands 1 / 4 / 8 / 12 / 16: Bit Basher's Megabonk lists exactly these five
  numbers at Level 1+/4+/8+/12+/16+.
- **Multipliers sit on sevenths:** 1/7 (Multi-Shot), 2/7 (Flame Flash, Glancing Blow, most first attacks),
  4/7 (Spinning Attack, Volley, Firestorm), 5/7, 1.0 (Triage, Leg Sweep, 1000 Storms), 9/7 (Dragonstrike,
  Lightning Blast, Cleave). Many come in a x1.1 variant (0.314, 0.792, 1.414): two versions of the same weapon
  differ by exactly 1.1 (Balloon weapons' Party Crasher 7685 vs 8453), likely a later rebalance or an upgraded version.
- **Heals** use the same scale (Triage heals 2/7 of the tier base).
- **Vendor weapon prices** by level: 750 / 850 / 1055 / 1504 / 2152 coins at levels 1 / 4 / 8 / 12 / 16.
  Resell value is one tenth of the buy price.
- New School weapons (Power 5, Level 1, SC shop) scale with the player; their pages show level-1 numbers.

## Accuracy

Where the page text and a tooltip image both give a number they agree 91% on damage (252/278), 96% on level and
97% on power; most disagreements are real version differences (old and new versions, the x1.1 pairs), a few are
misreads (one "Power 22"). Every reading keeps its image sha1 and file name, so any number can be checked by eye.
36 files the CDN no longer serves as originals and 2 images the reader failed on are missing.
