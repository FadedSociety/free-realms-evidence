<!-- fleet job=test-audit id=tests-profiles-rs-L1 status=done turns=5 usd=0.0069 tokens(read,write,in,out)=[50419, 22913, 12, 7124] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/profiles.rs lines 1-479 of 479

Window: `prototype/osfr-tools/tests/profiles.rs` lines 1-479. Read in full, plus `src/profiles.rs` 315-440, `src/inventory.rs` 1305-1330, and `src/gateway.rs` 1249-1262.

- **[medium] prototype/osfr-tools/tests/profiles.rs:275-284 gender_and_class_splices_preserve_unowned_bytes_and_reject_unproved_input - the "preserves" round trip runs on a fixture that is already in canonical form, so the patch steps are no-ops.**
  - Why it cannot catch a regression: the fixture template has active = 1, and the progression bytes at each profile's rank offset are `[1,0,0]`, which is what `progression_bytes(1)` produces at xp 0 (`profiles.rs:365-376`). `patch_gender` only touches the trailing gender word. So `profiles.patch_self(&template)` (`profiles.rs:379-407`) and `inventory.initialization_patch(...)` (`inventory.rs:1305-1330`) would both return their input unchanged, and `assert_eq!(patched, template)` at line 284 would still pass. Making `patch_self` a no-op, or having `initialization_patch` skip splicing, passes this test. Line 285 (`signed(&patched, f.active) == 1`) is also already true of the input.
  - Fix: start from a template that is not canonical, for example a fixture with `active` = 43 or with XP already added, and assert that `patch_self` changes the active word and rank bytes at the expected offsets. Also assert that the spliced equipment bytes differ from the input, or that the output differs from the input at the expected offsets.

- **[medium] prototype/osfr-tools/tests/profiles.rs:254-271 profile_proofs_and_field_bounds_reject_corruption - there is no positive control, so every `is_err()` could pass for an unrelated reason.**
  - Why it cannot catch a regression: the test never asserts that `Profiles::load(&f.path, None)` succeeds on the untouched `original` fixture. If the loader always errors (a schema break, a missing file, a JSON-shape change), all five `is_err()` checks still pass, and the test cannot tell a bounds check from any other failure. The `{field}` message is only printed on failure, and the test does not check which error came back.
  - Fix: first `assert!(Profiles::load(&f.path, None).is_ok())` on the original profiles.json. Then, for each corruption, match the specific error (for example `err.to_string().contains("truncated")` or the invalid-proof message) so that the failure is the intended check.

- **[low] prototype/osfr-tools/tests/profiles.rs:189-203 snapshot_rejects_unknown_locked_or_unsupported_classes - same missing positive control; four bare `is_err()` checks.**
  - Why it cannot catch a regression: if `Profiles::load` rejected every snapshot, all four assertions would pass. The test never confirms that the unmodified `f.load().state()` snapshot is accepted.
  - Fix: assert that the unmodified state loads with `is_ok()` first, and check each rejection's error text or variant.

- **[medium] prototype/osfr-tools/tests/profiles.rs:381-383 private_all_opening_starters_and_fresh_identity_survive_activation_and_restore (`#[ignore]` with a reason) - the gender patch is only checked for non-emptiness.**
  - Why it cannot catch a regression: the test name claims identity and activation survive, and the loop is labelled by gender. But `game.patch_gender(&template, gender)` and `patch_self` are checked only with `assert!(!patched.is_empty())`. A `patch_gender` that writes the wrong gender, or does nothing, still passes. The test is ignored, so it does not gate merges, which makes this a coverage gap for the private run rather than a silent skip.
  - Fix: after `patch_gender`, read the gender word at the same trailing offset the fixture uses (`signed(&bytes, bytes.len() - 4) == gender`) and assert that it equals the requested gender.

- **[low] prototype/osfr-tools/tests/profiles.rs:312 private_all_opening_starters_and_fresh_identity_survive_activation_and_restore - `inventory.state().items.len() == 7` pins an exact content count.**
  - Why it cannot catch a regression: this test is about starter activation and restore. Any unrelated change to the opening item list, such as adding a starter, breaks it without touching the behaviour under test.
  - Fix: assert that every `profiles.starter_items(id)` definition is present and equipped, and drop the exact count (or keep it in a fixture-shape test that is clearly about content).

No findings for the remaining tests. Specifically, `class_selection_without_class_content_is_refused_and_keeps_the_save` (lines 434-479) does check `state_changed`, empty replies, the snapshot equality, and a follow-up request. Its name and doc match the body.
