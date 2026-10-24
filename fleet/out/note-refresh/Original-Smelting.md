<!-- fleet job=note-refresh id=Original-Smelting status=done turns=31 usd=0.0364 tokens(read,write,in,out)=[1603286, 85846, 64, 19211] model=claude-haiku-5-5 -->
# notes/Research/Original Smelting.md

**Verdict:** badly stale in the status headline and one economy number is wrong. The file/packet/gate claims I checked mostly hold; native entry, win and Close have since been accepted, and the win grant is five bars, not ten.

**Corrections:**

1. `old:` **Native entry/play/win is still pending.** Packet simulation is not evidence that the movie loads or its real controls work against Rust.
   `new:` **Native entry, play, win and Close are now accepted for the opening Smelting (captures 173814 and 103605).** The packet simulation is supporting evidence only.
   `why:` `repo:notes/Reviews/Native Gear Up and Smelting 173814.md:11` (client 39/5, server 39/17 and 26/12 for `game_smelting.gfx`), `:28` (OnGameWonMsg, 39/18, 39/19), `:32` (actual native Close, frame 8935); `repo:notes/Current Progress.md:92` (run 103605 completed the Smelting stage).

2. `old:` Numeric tuning and the fixed ten-bar output are reconstructed; the movie's hardcoded GameWon quantity10 is not proof of an authoritative economic rule.
   `new:` Numeric tuning is reconstructed. The server grants the recipe row's five-bar output (`miner.copper_bar.sample`), and the movie's hardcoded GameWon quantity10 is only a validation cap, not proof of an authoritative economic rule.
   `why:` `repo:prototype/osfr-tools/src/smelting.rs:764-765` (`product_quantity: row.output.count`), `:494` (quantity only capped at 10), `:514` (grant uses `recipe.product_quantity`); `repo:prototype/osfr-tools/data/content/recipes.json:3550-3553` (output count 5). `scripts/prepare-smelting.py:68` writes `product_quantity: 10` into `smelting.json`, but `Content.recipe` (`smelting.rs:70-74`) reads only `key`, so that value is ignored.

3. `old:` Winning consumes5 Copper Ore and3 Singing Coal, grants10 Copper Bars and advances the five-bar objective from the server transaction once.
   `new:` Winning consumes5 Copper Ore and3 Singing Coal, grants 5 Copper Bars and advances the five-bar objective from the server transaction once.
   `why:` `repo:prototype/osfr-tools/src/smelting.rs:514` and `:764-765` (grant = recipe output count, 5 per `data/content/recipes.json:3550-3553`); `repo:prototype/osfr-tools/src/gameplay/crafting.rs:368-379` (objective quantity = 21785 grants); `repo:notes/Autopilot/F193.md:311` ("exactly the server-owned five bars").

4. `old:` Next acceptance: native furnace entry, all four stages, normal score screen, material consumption/output, quest turn-in and restart.
   `new:` Native acceptance of the opening Smelting is recorded (173814: furnace entry, win, Close, Gear Up turn-in; 103605: repeat smelt and opening completion). The restart gate is not checked by this note.
   `why:` `repo:notes/Reviews/Native Gear Up and Smelting 173814.md:11,28,32`; `repo:notes/Current Progress.md:92`.

**Checked and holding (no change):**
- Packet IDs: Info 16 (`smelting.rs:564`), Payload 14 (`:658`), Start 17 (`:402`), StartFlash 26/12 (`:795-797`), GameOver 18 (`:694`), Remove 19 (`:333`, `:716`).
- Furnace: a click on the Miner Craft2002 trigger starts the tutorial craft and no longer completes the goal (`gameplay.rs:4533-4541`); profile 14 (`smelting.rs:17`).
- Blocked actions while the movie runs (`gameplay/movie.rs:55-56`); 26/42 cancels without zoning (`gameplay.rs:4277-4282`; `gameplay/crafting.rs:18-50`).
- Reconnect keeps `next_instance_id` and `completed` and cancels the active run (`gameplay.rs:1718-1724`).
- Gathering drops 2739×1 and 879×1 on a raised count with Miner profile 14 (`gameplay.rs:4758-4764`).
- Test names and commands: `tests/smelting_gameplay.rs:76-78` (ignored private test); `tests/opening_gateway.rs:139` (17 stages) and `:16-17` (movie helper).
- Script flag `--allow-reconstructed-phases` (`scripts/prepare-smelting.py:22,26-27`) and `--merge-material-definitions` (`:23`).

**Unsure:**
- "six isolated ordinary tests and the old-save serde test pass": `tests/smelting_gameplay.rs` has one ordinary `#[test]` (`:18-19`, the old-save test) and one ignored private test (`:76-78`). The other five were not located, so I could not confirm the count.
- "Info preloads the existing `SmeltingAssets.txt` with278 CRC-matching entries", the inventory SHA values, and the backup path are in the lab, not in the repo. I did not verify them.
- "Class/equipment/world interactions are blocked" is checked only for the blocked-message path (`movie.rs`), not for every interaction route.
