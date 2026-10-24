<!-- fleet job=bug-verify id=src-restoration-piece-056-rs-L1-f2 status=done turns=5 usd=0.0051 tokens(read,write,in,out)=[45314, 22210, 12, 3764] model=claude-haiku-5-5 -->
# medium: `prototype/osfr-tools/src/restoration/piece_056.rs:598-600`

**Verdict:** refuted

**Severity if confirmed:** n/a (no remote-reachable path)

**Evidence:**

1. **Module tree.** `piece_056.rs` is compiled into the library, but only as a dead-code helper. `src/lib.rs:3` has `pub mod abilities;`, and `src/abilities.rs:14-16` reads:
   ```
   #[allow(dead_code)]
   #[path = "restoration/piece_056.rs"]
   mod effect_packets;
   ```
   Only `tests/piece_056.rs:32-34` includes the file directly as its own module.

2. **Reachability.** The only production use of `effect_packets` is in `abilities.rs`, at lines 745, 929 and 954. Those calls use `encode_remove_effect_tag`, `EffectTagPayload` and `encode_add_effect_tag`. A search of `prototype/osfr-tools` for `StatusLedger`, `decode_profile_rows`, `effect_packets::` and `.restore(` finds no caller of `StatusLedger::restore`, `decode_profile_rows`, `StatusLedger::new` or `apply` outside `piece_056.rs` itself and `tests/piece_056.rs` (lines 186-390, which call `StatusLedger::restore(&rows, 0, 600)` and similar). No gateway or gameplay dispatch path decodes profile rows or builds a ledger. The claimed chain `decode_profile_rows → restore → apply → allocate` therefore never runs in the server.

3. **Upstream checks.** The claim's premise that "no range check on restored ids" is only half the picture. Even on the test-only path, `restore` (lines 555-582) is the only way to push `next_tag_id` near `i32::MAX`. Normal `allocate` from `FIRST_TAG_ID = 1` (line 86) would need about 2^31 applies. `apply` also rejects bad input before allocation (lines 460-471), but none of that matters because the input never reaches `apply` from a packet.

4. **The failure mechanics are correct in isolation.** At `piece_056.rs:598-599`, `while contains_key(next)` with `saturating_add` does spin forever when `next == i32::MAX` and that key is occupied. The defect is real code but unreachable from a player or save load in the shipped server. At most it is a latent hazard in a test-only or unwired helper.

**Corrected fix:** not needed for this report. If the helper is later wired into production, add a bounded search or `checked_add` in `allocate`, and reject restored `tag_id <= 0` (or `i32::MAX`) in `restore`/`decode_profile_rows`. Track this as a future-integration note, not as a current medium-severity defect.
