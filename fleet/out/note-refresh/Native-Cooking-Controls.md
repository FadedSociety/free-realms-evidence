<!-- fleet job=note-refresh id=Native-Cooking-Controls status=done turns=14 usd=0.0150 tokens(read,write,in,out)=[351760, 56877, 30, 8823] model=claude-haiku-5-5 -->
# notes/Research/Native Cooking Controls.md

**Verdict:** current, with one minor drift. The round tuning matches the shipped reconstructed content, the stopwatch and stat-report claims hold, and the note's "not established" caveats are still accurate.

**Corrections:**

- `old:` The server ignores the reported quantity for reward size and requires all six report groups before the fixed recipe transaction.
  `new:` The server requires the reported quantity to be `0` (any other value is rejected as invalid), does not use it for reward size, and requires all six report groups before the fixed recipe transaction.
  `why:` repo:prototype/osfr-tools/src/cooking.rs:504-509 returns an error for `quantity != 0`, so the field is validated, not merely ignored. The reward comes from the fixed recipe at cooking.rs:526-531, and the six-round and final-stat gate is at cooking.rs:513-519.

**Checked and holding:**

- Tuning counts (table rows and the stew line). The configured values are Tenderize `8` hits (`data[1]=8`), Chop `15` slices (`data[1]=15`), Smash `2` hits per fruit (`data[2]=2`), and Stir `10` turns (`data[1]=10`). Source: `refs:rust-opening-cooking-original-assets/cooking.json`, phases 1 to 6. The server's range checks at cooking.rs:642-656 and 674-681 accept these values.
- Six rounds: `cooking.rs:614` requires exactly 6 phases, and the phase order matches `STAGES`/`INGREDIENTS` at cooking.rs:22-23.
- Stopwatch: `cooking.rs:478-481` and the comment at cooking.rs:479 say the timer is a stopwatch, not the 90-second row countdown. The row duration is 90 (`cooking.json`), which matches the note's contrast.
- Four stage statistics per round and summed bad/good/perfect totals plus cumulative time on the final report: `cooking.rs:474-493` (kinds 0-3 per round) and `cooking.rs:692-707` (`validate_totals`).
- `Research/Original Cooking.md` link target exists, and the `scripts/prepare-cooking.py:46-47` comment repeats the same defaults.

**Unsure:**

- The `../lab/decompiled/minigames/cooking/scripts/__Packages` file list cannot be checked: `lab/` is not in the repo or refs. The provenance list in `refs:rust-opening-cooking-original-assets/cooking.json` names `TenderizeElem.as`, `RoundChop.as`, `RoundSmash.as`, `RoundMeasure.as`, `RoundAddIngredient.as`, `RoundStir.as`, `Library/Timer.as` and `CookingGameClient.as`, all of which the note lists. It does not list `RoundTenderize.as`, `ChopKnife.as`, `Hammer.as` or `StirBowl.as`, so those are unverified.
- The client-side mouse behaviour (knife hit test, bucket direction, add-ingredient drop rules, the "Click the visible knife" wording) is AS2 behaviour. It is not reachable from the server code or the decompiled client database. `Research/Original Cooking Later Controls.md` describes the Measure, Add and Stir controls consistently with the note, but I did not verify the Chop or Tenderize rows independently.
- The "roundCompleted" trigger name is not in the server code except as a comment at cooking.rs:694. It is consistent with `Reviews/Native Cooking and Mae 054421.md`.
