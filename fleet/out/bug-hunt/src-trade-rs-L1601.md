<!-- fleet job=bug-hunt id=src-trade-rs-L1601 status=nothing_found turns=7 usd=0.0049 tokens(read,write,in,out)=[70446, 19706, 16, 3379] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/trade.rs lines 1601-1624 of 1624

Window `repo:prototype/osfr-tools/src/trade.rs` 1601-1624 (`write_name`, `write_string`, `packet`) reviewed. No defect I can tie to a line.

What I checked:
- **Panics:** this is outbound packet encoding only. Nothing is parsed from client bytes here. `write_string` converts `value.len()` with `i32::try_from` and returns `WireRange` rather than panicking. `[0u32; 3]` and the `to_le_bytes` calls cannot fail.
- **Unbounded growth:** the only input is a `SocialName` (`social_lists.rs:46`), a server-held name. Its length is bounded by the name data the server stores, and the function neither grows nor loops on a client count.
- **Atomicity:** the three callers (`invite_packet` 1457, `start_packet` 1470, `rejected_packet` 1483) build a local `out` buffer and return `Result`. A failure mid-write discards the buffer, so no shared state is mutated.
- **Trusting the client:** the name written is server state, not a packet field, so there is no client authority to check.
- **Logic:** writing zeroes for the three leading i32 words matches the explicit `(R)` note in the code and the note at `notes/Build Guides/Gameplay/Trade.md:120-128`, which says the meaning is unknown. The Legacy `NameData.cs` names them FirstNameId, LastNamePrefixId and LastNameSuffixId. Zeroing them is a possible display-fidelity question, not a demonstrable defect. The chat path (`social_chat.rs:329`) writes stored `fields` instead, but that does not make this one wrong on its own, and I could not show a client-visible failure from the zeroes.

Nothing reportable.
