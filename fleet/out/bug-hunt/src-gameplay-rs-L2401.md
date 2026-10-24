<!-- fleet job=bug-hunt id=src-gameplay-rs-L2401 status=done turns=30 usd=0.0404 tokens(read,write,in,out)=[1455245, 78707, 62, 32099] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay.rs lines 2401-3200 of 5475

Window `gameplay.rs:2401-3200` read in full, plus the callers and helpers it depends on. No high or medium defect found. Two low-severity findings, both confined to the developer `realm` console, which only Admin accounts can reach.

**Ruled out (checked, not defects):**
- Gathering-node packet slice `inner[4..12]` (2499) is guarded by `inner.len() < 12`.
- Kart `exit().unwrap()` (2681) and `kart_entry.unwrap()` (2662, 2673) are guarded by `active` and the caller's `is_some()`.
- Kart claim (2698) and `changed_for_save` (2702): a paid claim sets `last_paid_unix`, so the save is flagged.
- Fishing `adopt_reward_state` (2640) and the swallowed `route` error (2604-2610): the gateway stages each in-world event (`gateway.rs:1656`, `1725`) and drops the staged clone on `Err`, so partial mutation does not persist.
- Developer commands: `may_run` (`gameplay.rs:3661`) plus `can_run_realm_command` (`account_store.rs:52`) keep Player accounts out, so client input cannot reach them.
- `realm goto` float parsing has finite checks in `dev_teleport.rs:368`.

**[low] gameplay.rs:2946-2947 and 2956-2957 - the reply reports the unclamped amount, not the amount granted.**
- Failure scenario: an Admin types `realm give 2884 5000`. The code grants `count.clamp(1, 999)` = 999 but says "Gave 5000 x item 2884." `realm coins 5000000` grants 1,000,000 but says "Gave 5000000 coins." `realm give 2884 0` grants 1 and says "Gave 0 x item 2884."
- Reach: `realm` chat → `handle_in_world_inner` → `developer_cheat` (`gameplay.rs:4330`), gated by `may_run` (`gameplay.rs:3661`), which allows only Admin for `give` and `coins`.
- Fix: format the clamped value. Bind `let granted = count.clamp(1, 999);` and use `granted` in both the grant and the message. Do the same with `coins.min(1_000_000)` for the coin reply.

**[low] gameplay.rs:2905, 2975 (and 3027 in `simulate_battle`) - `unwrap()` on optional engine or profile state in developer commands.**
- Failure scenario: an Admin runs `realm level 5` on a build with no profile content, so `self.profiles` is `None`. Line 2905 panics. Similarly `realm win` with no encounter engine panics at 2975 (`self.encounter.as_mut().unwrap().debug_win(...)`). The neighbouring `heal`/`god` arms guard with `if let` / `is_some_and`, so this is inconsistent. `realm sim` panics at 3027.
- Reach: only Admin-role accounts (or `--dev-tools` with Admin) can reach these arms. The panic is not client-packet-driven. I did not verify whether the gateway's `catch_unwind` (`osfr-gateway.rs:4481`) turns it into a per-request error or tears down the connection.
- Fix: replace each `unwrap()` with `let Some(..) = .. else { say(out, "...not available...") ; return Ok(true) }`, matching the `heal`/`god` arms.
