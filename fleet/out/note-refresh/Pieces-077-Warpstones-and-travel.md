<!-- fleet job=note-refresh id=Pieces-077-Warpstones-and-travel status=done turns=11 usd=0.0135 tokens(read,write,in,out)=[242567, 43782, 24, 11287] model=claude-haiku-5-5 -->
# notes/Research/Pieces/077 Warpstones and travel.md

**Verdict:** moderate drift. The wire facts hold: the opcodes, the 8-frame capture table, the 6 captured destinations, the 4-byte request and the 34-byte `38/12` reply all match the code. The reconstructed-policy, integration and native-status sections are stale. The file path `prototype/osfr-tools/src/restoration/piece_077.rs` and the test and script paths all exist.

**Corrections:**

1. `old:` Attunement is modelled as a set the caller fills; the module does not invent
where the server learns it from.
`new:` Attunement is a set in `WarpRegistry`, and `WarpRegistry::visit` attunes a warpstone server-side when the character's own position is within `attune_radius_m` (default 12 m) of it. `on_location` calls `visit` after movement is accepted. This proximity rule is reconstruction; no attunement packet was recovered.
`why:` `repo:prototype/osfr-tools/src/restoration/piece_077.rs:1099-1131` (`visit`), `:860` (`attune_radius_m: 12.0`); `repo:prototype/osfr-tools/src/gameplay.rs:1812`.

2. `old:` Native acceptance has not been run. The lead should, in the shared client:
`new:` Native acceptance is partial. Run client-baseline-20261021T033319Z passed the Atlas list, 90 travel and the menu's 122. Still open: 58, the fight/knockout/cooking refusals, the client's automatic 122 after falling, and the confirmations below. The lead should, in the shared client:
`why:` `repo:notes/Design/Build Ledger.md:57`; `repo:notes/Autopilot/L039.md:33-36`.

3. `old:` Integration: register `restoration::piece_077` in `lib.rs`, route the tunneled op-90 request through `WarpRegistry`, and source the destination table from the recovered `57` catalogue once one is captured or exported.
`new:` Integration: the module is included from `gameplay.rs` (`#[path]`, not `lib.rs`), and `Gameplay::handle_warp` routes 56, 90, 122 and 58 through `WarpRegistry`. The destination table is still the curated `CURATED` set, not the recovered `57` catalogue, so that part of the gap stands.
`why:` `repo:prototype/osfr-tools/src/gameplay.rs:59-61` (`mod piece_077`), `:2321` and `:3559-3573` (`handle_warp`); `repo:prototype/osfr-tools/src/restoration/piece_077.rs:682` (`CURATED`); `repo:prototype/osfr-tools/src/lib.rs` has no piece_077 registration.

4. `old:` `WarpRegistry` in `piece_077.rs` refuses, without emitting a reply or moving the
`new:` `WarpRegistry` in `piece_077.rs` refuses without moving the character or changing state, and the refusal produces a system chat notice (for unknown, locked and non-warpstone ids: "You have not attuned to that warpstone yet.") but no `57` or `38` reply. The refusal list is:
`why:` `repo:prototype/osfr-tools/src/restoration/piece_077.rs:992-998` (`WarpReply::refused` sets notices only), `:960-966` (notice text); `repo:prototype/osfr-tools/src/gameplay.rs:3598` (notices sent as chat).

5. `old:` * a request body that is not exactly four bytes (`MalformedRequest`),
`new:` * a request body that is not exactly four bytes (`MalformedRequest`); the gate also refuses `WrongZone`, `Blocked` (knocked out, encounter, busy), `Cooldown` (5 s zone teleport, 300 s stuck cooldown for `122`), `SelfTarget` and `TargetUnavailable` (friend teleport, `58`, which the server currently refuses because no friend view is wired),
`why:` `repo:prototype/osfr-tools/src/restoration/piece_077.rs:943-954` (`WarpRejection`), `:860-862` (cooldowns); `repo:prototype/osfr-tools/src/gameplay.rs:3559-3572` (`friend: &|_| None`).

   The list in the note is incomplete rather than false. Replace the four-bullet list with the expanded list above, or keep the four bullets and add the remaining kinds.

**Unsure:**

- "How the server learns a character attuned a warpstone is unknown" (Gaps section). The code now uses a proximity reconstruction (see correction 1). The original mechanism is still unrecovered, so the sentence is probably still true as stated, but the note should cross-reference `visit`.
- Community comparator and capture paths under `lab/` (`lab/decompiled/server`, `lab/references/...`, `lab/captures/...`, `lab/reports/...`) are not in the repo, so I could not check them. The `pseudocode.c` function addresses (`FUN_00b97a20`, `FUN_00b97ad0`, `FUN_00c1a5e0`, `FUN_00b97b80`, `FUN_00bf7a50`, `FUN_0089dd60`, `FUN_00b97c40`, `FUN_00b991d0`, `FUN_00b98b70`) all resolve in the client database.
- The claim that "the shipped client already hides unattuned warpstones" was not checked.
- The captured-frame offsets and sha256 pins were not checked against the capture files, which are outside the repo.
