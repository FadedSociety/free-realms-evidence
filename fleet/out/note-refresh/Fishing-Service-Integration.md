<!-- fleet job=note-refresh id=Fishing-Service-Integration status=done turns=19 usd=0.0263 tokens(read,write,in,out)=[693992, 69393, 40, 21340] model=claude-haiku-5-5 -->
# notes/Research/Fishing Service Integration.md

**Verdict:** badly stale. The note describes the Oct 9 freeze. Later autopilot work (W160, F120, F153, F186, F210 and others) wired fishing into `lib.rs` and `Gameplay`, added rewards and a catch cap, and changed the bite, bobber and result paths. The fishing.rs codec, `Session::cancel`, `Session::server`, `AtCapacity` and `MAX_SESSIONS` = 4 still hold.

**Corrections:**

1. `old:` It does **not** register the service in
   `lib.rs`, route the gateway, drive the native client, or grant coins,
   experience, items or quest credit.
   `new:` Since this snapshot, `lib.rs` declares `pub mod fishing_service;`, `Gameplay` routes opcode 138 into the service, and catches pay coins, Fisherman XP, items and quest events (see the reward-path correction below).
   `why:` repo:prototype/osfr-tools/src/lib.rs:22; repo:prototype/osfr-tools/src/gameplay.rs:2286-2287, 2590-2600

2. `old:` - **No reward path.** No coin, experience, item, quest or save mutation exists
   in the service. The result body is presentation only.
   `new:` - **Reward path.** `settle_catch` selects the catch on the server, stages the grant (coins, one item, Fisherman XP) through `apply_grant`, and commits only if that succeeds. A bag-full or cap-blocked catch escapes with no payout. `Change` reports `paid` and `quest_events`. The result body is presentation only.
   `why:` repo:prototype/osfr-tools/src/fishing_service.rs:885-1010 (grant 972-992, escape on failure 995-1002, `CollectItem` quest event 1007); `Change` fields at :89-99

3. `old:` No packet is emitted for the bite because no recovered fishing packet
   carries it; the client's own hook presentation and any tension/distance
   stream are still unrecovered.
   `new:` The bite sends a sub 10 `UpdateBobber` (`update_fish`) and the hook a second one. A lost reel window sends an `update_fish` with both flags cleared, then a sub 14 result with `at_18: 0`. Tension/distance streams stay unrecovered.
   `why:` repo:prototype/osfr-tools/src/fishing_service.rs:847-861 (advance), :870-883 (escape), :1177-1182 (update_fish uses `Sub::UpdateBobber`); repo:prototype/osfr-tools/src/fishing.rs:121 (`UpdateBobber => 10`)

4. `old:` applied through `Session::server`, whose one-shot gate refuses a result that
   `new:` applied by `settle_catch` (`fishing_service.rs:885`), not through `Session::server`. The catch is one-shot because `attempt` is consumed (`:893`; `escape` takes it at `:871`). `Session::server` keeps the same one-shot gate for direct callers, and it refuses a result that
   `why:` repo:prototype/osfr-tools/src/fishing_service.rs (no `.server(` call; `attempt.take()` at :871); repo:prototype/osfr-tools/src/fishing.rs:741-757 (gate still present)

5. `old:` - `new()` / `with_config(FishingConfig)`; `FishingConfig { bite_delay_ms,
   reel_window_ms, test_fish_id, test_fish_name, anchor }` is clamped into the
   declared min/max window by `bounded()`.
   `new:` - `new()`. There is no `with_config`, `FishingConfig` or `bounded()`. Timings come from the `timing` block of `data/content/fishing.json` (bite 1500, nibble 900, reel window 7000).
   `why:` repo:prototype/osfr-tools/src/fishing_service.rs:165-171 (only `new`), :47 (`CONTENT_JSON`), :189-191; repo:prototype/osfr-tools/data/content/fishing.json:8-10

6. `old:` `Change { replies: Vec<Vec<u8>>, changed: bool }`; `set_anchor(Vec4)`,
   `new:` `Change { replies, quest_events, changed, paid, notices }`; `set_anchor(guid, Vec4) -> Result<(), Error>`,
   `why:` repo:prototype/osfr-tools/src/fishing_service.rs:89-99, :385; `reset(guid)` returns `bool` and `reset_all()` returns `usize` (:466, :471)

7. `old:` (`SNAPSHOT_POLICY = SnapshotPolicy::Ephemeral`): nothing is persisted, and a
   `new:` (there is no `SNAPSHOT_POLICY`; the round is held in `Gameplay` and released on reconnect, and `reset_all` runs there. The rolling-hour paid-catch ledger is restored from the gateway's character ledger on reconnect), and a
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:206, :1525-1527; repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:480, :1600-1602; repo:prototype/osfr-tools/src/fishing_service.rs:155-163 (`PaidCatches`, `#[derive(Clone)]` at :155 still holds)

8. `old:` bobber carries the caster's own handle and a server-side code of 0; the
   `new:` bobber carries the caster's own handle and a server-side `fish_key` derived from the GUID and cast sequence; the
   `why:` repo:prototype/osfr-tools/src/fishing_service.rs:779 (`fish_key`), :789 (`bobber_reply`), :1161-1163

9. `old:` `DEFAULT_REEL_WINDOW_MS` 10000 (bounded 500..60000)
   `new:` `reel_window_ms` 7000 from `data/content/fishing.json:10` (no clamp; the `DEFAULT_*` constants do not exist)
   `why:` repo:prototype/osfr-tools/data/content/fishing.json:10; repo:prototype/osfr-tools/src/fishing_service.rs (grep finds no `DEFAULT_` constants)

10. `old:` recovered, so no economy path was added.
    `new:` not all recovered, and the service now pays a server-selected catch (`settle_catch`, with an optional cap from `fishing_spots.json`). The economy question is open, not absent.
    `why:` repo:prototype/osfr-tools/src/fishing_service.rs:885-1010, :20-22 (payout and cap are operator content)

**Unsure:**
- The verification counts (`12 + 19 + 12 = 43`) are a historical log. The current `tests/fishing_service.rs` has several `#[test]` fns (lines 190, 240, 263, 281, and more). Autopilot reports F153/F186 say 8 and F287/T385 say 7, so I did not count them exactly.
- `CANDIDATE_PLAYER_CONFIG`, `CANDIDATE_ZONE_CONFIG`, `CANDIDATE_FISH_TYPE` and `CANDIDATE_RESULT_TYPE` are not in `src/` (grep finds none). I did not confirm where the registration values and fish entry now live, nor whether the fish id 418 survives in `fishing.json`.
- The file hashes in "Files and freeze hashes" were not checked. They are a frozen snapshot, so they are probably still accurate for that snapshot.
- Sub 15 handle-only, sub 18 unimplemented and the sub 3/4/11 wire widths were not re-checked against the client.
