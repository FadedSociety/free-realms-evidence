<!-- fleet job=test-audit id=tests-gathering-nodes-rs-L1 status=done turns=6 usd=0.0122 tokens(read,write,in,out)=[99431, 40524, 14, 12201] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/gathering_nodes.rs lines 1-1126 of 1126

Reviewed `prototype/osfr-tools/tests/gathering_nodes.rs` lines 1-1126 (helpers and all tests). Most tests compare concrete state (snapshots, exact chat text, save bytes, phase, counts) and I found no cannot-fail assertions, no `#[ignore]`, and no early-return skips. Fixture misses (missing content dir, missing `data/content`, missing `mining.json`) panic via `unwrap`/`expect`, so they fail loudly. I also checked that the shipped `mining.json` maps both outputs to 2739, so the `count(2739) == 12` expectation at line 622 is consistent with the content. The `xp`/`profile_xp` helpers use `unwrap_or(0)`, but the positive XP checks on the same key (line 744) guard against the key going missing, so I did not report them.

Two low-severity findings:

- **[low] tests/gathering_nodes.rs:1109 node_content_is_bounded_and_unique - the name and the comment at 1114 ("pool maxima") claim a per-pool bound, but the body only pins the total count and checks uniqueness and finiteness.**
  - Why it cannot catch a regression: a change that moves slots between pools (e.g. mushroom pool max 12→13 and copper veins 4→3, or a pool max raised with an equal drop elsewhere) keeps the total at 18 and still passes. Nothing in the body reads a pool max.
  - Fix: assert each pool's count against its declared max, e.g. count actors per `game`/node name and check `<= max` for each pool, or rename the test to `node_content_total_is_18_and_unique` and drop "bounded" and "pool maxima" from the comment.

- **[low] tests/gathering_nodes.rs:1115 node_content_is_bounded_and_unique - `actors.len() == 18` (and the duplicate `ids.len() == 18` at 1119) pins a content-size number that changes whenever a node is added or removed, while the test is about node-table shape.**
  - Why it is churn, not a hole: adding one legitimate node to `data/content` fails this test even though the bounds and uniqueness it claims still hold. The duplicate at 1119 repeats the same pin without adding information.
  - Fix: replace the literal with a derived expectation (e.g. `ids.len() == actors.len()` after dedup, plus the per-pool max checks suggested above), so the content can grow without editing this test.
