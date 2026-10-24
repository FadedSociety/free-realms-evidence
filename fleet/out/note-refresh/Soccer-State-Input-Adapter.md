<!-- fleet job=note-refresh id=Soccer-State-Input-Adapter status=done turns=10 usd=0.0096 tokens(read,write,in,out)=[137892, 31151, 22, 8605] model=claude-haiku-5-5 -->
# notes/Research/Soccer State Input Adapter.md

**Verdict:** minor drift. The adapter logic, policy validation, state ranges, authority path and refusals all match the tip. The one materially false claim is the "not registered in the production crate" statement, because the same logic now ships in a registered production module. The pinned `soccer_match.rs` hash is also no longer the tip value.

**Corrections:**

1. `old:` It is **not** registered in the production crate (`prototype/osfr-tools/src/lib.rs` is unchanged)
   `new:` The lab candidate itself is not registered, but its logic was copied into the production module `prototype/osfr-tools/src/soccer_service.rs` (`AdapterPolicy`, `charge_from_aux`, `state_request_intent`, `apply_state_request`). That module is registered at `lib.rs:84` (`pub mod soccer_service;`), via the W30 module registration.
   `why:` repo:prototype/osfr-tools/src/lib.rs:84; repo:prototype/osfr-tools/src/soccer_service.rs:140-298 (the copied adapter, marked "Copied from the frozen private adapter"); repo:notes/Research/Module Registration 2026-10-13.md:8,12 (`soccer_service` registered); repo:notes/Research/Soccer Service Integration.md:3-12 (the lab adapter is still frozen at `11d291c2…`).

2. `old:` `33f642e2…`, `soccer.rs` `c68bb857…`.
   `new:` `33f642e2…` (the adapter-receipt pin; the tip `soccer_match.rs` is `eb73cc17…` after the additive `Authority::unregister`), `soccer.rs` `c68bb857…`.
   `why:` repo:notes/Research/Soccer Service Integration.md:20 (`eb73cc17…` after, `33f642e2…` before); repo:prototype/osfr-tools/src/soccer_match.rs:549 (`pub fn unregister`). I did not hash the file myself.

**Checked and holding:**
- `classify_state` ranges (kick 16-26/31-34, pass 27-30): `soccer_match.rs:273-279`.
- `charge_from_aux = aux / 255`, `power = charge * max_power`, and the kick/pass target rules: `soccer_service.rs:176-253`.
- `AdapterPolicy` validation (`max_power` and `min_direction_norm` finite and positive, `charge_floor` in `0..=1`): `soccer_service.rs:143-172`.
- `sender != payload player` and stale-sequence checks run before the authority is touched: `soccer_service.rs:262-298`.
- `Authority::register` and `Authority::apply` exist: `soccer_match.rs:505`, `:594`. The `(0, max_kick_power]` bound is at `soccer_match.rs:690`.
- Server-only refusals: GoalMade (2) and ImpulseBall (13) are refused in `client_packet` at `soccer_match.rs:340-343`. UpdateSoccerBall (4) falls through to the unsupported-packet refusal at `:344`.
- `word` is advisory and the gateway sequence is the only sequence: `soccer_match.rs:252-254`, `:298-299`.
- Cross-link targets exist under `notes/Reviews/` and `notes/Research/`.

**Unsure:**
- The lab paths (`lab/reports/soccer-state-adapter-20261009T174320Z/`, including `src/adapter.rs`, `tests/state_adapter.rs`, the logs and `receipt.json`) are not in the repo tree, so the RED/GREEN counts (14 passed), the "thirteen lead tests" and the source hashes could not be checked directly. The review note `notes/Reviews/Soccer State Input Adapter Review.md:5,9` is consistent with them, including the Scale100/aux10 pass and aux255 refusal.
- Whether the production registration of `soccer_service` (lib.rs:84) counts as "registering the candidate". I treated it as registration of the copied logic, not of the lab crate.
