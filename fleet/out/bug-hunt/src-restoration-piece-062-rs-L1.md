<!-- fleet job=bug-hunt id=src-restoration-piece-062-rs-L1 status=nothing_found turns=7 usd=0.0070 tokens(read,write,in,out)=[95437, 22359, 16, 6438] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_062.rs lines 1-534 of 534

## piece_062.rs lines 1-534: no defect found

I read the whole window. It is almost entirely `const` tables plus three small pure functions (`advance`, `ability`, `attack_timing`) and `validate()`. I found no defect that I could tie to a line and show.

What I checked:

- **Panics / indexing (category 1):** `validate()` slices `PHASE_TRANSITIONS[..index]` with `index` taken from `enumerate()`, so the slice is always in bounds. The `as usize` cast on line 516 is on a `u8` widened to `usize`, so it cannot overflow. The float comparisons on lines 506 and 510 are guarded by `is_finite()`. Nothing in the window unwraps client data.
- **Reach (categories 2 and 4):** nothing in `src` declares `mod piece_062` or `pub mod piece_062`. The only hits for `piece_062` are a doc comment in the file itself and the test and checker scripts. The module is not compiled into the crate, so no client packet or save can reach it. `advance`, `ability` and `attack_timing` have no callers outside the file and its tests.
- **Logic (category 5):**
  - `advance` matches the documented three-step order, and `Defeated` is refused first.
  - `validate()` checks ability/clip agreement against `ATTACK_TIMINGS`, the interrupt-after-contact ordering, and portal ordering. Each check does what its error name says.
  - The ability/clip/effect bindings agree with `SLOT_EFFECT_BINDINGS` and `ATTACK_TIMINGS`.
  - The doc counts ("seven attack slots", "eight portal objectives", "three dialogue cues", "three bark recordings") match the tables.
- **Data spot-checks against locale:** I confirmed that the ids and names match for the portal objectives 5100669 through 5100683 (Portal 1 to 8, in order), 5100663, 5100664, 5100666, 5100994, 5100995, 5100996, 5100998, 5101000, 5100650, 5100652, 5100653, 5100693, 5100695 and 5101015. I did not check every id.

Nothing in this window is a real defect at the level of the rules.
