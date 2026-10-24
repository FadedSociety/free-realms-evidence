<!-- fleet job=note-refresh id=Pets-Service status=done turns=26 usd=0.0339 tokens(read,write,in,out)=[1196308, 84871, 54, 22698] model=claude-haiku-5-5 -->
# notes/Research/Pets Service.md

**Verdict:** minor-to-moderate drift. The core service rules (need decay, care amounts, minigame and in-water gates, dismiss sentinel, favourite slot range, species and name counts, client favourite sender) match the code. The wiring and integration status are stale: the note says pets is unregistered and unconnected, but gameplay and the gateway already use it.

**Corrections:**

1. `old:` standalone service module, intentionally not registered in `lib.rs`.
   `new:` service module, registered as `pub mod pets;` (`src/lib.rs:66`) and held by the gameplay session as `pets: crate::pets::PetService` (`src/gameplay.rs:256`); the gateway imports its presence helpers (`src/bin/osfr-gateway.rs:16`).
   `why:` repo:prototype/osfr-tools/src/lib.rs:66; repo:prototype/osfr-tools/src/gameplay.rs:256, 1144, 2073-2075, 2116-2135; repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:16.

2. `old:` Register `pets` and connect PetService to the player session after the local player object exists. Route the minigame and in-water state into its busy/care checks.
   `new:` PetService is already connected to the session (`gameplay.rs:256`, loaded by `load_pet_roster` at `gameplay.rs:2073`), and the minigame flag already reaches `PetBusy` (`gameplay.rs:2122-2123`). Still open: `set_in_water` (`pets.rs:1219`) has no caller outside `pets.rs`, so in-water state is not routed. Also `follow_location`, `care`, `play`, `learn_trick` and `set_favorite` have no caller outside `pets.rs`; `PetRequest::decode` accepts only subtypes 4, 6, 24 and 32 (`pets.rs:547-607`).
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:256, 2073-2075, 2122-2123; repo:prototype/osfr-tools/src/pets.rs:547-607, 1219; grep of `src/` for `set_in_water|follow_location|\.care\(|\.play\(|\.learn_trick\(|set_favorite` finds only definitions in `pets.rs`.

3. `old:` Translate `PetPresenceEvent` spawn/despawn/follow events into the actor replication path used by other players; the pet protocol guide does not establish those actor packets.
   `new:` Spawn and despawn already become shared packets in `PetService::wire` (`pets.rs:1160-1172`), and `pet_outcome` sends them to nearby players (`gameplay.rs:2109`). `Follow` events are still dropped there (`pets.rs:1170`), so follow replication is the remaining gap.
   `why:` repo:prototype/osfr-tools/src/pets.rs:1160-1172; repo:prototype/osfr-tools/src/gameplay.rs:2101-2111.

4. `old:` Saves with no pet payload remain schema 5; writing pet state bumps that envelope to 6.
   `new:` Saves with no pet payload and no gameplay snapshot remain schema 5; writing pet state bumps that envelope to 6. A save with a gameplay snapshot is written as schema 7 (`GAMEPLAY_SCHEMA_VERSION`).
   `why:` repo:prototype/osfr-tools/src/game_store.rs:15-18 (`PET_SCHEMA_VERSION` 6, `SCHEMA_VERSION` 7), 86-94 (the gameplay branch is checked first).

**Checked and holding** (no change needed): need decay 0.01 idle / 0.02 summoned and 0-100 range (`pets.json` need_policy; `pets.rs:1543-1548`); care restores 25/25/35 for 1835/1836/10521 (`pets.json` care_items); play toy +20 (`pets.rs:1244-1247`); minigame refusal for summon and care (`pets.rs:894`, `1314`); in-water refusal for care (`pets.rs:1321`); dismiss uses (0,0) (`pets.rs:963-965`); follow reply `can_go=true` (`pets.rs:1207-1209`); favourite slots 1-4 (`pets.rs:1415`); PetNames 60/250 with blank first row (`pets.rs:263-265`); 113 species IDs `1000001`-`1000113` (`pets.json`); favourite sender takes one-based UI slots and sends zero-based (client `00b5f670`: range `param_2-1 < 4`, `local_14 = param_2 - 1`); feed-sender gates `+0x1300` and `+0x143 & 0x20` (client `00b5f720`); `00ccecf0`/`00ccf3c0`/`00ccf260` are ControllerFishing functions (client labels); pet family 53 (`pets.rs:20`).

**Unsure:**

- `Final result: pets 7 passed, 0 failed` (the W26 run). `tests/pets.rs` now has 8 `#[test]` functions (lines 196, 221, 250, 311, 350, 364, 401, 422). The species-catalogue test at 422 is not in the note's test list at line 41. This may be a historical run, so I left the line unchanged.
- Counts in the W46c section (26 models, 16 adoption items, 113 rows with 26 model fields) could not be re-counted reliably. The search tool capped its results, so I confirmed only spot checks: 113 `species_id` values, `dog_large_stbernard.adr` as a model, and the three care item ids.
- Trick count (23) and the 147 waypoint rows were not counted. Spot checks show the trick entries have `waypoint_count` 3-15, which the validator enforces.
- The lead-adapter claim that the busy flag comes from `MinigameRuns` could not be confirmed. `gameplay.rs:2122` reads `self.blocks(|gates| gates.pets)`.
