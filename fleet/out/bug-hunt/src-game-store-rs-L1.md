<!-- fleet job=bug-hunt id=src-game-store-rs-L1 status=nothing_found turns=13 usd=0.0101 tokens(read,write,in,out)=[210762, 29087, 28, 8690] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/game_store.rs lines 1-184 of 184

No defects found in `prototype/osfr-tools/src/game_store.rs` lines 1-184 that I could tie to a client-reachable input, a save, or a caller.

What I checked:

- **Panics / indexing:** `read_document` caps the read at `MAX_SNAPSHOT_BYTES + 1` and rejects anything over 1 MiB before parsing. The parse uses `serde_json::from_slice` with `map_err`, not `unwrap`. No slicing or arithmetic on client values exists in the window. `(MAX_SNAPSHOT_BYTES + 1) as u64` is safe.
- **Unbounded growth:** the 1 MiB bound applies on read (176 area, `read_document`) and on write (`write_document`, line 180). The two bounds agree, so a file the server wrote can always be read back.
- **Atomicity:** `save_document` validates the character (line 80) and reads the existing envelope before any write, so a failed read leaves the file untouched. `save_with_pets` (line 74) lands the character and pet roster as one `replace_bytes` call. `save_housing_state` and `save_pets_state` mutate only a local copy before `write_document`, so an early `?` error leaves disk unchanged. `replace_bytes` (character_store.rs:106-140) writes a temp file, fsyncs it, then renames.
- **Round-trip consistency:** the writer always emits `schema_version` in {5, 6, 7} with `version` omitted, which `read_document`'s match accepts. `character.validate()` runs on both write and read.
- **Trusting the client:** `load_housing_state` and `load_pets_state` deserialize server-owned envelope fields only. No packet value reaches this module. The pet-roster client input is validated in `pets.rs` (`validate_roster`), outside this window.
- **Logic against doc comments:** the schema selection at lines 88-94 and 118-124 and the preservation of character, gameplay, pets and housing in the helper functions match their doc comments.

Things I considered and dropped:

- `save()` with `gameplay: None` would drop existing gameplay (line 97). The only caller that passes `None` is `gateway.rs:1346`, reached when `Gateway.gameplay` is `None`. `osfr-gateway.rs:942-943` refuses to start if the disk file has a gameplay snapshot without `--content`, so this cannot wipe gameplay in the current flow.
- A full bag near the 1 MiB bound: `notes/Reviews/Economy Independent Review.md:47-49` measures 650,482 bytes at `MAX_ITEMS`, so the bound is not reached today.
- Schema 3/4 or v1/v2 files carrying extra `pets`/`housing` fields are accepted. Nothing in the server writes such files, so this is harmless.
