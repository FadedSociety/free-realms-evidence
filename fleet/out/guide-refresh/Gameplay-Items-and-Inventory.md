<!-- fleet job=guide-refresh id=Gameplay-Items-and-Inventory status=done turns=32 usd=0.0362 tokens(read,write,in,out)=[1497145, 90518, 68, 19839] model=claude-haiku-5-5 -->
# notes/Build Guides/Gameplay/Items and Inventory.md

**Verdict:** minor drift. The client-side analysis (packet tables, offsets, Lua, resource counts) is mostly untouched by the code, but several "What the Rust server must do" items state server behaviour that the tip does not have or does differently. I checked about 15 claims with grep and reads, not all 900 lines.

**Corrections:**

1. `old:` Send the membership activation message (id 202, which sets `player+0x464`)
   `new:` Send the membership activation message (opcode 100, which sets `player+0x464`)
   `why:` `repo:prototype/osfr-tools/src/game_rules.rs:291-296` (`encode_membership_activation` writes `100u16`, "the native opcode-100 membership update"); `repo:prototype/osfr-tools/src/activity_portal.rs:11` ("when membership activates (`009471a0`, message 100)"). Client: the main dispatcher `009471a0` has `case 0x64` and no `0x202` case.

2. `old:` Accept 42/3, 42/2, 42/8, 42/10 to 42/14.
   `new:` Accept 42/2, 42/3 and 42/8 (routed today). 42/10 to 42/14 are not handled yet and fall through to a no-op.
   `why:` `repo:prototype/osfr-tools/src/inventory.rs:1164-1211` (`route` matches only opcodes 2, 3 and 8; `_ => Ok(InventoryOutcome::default())` at 1209-1211).

3. `old:` and accept 42/10 per changed slot
   `new:` and accept 42/10 per changed slot (not built at tip; 42/10 currently hits the no-op arm)
   `why:` `repo:prototype/osfr-tools/src/inventory.rs:1209-1211`; grep for `UseStyleCard`, `style_card`, `stylecard` in `prototype/osfr-tools/src` returned nothing.

4. `old:` Send the rental block with an expiry in the client clock's base, expire server-side, and delete or refuse the row (R).
   `new:` Send the rental block with an expiry in the client clock's base, expire server-side, and delete or refuse the row (R). Today expiry is off: `rental_now` is `None` in the live path, so the expiry check never runs.
   `why:` `repo:prototype/osfr-tools/src/gameplay.rs:5226` (`rental_now: None, // (R) rental expiry unit unproven`); `repo:prototype/osfr-tools/src/inventory.rs:1381-1385` (expiry only when `rental_now` is `Some`); Build Ledger line 91 ("rental expiry off until its unit is proven").

5. `old:` 12. **Storage.** Open with 42/18, publish 38/31 usage and capacity once the field order is settled, and 38/32 when full.
   `new:` 12. **Storage.** Open with 42/18, publish 38/31 usage and capacity once the field order is settled, and 38/32 when full. (Not built at tip: no 42/17, 42/18, 38/31 or 38/32 handler exists in `prototype/osfr-tools/src`.)
   `why:` grep of `prototype/osfr-tools/src` for `storage`, `42/17`, `42/18`, `38/31`, `38/32`, `MoveItemToStorage`, `RequestStorage` returned no inventory handler. The Evidence section already says storage is "not yet accepted natively", so this is a missing status tag, not a contradiction.

**Unsure:**

- Line 80 ("38/3 ... seven `i32`"): consistent with `repo:prototype/osfr-tools/src/inventory_v2_fixes.rs:3` and `:92` (five i32 plus one i64 = seven dwords). Not changed.
- Line 71 and line 240 (35/37 byte-length prefix, count, then records): matches `inventory_v2_fixes.rs:74-88`. Not changed.
- Line 248 (35/34 with exactly one definition): matches `inventory.rs:1120-1124`. Not changed.
- Line 247 (coins in 38/19): matches `repo:prototype/osfr-tools/src/encounter/field_rewards.rs:326` and `inventory.rs:876-898`. Not changed.
- Line 80 and the Evidence section "Pieces 081" durable counter: matches `inventory.rs:41` (`pub mod instance_ids`) and `inventory.rs:1014`. Not changed.
- Client resource row counts (EquipmentSlotDefinitions 20 rows, CharacterCreate/ItemDefinitions 302 rows) were not verified; the resource folder is listed but I did not count rows.
- Line 232 and the 39-family row: not checked.
