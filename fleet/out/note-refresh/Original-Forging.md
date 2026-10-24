<!-- fleet job=note-refresh id=Original-Forging status=done turns=21 usd=0.0241 tokens(read,write,in,out)=[747152, 73532, 44, 14861] model=claude-haiku-5-5 -->
# notes/Research/Original Forging.md

**Verdict:** badly stale on native status (two sentences say native play is pending; the reviews say it was accepted). The code-level claims I checked (board, quota, timers, packet IDs, StopLevel/OnNextLevelMsg ordering, 39/18 GameOver, chain minimum, gravity order, migrator path and guards, campaign-marker binding) are current.

**Corrections:**

1. `old:` **Native entry, drag play, win and exit are still pending.** The packet simulation does not establish that the real movie renders or completes against Rust.
   `new:` **Native play is recorded for the opening Forging139 run.** `Reviews/Native Forging Victory 181715` shows 18 actual native chains, five quota drops, `OnGameWonMsg`, the delayed `FRServer_GameOver` followed by the 39/18 → 39/47 → 39/19 burst, the player's 26/42 Close, and one atomic output (Hammer 30280). `Current Progress.md` records a native Forging run with ordinary mouse chains (run 103605). Later restart and migrated-save gates remain open.
   `why:` repo:notes/Reviews/Native Forging Victory 181715.md:5-7; repo:notes/Current Progress.md:92; repo:notes/Build Guides/Gameplay/Minigame Framework.md:24 (client completed Forging 139 end to end); repo:notes/Design/Build Ledger.md:95 ("Native-verified"). Code side: repo:prototype/osfr-tools/src/forging.rs:435 (Start 39/17), :598 (StopLevel on quota), :624-638 (single reward intent), :1175-1182 (GameOver 39/18).

2. `old:` Next native gate: original139 entry/tutorial, real drag chains, queue/gravity without desync, hammer collection/mold fill, normal score/exit, fixed ingredient consumption and one output/quest update, restart, then native Brawler equip of the forged hammer.
   `new:` Native gates for entry, drag chains, queue/gravity, hammer/mold, score/exit, consumption, one output/quest update and the Brawler equip of the forged hammer are recorded in `Reviews/Native Forging Victory 181715`. Still open per that review: the final capture, a restart, and later stage7 gameplay.
   `why:` repo:notes/Reviews/Native Forging Victory 181715.md:13 ("Final capture, later stage7 gameplay and restart still require their own gates") and :15 (Brawler equip of forged hammer, `[31,43,7]`).

**Unsure:**

- "The full ordinary Rust suite passes128 tests with23 explicit private oracles ignored." `notes/Current Progress.md:132` gives a later-looking figure of 154 ordinary tests passing and 29 private checks ignored. I could not date either count, so I did not replace it.
- "Verification: 9 ordinary forging tests." `prototype/osfr-tools/tests/forging.rs` has 15 `#[test]` functions, one of them `#[ignore]` (line 705), so 14 ordinary there. Other forging tests are in `tests/forging_gameplay.rs`, `gameplay/t013_objective_events.rs`, and `gameplay/s6_characterization.rs`. The scope of "9" is not clear from the note, so I left it.
- "Native 26/42 closes without dungeon zoning." I found the forging 26/42 handling (`gameplay/movie.rs:33-43`, `forging.rs:398-406`) but no zoning code path to confirm or refute the negative claim.
- The "six golden packet vectors" and "fifteen complete item definitions" are in the private lab and could not be checked from the repo.
- The board values (8x8 at left/top 3 inside 14x14, three colors, 10% hammer, quota 5, 180 s, mold 6) match `scripts/prepare-forging.py:64-67` and `forging.rs:20-25`. The "tuning is reconstructed" framing matches `prepare-forging.py:54-60`.
