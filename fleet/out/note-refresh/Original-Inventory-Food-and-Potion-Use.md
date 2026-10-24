<!-- fleet job=note-refresh id=Original-Inventory-Food-and-Potion-Use status=done turns=12 usd=0.0119 tokens(read,write,in,out)=[232808, 38239, 26, 9517] model=claude-haiku-5-5 -->
# notes/Research/Original Inventory Food and Potion Use.md

**Verdict:** badly stale in the "Current gap" section. The item bar (W146) is built and wired, so the note's claim that Rust has no consumable path is false. The Lua citations and the locale/catalogue claims I could check hold.

**Corrections:**

1. `old:` Current Rust intentionally no-ops42/6 and ignores bar2 in36/10;
   `new:` Current Rust handles 42/6 assignment and bar-2 36/10 activation for the item bar (W146);
   `why:` repo:prototype/osfr-tools/src/item_bar.rs:233-240 (42/6 → `assign`), item_bar.rs:272-278 (36/10 with bar id 2 → `activate`); routed before the chest/shared 42 branch at repo:prototype/osfr-tools/src/gameplay.rs:4439-4443. The gateway routes 42/6 as `item_bar` at repo:prototype/osfr-tools/src/gateway.rs:2097.

2. `old:` There is no normal client consumable workflow, saved actionbar binding, native slot refresh or health/size/potion effect implementation.
   `new:` The item bar is built but has never been run natively: four saved slots persist (repo:prototype/osfr-tools/src/gameplay.rs:1371), 38/25 slot refresh is sent for all four slots (repo:prototype/osfr-tools/src/item_bar.rs:284-295), and only the Small Health Potions 2173 and 11002 are usable, healing 35% of maximum health with a 10 s recast from a reconstructed (R) table (repo:prototype/osfr-tools/src/item_bar.rs:22-26, 79-86). Strong Arm Stew and the other catalogue consumables are refused with no effect; their original numbers remain unrecovered.
   `why:` repo:prototype/osfr-tools/src/item_bar.rs:22-26, 79-86, 322-328; repo:prototype/osfr-tools/src/gameplay.rs:5081-5112 (heal via `encounter.heal_player_percent`); Build Ledger row "Item bar and potion" at repo:notes/Design/Build Ledger.md:92 ("Built and wired (W146)... Never run natively").

3. `old:` 2. Implement only the proven owned-item assignment/slot presentation with exact packet framing and bounded slot IDs; no consumption yet.
   `new:` 2. The owned-item assignment and slot presentation are already implemented (W146), but they also consume on use; a native capture of the 42/6 and bar-2 36/10 flow is still needed.
   `why:` repo:prototype/osfr-tools/src/item_bar.rs:297-328 (assign), item_bar.rs:284-295 (refresh), item_bar.rs:27 ("A use consumes exactly one item"). Note that the plan step refers to work now done.

4. `old:` `Inventory::consume` is an internal atomic recipe/economy primitive.
   `new:` `Inventory::consume` is still the internal atomic primitive; the item bar calls its own consume path for a use (`item_bar.rs` consume at line 423), not a client-facing request.
   `why:` repo:prototype/osfr-tools/src/inventory.rs:1062 and repo:prototype/osfr-tools/src/item_bar.rs:423. Lower confidence on this one; I did not trace the full call chain, so only apply it if the call is confirmed.

**Checked and holding:**
- `ScriptsBase.lua:8816-8831` (equipItem, map 18 → `Ui.AssignToItemActionBar`) and `ScriptsBase.lua:30492-30494` (activateItem → `Ui.ClickedAbility(button-5, 2)`): verified in ui.
- Locale/catalogue entries: the consumable rows in `restoration/piece_046.rs:119-180` match the note's ability IDs (3264 Stew, 4696 and 4697 potions, 267 for 2173).

**Unsure:**
- Line 36: "2173 ... is absent from the current prepared catalog." `piece_046.rs:116-117,149` keeps 2173 as a recovered consumable row, and the item-bar default table uses 2173 (`item_bar.rs:79`). A search of `data/content` found no 2173 item definition, so the absence claim may be true in the data files only. The wording needs to say which catalogue is meant.
- Line 54: "Current saved candidate item records have `activate_enabled=false`." Test fixtures do set it false, but I did not find the saved candidate records themselves, so I could not confirm this.
- The `lab/reports/...` proofs, hashes, and the 2026-10-08 review receipts are outside the roots I can read; I did not check them.
