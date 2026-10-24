<!-- fleet job=note-refresh id=Card-Game status=nothing_found turns=30 usd=0.0364 tokens(read,write,in,out)=[1497160, 95647, 64, 18910] model=claude-haiku-5-5 -->
# notes/Research/Card Game.md

**Verdict:** current. I found no statement about our code or project status that is now false. The note's repo-facing claims hold at the tip.

**Corrections:** none.

**Checked and holding:**
- `prototype/osfr-tools/src/restoration/piece_010.rs` exists. `TcgMatch`, `from_snapshot`, `MatchError`, and the 38/40/18/47/21 packet constants are there (piece_010.rs:37-48, 343, 415-450).
- `piece_010` is not registered in `prototype/osfr-tools/src/lib.rs` (no `restoration` or `piece_010` match). The note's "not registered in `lib.rs`" holds.
- No wire codec in piece_010.rs: only `pub fn` helpers for classification, parse and the match model. The "named reward-card hook" (`reward_card`, `parse_reward_card`, lines 219, 318) is present.
- `tests/piece_010.rs` has 18 `#[test]` functions, matching "18 behavioral tests".
- `piece_043.rs` has `OutcomeSource::TcgMatch` mapped to `ProgressionJob::CardDuelist` (lines 252, 289, 575).
- The proposed `card_*.rs` modules do not exist, which is consistent with the note calling them "proposed". `minigame.rs` exists (its run lifecycle is generic, with no TYPE 16/23 admission yet).
- `GatewayCommand_GetConnectionServer` (414) and the 411/81/103 login and lobby commands have no code in `prototype/osfr-tools/src`. This is consistent with the note's "unrouted" and "no route added yet" framing.
- `Autopilot/T031.md` matches the note's scope: no Rust changed, no gateway route, no playable claim. F123 already corrected the 546/575 boundary.
- Client-side citations hold: ScriptsBase.lua 12857-12862, 13708-13714, 14535-14546, 19034-19041, 54329-54406 all match the note's line anchors.
- `Resources/MiniGameData.txt` anchors match: row 387 at line 371, 499 at 419, 537 at 457, 727 at 637 (type 23), 1036 at 703, 9997 at 782. The file has 783 data rows plus a header. "Battle Cards" does not occur in the client.
- Build Guide anchors: the Trading Card Game overview, launch, data, network and server-requirement sections fall where the note cites them. Matchmaking and Lobby card lobby is at 125-149. Minigame Framework rows at 129, 162, 175 are inside the cited 129-185 range.
- Wiki links (Research/TCG Client Protocol, Research/Pieces/010, Build Guides/Gameplay/Trade, Build Guides/Content/Jobs/Card Duelist) resolve to existing files.

**Unsure:**
- The DLL SHA-256 and 8,990,720-byte size, the DLL's default hosts and ports (lvsccg-01-02/01 on 17782/17783), and the 21782/21783 Treasure War ports. These live in the lab or the binary, and I could not hash or search them with the available tools.
- The TYPE 16 count of 124, the TYPE 3 count of 4, and the asset counts (TradingCardAssets 45 `.lst` / 151 `.dds`; SimpleCardAssets 62 / 244). My search results were capped below the full row count, so I could not recount them.
- The 546/575 rows sit at Build Guide lines 139 and 197, outside the note's cited "network lines 154-182". The note does not cite those lines for 546/575 itself, so I did not treat this as a correction.
