<!-- fleet job=note-refresh id=Go-Kart-Native-Integration-Readiness status=done turns=12 usd=0.0163 tokens(read,write,in,out)=[241144, 39224, 26, 18064] model=claude-haiku-5-5 -->
# notes/Research/Go Kart Native Integration Readiness.md

**Verdict:** badly stale. The note describes the kart work before the registration, gateway-binding and lobby-codec integration landed. Its launch order and recovered-capture facts still hold, but its integration status and blockers are largely wrong at the current tip.

**Corrections:**

1. Row 22 (`src/kart_racing.rs`)
   - `old:` unregistered module, 13 builder tests + 12 review tests green
   - `new:` registered in `src/lib.rs:46`; 14 builder tests + 12 review tests green
   - `why:` repo:prototype/osfr-tools/src/lib.rs:46 (`pub mod kart_racing;`); notes/Autopilot/F207.md:174 (`kart_racing` 14 passed, `kart_review` 12 passed)

2. Row 23 (`tests/kart_racing.rs`, `tests/kart_review.rs`)
   - `old:` `#[path]` harness | the module is not in `src/lib.rs` and not referenced by `src/gateway.rs` (proof `current_wiring`)
   - `new:` plain crate import (no `#[path]`) | the module is in `src/lib.rs:46`; `gateway.rs:509` routes 33 and 102/1 by name only, and the module is consumed through `kart_gateway.rs` and `gameplay.rs`
   - `why:` repo:prototype/osfr-tools/tests/kart_racing.rs:8 and tests/kart_review.rs:9 (`use osfr_tools::kart_racing::…`); src/lib.rs:46; src/gateway.rs:509; src/gameplay.rs:2273-2285

3. Step 1 of "Minimum production wiring"
   - `old:` 1. Register `kart_racing` (lead-owned `src/lib.rs`) and route inner opcodes 102/141/33 from
   - `new:` 1. Done at tip: `kart_racing` is registered (`src/lib.rs:46`), and 33 and 102/1 are routed to the kart handler (`gateway.rs:509`) and dispatched in `gameplay.rs:2273-2285` (`handle_kart_entry`). 141/1, 3, 13 go to matchmaking (`gateway.rs:491`).
   - `why:` repo:prototype/osfr-tools/src/lib.rs:46; src/gateway.rs:491, 509; src/gameplay.rs:2273-2285

4. Blocker context, lines 40-41 ("gateway binding")
   - `old:` id, who may send checkpoints) does not exist yet.
   - `new:` id, who may send checkpoints) is enforced in `kart_gateway.rs`: GUID and session checks on the vehicle/session frame and the return location. `kart_racing.rs` still cannot verify ownership alone (its header says so).
   - `why:` repo:prototype/osfr-tools/src/kart_gateway.rs:269-286, 308-314, 496; src/kart_racing.rs:48-49

5. Row 32 (`018 Minigame native test routes`)
   - `old:` no launch route
   - `new:` launch routes now exist: the `realm race` dev command and gate-NPC menus (`kart_gates.json`, default-gated)
   - `why:` repo:prototype/osfr-tools/src/gameplay.rs:2276-2285 (`realm race` with `dev_tools`); src/kart_gateway.rs:1-9 (gate NPC menu, 26/9 → 26/10)

6. Step 2 (102/1 → 102/2)
   - `old:` the remaining catalogue rows and trailing blocks are unrecovered, so this is the first
   - `new:` the lobby body is encoded by `kart_lobby_native.rs` from the caller-authored `kart_lobby.json` and replied to 102/1 only under `dev_tools`; real catalogue rows remain unrecovered, so a real lobby still needs recovered content. This is the
   - `why:` repo:prototype/osfr-tools/src/gameplay.rs:1043-1061 (load), 2299-2312 (102/1 reply); src/kart_lobby_native.rs:10-16 (five tables, counts `[6,30,43,37,17]`)

7. Lines 60-62 (community encoder comment)
   - `old:` trailing blocks are not decoded, so the community encoder is a subset and must not be shipped as the
   - `new:` trailing blocks are decoded as five typed tables by `kart_lobby_native.rs` (counts 6/30/43/37/17); the community encoder is a subset and must not be shipped as the
   - `why:` repo:prototype/osfr-tools/src/kart_lobby_native.rs:10-16, 28-30 (the codec supersedes the 140-byte subset, which is still the community writer)

8. Blocker (a), line 122
   - `old:` (a) the full 102/2 framing
   - `new:` (a) recovered 102/2 catalogue content (the framing is coded in `kart_lobby_native.rs`; client tolerance of trailing bytes is unproven)
   - `why:` repo:prototype/osfr-tools/src/kart_lobby_native.rs:22-26 (strict/tolerant trailing-byte policy, unproven client behaviour)

9. Blocker (d), line 124
   - `old:` 141's semantics are only enum-named
   - `new:` family 141 is modelled in `matchmaking.rs` (141/2 fixed rows and layouts); whether 141 carries a race result is still unverified
   - `why:` repo:prototype/osfr-tools/src/matchmaking.rs:14, 968, 1041 (141/2 row layout), 879 (141/1)

10. Blocker (e), line 125
    - `old:` and session ownership, (f) reward numbers.
    - `new:` and session ownership, which `kart_gateway.rs` now checks by GUID for the solo path, so (e) is closed there; (f) reward numbers.
    - `why:` repo:prototype/osfr-tools/src/kart_gateway.rs:269-314, 496

11. Row "Reward" in the test-gates table, line 134
    - `old:` no pricing data and no finish binding; the module returns `Unpriced` for any track without an explicit schedule
    - `new:` pricing is content-driven (`kart_gateway.rs` reward claim and cooldown); Build Ledger records 50 coins and 25 XP as native-verified. The module itself still returns `Unpriced` for any track without an explicit schedule.
    - `why:` repo:notes/Design/Build Ledger.md:103; prototype/osfr-tools/src/kart_racing.rs:594, 711; src/kart_gateway.rs:148 (`KartRewardClaim`)

**Unsure:**
- The "Next builder assignment" section (lines 143-151) says to extend only `kart_racing.rs` and its tests, with `lib.rs`/`gateway.rs`/`gameplay.rs` lead-owned. It was written before `kart_gateway.rs`, `kart_lobby_native.rs` and the `lib.rs:46` registration existed, so the owned-path list is probably stale too. I did not settle which paths are still lead-owned.
- The "Race finish" gate (line 133, "not definable today") may still hold for the native finish message. `kart_racing.rs` has a server-side `finish` and audit `RaceResultProposal` (kart_racing.rs:579-580), but I did not confirm whether any native results message is recovered.
- The `lab/` artifacts (proof sha256, trace log, capture index hash) and the `karts1.gfx` discrepancy are outside the roots I could read, so I did not verify them.
- The 33/sub-opcode mapping (sub 9/34/11/5/14/2/3/1/4) was not checked case by case against `gameplay.rs` / `kart_gateway.rs`; the opcode-level routing above is confirmed, the subtype table is not.
