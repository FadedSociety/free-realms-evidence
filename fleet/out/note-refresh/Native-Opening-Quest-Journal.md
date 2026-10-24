<!-- fleet job=note-refresh id=Native-Opening-Quest-Journal status=done turns=13 usd=0.0171 tokens(read,write,in,out)=[333396, 58908, 28, 12704] model=claude-haiku-5-5 -->
# notes/Research/Native Opening Quest Journal.md

**Verdict:** minor drift. The writer's wire layout, packet sizes, subtype set, key rule, reward/reference checks and root-byte preservation all match `prototype/osfr-tools/src/opening_journal.rs`. The stale parts are the test counts and one objective-state sentence.

**Corrections:**

1. `old:` Five focused tests pass, including the explicit private-reference test:
   `new:` The focused suite `prototype/osfr-tools/tests/opening_journal.rs` has eight tests. Six run in a normal test run; the two private-data tests (the captured-journal test and the all-51-goal label test) are `#[ignore]`d. The private-reference test is one of the two ignored tests.
   `why:` `repo:prototype/osfr-tools/tests/opening_journal.rs:215,271,324,370,387,480` are plain `#[test]`s; `:520-521` and `:551-552` are `#[test]` plus `#[ignore]`. `repo:notes/Autopilot/F227.md:77-78` records `opening_journal 6/2` (6 passed, 2 ignored).

2. `old:` Result: 5 passed, 0 failed. Normal `test --test opening_journal` runs four synthetic tests and leaves the private-data test ignored.
   `new:` Result at the tip: 6 passed, 2 ignored in a normal run. Normal `test --test opening_journal` runs six synthetic tests and leaves the two private-data tests ignored. `--include-ignored` also needs `OSFR_JOURNAL_SOURCE_CONTENT` and `OSFR_JOURNAL_MAPPED_CONTENT` for the all-51-goal test, which the command above does not set.
   `why:` `repo:prototype/osfr-tools/tests/opening_journal.rs:521-522` and `:552-553` (env vars read for the second ignored test); `repo:notes/Autopilot/F227.md:77-78`.

3. `old:` All objectives are journal-visible as active; ordered gameplay triggers remain enforced by OpeningEngine.
   `new:` Objectives are journal-visible with state 1 (active) until their counter reaches the requirement, then state 2 (complete); ordered gameplay triggers remain enforced by OpeningEngine.
   `why:` `repo:prototype/osfr-tools/src/opening_journal.rs:500` (`if goal.count == goal.required { 2 } else { 1 }`). This also contradicts the note's own line on state 2 in the packet section.

**Checked and holding (no change):** the full-record layout and the 69-byte empty RewardBundle (`opening_journal.rs:465-509`); subtype set 3/4/9/10/12 and their inner lengths 10/27/23/10 plus the 6-byte header (`:300-383`, `:459-463`); the 8-byte root tail preserved (`:177-178`, `:282`, `:567-596`); live keys use `goal.id` while full records use the tuple ordinal (`:356-358`, `:487-488`); visibility and rewarded-omission on reconnect (`:387-389`, `:333-340`); regression and definition-change rejection (`:315-328`); reward type 1 only (`:549`); patch length-header and unique-span checks (`:249-269`). Native function addresses cited in the note (`00c7cc80`, `00c7aeb0`, `00c7af60`, `00c7b070`, `00c7b230`, `00c7b300`, `00c7c130`, `00c7a910`, `00c7a990`, `00c7aa10`, `00940c60`, `0093c840`, `008fd770`, `00922810`, `0092b050`, `00c7cd40`, `00baf380`, `00bab950`) all exist in the client `fn` table. `gameplay.rs:1574` and `:4243-4255` wire `patch_self` and `updates`.

**Unsure:**
- The byte counts (7,970-byte span, 203,837 and 196,215 oracle bytes) and the `lab/reports/*` oracle paths are private. The 7,970 figure matches `tests/pieces/test_piece_070.py:257`; the others could not be checked.
- The native field offsets (for example `+0xf0` set by `00bab950`, and the root and objective offsets) were only checked for function existence, not re-disassembled.
- The Native Creator Delivery Proof run is cited as "run072258". The note file calls it `client-baseline-20261008T072258Z`, which is consistent, but I did not verify the "initially empty journal" and first-accept claims.
