<!-- fleet job=guide-refresh id=Gameplay-Minigame-Framework status=done turns=28 usd=0.0336 tokens(read,write,in,out)=[1389695, 95181, 60, 15643] model=claude-haiku-5-5 -->
# notes/Build Guides/Gameplay/Minigame Framework.md

**Verdict:** minor drift. Most of the server-side claims hold at the tip. One status line on Harvesting is stale against the Build Ledger and Current Progress.

**Corrections:**

1. `old:` Harvesting is code-tested only
   `new:` Harvesting has loaded its board in a native run (Harvest 202011 selected Chef and loaded the original board), but no native round has finished. Payout is tested in-process. Whole-round native acceptance is still open.
   `why:` notes/Current Progress.md:54 (Harvest202011 loaded the original board); notes/Design/Build Ledger.md:105 ("Wired; native round unverified", "payout tested in-process, not natively"); notes/Current Progress.md:69 (Harvest111 native victory and payout still open).

**Checked and holding:**
- Cooking 46, Smelting 77, Forging 139 are the constants in `prototype/osfr-tools/src/cooking.rs:17`, `smelting.rs:16`, `forging.rs:17`. The "completed end to end" claim is backed by the vault reviews the note cites (Native Cooking Finish and Mae 171251, Native Gear Up and Smelting 173814, Native Forging Victory 181715), all of which exist under notes/Reviews/.
- Mining 18 is `mining.rs:49`. The "one accepted drag and a clean quit" claim matches notes/Reviews/Native Mining Score 121834.md:12 and 47. Later runs (151307, 200750) lost, which the note does not contradict because it says "partial".
- Terminal sequence in `minigame.rs`: 39/16 info (`info_packet`, line 666), 39/17 ack plus 26/12 for Flash (`start`, lines 605-638), 39/18, 39/47 with one `scoreTotalScore` row, 39/19 (`result_packets`, lines 747-776). Matches "What the Rust server must do" items 3, 4, 6.
- 39/5 requires the `[instance, -1, -1]` sentinel (`handle_client`, lines 304-309). Matches item 4.
- Pre-win 39/6 answers with 39/19 only (lines 353-367). A 26/42 Close after Won/Lost retires the run without a second 39/19 (lines 372-384). Matches items 7 and 8.
- 39/46 never pays (lines 326-343). Wheel prize is chosen before the spin via `choose_wheel_prize` (lines 484-511). Matches item 10.
- One live run at a time (`offer`, lines 257-261). A stale finish is rejected (`finish_inner`, lines 545-550).
- Registry counts (783 rows, 22 types, 20 groups, 610 links) match `restoration/piece_015.rs` and the note.

**Unsure:**
- "Piece 015 receipts bind rows 46, 77 and 139 as the three natively accepted rows; the other 780 are not" (note line 318). I did not find the receipt file to confirm this.
- Item 5 says to tolerate a trailing `)` on `FRServer_StatUpdate`/`StopLevel`. I did not find handling for it in `cooking.rs` or `forging.rs`. This is a prescription, not a claim about the current code, so I left it.
- Item 11 and item 12 prescribe sending 39/21, 39/23 and 39/67. `minigame.rs` sends none of these. This reads as advice rather than a status claim, so I did not correct it.
- The `IsMiniGameFlashType` set (note line 50) and dispatcher arm lists are client pseudocode. I spot-checked `008a5850` and it agrees (types 3, 6-9, 14-16 return true). I did not verify the rest.
