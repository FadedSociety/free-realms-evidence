<!-- fleet job=pin-audit id=tests-piece-034-rs status=nothing_found turns=6 usd=0.0040 tokens(read,write,in,out)=[52636, 17706, 14, 2591] model=claude-haiku-5-5 -->
# tests/piece_034.rs

No findings in `prototype/osfr-tools/tests/piece_034.rs`. Every screened number comes from the test's own fixture or a recovered original-game fact, not from a shipped `data/content` value that tuning would change.

- **192** `the_..._power_2_blade` (weapon `power_rating` 2): from the inline `CATALOGUE` fixture (line 71). The test builds it, so it is not a finding.
- **205, 208** `the_training_sword_resolves_the_recovered_ability_pair` (`damage` 254 / 889): from the inline `CATALOGUE` abilities (lines 77-83). Not a finding.
- **206, 251** (`cooldown_ms` 600): from the inline `CATALOGUE` (`basic_recast_ms` and ability 2154). Fixture-owned, not a finding.
- **297, 318, 396** (`energy()` 100): from the inline `CATALOGUE` `energy_max` 100 (line 93). Fixture-owned, not a finding.
- **456** `the_emitted_ninja_catalogue_validates` (`special.damage` 889): this reads the emitted catalogue at `OSFR_PIECE_034_CATALOGUE`, which `scripts/pieces/piece_034.py` builds from the wiki's Power-1 damage ladder. The script does not read any `data/content` file. The 889 is a recovered original-game damage value, and the test is env-gated. Retuning a `data/content` field would not break it. Not a finding, though a reader could reasonably check it against `data/reference/attacks.json` `tier_base["1"]`, which holds the same 889.
