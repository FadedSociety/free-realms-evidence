<!-- fleet job=test-audit id=tests-warpstone-travel-rs-L1 status=done turns=5 usd=0.0127 tokens(read,write,in,out)=[75462, 38056, 12, 14402] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/warpstone_travel.rs lines 1-866 of 866

Window `prototype/osfr-tools/tests/warpstone_travel.rs` 1-866. Most tests here are sound: they pin server-side values, use negative controls, and check state. The findings below are the gaps I could confirm.

- **[medium] tests/warpstone_travel.rs:685 curated_rows_equal_the_captured_original_57 - the only test that ties the curated rows to the original client's `57` returns early and passes when the capture is absent.**
  - Why it cannot catch a regression: the path `../../../lab/captures/...` resolves outside the repo (the repo root holds no `lab/`). The `let Ok(frame) = std::fs::read(..) else { eprintln!; return; }` branch makes the test green. The `eprintln` is hidden unless tests run with `--nocapture`. Any drift in `curated_definitions()` then passes on the integrator. The doc comment at line 680 admits the skip, but the module doc (lines 11-12) presents this check as the evidence for the curated rows.
  - Fix: when `OSFR_REQUIRE_LAB` (or similar) is set, panic instead of returning. Or move the check into a fixture that is committed under `tests/fixtures`, so it always runs.

- **[medium] tests/warpstone_travel.rs:646 hostile_bodies_never_panic_or_move_anyone - the name says nothing moves, but the "no relocation" assertion only runs for non-exact lengths.**
  - Why it cannot catch a regression: for the exact lengths `(56,0)`, `(58,8)`, `(90,4)` and `(122,0)` (lines 658-664) the body is never checked for relocation or rejection. A change that lets an exact-length `58` or `90` with a fixed fill relocate would pass. The `122` zero-length call at line 652-668 actually relocates the character to Sanctuary on the first fill, and nothing asserts that or the outcome of the subsequent calls.
  - Fix: for the exact-length cases, assert the outcome explicitly: for `(90,4)` with fill `0x00` (id 0), `(58,8)`, and `(122,0)`, compare `relocation`/`rejection` against the expected values. Or narrow the test name to "malformed bodies never move anyone".

- **[low] tests/warpstone_travel.rs:547 safe_teleport_shares_the_travel_gates - no positive control, so a gate that refuses every request still passes.**
  - Why it cannot catch a regression: the loop only asserts `relocation.is_none()` for the three gated contexts. A `safe_teleport` that always returns `Err` passes. The unblocked path is exercised elsewhere (line 481), but this test is supposed to show the gates are what refuse, and it cannot.
  - Fix: add a fourth case `(0, None)` with the ground-level position, and assert `relocation.is_some()`. Use `rejection` for the refused cases so the reason, not just the absence of a move, is pinned.

- **[low] tests/warpstone_travel.rs:481 safe_teleport_goes_to_the_nearest_warpstone_and_takes_no_position - the name claims "nearest warpstone", but only `relocation.position[0]` (x) is checked.**
  - Why it cannot catch a regression: a change to `nearest_warpstone` that picks another destination with the same x, or that returns a wrong y/z for Lakeshore, still passes (`piece_077.rs:1218-1227` checks only the planar distance and never the arrival y/z).
  - Fix: `assert_eq!(relocation.position, [-733.9340209960938, 9.086000442504883, 945.948974609375])`, the captured Lakeshore spawn already used at line 235. Or compare the full array against `arrive_at_destination`'s expected output.

- **[low] tests/warpstone_travel.rs:447 attunement_survives_a_relog_and_a_save_cannot_unlock_other_ids - pins the exact serialized JSON `{"attuned":[5,9]}`, which the relog claim does not need.**
  - Why it cannot catch a regression: it is not a regression check on relog. It is churn: any harmless change to the save format (field order, a version key, a different set container) fails this test while the relog behaviour is unchanged. This is the over-pinned category.
  - Fix: round-trip the value (`serde_json::from_str::<WarpState>(&json)` and compare `state()`), and keep only the `deny_unknown_fields` assertion at line 475 as the format check.
