<!-- fleet job=bug-verify id=src-restoration-piece-098-rs-L1-f1 status=done turns=4 usd=0.0047 tokens(read,write,in,out)=[28925, 21197, 10, 3506] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/restoration/piece_098.rs:548-553

**Verdict:** refuted (as a server defect with the claimed medium severity and remote reach). The arithmetic wrap is real, but only in an offline asset tool that reads trusted local files.

**Evidence**

1. **Module tree.** `piece_098` is not in `src/lib.rs` (its `pub mod` list has no `restoration` or `piece_098`) and no `mod.rs` declares it. The only non-test includes are `#[path = "../restoration/piece_098.rs"] mod piece_098;` in `src/bin/osfr-terrain.rs:8-10`, and `tests/piece_098.rs:21-23`. So the code is compiled only into the `osfr-terrain` offline binary and the test target. It is not in gateway, login or library code.

2. **Reach.** A grep for `load_terrain(` and `piece_098::` across `prototype/osfr-tools/**/*.rs` finds exactly one production caller: `src/bin/osfr-terrain.rs:57`. That binary reads `lab/extracted/client-assets` files listed in a catalog (`--catalog`, `--assets`, lines 29-55) and writes a `.hgt` grid. Its header says the input is "the client's terrain chunks". `scripts/build_terrain.py` runs it as a build step. No packet handler, save load or gateway path calls `load_terrain`. The gateway reads only the `.hgt` output (`osfr-gateway.rs:290`, `:4214`). The input is therefore a retail asset file that the operator supplies, not player-controlled data. The claimed "remote player" path does not exist.

3. **Arithmetic (real, but local).** Lines 546-548 check that both `index_offset` and `index_count` are `>= 0`. The sum at 548 is `i32`, so the wrap can happen as described. The `> indices.len()` check can then pass, and the slice at 553 panics. The `Cargo.toml` has no `[profile]` or `overflow-checks` setting, so release builds wrap and debug builds panic. This only crashes the offline tool on a corrupt or hand-crafted asset file. It cannot corrupt a save, grant items or coins, or take down the server.

**Severity if the claim were kept as stated:** low (offline dev tool, trusted local input, no player reach). The medium "server-reachable" framing is refuted.

**Corrected fix (optional, low priority):** compare in `i64` (`batch.index_offset as i64 + batch.index_count as i64 > indices.len() as i64`) or use `checked_add` at 548, so the tool returns `IndexOutOfRange` instead of panicking. Note that `osfr-terrain.rs:64` also slices without a check, so it relies on this one.
