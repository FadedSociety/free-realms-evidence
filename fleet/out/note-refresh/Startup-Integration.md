<!-- fleet job=note-refresh id=Startup-Integration status=done turns=19 usd=0.0186 tokens(read,write,in,out)=[565872, 55766, 40, 11881] model=claude-haiku-5-5 -->
# notes/Research/Startup Integration.md

**Verdict:** minor drift. The architecture, runtime and export claims hold at the tip. One verification line cites a test that does not exist.

**Corrections:**

- `old:` `- \`cargo test --test gateway startup_builders_use_typed_snapshot_and_keep_self_data_on_its_patch_path -- --exact\` — 1 passed.`
  `new:` `- \`cargo test --test gateway typed_startup_builder_serializes_session_position_and_preserves_tail -- --exact\` — the W19 run named a test that is no longer in the tree; this is the tip test that covers the same ground (typed index 07 self-data on its patch path, other indices via \`StartupSnapshot::build_packet\`).`
  `why:` No test named \`startup_builders_use_typed_snapshot_and_keep_self_data_on_its_patch_path\` exists anywhere in the repo (grep finds only this note). \`prototype/osfr-tools/tests/gateway.rs:155\` (\`typed_startup_builder_serializes_session_position_and_preserves_tail\`) builds index 7 via \`typed_selfdata::build_self\` and checks the other indices against \`startup.build_packet\` (lines 171-197). The "1 passed" result itself cannot be verified from the tip.

**Checked and holding (no change):**

- `src/lib.rs:89-93` and `:4-5, :77` register `startup_catalogues`, `startup_messages`, `startup_selfdata`, `startup_snapshot`, `startup_world`, `account`, `account_store`, and `rewards`.
- `src/gateway.rs:1900-1918`: login `0..8`, ready `8..46`; index 7 goes to `build_self_message`; all others go to `snapshot.build_packet`. Indices 10..=32 are dropped during opening gameplay (`gateway.rs:1905`), which matches the 23 AddNpc rows (`startup_snapshot.rs:323`, `:505`).
- `src/gateway.rs:311-385`: `load_reference` checks 46 templates for count, length and SHA-256. It returns only `templates[7]` as the self-data seed, and no captured bytes are replayed. No `TEMPLATE_FALLBACK` remains in `gateway.rs`, which matches D010.
- `src/gateway.rs:2029-2038`: `OSFR_GATEWAY_STARTUP_SNAPSHOT` override, with the default `lab_root/content/startup-snapshot/startup.json`.
- `src/startup_snapshot.rs:20-28`, `:83-98`: the snapshot has no name, GUID, inventory or chat fields (`CharacterSnapshot` holds only combat, HP/mana, journal and stat values). `:223-242` restricts export to the lab path. `:543-555` compares every index except 7 (45 messages) byte-for-byte with the capture.
- `tests/gateway.rs:98-128`: 8 login and 38 ready messages. `tests/startup_snapshot.rs:5` and `:19`, `tests/startup_messages.rs:33`, `tests/startup_world.rs:36`, `tests/startup_catalogues.rs:64`, `tests/gateway.rs:132`, and the `quest_engine.rs` test names all exist.
- Client addresses in the note (`00921a10`, `00944fe0`, `009471a0`, `0089b240`, `0090a630`, `00b90750`, `00b8f090`, `00a45bf0`, `00a45680`, `0089e8c0`, `008cebc0`, `0090e6a0`) all resolve to functions in the client DB.

**Unsure:**

- The `lab/content/startup-snapshot/startup.json` size (1,911,797 bytes) and the cargo pass/fail results cannot be checked from the tip. The lab directory is not present in this checkout.
- The `quest_engine` failure claim and the "no `quest_engine` source changed" claim cannot be checked from the tip (only the test names exist).
- The private target path under `lab/build/W19` is not checkable here.
