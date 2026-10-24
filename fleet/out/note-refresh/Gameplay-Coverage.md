<!-- fleet job=note-refresh id=Gameplay-Coverage status=done turns=14 usd=0.0200 tokens(read,write,in,out)=[450713, 67228, 30, 14224] model=claude-haiku-5-5 -->
# notes/Research/Gameplay Coverage.md

**Verdict:** badly stale in the minigame and lifestyle rows. The login, inventory, quest and checkpoint rows I spot-checked still match the tip. The rows for soccer, racing/derby, jobs/crafting, housing/pets/mounts and other minigames now contradict the code and the Build Ledger.

**Corrections:**

1. `old:` `| Original racing/derby | Original partial traces | Partial; racing has four sequence gaps | Not yet | Trace analysis only | Not launched against Rust |`
   `new:` `| Original racing/derby | Original partial traces | Partial; racing has four sequence gaps | Kart racing built; derby wired through the NPC menu and derby session | Not measured here | Kart racing native-verified (3 laps, 50 coins and 25 XP paid once, reload); derby not run natively |`
   `why:` `notes/Design/Build Ledger.md:103` (Kart "Native-verified (3 laps, 50 coins and 25 XP paid once, reload)"); `notes/Design/Build Ledger.md:108` and the derby entry in the Ledger's minigame table; `prototype/osfr-tools/src/gateway.rs:509-514` (families 26/33/41/102 routed as "kart", family 34 routed to "derby"); `prototype/osfr-tools/src/gameplay/derby_session.rs:1-3,112-132`. The "four sequence gaps" claim is not re-checked here.

2. `old:` `| Original soccer | Original arena/config/team/ball/goal captures | Partial lifecycle | Not yet | Capture CRC/schema checks only | Not launched against Rust |`
   `new:` `| Original soccer | Original arena/config/team/ball/goal captures | Partial lifecycle | Rust soccer session and service: soccer.rs, soccer_match.rs, soccer_service.rs, soccer_entry.rs; family 76 routed as "soccer" | Soccer test suites (soccer_entry, soccer_service, soccer_match, soccer_quest_credit) per Autopilot F226/F364 | Not verified natively (see Unsure) |`
   `why:` `prototype/osfr-tools/src/gateway.rs:515-518`; `prototype/osfr-tools/src/gameplay.rs:3289-3311` (`begin_soccer` starts a `soccer_entry::Session`); `prototype/osfr-tools/src/soccer.rs:1-19`; `notes/Autopilot/F226.md` and `notes/Autopilot/F364.md` (soccer_entry and soccer_quest_credit suites passing).

3. `old:` `| Jobs, crafting, gathering, collections | Some surviving presentation/data | Not measured | No gameplay restoration | No | No |`
   `new:` `| Jobs, crafting, gathering, collections | Some surviving presentation/data | Crafting and gathering behavior partly understood | Crafting (cooking, smelting, forging) and mining/harvesting wired; collections built, not routed | Per-system tests (e.g. tests/gathering_nodes.rs) | Crafting native-verified (opening tutorial only); mining and harvesting wired, whole-round native acceptance open |`
   `why:` `notes/Design/Build Ledger.md:95` (Crafting "Native-verified, opening tutorial only"), `:97` (collections "Built ... Not routed"), `:104-105` (Mining and Harvesting "Wired"); `prototype/osfr-tools/src/cooking.rs`, `smelting.rs`, `forging.rs`, `mining.rs`, `harvesting.rs` exist.

4. `old:` `| Housing, pets/mounts, social, travel, multiplayer | Partial data/UI only | Not measured | No gameplay restoration | No | No |`
   `new:` `| Housing, pets/mounts, social, travel, multiplayer | Partial data/UI only | Mounts and pets: owned rides and pet requests routed; social chat wired | Mounts wired (family 168); pets routed (family 53); social chat and lists wired; player registry native-verified; housing built, not routed | Mount and ride tests per the Ledger | Mounts natively unseen; player visibility native-verified 2026-10-15; housing not routed |`
   `why:` `prototype/osfr-tools/src/gateway.rs:520` (family 168 "mounts"), `:523` (family 53 "pets"); `notes/Design/Build Ledger.md:43` (player registry native-verified), `:44` (chat, friends, groups wired), `:108` (mounts wired, never run natively), `:109` (housing "Built (registered, not routed)"); `prototype/osfr-tools/src/mounts.rs`, `pets.rs`, `social_chat.rs` exist.

5. `old:` `| Other original minigames | 783 MiniGameData references and UI/assets | Unknown coverage | No | No | No |`
   `new:` `| Other original minigames | 783 MiniGameData references and UI/assets | Coverage partly mapped (restoration/piece_015.rs) | Partly: chess built; fishing, mining and harvesting wired; the rest not implemented | Per-system tests | Chess, fishing, mining and harvesting not run natively; others No |`
   `why:` `prototype/osfr-tools/src/restoration/piece_015.rs:7` (783 rows, the count is correct); `notes/Design/Build Ledger.md:104-107` (Mining, Harvesting, Fishing wired; chess "Built" under :109); `prototype/osfr-tools/src/chess.rs`, `fishing_service.rs`, `harvesting.rs`.

**Unsure:**
- **Soccer routing conflict.** `notes/Design/Build Ledger.md:109` says "Soccer, chess, derby, housing, pets | Built (registered, not routed)", but `gateway.rs:515-518` routes family 76 and `gameplay.rs:3289-3311` starts a soccer session. I could not find a native soccer run. Left as "not verified natively" in correction 2 pending the Ledger owner.
- **Quest 1617 "Matching disabled until evidenced".** `prototype/osfr-tools/src/restoration/piece_068.rs:26` says the router "never guesses a target for an objective such as 1617/14096". But `scripts/prepare-gameplay-quests.py:144-147` writes `enemy_definition: args.petty_yeti_definition` into the goals. I did not confirm the runtime behaviour, so the row is left as is.
- **Item categories (71 categories / 74 associations, 44/2 exact match, 2,675-byte oracle)** and **inventory counts (1,386 instances, 16 profiles)**: I did not find these figures in `prototype/osfr-tools/src/item_categories.rs` or the notes. `notes/Build Guides/Gameplay/Character and Customization.md:227` mentions 16 profiles as an earlier count. Not settled.
- **"Equip instance 2/profile 1/slot 4" and "native unequip appearance not accepted yet"**: not checked.
- **"46 private templates remain"**: consistent with `notes/Design/Build Ledger.md:39` (46 captured templates loaded and hash-checked), but I did not confirm the count in code.
