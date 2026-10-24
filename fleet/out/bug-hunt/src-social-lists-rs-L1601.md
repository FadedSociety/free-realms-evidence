<!-- fleet job=bug-hunt id=src-social-lists-rs-L1601 status=nothing_found turns=7 usd=0.0062 tokens(read,write,in,out)=[59910, 20958, 16, 5889] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/social_lists.rs lines 1601-1726 of 1726

Window `prototype/osfr-tools/src/social_lists.rs` 1601-1726 reviewed in full. No defect I could tie to a line and show reachable from client input or a save.

What I checked:

- `encode_group_accept_notice` (1602-1613): the `len < 24` guard makes `len - 20` and `data[4..tail_start]` safe. Its only caller is `respond_group_invite` (social_lists.rs:870, 885), which passes a server-built 40/1 body from `encode_group_invite`, so no client bytes reach it. The doc comment matches the code.
- `encode_group_result`, `encode_group_leave`, `encode_group_kick` (1616-1636): fixed-size writes, no client-sized allocation, and `write_social_name` validates names.
- Test `group_invite_and_notice_bytes_match_the_client_reader_layout` (1652-1689): the byte offsets agree with the layout built by `encode_group_invite` (1579-1597) and `write_social_name` (1217-1228). Total 114 bytes for 40/1 and 115 for 40/4 both check out.
- Test `full_group_accept_refusal_keeps_the_pending_invite` (1692-1725): traced through `respond_group_invite` (818-896). With max=2 and two members, the accept hits the full-group check at line 862 and returns code 5/2 (`[40,0,5,0,2,0,0,0]`) before `group_invites.remove` at 868. The invite, group membership and roster are unchanged, so the assertions hold.

Non-findings examined in the callee path (outside the window): in the accepted path, the mutations at 878-883 come before `group_member_record(...)?` and `encode_group_snapshot(...)?`. Both can only fail on a missing profile, and the profile is already checked at 843-852, so no partial-commit error is reachable. `expire_group_invites` runs before a possible `MissingProfile` return, but it is idempotent cleanup, not a broken save.
