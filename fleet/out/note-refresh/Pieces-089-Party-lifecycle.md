<!-- fleet job=note-refresh id=Pieces-089-Party-lifecycle status=done turns=13 usd=0.0162 tokens(read,write,in,out)=[335852, 47108, 28, 13850] model=claude-haiku-5-5 -->
# notes/Research/Pieces/089 Party lifecycle.md

**Verdict:** badly stale on the integration and gap claims. The module-level claims about `piece_089.rs`, its tests and its registration status are current. The note says family 40 has no body codec and no gateway wiring, but the live gateway already routes and decodes family-40 group traffic (the T020 group routing, F115 and F139 work).

**Current (verified):** `src/restoration/piece_089.rs` exists with `GROUP_FAMILY = 40`, `GROUP_SUBOPCODE_COUNT = 15`, `parse_family_header`, and `PartyRegistry`. `tests/piece_089.rs` has 15 test functions (`^fn` count, including `envelope`). `src/lib.rs` does not register a `restoration` module, so the "not registered in `lib.rs`" claim holds.

**Corrections:**

1. `old:` Message *bodies* remain unrecovered, so the module parses headers only and writes no group payload. (wraps across lines 9–10)
   `new:` Message *bodies* remain unrecovered for this module, which parses headers only and writes no group payload. The live gateway already decodes some family-40 bodies (40/1, 40/3, 4, 6 requests) and routes them through `SocialService`.
   `why:` `repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:2899-2933` (request decoders `(40, 1)`, `(40, 3)`, `(40, 4)`, `(40, 6)` with client-reader comments); `repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:2195-2206` (routing to `invite_to_group`, `leave_group`, `respond_group_invite`, `kick_from_group`); `repo:notes/Design/Build Ledger.md:44` (groups listed as Wired in `social_lists.rs`).

2. `old:` Wiring the registry to the gateway needs a body codec that does not exist yet; (wraps across lines 111–112)
   `new:` The gateway already has body codecs for the group requests (see the family-40 decoders); the `PartyRegistry` is a separate, unwired model, and its membership state does not feed the live group state in `SocialService`.
   `why:` `repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:2899-2933`; `repo:prototype/osfr-tools/src/social_lists.rs:327-357` (`SocialService` with `max_group_members` and group state); `repo:prototype/osfr-tools/src/restoration/piece_089.rs:257` (`PartyRegistry`, not referenced from `src/`).

3. `old:` the per-field body of every group message is opaque. (wraps across lines 83–84)
   `new:` the per-field body is opaque in `piece_089.rs`, but the gateway decodes the 40/1, 40/3, 40/4 and 40/6 request bodies and encodes the 40/2 and 40/5 results from the recovered client readers.
   `why:` `repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:2899-2933`; `repo:prototype/osfr-tools/src/social_lists.rs:718-760` (`invite_to_group`, result codes 2/1 through 2/7).

4. `old:` any member may invite, an open invite
   `new:` the live server lets only the leader invite (the `PartyRegistry` policy is still "any member may invite", which is RECONSTRUCTED and unwired)
   `why:` `repo:prototype/osfr-tools/src/social_lists.rs:757-761` (non-leader invite returns result 2/5); `repo:prototype/osfr-tools/src/restoration/piece_089.rs:301-311` (`PartyRegistry::invite` allows any member).

**Unsure:**
- The note says "The original server's invite timeout ... rules are unrecovered." That is still true of the original rule, but the gateway now uses a reconstructed 60 s TTL (`DEFAULT_GROUP_INVITE_TTL_MS = 60_000`, `repo:prototype/osfr-tools/src/social_lists.rs:36`). I did not change the line; the lead may want to add the reconstructed TTL beside it.
- I did not verify the client line numbers (`pseudocode.c:976825`, etc.), the Python checker counts (`tests/pieces/test_piece_089.py`, 8 tests), or the `lab/reports/` artifacts. They were outside the tip-code checks I could make within budget.
- Whether `tests/piece_089.rs` run still passes at the tip was not run.
