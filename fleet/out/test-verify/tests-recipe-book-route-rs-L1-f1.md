<!-- fleet job=test-verify id=tests-recipe-book-route-rs-L1-f1 status=done turns=6 usd=0.0064 tokens(read,write,in,out)=[59613, 21668, 14, 6233] model=claude-haiku-5-5 -->
# high: tests/recipe_book_route.rs:232

**Verdict:** `confirmed`

**Evidence:** I tried to refute the claim and could not, for the two length-tolerant mutations it names.

- **Recipe 1 is not learned.** `fixture()` (tests/recipe_book_route.rs:152-156) makes the learned set explicit for GUMBO (70) only. The base set comes from `Gameplay::load(..., None)`, which seeds `[11, 70, 4, 2002]` (src/gameplay.rs:867). Recipe 1 is not in it, so a start with id 1 is refused as `NotLearned` before any state change.
- **Mutation A: trailing bytes accepted.** Relax `decode` (src/recipe_book.rs:43-48) so a 9-byte packet decodes its first id. `[26,0,24,0,1,0,0,0,0]` then yields recipe 1. The start is refused as not learned, `g.snapshot()` is unchanged, and `assert_same(..., "malformed")` at line 235 passes. The 4-byte packet still gets rejected by the unchanged `Err`. So this regression passes the whole test.
- **Mutation B: missing id defaults to 0.** The 4-byte packet decodes as id 0, which is never learned, so it is refused and the snapshot is unchanged. This also passes.
- **Counterfactual that would be caught.** Using GUMBO (70) in the 9-byte packet would, under Mutation A, run the same start that `recipe_book_cooks_a_learned_recipe_once` (line 244) runs from this same ready state. That changes the snapshot, so `assert_same` at line 235 would fail. The claim's proposed fix is sound.

**Caveat (does not overturn the verdict):** the naive removal of the length check is caught by the 4-byte packet. `inner[4..8]` with a 4-byte slice panics, `handle_at` has no `catch_unwind` (src/gateway.rs:1409), and the panic fails the test. Only the variants that accept trailing bytes, or that default a missing id to 0, pass. The claim's own `< 8` wording is the trailing-bytes variant, which is one of the escaping mutations.

The `let _ =` discard is a weakness but not the regression gap: `decode`'s `Err` is the rejection, and the test does not assert it. The fix below is about detection power, not the discard.

**Minimal fix:** in the malformed loop, use the learned id so a length-tolerant decoder would actually start a cook, e.g. `vec![26, 0, 24, 0, 70, 0, 0, 0, 0]` and `vec![26, 0, 24, 0, 70, 0, 0]`. The existing `assert_same(&g.snapshot(), &ready, "malformed")` then catches the regression.
