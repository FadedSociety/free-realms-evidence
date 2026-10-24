<!-- fleet job=test-audit id=tests-field-camps-high-band-rs-L1 status=done turns=5 usd=0.0078 tokens(read,write,in,out)=[57263, 32250, 12, 6297] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/field_camps_high_band.rs lines 1-937 of 937

Window reviewed: `prototype/osfr-tools/tests/field_camps_high_band.rs` lines 1-937 (whole file). No `#[ignore]` and no early-return fixture skips in the window. Most tests pin rows by digest or compare against the named W102 row, and the kill/payout tests check exact packets and bank state, so they are sound. The findings below are the exceptions.

- **[medium] tests/field_camps_high_band.rs:715 `an_unclaimed_high_camp_credit_expires_or_is_lost_on_leaving_and_pays_nothing` - the body never shows that B held a credit before the TTL, and never exercises leaving; it only checks that nothing is paid after expiry.**
  - Why it cannot catch a regression: if the shared-kill path never credits a non-killer (B), then B's `tick_shared_effects` at `killed_at + CREDIT_TTL_MS + 1` (lines 740-744) and the later tick (745-749) also pay nothing, and the test still passes. The "lost on leaving" half of the name has no code at all: no logout, zone change or leave call appears between lines 715 and 750.
  - Fix: after the kill, add a positive control in the style of the test at 752: call `b.tick_shared_effects(..., killed_at + 50)` and assert 18 coins and the 38/19 packet for B. Then run a second scenario that expires the credit and asserts nothing is paid. For the leaving case, either call the production leave/logout path and assert no payout, or rename the test to drop "lost on leaving".

- **[low] tests/field_camps_high_band.rs:876 `a_malformed_high_camp_or_band_is_refused_atomically` - the band half of the name claims atomicity, but lines 931-936 only check that a fresh `EncounterEngine::load` returns Err and then Ok.**
  - Why it cannot catch a regression: no live engine state is captured or compared around the band refusal, so a loader that partly applies the band before failing would still pass. The atomicity check exists only for the field mutations at lines 911-929.
  - Fix: either rename the band half to "refused at load" or capture a live observable before and after a malformed band load (for example, the `engine.field_teleport_targets()` and the payout from `RewardFixture` for HIGH_SHAMAN_14), and assert it is unchanged.

- **[low] tests/field_camps_high_band.rs:287-296 and 449-458 (also 314-315 `areas.len() == 30`, `guids.len() == 34`) - exact actor and group counts are repeated in three tests, and they pin totals that unrelated content work changes.**
  - Why it cannot catch a regression: it is churn, not a missed bug. Adding one unrelated field actor or spawn group fails four asserts in two tests, even though the tests are about the HIGH camps or the existing rows.
  - Fix: assert that the HIGH and pre-T296 rows exist at their known positions (the `take`/`skip` checks already do this), and drop the total-length pins or keep only one of them in the file with a comment that says why it is pinned.
