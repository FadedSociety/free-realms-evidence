<!-- fleet job=test-audit id=tests-kart-entry-rs-L1 status=done turns=6 usd=0.0085 tokens(read,write,in,out)=[91401, 28877, 14, 7898] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/kart_entry.rs lines 1-879 of 879

Window reviewed: `prototype/osfr-tools/tests/kart_entry.rs` lines 1-879, with the code under test in `prototype/osfr-tools/src/kart_entry.rs` (`on_register` 650-687, `scene_frame` 588-594, `open` 597-618, `RaceEntryContent` 186-199).

- **[high] prototype/osfr-tools/tests/kart_entry.rs:327 register_emits_the_ordered_start_bundle - the 33/5 check cannot see the client_data echo, because the fixture makes the echo a no-op.**
  - Why it cannot catch a regression: `on_register` overwrites `client_data[77..81]` and `[81..85]` with `register.word_8` and `word_12` (src/kart_entry.rs:676-677). The fixture sets those bytes to `0x2a6ac44a` and `1` (test lines 98-99), and `register_payload` sends the same values (lines 125-126). So the test's `content.client_data.as_slice()` equals the output whether the handler echoes the register words, writes them swapped, or drops the overwrite entirely. Deleting lines 676-677 keeps this test green.
  - Fix: in this test, send a register with distinct words (for example `word_8 = 0x1111_2222`, `word_12 = 3`). Then assert that `frames[3]` payload bytes `77..81` equal `0x1111_2222` LE and `81..85` equal `3` LE, and that bytes `0..77` equal the content. Add a comment tying this to the "local player's registration" rule.

- **[medium] prototype/osfr-tools/tests/kart_entry.rs:315-334 register_emits_the_ordered_start_bundle - the expected bytes come from the same encoders the handler calls.**
  - Why it cannot catch a regression: `content.race_config.encode()`, `content.entry_vehicles[i].encode()`, and `kart_progress_native::encode_progress` (src lines 667, 670, 682) are the code under test. A change inside any of those encoders changes both sides and still passes. Only the order and the subtype labels are independently pinned.
  - Fix: add independent layout canaries, such as the config payload length `4 * RACE_CONFIG_WORDS`, the vehicle payload's leading u32 equal to `body_asset.len()`, and the progress payload length. Alternatively, compare against the captured frames in the ignored private test.

- **[medium] prototype/osfr-tools/tests/kart_entry.rs:661-668 private_content_package_format_round_trips_and_is_strict - "drives the same ordered bundle" is not asserted, so two identical refusals would pass.**
  - Why it cannot catch a regression: the test only checks `derived.handle_inner(&frame) == packaged.handle_inner(&frame)`. If both handlers return the same `Refused(...)`, the equality holds. A regression that refuses every register (or breaks the bundle for both paths identically) still passes.
  - Fix: take `replies(&outcome)` for both handlers and assert `subtypes(...)` equals the five-entry ordered list, then compare the reply vectors.

- **[medium] prototype/osfr-tools/tests/kart_entry.rs:742-751 private_capture_reencodes_the_full_entry_bundle - the comment says the encounter and instance are "read from the captured 41/114 body, not invented here", but the code falls back to invented constants.**
  - Why it cannot catch a regression: if the 41/114 file is missing or short, `.ok()` swallows the error and the match at 748 uses `(917_566, 1008)`. The `assert_ne!(..., 0)` checks at 750-751 cannot fail on those values. A bug that makes the wrong encounter or instance reach `RaceEntryContext` is not caught on a machine where that file is absent. This only runs with the capture present, which is the case where the claim matters.
  - Fix: when `OSFR_KART_ENTRY_CAPTURE` is set, `expect` the 41/114 file and require `len >= 19`. Either drop the fallback or pin the constants and assert equality against them, not just non-zero.

- **[low] prototype/osfr-tools/tests/kart_entry.rs:447-459 scene_frame_preserves_rotation_w_zero_through_the_zone_codec - the digest comparison restates the computation.**
  - Why it cannot catch a regression: `scene_frame` is `zone_transition::encode(&context.scene)` (src line 593), so `digest(&frame) == digest(&zone_transition::encode(&recovered_scene()))` only checks that the handler calls the codec. The byte-level checks at 454-455 are the meaningful part. Line 451 repeats line 450.
  - Fix: keep 454-455 and remove the digest check, or keep the digest only as a pinned SHA of the expected frame bytes rather than a value recomputed by the same codec.

Not reported: the other tests' names match their bodies (for example, the state and phase checks in the refusal tests), and the ignored capture test has a stated reason and a real fixture gate. Line 651 (`is_ok()` after a successful round-trip) is redundant but harmless.
