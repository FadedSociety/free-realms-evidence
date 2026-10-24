<!-- fleet job=bug-verify id=src-bin-osfr-gateway-rs-L2401-f3 status=done turns=8 usd=0.0079 tokens(read,write,in,out)=[92751, 23294, 18, 8193] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/bin/osfr-gateway.rs:2635-2638

**Verdict:** confirmed (the divergence is real; the claimed disk state is slightly off, see below)

**Severity if confirmed:** medium. The trigger is a disk or write error inside the server, not something a remote player can send. The duplication also needs a further action by the live partner, such as selling or trading the item, followed by a save and then a restart. That does not meet the "remote player can gain items" bar for high.

**Evidence:**

1. **Real server code.** `commit_trade`, `commit_trade_parties`, `settle_trades` and `recover_trade_journals` are defined in `src/bin/osfr-gateway.rs` itself (2550, 2579, 2691, 2656). That is the binary root, not a `#[path]` test include. Only `lead_trade_commit.rs` is test-only (`#[cfg(test)] #[path]` at 4639-4641).

2. **Input reach.** `settle_trades` is called from the session's `handle` at 2008, and `commit_trade` is called from `settle_trades` at 2698. The only check before the journal is the ownership and inventory check at 2594 (`selected_character` and `inventory_state() == before`). No check covers a write error after the journal rename at 2633. The claimed path is real.

3. **Failure mechanics.** Confirmed in the code:
   - The journal is renamed at 2633.
   - `save(...)?` at 2636 returns early on error, so steps 5 (2641-2644) and the `settled` call (2701-2705) are skipped.
   - `commit_trade` puts the taken sessions back at 2575, but their gateways are still the pre-trade copies, because staged gateways are only installed at 2643. So the live partner keeps the item in memory.

4. **Correction to the claim's disk story.** The erroring session `me` is not left alone. `handle` propagates the `Err` from 2008, and `run` calls `end_session` (3751-3752). `end_session` then saves `me`'s in-memory pre-trade snapshot (4429). That overwrites `me`'s on-disk post-trade save if `me` was side 1. The lasting divergence is therefore for the live other party (the restored taken session), not for "side 1 stays post-trade". The journal still holds the post-trade state for both sides until restart. The duplication mechanism still works if the live other party saves a sold or changed state and then the restart replays the journal.

5. **Design context.** Step 4's doc comment (2546-2548) says a write error between the saves "leaves the journal, and the next start writes both saves from it". So the restart replay is the intended recovery. The in-memory divergence is an unhandled gap in that design, not an accident the author missed in the docs.

**Corrected fix:** the claimed fix (log and continue after the journal rename, install the staged gateways, and return `Ok(Some(deliveries))`) would make live memory match the durable journal. It does not fix the disk-side issue, though: the failed side stays pre-trade on disk until restart. A complete fix should also stop `end_session` from saving a stale pre-trade snapshot for a trader whose trade is journaled, and should still send `settled` so the trade service does not hold the trade open. Logging the save error and continuing is a judgement call that trades a visible error for in-memory consistency.
