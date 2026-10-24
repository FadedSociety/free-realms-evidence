<!-- fleet job=bug-hunt id=src-restoration-piece-037-rs-L1 status=nothing_found turns=5 usd=0.0039 tokens(read,write,in,out)=[33495, 17116, 12, 2832] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_037.rs lines 1-287 of 287

Reviewed `prototype/osfr-tools/src/restoration/piece_037.rs` lines 1-287 in full. I found no defect that meets the criteria, so I am not reporting a finding.

What I checked:
- **Panics / indexing (criterion 1):** `first_aid_heal` (l.215-218) uses `usize::from(rank).checked_sub(1)?` and `.get(index)`, so rank 0 and 6+ return `None` without panicking. No other slicing, unwrap, or arithmetic on client values is present in the window.
- **Overflow / resource growth (criteria 1-2):** `ReviveOffer::choices` (l.251-264) builds a fixed-size `Vec` of at most two entries. `paid_revive_enabled` (l.268-270) is a plain `>=` on `u32`, with no arithmetic that can overflow.
- **Trusting the client (criterion 4):** the functions take already-decoded enums and integers. They are not packet readers. `ReviveOffer` cost and timer are documented as server-supplied (l.220-221).
- **Logic vs. doc comments (criterion 5):** `paid_revive_enabled` matches its doc (`wallet >= cost` is the negation of `wallet < cost`). `target_allowed` matches the module doc: Heal needs a friendly, living target; Damage needs an opponent and has no knocked-out restriction, which is the documented open gap; Revive needs a non-self friendly, knocked-out target. `revive_event` maps Countdown to Respawn, PaidRevive(true) and SafeRevive(false), which matches the doc at l.273-274. `can_use_ability` checks knock-out before energy, as its doc describes.
- **Reach:** I searched the repo for callers. The only references outside this file are `tests/piece_037.rs` (a `#[path]` include) and the work-item notes. The notes state the module is not yet registered in `src/restoration/` or `lib.rs`. No server handler, packet decoder, or save path calls any function in this window, so no client input can reach it today.

One design note, not a defect: `can_use_ability` and `target_allowed` are independent. Any future caller must run both to enforce the knocked-out-caster rule for heals and revives. The notes list the target-matrix policy as needing independent review, so this should be checked when the module is wired in.
