<!-- fleet job=test-audit id=tests-kart-npc-entry-rs-L1 status=done turns=6 usd=0.0083 tokens(read,write,in,out)=[100632, 33314, 14, 6214] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/kart_npc_entry.rs lines 1-1200 of 1621

Reviewed `prototype/osfr-tools/tests/kart_npc_entry.rs` lines 1-1200. Most tests here are sound: the gate-file refusals really are reachable (`MAX_GATES_FILE` = 16 KiB, `MAX_REWARD_COOLDOWN_S` = 86 400, both checked in `kart_gateway.rs`); the "without moving state" tests compare full state; `changed_for_save` (`kart_gateway.rs:124`) really excludes the observation budget, so the `33/6` no-save test in `an_observation_commits_the_persisted_budget_without_a_save` (line 1095) can detect a regression by the `real.next_instance += 1` canary. I found one weak assertion, below.

- **[low] tests/kart_npc_entry.rs:586 `start_to_green` (helper used by the cooldown, ordinary-entry and cancel tests) - asserts the exact reply count of the Go frame (`.len() == 1` at line 591) although these tests are about payouts and cooldown, not the Go reply shape.**
  - Why it cannot catch a regression: it is not a miss; it is churn. The exact count is incidental, so an unrelated change that adds or removes a companion frame on Go (for example an extra status or NPC-count frame) fails every payout test in the file without any payout behaviour changing. It also does not prove the countdown started, since a single reply of any kind satisfies it.
  - Fix: assert the reply is non-empty (as line 586 already does for the grid register), and leave the exact frame shape to a test that is about the Go reply. Do not pin the count here.

No other findings in this window. Notes outside the window, not reported as findings: `clock_only_racing_ticks...` (line 1191) binds `prior_job` at line 1197, and I did not read its use beyond line 1200.
