<!-- fleet job=bug-hunt id=src-gameplay-housing-rs-L1 status=done turns=10 usd=0.0100 tokens(read,write,in,out)=[135634, 26325, 22, 10605] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay/housing.rs lines 1-232 of 232

Reviewed `gameplay/housing.rs` lines 1-232 and the callers it depends on (`gameplay.rs` 1147, 1377, 1642, 1685, 2239; `gateway.rs` 1257, 1393; `housing_service.rs` enter/leave/end_visit; `inventory.rs` adopt_state). No remote-triggerable crash, unbounded growth, or gain/loss of items or coins was found in this window. The request path is atomic: the session and the inventory are cloned, and both are committed only at the end (`self.housing = Some(session)` after `adopt_state(...)?`). The `scene.position[..3]` slices at 202-203 are on `[f32; 4]`, so they cannot panic. The `leave` branch dropping `outcome.replies` is correct, since `leave()` returns no replies.

One finding, low severity, which needs an operator action to trigger:

- **[low] prototype/osfr-tools/src/gameplay/housing.rs:41-49 (load, `Ok(None)` at 37-39) - when `houses.json` is absent, saved lots are discarded and the next save erases them.**
  - Failure scenario: the operator runs with `houses.json`, a player buys or is granted a lot, and it is saved. The operator later removes `houses.json`. On login, `load` returns `Ok(None)` without looking at `saved`. `Gameplay::state` (gameplay.rs:1377) then writes `housing: None` (the `self.housing` is None), so the lot and its fixtures are gone from the save on the next save.
  - Reach: `gameplay.rs:1147` calls `HousingSession::load(directory, saved_housing.as_ref(), ...)`. `saved_housing` comes from the stored character state (gameplay.rs:607). The `saved` argument is ignored whenever the file is missing.
  - Fix: when `houses.json` is missing and `saved` is `Some` with non-empty lots, return an error (or keep the saved state in a passthrough field so `state()` writes it back) instead of silently returning `Ok(None)`. Only then should the dormant path drop it.

Also noted, not reported as defects: `housing.rs:133` (`u8::try_from(scene.unknown).unwrap_or(1)`) is a silent fallback on server-side content, not on client input.
