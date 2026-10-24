<!-- fleet job=test-audit id=tests-support-scavenger-hunt-rs-L1 status=nothing_found turns=9 usd=0.0077 tokens(read,write,in,out)=[136664, 26060, 20, 6156] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/support/scavenger_hunt.rs lines 1-223 of 223

Reviewed `prototype/osfr-tools/tests/support/scavenger_hunt.rs` lines 1-223 in full, and read the code under test it depends on: `npc_quest_chain.rs` (counts, pending_offer, saved, assert_packet_changes_nothing, objective_update/complete/activated, has_family), `gameplay.rs` `on_location` (1806) and `handle_in_world` (2169), and `quest_engine.rs` runtime VisitPosition goal construction (140-200). I also checked callers in `scavenger_hunt_quest.rs` and `scavenger_hunt_two_players.rs`.

No finding meets the five categories:

- **Cannot fail:** `visit` derives its expected counters and its 49/9 check from the test's own stop index, but the counters come from the live `game.on_location` path and are compared against the spec sequence [1,0,0,0] → [1,1,0,0] → ..., so a regression in counting or ordering is caught. `accept_hunt` checks the objective count (4) and ids [1,2,3,4] read from the 49/3 bytes, which is the hunt's specified content, not a restatement of the code. `npc_position` reads the NPC spawn that the range check uses, but the hunt's quest objectives come from separate quest content (`VisitPosition` radius), so a wrong quest stop still fails the counters.
- **Asserts nothing that matters:** `refused_interaction` checks `is_err()` plus full `GameplayState` and save-byte equality, which is the claimed refusal property. `refused` wraps `assert_packet_changes_nothing` and adds the same state/byte comparisons; it is redundant but not a hole.
- **Name overclaims:** the `visit` comment says the caller asserts 49/10 and the next 49/8. The callers in `scavenger_hunt_quest.rs` (lines ~196-244, 624, 714-755) and `scavenger_hunt_two_players.rs` (line 74) do assert `has_objective(..., 10, n)` and `has_objective(..., 8, n)`, so the claim holds in practice.
- **Silent skip:** no `#[ignore]`, and the only early-exit-style code is `expect` on NPC content loading, which panics rather than passing.
- **Over-pinned:** the byte offsets in `accept_hunt` (109..113, 107-byte records) are the client reader layout documented in the file, not incidental detail.
