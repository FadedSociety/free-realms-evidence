<!-- fleet job=test-verify id=tests-piece-034-rs-L1-f1 status=done turns=5 usd=0.0070 tokens(read,write,in,out)=[49190, 28390, 12, 5891] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/piece_034.rs:412

**Verdict:** `confirmed` (the gap is real; the severity label is arguable, and the test's skip is documented in its doc comment, so the real problem is that the skip is silent in the gate).

**Evidence I tried to refute it with, and why it failed:**

1. **No gate sets the variable.** A repo-wide search for `OSFR_PIECE_034_CATALOGUE` finds only `prototype/osfr-tools/tests/piece_034.rs:413`. No CI, script, or `.ps1`/`.yml` config sets it. The only other hits are notes (`notes/Research/Pieces/034 Ninja progression.md:147`, the one-off `green-final.log` run).

2. **The early return passes silently.** `tests/piece_034.rs:412-415`: `let Some(path) = std::env::var_os("OSFR_PIECE_034_CATALOGUE") else { return; };` with no `#[ignore]` and no failure. Cargo reports it as `ok`.

3. **The real-catalogue assertions are not duplicated elsewhere in the default run.** The synthetic `CATALOGUE` const (`tests/piece_034.rs:46-108`) is a 3-weapon trimmed document, so `weapon_count() == 71` (line 423) and the full `canonical_tiers()` list of five tiers (line 428) are asserted only in the gated test. The Python suite `tests/pieces/test_piece_034.py` runs separately, is not part of `cargo test`, and does not pin 71 (grep shows no `71` hit in that file). A change to the producer's output (`scripts/pieces/piece_034.py:1084`) therefore changes nothing the default gate reads.

4. **Walk-through of the named regressions against the default run:** the emitted-document count (71), tiers, level-1 mapping (`75091 -> 2154/2050`) and special damage/recast (889, `cooldown_ms: None`) are checked only when the env var is set. Under the default run, any change to the emitted file passes. The synthetic fixture would catch edits to its own inline text, but not to the producer or to the emitted artifact. So the claim's "cannot catch the regression it names" holds for the named regression.

**Caveat on the fix:** the proposed `#[ignore = "..."]` is sound. Cargo then lists the test as `ignored`, so the skip is visible. A CI-conditional `expect` also works. The strongest fix is a trimmed checked-in copy of the emitted document, but that needs its provenance (lab-only data) cleared first.

**Minimal fix:** at minimum, make the skip visible: `#[ignore = "needs OSFR_PIECE_034_CATALOGUE; run with --ignored"]` on `the_emitted_ninja_catalogue_validates`, or fail when the variable is unset and `CI` is set. Add a canary such as `assert_eq!(synthetic_weapon_count, 3)` only if you also want the trimmed fixture to pin the count.
