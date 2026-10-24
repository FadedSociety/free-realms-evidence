<!-- fleet job=test-audit id=tests-mount-routing-rs-L1 status=done turns=5 usd=0.0053 tokens(read,write,in,out)=[45144, 18113, 12, 5261] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/mount_routing.rs lines 1-533 of 533

Window reviewed: `prototype/osfr-tools/tests/mount_routing.rs` lines 1-533 (whole file). Checked against `src/mounts.rs` (`dismount_request` 507-541, `on_minigame_start` 543-550, `on_ability_use` 552-559) and `src/social_chat.rs` (`authorize_emote` 461-474, `emote_context` 485-491). The emote test is sound: `authorize_emote` returns `Ok` for animation 0, so a missing `Mounted` refusal would fail the `matches!` check rather than pass vacuously.

- **[medium] tests/mount_routing.rs:280 every_server_trigger_dismounts_and_removes_the_ride - the "zoning", "combat" and "knockout" triggers are never exercised; all four loop iterations (except "minigame") run the identical `service.dismount_request(OWNER, &owned, &[])` call, and the `trigger` string only selects between two identical calls.**
  - Why it cannot catch a regression: the test would still pass if zoning, combat or knockout handling were rewired to any other path (or removed entirely), because the test never calls such a path; its only real extra coverage is that `on_minigame_start` delegates to `dismount_request`. The `on_ability_use` hook (mounts.rs:552) is not referenced at all.
  - Fix: either rename the test to cover only `dismount_request` and `on_minigame_start`, or call each real server-side entry point (for example via the gateway hooks for zoning, combat start and knockout) and assert the same outcome for each. Add a canary that fails if a trigger stops producing `DespawnRide`.

- **[medium] tests/mount_routing.rs:311-321 every_server_trigger_dismounts_and_removes_the_ride (tail block) - the comment says "the same player cannot board again until revived", but the block only spawns while knocked out and asserts `shared.is_empty()`.**
  - Why it cannot catch a regression: no 168/1 boarding is attempted, and there is no revive step or assertion on `notice`, `view(OWNER)` or `is_mounted()`. A change that let a knocked-out player board (after a spawn that still produces no shared packets, for example a notice-only path) would pass.
  - Fix: after the knockout spawn, assert `wire.notice == Some("You cannot use a ride here right now.")` and `service.view(OWNER).is_none()`, then attempt `mount_request(actor)` while knocked out and assert it is refused and `!is_mounted()`; optionally clear `knocked_out` and assert boarding succeeds to pin the "until revived" claim.

- **[medium] tests/mount_routing.rs:488-504 every_catalogued_ride_builds_a_valid_actor - the doc says each ride "has a model", but the body never checks a model; it only checks the notice, the shared packet count and the `35,0,2,0` prefix.**
  - Why it cannot catch a regression: a shipped ride whose model id is missing or blank in `mounts.json` (or a model lookup that falls back to a default) still builds an AddNpc with that prefix and passes. The test also only tries `item_definition_id_candidates[0]`, so a broken second candidate is never summoned by item.
  - Fix: assert on the model field the AddNpc carries (or the catalog's model accessor, non-zero and equal to the catalog's value) for each ride, and loop over every item candidate with `SpawnByItem` as well as `Spawn`, or correct the doc to drop "has a model".

- **[low] tests/mount_routing.rs:502-503 every_catalogued_ride_builds_a_valid_actor - `seen == catalog.mounts().count()` is tautological (the counter is incremented once per loop iteration), and `seen >= 50` pins a magic count of the shipped content.**
  - Why it cannot catch a regression: the first check can never fail, and the second breaks whenever the content file changes size, without testing the ride behaviour the test is about (churn, not a missed bug).
  - Fix: drop the `seen` counter and keep a non-empty check (`assert!(catalog.mounts().count() > 0)`), or assert against a named list of the rides that must be present.

- **[low] tests/mount_routing.rs:531-532 effects_keep_the_owner_roster_private - the test pins the exact number and order of effects (`vec![(false, false), (true, true)]`) for a spawn.**
  - Why it cannot catch a regression: it is about roster privacy, but any added or reordered effect (for example a second notice or a re-ordered roster refresh that is still private) breaks it without any privacy change, which is churn rather than a missed bug.
  - Fix: filter the effects to the roster packet and the `SpawnRide` effect and assert only their `nearby()` flags and kinds, rather than the full vector.
