<!-- fleet job=note-refresh id=Pieces-043-Pet-trainer-and-card-progression status=done turns=24 usd=0.0235 tokens(read,write,in,out)=[803619, 57074, 50, 16722] model=claude-haiku-5-5 -->
# notes/Research/Pieces/043 Pet trainer and card progression.md

**Verdict:** minor drift. The code-side claims hold (paths, registration, test counts, the Lua table, the locale blocks, the Card Duelist rows). Two asset claims about shipped data are false.

**Corrections:**

1. Old: `levelup_tcg.gfx` and the per-job audio `levelup_{pettrainer,cardduelist}_level{1,5,10,15,20,_misc}.mp3`;
   New: `levelup_tcg.gfx` and the Card Duelist audio `levelup_cardduelist_level{1,5,10,15,20,_misc}.mp3.z`; no Pet Trainer `levelup_pettrainer_level*.mp3` row is shipped (only `levelup_pettrainer.gfx` and `levelup_pettrainer.lst.z`);
   Why: repo:`client:Assets_manifest.txt:161287-161292` lists only the `levelup_cardduelist_*` mp3 rows. A case-insensitive search for `pettrainer` across the manifest finds only the `.gfx`/`.lst.z` (lines 14227-14228) and badge/clothing rows. The same mistake is in the module doc at repo:prototype/osfr-tools/src/restoration/piece_043.rs:21-22.

2. Old: its 256px badge tier entries are unrecovered.
   New: the 256px Pet Trainer badge tiers are shipped (`icon_job_badge_pettrainer01..05_256`). The 256px Card Duelist tier 04 is shipped too. The "256 missing" findings come from the lab catalogue, not the shipped tables.
   Why: repo:`client:Resources/Images/Images.txt:4509, 4512, 4515, 4518, 4521` (pettrainer01-05 _256) and `:4364` (`icon_job_badge_tcg04_256`); repo:`client:Assets_manifest.txt:106275, 106278, 106281, 106284, 106287` (pettrainer _256) and `:106374` (tcg04_256). The checker's `tcg-badge-tier04-256-missing` and `pettrainer-badge-256-missing-in-pack-catalog` (repo:scripts/pieces/piece_043.py:385-407) read `manifests/rust-asset-catalog.tsv` (lab, `INPUT_PATHS`, line 53), which is outside the repo and could not be checked here.

**Checked and holding:**
- `piece_043.rs` exists; `lib.rs` does not register it (repo:prototype/osfr-tools/src/lib.rs:1-102).
- `tests/piece_043.rs` has 13 `#[test]`s and `#[path]`-includes the module (repo:prototype/osfr-tools/tests/piece_043.rs:33-35, 13 test attributes).
- `tests/pieces/test_piece_043.py` has 13 `def test_` methods; `scripts/pieces/piece_043.py` exists.
- The ledger behaviour matches the note: replays are refused, Abandoned and Lost credit nothing and do not consume the instance, and the non-member cap is 4 (repo:piece_043.rs:430-568, 580-581).
- The Lua claims match: `JobLevelUp` at ScriptsBase.lua:11776, badge set list at :11790-11804, `t[1783]`/`t[1785]` at :11813-11814, messages 919922/919923 at :11783-11787, sound rows `s[1783]`/`s[1785]` at :11870-11881 (16114 and 16119-16123 confirmed in the client).
- `FUN_0089b240` installs `PacketSendSelfToClient::vftable` and writes 0xc (client fn table).
- Locale: 34070-34074, 34110-34114, 34150-34154 and 34190-34194 exist; 2410 is "Card Duelist"; 17419 is "Pet Trainer"; 2436 and 4624 are Pet Trainer gear and achievement strings. Id 919922 returns "no such id", which matches "absent from the export".
- Refs: `Profiles.json` has Card Duelist at Id 120 with BadgeImageSet 1783 (FreeRealms-Legacy, line 1560-1565). No Pet Trainer row (no 1785 BadgeImageSet, no 17419 NameId).
- The cross-linked pieces 010 and 011 exist. The piece_011 trick rounds and piece_010 card matches match the note.

**Unsure:**
- The "16/16" catalogue match, the recorded profile values (job 120, level 20, 0 XP), and the `pseudocode.c:1099444` citation all point to lab files (`lab/working`, `lab/references`, `lab/decompiled`) that are outside the repo. I could not check them.
- The native five-value `JobLevelUp` dispatch is in `FUN_009392c0` (client fn table, which contains the string "JobLevelUp"). The argument count is consistent with the note, but I did not verify the exact five-value layout.
- The audio-to-sound level mapping (1/5/10/15/20 vs 1/4/8/12/16) is left open by the note. The client confirms only the Card Duelist audio names; see correction 1.
