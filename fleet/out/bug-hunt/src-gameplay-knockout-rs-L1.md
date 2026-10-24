<!-- fleet job=bug-hunt id=src-gameplay-knockout-rs-L1 status=nothing_found turns=9 usd=0.0053 tokens(read,write,in,out)=[80221, 18685, 20, 4375] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay/knockout.rs lines 1-50 of 50

No defect in `prototype/osfr-tools/src/gameplay/knockout.rs` lines 1-50 that a client packet or save can reach.

What I checked:

- **`handle_paid_revive` (lines 37-48), length and prefix guard.** `inner.len() != 13` is checked before `inner[12]`, so there is no out-of-bounds read. The non-1 flag returns `Ok(false)`, and `resume` (`encounter/revive.rs:64-73`) rejects anything above 1 on the free path.
- **Price and wallet (lines 43-44).** The price comes from the server's `paid_revive_cost` (`encounter.rs:1085`, `encounter/field.rs:245`), not from the packet. The engine checks `wallet < cost` (`encounter/revive.rs:119-125`) against the same coin value that `spend_coins` checks. `spend_coins` (`inventory.rs:877-882`) uses `checked_sub`, so a short wallet is an error and not an underflow.
- **Mutation before `?` (lines 43-44).** `engine.paid_revive` revives the player (`revive.rs:126`) before `spend_coins` runs. If `spend_coins` failed, the engine would stay revived with no charge. I could not reach that failure, since the engine has already checked the same wallet value. The whole `Gameplay` is also staged and cloned by the gateway (`bin/osfr-gateway.rs:1644-1645`), so an `Err` discards the staged world. I'm noting it as a fragility, not a finding.
- **`receive_field_damage` (lines 11-24).** The `damage` value comes from server-side `tick_shared_motion` hits, summed with `saturating_add` (`bin/osfr-gateway.rs:3117-3127`), not from the client. `engaged` comes from `field.enemies_targeting`, also server-side. The field-damage path therefore does not trust client values.

Out of window, and not a finding: `gameplay.rs:4745` and `:4730` call `self.encounter.as_mut().unwrap()` unguarded, while `handle_paid_revive` tolerates `encounter == None`. I did not verify that `encounter` is always `Some` in-world, so I have not reported it.
