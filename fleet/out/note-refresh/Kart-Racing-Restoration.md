<!-- fleet job=note-refresh id=Kart-Racing-Restoration status=no_submit turns=13 usd=0.0169 tokens(read,write,in,out)=[336145, 49106, 28, 14766] model=claude-haiku-5-5 -->
# notes/Research/Kart Racing Restoration.md

**Verdict:** Minor-to-moderate drift. The wire schema, the contract table and the speedway/identity data still match the code. The integration status, the test counts and the native-gates list are out of date, because `kart_lobby_native.rs`, `kart_progress_native.rs` and `kart_entry.rs` now decode parts of the gates the note lists as open.

**Corrections:**

1. `old:` The module is not registered in `src/lib.rs` (a shared file); the test target compiles the exact source with `#[path = "../src/kart_racing.rs"]`. Lead integration step: add `pub mod kart_racing;` to `src/lib.rs` and drop that include.
   `new:` The module is registered in `src/lib.rs` (`pub mod kart_racing;`); the two test targets import it as `osfr_tools::kart_racing`, with no `#[path]` include. The lead integration step is done.
   `why:` repo:prototype/osfr-tools/src/lib.rs:46; repo:prototype/osfr-tools/tests/kart_racing.rs:8-14; repo:prototype/osfr-tools/tests/kart_review.rs:9-14 (no `#[path]` in either file).

2. `old:` Builder tests: 13 cases; repaired contract (flags, clock, names, snapshots, reward authority)
   `new:` Builder tests: 9 cases; repaired contract (flags, clock, names, snapshots, reward authority)
   `why:` repo:prototype/osfr-tools/tests/kart_racing.rs has 9 `#[test]` functions (lines 96, 124, 155, 209, 254, 282, 315, 350, 400).

3. `old:` Independent guard suite: 12 cases, written RED before the repair then GREEN
   `new:` Independent guard suite: 8 cases, written RED before the repair then GREEN
   `why:` repo:prototype/osfr-tools/tests/kart_review.rs has 8 `#[test]` functions (lines 111, 136, 162, 205, 243, 359, 397, 447).

4. `old:` 2. Opcode 102/2 lattice: the captured 2,393-byte lobby payload starts with a `u32` remaining-length field (2378), a six-row body (`37`/`3030` pair present in row 0) and further blocks; the community writer's bytes are a subset, not the native framing, and must not be sent as a live 102/2 response. The full original catalogue framing is open.
   `new:` 2. Opcode 102/2 lattice: the captured 2,393-byte lobby payload starts with a `u32` remaining-length field (2378), a six-row body (`37`/`3030` pair present in row 0) and further blocks; the community writer's bytes are a subset, not the native framing, and must not be sent as a live 102/2 response. The native framing and five-table body are decoded in `kart_lobby_native.rs` (counts `[6, 30, 43, 37, 17]`); the meaning of the options, values, display and settings fields, and whether the client tolerates trailing bytes, remain open.
   `why:` repo:prototype/osfr-tools/src/kart_lobby_native.rs:1-30 (framing, five tables, capture counts, trailing-byte policy).

5. `old:` 1. Subtype-to-class mapping: the native class names are recovered, the concrete subtype numbers each class serialises are not.
   `new:` 1. Subtype-to-class mapping: the native class names are recovered; concrete subtype numbers are mapped for 1, 12 and 14 (`kart_progress_native.rs`) and for the entry exchange 1, 2, 3, 4, 5, 9, 11, 14 and 34 (`kart_entry.rs`). The remaining subtypes are unmapped.
   `why:` repo:prototype/osfr-tools/src/kart_progress_native.rs:44-49 (`GAME_STATE_SUBTYPE`, `PROGRESS_SUBTYPE`, `DESTROY_RACER_SUBTYPE`); repo:prototype/osfr-tools/src/kart_entry.rs:5-19 (33/9, 33/34, 33/11, 33/5, 33/14, 33/2, 33/3, 33/1, 33/4).

6. `old:` 5. Bulk stream layout (subtypes 5/6/14): open; positions stay non-authoritative.
   `new:` 5. Bulk stream layout: subtype 14 (73-byte progress block) is decoded in `kart_progress_native.rs`; subtypes 5/6 (85-byte racer state) stay open and positions stay non-authoritative.
   `why:` repo:prototype/osfr-tools/src/kart_progress_native.rs:5-9 (`u64` guid, slot, floats, laps, lap limit, best lap, total time).

7. `old:` The float layout of subtypes 5/6/14 is **not** decoded here, so no position is trusted (see below).
   `new:` The float layout of subtype 14 is decoded in `kart_progress_native.rs`; subtypes 5/6 are **not** decoded, so no client position is trusted (see below).
   `why:` repo:prototype/osfr-tools/src/kart_progress_native.rs:5-9 and 29-32 (`unknown_0c`/`unknown_10` remain positional, so the decode is partial).

**Unsure:**

- **Reward pricing (gates 4 and 6).** The note says reward numbers are open and the module refuses to price. That still holds for `kart_racing.rs` (`Unpriced` unless `TrackLayout.reward` is `Some`, repo:prototype/osfr-tools/src/kart_racing.rs:33-40, 594, 711). But `kart_rewards.rs` now has a registration seam with labelled starter prices (`RECONSTRUCTED`, repo:prototype/osfr-tools/src/kart_rewards.rs:40-42, 56-74), and `kart_gateway.rs:738` checks `reward_priced()`. The note does not mention this. I did not change gates 4 or 6 because their claims about original numbers still hold.
- **Test counts in the verification table.** The logged runs ("kart_racing 13 passed / kart_review 12 passed", "11 of 11 pass") are historical and may have been taken on a different tree. I did not correct them, because the logs are not in the repo. The tip has 9 and 8 `#[test]` functions.
- **Reconstructed gate route.** MODLOG.md:594 mentions a reconstructed 93-gate, three-lap route with oriented gate bands. I did not check that code path, so I left gate 3 ("concrete numbers are open") unchanged.
- **`../lab/...` paths** in the note point outside the repo. I could not check them.
