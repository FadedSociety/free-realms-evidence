<!-- fleet job=bug-hunt id=src-startup-selfdata-rs-L1 status=nothing_found turns=6 usd=0.0112 tokens(read,write,in,out)=[103426, 37426, 14, 10909] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/startup_selfdata.rs lines 1-800 of 1327

## Window review: `prototype/osfr-tools/src/startup_selfdata.rs` lines 1-800

No finding that a remote player can reach. I read lines 1-800 in full and checked the callers.

**Reachability.** The only non-test caller of the parser is `gateway.rs:853-855`. It runs `parse_self` on `self_bytes`, which comes from `load_reference(directory)` (`gateway.rs:831`). That is a server-side reference template loaded from disk, not a client packet, and the call is wrapped in `catch_unwind`. The other callers are in `tests/`. Nothing in the inbound packet handlers feeds client bytes to `parse_self`, `parse_profile`, or the other `parse_*` readers. So the panic sites in the window (`Cursor::take`/`u32`/`counted_string` `expect`s, `count` asserts, `parse_profile` line 493 direct slice index, `parse_profile` line 506 `i32::try_from(...).expect`, `parse_reward_bundle` line 426 `panic!` on an unmapped kind) are not client-triggerable.

**Checked and ruled out:**
- **Count bounds vs. minimum row sizes.** Every `cursor.count(N)` call in the window uses an N that matches the minimum serialized size of one row. Checked: reward entry 38 (4+1+24+4+5), objective 107, collection 101, quest-first 113, quest-second 127, keyed string 25, recipe 42, components 32, keyed row 33, profile pairs/equipment 12, abilities 4. So allocation is bounded by the input length.
- **Arithmetic.** `first_pairs * 12` and `count * minimum` are bounded by `remaining()`, so no overflow.
- **Parse/write symmetry.** `parse_reward_bundle` and `write_reward_bundle` agree on `kind_fields` widths (`1 if success!=0`→4, `1|3|12`→0, `6|10`→4). `parse_profile` and `write_profile` agree on the 37-byte prefix, the 34-byte tail, the equipment rows, the ability kind-field counts, and the zero sentinel. `before[4..]` correctly strips the map key.
- **Doc vs. code.** The fixed sizes in the window match the documented layouts for the collection, quest, keyed-string, recipe, and profile rows.
- **`last_cast_time` i32 narrowing (`write_inventory_item`).** Server-side inventory values are range-checked upstream (`inventory.rs:1435`, `trade.rs:1189/1571`), and the value originates from an i32 on the parse side, so it does not panic on client input.

**Not defects (observations only):** the `REWARD_BUNDLE_FIXED_BYTES` doc comment ("nine dwords, two u64 pairs, two scalars") does not obviously add up to 60 bytes. That is a documentation question I could not resolve from the window, not a runtime defect. The rental and activate flags are canonicalized to 0/1 on write, which is a harmless normalization.
