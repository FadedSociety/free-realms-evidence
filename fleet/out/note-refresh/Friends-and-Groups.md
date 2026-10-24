<!-- fleet job=note-refresh id=Friends-and-Groups status=done turns=22 usd=0.0250 tokens(read,write,in,out)=[856270, 69266, 46, 15576] model=claude-haiku-5-5 -->
# notes/Research/Friends and Groups.md

**Verdict:** minor drift. The core friend, ignore, and family-40 claims (result codes, 1 MiB cap, 128-byte name cap, `SocialService::new` minimum of 2, leader transfer and one-member dissolve, disconnect cleanup, 74/6 on accept, the 40/1 and 40/4 layouts, persistence through `replace_bytes`) match the tip. The group-invite expiry statement is false: the feature was added after this note was written.

**Corrections:**

1. `old:` No group-invite expiration timer is implemented here.
   `new:` Group invites expire lazily: `expire_group_invites` drops any invite older than its TTL before the next invite or response, with no timer and no notice. The TTL defaults to 60 s (`DEFAULT_GROUP_INVITE_TTL_MS`) and is host-configurable from 1 s to 600 s via `set_group_invite_ttl` (`--group-invite-ttl-ms`).
   `why:` repo:prototype/osfr-tools/src/social_lists.rs:36-38 (TTL constants), :368-379 (getter and setter), :726 and :825 (lazy expiry calls), :900-904 (`expire_group_invites`); repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:301, :325, :350, :3369.

2. `old:` Add a host-owned friend timeout and group-invite expiry policy before live service integration; only friend timeout has an API in this slice.
   `new:` Group-invite expiry is now a host setting (`--group-invite-ttl-ms`, `set_group_invite_ttl`). The friend timeout still has no production caller: `timeout_friend_request` is called only from tests, so the host timer remains unbuilt.
   `why:` repo:prototype/osfr-tools/src/social_lists.rs:373 (`set_group_invite_ttl`) and :614 (`timeout_friend_request`); repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:325, :350, :3369; the only other call is repo:prototype/osfr-tools/tests/social_lists.rs:172.

3. `old:` One unrelated existing dead-code warning remains in `src/housing.rs` (`Lot::instance_index`).
   `new:` The W23 build reported one unrelated dead-code warning in `src/housing.rs` (`Lot::instance_index`). At the tip, `instance_index` no longer appears in `housing.rs`, so this warning no longer applies.
   `why:` search of repo:prototype/osfr-tools/src/housing.rs finds no `instance_index`; `Lot` is defined at repo:prototype/osfr-tools/src/housing.rs:568.

**Unsure:**

- **Test count.** The note says `cargo test --test social_lists` gave "10 passed" (lines 154-161). This is a W23 run record. The file tests/social_lists.rs has 6 `#[test]` functions (lines 81, 154, 191, 216, 319, 372). Autopilot F115, F156 and F183 record "11 passed" for the same target. I did not run the tests, so I left the note's number alone.
- **"Lead integration steps" (lines 103-109).** Steps 1-4 now appear to be implemented in the gateway: profile load and register at repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:584-598; login at :661; disconnect at :807; request routing at :2147-2212; `chat_ignore_lists()` at :2258 and :2316; `persist_social_changes` at :1938 and :2724-2729. The section reads as pending work, but I did not change it because it is an instruction list, not a claim. The lead may want to mark it done.
- **Scope line 11** says chat routing stays separate work. The chat ignore feed is wired (see above), but I did not judge whether this slice's scope statement is still accurate.
- The client-side packet, opcode and reader claims (for example 26/14 sender `0093b9b0`, the 40/1 and 40/4 reader addresses) were not checked. They are outside the repo and need the native map.
