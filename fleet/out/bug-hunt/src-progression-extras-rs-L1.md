<!-- fleet job=bug-hunt id=src-progression-extras-rs-L1 status=nothing_found turns=12 usd=0.0173 tokens(read,write,in,out)=[348929, 47113, 26, 15747] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/progression_extras.rs lines 1-800 of 1686

No reportable defects in `prototype/osfr-tools/src/progression_extras.rs` lines 1-800 after reading the window and its callers.

Checked and ruled out:
- **Panics:** `achievement_claim_id` (line 381) slices a 32-byte SHA-256 digest, so `[..8]` cannot go out of range. The f32 progress division (line 766) cannot divide by zero, because `AchievementProgression::new` (line 602) rejects `threshold == 0`.
- **Client-controlled counters:** the only production caller of `observe` is `gameplay/progression.rs:101`, which feeds server-derived absolute counters from `achievement_counters()`. `on_event` has no production caller. Amounts and counters are bounded by `MAX_COUNTER`.
- **Atomicity:** `advance` (lines 675-729) stages everything and assigns `self.state` only on success. `apply_award` errors propagate before any commit. `CollectionProgression::collect` (lines 515-562) commits `self.ledger` only after the reward step succeeds. The caller in `gameplay/progression.rs:83-126` stages the whole completion before committing.
- **Reward validation:** `validate_reward_rows` (line 58) checks the forbidden and supported type lists correctly, and both lists have the stated lengths. `apply_grant` in `rewards.rs` already covers bag capacity, locked profiles and XP/coin overflow. Reward rows are server-authored (`gameplay/npc.rs:1394`, empty rows for achievements), so the missing trailing-u32 check in `validate_reward_rows` is not reachable from a client.
- **Logic:** the `observe` skip condition (lines 662-663) and the completed-rule handling in `on_event` and `advance` match their doc comments. Dropped progress packets in `gameplay/progression.rs` are intentional: `soccer_entry.rs:713-719` asserts that progress-only gains emit no packet.
- **Content loading:** unmatched `title_names` are silently skipped in `load` (line 297). I checked the sample in `achievements.json:581` against `titles.json` and it matches, and the content is server-authored, so this is not a client-reachable defect.
- **Minor, unreachable:** `collect` (line 536) maps a negative `collection_id` to 0 via `unwrap_or(0)`. Catalogue ids are server content, and `collect` has no production caller.
