<!-- fleet job=bug-verify id=src-encounter-rs-L801-f1 status=done turns=19 usd=0.0175 tokens(read,write,in,out)=[442392, 42073, 40, 15710] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/encounter.rs:825

**Verdict:** refuted as stated. The claimed trigger (disconnect, then `reset_session`, then `bind_run_instance(0)`) cannot happen in production. A narrower path to the same write exists, but it is low severity and not remotely reachable. I did not run it.

**Severity if confirmed:** low (for the narrow path only). The claimed medium/remote scenario does not hold.

**Evidence:**

1. **The code is in the real server.** `encounter` and `gateway` are `pub mod` in `src/lib.rs:19,27`, and `osfr-gateway.rs` calls them. The `bind_run_instance` guard at encounter.rs:825 (`instance < 0`) and the `load()` check at encounter.rs:1041 (`a.instance_id <= 0`) match the claim.

2. **The claimed disconnect trigger is test-only.** `Gateway::reset_session` (gateway.rs:1382-1383 sets `logged_in = false`) has one caller, `f160_field_views.rs:35` (`test_lose_world`). That file is included only under `#[cfg(test)]` (osfr-gateway.rs:4537-4539). In production, `logged_in` is set `true` at `Event::Login` (gateway.rs:1452, 1814) and never cleared. A disconnected session that was logged in still takes the `is_logged_in()` branch (osfr-gateway.rs:1748), so `change` is `Some` and `instance` comes from `change.instance_id()`, not the `unwrap_or(0)` fallback at 1786.

3. **The 0 can only come from a pre-login session.** Trace the path that does reach 0:
   - `from_world(zone, 0)` and `world_instance_id()` both accept 0 (players.rs:32-39), so 0 is not rejected there.
   - Before login, `change` is `None`, and `old_instance` is `None` because membership is committed only inside `if let Some(change)` (osfr-gateway.rs:1954-1956). So `instance = 0` at 1786 and `bind_run_instance(0, …)` runs at 1790.
   - The saved encounter state is loaded before login (osfr-gateway.rs:936-946), so an active encounter can exist.
   - A non-login message is needed. Pre-login `Event::Application` is ignored (gateway.rs:1640-1649, `gameplay_not_loaded`), but `commit_outcome` still runs. `bound` is `true`, so `deferred` is `false` (osfr-gateway.rs:1921-1924) and the save at 1935 persists instance 0.
   - Pre-login `Time` and `Ready` return `Err` before commit (gateway.rs:1457, 1623).

4. **Account-store mode blocks it remotely.** With an account store, dispatch rejects any message before character selection (osfr-gateway.rs:1544-1560: "account character selection is required before gateway use"). Without an account store, the gateway binds loopback only (osfr-gateway.rs:963-966), so the path needs a local client. The reviewer's stated precondition (a disconnected, not-logged-in session) is unreachable.

**Corrected fix (the proposed one is wrong):** changing the guard at 825 to `<= 0` would not be safe. `bind_run_instance(…)?` at osfr-gateway.rs:1790-1791 sits inside the `prepared` closure, and `Err(error) => return Err(error)` at 1952 aborts the commit. So every pre-login `Application` would become a hard error, not a silent ignore. The fix belongs in `commit_outcome`: skip the bind when `change` is `None` and `old_instance` is `None` (no world instance is known). Optionally also reject a non-positive instance at the `load()` side so it does not brick the character. That is only defensive, since the write itself is the bug.
