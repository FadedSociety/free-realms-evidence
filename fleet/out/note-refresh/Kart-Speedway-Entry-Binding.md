<!-- fleet job=note-refresh id=Kart-Speedway-Entry-Binding status=done turns=13 usd=0.0126 tokens(read,write,in,out)=[310836, 44803, 28, 7839] model=claude-haiku-5-5 -->
# notes/Research/Kart Speedway Entry Binding.md

**Verdict:** minor drift. The POI, job and encounter-id claims hold. Two source citations in the reconstruction paragraph point at lines that no longer hold that code, and one description overstates what the 41/114 builder writes.

**Corrections:**

1. `old:` (`src/encounter.rs:458-461`)
   `new:` (`src/encounter.rs:1500-1503`, in `EncounterEngine::on_zone_ready`)
   `why:` repo:prototype/osfr-tools/src/encounter.rs:1500-1502 emits `encounter_header(2, d.id, active.instance_id)`, then `enter.extend(1_u64.to_le_bytes())` and `enter.push(0)`, so the `u64 = 1` claim is still true. Lines 458-461 are now a doc comment on the `FieldEnemy` `quest_ids` field (encounter.rs:457-461).

2. `old:` (`src/encounter.rs:1055-1093`)
   `new:` (`src/encounter.rs:2661-2723`, `fn details_packet`)
   `why:` The range 1055-1093 is now inside `EncounterEngine`'s constructor (encounter.rs:1057-1099). The 41/114 builder is `details_packet` at encounter.rs:2661-2723, and `encounter_header(114, ...)` is at encounter.rs:2672.

3. `old:` and the reconstructed `41/114` zero-fills the const/u64/spawn fields
   `new:` and the reconstructed `41/114` (`details_packet`) zero-fills its reward, objective and flag blocks; it writes no spawn triple and no `0xde2106fb` constant
   `why:` repo:prototype/osfr-tools/src/encounter.rs:2672-2720. The packet has zero i32 runs, `[1, 0, 1]`, `prize_bundle`, and `[0, 1, launch]` tail bytes, with no float spawn field. The kart path (repo:prototype/osfr-tools/src/kart_gateway.rs:528-541) does not zero-fill either; it patches the captured `details_loading`/`details_ready` templates' instance and session bytes. The "spawn" wording is the part I would not trust.

**Checked and holding:**
- Five POIs (31, 32, 33, 34, 39) and their LocationId/TeleportLocationId: the Sanctuary and Lxzxrus copies agree on 202678/210046 and the position for POI 32 (refs:Sanctuary/src/Resources/PointOfInterests.json:392-400; refs:OpenSourceFreeRealms/ofrserver/Customize/PointOfInterestDefinitions.json:430-440).
- Kart Driver profile 48 and Demo Derby Driver profile 49 (repo:prototype/osfr-tools/data/content/jobs.json:612, 815). Both have max_level 20.
- No community entry for encounter `917566` or `1310785` (refs, `*.json`: no matches).

**Unsure:**
- The `41/114` spawn-triple and `0xde2106fb` claims come from the lab capture and the pinned reproducer, which are not in the repo. I could not verify them.
- The POI breadcrumb and heading values and the Chase Wheeler and trainer wiki claims are outside the repo, so I did not check them.
- The `lab/reports/...` artifact paths and hashes are not present in the repo, so I did not check them.
