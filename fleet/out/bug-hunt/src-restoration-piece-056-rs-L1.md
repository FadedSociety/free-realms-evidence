<!-- fleet job=bug-hunt id=src-restoration-piece-056-rs-L1 status=done turns=6 usd=0.0099 tokens(read,write,in,out)=[96583, 34202, 14, 9413] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_056.rs lines 1-800 of 969

Window reviewed: `piece_056.rs` lines 1-800 (plus 800-930 for the payload reader and `check`). Three latent defects in the restore/profile path. None is reachable from a live client packet today: a search of `src/` finds no caller of `StatusLedger::restore`, `StatusLedger::profile_rows` or `decode_profile_rows` outside this file (`abilities.rs` only pulls the module in with `#[path]`, and the tests call it directly). Severities are therefore set for the day the path is wired to the profile/save loader, which the module's own doc (lines 56-57, 319-321 of the test file) says is pending.

- **[medium] `prototype/osfr-tools/src/restoration/piece_056.rs:563-568` - `restore` does unchecked i32 subtraction on a stored duration and never bounds it, so a hostile stored row can overflow or become a near-permanent buff.**
  - Failure scenario: a stored/profile row carries `unknown_7 = i32::MIN` (or any huge value). With `downtime_seconds = 1`, `stored - 1` overflows. A debug build panics; a release build wraps to `i32::MAX`, so the row is restored with about 68 years left. `restore` does not apply the `MAX_EFFECT_SECONDS` (86 400) check that `apply` enforces at line 463, so even `stored = i32::MAX` with zero downtime is accepted and re-broadcast. `profile_rows` then persists that duration forever.
  - Reach: `decode_profile_rows` (780-807) takes any i32 duration from the wire (`read_payload`, line 805), then `restore` (555-568) with no range check on the row. Nothing upstream prevents it once the loader calls these.
  - Fix: use `stored.saturating_sub(downtime_seconds.max(0))` and skip or reject rows where `stored <= 0 || stored > MAX_EFFECT_SECONDS`. Apply the same `definition_id > 0` and `icon != 0 ⇒ name_id > 0` checks that `apply` (lines 466-471) makes.

- **[medium] `prototype/osfr-tools/src/restoration/piece_056.rs:598-600` (with 577 and 594-604) - `allocate` loops forever once `next_tag_id` reaches an id that is already active at `i32::MAX`, because `saturating_add` never moves past `i32::MAX`.**
  - Failure scenario: a profile row with `tag_id = i32::MAX` (accepted at line 805 and inserted at line 579) sets `next_tag_id = max(.., i32::MAX.saturating_add(1)) = i32::MAX` (line 577). The next `apply` calls `allocate`; `contains_key(i32::MAX)` is true, `saturating_add` keeps the value at `i32::MAX`, and the `while` never exits. The server thread hangs.
  - Reach: `decode_profile_rows` → `restore` (line 577 sets the allocator, line 579 inserts the id) → `apply` → `allocate`. No range check on restored ids.
  - Fix: reject restored ids `<= 0` or `== i32::MAX`, or make `allocate` return an error when the id space is exhausted (for example, `checked_add` and a bounded scan).

- **[low] `prototype/osfr-tools/src/restoration/piece_056.rs:569-579` - `restore` silently overwrites a row when the input repeats a tag id, but still emits an add packet for each copy, so the earlier row is lost from the ledger and the client is left with two rows under one id.**
  - Failure scenario: `rows = [(7, A), (7, B)]`. Both pass the length checks. The second `BTreeMap::insert` replaces A, `packets` holds two AddEffectTag packets for id 7, and A's later removal is impossible because the ledger no longer knows it.
  - Reach: the same profile-row loader as above, with a duplicate id in the payload.
  - Fix: track seen ids in `restore` and return an error (or skip) on a duplicate, before extending `packets`.
