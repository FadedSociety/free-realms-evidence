<!-- fleet job=note-refresh id=Housing-Fixture-Tail-Compatibility status=done turns=18 usd=0.0242 tokens(read,write,in,out)=[697320, 74664, 38, 15762] model=claude-haiku-5-5 -->
# notes/Research/Housing Fixture Tail Compatibility.md

**Verdict:** minor drift. The 94-byte tail decomposition and the native anchors still hold at the tip. One boundary sentence is stale because the `127/2` first dword has since been partly resolved.

**Corrections:**

- `old:` the earlier `127/2` first-dword identity and
  `127/53` extra-field blockers are unchanged.
  `new:` the `127/2` first dword is now documented as the client placement selection id (the inventory item guid the decorate bar passes to 127/1), not item identity; the `127/53` extra-field blocker is unchanged.
  `why:` repo:prototype/osfr-tools/src/housing_service.rs:9-12 (first dword is the client's placement selection id, bound via `00c0b710`/`00ac4200`); repo:prototype/osfr-tools/src/housing_native.rs:22-24 (`127/2` first_dword is the client selection id, `+0x40`); repo:notes/Reviews/Housing Placement Selection Identity Review.md:19-25 (selection echo 12/12, membership 8/8, selection id is not an item sub-field). The `127/53` trailing-bytes gap is still open at repo:prototype/osfr-tools/src/housing_native.rs:20-21.

**Checked and current (no change):**

- Tail codec: `FixtureUpdate::TAIL_BYTES_EMPTY = 94` (repo:prototype/osfr-tools/src/housing_native.rs:528). Order is instance, `FixtureInstanceInfo`, `FixtureDefinition`, count-prefixed guid list, three `u32` (lines 530-548). Empty-case widths are 28 (lines 396-410), 50 (lines 427-498) and 4+12 trailer, so 28+50+4+12 = 94. Test at repo:prototype/osfr-tools/tests/housing_native.rs:129-136 asserts 2+133+94.
- Native anchors, read from the client pseudocode table. `FUN_00ac2180` calls `2bc0`, `6f40`, `aafd30`, `abeb40`, `aafa90(+0x1c)`, then three `u32` (fn 00ac2180). `FUN_00aafd30` reads u64, u32, u32, then the `aafa90` array, then u32, u32 (fn 00aafd30). `FUN_00aafa90` is the count-prefixed guid array reader (fn 00aafa90). Line ranges in the note are within a few lines of the reviewer's machine-checked ranges.
- Our Housing guide (`notes/Build Guides/Gameplay/Housing.md:593`) already states the 50-byte empty-case definition, which agrees with the note.

**Unsure:**

- The lab-only claims (9/9 cursor, 9/9 oracle byte-identical, `64F9854A…` hash, `final-hashes.txt`) cannot be checked from the repo tip, since there is no `lab/` directory in the repo. An independent review (repo:notes/Reviews/Housing Fixture Tail Compatibility Review.md:12-19) reports the same 9/9 result, so I left them as is.
- Not a note claim, but noticed: the test name `update_empty_round_trip_is_227_bytes` (repo:prototype/osfr-tools/tests/housing_native.rs:130) asserts a 229-byte encoding (2+133+94). The note's "227" refers to the payload after the subtype, so the note is correct.
