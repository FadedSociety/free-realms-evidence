<!-- fleet job=note-refresh id=Native-Zone-Transition-Codec status=done turns=8 usd=0.0078 tokens(read,write,in,out)=[104945, 25701, 18, 7023] model=claude-haiku-5-5 -->
# notes/Research/Native Zone Transition Codec.md

**Verdict:** badly stale on integration status. The codec, tests, field layout, envelope, bounds, and test counts all match the tip. The note's claim that the module is unregistered and unwired is no longer true.

**Corrections:**

1. `old:` the module is unregistered and the test includes it by path.
   `new:` the module is registered as `pub mod zone_transition;` and the test imports the library module (`use osfr_tools::zone_transition::{...}`).
   `why:` `repo:prototype/osfr-tools/src/lib.rs:102` (`pub mod zone_transition;`); `repo:prototype/osfr-tools/tests/zone_transition.rs:3` ("tests the registered production module") and `:7-9`. The test file has no `#[path]` include.

2. `old:` No runtime world entry, gateway wiring or scene loading; the module stays
     unregistered until the lead integrates it.
   `new:` The codec is wired into production paths: the gateway decodes the opcode-31 frame at zone change and encodes the zone-change reply, kart entry and the kart gateway encode the scene before sending, and the world and soccer paths call `encode` too. Remaining limits are the unrecovered `unknown` byte and the gameplay meaning of `id`, update radius and geometry id.
   `why:` `repo:prototype/osfr-tools/src/gateway.rs:976-977` (`crate::zone_transition::decode(&packet)?`), `repo:prototype/osfr-tools/src/gateway.rs:1789` and `:1886` (`crate::zone_transition::encode(&scene)?`), `repo:prototype/osfr-tools/src/kart_gateway.rs:261` (`zone_transition::encode(&content.context.scene)?`), `repo:prototype/osfr-tools/src/kart_entry.rs:593`, `repo:prototype/osfr-tools/src/world.rs:1493`, `repo:prototype/osfr-tools/src/soccer_service.rs:1032`. The original "stays unregistered" wording is contradicted by `lib.rs:102`.

3. `old:` No native claim: no world entry exists yet.
   `new:` No native claim is made here; the codec is already called by the gateway zone-change and kart entry paths (see Rust artifact).
   `why:` `repo:prototype/osfr-tools/src/gateway.rs:1789`, `repo:prototype/osfr-tools/src/kart_gateway.rs:261`. The Build Ledger also lists zone transfers as "Wired" (`repo:notes/Design/Build Ledger.md:56`). This is a softer correction: "no world entry" may still be literally true for the native world-entry path, so treat it as a wording fix.

**Checked and holding:**
- Module path `src/zone_transition.rs` exists; `OPCODE = 31`, `OUTER_FAMILY = 5`, `MAX_STRING_BYTES = 4096`, 9-byte minimum (`HEADER_BYTES + 2`), `!= 0` booleans, envelope flag preserved, trailing bytes refused, opcode-43 frames refused by the opcode check (`repo:prototype/osfr-tools/src/zone_transition.rs:25-33, 96-129, 190-264`).
- `Default` is derived with zeros and empty strings (`zone_transition.rs:39`).
- The test file has 10 `#[test]` functions, one `#[ignore]`d and env-gated on `OSFR_ZONE_OP31_CAPTURE` (`tests/zone_transition.rs:44-235`). That gives the note's "9 passed, 1 ignored".
- The 87-byte capture offset table sums correctly (80-byte inner + 7-byte envelope).
- The client reader `FUN_008e4ae0` exists in the decompiled client DB.

**Unsure:**
- The client line numbers (`pseudocode.c:1029104`, `:1108664`) and the per-field offsets (`+0x04` … `+0x81`) are in the lab, which I could not read. I did not verify them.
- The lab capture file, its sha256, and the `green*.log` and `oracle-comparison.json` evidence are outside the repo, so I did not check them.
- The "9 passed" count matches the test attributes, but I did not run the tests.</result>
