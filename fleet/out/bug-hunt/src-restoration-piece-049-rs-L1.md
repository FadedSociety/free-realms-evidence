<!-- fleet job=bug-hunt id=src-restoration-piece-049-rs-L1 status=nothing_found turns=4 usd=0.0058 tokens(read,write,in,out)=[33693, 20528, 10, 5849] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_049.rs lines 1-571 of 571

Reviewed `prototype/osfr-tools/src/restoration/piece_049.rs` lines 1-571 in full, plus the callers and the test file `tests/piece_049.rs`. No defect that meets the criteria.

What I checked:
- **Panics on client input (criterion 1):** There are no client-reachable indexing or unwrap paths. The only indexing is `CHARACTER_TYPES[slot]` (line 516) and `CHARACTER_TYPES[..index]` / `CREATOR_CATEGORIES[..index]` (lines 485, 501), all over fixed-size `const` arrays with `slot` in 0..4. The lookups (`character_type`, `category`, `excluded_rows_for`, `skin_tone_exclusion`, `head_exclusion`) are pure `iter().find`/`contains` with no panic path. The arithmetic at lines 547-559 is `usize` sums of `u8` constants.
- **Unbounded resources (criterion 2):** None. Every collection is a fixed `const` table; `excluded_rows_for` returns at most 12 entries.
- **Atomicity (criterion 3):** `validate()` is read-only and has no mutation before a `?`/return.
- **Trusting the client (criterion 4):** The module has no production caller. `src/lib.rs` does not register it (per `notes/Reviews/Delegated Task Readiness.v1.json`), and the only references outside the file are the test and the Python checker. Nothing in the server parses a packet or save into these lookups, so the "authority" concern does not reach a client-controlled value.
- **Logic errors (criterion 5):** I cross-checked the counts against the doc comments and the test assertions. Results:
  - Category `rows_per_type` sums to 253. Per type: Pixie Female 67, Human Female 61, Human Male 63, Pixie Male 62. These match the doc.
  - `excluded_per_type` sums to 12 (SkinTone 2×4 = 8, FaceType 1×4 = 4). Per type it matches the `EXCLUDED_CREATOR_ROWS` entries.
  - Mapping rows: 223 + (16+30+1+1+1) = 272, as `validate()` checks.
  - Mapping types {8,0,1,2,3,6,4,7,5} are unique.
  - `FaceHair` [0,0,7,0] sits at index 2 (Human Male) and `WingsPixie` [6,0,0,6] at indexes 0 and 3 (Pixie), both consistent with their scopes.
  - Character-type and name ids match the doc comments.

One observation I did not report because it is intended behaviour, not a defect: `skin_tone_exclusion` and `head_exclusion` are blocklist lookups, so ids outside the recovered sets (for example 0 or 9+) return `None`, and the doc comment "Whether ... is supported" reads more broadly than the code. The test `wire_level_lookups_reject_only_the_recovered_unsupported_ids` (tests/piece_049.rs:164) asserts exactly this blocklist behaviour. The integration step that would turn these lookups into an allowlist sits with the lead, per the module's own BOUNDARIES note. If that integration is wired up later, the allowlist (`SUPPORTED_SKIN_TONE_IDS`, `SUPPORTED_HEAD_IDS`) should be used rather than the blocklist. This is a design note for the integrator, not a defect in this window.
