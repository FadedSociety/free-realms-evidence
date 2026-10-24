<!-- fleet job=bug-hunt id=src-character-store-rs-L1 status=nothing_found turns=4 usd=0.0034 tokens(read,write,in,out)=[19565, 11733, 10, 3396] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/character_store.rs lines 1-221 of 221

Reviewed `prototype/osfr-tools/src/character_store.rs` lines 1-221 in full, and checked the callers that matter (`account_store.rs` around lines 439, 565-575, 674-687; `bin/osfr-gateway.rs` around lines 923, 1149 and 4089). I found no defect that meets the criteria.

What I checked:
- **Load size and parsing (61-86):** the read is capped at `MAX_FILE_BYTES + 1` and the length is checked before parsing. `serde_json` has its own recursion limit, and `deny_unknown_fields` plus the fixed-shape structs leave no unbounded collection. Schema/version gating and `validate()` run before the state is returned.
- **Validation (33-45):** rejects guid 0, non-finite components, and components above 1e6 in magnitude. JSON cannot encode NaN or infinity, so the `is_finite` check is defence in depth.
- **Save path (91-103):** validates, serializes, and applies the same 16 KiB cap as the loader, so a save the loader would reject is never written.
- **Atomic replacement (106-141):** the temp file is written and fsynced before the rename. On any error before a successful rename, `TemporaryFile::drop` removes the temp file and the destination is untouched. `committed` is set only after `replace` succeeds, so a successful rename is never followed by a delete. The `expect` at line 116 holds because `create_temporary` always returns an open file.
- **Temp naming (158-184):** `create_new` with pid plus a process-wide sequence, retried up to 32 times, so collisions cannot silently reuse a file.
- **Windows retry (121-138):** retries only the rename, only for error codes 5/32, capped at 20 attempts, and never deletes or truncates the old save.

Out of scope but noticed: `bin/osfr-gateway.rs:4089` passes a request body to `replace_bytes`. It is a studio/dev endpoint that validates the JSON and the path, and it is not a player-facing path, so I did not report it.
