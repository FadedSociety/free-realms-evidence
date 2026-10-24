<!-- fleet job=note-refresh id=Soccer-Match-Authority status=done turns=19 usd=0.0190 tokens(read,write,in,out)=[550231, 50261, 40, 14348] model=claude-haiku-5-5 -->
# notes/Research/Soccer Match Authority.md

**Verdict:** moderate drift. The authority core (apply guard order, HalfPolicy, restore/snapshot, goal and half logic, `advance` bound) matches the tip. The status claims about `lib.rs` registration, the captured kick/pass channel and the sub-13 gap are now false.

**Corrections:**

1. `old:` (both new; the module is **not**
registered in `lib.rs` - lead-owned integration)
   `new:` (both new; the module is registered in `lib.rs` line 83 as `pub mod soccer_match;`, lead-owned integration)
   `why:` repo:prototype/osfr-tools/src/lib.rs:83 (`pub mod soccer_match;`).

2. `old:` ball spawn `(226.7, 2.0, 212.905)` offered as `CAPTURED_BALL_SPAWN`
   `new:` ball spawn `(226.7, 2.0, 212.905)` is preserved as captured evidence; no `CAPTURED_BALL_SPAWN` constant exists in `src/soccer_match.rs`, and `MatchConfig::new` defaults `kickoff_spawn` to the origin
   `why:` repo:prototype/osfr-tools/src/soccer_match.rs:141,155 (grep for `CAPTURED_BALL_SPAWN`, `226.7`, `212.9` across `prototype/osfr-tools` finds nothing in src or tests).

3. `old:` client kick/pass request packet (`ImpulseBall` 13 never captured)
   `new:` client-authored sub-13 `ImpulseBall` (layout recovered; no client sender observed, so it stays refused by policy)
   `why:` repo:prototype/osfr-tools/src/soccer_match.rs:340-342 (sub 13 refused as server-authored); tests/soccer_match.rs:212-214 ("layout is recovered, but no authenticated client-to-server send was observed"). The kick/pass channel itself is captured: sub-14 state codes are classified at soccer_match.rs:273-277.

4. `old:` (ids 3/14) -> `ClientPacket::ReadOnly` with the decoded packet.
   `new:` (id 3) and non-kick/pass id-14 states -> `ClientPacket::ReadOnly` with the decoded packet; id-14 kick/pass states (codes 16-34) -> `ClientPacket::State(StateRequest)`.
   `why:` repo:prototype/osfr-tools/src/soccer_match.rs:286-290 (`ClientPacket::State` variant), :319-338 (UpdatePlayerState -> `classify_state` -> State, else ReadOnly), :339 (RegisterPlayer -> ReadOnly), :273-277 (classify_state).

5. `old:` missing-mapping message.
   `new:` server-authored message: no client author path was located. (`client_intent` now also refuses `State` with "needs configured charge policy and a server-verified pass target".)
   `why:` repo:prototype/osfr-tools/src/soccer_match.rs:340-342 and :355-357.

6. `old:` - Kick and pass have no captured wire layout (sub 13 missing), so a native client cannot yet drive them; the mapping stays an explicit gap.
   `new:` - Kick and pass: the sub-14 state codes (16-34) are captured and mapped to `ClientPacket::State`, but sub 13 has no client sender, so a native client cannot yet supply a ball impulse; the sub-13 mapping stays an explicit gap.
   `why:` repo:prototype/osfr-tools/src/soccer_match.rs:273-277, :286-288, :340-342; tests/soccer_match.rs:212-214.

7. `old:` `captured_registration_and_player_state_are_read_only_decodes`
   `new:` `registration_and_player_state_are_read_only_decodes`
   `why:` repo:prototype/osfr-tools/tests/soccer_match.rs:245 (no test with the cited name exists).

**Unsure:**

- Artifact sha256 for `src/soccer_match.rs` (`a1406892…`): I cannot hash the file. Other notes give different tip hashes: `Reviews/Soccer Native Wire Repair Review.md` cites `4d6006ce…` and `Research/Soccer Service Integration.md:20` cites `eb73cc17…` after the `Authority::unregister` addition. Hashes were not verified; the `unregister` addition (soccer_match.rs:549) confirms the file has changed since the note was written.
- Test count "27 passed": I could not get a reliable count of `#[test]` functions in `tests/soccer_match.rs` from the search tool (results were inconsistent), so the 27 figure is neither confirmed nor refuted. The cited test names for F1-F4, F6 and N1-N3 all exist.
- `Research/Soccer Service Integration.md:54` also says `soccer_match::CAPTURED_BALL_SPAWN` exists. That note is outside this check, but it has the same unsupported claim as correction 2.
- Gateway integration: the Build Ledger reads "Built (registered, not routed)" for soccer, and `soccer_service.rs` now uses `soccer_match`. I did not check whether gateway routing has changed, so the "integration ... not part of this work" line (scope of this note) is left as is.
