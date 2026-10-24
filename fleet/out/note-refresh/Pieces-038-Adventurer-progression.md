<!-- fleet job=note-refresh id=Pieces-038-Adventurer-progression status=done turns=16 usd=0.0228 tokens(read,write,in,out)=[600642, 68501, 34, 16423] model=claude-haiku-5-5 -->
# notes/Research/Pieces/038 Adventurer progression.md

**Verdict:** minor drift. The module, file paths, test counts, opcodes and reconciliation rules hold at the tip. The statements about the server-side wire writers and the snapshot profile check are stale or overstated.

**Corrections:**

1. `old:` no payload writer exists yet on the server side;
   `new:` a server-side encoder now exists for all four packets (`CollectionMessage::encode`, Start takes a caller-built record blob and Remove a caller-supplied body), but collection progression is not routed to the live gateway;
   `why:` `repo:prototype/osfr-tools/src/progression_extras.rs:426-463` (encodes subtypes 8, 9, 10, 11 as `[38,0,sub,0]` + body); tested at `repo:prototype/osfr-tools/tests/progression_extras.rs:228-231` and `:644-664`. Routing status: `repo:notes/Design/Build Ledger.md:97` ("Built | `progression_extras.rs` | Not routed.").

2. `old:` the four recovered update packets need writers (collection id, entry id, index,
   `new:` the four recovered update packets already have encoders (`CollectionMessage::encode`) but are not routed live; what is still missing is the full field set (collection id, entry id, index,
   `why:` `repo:prototype/osfr-tools/src/progression_extras.rs:426-463`; `repo:notes/Design/Build Ledger.md:97`. Only AddEntry is fed by real progress (`progression_extras.rs:534-542`); Start and Remove bodies are caller-supplied.

3. `old:` * updates and snapshots carry the owning profile GUID and are refused with `ForeignProfile` when they
   `new:` * updates carry the owning profile GUID and are refused with `ForeignProfile` when they (snapshots and the count readers take no GUID and check nothing; the profile is fixed at construction);
   `why:` `repo:prototype/osfr-tools/src/restoration/piece_038.rs:286-295` (only `apply` checks `player`); `:423` (`pub fn snapshot(&self)`, no player argument); `:433` and `:442` (`collected_entry_count`, `completed_count`, no check).

4. `old:` * a collection reports `Completed` exactly on the transition that fills the last entry, so a reward
   `new:` * `apply(AddEntry)` reports `Completed` exactly on the transition that fills the last entry (`approach` and `collect` return `Unlocked` even when they fill the last entry, so they do not signal completion), so a reward
   `why:` `repo:prototype/osfr-tools/src/restoration/piece_038.rs:320-324` (Completed only in `apply`); `:357-363` and `:385-386` (`approach` and `collect` return `Unlocked` with no completion check).

**Checked and holding (no change):** file paths `src/restoration/piece_038.rs`, `tests/piece_038.rs`, `scripts/pieces/piece_038.py`, `tests/pieces/test_piece_038.py` exist; opcodes 8-11 (`piece_038.rs:45-51`); type ids 10/11 (`:54-56`); `ForeignProfile`, `DuplicateIgnored`, `RequiresInteraction`, `CompletedByChildren`, `resolve_explorer_unlocks` exist (`:157-176`, `:391`); Remove keeps the definition (`:309-313`); RemoveEntry clears a flag so completion reverts (`:326-333`); `completed_count` is derived (`:442-447`); proximity range is caller-supplied and validated finite/non-negative (`:473-480`); the module is not yet registered (no `restoration` module in `src/lib.rs`, the test still uses `#[path]` at `tests/piece_038.rs:27`), so the "lead integration" gate is still open; 15 `#[test]` in `tests/piece_038.rs` and 9 `def test_` in `tests/pieces/test_piece_038.py`, matching the Verification section; the Sanctuary community reference (`refs:Sanctuary/src/Sanctuary.Packet/BaseClientUpdatePacket/`) ships only Start and AddEntry, as the note says; the checker's non-ascending-row reporting is verbatim (`scripts/pieces/piece_038.py:224-230`, `:267-268`).

**Unsure:**
- "The module normalises on definition order": `define()` stores entries in the order the caller passes and does no sorting (`piece_038.rs:258-282`). The doc comment at `:199-200` says "normalised here", which overstates it. The caller has to supply index order. I did not make a correction because the wording is ambiguous.
- The payload figures (253 rows, 1815 entries, 841 collected, 55 complete, 126 CollectionAdd rows, 19 non-ascending rows) and the 62-parameter / 14-outside-range claim: the checker and its test expect these (`tests/pieces/test_piece_038.py:129-151`, `scripts/pieces/piece_038.py:267`), but the captured `PacketSendSelfToClient.json` and the `lab/` tree are not in this checkout, so I could not recount them.
- The `pseudocode.c` line citations and the `lab/reports/piece-038-20261009T0405Z/` hashes: `lab/` is absent from the repo root, so these are unverified.
- The `Collections.json` row 10 claim (item definitions 11081-11088): the test asserts it (`tests/pieces/test_piece_038.py:161`), but I did not open the Sanctuary resource file.
