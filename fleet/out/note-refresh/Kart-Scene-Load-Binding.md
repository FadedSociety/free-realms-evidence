<!-- fleet job=note-refresh id=Kart-Scene-Load-Binding status=done turns=10 usd=0.0146 tokens(read,write,in,out)=[244625, 44278, 22, 13316] model=claude-haiku-5-5 -->
# notes/Research/Kart Scene Load Binding.md

**Verdict:** Moderately stale. The core observations (the `0xde2106fb` constant is not a scene selector, the encounter frames, 41/107 and 41/114 shapes) still hold against the tip. But the verdict and the "what selects the geometry" sections still say the scene binding is missing and point to `sanctuary.db`. The note's own Correction (lines 144-175) withdraws that and finds the op31 scene name, so the body contradicts the correction. The op31 scene name is carried in our code now; per-track scene selection is the part still missing.

**Corrections:**

1. `old:` The world/scene/geometry binding stays the specific missing piece. (wrapped across lines 29-30)
   `new:` The scene name is now carried by the op31 begin-zoning frame (`sg_kt_track` for kart racing). The missing piece is per-track scene selection: every gate starts the same `sg_kt_track` scene.
   `why:` repo:prototype/osfr-tools/src/kart_entry.rs:24-27 (the scene is named by opcode 31 through `zone_transition`; the `sg_kt_track` frame is built there); repo:prototype/osfr-tools/src/kart_entry.rs:580-594 (`scene()` / `scene_frame()`); repo:notes/Autopilot/T221.md:109 ("Per-track race scenes are not selected: every gate starts the shipped `sg_kt_track` scene").

2. `old:` Nothing inspected does.
   `new:` The op31 begin-zoning frame does: it names the scene (`sg_kt_track` for kart racing, with the spawn and sky). What is still missing is per-track scene selection.
   `why:` repo:prototype/osfr-tools/src/kart_entry.rs:24-27 and 580-594; repo:notes/Autopilot/T221.md:109.

3. `old:` A concrete external lead: the community `FreeRealms-Legacy` /
   Sanctuary server consumes a `sanctuary.db` database file for world data
   (`Sanctuary.Database` README) - that server-side DB, or the same table on a
   retail server, is where an encounter -> zone/scene binding would live; it is
   not present in this workspace.
   `new:` The `sanctuary.db` lead is withdrawn (see Correction 3). It is the Sanctuary emulator's own EF Core persistence DB and has no zone, scene or encounter table, so it is not where an encounter -> zone/scene binding lives.
   `why:` refs:Sanctuary/src/Sanctuary.Database/DatabaseContext.cs:9-18 (DbSet list: Users, Items, Titles, Mounts, Guilds, Friends, Ignores, Profiles, Characters, GuildMembers; no zone, scene or encounter set).

4. `old:` (only `FabledRealms.json`).
   `new:` (only `FabledRealms.json` in the Sanctuary pin; the Lxzxrus-Free-Realms-Server copy also carries `hsg_*` housing-lot zones and `*_fishing_*` zones).
   `why:` refs:Sanctuary/src/Resources/Zones (one file, `FabledRealms.json`); refs:Lxzxrus-Free-Realms-Server/src/Resources/Zones (about two dozen files, including `hsg_emptylot_*`, `hsg_hum_*`, and `*_fishing_*`).

5. `old:` ## What actually selects the race geometry
   `new:` ## What selects the race geometry (op31 names the scene; per-track selection is open)
   `why:` Same evidence as Correction 1; the heading otherwise implies nothing selects it, which the note's own correction at line 170 contradicts.

**Unsure:**
- Line 124 "the accepted entry candidate still does not make the race playable." `notes/Design/Build Ledger.md:103` says kart is native-verified (3 laps, reward paid, reload) via `realm race`, and that gate-NPC entry was built but never run natively. So "playable" depends on which entry path is meant. I did not settle this.
- Client counts and identities (MiniGameData 783 rows / 123 kart rows / `PRELOAD_FILE` empty; `Assets_manifest.txt` 162,653 rows; the 41/114 and 41/107 class ctor addresses; the 41/2 field layout). `MiniGameData.txt` exists in the client with the expected header, but I did not count rows or query the decompiled ctors. The repo's 41/2 encoder (repo:prototype/osfr-tools/src/kart_gateway.rs:613-617: encounter, instance, u64 session, flag 0) does not contradict the note's layout.
- The hash, manifest and `karts1.gfx` claims, and the `lab/` paths, are not in the repo and were not checked.
