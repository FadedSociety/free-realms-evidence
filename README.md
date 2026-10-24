# Free Realms revival: evidence (PRIVATE)

The off-machine copy of the research behind the revival. In the game repo, `lab/` is never committed; this repo
mirrors the curated part of it. It holds copyrighted Free Realms wiki, freerealms.com, Ten Ton Hammer and forum
text, so it must stay private and is never shared.

Synced by `fleet/evidence_sync.ps1` (from `lab/fleet/` in the game checkout). Layout mirrors `lab/`:

- `references/quest-lines/`: the inferred answers with per-claim evidence: quests, quest lines, NPCs, dialogs, enemies,
  events, event schedules, items (wiki and client catalogue), the tagged client text index (`index.sqlite`), Jev's
  item tags (`catalogue.sqlite`) and the flag lists. `README.md` there explains each file.
- `references/articles/`, `references/freerealms-com/`, `references/freerealmsforums/`: the Wayback archives of the
  official site, Ten Ton Hammer and the forums, and the facts read from them.
- `references/freerealms-wiki/harvest/lists/`: the lists merged from the full wiki harvest (weapons, attacks,
  catalogue, quests, image text). The 2.8 GB raw harvest and images stay local (re-harvestable).
- `fleet/out/`: every agent answer and critique, the audit trail behind each final answer.
- `fleet/jobs/`, `fleet/*.py`, `fleet/quests/*.py`: the prompts and scripts that produced it.
- `reports/`: lead reports built from the evidence.

Rules: client evidence overrides the wiki; reconstructed values are marked (R).
