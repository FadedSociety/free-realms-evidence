<!-- fleet job=bug-hunt id=src-rewards-rs-L1 status=nothing_found turns=8 usd=0.0102 tokens(read,write,in,out)=[125054, 34779, 18, 9201] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/rewards.rs lines 1-250 of 250

Reviewed `prototype/osfr-tools/src/rewards.rs` lines 1-250 in full and read the callers and helpers they depend on (`inventory.rs` `grant_coins` 859-873 and `grant_with_tint` 962-1010, `progression_extras.rs` `validate_reward_rows` 58-68 and `apply_award` 70-77, `gameplay/derby_session.rs` `pay_derby_completion` 198-217, `encounter.rs` `prize_bundle` 596-618). No finding I could tie to a line and show as a defect.

Checked and cleared:

- **Atomicity (`apply_grant` 93-173):** all mutation goes to a clone (`next`). Every `?` / `return Err` after that point discards `next`, so the caller's state is untouched on refusal. The idempotent early return (104-106) changes nothing.
- **Integer overflow:** XP totals use `checked_add` (115-119, 141-143). The `coins` / `stars` / `row_count` conversions to i32 are checked (120-123). `experience_packets` (175-197) cannot overflow: `updated / 100` is at most about 4.3e7 for a u32, and `.min(20)` runs before the `as i32` cast. `grant_with_tint` (inventory.rs 1003-1006) bounds the stack count with `checked_add` and `fits_one_stack`.
- **Client input:** `grant_key` length and trim are checked (98-103). Client-sourced profile ids and item ids are checked for locked profiles (111, 86) and for `definition_id > 0` and `has_definition` (148-153). Quantity is bounded by `grant_with_tint` (972). The callers I read (`progression_extras.rs:308`, `derby_session.rs:203-214`) build grants from server content or server state, not from packet fields.
- **Panics:** no indexing or unwrap on packet data in this window. `encode_display_bundle` (199-239) bounds rows by `supported_entry` and a minimum body length, and its capacity sum is checked.
- **Logic:** the locked-profile rule in `locked_job_profile` (84-89) matches the check in `apply_grant` (111). Zero-amount XP entries are skipped consistently in both the check and the loop.

One candidate dropped: the doc comment at lines 28-29 says a successful Item/Chest bundle "requires the entry-specific trailing u32", but `encode_display_bundle` does not enforce it. I could not confirm which type ids are Item/Chest or what that trailing field is. `encounter.rs:596-618` builds Item entries as 34-byte bodies with a single trailing i32 at the bundle end, so the doc and the code may just be describing the same thing differently. The only triggers are server-authored content rows, not client bytes, so I did not report it.
