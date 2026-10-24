<!-- fleet job=note-refresh id=Player-Visibility status=done turns=14 usd=0.0157 tokens(read,write,in,out)=[308895, 44236, 30, 14180] model=claude-haiku-5-5 -->
# notes/Research/Player Visibility.md

**Verdict:** Badly stale in the Implementation and Lead-integration sections. The packet facts (35/2 NPC builder, 35/1 AddPc and 35/3 remove layouts, opcode 125 shape, `[sin, 0, cos]` direction, envelope) and the reconstructed policy section still match the code. The registry is no longer isolated: the gateway binary already wires it in.

**Corrections:**

1. `old:` Candidate selection uses an O(n²) scan; `ponytail:` it is suitable for the small bounded registry tests, with a spatial index only if zone population makes it necessary.
   `new:` Candidate selection uses a uniform 3D cell grid as the broad phase (`cells`, `cell`, `nearby`), then exact f64 distance and the per-viewer cap. Cached directed sets (`views`) limit rebuilds to affected viewers.
   `why:` repo:prototype/osfr-tools/src/players.rs:189-190 (cells and views fields), 419-476 (`cell`, `insert_cell`, `remove_cell`, `nearby` with the 5x5x5 neighbourhood), 592-590 `refresh_views` (cached rerank).

2. `old:` `Gateway::handle_at` saves its position/rotation at lines 642-654 and returns replies only to that connection. It does not fan movement or actor lifecycle messages to other sessions.
   `new:` `Gateway::handle_at` (gateway.rs:1409) returns replies only to that connection; the opcode-125 arm is in `parse_message` (gateway.rs:616-629). Fanout is wired one layer up in `src/bin/osfr-gateway.rs`: `join_player` calls `join_with_presentation` (602-620), movement calls `update_pose_with_state` and maps its deliveries (1857-1873), and disconnect calls `leave` (689-699). Nearby-player fanout is in `ride_fanout` (706-716).
   `why:` repo:prototype/osfr-tools/src/gateway.rs:616-629, 1409; repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:466, 602-630, 689-699, 706-716, 1857-1873. Lines 642-654 of gateway.rs are now the Camera/Time/fallback arms of `parse_message`.

3. `old:` Register `players` in `src/lib.rs` and include the scoped test in the root test target; this worker used `#[path]` and did not edit shared registration.
   `new:` `players` is already registered (`pub mod players;`), and the scoped test is `tests/players.rs`, which the gateway binary and other tests use directly. Step 1 is done.
   `why:` repo:prototype/osfr-tools/src/lib.rs:68. `#[path]` appears only in tests/load_players.rs:60, not in the players registration.

4. `old:** 5. Replace the current zero/empty AddPc profile defaults with authenticated character presentation data. The current gateway character state does not supply all AddPc appearance/profile fields.`
   Use the text without the bold markers: `5. Replace the current zero/empty AddPc profile defaults with authenticated character presentation data. The current gateway character state does not supply all AddPc appearance/profile fields.`
   `new:` `5. Authenticated presentation is wired: `Gateway::player_presentation` (gateway.rs:1033) feeds `join_with_presentation` (osfr-gateway.rs:611, 1849-1850) and `set_presentation` (osfr-gateway.rs:1838). Guild, title, and persistent-effect fields are still hard-coded zero in `build_add_pc` (players.rs:798-814).`
   `why:` repo:prototype/osfr-tools/src/gateway.rs:1033; repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:611, 1838, 1849-1850; repo:prototype/osfr-tools/src/players.rs:798-814.

5. `old:` AddPc appearance, name IDs/strings, model, membership, guilds, title, mount, speed, and related fields default to zero/empty because the registry input has no character profile.
   `new:` AddPc appearance, name IDs/strings, model, membership, guilds, title, mount, and related fields default to zero/empty, except max movement speed, which defaults to 10.0 (the gateway's base speed), because the legacy `join` wrapper supplies no character profile.
   `why:` repo:prototype/osfr-tools/src/players.rs:73-95 (`Default for PlayerPresentation`: `max_movement_speed: 10.0`, `attachments_wire: vec![0; 4]`), 255-257 (legacy `join` wrapper).

6. `old:** — 7 passed, 0 failed.` (the command line in "Commands and results" is followed by this text; use the substring `— 7 passed, 0 failed.`)
   `new:` `— 7 passed, 0 failed when recorded. tests/players.rs now has 14 `#[test]` functions, so re-run for the current count.`
   `why:` repo:prototype/osfr-tools/tests/players.rs `#[test]` lines at 203, 260, 272, 336, 393, 406, 429, 449, 491, 531, 550, 586, 638, 704.

**Unsure:**

- The note's line "The crate emitted one pre-existing `housing.rs::Lot::instance_index` dead-code warning" and the test-binary path under `lab/build/W13` are build-log facts. I did not run a build, so I could not check them.
- The World and Network Build Guide placeholder claim and the four guide links: the Actors and NPCs, Movement and Pathfinding, Command System, and Gateway and Transport pages exist under `notes/Build Guides/`. I did not read their contents.
- The client-side addresses (`0091d000`, `00921a10`, `0092f460`, `008e5940`, `0090de90`, `0095dae0`) are client evidence, not repo code, so I did not check them.
- `set_mount` and the ride fanout (osfr-gateway.rs:1876-1884, players.rs:330-341) are new since the note. The note does not mention them, so they are not a correction, but the snapshot is now behind on mounts.</result>
</invoke>
