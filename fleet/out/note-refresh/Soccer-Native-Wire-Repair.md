<!-- fleet job=note-refresh id=Soccer-Native-Wire-Repair status=done turns=13 usd=0.0175 tokens(read,write,in,out)=[335216, 45794, 28, 16785] model=claude-haiku-5-5 -->
# notes/Research/Soccer Native Wire Repair.md

**Verdict:** minor drift. The wire layouts, reader addresses, test-file paths and the sub-13 refusal all hold at the tip. Three statements are false: a struct field name that does not exist, the wrong refusal message, and a stale "unregistered" limit. The test-count claims also need a check (see Unsure).

**Corrections:**

1. `old:` `` `StateRequest { player, sequence, state, aux, unknown_word, action, vectors }` ``
   `new:` `` `StateRequest { player, sequence, state, aux, state_counter, action, action_direction, steering_vector, position_vector }` ``
   `why:` repo:prototype/osfr-tools/src/soccer_match.rs:256-270 (the struct has `state_counter`, `action_direction`, `steering_vector`, `position_vector`; there is no `unknown_word` or `vectors` field). The same identifier is also `state_counter` at repo:prototype/osfr-tools/src/soccer.rs:197 and in tests/soccer_native_wire.rs:92.

2. `old:` `the verbatim `unknown_word` and the three vectors, and`
   `new:` `the verbatim `state_counter` and the three vectors, and`
   `why:` repo:prototype/osfr-tools/src/soccer.rs:193-199 (`UpdatePlayerState { state_counter: u32, vectors: [[f32; 4]; 3] }`). `unknown_word` appears nowhere in the soccer code (grep of prototype/osfr-tools finds it only in housing_*.rs).

3. `old:` `the `player+0xB0` word is `unknown_word` documented as unverified meaning (not a`
   `new:` `the `player+0xB0` word is `state_counter`, documented as a state-change counter (not a`
   `why:` repo:prototype/osfr-tools/src/soccer_match.rs:261-262 (doc: "Incremented on client state changes (`player+0xB0`); not a replay clock") and repo:prototype/osfr-tools/src/soccer.rs:189-191.

4. `old:` `explicit`
   `new:` `explicit` (no change to this word; the replacement is in the next entry)

   Correction for the sentence that wraps across lines 47-49. Replace the fragment
   `old:` `adapter-gap error - the gateway must supply the authoritative facing; the`
   `new:` `error that the kick/pass still needs the configured charge policy and a server-verified pass target; the`
   `why:` repo:prototype/osfr-tools/src/soccer_match.rs:355-357 returns "soccer kick/pass state needs configured charge policy and a server-verified pass target". No "adapter gap" or "facing" text exists in the module. tests/soccer_native_wire.rs:103-106 asserts exactly those two phrases. The service, not the gateway, derives the emitted direction: repo:prototype/osfr-tools/src/soccer_service.rs:935-956 (probe clone, then `unit(probe.ball_velocity())`).

5. `old:` `still unregistered (no `lib.rs`/gateway integration), so no native world entry`
   `new:` `exported from `lib.rs` (lines 81, 83) and consumed by `soccer_service.rs:930`; gateway wiring is lead-owned, so the native world entry`
   `why:` repo:prototype/osfr-tools/src/lib.rs:81 and :83 (`pub mod soccer;`, `pub mod soccer_match;`); repo:prototype/osfr-tools/src/soccer_service.rs:930 (`match client_packet(bytes, sequence)?`). This also makes the note's own cleanup checkpoint ("lib.rs now exports both modules") consistent with the Limits section, which still said the opposite.

**Unsure:**

- **soccer_match test count.** The note says `cargo test --test soccer_match | 27 passed` and the cleanup row says "56 passed, 0 failed, 1 ignored". At the tip, `tests/soccer_match.rs` contains 20 `#[test]` functions (lines 184-776). I could not run cargo, so I cannot say whether any test was removed after the 27 count. Other notes (`Autopilot/F226.md:195`, `Autopilot/T393.md:79`, `Research/Login Integration.md:64`) still say 27. If the 20 count holds, the cleanup total is 11 + 20 + 10 + 8 = 49 passed plus 1 ignored, not 56.
- **Native reader addresses.** The reader addresses `FUN_00b794b0` (sub 14), `FUN_00b793c0` (sub 16) and `FUN_00b79580` (sub 13) exist in the client DB with the expected shape. I did not verify the constructor arguments `0xe/0x10/0xd`, the field offsets, or the private `lab/reports/...` bundles, which are not in the repo.
- **Corpus pins.** The gate in `tests/soccer.rs:533-580` pins 2917 frames and the per-sub counts the note lists. I did not run the ignored gate, so the "2917/2917 byte-exact" result is unverified.
- **Comment-only and hash claims** (file hashes, "hex-literal scan is empty", "comment-only diff") are not checkable from the tip.
- **Other notes that copy the same wording.** `notes/Research/Multiplayer Routing.md:36` quotes a test name `sub14_kick_state_becomes_a_typed_request_with_an_explicit_adapter_gap`, but the test at the tip is `sub14_kick_state_refuses_context_free_intent_conversion`. That note is not the one I was asked to check; the mismatch is for its owner.
