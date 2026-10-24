<!-- fleet job=note-refresh id=Derby-Service status=done turns=13 usd=0.0164 tokens(read,write,in,out)=[300565, 51210, 28, 13987] model=claude-haiku-5-5 -->
# notes/Research/Derby Service.md

**Verdict:** badly stale. The module-level facts still hold (file paths, 20 subtype layouts, `SUBTYPE_SPECS` with 20 entries, the rule defaults, the 5 tests, `pub mod derby;` in `lib.rs`). But the note says the derby reward is paid on Close, that gateway integration and routing do not exist, and that the service tests cover reward-once behaviour. None of that holds at the tip: F164 removed the Close payout, T219 added a results-phase payout in the gateway, and a gateway layer now routes derby records.

**Corrections:**

1. `old:` and once-only reward application on Close.
   `new:` and a Close that retires the match once. The flat completion reward is paid by the gateway when the results phase is reached (`gameplay/derby_session.rs:190-217`).
   `why:` `repo:prototype/osfr-tools/src/derby.rs:1762-1783` (`handle_close` pays nothing: "F164 withholds derby payouts"); `repo:prototype/osfr-tools/src/gameplay/derby_session.rs:143-170` (Close retires the match) and `:190-217` (`pay_derby_completion` on the server-observed results phase); `repo:prototype/osfr-tools/src/derby_gateway.rs:8-15`.

2. `old:` and applies the supplied reward grant once for each human Close.
   `new:` and retires the match on each human Close (`26/42`). The gateway pays a flat completion reward once per match instance when the results phase is reached, not on Close. Amounts come from `derby_entry.json`.
   `why:` `repo:prototype/osfr-tools/src/derby.rs:1762-1783`; `repo:prototype/osfr-tools/src/gameplay/derby_session.rs:190-217`; `repo:prototype/osfr-tools/src/derby_gateway.rs:8-15` and `:103` (`paid_matches` ledger).

3. `old:` or gateway integration. The earlier
   `new:` or gateway integration (the gateway layer is separate: `derby_gateway.rs`, `gameplay/derby_session.rs`, and routing at `gameplay.rs:2267`). The earlier
   `why:` `repo:prototype/osfr-tools/src/derby_gateway.rs:1-6` (entry binding and the results hold); `repo:prototype/osfr-tools/src/gameplay.rs:2267-2271` (`derby_active()` routes inner records to `handle_derby`); `repo:prototype/osfr-tools/src/gameplay/npc.rs:585-595` (NPC menu calls `begin_derby`).

4. `old:` disconnect, and reward-once behavior.
   `new:` and disconnect abort. Reward-once behaviour is not tested in this file; it is covered by the gateway tests (`tests/derby_route.rs`, `tests/app_fuzz.rs`).
   `why:` `repo:prototype/osfr-tools/tests/derby.rs` has five `#[test]` fns (lines 185, 309, 350, 388, 450) and no reward or grant reference (grep for `reward|grant` is empty). `repo:prototype/osfr-tools/tests/derby_route.rs:1068` and `:1224` (`paid_matches`).

5. `old:` and one reward; contact damage/knockout/respawn;
   `new:` and one Close that retires the match; contact damage/knockout/respawn;
   `why:` `repo:prototype/osfr-tools/tests/derby.rs:309-310` (`solo_offer_... closes_once`; no reward assertion).

6. `old:` or gateway integration. (line 9-10 status sentence)
   Use the replacement in item 3, which covers the Status line. The Status claim that this is "not ... gateway integration" is false at the tip.

7. `old:` No gateway route, authenticated player-key adapter, status-bit-11 carrier, arena/catalogue
   `new:` Gateway route, player-key binding, status-bit-11 carrier, and outer teardown now exist in `derby_gateway.rs` and `gameplay/derby_session.rs` (`derby_gateway.rs:49,366`; `gameplay.rs:2267`; `gameplay/derby_session.rs:41`). Arena/catalogue
   (The following line, "content selection, or outer minigame teardown is implemented here.", should become "content selection is still open here.")
   `why:` `repo:prototype/osfr-tools/src/derby_gateway.rs:49` (`ACTIVE_STATUS_MASK` uses `DERBY_ACTIVE_STATUS_BIT`), `:366` (sets the status); `repo:prototype/osfr-tools/src/gameplay/derby_session.rs:41` (`retire_derby_for_reset`); `repo:prototype/osfr-tools/data/content/derby_entry.json` exists (cited in notes/Autopilot/T313.md:36).

8. `old:` `src/lib.rs` already declares `pub mod derby;`; no shared routing or gateway file was changed.
   `new:` `src/lib.rs` already declares `pub mod derby;` and `pub mod derby_gateway;`. The gateway layer is a separate module, not part of this candidate's file set.
   `why:` `repo:prototype/osfr-tools/src/lib.rs:16-17`.

9. `old:` Tests use smaller synthetic
   `new:` Tests use smaller synthetic health fixtures (`start_health: 20`) and a 1-second results hold; the reward fixture no longer exists in this file.
   `why:` `repo:prototype/osfr-tools/tests/derby.rs:26` (`start_health: 20`), `:43` (`results_duration_ms: 1_000`), with no reward field.

**Checked and current:** `derby.rs` and `tests/derby.rs` exist; `SUBTYPE_SPECS` has 20 entries (`derby.rs:54`; `tests/derby.rs:285`); `MAX_DERBY_DRIVERS` = 8 (`derby.rs:23`); defaults match the R list: 100 health, 1.0 damage per unit, 500 ms cooldown, 3.0 m pickup radius, +25 health/boost, 5 s effects, 2.0 multipliers, 4 s respawn, knockout points 2/3, loss 1, results 10 s (`derby.rs:703-736`); results sort by score, then damage difference, then key (`derby.rs:1611-1620`); the 10 s results hold moves to state 11 (`derby.rs:1655-1663`); the test count of 5 matches.

**Unsure:**
- The "Verification" pass count (5 passed) and the rustfmt result were not re-run. I only counted `#[test]` fns.
- Open gaps still says "reward amounts" and "job progression" are not source-established. Gateway content (`derby_entry.json`, per notes/Autopilot/T313.md:36 and :96) now carries 25 coins / 10 XP as "reviewed T219 fixture values". Whether that counts as source-backed is a judgement call; I did not change it.
- Build Ledger row 109 ("Built (registered, not routed)") is also out of date for derby, but that note is outside this file.
- I did not check the client-side table rows (subtypes 1-20) or the state-gate addresses.
