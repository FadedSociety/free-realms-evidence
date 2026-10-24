<!-- fleet job=bug-hunt id=src-restoration-piece-070-rs-L1 status=nothing_found turns=5 usd=0.0055 tokens(read,write,in,out)=[39869, 18392, 12, 5541] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_070.rs lines 1-283 of 283

No defects found in `prototype/osfr-tools/src/restoration/piece_070.rs` lines 1-283.

What I checked:

- **Panics:** every slice and `try_into().unwrap()` in the window is preceded by an exact length guarantee. `parse` checks `len == 17` before indexing `bytes[8]` and the sub-slices. `Reader::take` uses `checked_add` and `get(..)`. `Reader::count` rejects negatives before `as usize`. The `f32` progress is checked for finiteness. `replace_in_span` copies into `result[range]`, and `range` is `start..span.len()` with `start = len - 17`, so the lengths match.
- **Unbounded growth:** quest count (256), objective count (64), reward entries (256) and string length (65,536) are all capped. Total work is linear in the span, which is capped at 2 MiB by `MAX_SPAN_BYTES`.
- **Layout versus the writer:** I compared `locate` and `Reader::reward` against `parse_quest_record`, `_Reader.reward` and the tail reads in `scripts/pieces/piece_070.py` (lines 120-215). The byte counts match field by field: the quest header is 16+1+12+1+4 bytes; the reward is 1+60, then the entry count, then per entry 4+1+24+len+4+1(+4 if extended), then a trailing 4; the objective is 16+1+reward+16+1+4; the tail is 4+4+1+4+4 at offsets 0/4/8/9/13.
- **Validation logic:** `validate` accepts `-1` or positive selected ids and non-negative completed counts, matching its doc comment and the `opening_campaign` contract. The flag byte is read at offset 8 as documented.
- **Atomicity:** `replace_in_span` and `to_bytes` do not mutate their inputs; the result is a new `Vec`.
- **Reach:** the module is not registered in any `mod` declaration in `src`. Its only callers are `tests/piece_070.rs` and the notes. The loader reads a captured reference span, not client packets, so no client-controlled input can reach these functions in the current tree.

Anything I noted but did not report: `validate` does not bound the unnamed i32 fields or the quest progress range, but the docs say these are deliberately unconstrained and the path is not reachable from clients.
