<!-- fleet job=testaudit-infer id=recipe_book_route-v1 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[8081, 11769, 6, 1183] model=claude-haiku-5-5 -->
# tests/recipe_book_route.rs

{"file": "tests/recipe_book_route.rs",
 "tests": [
  {"name": "recipe_book_refusals_change_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal file: missing inputs, unknown/extreme ids, away from station, wrong active job, and malformed lengths each assert the snapshot is unchanged. tests/crafting_stations_route.rs (line ~446 comment) names this file as the gateway-level partner for the private-content case, and the public-content counterpart there does not exercise the private Cooking movie path, so no equally strong test elsewhere was found."},
  {"name": "recipe_book_cooks_a_learned_recipe_once", "verdict": "keep", "covered_by": null, "reason": "Only end-to-end check that a book start runs the cooking movie, replay-safe start, remote win refused when away from station, input consumption exactly once, replayed win is a no-op, and exit leaves the recipe unrunnable without inputs. Closest files (tests/cooking.rs six-round/once-only tests, tests/piece_012.rs repeated completion) drive the cooking transaction without the recipe-book gateway route, so they are not the same path."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "Both tests are #[ignore]d and need private versioned Cooking content, so they may not run in the normal suite; that does not make them redundant. Overlap exists with tests/recipe_book.rs (unit-level decode/start refusals), tests/crafting_stations_route.rs (public gateway book_start cases) and tests/cooking.rs (movie transaction). Those cover pieces, not the full gateway route with private content, so I kept both. Excerpt was truncated but the file was read to its end (line 287)."}
