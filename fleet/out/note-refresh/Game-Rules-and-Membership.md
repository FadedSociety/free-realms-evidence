<!-- fleet job=note-refresh id=Game-Rules-and-Membership status=done turns=11 usd=0.0139 tokens(read,write,in,out)=[224896, 43613, 24, 12336] model=claude-haiku-5-5 -->
# notes/Research/Game Rules and Membership.md

**Verdict:** minor drift. The client-fact and policy sections hold against the code at the tip. The wiring and test-layout statements are stale: they describe steps that have since been done, and one test-file claim is now false. Two path:line citations have moved.

**Corrections:**

1. `old:` `direct `#[path]` include so shared `lib.rs` stays untouched;`
   `new:` `imports the library module `osfr_tools::game_rules` directly (the earlier `#[path]` copies were removed);`
   `why:` `prototype/osfr-tools/tests/game_rules.rs:1-7` begins with `use osfr_tools::game_rules::{...}`; `notes/Research/Integration Round 4.md:11` records that the test-only `#[path]` copies were removed.

2. `old:` `2. Add the one-line module registration `pub mod game_rules;` to `src/lib.rs` in a lead-owned integration change; this task does not edit shared module registration.`
   `new:` `2. Module registration is done: `pub mod game_rules;` is at `src/lib.rs:24`.`
   `why:` `prototype/osfr-tools/src/lib.rs:24` (`pub mod game_rules;`, in the public module list).

3. `old:` `1. Map trusted `AccountFlags.membership` from `src/account.rs` / `src/account_store.rs` to `MembershipState`; do not derive it from self-data `membership_status=1` without evidence. Choose where account configuration overrides the R member default.`
   `new:` `1. Trusted `AccountFlags.membership` is already mapped to `MembershipState` at character load (`osfr-gateway.rs:1167-1170`, `account.flags.membership`), and the account-info callback is built from it (`login.rs:620-624`). Do not derive it from self-data `membership_status=1` without evidence. The R member default is still not configurable beyond the stored account flag.`
   `why:` `prototype/osfr-tools/src/bin/osfr-gateway.rs:1167-1170`; `prototype/osfr-tools/src/login.rs:620-624`; `prototype/osfr-tools/src/account.rs:20` (`pub membership: bool`).

4. `old:` `Existing warning: `housing.rs:567` dead-code method `instance_index`.`
   `new:` `At the time of that run the build printed a dead-code warning for `instance_index`; that citation no longer resolves (`housing.rs:567` is now `struct Lot`, and no `instance_index` method exists in `housing.rs`).`
   `why:` `prototype/osfr-tools/src/housing.rs:567` (`#[derive(Debug)] struct Lot`); a search of `prototype/osfr-tools/src` finds no `fn instance_index` in housing.rs.

5. `old:` `(`parse_self` around 1069-1082; `build_self` around 1194-1205)`
   `new:` `(`parse_self` account block around 1069-1084; `build_self` account block around 1190-1206)`
   `why:` `prototype/osfr-tools/src/startup_selfdata.rs:1069-1084` (`let account = AccountState {...}`) and `:1190-1206` (`put_u8(... underage)` through `active_vehicle_loadouts`). The field order the note describes is correct.

**Unsure:**

- The note describes `GameRuleSet::may` as the single policy entry point. Its only callers in `src` are inside `game_rules.rs` (`src/game_rules.rs:175`). Quest limits are read directly from the policy (`src/gameplay/npc_quests.rs:123-128`), and the account callback uses `account_info_callback_bytes` (`login.rs:624`). The note does not claim `may` has runtime callers, so I left it alone. Its wiring list (step 4) does say the gates are still to be passed in, which matches the code.
- The coin shop still takes membership from its caller (`src/coin_shop.rs:532`), not from `GameRuleSet`. The note's "not wired" framing is consistent with that.
- The membership encoders `encode_membership_activation` and `encode_membership_service_flags` have no callers outside `game_rules.rs`. That matches the note's statement that `startup_messages.rs` has no membership builder.
- I did not re-verify the native client addresses (`00719330`, `009471a0`, `014a6720`, and the rest). They are client-side and outside this repo's tip.
- The test totals (7 passed, 1 ignored) match the test file: seven `#[test]` functions run by default, and one `#[ignore]`d.
