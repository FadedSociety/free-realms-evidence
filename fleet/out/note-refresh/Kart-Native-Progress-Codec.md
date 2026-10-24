<!-- fleet job=note-refresh id=Kart-Native-Progress-Codec status=done turns=9 usd=0.0132 tokens(read,write,in,out)=[195646, 49989, 20, 10058] model=claude-haiku-5-5 -->
# notes/Research/Kart Native Progress Codec.md

**Verdict:** minor drift. The codec itself matches the tip: the 73-byte layout, the 4-byte and 8-byte payloads, both NaN policies, `results_row_finished` (`wrapping_add(1)`), `results_screen_trigger` (`<=`), and the ignored private gate's assertions (9,358 / 7 frames, laps `{0: 8869, 1: 489}`, 0 at limit, FLT_MAX counts 6 and 5) all match the code. The integration bookkeeping is stale: the module is now registered and partly routed, and the `#[path]` include is gone.

**Corrections:**

1. `old:` The module is a `#[path]` include in the test target; the test also includes the
   `new:` The module is registered in the crate (`pub mod kart_progress_native;`, `lib.rs:45`) and the test imports it from `osfr_tools`, with no `#[path]` include; the test also uses the
   `why:` `repo:prototype/osfr-tools/src/lib.rs:45` registers the module; `repo:prototype/osfr-tools/tests/kart_progress_native.rs:30-37` imports `osfr_tools::kart_racing` and `osfr_tools::kart_progress_native`, and the file has no `#[path]` (grep found none).

2. `old:` 1. Lead integration: register `pub mod kart_progress_native;`, drop the `#[path]` includes, and route
   `new:` 1. Lead integration (registration and crate import are done, see `lib.rs:45`): still to do, route
   `why:` `repo:prototype/osfr-tools/src/lib.rs:45`; `repo:prototype/osfr-tools/src/kart_service.rs:121` and `:130` import the module; `repo:prototype/osfr-tools/tests/kart_progress_native.rs:30-37`.

3. `old:` decoded subtype-14 frames from the gateway/racer path through `decode_progress`/`encode_progress`.
   `new:` decoded subtype-14 frames from the gateway/racer path through `decode_progress`. Encoding is already routed (`kart_service.rs:2706` in `progress_frame`, `kart_entry.rs:682` in the `on_race_ready` replies), but `decode_progress` has no production caller yet; its only callers are in `tests/kart_progress_native.rs`.
   `why:` `repo:prototype/osfr-tools/src/kart_service.rs:2693-2708`; `repo:prototype/osfr-tools/src/kart_entry.rs:679-684`; `grep decode_progress` under `prototype/osfr-tools/src` returns only the module itself.

4. `old:` 8 committed vectors + 1 ignored private gate
   `new:` 9 committed vectors + 1 ignored private gate
   `why:` `repo:prototype/osfr-tools/tests/kart_progress_native.rs:81,99,126,156,192,209,227,246,255` are nine `#[test]` functions, plus the ignored one at `:282`. The note's own green log ("9 passed, 0 failed, 1 ignored") and `notes/Autopilot/F181.md:148`, `F207.md:174` agree with nine.

**Unsure:**

- Line 16's sentence "No shared `lib.rs`, `kart_racing.rs`, gateway, gameplay, `Cargo.toml`, content, save, UI or release path was touched" was true for the codec's own work, but `lib.rs:45` now carries the registration. I did not correct it because it is a historical statement about that work and spans a line break.
- The native reader claims (reader+0x10 on truncation, reader+0x11 on NaN, `processor+0x194`, `racer+0x161c`, etc.) were not re-checked against the pinned export. The client-side note `notes/Native Map/Shards/S0361 00b9a660-00ba0260.md:381` describes `00b9fc80` as a parser with a different-looking field summary; I did not reconcile it.
- The `lab/reports/kart-progress-native-codec-20261009T1622Z/` log paths lie outside the repo and were not checked.
- The cross-link `../Design/MMO Worker Contract` was not opened.
- The `kart_racing` "14 tests" and the focused-sweep counts were taken from `notes/Autopilot` reports, not re-run.
