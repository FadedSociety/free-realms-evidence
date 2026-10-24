<!-- fleet job=bug-hunt id=src-restoration-piece-088-rs-L1 status=nothing_found turns=6 usd=0.0088 tokens(read,write,in,out)=[79448, 31058, 14, 8335] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_088.rs lines 1-529 of 529

I read `prototype/osfr-tools/src/restoration/piece_088.rs` lines 1-529 in full and checked the callers and tests they touch. I found no defect I can tie to a line.

What I checked:

- **Packet parsing (`Reader`, `parse_request`, lines 315-388):** every read goes through `take`, which uses `checked_add` and `slice.get(..)`, so an oversized or truncated record returns `Err` and cannot panic. `string` checks the u32 length against its limit before taking bytes, so allocation is bounded by 128 for names and 2048 for messages. The `from_utf8` failure maps to `Err`. The fixed-width `try_into().unwrap()` calls are preceded by `take(n)` of exactly n bytes, so they cannot fail. Trailing bytes are rejected at line 372.
- **Channel mapping (`from_wire`, `facts`, lines 229-275):** `facts` cannot panic, because `CHANNEL_FACTS` has one entry per channel. Reserved wire values 2 and 3 parse but are refused by `route` as `NotClientChannel`.
- **Recipient routing (`route`, lines 447-492):** the sender is excluded, and duplicate guids are removed with `contains`. The ignore handling matches its doc comment and the test at `tests/piece_088.rs:316-335`.
- **Tell routing (`route_tell`, lines 494-529):** I first suspected that `Vec::dedup` only removes adjacent duplicates. That does not matter here, because the name filter keeps only name matches, so two matches for the same guid can only be adjacent unless a different guid matched in between, and that case is genuinely ambiguous. `matched[0]` is safe because the `1 =>` arm implies `matched` is non-empty. Tell routing uses the name and ignores the client-supplied `to_guid`.
- **Trust boundary:** `from_guid`, `to_guid` and `guild_guid` are carried for logging only. Sender identity and guild membership come from caller-supplied `sender_guid` and `Peer` flags. The module header and the `ParsedChat` doc comment state this.

Other observations, none of which is a defect:

- The module is not registered in production code. Its only consumer is the `#[path]` include in `tests/piece_088.rs`, so there is no production caller to trace further.
- The group-membership gate for Members-Only is listed as a GAP in the module header, so I did not report it.
- Echo-to-sender is true for every non-tell channel. The doc comment on `Delivery.echo_to_sender` lists only some channels, but it does not say "only", so I did not count that as a contradiction.
