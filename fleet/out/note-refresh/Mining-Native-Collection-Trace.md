<!-- fleet job=note-refresh id=Mining-Native-Collection-Trace status=done turns=17 usd=0.0142 tokens(read,write,in,out)=[296249, 36362, 36, 13296] model=claude-haiku-5-5 -->
# notes/Research/Mining Native Collection Trace.md

**Verdict:** minor drift. The core claim holds: `+500` and `collected+1` at unchanged chain count can only come from `collect_fall`, reached from `OnLevelEventMsg 50`. But the "chain ACK never collects" wording is now over-broad, and nearly every `src/mining.rs` line citation has moved (the file is now 2434 lines).

**Corrections:**

1. old: `the chain ACK path never collects.`
   new: `the chain ACK path never credits the 600-value ore goal (it advances only selectable-valued goals, via `collect_chain_goals`, without score).`
   why: repo:prototype/osfr-tools/src/mining.rs:751-757 (chain arm calls `collect_chain_goals`), 1622-1652 (`collected` +1 per matching goal, no score); the 600 ore never matches a 400-block chain value (1619-1621 comment).

2. old: `COLLECTABLE_SCORE = 500` and `collected+1` exist only in `collect_fall`
   new: `COLLECTABLE_SCORE = 500` exists only in `collect_fall`; `collected+1` also occurs in `collect_chain_goals` (selectable goals, no score)
   why: repo:prototype/osfr-tools/src/mining.rs:117, 1594, 1610 (score only in `collect_fall`); 1638 (`collected` +1 in `collect_chain_goals`).

3. old: `(`src/mining.rs` 1249-1311), reachable only from `OnLevelEventMsg 50``
   new: `(`src/mining.rs` 1554-1614), reachable only from `OnLevelEventMsg 50``
   why: repo:prototype/osfr-tools/src/mining.rs:1554 (`fn collect_fall`), 1614 (end); sole call site 833.

4. old: `(658-668). Full save table:`
   new: `(830-844). Full save table:`
   why: repo:prototype/osfr-tools/src/mining.rs:830-844 (`["OnLevelEventMsg", "50", x, y]` arm).

5. old: `The chain arm (574-626) sends chain score/time-bonus/gravity/rebuild only.`
   new: `The chain arm (694-775) sends chain score/time-bonus, collects selectable-valued goals (`collect_chain_goals`, 751-757, no score), then gravity and settle/rebuild.`
   why: repo:prototype/osfr-tools/src/mining.rs:694 (`["OnChainMsg", list]`), 727-750 (score, time bonus), 751-757 (`collect_chain_goals`), 758-773 (gravity, settle).

6. old: `our `initialize_board(..., reshuffle=true)` at `src/mining.rs` 616-624, 1070-1081`
   new: `our `initialize_board(..., reshuffle=true)` at `src/mining.rs` 1678 (`settle_after_collect`) and 1810 (powerup action path)`
   why: repo:prototype/osfr-tools/src/mining.rs:1678, 1810 (both `initialize_board(..., true, ...)`); `OnLevelEventMsg\t11\t1` reshuffle message at 1333. Lines 616-624 are now the `OnLevelEventMsg 50`/`OnLevelEventMsg 51` and quit handling area, and 1070-1081 is not a reshuffle site.

7. old: `(`Type8Engine::cancel` 404-405)`
   new: `(`Type8Engine::cancel` 517-531)`
   why: repo:prototype/osfr-tools/src/mining.rs:517-531 (`pub fn cancel`); 404-410 is now `seed_random_queue`.

8. old: `(`cancel` 404-405; native close/cancel likewise)`
   new: `(`cancel` 517-531; native close/cancel likewise)`
   why: repo:prototype/osfr-tools/src/mining.rs:517-531.

9. old: `(`gravity`, `src/mining.rs` 1198-1247 pulls queue`
   new: `(`gravity`, `src/mining.rs` 1502-1551 pulls queue`
   why: repo:prototype/osfr-tools/src/mining.rs:1502 (`fn gravity`), ends ~1550.

10. old: `refills (1231-1243)`
    new: `refills (1536-1548)`
    why: repo:prototype/osfr-tools/src/mining.rs:1536-1548 (refill batch in `gravity`, `random_tile(run, spec, true, ...)` at 1539).

11. old: `reshuffle 616-624 / 1070-1081)`
    new: `reshuffle 1678 / 1810)`
    why: repo:prototype/osfr-tools/src/mining.rs:1678 (`settle_after_collect`), 1810 (powerup action). Same drift as item 6.

12. Not a text fix: the pending-fall, Harvest and Native Dead Board notes cite the same `collect_fall` range (1249-1311) and the `OnLevelEventMsg 50` arm (658-671). Those notes need the same update.

**Unsure:**
- The save-table values (lines 146-152: chains, score, collected, wall_ms, board ores incl. (8,10,601)) are in `lab/` run artifacts that I could not read. Not checked.
- Route 39 mapping (`["OnLevelEventMsg","50",x,y]` → `collect_fall`): the arm exists at mining.rs:830, and the gateway routing of `39/*` to Type8 is in `notes/Design/Security Model.md:59`. I did not trace the gateway dispatch itself.
- Original-client citations (`core/ServerGrid.as` 321-335, `Tile.as`, `Grid.as`, `GameClientNetwork.as`) live in the decompiled client or refs, not in our code. I did not verify them.
- Pending-fall note (`notes/Research/Mining Pending Fall Reshuffle.md`) exists, but I did not read its contents.
