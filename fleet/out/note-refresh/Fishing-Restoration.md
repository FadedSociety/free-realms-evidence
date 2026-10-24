<!-- fleet job=note-refresh id=Fishing-Restoration status=done turns=12 usd=0.0155 tokens(read,write,in,out)=[280796, 48662, 26, 13246] model=claude-haiku-5-5 -->
# notes/Research/Fishing Restoration.md

**Verdict:** badly stale. The wire codec claims (opcode 138, sub-opcode table, handle/vec4 layouts, 12 tests in `tests/fishing.rs`) still hold. The status, integration and "no server authority" claims are false: the module is registered in `lib.rs` and routed in-world, and the service already selects and pays catches.

**Corrections:**

1. `old:` module landed with focused tests; fishing is **not** playable and no native client
   `new:` module is wired into the crate and the in-world route (`lib.rs:21`, `gameplay.rs:2600`); fishing is **not** playable natively and no native client
   `why:` `repo:prototype/osfr-tools/src/lib.rs:21` (`pub mod fishing;`); `repo:prototype/osfr-tools/src/gameplay.rs:2600` and `:3500` call `.route(...)`; `repo:prototype/osfr-tools/src/fishing_service.rs:600-616` routes opcode 138 (`fishing::OPCODE`); `repo:notes/Design/Build Ledger.md:107` says "Wired, never run natively", with six guide NPCs admitting players.

2. `old:` (self-contained, path-included by
   `new:` (self-contained, library module imported by
   `why:` `repo:prototype/osfr-tools/tests/fishing.rs:1-3` imports `osfr_tools::fishing::{self, ...}`; there is no `#[path]` include. `repo:prototype/osfr-tools/src/lib.rs:21`.

3. `old:` `prototype/osfr-tools/tests/fishing.rs`; not registered in `lib.rs`). Public API:
   `new:` `prototype/osfr-tools/tests/fishing.rs`; registered in `lib.rs:21`). Public API:
   `why:` `repo:prototype/osfr-tools/src/lib.rs:21`; `repo:prototype/osfr-tools/tests/fishing.rs:1`.

4. `old:` Root integration: add `pub mod fishing;` to `lib.rs`, route opcode 138 payloads to
   `new:` Root integration (landed): `pub mod fishing;` is at `lib.rs:21`, and opcode 138 payloads reach `ClientRequest::decode` through `FishingService::route` (`fishing_service.rs:600-616`, called from `gameplay.rs:2600`) for inbound client requests, with
   `why:` `repo:prototype/osfr-tools/src/lib.rs:21`; `repo:prototype/osfr-tools/src/fishing_service.rs:611` (`fishing::ClientRequest` path via `handle`); `repo:prototype/osfr-tools/src/gameplay.rs:2600`. The following clause ("after the SOE codec strips framing, and use `ServerPacket::decode_known` only for outbound evidence") still reads as the rule in use.

5. `old:` No timing, no tension thresholds, no catch tables, and no server authority for a
   `new:` No tension thresholds or recovered catch tables, and no recovered native authority for a
   `why:` `repo:prototype/osfr-tools/src/fishing_service.rs:636-637` (bite timers and leash in `supervise`), `:1250` (`select_species`), and `:14-20` (server-owned catch selection and payout from `fishing_spots.json`).

6. `old:` catch are implemented. Nothing here should be described as original balance.
   `new:` catch are implemented as reconstructed service policy in `fishing_service.rs` (bite timers, species selection, server-owned payouts). None of it is recovered from the client. Nothing here should be described as original balance.
   `why:` same as item 5; `repo:prototype/osfr-tools/src/fishing_service.rs:14-15` says "Only this service selects and awards a catch."

7. `old:` 1. Server authority: nothing decides which fish bites.
   `new:` 1. Server authority is reconstructed, not recovered: `fishing_service.rs` picks the fish and pays the catch, but the body layouts for `FishingPacketUpdateData`, `FishInfoUpdate`, `SpawnFishRun` and `SpawnProxiedFishingSchool` still must be recovered before a real catch can be validated.
   `why:` `repo:prototype/osfr-tools/src/fishing_service.rs:14-15`, `:1250`; `repo:prototype/osfr-tools/src/fishing.rs:488-491` (`Opaque` fallback for sub 3/4/11/16/18).

8. `old:` 4. No native client run; fishing cannot yet be exercised from the server side.
   `new:` 4. No native client run. The server side is exercised by `tests/fishing_entry.rs` and `tests/fishing_service.rs`, but nothing has been run in the client.
   `why:` `repo:notes/Design/Build Ledger.md:107`; `repo:notes/Autopilot/F120.md:42` ("`fishing_entry` 27 passed 1 ignored"); `repo:notes/Autopilot/F112.md:63` ("`fishing_service`: 7 passed"); `repo:prototype/osfr-tools/tests/fishing_entry.rs` and `tests/fishing_service.rs` exist.

9. `old:` Sub 3, 4,
   `new:` Sub 3, 4 (decoder leaves them opaque; the service writes them from reconstructed widths),
   `why:` `repo:prototype/osfr-tools/src/fishing_service.rs:1065` (`Sub::RegisterPlayerResponse`), `:1104` (`Sub::FishInfoUpdate`), `:1158` (`Sub::SpawnSchool`); `repo:prototype/osfr-tools/src/fishing.rs:488-491` (no decode arm for those subs, so they stay `Opaque`). Sub 11 is the school spawn written at `:1158`.

**Unsure:**

- "The server has no fishing serializer" (line ~58). This may refer only to the preserved original server. Our server now has fishing writers (`fishing_service.rs:1065-1215`), so the sentence is misleading if it describes our tree. I did not change it.
- Verification section (lines ~134-146) gives "7 tests" and "12 tests". `tests/fishing.rs` has 12 `#[test]` functions today, so the 12 count still matches; the 7 is a dated RED/GREEN record and was left alone.
- Lines 54-67 and the `lab/` paths cite files outside the repo. I could not check them.
- Tension/distance meter math and the Flash widget gap (open gap 3): I did not search the repo for any tension rule, so I could not confirm whether any tension threshold is implemented.
