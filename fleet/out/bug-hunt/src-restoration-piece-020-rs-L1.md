<!-- fleet job=bug-hunt id=src-restoration-piece-020-rs-L1 status=done turns=8 usd=0.0126 tokens(read,write,in,out)=[157793, 45817, 18, 10580] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_020.rs lines 1-800 of 875

Window reviewed: `prototype/osfr-tools/src/restoration/piece_020.rs` lines 1-800 (plus helpers 800-875 for `group`, `group_mut`, `index_of`).

No panics, unchecked indexing, or unbounded growth reachable from wire bytes were found. `parse_family_header` (225-266) checks the length before every index, and `body` is a copy bounded by the input. `launch` (611-658) mutates `next_instance_id`, the group phase, and `instances` only after every fallible check has passed. `disconnect` (683-750) keeps its `expect`s safe, because the group is not removed between the `get` and the `get_mut`.

**[low] prototype/osfr-tools/src/restoration/piece_020.rs:464 - `invite` lets a not-yet-accepted (`Invited`) member act as an inviter, which contradicts the module's own state and error docs.**

- Failure scenario: the owner invites B (`invite` pushes B as `MemberState::Invited`, lines 475-478). B has not accepted. B calls `invite(activity, B, C)`. Line 461 passes (phase is Forming). Line 464 `index_of(group, B).is_none()` is false, because B is in `members`, so the check passes. Line 467 finds C absent. Line 472 has capacity room. C is pushed as `Invited` and `InviteSent` is returned. A player the owner never invited is now in the owner's launch group, and the owner's launch is blocked until C answers.
- Contradiction: `MemberState::Invited` is documented as "Invited, not yet accepted" (275). `GroupError::NotAccepted` is documented as "the member exists but has not accepted the invitation yet" (378-379). `set_ready` enforces this at line 538, but `invite` does not. The policy summary (406) says "any member may invite", and "member" in this module means an accepted or ready member.
- Reach: no server path. `ActivityGroupRegistry` is referenced only from `src/restoration/piece_020.rs`, `tests/piece_020.rs`, and `tests/piece_099.rs` (`piece_099` pulls the file in through `#[path]`). The module is not registered in `lib.rs`. So the impact is latent until the module is wired to the family-175 dispatcher. Once wired, the `actor` value comes from the client's sender id, and no upstream check stops a pending invitee from inviting.
- Impact: bounded to one group and capped by capacity. The owner can kick the extra member, and nothing is granted (the module grants no rewards). Severity is low.
- Fix: at line 464, require `index_of(group, actor).map(|i| group.members[i].state)` to be `Accepted` or `Ready`, and return `GroupError::NotAccepted` otherwise (the same pattern `set_ready` uses at line 538).

Items I checked and dropped: the `launch` `checked_add` error precedence (`InstanceSpaceExhausted` is reported before `UnknownActivity`) and the unreachable `i32::MAX` id are cosmetic. Players can be in several forming groups at once, but the `disconnect` doc ("every group and instance they belong to") suggests that is intended.
