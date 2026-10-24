<!-- fleet job=note-refresh id=Pieces-095-Multi-character-persistence status=done turns=13 usd=0.0193 tokens(read,write,in,out)=[404333, 59105, 28, 15740] model=claude-haiku-5-5 -->
# notes/Research/Pieces/095 Multi-character persistence.md

**Verdict:** Substantially stale. The piece_095 module, its 10 tests, the `#[path]` include and the unregistered module are current. The save format and the login/wire status are contradicted by the tip.

**Corrections:**

1. `old:` * `prototype/osfr-tools/src/character_store.rs` stores one version-1 document
   `new:` * `prototype/osfr-tools/src/character_store.rs` stores one schema-2 document per file (`{"schema_version":2,"character":{...}}`; version-1 files are still read)
   `why:` repo:prototype/osfr-tools/src/character_store.rs:17 (`SCHEMA_VERSION = 2`), :50-56 (`schema_version` / `version` fields), :77-78 (reads `(Some(2), None)` or `(None, Some(1))`), :93-98 (`save` writes `schema_version: Some(SCHEMA_VERSION)`, `version: None`).

2. `old:` so the legacy bytes cannot drift from what the single-character build wrote.
   `new:` so the legacy reader stays the real one. The shared writer now emits schema 2, so the bytes no longer match what the single-character build wrote.
   `why:` repo:prototype/osfr-tools/src/character_store.rs:93-98; repo:prototype/osfr-tools/src/restoration/piece_095.rs:62-64, :84-87.

3. `old:` * `rollback_to_legacy` writes the canonical version-1 document with the real
   `new:` * `rollback_to_legacy` writes the canonical single-character document (through the real writer, so schema 2 today, not version 1) with the real
   `why:` repo:prototype/osfr-tools/src/restoration/piece_095.rs:364-365 and :383 (`save_legacy` → `character_store::save`); repo:prototype/osfr-tools/src/character_store.rs:93-98.

4. `old:` answers selection with
   `selection_reply(identity: Option<&CharacterIdentity>)`, i.e. status 1 and at
   most one entity row.
   `new:` answers the opcode-11 request from the account store (`character_list_reply`), listing every character the account owns. `selection_reply(identity: Option<&CharacterIdentity>)` now only builds one row's appearance payload.
   `why:` repo:prototype/osfr-tools/src/login.rs:207-261 (`authenticate_account` loads `AccountStore`), :274-294 (`character_list_reply`), :333-336 (opcode 11); repo:prototype/osfr-tools/src/account.rs:304-335 (`character_list` iterates `character_guids`, calls `selection_reply` per row at :324); repo:prototype/osfr-tools/src/login.rs:643.

5. `old:` * Login/wire: `identity.rs` and `login.rs` still load and answer a single identity;
   `new:` * Login/wire: `login.rs` authenticates against `AccountStore` and lists the account's characters; `identity.rs` remains the legacy import source and the account-1 mirror;
   `why:` repo:prototype/osfr-tools/src/login.rs:217-242 (legacy migration path), :360-362 (`identity::save` only for account 1 / guid 1), :274-294.

6. `old:` `selection_reply` still emits at most one entity, so no second character can be
   `new:` `selection_reply` builds one row payload per entity, and `character_list` calls it once per owned character, so a second character can be
   `why:` repo:prototype/osfr-tools/src/account.rs:315-335; repo:prototype/osfr-tools/src/login.rs:643-656. Native selection of a second character is still unproven (see the Native acceptance gate).

7. `old:` list is the wire shape the login service must adopt.
   `new:` list is the wire shape the login service now emits (opcode 12 with a per-character entity list).
   `why:` repo:prototype/osfr-tools/src/login.rs:277-292.

**Unsure:**
- Account slot bound: the server now enforces a local slot limit, `--max-characters` (default 6, `bin/osfr-login.rs:68`), through `SlotPolicy` (`account.rs:29-31`, `:110`; `account_store.rs:328`). The note's statement that the server value is unrecovered is still true. The note just does not mention the local enforcement point.
- Pinned SHA256 values for `piece_095.rs`, `tests/piece_095.rs`, the checker and the test script, and the Lua/locale/community hashes: I could not compute hashes with these tools, so I did not check them.
- Test count: `tests/piece_095.rs` has 10 `#[test]` functions (lines 101-316), matching "ten tests". Pass counts in the logs are not checked.
- `game_store.rs` and the gateway still bind one state file per character: plausible (`README.md:63`), but not traced in full.
- Integration gate: `src/lib.rs` has no `restoration` module, so the "lead registers the module" gate still holds.
- Original-facts line citations for `ScriptsBase.lua` (3103-3110 for the column list was not re-read) and the `CharacterSelect` functions (16187-16202, 16204-16209, 16211-16234) match the tip.
</result>
