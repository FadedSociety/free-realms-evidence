<!-- fleet job=pin-audit id=tests-chat-settings-rs status=nothing_found turns=3 usd=0.0017 tokens(read,write,in,out)=[8712, 8424, 8, 1159] model=claude-haiku-5-5 -->
# tests/chat_settings.rs

Checked `prototype/osfr-tools/tests/chat_settings.rs:371` (`the_action_budget_covers_the_three_requests`, `assert_eq!(allowed, 10, ...)`).

The 10 does not come from a data file. `ActionBudgets::default()` (src/social_chat.rs:47-50) builds `KeyedBuckets::new(ACTION_RATE, ACTION_BURST, MAX_ACTION_ACCOUNTS)`, where `const ACTION_BURST: f64 = 10.0;` is a Rust constant at src/social_chat.rs:34 (`ACTION_RATE` = 5.0 at line 33). No file under `data/content/` holds a chat or action-budget burst value; a search for "burst" across the crate found only unrelated hits (jump relay `RELAY_BURST` in code, gateway handshake constants in code). The test does not build its own fixture for this number either. So the assertion pins a code constant, not a tunable data value, and it is outside the data-file rule. The test's own comment ("burst of 10") just restates that constant.

No finding.
