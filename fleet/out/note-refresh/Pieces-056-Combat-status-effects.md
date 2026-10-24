<!-- fleet job=note-refresh id=Pieces-056-Combat-status-effects status=done turns=12 usd=0.0164 tokens(read,write,in,out)=[331927, 53120, 26, 12813] model=claude-haiku-5-5 -->
# notes/Research/Pieces/056 Combat status effects.md

**Verdict:** Moderately stale. Every path, byte size, packet id, captured-row value and the `MAX_EFFECT_SECONDS` bound still match the tip. The integration status is wrong: the module is no longer test-only, and the live library already uses its codec.

**Corrections:**

1. `old:` the module is not
  registered in `src/lib.rs`, which the lead owns).
   `new:` the codec is compiled into the library through `abilities.rs` (`#[path = "restoration/piece_056.rs"] mod effect_packets;`, inside `pub mod abilities`), which the lead owns).
   `why:` repo:prototype/osfr-tools/src/abilities.rs:15-16; repo:prototype/osfr-tools/src/lib.rs:3

2. `old:` Lead integration: the module is only reachable through its own test target. Registering
   `new:` Lead integration: the codec is reachable from the live library. `abilities.rs` calls it at lines 745, 929-954 (`encode_remove_effect_tag`, `EffectTagPayload`, `encode_add_effect_tag`), and `encounter/power_up_use.rs:140` calls `build_effect_tag`. The `StatusLedger` has no callers outside its own tests. Registering
   `why:` repo:prototype/osfr-tools/src/abilities.rs:745, 929-954; repo:prototype/osfr-tools/src/encounter/power_up_use.rs:140; a grep for `StatusLedger` finds only `src/restoration/piece_056.rs` and `tests/piece_056.rs`

3. `old:` `piece_056` under `src/restoration/`/`lib.rs` and routing encounter combat through the ledger is the lead's call
   `new:` routing encounter combat through the `StatusLedger` (not just the wire codec) is the lead's call
   `why:` the module is already registered via `abilities.rs:15-16`; only the codec is wired (see correction 2)

4. `old:` Historical fidelity gaps: no server-side apply/stack/immunity/cleanse logic, no table for the
   `new:` Historical fidelity gaps: no server-side immunity/cleanse logic. Live apply exists but is separate from the ledger: `abilities.rs` refreshes by definition id (`abilities.rs:718-727`), and `encounter/power_up_use.rs` applies caster buffs (`power_up_use.rs:128-145`). No table for the
   `why:` repo:prototype/osfr-tools/src/abilities.rs:705-727; repo:prototype/osfr-tools/src/encounter/power_up_use.rs:128-145

5. `old:` 18 stdlib tests over the preserved corpus.
   `new:` 17 stdlib test methods over the preserved corpus.
   `why:` repo:tests/pieces/test_piece_056.py has 17 `def test_` methods (lines 107-252). The "18 tests OK" line in the Commands section is a historical run record, so I left it alone (see Unsure).

**Checked and current (no change):**
- `src/restoration/piece_056.rs` and `tests/piece_056.rs` exist. The test file includes the module via `#[path]` (line 32-34) and has 16 `#[test]` functions.
- `scripts/pieces/piece_056.py` and `tests/pieces/test_piece_056.py` exist.
- Wire sizes match the code: 93 / 8 / 36 / 16 / 16 bytes (`ADD_EFFECT_TAG_LEN`, `REMOVE_EFFECT_TAG_LEN`, etc.); 72 + 13 = 85 (`CLIENT_EFFECT_TAG_LEN`).
- `MAX_EFFECT_SECONDS` = 86 400 and `FIRST_TAG_ID` = 1 (`piece_056.rs:84-86`).
- Captured row values in `captured_coin_boost()` (`piece_056.rs:272-295`): unknown_2 495, duration 3600, unknown_10/11 142556/3978, icon 7334, name 4270.
- `restore`, `profile_rows`, `disconnect_clear` and the immunity refusal before any row or packet (`piece_056.rs:455-462`, `539-592`).

**Unsure:**
- The Python test count (17 by grep, against the note's 18) could also reflect a run before a test was removed. The historical "18 tests OK" line is unverified; I did not run the suite.
- Whether the "Coin Boost" icon and locale checks hold depends on the private lab corpus (`lab/`), which I could not read. The same applies to the ClientPcData and packet-id claims that cite `decompiled/`.
- Lines 8 and 116 are the only spots where the note calls the module unregistered or test-only. I did not check whether `abilities.rs` is the only integration point or whether other encounter code now routes status through it.
