<!-- fleet job=bug-hunt id=src-startup-catalogues-rs-L1 status=nothing_found turns=7 usd=0.0066 tokens(read,write,in,out)=[89646, 25965, 16, 4927] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/startup_catalogues.rs lines 1-259 of 259

No reachable defect in `startup_catalogues.rs` lines 1-259.

What I checked:

- **Input provenance.** Every builder in the window takes its data from `StartupSnapshot` (`startup_snapshot.rs:309-364`, `396-486`). That snapshot is an operator-supplied file (`lab/content/startup-snapshot/startup.json`, loaded at `gateway.rs:838`). The only per-client value that reaches a builder is `character_guid` (`build_stats`, `startup_snapshot.rs:483`). Nothing a remote client sends becomes a builder argument, so the panics and asserts in the builders are not reachable from a client packet.
- **Builder asserts vs. snapshot validation.** `StartupSnapshot::validate` (`startup_snapshot.rs:254-304`) guards each assert in the window:
  - `build_item_definitions` (`:115-120`): the length >= 4 and id match are checked at `:278-285`.
  - `build_ability_set_definition` (`:171-177`): the kind range and the kind-0-empty rule are checked at `:286-293`.
  - `build_stat_update` (`:214`): NaN is rejected at `:298-302`. `kind` is `u32` (`startup_snapshot.rs:67`), so negative kinds cannot occur.
  - `build_effect_tag` index: `effect_tags.len() == 2` is enforced at `:258`, and `36 | 37` only indexes 0 and 1.
- **Length arithmetic.** `build_item_definitions` writes `records + 4` as the byte length. The byte-exact oracle test (`tests/startup_catalogues.rs:88-92`) compares this against the captured 5/login packet, so the `+4` matches the client reader. `tunnel` and `count_i32` `expect`s only fire at sizes capped by `MAX_ROWS = 100_000` (`startup_snapshot.rs:14`) and are reachable only from the operator file.
- **Fixed-value builders.** `build_overworld_combat_flag`, `build_client_game_settings`, `build_unidentified_193_2`, and `build_opcode_14_marker` take no external input and write constants, so no defect.
- **Coin store.** Each row is 19 bytes (id, three dwords, three flags), matching the doc comment. No check is missing that a client could exploit.

No findings.
