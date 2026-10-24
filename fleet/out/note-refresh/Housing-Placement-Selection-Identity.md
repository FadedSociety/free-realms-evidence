<!-- fleet job=note-refresh id=Housing-Placement-Selection-Identity status=done turns=12 usd=0.0155 tokens(read,write,in,out)=[252955, 40137, 26, 15838] model=claude-haiku-5-5 -->
# notes/Research/Housing Placement Selection Identity.md

**Verdict:** minor drift. The core identity and native-anchor claims hold at the tip. Five statements are now false or overstated: one authority wording the note's own receipt says was fixed but was not, a mode-field value, a namespace-overlap receipt line, an item-id count, and an ordering implication.

**Corrections:**

1. `old:` the authority link is the `127/40` fixture definition / item definition pair
   `new:` the ids the server sent alongside the fixture record are the `127/40` fixture definition / item definition pair, a client-observed co-occurrence with the earlier `127/42`; ownership authority remains unproven
   `why:` repo:prototype/osfr-tools/src/housing_service.rs:13-14 says the client readers expose these ids and "This does not establish how the original server authorized or paired them." The note's own receipt (lines 93-95) requires this wording, but line 63 was never changed.

2. `old:` mark the mode (`+0x4140` = 1/2)
   `new:` set `+0x4140` = 1 in both callbacks, with `+0x18` = 1 (`FUN_00ab0d60`) or 2 (`FUN_00ab2250`) selecting the callback
   `why:` client fn `00ab0d60` sets `param_1+0x18 = 1` and `+0x4140 = 1`; fn `00ab2250` sets `+0x18 = 2` and `+0x4140 = 1` (client_sql fn table, decompiled pseudocode). `00ac42d0` is the only one that sets `+0x4140 = 3`.

3. `old:` 4179/4214 in `Npcs.json`
   `new:` 4179/4214 in `Npcs.json`, `StoreBundles.json` and `StoreBundleGroups.json` (4179 as a `GameItemId`, 4214 as a `StoreBundleId`); delete the following word "only,"
   `why:` repo ref copy Sanctuary/src/Resources/StoreBundles.json:14819 (`"GameItemId": 4179`) and Sanctuary/src/Resources/StoreBundleGroups.json:155 (`"4214": {"StoreBundleId": 4214`). The receipt's "Npcs.json only" is false. 4594/4595 in none of the three files is confirmed (only ClientItemDefinitions.json).

4. `old:` resolves **all eight authoritative
   item ids** to housing models
   `new:` resolves **all eight** placement item-definition ids (seven distinct; 7466 is used by two placements) to housing models
   `why:` the note's own table (lines 31-32) lists 7466 twice. Sanctuary/src/Resources/ClientItemDefinitions.json:140926 (`"Id": 7466`, Blue Square Block) and the other six ids (7462, 14300, 16039, 16040, 18110, 77259) are present.

5. `old:` `127/1` request id -> `127/2` first dword, echoed by
   `new:` `127/1` request id -> `127/2` first dword (7 of 8 placements follow a matching `127/1`; placement frame 31494 precedes its `127/1` at 31629, so it shows membership only), echoed by
   `why:` the note's receipt item 1 (lines 87-90) records this ordering. The verdict's arrow chain still implies a request-before-placement pairing for every row.

**Unsure:**
- The `lab/reports/housing-placement-selection-identity-20261009T2230Z/` and `…corrections-20261009T1745Z/` artifacts (96/96 log, receipt JSON, pre-correction note) are not in the repo tree. `.gitignore` puts `/lab/` in the sibling `../lab`, so I could not confirm the 96/96 counts or the 8 placement frames (31494 to 32619) or the 127/40 frame 32098.
- The pinned community table exists at `refs:Sanctuary/src/Resources/ClientItemDefinitions.json` as cited. The note's `ClientItemDefinitions` model names for 7466 (`hsg_block_01.adr`) and 77259 (`hsg_block_flatrectangle_01.adr`) were not individually confirmed.
- Pseudocode line ranges (e.g. 1393520-1393568, 1407911-1407944, 1409713-1424) and the wire-builder claim about `+0x4160` as the first payload dword were not checked.
- Body lines 59-60 still say the selection ids appear in "`Npcs.json`, `CoinStoreItems.json` and `StoreBundles.json`" as a blanket statement. The receipt narrows it, but the body was not changed. This is not false in aggregate, so I did not propose an edit.
