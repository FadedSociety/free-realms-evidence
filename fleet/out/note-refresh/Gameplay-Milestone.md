<!-- fleet job=note-refresh id=Gameplay-Milestone status=done turns=18 usd=0.0223 tokens(read,write,in,out)=[696138, 76690, 38, 11534] model=claude-haiku-5-5 -->
# notes/Research/Gameplay Milestone.md

**Verdict:** minor drift. One stated bound is false at the tip. The rest of the claims I could check in code still hold. Most of the note's evidence (client runs, lab content values such as 100 HP, 25 coins, 90 s limit, 6-unit radius, definition IDs) lives in the private lab, which is not in the repo, so I could only check the code paths and rules around it.

**Corrections:**

1. `old:` The harness allows 10–900 seconds, copies the client, serves the asset manifest locally and records traffic.
   `new:` The harness allows 10–3600 seconds, copies the client, serves the asset manifest locally and records traffic.
   `why:` repo:scripts/run-local-baseline.py:57-58 (`if not 10 <= run_options.seconds <= 3600: parser.error("--seconds must be between 10 and 3600")`). The 10–900 figure in the note (and in prototype/osfr-tools/README.md:51 and notes/Research/Recovery Commands.md) is no longer the code's bound. The `input_automation: False` statement still matches scripts/run-local-baseline.py:255.

**Checked and still holding (no change):**
- Respawn via `realm respawn`, attack feedback as chat text, 4-hit kill from 100 HP / 25 damage: repo:prototype/osfr-tools/src/combat.rs:231-271, 273-293 (attack/respawn use content values; feedback is chat text).
- Equip request 42/3 is routed: repo:prototype/osfr-tools/src/gameplay.rs:1329 (`inner.starts_with(&[42, 0, 3, 0]) && inner.len() == 16`).
- Quest 900001 accept command, `realm race start`, `realm race cancel`, `realm status`, `realm quest`: repo:prototype/osfr-tools/src/quests.rs:366, 390-408; repo:prototype/osfr-tools/src/gameplay.rs:5313.
- Reward once: quest reward flag is set only on acknowledgement after a successful bundle, and completed quests are skipped: repo:prototype/osfr-tools/src/quests.rs:344-356, 463-504.
- Checkpoint order, elapsed time and travel plausibility checks; timed-out attempt grants nothing; best time and completion count persist: repo:prototype/osfr-tools/src/quests.rs:537-600.
- Reconnect clears unfinished activity clock but keeps records: repo:prototype/osfr-tools/src/quests.rs:358-363.
- Activity start requires being within the radius of the start point; cooldown enforced: repo:prototype/osfr-tools/src/quests.rs:506-519.
- Gameplay snapshot bound is 1 MiB and is version-2 bounded: repo:prototype/osfr-tools/src/game_store.rs:13, 156-181. Version-1 character saves are still accepted for migration: repo:prototype/osfr-tools/src/character_store.rs:78.
- A gameplay save without `--content` is refused: repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:943.
- Search crash status: the note says "No fault address/dump established a cause" and calls the causes hypotheses. That still holds. The later note notes/Research/Inventory Search Crash.md is a static hypothesis, not a proven diagnosis, so no change is needed.

**Unsure:**
- "The Windows ordinary suite passes 73 tests" and "eight private-input oracles are opt-in" (the note's Verification line, mirrored in prototype/osfr-tools/README.md:74). I did not run the suite. The repo now has far more than eight `#[ignore]` tests across tests/ and src/ (for example, 8 in tests/dev_teleport.rs alone and about 8 in the gameplay w104/s6 modules). The "eight" may refer only to the gameplay oracles, but I could not confirm that from the code.
- The 6-unit checkpoint radius, 90 s limit, 10/25-coin rewards, 30 s cooldown, and the 100/25/8/600 enemy numbers. The rules are loaded from the lab's `rust-gameplay` content (repo:prototype/osfr-tools/src/quests.rs:119-127, combat.rs:70-83), which is not in the repo, so I could not compare the values.
