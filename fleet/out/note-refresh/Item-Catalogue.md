<!-- fleet job=note-refresh id=Item-Catalogue status=done turns=13 usd=0.0157 tokens(read,write,in,out)=[312216, 48359, 28, 13009] model=claude-haiku-5-5 -->
# notes/Research/Item Catalogue.md

**Verdict:** minor-to-moderate drift. The file paths, the row-layout and round-trip claims, the W166 runtime union (58,835 ids), the bundle gate and the 35/34 wire framing all check out at the tip. The 35/34 section is out of date: it says no route is built and that the generated map still has to be supplied to the lookup, but the catalogue is already merged into the lookup. The loader-cap sentence is also stale.

**Corrections:**

1. old: `## On-demand 35/34 plan (no route built)`
   new: `## On-demand 35/34 lookup (route and catalogue merge built; native gate open)`
   why: `repo:prototype/osfr-tools/src/inventory.rs:414-416` merges `item-catalogue.json` into the same `definitions` map (`entry(id).or_insert`), and `inventory.rs:1109-1125` (`definition_replies`) serves any merged ID from `self.content.definitions`. `inventory.rs:1155-1160` routes 35/34 to it. Only the native gate is still open.

2. old: `Lead integration should supply the generated ID map to this existing lookup, preserve the current malformed-request rejection and unknown-ID no-op policy (R), and bound/rate-limit replies per session (R).`
   new: `The generated ID map is already merged into this lookup (`Inventory::parse_content` inserts the catalogue rows under the captured rows). Keep the current malformed-request rejection and unknown-ID no-op policy (R). Bounding and rate-limiting replies per session (R) is still for the caller: `definition_replies` does not apply it, so the lead must apply the session budget before calling it.`
   why: `repo:prototype/osfr-tools/src/inventory.rs:414-416`, `inventory.rs:1109-1125`; the caller-side budget requirement is stated at `inventory.rs:7-9`.

3. old: `` `Inventory::load` currently caps definitions at 4,096 rows and its whole manifest at 4 MiB; ``
   new: `` `Inventory::load` caps the captured `inventory.json` manifest at 4,096 definitions and 4 MiB; the merged `item-catalogue.json` has its own bounds of 65,536 rows, 32 MiB of definition bytes and a 128 MiB file; ``
   why: `repo:prototype/osfr-tools/src/inventory.rs:28-29` and `:390`, `:384` (manifest cap, `MAX_ITEMS` and `MAX_CONTENT`), and `inventory.rs:36-38`, `:246-253`, `:266-276` (`MAX_CATALOGUE_ROWS`, `MAX_CATALOGUE_BYTES`, `MAX_CATALOGUE_FILE`). The 4,096 cap no longer applies to the merged runtime, which holds 58,835 ids.

4. old: `The route already exists: `gameplay.rs` delegates 35/34 to `Inventory::handle`;`
   new: `The route already exists: `gameplay.rs` delegates 35/34 to `Inventory::handle_with` when a player context exists, and to `Inventory::handle` otherwise;`
   why: `repo:prototype/osfr-tools/src/gameplay.rs:5230-5234` (`handle_inventory`) and `gameplay.rs:4447-4449`. Both paths reach `route()`, which handles 35/34 (`inventory.rs:1145-1160`). This is a precision fix, not a behaviour change.

**Unsure:**
- The "about 68 MiB" fragment size: `inventory.rs:272` repeats the 68 MiB figure as a comment, but I did not measure it. The "about 12 MiB" complete-batch size was not checked.
- The self-check summary (line 147) says "roundtrip, a mutation canary and five malformed rows passing". `scripts/build_item_catalogue.py:214` also reports "8 loader-rule refusals passed". This is an omission, not a falsehood, so I did not correct it.
- Counts from the private lab (1,703 rows, 1,649 ids, 419/1,284 mismatches, 302 client overlays, the 36/4 absent IDs) and the native addresses in the table could not be checked from the repo. `client_sql` confirmed that the functions named in the 35/34 section exist (`00933501`, `008f8180`, `008d7980`, `00919e10`, `00a3c290`, `008cc760`, `008e3760`, `00911a90`), but I did not trace their call graph.
- The repo-side claims all held: `scripts/build_item_catalogue.py`, `scripts/bundle/item_content.py`, `scripts/content_check.py` (`load_item_definitions`, `item_coverage`), `tests/item_catalogue_roundtrip.rs` (ignored, requires `OSFR_ITEM_CATALOGUE`, calls `encode_definition_batch_v2`), `inventory.rs:607` (`definitions_packet`), and the 54/54 ride coverage (`notes/Autopilot/T230.md`).
