<!-- fleet job=test-audit id=tests-ability-lookup-rs-L1 status=done turns=4 usd=0.0042 tokens(read,write,in,out)=[15406, 9124, 10, 5772] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/ability_lookup.rs lines 1-219 of 219

Reviewed `prototype/osfr-tools/tests/ability_lookup.rs` lines 1-219 against `src/abilities.rs` (`definition_reply` 799, `parse_definition_request` 785, `unsupported_cast` 821, `unsupported_cast_failure` 778). The refusal and malformed-shape tests are sound: I checked the 24/32-byte length rule against each `cast()` fixture, and every malformed case in `malformed_cast_shapes_error_instead_of_guessing` hits a real `Err` path. No `#[ignore]`, no early returns. The findings below are the weak spots in this window.

- **[low] tests/ability_lookup.rs:104 definitions_above_the_player_level_or_of_another_job_are_not_served - `assert_eq!(definition_reply(&none, 4895), None)` runs on an empty list, so it passes for any implementation that searches `loaded`.**
  - Why it cannot catch a regression: `definition_reply` on `&[]` returns `None` by construction. The only way this line fails is an implementation that fabricates a reply without reading its input, and line 98 already catches that.
  - Fix: delete the line, or make it meaningful by passing a non-empty list of definitions from a non-combat profile that is known to contain id 4895 and asserting `None`.

- **[low] tests/ability_lookup.rs:124-130 missing_ids_are_bounded_and_answer_nothing - the comment "at most one 160-byte 36/13 can come back" is not what the loop checks.**
  - Why it cannot catch a regression: the assertions sit inside `if let Some(reply)`, so a `definition_reply` that returns `None` for every id in -50..70000 passes the loop. The "at most one" part is enforced by the `Option` return type, not by anything the loop asserts. Only the length and id-echo checks run, and only on hits.
  - Fix: count the hits and assert the count equals the number of loaded 160-byte entries whose id lies in the scanned range (for example `assert_eq!(hits, loaded.iter().filter(|d| (-50..70_000).contains(&id_of(d))).count())`), and assert that each loaded id is found.

- **[low] tests/ability_lookup.rs:205 classifier_never_panics_on_arbitrary_short_input - the name says "arbitrary short input", but the body only sweeps prefixes of `cast()`-shaped requests with one fixed `0xff` tail.**
  - Why it cannot catch a regression: inputs with a different header (for example `[36,0,12,0,...]`, `[26,0,10,0,...]`), a non-36 family, or a tail longer than 16 bytes are never generated. The `let _ =` discards the result, so the only signal is a panic.
  - Fix: rename it to match the prefix-sweep scope (for example `classifier_never_panics_on_every_prefix_of_cast_shapes`), or add a deterministic byte-pattern generator covering the other header families and tail lengths 0..=40, and assert that every result is either `Ok(None)` for non-36/10 headers or `Ok` / `Err` consistent with the 24/32 length rule.
