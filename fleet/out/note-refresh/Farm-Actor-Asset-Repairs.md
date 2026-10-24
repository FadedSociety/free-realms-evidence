<!-- fleet job=note-refresh id=Farm-Actor-Asset-Repairs status=done turns=8 usd=0.0092 tokens(read,write,in,out)=[128406, 35958, 18, 6873] model=claude-haiku-5-5 -->
# notes/Research/Farm Actor Asset Repairs.md

**Verdict:** minor drift. The repair data (model 3519 well, model 204 fires, fire 3 at Y -55.65, the well at the local quest position) matches the code. One sentence is stale: it still says the native farm visuals need play, but a later run has played them and a review accepted them.

**Corrections:**

1. `old:` Native appearance, target selection and extinguishing still need actual play after the separately reviewed migration.
   `new:` Native appearance, target selection and extinguishing were then proven by actual play in run 151602: the well and all three fires were selected in authored order, each fire removal was recorded, and Pappy's turn-in completed the quest. Gloam-colored flame appearance remains unproven ([[../Reviews/Native Farm Completion 151602]]).
   `why:` `repo:notes/Reviews/Native Farm Completion 151602.md:3,7,9` (accepts the reconstructed well and three fires, with the 16 well/campfire dependencies passing the hash/CRC checks and original Gloam flame appearance still unproven). Also `repo:MODLOG.md:256` and `repo:notes/Current Progress.md:124`.

2. `old:` Run 090058 cannot accept the well and fire visuals.
   `new:` Run 090058 could not accept the well and fire visuals; later run 151602 accepted the reconstructed well and three fires.
   `why:` The 090058 failure is correct as history (`repo:notes/Reviews/Native Farm Travel 090058.md:13`). The present tense now misleads, because `repo:notes/Reviews/Native Farm Completion 151602.md:3` accepts those visuals.

**Checked and holding:**
- Repair data: `repo:prototype/osfr-tools/tests/fixtures/quests/opening.json:153-244` has the well as `farming_well_01.adr`, model 3519, at `[-2113, -56.5, 222]`. The three fires are model 204 `bw_campfire_01.adr`, and fire 3 sits at `[-2124, -55.65, 237]`, which matches "Only that fire moves vertically, to -55.65."
- Original placements: `repo:scripts/prepare-opening-content.py:87-93` has the same well and fire positions with fire 3 at -56.5, so the note's "old Y" claim is consistent.
- Original model IDs: `repo:prototype/osfr-tools/data/content/npc_spawns_extra.json:59250-59307` maps Npcs 6433 to ModelId 3097 (`hsg_well_01.adr`) and the campfire to ModelId 204.
- Forging variant: `repo:scripts/prepare-forging-campaign.py:33-54` takes an optional `--asset-repairs` proof under `lab/`, and `repo:scripts/forging_campaign_proof.py:18` checks it. This matches "restricted to a new forging variant."

**Unsure:**
- `sg_well_01.adr` at `[-2196.748, -31.475924, 324.771]`, the `-56.6594975`/`-56.5658735`/`-56.7464775`/`-55.703051` floors, the `[-2154.1, 286.5]` approach, the dependency counts (six and ten), and the CRC/envelope claims all live in `../lab/` artifacts that are not in the repo. I could not verify them.
- The "Universal Modder" and "gateway audit" ownership lines are process claims with no repo evidence either way.
