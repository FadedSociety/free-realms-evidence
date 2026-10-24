<!-- fleet job=note-refresh id=Stage7-Native-Return-Routes status=done turns=15 usd=0.0145 tokens(read,write,in,out)=[397154, 43510, 32, 10116] model=claude-haiku-5-5 -->
# notes/Research/Stage7 Native Return Routes.md

**Verdict:** minor drift. Most checkable claims hold at the tip. The one stale claim is the closing Pappy→Bartle status, which predates the run-193318 descent proof.

**Corrections:**

- `old:` No successful native Pappy→Bartle route was recovered.
  `new:` No complete native Pappy→Bartle walk is accepted. Run 193318 retains a reverse native descent and input prefix that reaches the known climb foot `[-2142.506,-56.058884,300.35257]`, but the descent, road and approach beyond it remain unaccepted. The current next candidate is [[Pappy to Bartle Main Road Detour]].
  `why:` `notes/Research/Pappy to Bartle Main Road Detour.md:3` (retained 193318 descent/input proof, climb foot reached, "Do not call the static road chain collision-free"); `:5` ("Native walking still needs bounded inspection"). `notes/Research/Pappy to Bartle Route Candidates.md:5` says the Main Road Detour "supersedes the rejected cliff route as the next candidate", which this note does not mention. The `Route Candidates` note's "No Pappy→Bartle walking history was recovered from 151602" (line 42) is still true, because that run's history is only the Pappy-side climb.

**Checked and holding:**

- Both linked notes exist: `Farnum Stage7 Route Geometry` and `Anvil Placement Repair Proposal`.
- The anvil move `[-2084,-55.6,190]→[-2088,-54.79,200]` is in `scripts/anvil_placement.py:25` and `prototype/osfr-tools/tests/fixtures/quests/opening.json:369-370`.
- The opening content hash `4e6ac15c…0ad1` (`scripts/anvil_placement.py:22`) and the `rust-opening-forging-assets` name (its own opening hash is `cef51222…`, in `notes/Research/Original Forging.md:25`) are used consistently with the note.
- The 181715 tree stop `[-2098.401,-52.621204,423.78705]` is recorded in `MODLOG.md:341`.
- Pappy's position `[-2184.513,-31.53728,328.1112]` matches `prototype/osfr-tools/data/content/npcs/farnum_farmstead.json:5473`.
- The 12 m interaction radius matches `prototype/osfr-tools/src/npc_interaction.rs:52`.
- The 090058 arrival was a Magic Door transition (`notes/Reviews/Native Farm Travel 090058.md:7`).
- 151602 completed the Pappy turn-in, which `notes/Reviews/Native Farm Completion 151602.md:7` confirms.

**Unsure:**

- All the `C:/Users/Bryce/.../lab/reports/*.json` proofs, their SHA256 values, the "31 source hashes" and "303/426 rechecked bindings" counts, `lab/reports/finalize-stage7-return-route-review.py`, and the 151602 manifest contents. The lab directory is not in the repo or refs roots, so I could not check them.
- The sub-metre geometry figures (grades, normal Y, clearances, the "1.191 units" log rejection) are only in those external proofs, so I did not verify them.
- The claim that Pappy's 1.6 m final distance is "inside his 12m interaction radius" relies on the 12 m constant, which I confirmed for the generic NPC interaction path, not for Pappy's row specifically.
