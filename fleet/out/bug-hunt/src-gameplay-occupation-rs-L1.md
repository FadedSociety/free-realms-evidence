<!-- fleet job=bug-hunt id=src-gameplay-occupation-rs-L1 status=nothing_found turns=9 usd=0.0053 tokens(read,write,in,out)=[88362, 17844, 20, 4289] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay/occupation.rs lines 1-166 of 166

Reviewed `prototype/osfr-tools/src/gameplay/occupation.rs` lines 1-166 in full. No defect that a remote client can trigger.

What I checked:
- **Macro and enum (1-42):** `Occupation::ALL` is generated from the same list as the enum, so no variant can be missing from `blocks`.
- **`gates` (63-83):** match is exhaustive, with no wildcard. The values agree with the test at 131-165 (start/warp/ride/pets/location membership).
- **`is_occupied` (88-107):** each predicate resolves to a real state field, and the clearing paths exist:
  - Soccer: cleared by `exit_soccer` (gameplay.rs:3376) and `abandon_soccer_for_reconnect` (gameplay.rs:1537). Set at gameplay.rs:3303.
  - Fishing: `!fishing.is_empty()` is cleared on terminal state (fishing_service.rs:342), `end` (677), `reset` (468) and `disconnect` (370).
  - FieldEngaged: reset at gameplay.rs:1512.
  - Housing: `return_to` is set in `housing.rs:123` and cleared in `housing.rs:147` and `housing.rs:183`. The housing handler works on a clone and commits only on success (`housing.rs:92`, `161`), so the `?` at `housing.rs:151` does not leave a half-applied visit.
- **`blocks` / `activity_busy` (110-120):** `any` over `ALL` with a gate check and an occupation check. No indexing, unwrap or arithmetic on client data.

Nothing in this window parses packets or saves, and no client value reaches an unchecked index, allocation or unwrap here. I did not find a logic error against the doc comments or the pinned test.
