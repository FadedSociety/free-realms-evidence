<!-- fleet job=test-audit id=tests-shared-field-interest-rs-L1201 status=nothing_found turns=13 usd=0.0055 tokens(read,write,in,out)=[124581, 16295, 28, 4335] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/shared_field_interest.rs lines 1201-1213 of 1213

No findings in `prototype/osfr-tools/tests/shared_field_interest.rs` lines 1201-1213 (`f160_hidden_view_forgets_every_known_actor_in_the_shared_field_layout`).

What I checked:
- `E` is defined in `tests/shared_field_state.rs:1` (`131000108001`), pulled in by `include!` at line 3, so the fixture exists.
- The expected bytes are built by hand in the test (`[35,0,3,0]`, u16 submode 1, GUID LE, 17 zero bytes). They are not derived from the code under test. They match the production encoder: `encounter.rs:2907` `header(op, sub)` gives `[35,0,3,0]`, and `encounter.rs:3080` `remove()` writes `header(35,3)`, `1_u16`, the GUID, and `[0;17]`. The layout also agrees with the gateway comment that 35/3 carries a u16 submode before the GUID.
- `world.rs:232` `NpcVisibility::hidden_view` returns an empty wanted set and one `SharedFieldState::removal` per known GUID. It iterates a `BTreeSet`, so the expected order `[E, E+1]` is deterministic. The assertion would fail if the packet count, order, submode, or payload changed.
- The second half (empty known set gives empty wanted and empty packets) would catch a stray packet from `hidden_view`. It is thin, but it is a real check and not a tautology.
- No `#[ignore]`, no early return, and the name matches what the body checks (the removal packets for each known actor, plus the empty wanted set).

I found no cannot-fail, vacuous, overclaiming, skipped, or over-pinned problem in this window.
