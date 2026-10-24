<!-- fleet job=note-refresh id=Mining-Completion status=done turns=28 usd=0.0244 tokens(read,write,in,out)=[888632, 62474, 58, 15300] model=claude-haiku-5-5 -->
# notes/Research/Mining Completion.md

**Verdict:** minor drift. The code claims hold at the tip: the 40% / 6+6 / seed 18 / 180 s default, the 25 Miner XP constant, the 2739 output mapping, the `minigame-run:<instance>` grant key, the 39/6 Quit path, the three-test lifecycle file, the 96-chain assertion, and the `mining::lifecycle` exposure. Two statements need fixing: one citation points at the wrong lines, and one "(R) in its rule notice" wording is off.

**Corrections:**

1. `old:` see [[Current Progress]] lines 33 and 37
   `new:` see [[Current Progress]] lines 68, 187, 200 and 207 (the Mining 151307 entries) and [[Reviews/Mining Native 151307 Final Review]]
   `why:` `notes/Current Progress.md:33` and `:37` are kart checkpoints with no Mining content. The 85-chain, `[2,0]`, wall-cap Lost record is at `notes/Current Progress.md:68,187,200,207` and `notes/Reviews/Mining Native 151307 Final Review.md:11,31`.

2. `old:` marks the balance and output mapping `(R)` in its rule notice.
   `new:` marks the balance and output mapping as reconstructed in its rule notice (`reconstructed_rules: true`; the notice reads "40% collectable rate, 6+6 quotas, seed, item mapping and Miner XP are local tuning"). The literal `(R)` tags are code comments at the output mapping and the XP constant.
   `why:` `prototype/osfr-tools/src/mining.rs:1020` (the `(R)` comment above `outputs`), `:1041-1042` (`reconstructed_rules: true` and the rule notice text, which has no "(R)"), and `prototype/osfr-tools/src/mining_lifecycle.rs:19` (the XP `(R)` comment).

**Checked and holding (no change needed):**
- `mining.rs:1037` `collectable_percent: 40`; `:1008-1016` quotas 6 and 6 with per_reward 1 and 2; `:1034` `duration_seconds: 180`; `:1035` `seed: MINING_GAME_ID as u32` with `MINING_GAME_ID = 18` at `:49`. The shipped `data/content/mining.json:16,17,22-30,51` agree.
- `mining.rs:1162-1163` rejects `quota % per_reward != 0`.
- `mining.rs:1024-1031` maps both 601 and 602 to definition 2739, quantities 1 and 2.
- `mining_lifecycle.rs:22` `RECONSTRUCTED_MINER_XP_PER_WIN = 25`, applied in `:427`.
- `minigame.rs:581` `format!("minigame-run:{instance_id}")`; `mining_lifecycle.rs:361-364` returns CollectItem events plus `FinishMinigame { minigame_id: 18 }`.
- `minigame.rs:353-367` Quit (39/6) returns `state_remove_packet` (39/19) only; `minigame.rs:781-782` 39/19 is the removal packet.
- `minigame.rs:372-395` Close (26/42) moves Won/Lost to Closed. `mining_lifecycle.rs:331-296` ignores repeated terminal movies unless they are `FRServer_GameClose`.
- `mining.rs:44-46` declares `pub mod lifecycle` via `#[path = "mining_lifecycle.rs"]`, and `lib.rs:54` exposes `pub mod mining`.
- `tests/mining_lifecycle.rs` has 3 `#[test]` functions (lines 438, 503, 536). The seeded driver asserts 96 actions (`:445`), `remaining_ms > 0`, and `wall_ms <= 600_000`.
- `tests/mining_move_detection.rs:166-167` holds the ignored `chain21_snapshot_with_no_legal_path_must_reshuffle`. `tests/mining_review.rs`, `mining_shape_parity.rs` and `mining_tile_rendering.rs` exist.
- `mining.rs:67-76` and `:263` back the claim that powerups 950–953 are clickable and only 950..=953 are honoured, so 900–902 are deferred.

**Unsure:**
- The wiki-link line ranges into other notes (`Mining Starting Round Playable Candidate` lines 18–30, 44–53, 55–68; `Mining Restoration` lines 3–35; `Minigame Lifecycle` 11–36; `Minigame Framework` 54–71, 108–115, 292–310; `Native Gear Up and Smelting 173814` line 32; `Research/Pieces/013 Smelting recipes/content.md` lines 81–82) were not checked. The 85-chain / 340 s figures do match `notes/Reviews/Mining Starting Round Candidate Review.md:39`.
- The client-side claims (Iron labels, tile frames, `39/x` reader addresses) were not checked against `client`/`ui`.
- The "85 chains in 340 modeled seconds" study is reported in the Review note, not in the Playable Candidate note I was pointed to, so I could not confirm the cited lines.</result>
