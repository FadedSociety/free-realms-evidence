<!-- fleet job=bug-hunt id=src-bin-osfr-gateway-t006-guild-routing-rs-L1 status=nothing_found turns=5 usd=0.0029 tokens(read,write,in,out)=[40463, 13429, 12, 1617] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bin/osfr_gateway/t006_guild_routing.rs lines 1-525 of 525

## Window reviewed: `prototype/osfr-tools/src/bin/osfr_gateway/t006_guild_routing.rs` lines 1-525

**No findings.** The whole window is test code and is excluded by the brief.

- The file is included only from `prototype/osfr-tools/src/bin/osfr-gateway.rs:4669-4671`, which is gated by `#[cfg(test)]` and `#[path = "osfr_gateway/t006_guild_routing.rs"] mod t006_guild_routing;`.
- Every function in the window is either a `#[test]` or a helper used only by those tests (`rig`, `eligible_rig`, `route`, `wrap`, `log_in`, `dispatch`, `dispatch_result`, `create`, `motd`, `invite`, `one_guid`, `family_sub`, `has`, `chat_with_guild`, `seed_*`, `identity`, `session`, `options`).
- The helpers' unchecked slicing and indexing (for example `family_sub` at lines 287-293 and `chat_with_guild` at lines 516-524) and the `unwrap`s are test-only and cannot be reached from a client packet or a save. Under the brief, these are not defects.

I did not trace the production code these tests exercise (`Session::route_application`, `dispatch_message`, `GuildStore`), because it is outside this window and the brief asks for review of the window only. Any real guild-routing defect would have to be reported against those production files in their own windows.
