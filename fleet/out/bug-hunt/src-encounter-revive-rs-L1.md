<!-- fleet job=bug-hunt id=src-encounter-revive-rs-L1 status=nothing_found turns=10 usd=0.0061 tokens(read,write,in,out)=[92166, 16657, 22, 6261] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/encounter/revive.rs lines 1-170 of 170

Reviewed `encounter/revive.rs` lines 1-170 and the callers that reach it. No defect I can tie to a line and show is reachable from a client packet or save.

Checked and ruled out:
- `resume` (revive.rs:64-92): the length check at :65 (`inner.len() != 13`) runs before the `inner[4..8]`, `inner[8..12]` and `inner[12]` reads at :65/:81-82, so no out-of-bounds or `unwrap` panic. The `try_into().unwrap()` on fixed 4-byte slices cannot fail.
- `paid_revive` (revive.rs:100-129) and its only caller `handle_paid_revive` (gameplay/knockout.rs:31-49): the wallet check at :120 uses the same balance that `spend_coins` (inventory.rs:877-893) later checks via `checked_sub`, so the charge cannot fail after the engine has revived. The `? ` after `spend_coins` therefore cannot leave a revive without a charge in practice. The revive outcome carries no rewards, defeats or completions, so `apply_encounter` has nothing that can fail after the spend.
- Price bounds: `paid_revive_cost` is either `RETAIL_REVIVE_COST` or `PaidRevive::cost()` (revive.rs:51-56), which rejects values above `MAX_REVIVE_COST` and bad provenance at load (field.rs:83-86). So the `as i32` at revive.rs:162 is safe, and the client never supplies the price.
- Client authority: the 41/122 payload contributes only the paid bool (:68) and the instance/encounter ids (:81-85, which only select the Lost-exit path). Health, grace and the price come from server state. The client does not choose the place: the safe location is `self.content.world` (:134) and the Lost exit uses the stored return location (encounter.rs:2583-2586).
- `revive` (:142-151): `saturating_add` for the grace time; no panic.
- Zero-cost paid revive (:72, :120): a price of 0 is documented as a free spot revive, so it is by design, not a defect.
- Auto-revive (encounter.rs:2336-2339) and `exit` (encounter.rs:2579-2607) were read only as needed; no problem found.
