<!-- fleet job=pin-audit id=tests-quest-item-reward-rs status=nothing_found turns=2 usd=0.0008 tokens(read,write,in,out)=[1875, 3298, 6, 763] model=claude-haiku-5-5 -->
# tests/quest_item_reward.rs

No findings. Both screened lines compare against test-local constants, not shipped data:

- `tests/quest_item_reward.rs:65` `const COINS: u32 = 7;` and `:66` `const XP: u32 = 3;` are defined in the test file. The fixture writes them into the quest rewards it builds (`rewards(COINS, ...)` at lines 110, 124), and `QuestEngine::from_split_content(fixture.path(), ...)` loads that fixture catalogue. The values in `data/content/*.json` do not feed these assertions, so retuning shipped data would not break them.
- 487 (`COINS`) and 488 (`XP`) therefore pin fixture-set values, which the rule says are not findings.
