<!-- fleet job=bug-hunt id=src-restoration-piece-020-rs-L801 status=nothing_found turns=6 usd=0.0032 tokens(read,write,in,out)=[36825, 13571, 14, 2322] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_020.rs lines 801-875 of 875

Window `prototype/osfr-tools/src/restoration/piece_020.rs` lines 801-875 reviewed in full, with supporting reads at lines 295-330, 405-430, 640-800.

Functions in the window:
- `instance_activity` (801-805): a `BTreeMap::get` plus a copy of `roster.activity_id`. It has no panic, arithmetic or allocation risk. Its only callers are in tests or nowhere; the repo-wide search found no production caller, so no client packet can reach it.
- `state` (808-855): builds a JSON snapshot. `groups` and `instances` are `BTreeMap`s (declared at 412-413), so the "stable" claim in the doc comment at 807 holds. The `GroupPhase` and `MemberState` matches are exhaustive. Nothing indexes or unwraps on client data. The snapshot is read-only.
- `group` / `group_mut` (857-867): thin `ok_or` lookups with no mutation before an error.
- `index_of` (870-875): `position` over members, no indexing.

No defect in this window reaches the categories (panic on client input, unbounded growth, broken atomicity, trusting client, logic error). I am not reporting anything.
