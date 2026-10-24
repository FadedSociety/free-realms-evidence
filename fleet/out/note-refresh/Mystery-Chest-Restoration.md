<!-- fleet job=note-refresh id=Mystery-Chest-Restoration status=nothing_found turns=13 usd=0.0151 tokens(read,write,in,out)=[350037, 53348, 28, 9841] model=claude-haiku-5-5 -->
# notes/Research/Mystery Chest Restoration.md

**Verdict:** current. Every checkable claim about our code and status I could settle still holds at the tip. No correction is needed.

**Checked and holding:**
- Files exist: `src/mystery_chest.rs` (codec), `src/mystery_chest_loot.rs` (bindings), `tests/mystery_chest_codec.rs` (12 `#[test]`s), `tests/mystery_chest_gameplay.rs` (4 `#[test]`s, each `#[ignore]`d as private). This matches the "12 passes" and "four private chest checks" claims.
- Codec constants match the note: request subtypes 15 (Use) and 16 (Check), reply 38/30 with five i32 values then a success byte, reward 50/1 with reward kind 16, Mystery Key `KEY = 78137`. Source: `src/mystery_chest.rs:79-97`, `src/mystery_chest.rs:146-157`, `src/mystery_chest_loot.rs:17`.
- Load validation matches the note: Type28 check, key presence, distinct known rewards, content bounds (256 KiB, 64 chests). A missing `mystery_chests.json` returns `Ok(None)`, so existing packages are preserved. Source: `src/mystery_chest_loot.rs:42-95`.
- Check verifies both chest and key (`success = chest.is_some() && key.is_some()`), and an eligible Check records one instance ID in `pending`. Source: `src/mystery_chest_loot.rs:124-130`.
- Use is a confirmation guard, not a replay path. A Use for another instance does not clear the pending Check (`src/mystery_chest_loot.rs:132-136`), and an unconfirmed Use sends the "Confirm" refusal without opening anything (`:145-150`). Replay therefore needs a fresh Check, as the note says.
- Use is atomic. It rechecks ownership and key possession, consumes both on a cloned inventory, builds the reward packet, and commits with `*inventory = staged` only at the end (`src/mystery_chest_loot.rs:164-194`).
- Routing: `handle_mystery_chest` runs before the generic 42/35-34 inventory branch in both call sites (`src/gameplay.rs:4444` before `:4447`, and `:5334` before `:5337`).
- Session reset clears the transient eligibility (`src/gameplay.rs:1508`, `self.pending_chest = None`).
- Save before send: the gateway saves the snapshot (or the pet roster atomically) inside the staged commit, before deliveries are queued (`src/bin/osfr-gateway.rs:1928-1945`).
- The four private gameplay check names in the note match the test functions (`tests/mystery_chest_gameplay.rs:51, 130, 181, 201`).
- The reproduce target `tests/mystery_chest_gameplay.rs` exists and reads `OSFR_CHEST_CONTENT` (`tests/mystery_chest_gameplay.rs:6`).

**Unsure (not corrected, because the note does not make a false claim):**
- The Verification section does not mention a later fix. The W90 fuzz finding (an unknown-instance Use cancelling another chest's pending confirmation; see `notes/Design/Build Plan.md:149` and `tests/fixtures/app_fuzz/README.md:72`) is already fixed at `src/mystery_chest_loot.rs:132-136`. A reader may want a one-line note of that.
- "Ordinary whole Rust suite: 1549 passed" and "25 focused inventory/codec tests" are point-in-time gate counts from 2026-10-09. They match `notes/Current Progress.md:57` and `notes/Tasks.md:266`, but I did not re-run them, and later tests (e.g. `app_fuzz`) may have changed the total.
- "No purchasing backend is implemented" (the marketplace branch when success is 0) is an absence claim I did not verify by exhaustive search.
- The reconstructed chest definition 910100 appears only in the private gameplay test and in the external test package, not in shipped data. This matches the note's "local reconstruction" wording.
