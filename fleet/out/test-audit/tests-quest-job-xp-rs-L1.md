<!-- fleet job=test-audit id=tests-quest-job-xp-rs-L1 status=done turns=6 usd=0.0091 tokens(read,write,in,out)=[98267, 34882, 14, 7459] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/quest_job_xp.rs lines 1-1200 of 1386

Window `prototype/osfr-tools/tests/quest_job_xp.rs` 1-1200 (read in full, plus the support helpers `npc_quest_chain.rs` 483-740 that the window calls). No test in the window is a tautology or `#[ignore]`d, and none early-returns on a missing fixture. The main problems are overclaiming names and doc comments, plus one weak error assertion.

- **[medium] quest_job_xp.rs:375 each_enabled_quest_pays_its_configured_job_xp_once - the name says every enabled quest is paid, but the body only calls four line tests (adventurer intro 3000020, Chef Ranger 3050011, Kart 3080001, Ninja 3110001).** The task table at 995-1200 has 24 rows, and most of the other enabled quests (3000021/22/59/60, 3050004, 3080002, 3110002/4, 3000009/16/29/24/32/33/34, and the Brawler rows) never reach a turn-in test here.
  - Why it cannot catch a regression: a change that breaks the job XP or gate for any of the other 20 quests still passes, because only the static table covers them.
  - Fix: either rename it to `four_playable_lines_pay_their_job_xp_once`, or drive every quest in the table through offer, accept, turn-in and assert `profile_xp` against the table's XP value.

- **[medium] quest_job_xp.rs:849-913 reward_bundle_displays_each_configured_job_xp_total - the doc says "Every configured row must reach that dword", but `listed` at 854 has 12 entries and skips quests the table covers.** Missing examples are 3000009, 3000016, 3000029, 3000024, 3000032-3000034 and the Brawler 3030004 records. The expected coins and XP are read from the same JSON that the engine uses, which is a valid oracle, so the gap is coverage only.
  - Why it cannot catch a regression: a bundle that drops or mis-stars a job-XP row on one of the skipped quests still passes.
  - Fix: iterate over the same 24-row table used at line 995 (or every record in `quests/*.json` with a non-empty `job_xp`), so the doc claim matches the loop.

- **[medium] quest_job_xp.rs:964 and 972 content_overflow_is_rejected_at_load - both rejections assert only `error.kind() == InvalidData`.** The overflow case (2_000_000_000 + 2_000_000_000) and the unknown-profile case (`9999`) both raise InvalidData (quest_engine.rs:2379-2400 and `job_xp_profile_unknown`). The `checked_add` on the per-grant total at quest_engine.rs:2390 is not the only InvalidData source.
  - Why it cannot catch a regression: if the overflow check were replaced by any other InvalidData error (for example a malformed-row error), or the profile check were removed while another validator still rejected, the test would still pass.
  - Fix: assert the message, e.g. `error.to_string().contains("quest XP reward overflow")` for the first case and `contains("unknown job profile 9999")` for the second, and keep the control load on the same scratch copy.

- **[low] quest_job_xp.rs:576-634 locked_profile_turnin_refuses_without_profile_content - the name says "refuses", but the only checks are `refused.changed`, `pending_turnin == None` and status `Active`.** Unlike the sibling test at 483-571, it never checks coins, inventory, or that no profile XP was granted on the synthetic-fallback path.
  - Why it cannot catch a regression: a fallback that grants coins or synthetic XP while leaving the quest Active would still pass.
  - Fix: capture `coins(&game)` and `game.state().inventory` before the 49/14, and assert both are unchanged, as lines 532-534 do.
