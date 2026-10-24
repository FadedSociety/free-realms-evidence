<!-- fleet job=bug-verify id=src-restoration-piece-008-rs-L1-f1 status=done turns=4 usd=0.0037 tokens(read,write,in,out)=[27155, 16561, 10, 2725] model=claude-haiku-5-5 -->
# medium: `prototype/osfr-tools/src/restoration/piece_008.rs:1212`

**Verdict:** `refuted` (as a server defect). The panic is real in the module's code, but no build of the real server can reach it.

**Severity if confirmed:** n/a (refuted). If the module is wired in later, the latent panic would be a real hardening item.

**Evidence:**

1. **Module tree (check 1 fails for the claim).** `piece_008.rs` is not declared anywhere in `src/`. A search of `prototype/osfr-tools/src` for `piece_008|ChessSession|restoration/piece_008` matched only the file itself (`piece_008.rs:1150`, `:1159`, `:1253`). The only inclusion is `prototype/osfr-tools/tests/piece_008.rs:10-12`: `#[path = "../src/restoration/piece_008.rs"] mod piece_008;`. The `src/` tree has no `mod restoration`, and the chess types are not referenced by any gateway or login code. The defect is test-only, as the claim's own caveat states.

2. **Reachability (check 2).** `ChessSession::play` (`piece_008.rs:1208`) has no caller in `src/` or `src/bin/`. No packet handler decodes a client chess move into `ChessMove`. The out-of-range input therefore cannot come from a remote player today.

3. **Line facts (check 3) are accurate but moot.** `play` calls `engine_move_bytes` at 1212 before `apply` at 1213. `special_code` indexes `self.squares[mv.from as usize]` at 1070 and `self.squares[mv.to as usize]` at 1099. `engine_move_bytes` indexes `mv.from` at 1112. `squares` is `[Option<Piece>; 64]` (line 303), so `from`/`to` ≥ 64 would panic. The claim's facts check out, but they only matter once the module is compiled in.

**Corrected fix:** Not needed for the current build. If the module is wired into the server, add the bounds check the claim proposes at the top of `play`, or move the `engine_move_bytes` call after `apply` (computed from a cloned pre-move position). The bounds check is the simpler option.
