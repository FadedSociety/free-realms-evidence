<!-- fleet job=pin-audit id=tests-abilities-rs status=nothing_found turns=4 usd=0.0026 tokens(read,write,in,out)=[18824, 12500, 10, 1740] model=claude-haiku-5-5 -->
# tests/abilities.rs

No findings in `prototype/osfr-tools/tests/abilities.rs`. None of the five screened lines pins a value from a shipped `data/content` file:

- **175 `first_aid_..._fixture_loads...`** (`250`): comes from `tests/fixtures/abilities/medic.json` line 55 (`effects[0].amount.value`). That is a test-owned fixture, not a file in `data/content`, and the test loads it itself. Retuning shipped data does not affect it.
- **242 `damage_cast_updates_energy_health...`** (`15`): 40 (the `hostile()` fixture's health) minus 25 (the `damage(25)` the test builds). Fixture-owned.
- **243 same test** (`200`): `now_ms` 100 plus `cooldown_ms` 100 from the test's own `definition()` helper (`abilities.rs:89`). Fixture-owned, not from `data/content`.
- **307 `healing_emits_hitpoint_delta...`** (`100`): the max-health argument the test passes to `CombatState::new` for the target. Fixture-owned.
- **340 `first_aid_can_select_the_caster_as_its_target`** (`100`): the max-health argument in the test's `caster()` helper (`abilities.rs:96`). Fixture-owned.

Only the medic fixture is loaded from a file, and it is under `tests/`, so it is not a shipped data value.
