<!-- fleet job=bug-hunt id=src-restoration-piece-031-rs-L1 status=done turns=7 usd=0.0061 tokens(read,write,in,out)=[70153, 21486, 16, 5513] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_031.rs lines 1-476 of 476

The window (piece_031.rs 1-476) is almost entirely constant tables plus small lookups. There is no panic, unbounded growth, save-atomicity or client-authority path: `job(id)`, `payload_for` and `unlocked_name` are linear searches over fixed arrays with no indexing that can fail. Nothing in `src/` calls `validate()`, `validate_locale()`, `payload_for()` or `job_unlock()` outside this file and its tests, so the findings below are documentation/validation mismatches only, not reachable from a client packet.

- **[low] prototype/osfr-tools/src/restoration/piece_031.rs:374-395 - `validate()` doc says every row keeps a unique name id, but the function never checks `name_string_id` for duplicates (only `id` and `name`).**
  - Failure scenario: a future edit gives two JOBS rows the same `name_string_id`. `validate()` returns `Ok(())`, so the catalogue reports itself valid while its doc comment says it is not. Today's data has no duplicates; only the test at tests/piece_031.rs:84-96 enforces it.
  - Reach: no runtime caller in `src/`. Only tests and the checker invoke it, so this is not client-reachable.
  - Fix: track `name_string_ids` alongside `ids`/`names` and return `DuplicateNameStringId` (or reuse `DuplicateName`-style error) when `row.name_string_id` already appears in `[..index]`.

- **[low] prototype/osfr-tools/src/restoration/piece_031.rs:120-121 and 399-419 - The JOBS doc says "Name ids and description ids are validated against the preserved original locale", but `validate_locale` only checks `name_string_id`; no code checks `description_string_id`.**
  - Failure scenario: the description ids are wrong and nothing notices. Two rows share a description id: Soccer Star (id 52, line 281) and Demo Derby Driver (id 49, line 270) both use 2920. The locale maps 2920 to "Demolition Derby Driver Driver Description", so Soccer Star's description points at Demo Derby's text. Enforcer (id 20, line 292) and Referee (id 58, line 292) also share 2302. The same values appear in Sanctuary's Profiles.json (Soccer Star DescriptionId 2920), so this is inherited from the community source, not a typo in this file.
  - Reach: the constants are only consumed by tests and the checker; no client packet path reads `description_string_id`.
  - Fix: either extend `validate_locale` to check description ids against the locale (the Soccer Star 2920 mismatch would then surface and needs a corrected id from a source), or correct the doc comment to say only name ids are validated.
