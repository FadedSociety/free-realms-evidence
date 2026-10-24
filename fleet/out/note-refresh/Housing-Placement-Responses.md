<!-- fleet job=note-refresh id=Housing-Placement-Responses status=done turns=17 usd=0.0239 tokens(read,write,in,out)=[617844, 69971, 36, 18021] model=claude-haiku-5-5 -->
# notes/Research/Housing Placement Responses.md

**Verdict:** minor drift. The recovered-layout facts (127/2 = 42 bytes, 127/41 = 10 bytes, 127/44 = 22 bytes, 127/53 = one string) still match the codec at the tip. The forward-looking "Minimal next integration scope" is badly stale: all four integration steps are already implemented in `prototype/osfr-tools`. Lab-only evidence (captures, oracle logs, pseudocode line numbers) could not be checked from the repo.

**Corrections:**

1. old: `1. Serialize the 133-byte 40 fixture prefix plus a 44 house-info update after a placement (oracle-` / `proven bytes today); the 94-byte tail stays a blocker until decoded.` (lines 105-106)
   new: `1. Already routed: a placement replies 40 plus 44 (\`housing_service.rs:1551-1563\`), and the 40 record is encoded by \`housing_native.rs:530\`. The 94-byte tail is still filled with empty/zero placeholders, so it stays a blocker until decoded.`
   why: `repo:prototype/osfr-tools/src/housing_service.rs:1551-1563` (`place` returns `FixtureUpdate` + `HouseInfo`); `repo:prototype/osfr-tools/src/housing_service.rs:1918-1919` ("Unresolved definition and tail fields use empty/zero placeholders"); `repo:prototype/osfr-tools/src/housing_native.rs:530`.

2. old: `2. Answer a pickup with 41 = the server-minted fixture guid; answer a save with 51.`
   new: `2. Already routed: a pickup answers 41 for the requested fixture guid plus 44, and a save/move answers 51 (PositionUpdate). The fixture guid is echoed from the request, not minted in this path.`
   why: `repo:prototype/osfr-tools/src/housing_service.rs:1594-1599` (pickup: `FixtureRemove { fixture_guid }` + `HouseInfo`); `repo:prototype/osfr-tools/src/housing_service.rs:1340-1344` (`PositionUpdate`).

3. old: `3. Parse 2 as client input (first dword + transform) and map the first dword to the item ledger only after its identity is recovered.`
   new: `3. Parse 2 as client input (already done: \`PlaceFixture::decode\`). The service treats the first dword as a 127/1 selection id bound to an inventory item (R, not established by this note's evidence). Keep any item-ledger mapping gated on the identity review.`
   why: `repo:prototype/osfr-tools/src/housing_native.rs:232-245` (`PlaceFixture::decode`); `repo:prototype/osfr-tools/src/housing_service.rs:9-12` (selection-id binding claim); `repo:notes/Reviews/Housing Placement Selection Identity Review.md:14-25`.

4. old: `4. Use the one-string 53 body for the \`HousingMaxFixtures\` denial with an accurate reason text.`
   new: `4. Already routed: a refused decorate request sends the chat line plus a 127/53 reply with a per-error reason (the fixture cap reads "Fixture limit reached."). Any other refusal uses the generic "Fixture placement denied." text.`
   why: `repo:prototype/osfr-tools/src/gameplay/housing.rs:99-104` (refusal path pushes `denial_reply()` for decorate requests); `repo:prototype/osfr-tools/src/housing_service.rs:672` (`FixtureLimitReached` → "Fixture limit reached."); `repo:prototype/osfr-tools/src/housing_service.rs:698-711`.

**Unsure:**

- **127/2 first-dword identity (line ~50, "identity not established", and the blocker at lines ~142-150).** `housing_service.rs:9-12` and the L031 brief say the decorate bar passes the inventory item guid (`ScriptsBase.lua:33602`, `House.PlaceFixture(id)` at `ScriptsBase.lua:33752`) and that 127/1 binds it. The Selection Identity Review (`notes/Reviews/Housing Placement Selection Identity Review.md:25`) found the selection id is not a scalar sub-field of the paired item entry. The note's "not established" wording still matches the review, but the code comment asserts a resolution. I did not change the note.
- **127/40 tail.** `housing_native.rs:519-576` (`FixtureUpdate`: instance + info + definition + guid list + 3 words, with `TAIL_BYTES_EMPTY = 94`) may cover more of the record than the note's "94 bytes not decoded" implies. I could not do the byte arithmetic against the 229-byte capture from the repo.
- **Lab-only claims** (capture counts, 91/91 and 9/9 checks, 19/19 127/44 bodies, CurFixtureCount ladder, "server build contains only the housing enum") cannot be checked; `lab/` is not in the repo.
- **Cross-links** (`Housing Restoration`, `Pieces/022`, `Pieces/025`, `WorkItems/025`, `WorkItems/030`) all resolve in `notes/`. Item 030 is "House native acceptance" (`notes/MMO Work Queue.md:42`), so the native-acceptance pointer is correct.
