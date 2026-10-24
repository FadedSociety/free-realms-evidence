<!-- fleet job=pin-audit id=tests-piece-062-rs status=nothing_found turns=3 usd=0.0022 tokens(read,write,in,out)=[11217, 11856, 8, 1245] model=claude-haiku-5-5 -->
# tests/piece_062.rs

No findings in `prototype/osfr-tools/tests/piece_062.rs`. None of the five screened lines pins a value from a shipped data file under `data/content`.

- **207, 209 (`BARK_RECORDINGS[0|2].seconds`, 1.392 / 3.552):** these come from `src/restoration/piece_062.rs:395-408`. The doc comment says they were measured from the preserved pack MP3s, so they are recovered constants, not tunables. The only `1.39222` and `3.552023` hits in `data/content` are NPC spawn position and heading values in `npc_spawns_extra.json`, which are unrelated.
- **215, 216 (`SPAWN_SMOKE_END_SECONDS`, `CHEST_BEAM_END_SECONDS`, 3.0):** these are `f32` constants at `src/restoration/piece_062.rs:425` and `:429`, documented as the authored end times of the original effect XMLs. No data file carries them.
- **217 (`CHEST_BEAM_HIT_FLASH_SECONDS`, 0.5):** same situation, a constant at `src/restoration/piece_062.rs:431` documented as the original hit-flash start time.

These are protocol or recovered-source values carried in code, not gameplay tunables in the data files, so the rule does not apply to them.
