<!-- fleet job=bug-hunt id=src-restoration-piece-092-rs-L1 status=nothing_found turns=9 usd=0.0123 tokens(read,write,in,out)=[184787, 39273, 20, 10987] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_092.rs lines 1-602 of 602

## Window: `prototype/osfr-tools/src/restoration/piece_092.rs` lines 1-602

No defect in this window meets the bar (a concrete failure that a client packet or save can reach). I read the whole window, plus `tests/piece_092.rs` (60-375) and the callers.

**Checked and cleared:**
- `decode_client_request` (366-408): every payload length is checked before indexing. The sub-opcode 8 path requires exactly 5 bytes before `payload[0..4]` and `payload[4]` are read. `read_i32` (426-439) rejects both short and long payloads. The `payload.to_vec()` in the `Unrecovered` arm copies only the frame's own bytes.
- `MountSpawn` (371-373) rejects `mount_number <= 0`, and `captured_mount` (299-300) bounds the rest. A client-chosen mount number cannot reach an unowned row.
- `MountSession::spawn` (495-508) only mutates `mounted` after the row lookup succeeds, so there is no mutate-then-error atomicity gap.
- `DismountRequest` with no mount returns `IgnoredNotMounted` and changes nothing.
- `item_bound_mount` (307-312) uses `next_back()`, which matches its doc comment and the test at `tests/piece_092.rs:198-208`. The 11038 tie-break is the only duplicate item id in `CAPTURED_MOUNTS`.
- `validate` (315-337): `seen[..index]` is in range for every index.
- `mount_stats` (512-542) branch order matches the doc comment and the counts asserted in the tests (9, 8, 1, 1).
- `encode_stat_update` (554-569) and the `u16 opcode + u16 subtype` header match the `mystery_chest.rs` note for root 38. `stats.len() as i32` is only ever fed internal constant slices.
- `encode_mount_response` and `encode_dismount_response` match their test byte layouts.

**Why nothing is reportable:**
- The module is not wired into the live server. `src/restoration/mod.rs` does not register `piece_092`, and the only consumer is `tests/piece_092.rs`. Nothing in `src/` calls `decode_client_request` or `MountSession::apply`. No client packet can reach these functions.
- The live mount path is `src/mounts.rs`, which gates spawns with `is_owned(...)` against the player's inventory (`mounts.rs:370`, `:481`, `:843`). That is a separate code path, outside this window.

**Limitation noted, not a defect:** `captured_mount` and `item_bound_mount` resolve against a static table of one captured character, not a per-player ownership record. A future integration that wires `MountSession` to real sessions would need a per-character check. The module doc already labels this as the captured-rows contract. It should be addressed at integration time, not reported as a bug in this window.
