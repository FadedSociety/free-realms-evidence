<!-- fleet job=bug-hunt id=src-gameplay-profile-outfit-rs-L1 status=nothing_found turns=12 usd=0.0083 tokens(read,write,in,out)=[149647, 22394, 26, 7954] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay/profile_outfit.rs lines 1-45 of 45

## Window: `prototype/osfr-tools/src/gameplay/profile_outfit.rs` lines 1-45

No defect I can tie to a line and show is reachable from a client packet or a save.

What I checked:

- **`profile_switch_packet` (lines 11-17).** The layout is header `[35,0,7,0]`, a u64 GUID, the counted attachment bytes, and a trailing i32 of 0. The notes (`notes/Autopilot/F223.md:52-55`, `F131.md:69-70`) record the client reader `0x0091af50` as the same layout. The `guid` argument comes from the server-side `character.guid` at the callers, not from packet bytes. The `attachments` slice comes from `inventory.profile_attachments`, which emits a count prefix matching `0x009131c0`. No length arithmetic on client values.
- **`announce_profile_outfit` (lines 22-38).** Callers are `gameplay.rs:4385`, `gameplay.rs:5019`, `gameplay.rs:5366`, `jobs.rs:137`, `npc.rs:888` and `derby_session.rs:129`. The `switched` flag is passed from the staging result, and the "announce when switched or the outfit changed" rule matches the doc comment. The `?` on line 32 comes after the job switch has already been committed (`jobs.rs:182`, `*self = staged`). I looked for a reachable error there. `profile_attachments` can only fail on missing item or definition rows. `client_visible_state` (`inventory.rs:836-848`) filters equipment to ids present in the retained items, and `items.retain` keeps only defined definitions, so both `ok_or_else` branches (`inventory.rs:662`, `:667`) look unreachable from client input or a consistent save. I did not report it as a finding.
- **`public_wield_type` (lines 42-44).** The `profile` argument comes from the server's active profile (`gateway.rs:1053-1061`), not the packet. `equipped_wield_type` (`inventory.rs:632-645`) uses `find`/`and_then`/`map_or` with no indexing, and `wield_type.max(0)` matches its doc comment about clamping negatives.

Possible but unproven: `equipped_wield_type` takes the first slot-7 equipment row and requires `count > 0`. `profile_attachments` instead emits every non-zero equipment row. These could disagree if duplicate slot-7 rows exist in a save. I found no path that creates duplicates, so I dropped it.
