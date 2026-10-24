<!-- fleet job=test-audit id=tests-common-vendor-fixture-rs-L1 status=done turns=6 usd=0.0034 tokens(read,write,in,out)=[38867, 11572, 14, 3138] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/common/vendor_fixture.rs lines 1-222 of 222

Window reviewed: `prototype/osfr-tools/tests/common/vendor_fixture.rs` lines 1-222. This is a fixture module with no `#[test]` functions. The price oracles (`price`, `sell_price`, `sell_price_of`) read `data/content/stores.json` independently of the purchase code path, so they are not derived from the code under test. The `option` lookup panics if no shop option exists, so there is no silent skip. The directory cleanup in `Drop` is real. No high or medium issues in this window.

- **[low] tests/common/vendor_fixture.rs:186-200 `state` (full_bag branch) - the bag is filled with a hardcoded 100 items (`100_000..100_100`, `next_instance_id = 100_100`), which duplicates the reconstructed 100-slot floor in `src/gameplay/npc.rs:325` (`.max(100)`) instead of deriving it from that limit.**
  - Why it cannot catch a regression: it does not hide a regression. If the floor changes, the "full bag" state stops being full and the refusal tests fail loudly, but they fail for a fixture reason rather than a purchase-logic one. That is churn, not a missed bug.
  - Fix: name the limit once (for example `pub const BAG_FLOOR: usize = 100;`, mirrored from the code under test) and build the full bag from it, or assert in `state()` that the resulting item count reaches the limit the gateway uses.

- **[low] tests/common/vendor_fixture.rs:4-6 (module doc) - the doc says "Only the NPC's zone/position is translated to zone 0", but `new` (lines 86-89) also rewrites `zone` to "FabledRealms", `placement` to "legacy_data", and `heading` to 0.0.**
  - Why it cannot catch a regression: this is not a test gap. It is doc drift that could mislead a reviewer into trusting the fixture as a verbatim copy of the shipped vendor record when assessing what it covers.
  - Fix: update the doc to list every field the fixture overwrites (zone_id, zone, position, heading, placement), so the "shipped" claim is accurate.
