<!-- fleet job=bug-verify id=src-harvesting-lifecycle-rs-L1-f1 status=done turns=6 usd=0.0064 tokens(read,write,in,out)=[74920, 27285, 14, 4558] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/harvesting_lifecycle.rs:208-236

**Verdict:** refuted (the mechanism is real inside the wrapper, but no production input can reach it).

**Evidence:**

1. **Module tree.** `src/lib.rs:29` has `pub mod harvesting;`. `src/harvesting.rs:33-34` includes `#[path = "harvesting_lifecycle.rs"] pub mod lifecycle;`. So the file is compiled into the library, but only its `reward_grant` is used in production (`gameplay/crafting.rs:446`, `crate::harvesting::lifecycle::reward_grant`).

2. **Reach: `HarvestingLifecycle::tick` has no production caller.** A repo-wide search for `HarvestingLifecycle` finds construction and calls only in `tests/harvesting_lifecycle.rs`, `tests/gathering_payout.rs` and the wrapper's own file. The live gameplay path holds a raw engine, not the wrapper: `gameplay.rs:167` is `harvesting: Option<Type8Engine>`, and `gameplay.rs:116` is `Option<Type8State>` in the snapshot. Harvesting input goes through `gameplay/crafting.rs:78-80` (`type8_mut(Gather::Harvesting).handle(inner)`) and `crafting.rs:87-94` (`tick_gather` calls `Type8Engine::tick` directly). Neither touches `runs` (`MinigameRuns`) or `validate_pair`, so the failure as described (engine `Lost` with a run `Offered`/`Starting`, saved, then rejected by `restore()`) cannot occur through the live server. The live save has no lifecycle snapshot to fail.

3. **Mechanism check (for completeness).** The claim's description of the internals is accurate. `mining.rs:552-554` sets `Lost` for any non-terminal phase when `wall_ms == MAX_WALL_MS`. `minigame.rs:548-549` makes `finish_inner` return a default outcome for non-`Playing` runs. `harvesting_lifecycle.rs:233-234` stores without `validate_pair`. But this is dead-in-production code. It affects only the test-only composition (the wrapper is not constructed by any handler or save path), so the input-to-defect chain breaks at step 2.

4. **Other paths.** `handle_control` (259), `close` (282) and `handle_movie` validate before storing. Only `tick` skips it, as the claim says. That matters only if `HarvestingLifecycle` is wired in later, so it is a latent hardening item, not a live defect.

**Severity if confirmed:** n/a (refuted). If the wrapper is wired into gameplay later, the `validate_pair` gap in `tick` would become a real medium-severity issue, and the suggested one-line fix (`validate_pair(&engine, &runs)?;` before line 233) would be correct. Note that the mapping `Offered`/`Starting` to `Lost` would also need the cancel-or-finish handling the claim suggests.
