<!-- fleet job=note-refresh id=Mounts-Service status=done turns=30 usd=0.0387 tokens(read,write,in,out)=[1425394, 89606, 62, 26420] model=claude-haiku-5-5 -->
# notes/Research/Mounts Service.md

**Verdict:** Current, with one stale server-trigger claim. The code, file paths, test names, data counts and the wire and packet facts I could check all match the tip. The one error is that the note treats an ability start as a server-side dismount trigger; the code has no such trigger.

**Corrections:**

1. `old:` Zoning, a fight, a knockout, a Flash minigame start and an ability start use the same call (server triggers R, minigame and ability from the client's own 168/3).
   `new:` Zoning, a fight and a knockout use the same call on the server side (`settle_mounts`, `gameplay.rs:2056`, which checks zoning, the ride gate and knockout). An ability start is not a server trigger: `on_ability_use` (`mounts.rs:552`) has no production caller, and `ability_active` is always `false` (`gameplay.rs:2009`), so an ability dismount comes only from the client's own 168/3. A Flash minigame start also comes only from the client's own 168/3 unless it falls in the ride gate (see Unsure).
   `why:` `repo:prototype/osfr-tools/src/mounts.rs:552` (the only definition; the only callers are in `tests/mounts.rs:383`); `repo:prototype/osfr-tools/src/gameplay.rs:2009` (`ability_active: false`) and `:2056-2064` (`settle_mounts`); `repo:prototype/osfr-tools/src/gameplay/occupation.rs:154-155` (ride gate = Encounter, Derby, Soccer, Kart, FieldEngaged, Housing).

**Checked and current (no change):**
- `src/mounts.rs`, `data/content/mounts.json`, `tests/mounts.rs`, `tests/mount_routing.rs`, `tests/mount_follow.rs`, `tests/mount_wired.rs` and `tests/mount_bots.rs` all exist. `scripts/native_map/nmq.py` exists.
- Family 168 is routed in `gameplay.rs:2242` (`handle_mounts`, `:2030`). Interest fanout uses `with_rides` and `ride_follow` in `bin/osfr-gateway.rs:731-766`.
- The 30 mount types (29 positive ids) and 54 mounts are asserted in `tests/mounts.rs:133-135`. Top-level `mount_type_id` is null throughout, and `members_only`, `is_upgraded` and `seat_count` are false, false and 1. The Lawn Chair has `max_movement_speed: 0.0` (`mounts.json:5605`).
- The one-second spawn guard is `SPAWN_DEBOUNCE_MS = 1_000` (`mounts.rs:22`, `:373-381`). The ride GUID is `owner ^ 0xc000…` (`mounts.rs:19`, `:711-713`).
- The request decoding matches the note: 168/1 board, 168/3 dismount, 168/6 spawn and 168/8 spawn by item. Other sub-opcodes are not answered (`mounts.rs:578-596`).
- Dismount is one step: `dismount_request` sends 168/4 for a mounted rider, sends remove-actor `35/3` (`mounts.rs:836-841`) and refreshes the roster (`mounts.rs:507-541`).
- The AddPc mount block is `u64 guid, i32 seat, i32 queue, f32 lift` (`players.rs:805-810`). `set_mount` exists at `players.rs:332`, and `MountTail::NONE` is (0, -1, -1, 0.0) (`mounts.rs:628-642`). `SEATED_QUEUE = 1` and lift 0.0 when seated (`mounts.rs:27`, `:666-673`).
- `RideView::follow` returns `None` for an unseated ride (`mounts.rs:683-693`), and `tests/mount_routing.rs:404-440` covers it.
- Emotes are blocked while mounted (`gameplay.rs:1991`, `gateway.rs:1323`, `social_chat.rs:485`).
- Ride speed is not sent to the client: `MaxMovementSpeed` appears only in `restoration/piece_047.rs`, not in the mount path.
- Trials and the other sub-opcodes (168/9-15) are not implemented (`mounts.rs:578-596`).

**Unsure:**
- **Speed comparison (line 80):** the gateway validates movement at `base_speed_per_second: 10.0` with `mount_multiplier: 1.0` (`repo:prototype/osfr-tools/src/gateway.rs:1528-1529`). The fastest ride in the data is 12.5 (`mounts.json`, many rows). `movement.rs:17-20` has soft and hard multipliers of 40 and 80, and the gateway comment (`gateway.rs:1519-1521`) calls the envelope "generous". I could not settle whether "far wider than the fastest ride" holds. The "(12.5 against 10)" wording also reads ambiguously.
- **Flash minigame start (line 65):** `ride_restrictions` maps the ride gate to Encounter, Derby, Soccer, Kart, FieldEngaged and Housing (`occupation.rs:154-155`). I found no Flash-minigame occupation in that list, so I did not assert whether a Flash minigame triggers a server-side dismount.
- **"Only 24 of the 54 rides" (line 55):** I found no code-level check. `notes/Reviews/Native Checklist 2026-10-16.md:655` says the same number. `tests/station_cash.rs:404` asserts 54 catalogue rows, but that is a different count.
- **`lab/runs/client-baseline-…` paths (line 12):** the `lab/` tree is not in the repo, so I could not check the path or the SHA-256. Other notes and pet data cite the same run directory.
