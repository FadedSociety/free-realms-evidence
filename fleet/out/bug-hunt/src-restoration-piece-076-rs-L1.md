<!-- fleet job=bug-hunt id=src-restoration-piece-076-rs-L1 status=done turns=5 usd=0.0073 tokens(read,write,in,out)=[51395, 24395, 12, 7466] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_076.rs lines 1-546 of 546

Reviewed `prototype/osfr-tools/src/restoration/piece_076.rs` lines 1-546 in full. No finding reaches a client packet or a save. The module is not registered in `src/` (no `mod`/`#[path]` include outside `tests/piece_076.rs`), and `audit`, `classify_guid`, `guid_for_npc`, `model_conflicts` and `regions_at` take only static recovered tables. Nothing parses external input, mutates state, or returns an error after a partial write. The checks I traced all hold:

- `audit` (l.344-348): `checked_sub`, `try_from`, and `alias as i32` cannot panic. The `GuidCollision` branch only runs when the alias equals an existing row id, which is non-negative, so the cast is safe.
- `area_contains` (l.261-277): rectangle bounds are normalised and the circle test is overflow-free for these magnitudes.
- Duplicate-guid, unknown-row, missing-binding and unexpected-guid severities match the module doc (l.18-23).

One latent defect, low severity:

- **[low] prototype/osfr-tools/src/restoration/piece_076.rs:248 - `guid_for_npc` computes `NPC_GUID_BASE + npc_id as u64` with no check, so a negative `npc_id` overflows the u64 addition.**
  - Failure scenario: `guid_for_npc(-1)` evaluates `npc_id as u64` as 2^64-1, then `100_000_000_000 + (2^64-1)` overflows. That panics in a debug build and wraps silently in release. The same path is hit from `classify_guid` (l.256) when a row has `capture_guid: None`, and `audit` calls it for any place whose npc_id matches a row.
  - Reach: `audit` (l.325) → `classify_guid` (l.339) → `guid_for_npc` (l.256). The only inputs are the `Place` and `NpcRow` slices, which are recovered constants or test fixtures. No client packet or save reaches them, and no upstream check rejects negative ids. The test suite never passes a negative id. So this is a debug-build panic in an offline audit tool, not a remote crash.
  - Fix: `NPC_GUID_BASE.checked_add(u64::try_from(npc_id).ok()?)` with `guid_for_npc` returning `Option<u64>`, or treat a negative npc_id as `UnknownNpcRow` in `audit` before classification.
