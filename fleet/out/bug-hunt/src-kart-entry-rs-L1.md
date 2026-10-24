<!-- fleet job=bug-hunt id=src-kart-entry-rs-L1 status=done turns=10 usd=0.0122 tokens(read,write,in,out)=[244437, 42482, 22, 8939] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/kart_entry.rs lines 1-752 of 752

Reviewed `prototype/osfr-tools/src/kart_entry.rs` lines 1-752 in full, plus the callers in `kart_gateway.rs` (`handle`, `handle_entry`, `race_ready`, `exit`) and `gateway.rs:1676`. I found one logic defect, and it is low severity.

- **[low] prototype/osfr-tools/src/kart_entry.rs:622-625 - `close()` overwrites `retired_session` with `None` when called with no entry open, so a second `close()` erases the retired-session marker that the doc comment at 620-621 promises to keep.**
  - Failure scenario: an entry for session S is open. `close()` runs, so `retired_session = Some(S)` and `phase = Closed`. A second `close()` runs with `context == None`. `self.context.take().map(..)` yields `None`, so `retired_session = None`. A late `33/9` or `33/2` for S then gets `own_session` → `NoOpenContext` (line 748) instead of the documented `StaleSession` (line 746).
  - Reach: no client input reaches this. `close()` has no caller in `kart_gateway.rs` (the only teardown is `exit()` at line 789, which sets `self.entry = None`), so the path is test-only today. The outcome is still a refusal either way. `handle_entry` (kart_gateway.rs:630-632) maps every `Refused` to an empty reply, so no state moves and nothing is granted. The same double-close behaviour is already logged as K4 in `notes/Reviews/Kart Entry Lead Review.md:100-104`.
  - Fix: `if let Some(context) = self.context.take() { self.retired_session = Some(context.session); }` and keep `self.phase = EntryPhase::Closed;`.

Checked and not defects:
- All payload slicing in `decode_register` and `decode_player_state` is preceded by an exact length check (`require_payload`), so there is no panic.
- `client_data[77..81]` and `[81..85]` are safe because `validate_content` pins `client_data.len() == 85`.
- `racer.slot as usize` is only reached after the `slot < 0` check.
- `value as usize > MAX_RACERS` is safe.
- Every refusal and every error path (`own_session`, the phase checks, `validate` inside `open`, `decode_*`) returns before any mutation. `open()` runs the scene encode before it sets `context`/`phase`.
- The gate is checked before decode.
- Malformed `33/x` frames returning `Err` (lead review K3) do not drop the connection. `gateway.rs:1676-1691` logs them as "rejected" and continues, unless the frame is combined, so I did not report it.
- The little-endian session value in the header doc (lines 9-11) is correct: `91ca73956acc524b` → `0x4b52cc6a9573ca91`.
