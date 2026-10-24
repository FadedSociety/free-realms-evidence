<!-- fleet job=bug-hunt id=src-smelting-rs-L1 status=done turns=17 usd=0.0273 tokens(read,write,in,out)=[614005, 59441, 36, 27436] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/smelting.rs lines 1-800 of 1082

Reviewed `smelting.rs` lines 1-800 in full (plus the tail 800-820 needed for context, the `handle` commit at 555-557, and the callers in `gameplay/crafting.rs`, `gameplay.rs` (staged clone at 2335-2351) and `recipe_book.rs`). No panic, unbounded-growth, or reward-duplication path reachable from a client packet was found. Length checks precede every `read_i32` and slice (header 15 bytes, payload 19+len), `decode_payload` checks `len` before `last().unwrap()`, `[..round]` and `kind - 4` are bounded by the earlier `contains` guards, and every early rejection returns before `self.state = next` (line 556). Win/loss/victory are one-shot (Won/Lost early returns, phase check on GameWon), and the transaction is re-checked against inventory in `apply_craft` (`gameplay/crafting.rs:356-366`) inside the caller's staged clone.

One low-severity finding:

- **[low] prototype/osfr-tools/src/smelting.rs:471 and :479 - stat slots are overwritten on every `FRServer_StatUpdate` with no replay check, unlike the sibling Cooking service.**
  - Failure scenario: during `Playing` (after data is sent), a client sends `FRServer_StatUpdate/t101/t3/t120)` and later `FRServer_StatUpdate/t101/t3/t5)`. Each is accepted, and the second value replaces the first in `a.round_stats[0][3]`. The same happens for final stats at line 479 (`game_stats[kind-4]`). Round 0's stopwatch can therefore be rewritten after the movie reported it, and the results packet (`results()`, `smelting.rs:701-718`, which uses `game_stats[0]` or the sum of round timers) reports the rewritten value.
  - Reach: `handle` (`smelting.rs:343`) → `FRServer_StatUpdate` arm (`:446-483`) → `a.round_stats[round][kind] = Some(value)`. Gameplay routes the packet through `route_movie` (`gameplay/crafting.rs:70-73`), and nothing upstream checks it. Cooking guards this with `assign_stat` (`cooking.rs:685-690`), which rejects a different value for a filled slot. Smelting has no equivalent.
  - Impact is limited: stats do not feed the transaction (consumes and grants come from the recipe, `:511-516`), so this changes only the displayed elapsed time and the saved stats. It is a parity gap, not an economic exploit.
  - Fix: route both assignments through an `assign_stat`-style helper that returns `Err` when the slot is already `Some` with a different value (mirror `cooking.rs:685-690`).

No medium or high findings in this window.
