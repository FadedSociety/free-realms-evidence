<!-- fleet job=bug-hunt id=src-social-lists-rs-L801 status=done turns=11 usd=0.0167 tokens(read,write,in,out)=[273843, 46801, 24, 16222] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/social_lists.rs lines 801-1600 of 1726

Reviewed `social_lists.rs` lines 801-1600 in full. One finding; the rest of the window checked out (details below).

**[medium] prototype/osfr-tools/src/social_lists.rs:1141-1145 - `remove_group_member` drops every pending invitation to the group on any leave or kick, although the group survives when two or more members remain.**

- **Failure scenario:** Group G has members A (leader), B and C, and the group has room (default cap 4). A invites D, so `group_invites[D] = {group G}`. C runs `leave_group` (or A kicks C). `remove_group_member(C, _)` runs `group_invites.retain(... && invite.group_id != group_id)`. That removes D's invitation even though G still exists with members [A, B]. D's pop-up is now dead. If D accepts, `respond_group_invite` returns 40/5 result 3 ("not invited") instead of joining. A gets no notice, and A's reserved slot in the `members + open` check (line 784) is silently released. Only a dissolving group should lose its invitations.
- **Reach:** Client 40/3 (leave) → `gateway osfr-gateway.rs:2200` → `leave_group` (line 907) → `remove_group_member(member, false)` (line 1125). The same path runs for kick (`kick_from_group`, line 926, reached from `osfr-gateway.rs:2205`) and for disconnect (line 935). None of these callers filters the invite list first, so the bad removal happens for any member of a 3+ member group.
- **Why the test suite does not catch it:** `tests/social_lists.rs` (`group_invite_accept_capacity_kick_leader_leave_and_disband`, lines 289-306) checks membership after `leave_group(101)`, but never has a pending invite open during that leave. The `piece_089.rs:249` test name ("last member leave disbands and drops open invites") ties invite removal to disbanding, not to ordinary leaves.
- **Fix:** Drop the invitations for this group only when the group is dissolved. In `remove_group_member`, move the `invite.group_id != group_id` clause into the dissolve branches (the `group.members.len() == 1` branch at line 1157, and the `group.members.is_empty()` branch at line 1168). Keep the `target != member_guid` and `inviter_guid != member_guid` clauses at line 1141 as they are.

**Checked and not defects:**
- `parse_location_request` (1482-1498): length is matched before `bytes[4]`, and `word`/`int` use `get`, so no out-of-bounds access. Coordinates are checked by `coord_ok`, which handles `i32::MIN` without panicking.
- `encode_friend_positions` (1424): the count is capped at `MAX_POSITION_ENTRIES` (512). `friend_positions` (968-1008) stops at the same cap and only emits coordinates that pass `on_map`, so the encoder's `InvalidPosition` error cannot be reached from a client.
- `group_map_ping` (1041): coordinates are validated, and the sender comes from the session, not from the packet.
- `remove_group_member` `self.profiles[&...]` indexing (lines 1147, 1149, 1164): profiles are only inserted by `register` and never removed, and every guid that can enter a group has a registered profile (checked at lines 736 and 843). No panic is reachable.
- `respond_group_invite` (818-896): the `expect` at line 880 follows a `get` at line 838 with nothing in between. The fallible `?` calls after the mutations at lines 884-888 need an invalid stored name or a zero guid, and both are rejected by `register` and `validate`.
- Line 1186 (`group.leader_guid != member_guid`) is always true when it is reached, so it only adds a redundant leader update. Not a defect.
