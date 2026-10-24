<!-- fleet job=note-refresh id=Kart-Entry-Encounter-Binding status=done turns=16 usd=0.0148 tokens(read,write,in,out)=[354679, 42394, 34, 11837] model=claude-haiku-5-5 -->
# notes/Research/Kart Entry Encounter Binding.md

**Verdict:** badly stale in the gateway paragraph of "Answer first" (the code now does what the note says it should do). The packet-level, offset and codec claims still hold.

**Corrections:**

1. `old:`
```
* Current `src/gateway.rs` replays the captured **world** Ready block
  (templates 8..46, first opcode 67) on op13 when `ready == false`
  (`gateway.rs:587-599`), requires op10 for `Event::Loaded`
  (`gateway.rs:600-616`), and skips application packets while `!loaded`
  (`gateway.rs:665`); a scene zoning reply resets both flags
  (`gateway.rs:697-706`, `746-755`).
```
`new:`
```
* Current `src/gateway.rs` answers op13 in the `Event::Ready` arm (`gateway.rs:1455-1476`): when a kart entry is active it sends `Gameplay::kart_ready_stream` first (details, 41/2 enter, 41/114 ready, PlayerUpdate/20, then 38/26 and 14), and only otherwise replays the captured **world** Ready block (`startup_for(Kind::Ready)`, templates 8..46). `Event::Loaded` still requires op10 (`gateway.rs:614-615` parse, `gateway.rs:1477-1480` state). Application packets are skipped while `!loaded` unless `accepts_kart_loading_application` admits them (`gateway.rs:1640`). Scene zoning replies reset both flags (`gateway.rs:1881-1882`; zone change `gateway.rs:1863-1864`; instance transfer `gateway.rs:985-986`).
```
`why:` `repo:prototype/osfr-tools/src/gateway.rs:1455-1498` (Ready/Loaded arms), `:614-615` (parse), `:1640` (`!loaded` gate), `:1863-1864`, `:1881-1882`, `:985-986` (resets). Lines 587-599, 600-616, 665, 697-706 and 746-755 are now parse and helper code (`parse_message`, `application_messages`, `ordered_messages`, `stage_instance_transfer`), not these behaviours. `repo:prototype/osfr-tools/src/gameplay.rs:1845-1863` (`kart_ready_stream`, `accepts_kart_loading_application`). `repo:prototype/osfr-tools/src/kart_gateway.rs:580-602` (`initialize` builds the 41/114 + 41/2 + 41/114 + PlayerUpdate/20 stream).

2. `old:`
```
For a kart scene that baseline world
  block is the wrong reply to op13 — use the kart-appropriate stream
  (below) instead, and do not gate the kart entry on op10.
```
`new:`
```
For a kart scene the code already answers op13 with the kart stream (`gameplay.rs:1845-1858`), and the kart entry is not gated on op10: `kart_ready_stream` says the client "registers the kart between Ready13 and Loaded10. Sending entry after Loaded creates a circular wait."
```
`why:` `repo:prototype/osfr-tools/src/gameplay.rs:1843-1858` (the comment and the function), `repo:prototype/osfr-tools/src/gateway.rs:1459-1476`.

**Checked and still current (no change):**
- `PacketCodes.cs:8` = 10 FinishedLoading and `:10` = 13 IsReady: `repo`/`refs:OpenSourceFreeRealms/ofrserver/Server/LibSOE/Core/PacketCodes.cs:8,10`.
- `src/kart_lobby_native.rs` is registered: `repo:prototype/osfr-tools/src/lib.rs:43`.
- 41/2 enter is 17 body bytes (encounter, instance, 9 zero bytes), with the session filled in on the later send: `kart_gateway.rs:587-590` and `:606`.
- Session at inner bytes 32..40 (body offset 28) and instance at 8..12 (body offset 4) in `details()`: `repo:prototype/osfr-tools/src/kart_gateway.rs:539-540`.
- 141/1 is the two-word session key only: `repo:prototype/osfr-tools/src/matchmaking.rs:879`.

**Unsure:**
- "first opcode 67" for the world Ready templates: I did not check the reference template bytes.
- The 141/1 role. The note calls it the "lobby selection request". `matchmaking.rs:879` calls it the "client queue catalogue request". This is a naming question, not a byte-layout one, so I left the note's wording alone.
- The `lab/reports/kart-encounter-binding-20261009/` artifacts (probe, proof.json, run.log, pcap-derived bins) and the capture timings (frames 15232, 15449, 21375). They are not in the repo view I can read, so I could not check them.
- The 41/114 field meanings and the `op31 id = 0` claim: only the `details()` byte offsets were checked.
