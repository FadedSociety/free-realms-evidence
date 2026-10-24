<!-- fleet job=note-refresh id=Startup-World-Content status=done turns=20 usd=0.0192 tokens(read,write,in,out)=[628096, 55407, 42, 11943] model=claude-haiku-5-5 -->
# notes/Research/Startup World Content.md

**Verdict:** minor drift. Most code claims hold at the tip: the six builder/parser pairs, the 9-dword quick-chat row, the 13-dword POI row, the 7/10/3/9 journal tables, the welcome and MOTD layouts, the 6-passed/1-ignored test split, and the native reader addresses (all present in the client DB). One claim is plainly false, and one count is an undercount.

**Corrections:**

1. `old:` The module is not registered in the shared library/gateway, and no native client was launched.
   `new:` The module is registered in the shared library (`src/lib.rs:93`, `pub mod startup_world;`) and the gateway startup path builds from its typed values; no native client was launched.
   `why:` `repo:prototype/osfr-tools/src/lib.rs:93` registers `pub mod startup_world;`. `repo:notes/Research/Startup Integration.md:3,7` records that W19 registers it and the gateway builds startup indices from typed values. Other modules already import it (`src/world.rs:9`, `src/startup_snapshot.rs:7`).

2. `old:` scalar fields and flags, two float4 values, lists, counted strings, and trailing scalar/string fields
   `new:` scalar fields and flags, four float4 values (position, rotation, tilt, and one trailing vector), lists, counted strings, and trailing scalar/string fields
   `why:` `repo:prototype/osfr-tools/src/startup_world.rs:880-881` (position, rotation), `:932` (tilt), `:948` (`unknown_vector_54`) each read a float4 in the AddNpc parser, so the note's "two" undercounts the reader's shape.

**Unsure:**

- Verification item 2 cites a dead-code warning in `src/housing.rs::Lot::instance_index`. `Lot` exists at `repo:prototype/osfr-tools/src/housing.rs:568`, but no `instance_index` symbol exists anywhere in `src/housing.rs` at the tip. This is a historical run's output, so I did not rewrite it. A reader should not look for that symbol.
- Private-capture counts (2,470 quick-chat rows, 149 POIs, 23 NPCs, 4/10/58/16 journal rows, 16 and 188 MOTD bytes, the 762,559-byte export) cannot be checked from the repo. The test code does assert 2,470 quick-chat rows and 23 NPC captures (`repo:prototype/osfr-tools/tests/startup_world.rs:43,55,65`), which agrees with the note.
- The client-side claims (reader addresses, the "confirmed" and "likely" labels) are only partly checked. The addresses exist as functions in the client DB, but I did not verify the field-width readings beyond the Rust parsers' consistency.
- The 6-test and 1-ignored counts match the test file's 7 `#[test]` functions. I did not run cargo.
</result>
