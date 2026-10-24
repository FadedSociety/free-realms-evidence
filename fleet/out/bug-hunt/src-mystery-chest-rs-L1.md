<!-- fleet job=bug-hunt id=src-mystery-chest-rs-L1 status=nothing_found turns=11 usd=0.0091 tokens(read,write,in,out)=[176474, 28418, 24, 7523] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/mystery_chest.rs lines 1-231 of 231

Reviewed `prototype/osfr-tools/src/mystery_chest.rs` lines 1-231 in full, plus the callers (`gameplay.rs:4444` and `:5334` for `handle_mystery_chest`, `mystery_chest_loot.rs:128` and `:184` for `check_reply` and `item_reward`) and the codec tests in `tests/mystery_chest_codec.rs:105-190`. I found no defect I could tie to a line.

What I checked:
- **`parse_request` (115-140):** `read_u16` uses `get(offset..offset+2)`, so short buffers return `Err` and do not panic. The `bytes[4..8]` indexing is guarded by the `len == 8` check. The `item_id <= 0` rejection is correct. The `Err` on 0-3 byte buffers is intentional and pinned by the tests at lines 141-146 and 150-165, so it is not a logic error.
- **`check_reply` (146-157):** the layout matches the 25-byte capacity and the documented field order.
- **`item_reward` (164-216):** the offsets match the doc table. The header is 3 bytes, the fixed body through the entry count is 65 bytes, and an entry is 42 bytes plus the 4-byte final word. That gives 114 total and 69 for the empty-entry body, both consistent with the doc comments. The positive-id checks run before any write, and nothing indexes client-sized data.
- **`read_u16`/`eof`/`invalid` (218-231):** no arithmetic that can overflow for the small offsets used.

Trust boundary: `mystery_chest_loot.rs` validates the client's instance id against server state (owned, non-rental, unconsumed, chest definition in the binding table) before any grant. That is outside this window, so I did not assess it further.

Nothing in this window meets the bar for a finding.
