<!-- fleet job=note-refresh id=Original-Cooking status=done turns=21 usd=0.0313 tokens(read,write,in,out)=[970885, 85138, 44, 21801] model=claude-haiku-5-5 -->
# notes/Research/Original Cooking.md

**Verdict:** Badly stale in its status prose. The code, path and packet claims hold at the tip, but the intro and the native-acceptance tail still say that native play, food reward, Close and restart are pending. Native runs 164218 and 171251 accepted them.

**Corrections:**

1. `old:` Six rounds of native mouse play, food reward, close and restart remain pending.
   `new:` Native runs 164218 and 171251 accepted six rounds of native mouse play and the food reward. Run 171251 also accepted the actual Close, the Mae turn-in and a post-reward restart.
   `why:` repo:notes/Reviews/Native Cooking Finish and Mae 171251.md:3 and :24-28 (six rounds, GameWon 5133, actual Close 26/42, Mae turn-in, restart172324). Build Ledger row "Crafting" (repo:notes/Design/Build Ledger.md:95) reads "Native-verified".

2. `old:` Native whole-recipe mouse play/reward remains pending in a fresh attempt.
   `new:` Native whole-recipe mouse play and the food reward were later accepted. Run 164218 completed all six rounds and granted food; run 171251 accepted the full finish. This sentence describes the superseded first attempt.
   `why:` repo:notes/Reviews/Native Cooking Finish and Mae 171251.md:3, :24-28; this note's own line 56 (164218 "All six original Cooking rounds completed").

3. `old:` actual parser tolerance remains an acceptance question. Capture real requests if the movie stalls. Native full mouse play and original reward/buff effects remain ahead.
   `new:` the final numeric `)` is now tolerated: one terminal `)` is stripped from StatUpdate and StopLevel values, and run 171251 accepted all 28 suffixed statistic fields. Native full mouse play is accepted (see the sections below).
   `why:` repo:prototype/osfr-tools/src/cooking.rs:467-469 (strip_suffix(')') on StatUpdate) and :560-562 (StopLevel); repo:notes/Reviews/Native Cooking Finish and Mae 171251.md:24.

4. `old:` Actual native phase/statistic transmission and the unusual FR_event quoting remain the next live gate.
   `new:` Native phase and statistic transmission was captured in runs 162238 and 164218, and the odd quoting is handled by the narrow `)` repair described below.
   `why:` repo:prototype/osfr-tools/src/cooking.rs:461-470 (suffix repair) and :486-489 (game-stat handling); repo:notes/Reviews/Native Cooking Launch 162238.md (phase rows sent, actual 39/5 start).

5. `old:` and the required fresh native acceptance branch.
   `new:` and native acceptance in run 171251, which accepted the actual Close, automatic ACK retention and the Mae turn-in.
   `why:` repo:notes/Reviews/Native Cooking Finish and Mae 171251.md:3 and :28; repo:prototype/osfr-tools/src/cooking.rs:381-385 (39/7 ignored) and :551-552 (GameClose cancels).

**Verified, no change needed:** scripts/prepare-cooking.py and its three `--allow-reconstructed-*` flags (lines 19-21); scripts/migrate-cooking-campaign.py (explicit source hash, NEW output, process check, only `gameplay.opening.content_sha256` changed); the 19 rejected transformations in scripts/check-cooking-migration.py:86; the six community vectors in tests/fixtures/cooking-community-vectors.json; stage order 1/2/3/6/17/7 and ingredients 10/24/40/49/46/46 (cooking.rs:22-23); Info/Start/Launch headers and `game_cooking.gfx` (cooking.rs:417, 591, 781); one food and four each of 2862/2875/2884/2900 for recipe 55824 (data/content/recipes.json:3260-3287); Student Chef Hat 14794 deferred only in the Cooking campaign (gameplay/jobs.rs:40); the 4 Bat Meat and 4 Spice supply on Chef steps 910004 and 910013 (gameplay.rs:2387-2405); Forging has no StatUpdate/StopLevel and keeps its GameOver handler (forging.rs:641); all links to the cited Reviews and Research notes resolve.

**Unsure:**
- "Six ordinary isolated tests ... pass" (line 15): tests/cooking.rs has 12 `#[test]` attributes, one of them `#[ignore]` (private), so 11 ordinary tests at the tip. I did not run them, and this may be a historical count.
- "Two explicit private gameplay checks" (line 15) and "3 private Cooking gameplay checks" (line 40): tests/cooking_gameplay.rs has 3 `#[test]`, two of them `#[ignore]`. Line 50's "9 private gameplay checks" does not match a single file. Left unchanged.
- "Ordinary Quit39/6 remains an explicitly separate cancellation acceptance item" (line 58): cooking.rs:386-400 handles sub 6 for pre-win runs. I did not read repo:notes/Reviews/Native Crafting Quit 005748.md, so I cannot say whether that acceptance is closed.
- Not in this note but stale: repo:notes/Research/Native Crafting Results Lifecycle.md:25 still says "Next native gate", which run 171251 has superseded.
- The gathering rule (line 13: only newly counted, nearby, ordered Chef gathers grant Rainleaf or Gummyfruit) was not traced in code.
