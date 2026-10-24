<!-- fleet job=bug-verify id=src-activity-portal-rs-L1-f1 status=done turns=7 usd=0.0049 tokens(read,write,in,out)=[75777, 18764, 16, 3636] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/gameplay/content_reload.rs:57-63

**Verdict:** confirmed (the defect is real, but the severity is overstated)

**Severity if confirmed:** low. The trigger is a developer-only operator command, nothing a remote player can reach. The only effect is that soccer disappears from the portal and Play is refused until restart. No items, coins, or saves are affected.

**Evidence:**

1. **In the real server.** `gameplay.rs:44` declares `mod content_reload;`, so `content_reload.rs` is in the module tree.
2. **Reach and gate.** The chat `["reload", rest @ ..]` arm at `gameplay.rs:2891-2897` calls `reload_content`. `Gameplay::developer_command_denied` (`gameplay.rs:3675-3698`) denies any `realm` command that is not ordinary and fails `may_run`, which checks `account_store::can_run_realm_command(self.role, ...)` (`gameplay.rs:3670`). So `realm reload` needs the dev tools and an authorized role. The claim's "operator-triggered" reading is correct.
3. **The bug is real.** `content_reload.rs:57-63` sets `self.activities = Catalogue::load(&path)?` and then re-adds only chess rows. The only `add_soccer_rows` call in the codebase is `gameplay.rs:956`, at startup. Nothing in the reload path re-adds soccer rows. `soccer_content` (`gameplay.rs:192`, `1181`) is not reloaded, so it stays loaded.
4. **Startup order matches the claim.** `gameplay.rs:939-957` builds battles, adds chess, then adds soccer.
5. **Admission refuses the soccer id.** `activity_portal.rs:274-279` (`admit`) looks up `self.rows` and returns `Refusal::Unknown` when the id is missing. The claimed `begin_soccer` path is never reached.
6. **Staging is fine.** `content_reload.rs:21-27` clones `self`, stages, and commits `activities` atomically. The reply still says "Reloaded: battles.", as claimed.
7. **Test coverage.** No test in `tests/` exercises soccer after `realm reload battles`. The only reload-related portal checks are in `field_battle_roster.rs:1099`, which is about battles.

**Corrected fix:** the claimed fix is correct. Inside the staged block of `reload_content_in_place`, after the chess rebuild (`content_reload.rs:58-63`), add `if let Some(content) = &self.soccer_content { self.activities.add_soccer_rows(content.portal_rows())?; }`. This must run on the staged `self` before the commit, so a failure still publishes nothing. A cleaner option is to move the startup catalogue build (`gameplay.rs:939-957`) into one helper and call it from both places. The claim's `self.activities.clone().add...` wording is not valid, since `add_soccer_rows` takes `&mut self` and returns `()`. Use the in-place call.
</result>
