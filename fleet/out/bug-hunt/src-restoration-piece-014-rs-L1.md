<!-- fleet job=bug-hunt id=src-restoration-piece-014-rs-L1 status=nothing_found turns=6 usd=0.0048 tokens(read,write,in,out)=[61007, 18132, 14, 3877] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_014.rs lines 1-558 of 558

No defects found in `prototype/osfr-tools/src/restoration/piece_014.rs` lines 1-558.

What I checked:

- **No panic surface on client input.** The only executable code is the linear lookups (`pattern`, `equipment_by_id`, `slot`, `class_owner`, `profile`), `allows`, and `check_equip` (lines 500-558). They use `iter().find` and `slice::contains` with no indexing, slicing, `unwrap`/`expect`, arithmetic, or allocation. Every input is a plain `i32` compared for equality.
- **No unbounded growth.** All collections are `&'static` tables. Nothing is built from client-supplied counts.
- **No atomicity issue.** `check_equip` is pure: it takes two ids, performs no mutation, and returns a `Result`.
- **Doc vs. behaviour.** `allows` (lines 532-546) and `check_equip` (lines 548-558) implement what their doc comments state: the class allowlist and the slot spool must both admit the definition. The `?` chain is correct, and the rejection order (definition, then profile, then class, then slot) matches the rejection variants.
- **Table consistency.** `PATTERNS` has 28 entries, matching `PATTERN_COUNT`. `param1` values are unique. Each `CLASS_OWNERS` profile id matches its `PROFILES` entry (43 for classes 25 and 71, 16 for classes 34 and 58). Each equipment class is in its owner's allowlist. Spot-checked locale strings agree: 1565 "Spunky Scrapper Hammer Recipe", 1587 is its description, 2614 "Blacksmith", 2873 "Brawler".
- **Reachability.** `src/` does not register `piece_014` (no `mod`/`pub mod` for it anywhere under `src/`). The module is only compiled by `tests/piece_014.rs` through `#[path]`. No production code or packet handler calls `check_equip` or any other function here. Even if it were wired in, the input path would still be bounded `i32` comparisons, so there is no client-controlled crash, growth, or item grant in this file.

Observation, not reported as a defect: `check_equip` does not consult `ClassOwner.wield_type`, and class 999 appears in both allowlists. Neither is contradicted by the file's own doc comments, and no equipment record uses class 999, so I did not treat either as a defect.
