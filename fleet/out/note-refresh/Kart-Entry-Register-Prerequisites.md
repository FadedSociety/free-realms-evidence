<!-- fleet job=note-refresh id=Kart-Entry-Register-Prerequisites status=done turns=23 usd=0.0226 tokens(read,write,in,out)=[622471, 56315, 48, 18597] model=claude-haiku-5-5 -->
# notes/Research/Kart Entry Register Prerequisites.md

**Verdict:** badly stale. The pseudocode facts (the `FUN_00ba5eb0` branch structure, the two callers, the `0x1be` offset) still hold. But the note's "missing link" and its "actionable" checks were closed at the tip, and the note never records that.

**Corrections:**

1. `old:` **Actionable missing prerequisite: the LOCAL ACTOR STATUS BITS at
   `new:` **Former missing prerequisite (now sent by the tip): the LOCAL ACTOR STATUS BITS at
   `why:` `repo:prototype/osfr-tools/src/kart_gateway.rs:591-594`. `initialize()` already sends `player_status(context.session, 0x401)` before the register, and the comment says bit 10 activates `VehicleRaceProcessor`, whose start branch sends `33/9`. Also `notes/Reviews/Kart Playable Integration.md:37` and `:43` (222147 run: client `33/9` at 88.671 s).

2. `old:` | register | 33/9 at t=+0.069 s after the entry burst | **absent** |
   `new:` | register | 33/9 at t=+0.069 s after the entry burst | **absent in v2 220503Z only**; the tip sends `0x401` (35/20) before the register and the 222147 run logs `33/9` at 88.671 s |
   `why:` `repo:prototype/osfr-tools/src/kart_gateway.rs:594`; `repo:notes/Reviews/Kart Playable Integration.md:43`.

3. `old:` link, and it is a client-side state transition, not an absent reply packet.
   `new:` link. It is the `35/20` status carrier with flags `0x401`, sent before the register at frame 15451 (repeated 15496). The tip now sends it.
   `why:` `repo:prototype/osfr-tools/src/kart_gateway.rs:591-594`; `repo:notes/Reviews/Kart Playable Integration.md:37`.

4. `old:` strongest hypothesis, now with the register identified as a processor-start
   `new:` no longer the lead. The review found the definition blobs are "not proved blockers", and the tip's `0x401` status fixed the register path without them.
   `why:` `repo:notes/Reviews/Kart Playable Integration.md:37` (and `:43`, "not the worker's missing-definition or scene-id hypotheses").

5. `old:` begin-zoning path that would reset the race controller and send `33/9`.
   `new:` begin-zoning path. That path only tears the controller down (`FUN_00ba5eb0(0)`, per the note's own correction), so skipping it cannot withhold `33/9`.
   `why:` `repo:prototype/osfr-tools/src/kart_gateway.rs:592-593` ("zoning's reset(0) only tears it down"); `repo:prototype/osfr-tools/src/kart_gateway.rs:593` and the note's own correction at lines 89-97.

6. `old:` Actionable check for the root: send the scene with the original tail `id`
   `new:` Superseded. The tip still sets `scene.id = instance_id` (`repo:prototype/osfr-tools/src/kart_gateway.rs:560`), and the 222147 run reached `33/9` with that tail, so this is not the register gate.
   `why:` `repo:notes/Reviews/Kart Playable Integration.md:43`; `repo:prototype/osfr-tools/src/kart_gateway.rs:560`.

7. `old:` GUID-bearing `41/2` **after** `Loaded 10`/the register, not before it.
   `new:` GUID-bearing `41/2` **after** `Loaded 10`. The tip now sends it from `loaded()` (`41/2` with the session GUID, plus `41/107`), so this is implemented, not missing.
   `why:` `repo:prototype/osfr-tools/src/kart_gateway.rs:604-624`, especially `:613-617`.

8. `old:` **Exact unresolved pointer (one read):** the `switch` variable above 1383500
   `new:` **Resolved at the tip:** `case 0x6b` is encounter sub-op 107, the bare `41/107` (EncounterZoneIsReady) packet. The code comment says native `case 0x6b` calls `HandlerMiniGameStart:setReady` after decoding it. The remaining sentences of this paragraph are superseded.
   `why:` `repo:prototype/osfr-tools/src/kart_gateway.rs:618-619`. The native map labels `ParseEncounterBody_SubOp107` a downgraded hypothesis (`notes/Native Map/Shards/S0313 00a9d3c0-00aa24e0.md:310`), so cite the code comment as the source, not the native map.

**Checked and holding (no correction):**
- `zone_transition.rs:57-58` ("Zone instance id") matches the note.
- `scene.id = instance_id` (48000001) is set by `kart_gateway.rs:560` and `:310`.
- The character's `zone_id` becomes 48000001 after the scene zoning (`gateway.rs:1771-1774`).
- The `FUN_00ba5eb0` branch structure and the two callers (`0092f460`, `0093d180`) match the client decompile.
- `0x1be` × 4 = `0x6f8`, so `actor+0x6f8` is right.

**Unsure:**
- Line numbers in the pseudocode (1583600, 1094460-1094510, 1207153, 1383528) are export line numbers. I could not map them to function addresses. The `FUN_009b0cc0` callers in the client DB are `009bf5e0` and `00aa36c0`, which does not obviously match the "exactly one caller" and the three-site list at lines 213-228.
- The bit 10 / bit 19 test at 1094460 was not isolated in `0092f460`. The Kart Racing guide (line 43) agrees with the note.
- `Native Map/Shards/S0282` says the note's `FUN_009f1b80` (line 123) is derby, not kart. The note does not call it kart, so I left it alone.
