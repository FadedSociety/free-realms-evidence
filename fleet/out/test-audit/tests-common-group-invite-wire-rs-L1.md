<!-- fleet job=test-audit id=tests-common-group-invite-wire-rs-L1 status=nothing_found turns=5 usd=0.0030 tokens(read,write,in,out)=[22022, 9671, 12, 3120] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/common/group_invite_wire.rs lines 1-29 of 29

Reviewed `prototype/osfr-tools/tests/common/group_invite_wire.rs` lines 1-29. The window contains no test functions, only two helpers (`invitation_id`, `invite_generation`), so none of the five test-level categories applies directly.

What I checked:
- `invite_generation` reads `len - 24`, i.e. the dword before five trailing opaque dwords. This matches the encoder in `src/social_lists.rs:1579-1597` (`encode_group_invite`: 4-byte header, two guid/NameData pairs, echoed dword, then `[0u32; 5]`). The helper is not a self-referential computation: it reads the delivered bytes, and the server's own encoder is the independent source of the layout.
- `invitation_id` filters by recipient and the `[40,0,1,0]` header and panics via `expect` when nothing was delivered, so a missing invite fails loudly rather than passing silently.
- Callers in `tests/social_lists.rs`, `tests/group_invite_expiry.rs`, `tests/friend_positions.rs`, and `tests/shared_world_membership.rs` use these helpers to build the generation they echo back, and the server-side check is what those tests exercise. No `#[ignore]` or early-return skip is present in the window.

Minor observations, not reported as findings:
- The module doc says the client reads the dword at record offset `+0x120`, but the code uses a tail-relative offset (`len - 24`). The two agree only because the record has a fixed five-dword trailer; the in-function comment states this, so the doc is loosely accurate rather than an overclaim.
- The "wrapped vs bare" claim in the `invite_generation` doc relies on a tunnel header being prepended rather than appended. I did not verify that path in this window.

No finding meets the stated criteria for this window.
