<!-- fleet job=note-refresh id=Developer-Teleport status=done turns=17 usd=0.0227 tokens(read,write,in,out)=[653446, 63292, 36, 16456] model=claude-haiku-5-5 -->
# notes/Research/Developer Teleport.md

**Verdict:** stale in its command-behaviour sections. The wire-packet, writer-vector, test-count and relocation-boundary claims still hold, but the standoff distance, the sampler's base direction, the name-matching rules, the zone gate and the `--dev-tools` gate have all moved since the note was written.

**Corrections:**

1. `old:` The arrival is `4.0m` from the actor at the actor's own Y, facing the actor.
   `new:` The arrival is `5.0m` (`STANDOFF`) from the actor at the actor's own Y, facing the actor.
   `why:` repo:prototype/osfr-tools/src/dev_teleport.rs:11 (`pub const STANDOFF: f32 = 5.0`); the test at tests/dev_teleport.rs:401 asserts the arrival is `STANDOFF` away. Native Round5 050310.md:96 records the 2 m → 5 m change.

2. `old:` The candidate directions are sampled relative to the character's current facing vector in the order `0, +45, -45, +90, -90, +135, -135, 180` degrees, with angle0 on the approach side (the facing vector reversed, so a repeated `goto` stays put) and positive angles counter-clockwise in XZ.
   `new:` The candidate directions are sampled relative to the target's own facing (its finite heading) in the order `0, +45, -45, +90, -90, +135, -135, 180` degrees, with angle0 on the side the target faces. Only an actor without a finite heading falls back to the approach side (the character's facing vector reversed, so a repeated `goto` stays put). Positive angles counter-clockwise in XZ.
   `why:` repo:prototype/osfr-tools/src/dev_teleport.rs:282-287 (`base` is `actor.heading.map(sin_cos)`, `approach_direction` only when that is absent); :38-49 (`Target::from(&OpeningActor)` sets `heading: Some(..)`); :274-281 doc comment.

3. `old:` Matching is exact name, then unique GUID, then unique name prefix, then unique name substring; ambiguous or unknown targets reply with candidates and never move the character.
   `new:` Matching is GUID (when the query parses as a number), then exact name, then unique name prefix. There is no substring match. Ambiguous or unknown targets reply with candidates and never move the character.
   `why:` repo:prototype/osfr-tools/src/dev_teleport.rs:209-247 (`resolve`: `parse::<u64>` first, then exact, then `starts_with`; no substring branch). The substring filter exists only in `list` (:169-178).

4. `old:` It is off unless the launcher passes `--dev-tools`, and it changes nothing except the character position and facing.
   `new:` It is off unless the launcher passes `--dev-tools` or the gateway runs an account store and the caller's role is builder or admin (both may run `goto`). It changes nothing except the character position and facing.
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:3669-3670 (`(self.dev_tools || self.role_commands) && can_run_realm_command`); repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:953 (`set_role_commands(options.account_store.is_some())`); repo:prototype/osfr-tools/src/account_store.rs:55-65 (`"goto"` is in the Builder list; Admin allows all).

5. `old:` `realm goto <name or GUID>` and `realm goto list` are handled before the existing opening chat dispatch, and only while the character is in zone0 with finite coordinates.
   `new:` `realm goto <name or GUID>` and `realm goto list` are handled before the existing opening chat dispatch, in zone0 or in another zone that lists its own targets (an encounter arena), and only with finite coordinates.
   `why:` repo:prototype/osfr-tools/src/dev_teleport.rs:99-106 (a non-zero zone is refused only when no target lists that zone; the comment says arenas work "only when they list their own targets").

6. `old:` Relocation is refused while a crafting movie is open, while an encounter is active, and while the character is knocked out; every refusal leaves all state unchanged.
   `new:` Relocation is refused while a crafting movie is open, while an encounter is active outside a battle arena (inside an arena, where only that arena's targets exist, relocation stays in the instance), and while the character is knocked out; every refusal leaves all state unchanged.
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:4226-4241 (`relocation_block`: `active() && !in_battle_arena()`).

**Unsure:**

- Note line 39 gives the farm-cluster numbers (`[-2116.839,-56.52175,208.5168]`, "4.000m from Mae and7.794m from the table", "1.436m" for the old approach). These were computed at the 4.0 m standoff and the old approach-side sampling. The current code arrives 5.0 m out and samples from the target's heading, so these figures are stale. I did not recompute the new arrival point, so I am not proposing replacement coordinates. The regression test (tests/dev_teleport.rs:386-425) is the current evidence.
- Note line 37 says the arrival is "inside the actor's12m interaction radius". The text is garbled and I could not confirm the radius value from `opening.rs` (`interaction_radius` is per-actor data, :126, :595).
- Note line 35 says `goto` is handled "before the existing opening chat dispatch". The call site is in the `realm ` branch at repo:prototype/osfr-tools/src/gameplay.rs:4315; I did not trace whether an earlier opening handler intercepts the chat first.
- The integration-test count holds: seven `private_dev_teleport*`/`private_dev_tools*` tests in tests/dev_teleport.rs (lines 202, 224, 386, 429, 473, 544, 603). The 187-passed suite count is in an evidence log I did not open.
