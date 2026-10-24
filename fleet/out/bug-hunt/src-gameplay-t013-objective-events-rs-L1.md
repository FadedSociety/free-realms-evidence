<!-- fleet job=bug-hunt id=src-gameplay-t013-objective-events-rs-L1 status=nothing_found turns=6 usd=0.0039 tokens(read,write,in,out)=[65409, 19530, 14, 1599] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay/t013_objective_events.rs lines 1-800 of 2102

No defects in `prototype/osfr-tools/src/gameplay/t013_objective_events.rs` lines 1-800.

Why nothing qualifies: the whole module is test-only. `src/gameplay.rs:5465-5466` declares it as `#[cfg(test)] mod t013_objective_events;`, so everything in the window is compiled only under `cargo test`. Its own notes (`notes/Autopilot/D005.md`, `T013.md`) describe it as a "test-only" module. The rules exclude `#[cfg(test)]` code.

What the window contains, all of it test scaffolding:
- Synthetic quest, mining/harvesting and kart fixtures built in temp directories (lines 25-300, 423-579).
- Packet builders for fishing, kart, gather and cooking requests (lines 306-336, 585-701). These are fixtures, not the production parser, and the production decoders are outside this window.
- Test helpers `count`, `select`, `station`, `reach_engine` (lines 615-779).
- Test `collect_reward_grant_advances_the_active_collect_objective` (lines 781-796). Its `unwrap`/`assert` calls are expected in tests.

Nothing in the window is reachable from a client packet or save at runtime. Production code that imports the `pub(super)` builders (`reward_adoption.rs:4`) is a separate file and outside this window.
