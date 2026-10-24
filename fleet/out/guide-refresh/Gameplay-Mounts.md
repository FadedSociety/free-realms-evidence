<!-- fleet job=guide-refresh id=Gameplay-Mounts status=nothing_found turns=29 usd=0.0352 tokens(read,write,in,out)=[1484563, 92104, 62, 17573] model=claude-haiku-5-5 -->
# notes/Build Guides/Gameplay/Mounts.md

**Verdict:** current on the client-side claims I checked; the server-side items are directives ("must do"), not status claims, and I found no sentence that is now false as written. I stopped at the tool budget before checking every address.

**Corrections:** none with a verified exact replacement.

**What I checked and found consistent:**
- Client mount-type table: `AnimationTypes.xml` (client Resources, lines 48-78) has ids 1-29 with the prefixes and descriptions the note lists, and "Qudraped" is the file's spelling. The note's "29 rows" holds (id 0 is the empty row).
- `Models.txt` has the two hoverboard mount rows; `ContentPacks.txt` row 25 "Rides/Mounts" is unlocked in 13 columns; `CodeStringMappings.txt` has `Mounts_ToolTip` and `membership_mount_deluxe`.
- Locale: "Mount Trial will end in %timeLeft minutes.", "Obtain 25 mounts.", "Tandem Mount Test", the "3-step program" text and the five Glide Training step names all exist.
- Client functions: `00b06100` dispatches sub-opcodes 2,4,5,9,10,11,13,15 (label); `00bffbc0` is `Mount::Upgrade` sending sub-opcode 14; `00b038c0` is the PacketMountSpawn constructor on sub-opcode 6; `00a2e540` returns 1 only for an elapsed value below 1000 and non-negative (pseudocode matches); `00bffa60` (Dismount) and `00bff8e0` (Despawn) both send 168/3 and differ in the button-reset argument, with Despawn taking one Lua argument, as the note says.
- Generated-section counts: the subsystem and confidence counts for `net.mount` (60) and `game.mount` (18), 28 confirmed, 32 likely, 1 speculative, 17 unknown, match the label table.

**Server-side observations (not corrections, since the note words these as requirements):**
- `prototype/osfr-tools/src/mounts.rs:731-776`: inbound handling covers only 168/1, 3, 6 and 8 (`decode_request`, lines 578-596). There is no handler for 168/9, 10, 11, 13, 14 or 15, so upgrades and trials are not wired.
- `mounts.rs:852` and `gameplay.rs:2028-2051`: the ride list is sent only after a spawn, dismount, refusal or minigame/zone settle. No login path includes it, so note item 3 ("include the mount list in the self packet") is still open.
- `mounts.rs:543-559`: `on_minigame_start` and `on_ability_use` are defined; `on_ability_use` has no caller in `src/`. `gameplay.rs:2004-2014` sets `ability_active: false`, so ability-start dismounts are not wired, though minigame and zone end are (`gateway.rs:1374`).
- `mounts.rs:496-535`: 168/4 is sent on dismount only when the rider was mounted. The note's item 6 ("reply with 168/4") is therefore stricter than the code.
- `data/content/mounts.json` exists (7081 lines, `mounts` array from line 335) with legacy and reconstructed sources. The note's item 2 says to derive the roster from design, which is now partly done. I did not count the entries.

**Unsure:**
- Whether `mounts.json` holds 54 rides (Build Ledger line 108 says so); I did not count the array.
- Whether the mount list is sent elsewhere at login: I found no mount reference in `startup_selfdata.rs`, but did not read the self-packet builder fully.
- Whether `Mounts.md` item 9's "end the ride on ability use" is meant as wired; the note does not say it is.
