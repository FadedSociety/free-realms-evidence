<!-- fleet job=guide-refresh id=Libraries-and-Runtime-Unclassified status=nothing_found turns=13 usd=0.0150 tokens(read,write,in,out)=[314953, 56728, 28, 9455] model=claude-haiku-5-5 -->
# notes/Build Guides/Libraries and Runtime/Unclassified.md

**Verdict:** current for every claim about our code and status. The note has no narrative yet, and its tables are generated client-function labels, not statements about the server. The only numbers I could test disagree with the current client database, so they are listed under Unsure rather than corrected.

**Corrections:** none.

What I checked:
- **Structure and generator.** The note is produced by `scripts/native_map/build_guides.py`. The "Unclassified" guide takes subsystem `unknown` and `unknown.*` (minus `unknown.lobby`, which goes to Matchmaking), per the GUIDES table at `scripts/native_map/build_guides.py:94` and `:105-111`. The note's "How it works" section is still the default placeholder (note lines 11-15), so there is no false status claim there.
- **Internal arithmetic.** 28 confirmed + 535 likely + 1847 speculative + 1015 unknown = 3425. The "563 of 3425" line equals 28 + 535. The subsystem list (line 21) sums to 3425. The index line in `notes/Build Guides/Build Guides.md:72` agrees.
- **Network-linked count.** The note says `Network-linked (wire): 0` (line 19). In `client_sql`, no record whose subsystem is `unknown` or `unknown.*` has a non-empty `wire` list (query returned 0). This holds.
- **Table rows.** I compared about 45 rows (addresses, names, confidence, subsystem) from the tables, including all the `confirmed` ones in the BaseAttachmentGroup, ActorHandler, and CtorBody sections, against the label records. All matched.
- **Shard links.** Spot-checked the "Source shards" links against `notes/Native Map/Shards/`. The sampled files exist. I did not check all ~200 links.

**Unsure:**
- **Header counts may be stale.** `notes/Reviews/Native Map Upkeep 2026-10-15.md:138` says the generated vault guides "remain older snapshots; current queries must use `map.sqlite`." The note is dated 2026-10-12. In `client_sql`, the `unknown`/`unknown.*` scope now holds 6649 labels, against the note's 3425. Subsystem `unknown` is 3192 against 2104 in the note, and `unknown.unclassified` is 1085 against 860. The `client_sql` database may not be the same snapshot as `lab/native-map/run/map.sqlite`. `notes/Design/Build Plan.md:123` cites 68,411 accepted labels, while `client_sql` reports 99,894. I could not confirm which snapshot is current, so I did not give replacement numbers. The fix, if the counts are wrong, is to re-run `build_guides.py`, not to hand-edit the note.
- **"Large or library guide" line (note line 23)** depends on the same generated counts, so it is in the same position.
