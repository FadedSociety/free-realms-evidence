<!-- fleet job=bug-hunt id=src-restoration-piece-019-rs-L1 status=done turns=4 usd=0.0070 tokens(read,write,in,out)=[27706, 19347, 10, 8612] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_019.rs lines 1-460 of 460

Window: `prototype/osfr-tools/src/restoration/piece_019.rs` lines 1-460. Scope note: the module is not registered in `src/lib.rs`, and the only includer is `tests/piece_019.rs` (`#[path]`, line 13-14). Nothing in `src/` calls `begin_session`, `commit`, `page_payload`, `save` or `load` outside that test, so both findings below are latent. They are not reachable from a client packet today.

Checked and clean: `commit` (212-260) validates the value before touching state, and every error return happens before any mutation. The `committed` flag and the board insert are in the same function with no fallible step between them. `rows` ranking and tie ranks (262-293) are correct. `page_payload` (297-310) bounds `count` to 1..=10, and `skip`/`take` cannot panic on any offset. `validate_board` and `validate_field` length and control-character checks are correct. `load` re-validates every field and value (341-376). `encode_rows` adds no row-level injection beyond the case below.

**[medium] piece_019.rs:409-423 - `validate_field` lets a trailing `:` through, and the `::` property separator then splits the field wrongly on the wire.**
- Failure scenario: `begin_session(BOARD, "P0001", "Ayla:", Points)` passes validation, because `"Ayla:"` contains no `::`. `encode_rows` (lines 383-384) writes `Name^Ayla:` followed by the separator `::` and `Guid^P0001`, which gives `Name^Ayla:::Guid^P0001`. A left-to-right split on `::` (the client rule replicated in `tests/piece_019.rs:81-96`) yields `Name^Ayla` and `:Guid^P0001`. The row then loses its `Guid` property, and the parser's `split_once` fails on the malformed prop. The same happens for a guid ending in `:`, which breaks the `Guid`/`Value` pair.
- Reach: `begin_session` (174-198) takes `name` and `guid` straight from the caller; `encode_rows` (379-397) concatenates them with `PROP_DELIMITER`. No upstream check rejects a trailing colon, because the `FIELD_DELIMITERS` check (416-421) is a plain substring test and does not look at the joined form.
- Fix: in `validate_field`, add `|| field.ends_with(':')` to the rejection at line 416 (or reject any field whose trailing character is `:`). The `load` path at 359-361 then rejects such entries as well.

**[low] piece_019.rs:184-197 - the `sessions` map only grows, with no cap and no removal.**
- Failure scenario: each `begin_session` inserts one `Session` into `self.sessions` (186-196). Nothing ever removes a session, committed or not (`commit` at 255-258 only sets a flag). If a future caller opens a session for every client request, memory grows without bound for the life of the process. Sessions are also not persisted, so they cannot be reclaimed on save or load either.
- Reach: this is latent. No production caller exists yet. The `#[path]` test is the only user.
- Fix: evict committed or unfinished sessions once they are committed, or cap `sessions.len()` and return an error when the cap is reached.

No other defects in this window meet the bar.
