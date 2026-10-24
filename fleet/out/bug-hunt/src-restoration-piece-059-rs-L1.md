<!-- fleet job=bug-hunt id=src-restoration-piece-059-rs-L1 status=done turns=4 usd=0.0059 tokens(read,write,in,out)=[31806, 24240, 10, 5109] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_059.rs lines 1-493 of 493

Reviewed `prototype/osfr-tools/src/restoration/piece_059.rs` lines 1-493 in full. No high or medium defect is reachable from client packets or saves. The module is a compile-time roster table plus a validator, and nothing outside its own file and its `tests/piece_059.rs` (which includes it via `#[path]`) references it. The only `ZONE_STUB_LIMIT` consumer is a notes file.

Checked and clean:
- `validate` (l.391-488): `row.difficulty as usize - 1` runs only after the 1..=5 range check. `index as u32 + 1` is bounded by the 43-row table. The objective-locale cursor (l.396, 451-458) is consistent with the 37 block rows 30439-30475.
- `DIFFICULTY_MEMBERSHIP` [8,8,9,9,9] matches the row difficulties.
- Zone count (14), stub (Den of Secrets), and removed/objective rules match the doc comments.
- `by_id`, `by_name`, `with_difficulty`, `entry_rule` (l.212-285) take no unbounded input and do no indexing that can panic.

**[low] prototype/osfr-tools/src/restoration/piece_059.rs:429-431 - a zone whose `zone_bytes` is at or below `ZONE_STUB_LIMIT` is rejected with `CatalogError::ZoneStemShape`, whose documented meaning is "a plain slash-free token".**
- Failure scenario: someone hand-edits a real zone row to `zone_bytes = 84`. `validate` returns `ZoneStemShape("sg_...")`, and the Display text reads "zone stem ... is not a plain token". The stem is valid, so the message misleads the editor about the cause.
- Reach: `validate_recovered()` (l.491) on the static `DUNGEONS` table only. It is not reachable from client input. Impact is a misleading validation message in a test-time check.
- Fix: add a `CatalogError::ZoneBelowStubLimit { stem: &'static str, zone_bytes: u32 }` variant with a matching Display arm and return it at l.430.
