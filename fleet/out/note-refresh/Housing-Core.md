<!-- fleet job=note-refresh id=Housing-Core status=done turns=29 usd=0.0334 tokens(read,write,in,out)=[1308222, 76060, 60, 21542] model=claude-haiku-5-5 -->
# notes/Research/Housing Core.md

**Verdict:** Badly stale in its status sections. The client-address and codec claims hold, but the enablement, gameplay wiring, asset-serving and warning statements were overtaken by later work (W39/W42, L030, the gameplay session). Six corrections follow.

**Corrections:**

1. `old:` `- No client lot/scene/spawn/build-box mapping; all bundled lots are disabled.` (line 129)
   `new:` `- No client lot/scene/spawn/build-box mapping; 22 bundled lots are enabled on reconstructed (R) joins and 9 stay disabled with a reason.`
   `why:` `prototype/osfr-tools/data/content/houses.json` has `"enabled": true` on property rows 1-6, 8-10, 14-22, 25, 29, 33 and 34 (e.g. line 999-1012 for property 25); the note's own "Enabled lots (R)" table (lines 238-270) and `notes/Autopilot/L030.md` (enabled count 21 -> 22) agree.

2. `old:` `The gameplay/gateway route is not wired, so live inventory and housing are not yet committed together by a caller.` (lines 105-106, joined by a space)
   `new:` `The gameplay session routes family 127 when `houses.json` is present and writes housing into the character state; a refused request changes neither the session nor the inventory.`
   `why:` `prototype/osfr-tools/src/gameplay.rs:2239` (`self.handle_housing(inner, character)`), `src/gameplay/housing.rs:81-96` (clones session and inventory, refusal changes nothing), `src/gameplay.rs:1377` (`housing: self.housing.as_ref().and_then(|h| h.state())`), `src/gameplay.rs:1147` (`HousingSession::load`).

3. `old:` `31 content rows have `scene: null` and `enabled: false`; entering one fails closed with`
   `new:` `the 22 rows joined in "Enabled lots (R)" below have a scene and `enabled: true`; the other nine keep `scene: null` and `enabled: false`. Entering a disabled row fails closed with`
   `why:` `prototype/osfr-tools/data/content/houses.json` (`"scene": null` / `"enabled": false` at lines 327-329 and 929 only; property 25 at lines 999-1012 carries a scene); `src/housing_service.rs:1371-1381` (`HouseSceneUnavailable` when disabled or sceneless).

4. `old:` `` `scripts/asset_delivery.py:29-31,63-91` supports only `.z` and `.gcnk`; ``
   `new:` `` `scripts/asset_delivery.py:23-65` indexes every safe manifest name from the extraction catalog and CRC-matched community sources (W42), so the admission rule is CRC match, not suffix; a trailing `.z` selects the compressed envelope (`:116-127`); ``
   `why:` `scripts/asset_delivery.py:23-27` (`_asset_name`), `:53-65` (catalog index keyed by name, CRC-checked), `:86-110` (loose-file index), `:122-127` (`.z` handling).

5. `old:` `- One pre-existing unused `Lot::instance_index` warning remains in `housing.rs`.`
   `new:` `- The unused `Lot::instance_index` warning from earlier slices is gone; no `instance_index` symbol remains in `src/housing.rs`.`
   `why:` `prototype/osfr-tools/src/housing.rs` (search for `instance_index` returns no match in that file; only `restoration/piece_046.rs:699-745` uses the name).

6. `old:` `1. Register `housing_service` in `lib.rs` and replace its temporary `#[path]` restoration include`
   `new:` `1. Done: `pub mod housing_service;` is at `src/lib.rs:32`, and no `#[path]` include of `housing_service` remains. The three restoration pieces still `#[path]`-include `housing.rs` (`restoration/piece_026.rs:54`, `piece_028.rs:69`, `piece_030.rs:55`).`
   `why:` `prototype/osfr-tools/src/lib.rs:32`; search for `#[path = .*housing` in `src` matches only the three `housing.rs` includes.

**Unsure:**

- Integration step 2 (line 115, "Add gateway ingress for family 127") and open gap line 136 ("No gateway registration"): family 127 is reached through `Gameplay` (correction 2), but `src/bin/osfr-gateway.rs` has no `housing` match, so I could not confirm the gateway binary reaches `Gameplay::handle_housing` for every session. Not corrected.
- Lines 300-302 (the W32-era `AssetDelivery.get` probe that found "no scene/area/cache source for Briarwood `.gzne`"): this predates W42's indexing, and the W39 section says the CRC-matched `.gzne` bodies are in the extracted packs (`catalog.tsv`). By the code the probe would now likely succeed, but I did not run it, so I left it as written.
- Client addresses checked against `client_sql` (`00ac3fe0` SendEnterRequestByGuid, `00ab6c80`, `00ac9dd0`, `00ab8ee0`, `00ac4160`, `00ac4200`, `00abffb0`, `00abc9a0`, `00abf620`, `00ac42d0`, `00ac4b80`, `00ab8dc0`, `00ac7f40`, `00ac1f50`, `00ac9bd0`, `00ac36c0`, `00abcb90`, `00aafa90`, `00ab8c50`, `00aab1a0`, `00aae6b0`): all resolve to the names the note gives. Line-number citations into `Housing.md` (lines 46-51, 94-102, 188-205, 230-249) were not checked.
- Constants checked and matching: starter property 25 (`houses.json:4`, `grant_starter_lot` at `housing_service.rs:1061`), cap 9999 and landmark 0 (`houses.json:975-976`), `RECONSTRUCTED_HOUSE_UNUSED = 10` and `RECONSTRUCTED_FLORA_ALLOWED = true` (`housing_service.rs:106-108`), `SERVICE_SCHEMA_VERSION = 2` (`:95`, a different counter from the save schema), `EnterHouse`/`ReturnToPreviousZone` (`:220`, `:228`), `offer` (`:1212`), 31 rows in `houses.json`, `tests/save_schema.rs` schema-4 migration test.
