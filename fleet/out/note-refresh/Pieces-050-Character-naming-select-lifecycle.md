<!-- fleet job=note-refresh id=Pieces-050-Character-naming-select-lifecycle status=done turns=10 usd=0.0128 tokens(read,write,in,out)=[183373, 37988, 22, 12368] model=claude-haiku-5-5 -->
# notes/Research/Pieces/050 Character naming/select lifecycle.md

**Verdict:** badly stale on delete (the note says native delete is not implemented and that opcode 9 answers status 2; the login service now deletes and answers 1 on success), and minor drift on the custom-name policy, which the production check-name path already applies. The artifact paths, the 10 Rust tests, the 9 Python tests, the 210/211 wire, the result-code table and the "module not registered in `lib.rs`" claim all hold at the tip.

**Corrections:**

1. `old:` Native **delete** is *not* implemented and no captured native 210/211 exchange has been
   `new:` Native **delete** is implemented in the login service (opcode 9 removes an account-owned character and saves the account store; status 1 on success, 2 when not owned or missing), but no captured native 210/211 exchange has been
   `why:` repo:prototype/osfr-tools/src/login.rs:460-479 (opcode 9 arm calls `account::delete_character` and saves); repo:prototype/osfr-tools/src/account.rs:349-390 (`CharacterDeleteStatus` 1/2, `delete_character`)

2. `old:` answers opcode 9 with status 2 because the separate gameplay save is not coordinated.
   `new:` answers opcode 9 with status 1 when the account owns the character and it is removed, and status 2 when it is not owned or missing. No gameplay-save check runs on this path.
   `why:` repo:prototype/osfr-tools/src/login.rs:460-479; repo:prototype/osfr-tools/src/account.rs:371-384. The only `GameplaySavePresent` gate is the unwired `delete_decision` in repo:prototype/osfr-tools/src/restoration/piece_050.rs:612-636.

3. `old:` until then opcode 9 keeps answering status 2.
   `new:` opcode 9 is live in `login.rs` and answers status 1 on delete, or 2 when the character is not owned; `delete_decision` is not called from it.
   `why:` repo:prototype/osfr-tools/src/login.rs:460-479; repo:prototype/osfr-tools/src/restoration/piece_050.rs:621 (`delete_decision` has no caller in `src/`)

4. `old:` recovered custom-length policy replaces today's 32-character window (that changes which custom
   `new:` recovered custom-length policy (2–14 per part, combined rule) is already applied by the production check-name path, `account::check_name_status`, which returns the short, long and total-length codes before the `identity::valid_name` check; the 32-character window is only the fallback for names that pass those thresholds (that changes which custom
   `why:` repo:prototype/osfr-tools/src/account.rs:266-286 (`check_name_status`: first/last <2 and >14, total >15, then `identity::valid_name` and `new_name_part`); repo:prototype/osfr-tools/src/identity.rs:95-107

   Note: the item "login.rs should resolve the three definition fields" still holds; login.rs:446-448 skips them (`inner.string(512)` ×3) and trusts the typed name.

5. `old:` the production-matching duplicate/invalid rule: same window as
   `new:` the duplicate/invalid rule that mirrors the `identity::valid_name` window. Production `account::check_name_status` is stricter, adding `new_name_part` (Latin letters only, single separators) and the custom-length codes, so `classify_name` is not production-matching:
   `why:` repo:prototype/osfr-tools/src/restoration/piece_050.rs:316-327 (`name_shape_valid`, identity window only); repo:prototype/osfr-tools/src/account.rs:194-202 (`new_name_part`), 279 (called from production check)

6. `old:` (key must match the saved character; a separate gameplay save blocks deletion).
   `new:` (key must match the saved character; a separate gameplay save would block deletion, but the live login delete path at `login.rs:460` does not call this gate).
   `why:` repo:prototype/osfr-tools/src/login.rs:460-479; repo:prototype/osfr-tools/src/restoration/piece_050.rs:612-636

**Unsure:**

- The total-length rule in the live path looks inverted against the note's client-text reading. `account.rs:277` rejects `first_len + last_len > 15` (letters only, no space), while the note says the client text requires combined ≥ 15 characters, and `piece_050.rs:363-365` counts the space (`"{first} {last}"` < 15). I did not change the note's table, which quotes the client text correctly. The code disagreement is worth a lead look.
- Item 4's catalogue counts (840 / 234 / 242 rows) and the 39,844-byte size were not checked against the client resources.
- The `Checks and results` figures (10, 9, 24 and 7 passing) were not re-run. The test counts are confirmed by source: 10 `#[test]` in `tests/piece_050.rs`, and 9 `def test_` in `tests/pieces/test_piece_050.py`.
- Login's delete and check-name behaviour changed after the note's status date (2026-10-09 05:30 UTC). I found no Autopilot report that covers it, so I could not tell whether the change is deliberate or dated.
