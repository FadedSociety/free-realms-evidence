<!-- fleet job=guide-refresh id=World-Movement-and-Pathfinding status=nothing_found turns=11 usd=0.0153 tokens(read,write,in,out)=[275983, 54018, 24, 11591] model=claude-haiku-5-5 -->
# notes/Build Guides/World/Movement and Pathfinding.md

**Verdict:** current. The note is a generated map of client functions. It makes no claims about our server code, routing or build status, and the claims I could check against the decompiled client hold.

**Checked and consistent:**
- Totals: 150 functions, 60 confirmed, 50 likely, 23 speculative, 17 unknown. I re-tallied every table row by confidence and got the same numbers. The Build Guides index line (`notes/Build Guides/Build Guides.md:44`, "150 functions (60 confirmed, 50 likely)") agrees.
- Subsystem counts (`game.movement` 53, `world` 45, `world.pathfinding` 25, `world.proximity` 16, `world.camera` 8, `world.railcamera` 3) sum to 150 and match the rows. The source-shard counts on line 342 also sum to 150.
- Network-linked count of 5 matches the 🌐 rows: 00bf9430, 009cd010, 009cd2f0, 009cd6c0, 009cd410.
- Client-side descriptions checked against `client_sql` `fn.c` and `label` records:
  - 008a7840 SetZoneType: the 0/1/2/3 mapping matches.
  - 008b3180 GetEntitySpeed: matches.
  - 008fdb80 MovementManager constructor: matches.
  - 00b09e20, 00b09e30, 00b09e40, 00b09e90: literal and static-data returns match.
  - 00b09eb0 SetReadyFlagWhenArgumentZero: matches.
  - 00b09ec0 ClearLoaderStateFields: matches.
  - 00b0a290 ReadSphereCenterAndRadius: offsets 0x1e0 to 0x1f0 match.
  - 008c5a10 PositionDeltaGate_Check: matches.
  - 0095f700 ComputeScaledSpeedFactor: matches.
  - 00963550, 00963670, 00963700: bit operations match.
  - 0107fb50 ZeroInitRecord0x30: matches.
  - 008bb440 ResetController: the helper calls with 1 and 0 match.
  - 01077910 MovementController::DtorBody: matches.
  - 010bc310 RoadMap::DtorBody: matches.
  - 010bc210 NodeGraphRemoveNode: ret 4 and the call sequence match.
  - 00bfc190 ResetTargetData: constant 0x017efda8 matches.
  - The label records for the pathfinding and camera entries (009cd010, 009cd2f0, 009cd6c0, 009cd410, 010bbdc0, 010bcf60, 010bb850, 008ee710, 0107fb90) match the names and subsystems in the note.
- The narrative section says "Not written yet". That is an accurate placeholder status, not a false claim.

**Unsure:**
- `00bfc3e0` (ProxiedCharacterSeekMovementController cleanup): the note says it calls 0101b370 with ECX=this+0x1c. The pseudocode shows only a cookie-like argument and does not show the ECX value, so I could not confirm the ECX detail.
- The `[[S0156]]`-style shard links on line 342 point to shard notes that are not in `notes/`. They may live in an external index, so I could not verify them.
- I did not re-check the per-row "What it does" prose for every one of the 150 functions. I sampled about 40 across all sections.
