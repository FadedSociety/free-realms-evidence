<!-- fleet job=note-refresh id=Pieces-011-Pet-training-activities status=done turns=19 usd=0.0249 tokens(read,write,in,out)=[787289, 69965, 40, 16522] model=claude-haiku-5-5 -->
# notes/Research/Pieces/011 Pet training activities.md

**Verdict:** minor drift. Nearly every checkable claim holds at the tip: the four files exist, the module is still unregistered, the test counts match (11 Rust, 12 Python), the 37-byte trick record, the wire constants, the once-only ledger, ordered crediting, timeout, force-end and sample bound all match the code, and the Lua handler and locale strings match the client. One gap statement is stale.

**Corrections:**

1. `old:` the 32-bit result value's meaning and the grade thresholds stay unrecovered.
   `new:` the grade thresholds stay unrecovered (the client's subtype 8 value is the selected trick id, not an unknown result code: `FinishPetGestureState` (`00cc9a90`) passes the handler's +0x94 field to `FUN_00b5ffe0`).
   `why:` client pseudocode `fn` row `00cc9a90` calls `FUN_00b5ffe0(*(param_1+0x94))` when the trick count is positive; `notes/Build Guides/Gameplay/Pets.md:77` ("sends `PetTrickGestureResult` ... with the selected trick id") and `notes/Build Guides/Gameplay/Pets.md:172` ("8 | PetTrickGestureResult | u32 trick id"). Confidence is medium: the +0x94 = trick-id reading rests on Pets.md and the field's use as a hash key, not on a separate check of the store.

**Checked and holding (no change):**
- `prototype/osfr-tools/src/restoration/piece_011.rs` exists (590 lines); `tests/piece_011.rs` has 11 `#[test]`s and `#[path]`-includes the module (line 31); `scripts/pieces/piece_011.py` and `tests/pieces/test_piece_011.py` exist, with 12 test methods.
- Not registered: no `piece_011` in `src/lib.rs`, and there is no `restoration/mod.rs`.
- `TRICK_RECORD_LEN` = 4 + 8×4 + 1 = 37 (`piece_011.rs:49`). Opcode 53 and subtypes 7/8/12/13/14/15 (`piece_011.rs:31-43`). Favourite guard `slot == 0 || slot > 4` and pet/slot-1/trick layout (`piece_011.rs:537-546`).
- Ordered crediting only against the pending node (`piece_011.rs:421-427`); `TimedOut`, `PastForceEnd`, `TooManySamples` (`:194-202`, `:408-417`, `:440`); once-only retirement by instance id (`:503-515`).
- Lua: `NotifyPetTrickReady`/`Go`/`Done` use 94617/94618 (`ScriptsBase.lua:11583-11602`); `doTrick` → `Pet.PerformTrick`, `PetWhistle1..3` on success, 1.4 s unlock on failure (`ScriptsBase.lua:23527-23544`); `PetInventorySlotMap` repeats `"TricksData"` four times (`ScriptsBase.lua:22303-22307`); `CancelPetTrick` calls `Pet.CameraRestore()`/`Pet.StopGestureGame()` (`:23178-23180`); `Pet.SetFavoriteTrick(tonumber(c)+1, b)` (`:22716`).
- Locale: 90155 Poor, 90163 Amazing!!, 94617 Get Ready!, 94618 Draw! (locale export).
- Loader `FUN_00cc9bb0` assigns the same settings keys (fn strings; the `pseudocode.c` line numbers could not be checked against this mirror).
- Waypoint counts in the table sum to 147 over 23 ids (checked by arithmetic).

**Unsure:**
- The `PetTrickGesturePoints.txt` data (147 rows, trick 103's repeated `0.5^0.7` at sequences 0 and 6) is not in the `client` mirror, so I could not re-hash or re-count the file. The hashes are cited only to `lab/`, which I cannot read.
- Locale ids 90157 and 90161 missing: the locale tool does not search by id, and I did not know their text, so I could not confirm the gap.
- The `pseudocode.c` line numbers (1806914, 1806897, 1806315, 1806329, 1348805) and the `lab/` evidence paths and SHA-256 values were not checkable from the repo.
- The Scapy / wire-probe results (929 datagrams, 17 inner frames, zero pet frames) and the 12/11-test log outputs live only in `lab/` and are not verifiable here.
- Trick-name mapping (field 2) and the "four names in the NOT LIVE catalogue row" corroboration sit outside the repo.
