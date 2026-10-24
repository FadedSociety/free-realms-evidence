<!-- fleet job=note-refresh id=Soccer-Restoration status=done turns=12 usd=0.0159 tokens(read,write,in,out)=[283135, 46958, 26, 14483] model=claude-haiku-5-5 -->
# notes/Research/Soccer Restoration.md

**Verdict:** badly stale on integration status. The protocol, envelope, file-path and interface claims still hold (`soccer.rs`, `tests/soccer.rs`, `tests/soccer_review.rs`, `gateway.rs::tunnel`, `CLIENT_PACKET_IDS`, `Match` methods, `Evidence::Missing` reward table all exist at the cited places). The note still describes the slice as unwired and the reducer as the authoritative path, and both are no longer true.

**Corrections:**

1. `old:` no shared gateway/lib wiring. Root integration and
   `new:` gateway and lib wiring are live through the native service (`lib.rs:81-84`, `gameplay.rs:3325`), while `Match` itself is not routed. Root integration and
   `why:` `prototype/osfr-tools/src/lib.rs:81-84` exports `soccer`, `soccer_entry`, `soccer_match`, `soccer_service`; `gameplay.rs:2248` calls `handle_soccer`, which at `gameplay.rs:3325-3330` sends family-76 client packets to `SoccerService::handle_client`. `gateway.rs:518` and `:1837` also name and gate on soccer.

2. `old:` - `Match`: message-driven state with an explicit `Direction`. Only
   `new:` - `Match` (a legacy candidate reducer, not the authoritative path, which is `soccer_match.rs` plus `soccer_service.rs`): message-driven state with an explicit `Direction`. Only
   `why:` `src/soccer.rs:746-748` labels `Match` "Legacy message-driven reducer for candidate server outputs ... not the authoritative service path"; `src/soccer_service.rs:1-5` names `soccer_match` as "server-owned authority".

3. `old:` wire `Match` into the gateway from the root integration path,
   `new:` `Match` is not on the gateway path (the gateway calls `SoccerService::handle_client`, `gameplay.rs:3325`), so this step is replaced by a direction-gate check on that service path, from the root integration path,
   `why:` grep finds no `Match::handle` or `Direction::` use outside `src/soccer.rs`; `gameplay.rs:3325-3330` is the live call.

4. `old:` The gateway integration must pass server traffic as `ServerToClient` and client traffic as `ClientToServer`; the reducer
   `new:` No gateway code passes a `Direction` today: the live path is `SoccerService::handle_client` (`gameplay.rs:3325`), and nothing outside `soccer.rs` calls `Match::handle`. The reducer
   `why:` `src/soccer.rs:835-837` (`handle(direction, ...)`); `src/gameplay.rs:3325-3330`.

5. `old:` proposal is a record shape with `Evidence::Missing` amounts;
   `new:` proposal is a record shape (`reward_table: Evidence::Missing`); the native service has its own reconstructed reward path through `RewardState` (`soccer_service.rs:46`), so the reward is no longer only a proposal;
   `why:` `src/soccer.rs:1066` keeps `reward_table: Evidence::Missing`; `src/soccer_service.rs:46` imports `RewardGrant, RewardState`; `notes/Autopilot/F226.md` and `F205.md` describe the payout applied once per run. The `Missing` part is accurate; "amounts" is not a field of `RewardProposal`.

**Unsure:**

- `soccer_service.rs:33-35` says the service "sends no packet and touches no shared gateway, content or save file". That header is stale against `gameplay.rs:3325` and the rewards/minigame imports, but I did not change any claim based on it.
- `notes/Design/Build Ledger.md:109` says "Soccer ... Built (registered, not routed)". That conflicts with the gateway routing above. I did not edit the ledger, only flagged it.
- Lab-only figures (2978 records, sha256 values, the `lab/reports/...` logs, the 21/21 verifier count) sit outside the `repo` root, so I could not check them.
- Test counts (`11 passed`, `10 passed`) were not re-run. `tests/soccer.rs` has 11 `#[test]` plus one `#[ignore]` (line 529), which is consistent with the note.
- The `Team.as` and client-UI field claims are client-side and I did not check them.
