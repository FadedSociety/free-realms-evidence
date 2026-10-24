<!-- fleet job=guide-refresh id=Gameplay-Soccer status=done turns=18 usd=0.0232 tokens(read,write,in,out)=[616526, 70032, 38, 16465] model=claude-haiku-5-5 -->
# notes/Build Guides/Gameplay/Soccer.md

**Verdict:** current, with one minor count drift in the generated section. The prose, packet layouts, sub-id offsets, function addresses and status claims all match the tip.

**Corrections:**

- `old:` 206 accepted functions: 93 confirmed, 63 likely, 24 speculative, 26 unknown.
  `new:` 206 accepted functions: 92 confirmed, 64 likely, 24 speculative, 26 unknown.
  `why:` The `label` table (client_sql) for subsystems `minigame.soccer` + `ui.soccer` gives confirmed 83 + 9 = 92, likely 61 + 3 = 64, speculative 21 + 3 = 24, unknown 25 + 1 = 26, total 206, all `accepted`. The totals (190 and 16) in the note's header are right. Only the confirmed/likely split is off by one. Being a generated line, it may be overwritten on the next regeneration.

**Checked and holding (no change):**
- Sub-14 (62 B), sub-16 (20 B) and sub-13 (36 B) layouts and offsets match `soccer.rs:188-209` and the decoder at `soccer.rs:545-572`. Reads are little-endian and short reads are rejected (`soccer.rs:49-56`).
- A client `GoalMade` is refused (`soccer_match.rs:343`). Sub-13 from a client is refused (`soccer_match.rs:340`).
- `classify_state` is a candidate allowlist (`soccer_match.rs:272-279`).
- Charge is `aux / 255.0` (`soccer_service.rs:176-177`).
- Sender must equal the payload player and the sequence is the transport sequence (`soccer_service.rs:270-280`).
- Passes need a server-verified teammate (`soccer_service.rs:286-295`).
- `TEAM_SLOT_COUNT = 4` (`soccer_match.rs:40`). `HALF_SECONDS = 180.0` (`soccer.rs:19`).
- `fill_bots_for_solo` (`soccer_service.rs:607`). `mark_started` waits for all humans to reach Playing (`soccer_service.rs:726-748`).
- Tie counts as a loss (`soccer_service.rs:131`). Winner-only grant (`soccer_service.rs:770`).
- Leave or disconnect removes the roster entry, releases the ball and cancels when no sessions remain (`soccer_service.rs:777-812`).
- The 39/18, 39/47, 39/19 terminal sequence (`minigame.rs:745-746`). The stable run-derived win key (`minigame.rs:513`).
- Every Key-functions and mapped-function address name and confidence I spot-checked matches the `label` table. That covers 00b80ac0, 00b794b0, 00cdc5c0, 01072020, 01074b50 (unknown), 01072610, 00b793c0, 00b79580, 00b7be70, 00b7c070, 00b7de60, 00afb4a0, 00cde9b0, ControllerSoccer, SoccerBall, SoccerBallBase, SoccerPickup and SoccerPlayer rows. The per-class row counts in the mapped section (11, 11, 17, 3, 35) also match.

**Unsure:**
- Line 61 says "On halftime, require the explicit second-half transition." The authority does require an explicit `start_second_half` from `HalfTime` with `half == 1` (`soccer_match.rs:568-569`). But the gateway adapter's `tick` calls `service.second_half()` automatically when the phase is `HalfTime` (`soccer_entry.rs:470-476`, and its module doc at `soccer_entry.rs:16-17` says "auto-resume/second-half transitions"). Whether "require the explicit" is false depends on whether the rule means the authority or the gateway. I left it unchanged. The note may want to say the adapter auto-advances the second half on tick.
- The Build Ledger row (`notes/Design/Build Ledger.md:109`) says Soccer is "Built (registered, not routed)". The gateway does route family 76 (`gateway.rs:515-518`). The Soccer note makes no routed/not-routed claim, so I did not correct it here. Someone should reconcile the ledger row.
- The "Network-linked (`wire`): 0" header figure could not be checked; the label records do not expose a clean wire field.
