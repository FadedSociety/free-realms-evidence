<!-- fleet job=bug-verify id=src-social-chat-rs-L1-f1 status=done turns=7 usd=0.0071 tokens(read,write,in,out)=[81543, 23446, 16, 6758] model=claude-haiku-5-5 -->
# medium: `prototype/osfr-tools/src/social_chat.rs:743-766`

**Verdict:** confirmed (the mechanism is real; the fix suggestion needs one correction, see below)

**Severity if confirmed:** medium. This is a sustained CPU stall of the single gateway loop. It does not crash the server, corrupt a save, or grant items or coins.

**Evidence (each link checked):**

1. **Module tree.** `src/lib.rs:85` has `pub mod social_chat;`, and `social_chat.rs` is the real file. `SpamGate` is used by the shipped binary (`bin/osfr-gateway.rs:23`, field at `:448`, constructed at `:1087`). This is not test-only code.
2. **Route from the wire.** `osfr-gateway.rs:2138-2139`: `inner.starts_with(&[15, 0, 1, 0])` calls `route_typed_chat`. That reads `parse_client_chat` (`:2242`), then `chat_permissions.authorize_free_text` and `spam_gate.allow` (`:2246-2254`), then `resolve_recipients`.
3. **Upstream caps don't limit the work.** `social_chat.rs:295-300`: `Reader::string(max)` rejects `len > max`, and `decode_packet_chat` calls it with `MAX_MESSAGE_BYTES` = 2048 (`:364`, `:21`). `authorize_free_text_with_filter` (`:629`) allows up to 2048 bytes and the default `PermissiveTextFilter` (`:646-649`) allows everything. So a 2048-char message reaches `SpamGate::allow`.
4. **Timing gate.** `CHAT_SPEED_ANY_MS = 330`, `CHAT_SPEED_MAX_MS = 30_000`, `MAX_SPAM_ENTRIES = 256` (`social_chat.rs:24-29`). Distinct messages are never rejected by the similarity branch. At 1 message per 330 ms, retention holds about 91 lines. `allow` (`:713-717`) then runs `similar_text` against every one of them. `edit_distance` (`:753-766`) is a full O(n·m) DP with no early exit. The `similar_text` length-difference check the reviewer proposed does not fire for equal-length messages.
5. **Budget does not stop it.** `ActionBudgets` (5/s refill, burst 10; `social_chat.rs:24-29` area, charged at `osfr-gateway.rs:1585`) is charged before the spam gate. An attacker at about 3 accepted messages/s stays under the 5/s refill. The byte and packet budgets (`osfr-gateway.rs:2947-2948`: 200/400 packets, 256 KiB/1 MiB) also allow about 3 × 2 KB/s easily.
6. **Single loop.** `osfr-gateway.rs:3668-3680` `step()` handles up to 64 packets per tick synchronously. The only `thread::spawn` in `src/bin` is in `osfr-bot.rs` and tests, so the gateway processes all sessions in one thread. A slow chat handler delays every other player's packets.

**Cost estimate.** 91 comparisons × 2048 × 2048 ≈ 3.8·10⁸ DP cells per accepted message. At about 1–3 ns per cell in release, that is roughly 0.4–1.1 s per message, at about 3 messages/s per account. This is close to the reviewer's figure. Even at the low end, one account would take a large share of the loop. Several accounts would multiply it.

**Caveats:**
- The attacker needs an authenticated account. The attack is not anonymous.
- The reviewer's exact timings are estimates; I did not benchmark them.

**Corrected fix (the proposed fix is partly wrong):**
- The length-difference early exit is correct (if `|len(a) − len(b)| > 0.2 × max(len)`, the distance exceeds the threshold, so return false). It does not help the equal-length attack, as the reviewer notes.
- The "compare only the first 256 chars" option changes semantics and is not needed.
- A better option that keeps the exact semantics is a banded edit distance with band `k = floor(CHAT_SPEED_SIMILARITY × scale)` (about 409 for 2048 chars). It returns the same yes/no answer as the current `d / scale <= 0.2` check, with about O(n·k) work per pair, about 5× cheaper at full length. Pair it with the length-difference exit. Mind the f32 comparison when computing `k`, so that the boundary matches `<=`. Add a test that compares the banded result against the full DP on random pairs.
- Alternatively, cache a hash or length per retained line and skip the DP for lines that cannot be similar, or cap the number of similarity comparisons per message.
