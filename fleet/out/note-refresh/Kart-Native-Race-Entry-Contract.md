<!-- fleet job=note-refresh id=Kart-Native-Race-Entry-Contract status=done turns=12 usd=0.0145 tokens(read,write,in,out)=[301385, 51804, 26, 10092] model=claude-haiku-5-5 -->
# notes/Research/Kart Native Race Entry Contract.md

**Verdict:** minor drift. The wire facts, field maps and capture order check out against the code. One status claim in the "Next launch binding" section is false: the 33/9 entry handler is already built and routed, so a builder following step 2 would rebuild code that exists.

**Corrections:**

1. `old:` what is missing is 33/9 handling, the
   33/34 + 33/11 + 33/5 start bundle, the 33/1/3/4 counters and this ordering.
   `new:` the 33/9 handling, the 33/34 + 33/11 + 33/5 start bundle, the 33/1/3/4 counters and this ordering are built in `src/kart_entry.rs` (`KartEntryHandler::on_register`, `on_player_state`, `on_race_ready`). They are routed from `src/kart_gateway.rs` (`handle_entry` at 626-634; subtypes 9 and 2 dispatched at 677-679). The handler is gated: `EntryGate::Disabled` by default, opened per active entry at `kart_gateway.rs:523`. What remains open is supplying the captured content blocks (race config, 33/5 body, 33/11 attribute blocks, 33/14 progress) through the private content package, plus live playtest verification.
   `why:` repo:prototype/osfr-tools/src/kart_entry.rs:credit 650-687 (register reply order 33/34, 33/11 per vehicle, 33/5, 33/14 per racer), :691-712 (33/2 → 33/3 + 33/1), :717-734 (33/1 = 4 + 33/4); repo:prototype/osfr-tools/src/kart_entry.rs:37-40 (opaque blocks supplied by content); repo:prototype/osfr-tools/src/kart_gateway.rs:523 (gate enabled per entry), :626-634, :677-679; repo:prototype/osfr-tools/src/lib.rs:41 (`pub mod kart_entry;`); repo:prototype/osfr-tools/tests/kart_entry.rs:837 (33/9 → 33/34, 33/11, 33/5, 33/14 byte-identical test).

**Checked and holding:**
- `src/zone_transition.rs` (op31 codec, `encode`/`decode` at 96/190) exists and is used for the scene frame (`kart_entry.rs:588-593`).
- `src/kart_lobby_native.rs` exists, is registered (`lib.rs:43`), and is in production use (`gameplay.rs:1061`, `encode_inner`). Its counts `[6,30,43,37,17]` and the five-table layout match the header (`kart_lobby_native.rs:1-20`).
- `src/kart_progress_native.rs` exists and is registered (`lib.rs:45`); the 33/14 codec is used by `kart_entry.rs:682`.
- Payload sizes match the code: 33/9 = 16 bytes (`REGISTER_PAYLOAD_LEN`), 33/2 = 12, counters = 4, 33/34 = 21 words / 84 bytes, 33/5 = 85 bytes (`kart_entry.rs:80-88`).
- Subtype numbers 9, 2, 3, 4, 5, 11, 14, 34 match the code constants (`kart_entry.rs:59-75`).

**Unsure:**
- The `lab/reports/kart-race-entry-contract-20261009T1735Z/` artifacts (probe, `proof.json`, `run.log`) and `probe-race-entry-contract-v2.py` / `proof-v2.json` are not under any root I can read. I did not check them. `tests/kart_entry.rs:11` does cite `proof-v2.json`, so that file was at least referenced by code.
- The claim that Sanctuary's writer emits only the single row0 shape with `Unknown 37`, and the "no community serializer for the 33 family" absence, sit in `refs`, which I did not check.
- The `33/34` and `33/11` field-meaning claims were not checked. They are "unrecovered" in the note, and the code keeps them positional, so they are consistent but not verified.</result>
