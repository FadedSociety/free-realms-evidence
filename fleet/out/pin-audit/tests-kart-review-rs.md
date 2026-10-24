<!-- fleet job=pin-audit id=tests-kart-review-rs status=nothing_found turns=6 usd=0.0033 tokens(read,write,in,out)=[34924, 16681, 14, 1795] model=claude-haiku-5-5 -->
# tests/kart_review.rs

No findings in `prototype/osfr-tools/tests/kart_review.rs` for the four screened lines.

- **240 `assert_eq!(row0, (1, 1, 1, 37, 3030))`:** these values are not from a data file. They come from the test's own lobby oracle. `lobby_oracle_re_derives_from_the_community_layout` (lines 166-167) hard-codes `(1, 1, KART_RACE_GAME_TYPE, 37, 3030)`, and `LOBBY_ORACLE_HEX` (line 47) is a pinned community wire capture. The `3030` is a name_id in that capture, a protocol-level value, not a tunable. No kart row in `data/content` carries it; the only `kart` hits there are achievements, jobs, NPC spawns, and `kart_entry.json`, which holds model assets.
- **500, 501, 541 (`coins: 10, xp: 25`):** these come from the test's own `priced_track()` fixture (`lines 29-37`: `Some(RewardSchedule { coins: 10, xp: 25 })`). The fixture sets the values and the test asserts what the fixture supplied. No file under `data/content` defines a kart reward schedule, so there is nothing to retune.

The same fixture values also appear at lines 371, 470-471, 505, 520, and 549. None of them is a finding for the same reason.
