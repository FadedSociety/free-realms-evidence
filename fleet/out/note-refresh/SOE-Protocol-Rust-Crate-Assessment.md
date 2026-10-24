<!-- fleet job=note-refresh id=SOE-Protocol-Rust-Crate-Assessment status=done turns=9 usd=0.0058 tokens(read,write,in,out)=[87078, 20177, 20, 4891] model=claude-haiku-5-5 -->
# notes/Research/SOE Protocol Rust Crate Assessment.md

**Verdict:** minor drift. One checkable claim about our gateway is false at the tip; the rest of the note's claims about our own code hold.

**Corrections:**

- `old:` Currentgateway runtime owns a single `Option<Session>`.
  `new:` The gateway runtime holds many sessions at once: `sessions: SessionMap`, where `SessionMap = BTreeMap<SessionKey, Session>` and `SessionKey` is peer `SocketAddr` plus `connection_id`.
  `why:` `repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:409-415` (SessionKey, SessionMap), `:2961` (`sessions: SessionMap` field), `:3390` (`sessions: BTreeMap::new()`), and inserts at `:3548`, `:3652`, `:4384`. The login executable is also multi-session: `repo:prototype/osfr-tools/src/bin/osfr-login.rs:826` is `HashMap<SocketAddr, Session>`. The `Option<Session>` change the Multi Login Design note proposes is therefore already done for login, and the gateway never used a single `Option`.

**Checked and holding:**

- `src/soe.rs` and `src/soe_send.rs` exist (`repo:prototype/osfr-tools/src/lib.rs:87-88`). `soe.rs` has CRC, zlib (miniz_oxide), ordering and fragment errors (`soe.rs:12-60`). `soe_send.rs` has `ReliableSender` with fragmentation, window, ACK and retry (`soe_send.rs:81-306`).
- CRC3 on native captures: the reviews `notes/Reviews/Native Mining134930.md:28` and `notes/Reviews/Mining Native 151307 Final Review.md:20` both record CRC length 3.
- The note's statements about the published crate (version, checksum, test counts, go-back-N behaviour, MIT vs GPL-3.0 licence) describe the external crate, not our tree. I did not check them.

**Unsure:**

- The note's sentence "login/gateway executables supply session/runtime handling" is vague but not false.
- Outside this note: `notes/Design/Security Model.md:40` says "One `Option<Session>` exists for the whole service" for the login handshake. The code at `osfr-login.rs:826` now uses a `HashMap<SocketAddr, Session>`, so that line looks stale too. I did not edit it because it is not in this note's scope.
