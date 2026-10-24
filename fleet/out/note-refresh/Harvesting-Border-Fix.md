<!-- fleet job=note-refresh id=Harvesting-Border-Fix status=done turns=21 usd=0.0171 tokens(read,write,in,out)=[499012, 48603, 44, 12002] model=claude-haiku-5-5 -->
# notes/Research/Harvesting Border Fix.md

**Verdict:** minor drift. The fix itself is as described: the padded 11x11 constants, `padded_engine_shape`, the bounds-aware `validate_content`, the notice text, the 3-test `harvesting_border.rs`, and the four assertion updates all match the tip. One function citation has moved.

**Corrections:**

- `old:` "`board_bounds` (non-empty, non-dropzone cells; rectangle must be full; drop row directly below;"
  `new:` "`validate_spec` in `src/mining.rs` (the shared engine's bounds derivation, returning `Bounds`; non-empty, non-dropzone cells; rectangle must be full; drop row directly below;"
  `why:` No function named `board_bounds` exists in the repo. The derivation the note describes is `fn validate_spec(spec) -> io::Result<Bounds>` at `prototype/osfr-tools/src/mining.rs:1130`, with the min/max scan at `:1212-1280`. The name survives only in comments: `src/harvesting.rs:1107` and `tests/harvesting_border.rs:79`. Those comments are stale too, but they are not in this note.

**Unsure:**

- The "Current focused Harvest family" line is a dated 2026-10-09 receipt, so 53 passed was true when it ran. At the tip, `tests/type8_harvesting_gateway.rs` has 14 `#[test]` functions (lines 438 to 1135), not 11, and none are `#[ignore]`. `tests/harvesting_lifecycle.rs` (4 tests) and `tests/harvest_nodes.rs` (1 test) are not in the list. I did not re-run the suite, so I have not changed the count. If the note is meant to describe the current family, the list and total need a fresh run.
- The `lab/reports/harvesting-border-fix-20261009-1417Z/` receipts (RED/GREEN logs, `family.log`) are not visible through the tools, so I could not check the logs or the quoted test lines. The review note (`notes/Reviews/Harvesting Runtime and Border Review.md:18-22`, `:70-72`) agrees that the builder's GREEN run was blocked by Application Control and that the review re-ran the 3-test target under the project target and got 3 passing.
- The Application Control block description and the `os error 4551` quote match what the review records. I could not confirm the verbatim log text.
