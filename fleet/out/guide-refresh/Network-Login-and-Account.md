<!-- fleet job=guide-refresh id=Network-Login-and-Account status=done turns=17 usd=0.0131 tokens(read,write,in,out)=[293993, 33441, 36, 11944] model=claude-haiku-5-5 -->
# notes/Build Guides/Network/Login and Account.md

**Verdict:** minor drift. The row-level data (addresses, names, confidence words, wire count, the other subsystem counts, and the per-shard counts except S0657) matches the client label table at the tip. The header totals and the ui.welcome section are short by three functions. Those three come from shard S0657, which the note's shard list leaves out. The "How it works" section is still the unwritten placeholder, which is not a checkable claim.

**Corrections:**

1. `old:` 651 accepted functions: 327 confirmed, 129 likely, 129 speculative, 66 unknown.
   `new:` 654 accepted functions: 329 confirmed, 129 likely, 129 speculative, 67 unknown.
   `why:` client `label` table, the six subsystems in this note (net.login 349, net.account_command 147, net.clientupdate 54, ui.welcome 45, ui.account 41, net.namechange 18 = 654). Confidence split: confirmed 75+40+153+15+21+25 = 329; likely 129; speculative 129; unknown 2+1+51+2+5+6 = 67. The `wire` count of 68 still matches.

2. `old:` `ui.welcome` (42)
   `new:` `ui.welcome` (45)
   `why:` client `label` rows at 012494e0, 0124a4b0 and 0124af50 (`UI::UIRespond{FeatureRotator,Advertisement,NewsMessage}DisplayAction::Handle`), subsystem ui.welcome, shard S0657. The section's 42 rows are the 19 unclassed plus the four WelcomeInfo classes; the 45 count includes these three.

3. `old:` [[S0658 0124dfe0-01253ee0|S0658]] (14)
   `new:` [[S0657|S0657]] (3), [[S0658 0124dfe0-01253ee0|S0658]] (14)
   `why:` client `label` shard counts for these subsystems: S0657 = 3 (the three ui.welcome Handle rows above). Every other shard count in the list matches, but S0657 is missing.

**Unsure:**
- The three `UI::UIRespond*DisplayAction::Handle` rows (012494e0, 0124a4b0, 0124af50) do not appear in the `### ui.welcome` tables. Adding them needs a regeneration of the generated section, so I did not write a table row for them. The row text would be: `UIRespondAdvertisementDisplayAction::Handle` confirmed, `UIRespondNewsMessageDisplayAction::Handle` confirmed, `UIRespondFeatureRotatorDisplayAction::Handle` likely.
- Outside this note: `notes/Build Guides/Build Guides.md:49` repeats the stale "651 functions (327 confirmed, 129 likely)" for this page. It should be updated to match whichever totals are used here.
- I did not verify the note's shard links resolve to existing shard pages, or the "Mapped functions" sample-row confidence labels beyond the roughly 20 addresses I spot-checked (all matched).
