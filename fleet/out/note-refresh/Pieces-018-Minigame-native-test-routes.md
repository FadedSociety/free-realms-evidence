<!-- fleet job=note-refresh id=Pieces-018-Minigame-native-test-routes status=done turns=11 usd=0.0158 tokens(read,write,in,out)=[252861, 44509, 24, 15446] model=claude-haiku-5-5 -->
# notes/Research/Pieces/018 Minigame native test routes.md

**Verdict:** badly stale. The forging TYPE 8/9 conflict the note centres on was resolved (row 139 is TYPE 8, the checker no longer raises a finding). The gate literal the checker re-reads has moved in `gameplay.rs`, and the test counts are off by one. The route catalogue itself (nine routes, gate, resolver, `Command::Route`) still matches the code.

**Corrections:**

1. old: `## The one recorded conflict`
   new: `## The forging row 139 conflict (resolved)`
   why: `repo:prototype/osfr-tools/src/restoration/piece_018.rs:153-157` gives forging `family: "TYPE 8 MatchThree (Forging row 139)"`, `original_type: 8`. `repo:notes/WorkItems/Candidate Evidence Reconciliation.md:11` records that the stale TYPE 9 claim was removed.

2. old: `while the accepted movie family is `TYPE 9` (mimic anvil).`
   new: `and the Rust route now uses the same catalogue family, `TYPE 8 MatchThree` (`forging.rs` keeps `const GAME: i32 = 139`), so the mismatch no longer exists.`
   why: `repo:prototype/osfr-tools/src/restoration/piece_018.rs:156-159`; `repo:prototype/osfr-tools/src/forging.rs:17`.

3. old: `The Rust table cites the module constant as the id authority and the checker
records the mismatch as a finding instead of silently rewriting either side:`
   new: `The Rust table cites the module constant as the id authority. The checker's finding applies only to `NativeAccepted` routes whose family starts with `TYPE 9`, so with row 139 at TYPE 8 it records no finding:`
   why: `repo:scripts/pieces/piece_018.py:420` (finding guard); `repo:prototype/osfr-tools/tests/piece_018.rs:274-278` (`forging_row_139_is_type_8_match_three`).

4. old: `This is the only finding in the bundle; a missing or extra finding fails the`
   new: `The bundle now has no finding. A finding appearing or disappearing is a change to review, and the Python tests check for it, though test_the_only_finding_is_the_recovered_forging_type_conflict (`tests/pieces/test_piece_018.py:238`) now needs updating:`
   why: `repo:scripts/pieces/piece_018.py:420` and `repo:tests/pieces/test_piece_018.py:238`. The finding no longer fires, so that test's premise is stale.

5. old: `| `src/gameplay.rs` | `dev_tools: false,` and `self.dev_tools && self.developer_teleport(` |`
   new: `| `src/gameplay.rs` | `dev_tools: false,` and `tool && self.developer_teleport(` (with `let tool = self.may_run(command);`) |`
   why: the literal `self.dev_tools && self.developer_teleport(` no longer appears in `repo:prototype/osfr-tools/src/gameplay.rs`. The call is now at `:4315` as `if tool && self.developer_teleport(`, with `tool` set at `:4308`. `repo:scripts/pieces/piece_018.py:52` still requires the old literal, so the checker's gate check fails at this tip.

6. old: `existing `self.dev_tools` branch, convert the loaded `OpeningActor` rows to`
   new: `existing `tool && self.developer_teleport(` branch (`tool` is `self.may_run(command)`, which also admits server-owned account roles, not only `--dev-tools`). Convert the loaded `OpeningActor` rows to`
   why: `repo:prototype/osfr-tools/src/gameplay.rs:3669-3670` (`(self.dev_tools || self.role_commands) && can_run_realm_command`) and `:4308-4315`. The integration must pass `enabled` as `self.dev_tools`, not as the `tool` flag.

7. old: `- The forging id/type conflict needs a lead decision; the checker keeps
  failing loudly if the finding disappears.`
   new: `- The forging id/type conflict is resolved: row 139 is TYPE 8 and the checker records no finding.`
   why: `repo:prototype/osfr-tools/src/restoration/piece_018.rs:156-157`; `repo:scripts/pieces/piece_018.py:420`.

8. old: `| `forging` (`forge`) | native-accepted | game 139 (see conflict below) |`
   new: `| `forging` (`forge`) | native-accepted | game 139, TYPE 8 MatchThree (row 139 conflict resolved) |`
   why: `repo:prototype/osfr-tools/src/restoration/piece_018.rs:156-159`; `repo:notes/WorkItems/Candidate Evidence Reconciliation.md:11`.

9. old: `verified by 13`
   new: `verified by 14`
   why: `repo:prototype/osfr-tools/tests/piece_018.rs` has 14 `#[test]` attributes (lines 154 to 485). Two are `#[ignore]` (lines 456 and 486), so 12 are ordinary, not 11.

10. old: `Rust tests (11 ordinary, 2 private-content)`
    new: `Rust tests (12 ordinary, 2 private-content)`
    why: same as item 9. Lines 154, 172, 229, 243, 273, 293, 316, 327, 342, 390, 400, 421 are ordinary, and 455 and 485 are the two ignored private-content tests.

11. old: `13 owned tests:`
    new: `14 owned tests (12 ordinary, 2 ignored):`
    why: same as item 9, `repo:prototype/osfr-tools/tests/piece_018.rs`.

12. old: `# routes=9 errors=0 findings=1      -> green-03-checker-cli.log`
    new: `# at this tip the checker reports routes=9 with the gate-literal error and findings=0 (re-run to confirm); the logged run predates the TYPE 8 correction`
    why: `repo:scripts/pieces/piece_018.py:437` (`gate_errors` runs on every route check) and `:420` (no finding for TYPE 8). This is derived from the source, not from a re-run of the checker.

**Unsure:**
- The Python test count (15) and the `not yet registered in lib.rs` claim check out. `restoration/` has no `mod.rs`, and no `mod restoration` appears under `src/`, so the module is not registered.
- The table's cited test files for the module-driver routes (`tests/mining.rs` and the others) and the cooking/smelting `GAME` constants (46, 77) match the code. I did not check the recovered catalogue types beyond row 139, which is TYPE 8 at `repo:notes/Research/original-activity-coverage.json:587`.
- The historical run logs (`green-*.log`, `red-01`) live in `lab/reports`, which I did not read, so I could not confirm their contents.
