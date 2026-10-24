<!-- fleet job=note-refresh id=Pieces-041-Racer-and-derby-progression status=done turns=23 usd=0.0317 tokens(read,write,in,out)=[1219323, 94989, 50, 15306] model=claude-haiku-5-5 -->
# notes/Research/Pieces/041 Racer and derby progression.md

**Verdict:** minor drift. Most checkable claims hold at the tip. One recovered fact contradicts the Minigame Framework note, and one rank statement is loose. Budget ran out before I could settle the catalogue totals, so those are listed under Unsure.

**Corrections:**

1. Fact 7 (Outcome link). The claim that the star packet's payload is one byte is contradicted by the minigame framework's wire table.
   - `old:` `and its payload is a single` (line 55; the sentence continues "byte; the client's minigame datasource exposes `MiniGame_DS.EarnedStars`")
   - `new:` `and its payload is an \`i32\` total plus a \`u8\` flag (likely, per the framework table)`
   - `why:` `repo:notes/Build Guides/Gameplay/Minigame Framework.md:240` lists 21 (`0x15`) StarsEarned as `i32` total, `u8` flag, status "likely". `repo:notes/Native Map/Shards/S0272 009b7660-009bd590.md:219` also parses the body into id, new star count and flag. The same single-byte claim is repeated in `repo:prototype/osfr-tools/src/restoration/piece_041.rs:30-31` and `:84` (`MAX_STARS_PER_OUTCOME = u8::MAX`), so that code comment and the u8-clamp rationale need the same review. I did not edit code.

2. Fact 3 (Rank model). The gear catalogues do not both gate across a continuous 1..20.
   - `old:` `and both gear catalogues gate items across ranks 1..20.`
   - `new:` `and the Kart Driver gear catalogue gates items across ranks 1..20, while the derby gear catalogue skips rank 9 (see item 4).`
   - `why:` `repo:prototype/osfr-tools/src/restoration/piece_041.rs:132-176`. `KART_DRIVER_GEAR` has 20 rows, ranks 1..20; `DEMO_DERBY_DRIVER_GEAR` has 19 rows with no rank 9. The note's own item 4 states the gap.

**Checked and holding (no change needed):**
- `piece_041.rs` exists; `DriverProgression` with `credit`, `Duplicate`, `WrongJob`, `AtMaxRank`, `unlocked` and `unlocks_at` matches the description (`piece_041.rs:286-368`).
- `tests/piece_041.rs` has 11 `#[test]` functions and still includes the module via `#[path]` (`tests/piece_041.rs:10`). `src/lib.rs` has no restoration module, so "until the lead registers it" is still true.
- `tests/pieces/test_piece_041.py` has 13 test methods.
- `scripts/pieces/piece_041.py` exists; its expected constants match the note's job, gear, part and captured-vehicle facts (`piece_041.py:26-127`).
- The client Lua cap `if tonumber(rank) == 20` exists (`ui:ScriptsBase.lua:8201`, `:45696`).
- The Profile_DS `Rank`/`StarsAvailable`/`RankPercent` columns and `MiniGame_DS.EarnedStars` (index 6) exist. `JobLevelUp` is present (`ui:ScriptsBase.lua:11776`), and the star counter increments from `EarnedStars` (`ui:ScriptsBase.lua:6239-6244`).
- Locale 2917 is "Kart Driver" and 2919 is "Demo Derby Driver".
- The wiki "revision 43870" claim holds: `refs:freerealms-wiki/wikitext/1977-43870-1d6cbe06678d.wiki:2` says "The maximum of a job's level is 20 (level 4 if you are not a member for most jobs)".
- The six captured loadout ids, name ids, description ids, model indices and power ratings match `piece_041.rs:206-213`.

**Unsure:**
- The totals of 1,842 Kart Driver gear rows and 1,647 derby gear rows. They are in the note and the module, but the item catalogue is not in the repo, so I could not re-derive them.
- The `Cost` 540 on priced vehicle rows, and the "members-only" decals on the kart-part rows. I did not reach these.
- The checker's "40 checks pass" figure. It is a lab log I could not open.
- The "Reproduce" paths point at a lab tree (`C:\Users\Bryce\...`) that is not in this repo, so I could not confirm them.
- Cross-link targets. `007 Demolition derby.md`, `015 Minigame launch catalogue.md` and `031 Job catalogue.md` exist; I did not check `Kart Racing Restoration`, `Gameplay Coverage` or `Rust Revival Roadmap`.
