<!-- fleet job=bug-hunt id=src-guilds-rs-L1601 status=nothing_found turns=13 usd=0.0202 tokens(read,write,in,out)=[358865, 58221, 28, 18668] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/guilds.rs lines 1601-2261 of 2261

Window `prototype/osfr-tools/src/guilds.rs` 1601-2261 read in full (plus callers and helpers it depends on: `GuildStore` promote/demote/kick/accept_invite/expire_invites/same_guild_ranks/set_motd/login/logout, `GuildService::handle_decoded`/`responds_to`, the gateway caller `t006_guilds.rs`). No defect I could tie to a line and show reachable from a client packet or save.

Candidates checked and dropped:

- **`decode_request` (1951-2045), `Reader` (2210-2261):** `take` uses `checked_add` and bounds-checks; `string()` rejects negative and >4096-byte lengths before the cast; sub 15 caps the count at 4096 before `Vec::with_capacity`; `finish()` rejects trailing bytes. No panic or unbounded allocation found.
- **`member_target` (1735-1747) / `manage` (1749-1783):** the target is only a candidate. `same_guild_ranks` (916-945) verifies both actor and target belong to the same guild before any `unwrap()` on `members.get_mut`. Snapshots are taken before mutation where needed for removed or demoted names.
- **Rank notices (1872-1885, 1886-1907):** `rank < previous` means promotion, since Leader=1 (lowest value). Status 4 = promoted and 5 = demoted, which matches the notes (`notes/Build Guides/Gameplay/Social (Friends, Guilds, Chat).md:118`, `notes/Autopilot/T006.md:85`).
- **`InviteAccept` (1543-1573):** the snapshot is taken after `accept_invite`, so the new member's name resolves. `dirty` is set only when `joined`. A timed-out or ignored accept returns Ok without a join, and the `joined` check then only causes a harmless extra roster push.
- **`Motd` (1604-1622) / `set_motd` (775-798):** text is capped at 1024 bytes, control characters are rejected, and only Leader/Officer may write. The mutation happens after all checks.
- **`login` / `logout` (1656-1711):** `unwrap_or_default` on `store.login` is unreachable as an error, since `guild_guid_for` was already `Some`. Presence is runtime-only and not persisted, so there is no atomicity issue.
- **`normalize_guild_name` (2136-2155):** the length and character checks are consistent with the stated rule. The trailing `previous_space` check is dead code, not a defect.
- **Early returns that skip `expire_invites` (1525-1527, 1605-1607):** the cleanup is only a memory bound. Every insertion path reaches the end-of-request cleanup, so this does not grow the map beyond the request rate.

Out-of-window observations that may be worth another reviewer's attention (not claimed as findings): the 129/3 Invite path (1450-1493) passes a client-supplied `second_guid` straight to `store.invite` as the target. Whether that is bounded depends on `store.invite` (outside my window, around line 300-415), which I did not read.
