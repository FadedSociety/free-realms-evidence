<!-- fleet job=test-audit id=tests-common-content-copy-rs-L1 status=nothing_found turns=3 usd=0.0014 tokens(read,write,in,out)=[5400, 5295, 8, 1365] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/common/content_copy.rs lines 1-35 of 35

Reviewed `prototype/osfr-tools/tests/common/content_copy.rs` lines 1-35 (the whole file). It contains no `#[test]` functions. It holds two filesystem helpers, `copy_tree` and `copy_missing`, so none of the five test-level categories applies directly.

I checked the helpers against their callers:
- `copy_missing` does what its doc comment says. It recurses, and it copies a file only when the destination path does not already exist, so existing fixture profile and inventory files survive.
- The `#[allow(dead_code)]` comment is accurate. The callers that use `copy_missing` are `tests/common/field_reward_fixture.rs:46,52`, `tests/soccer_quest_credit.rs:71,72` and `tests/support/npc_quest_chain.rs:106`, which fit "quest, reward and soccer fixtures".
- The failure modes I could find are loud, not silent. A directory-vs-file clash makes `create_dir_all` or `fs::copy` panic through `unwrap`. A symlink to a directory also panics in `fs::copy`. Neither can make a test pass when it should fail.

Nothing in this window can pass a regression that a test should catch. The redundant `#[allow(dead_code)]` on `tests/soccer_quest_credit.rs:41` is cosmetic and is not reported.
