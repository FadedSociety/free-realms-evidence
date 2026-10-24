<!-- fleet job=note-refresh id=Collections-Achievements-Titles status=done turns=20 usd=0.0202 tokens(read,write,in,out)=[552073, 57647, 42, 14956] model=claude-haiku-5-5 -->
# notes/Research/Collections Achievements Titles.md

**Verdict:** minor drift. Most checkable facts hold at the tip: reserved and supported bundle entry types, the ID namespaces (241 + 318 + 36 = 595), the 85 job-rank and 5 quest-count bindings with 228 unbound, the six `tests/progression_extras.rs` tests, `tests/startup_selfdata.rs:317` (253), and the 108/150/152 encoders. The integration statements are stale. They describe the module as unwired, but it is registered and called from `Gameplay`.

**Corrections:**

1. `old:` The new module is not registered in `lib.rs` and is not wired to harvest, quest, reward-bundle, account-save or gateway handlers.
   `new:` The module is registered in `lib.rs` and wired into `Gameplay`. Achievement counters settle at the login and zone-ready paths (`gameplay.rs:1713`, `:1802`), and `gameplay/progression.rs:1-12` says job XP, quest completion and minigame payouts settle there too. Client 108/152 requests route through `handle_progression_extras` (`gameplay.rs:2225`, `:2423`). The gateway's trusted award hooks call into `Gameplay` (`gateway.rs:1297-1306`).
   `why:` `repo:prototype/osfr-tools/src/lib.rs:71` (`pub mod progression_extras;`); `repo:prototype/osfr-tools/src/gameplay.rs:1713`, `:1802`, `:2225`, `:2423`; `repo:prototype/osfr-tools/src/gameplay/progression.rs:1-12`; `repo:prototype/osfr-tools/src/gateway.rs:1297-1306`.

2. `old:` claim history is exportable as claimed IDs but is not connected to an account save.
   `new:` claim history is exportable as claimed IDs and is saved with the character's gameplay state as `GameplayState.progression_extras`, which is written through the save store.
   `why:` `repo:prototype/osfr-tools/src/gameplay.rs:132-135` (field comment: "W178 title ownership and durable claim history"); `repo:prototype/osfr-tools/src/gameplay.rs:1347-1372` (`state()` emits `progression_extras`); `repo:prototype/osfr-tools/src/game_store.rs:25` (`gameplay: Option<GameplayState>`).

3. `old:` Claim once-per-account behavior requires the caller to persist `claimed_ids` with the reward state.
   `new:` Claimed IDs persist inside `GameplayState.progression_extras` on the gameplay save path, so the caller does not need to persist them separately. The tracker map is still session state.
   `why:` `repo:prototype/osfr-tools/src/gameplay.rs:132-135` and `:1372`. The "tracker map is session state" half of the note still holds (same comment at `:133`).

**Unsure:**

- Whether the character's `GameplayState` save counts as the "account save" the note means. The code only shows a `game_store` save of `GameplayState`. I did not check the account store.
- The exact trigger mapping for "harvest" and "quest". `sync_achievement_progress` is called only from the two login and zone-ready call sites I read. The harvest and quest coverage comes from the module's doc comments, not from a direct call in each handler.
- Client addresses, the `lab/` report hashes and the cq.py commands are outside `repo` or need the client, so I did not check them.
- The `startup_selfdata.rs` 7-dword prefix claim and the subtype-9 "opaque" claim were not traced line by line.
</result>
