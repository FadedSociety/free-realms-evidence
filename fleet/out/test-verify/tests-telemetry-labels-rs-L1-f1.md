<!-- fleet job=test-verify id=tests-telemetry-labels-rs-L1-f1 status=done turns=4 usd=0.0035 tokens(read,write,in,out)=[21954, 16134, 10, 2439] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/telemetry_labels.rs:257

**Verdict:** `refuted`

**Evidence:** The claim is that a quiet-family routing regression passes the gate because the replay test returns early when `lab/runs` is absent. The regression is still caught by a different test that never reads `lab/runs`:

- `quiet_shapes_seen_in_native_traces` (`tests/telemetry_labels.rs:171-182`) is an ordinary `#[test]` with no skip path. It sends the hard-coded `SHAPES` table (lines 150-169) through the real gateway on both outer 5 and outer 6, and calls `assert_quiet` for each. The table covers families 105, 109, 194, 193, 16 and 26 (subs 20/26/37), which are the same families the replay's `wanted` filter (line 265-266) checks.
- `assert_quiet` (lines 118-128) pins exact behaviour: `trace.len() == 1`, `event.handler == label`, `event.outcome == "handled"`, `event.reason == None`, `out.replies.is_empty()`, and `out.applications == [inner]`.
- `send` (lines 110-115) also asserts the gateway snapshot is unchanged.

Walk-through of the claimed regression: if quiet-family routing breaks (for example, 105/109/194/193/16 fall through to "unknown application message", or the handler name changes, or a reply is emitted), then `assert_quiet` fails on the `handler` or `outcome` assertion, or `assert_unknown`-style rejection trips the `outcome == "handled"` check. That test runs on every gate and does not depend on `lab/runs`.

The fixtures it does depend on fail loudly, not silently. `Content::new()` (lines 37-43) asserts `harvesting.json` exists under `lab/reports/round59-native-20261015T124443Z/content`, and `loaded_gateway` unwraps the reference state. Neither path returns early. The header (lines 10-11) and the shape-table comment (line 149) also state that the table stands alone without `lab/runs`.

The only real gap is narrower than the claim: the replay test would catch a *new* unknown shape found in future private traces that is not already in `SHAPES`. That is a coverage gap, not the regression named. The silent `return` at line 257 is a legitimate concern to note, but it does not hide quiet-family routing breakage. Adding `#[ignore]` would not change what the gate checks for that regression.

**Minimal fix:** Not required for the claim as stated. Optional hardening: have the replay test panic when `OSFR_REQUIRE_LAB=1` is set and `files == 0`, so a machine that should have traces cannot silently skip the replay.
