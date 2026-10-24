<!-- fleet job=test-audit id=tests-guilds-rs-L1 status=done turns=5 usd=0.0056 tokens(read,write,in,out)=[38364, 19489, 12, 5460] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/guilds.rs lines 1-379 of 379

Window: `prototype/osfr-tools/tests/guilds.rs` lines 1-379. I read the whole window plus `guilds.rs` (invite, accept_invite, decode_request) and `social_chat.rs` (resolve_recipients, Guild arm). No `#[ignore]` or early-return skips in this window. The lifecycle, kick/rank, invite-expiry, persistence, and error-reply tests all assert on real state or outputs that the code under test computes independently, so they are not findings.

- **[medium] tests/guilds.rs:313 all_supported_client_guild_request_bodies_decode - most decode checks only assert `is_ok()` or `matches!` on the outer enum, so a wrong variant or wrong field mapping still passes.**
  - Why it cannot catch a regression: at lines 336, 341, 347, 354, 361 and 366, `assert!(decode_request(..).is_ok())` passes for any `Ok` variant. Swapping sub 4 to `Demote` (`decode_request` line 1982 in `guilds.rs`), or mapping sub 8 to `InviteDecline` instead of `InviteAccept`, leaves these green. Field order or GUID values are never compared. Only sub 1 and sub 3 are checked by variant, and only with `matches!`.
  - Fix: compare full values, e.g. `assert_eq!(decode_request(&pair).unwrap(), GuildRequest::Promote { first_guid: 1, second_guid: 2 })` per sub, and for sub 13 assert `non_china == 0` and the strings. Also check the `Create` and `Invite` fields.

- **[medium] tests/guilds.rs:157 leader_departure_transfers_to_highest_rank_then_lowest_guid - the data cannot tell "highest rank" apart from "lowest guid", and the departure path is not what is asserted.**
  - Why it cannot catch a regression: both candidates, 2 and 3, end as `Officer` (lines 159-162). An implementation that ignores rank and picks the lowest GUID still makes 2 the leader, and the test passes. The rank-ordering claim in the name is never exercised. The final assertion at lines 174-180 checks the notice from `transfer_leadership(2, 3)`, a separate call that is not part of the departure.
  - Fix: give 2 `Member` and 3 `Officer` (only one promote on 2, two on 3), then `leave(1)` and assert 3 is `Leader`. A lowest-GUID implementation would pick 2 and fail. Assert the departure's own notices (or the leader state) instead of the `transfer_leadership` notice, or rename the test to match what it checks.

- **[medium] tests/guilds.rs:297 client_request_reader_uses_family_129_and_string_lengths - the name promises string-length coverage, but the only string is empty.**
  - Why it cannot catch a regression: the body uses `0i32` (line 302), so the length prefix is zero and no bytes follow. A reader that uses the wrong width or byte order for the length, for example a u16 prefix, reads the same 0 here. The test also never checks that the reader consumes exactly the frame, so trailing-byte bugs also pass.
  - Fix: use a non-empty string such as `"Guild-B"` with the i32 prefix, assert `text == "Guild-B"`, and add a case where the declared length is wrong and expect `Err`.

- **[low] tests/guilds.rs:225 duplicate_guild_name_is_rejected_case_insensitively - `assert_eq!(create_guild(...), Ok(1))` pins the first guild GUID to an allocation detail.**
  - Why it is churn: the test is about name collision. Any change to GUID allocation (starting at 0, using a counter that seeds differently, and so on) fails it without any behavioural regression.
  - Fix: capture the returned GUID with `let first = ....unwrap();` and compare against `first`, or only assert `is_ok()` for the first create.
