<!-- fleet job=note-refresh id=Pieces-075-Postman-delivery-routes status=done turns=15 usd=0.0157 tokens(read,write,in,out)=[398895, 54175, 32, 9838] model=claude-haiku-5-5 -->
# notes/Research/Pieces/075 Postman delivery routes.md

**Verdict:** minor drift. Nearly every checkable claim holds at the tip: the module path, the four gap constants, the `DeliveryRun` methods, the 23 mailbox rows, the 15 activity rows, the 16 route-text lines, the test counts (6 Rust, 10 Python), the checker file and its named checks, and the client Lua. One row-level claim is false.

**Corrections:**

1. `old:` The rest ship with the `NOT LIVE - ` prefix, including `Special Delivery` (12) and two `Postal Route: Sanctuary` rows (24 and 1002).
   `new:` The rest ship with the `NOT LIVE - ` prefix, except `What a Mess!` (14), which carries no prefix and is live. The `NOT LIVE - ` prefix also covers `Special Delivery` (12) and two `Postal Route: Sanctuary` rows (24 and 1002).
   `why:` repo:prototype/osfr-tools/src/restoration/piece_075.rs:371-379 (row 14 is named `"What a Mess!"`, and `live` is computed from the prefix at :155, so it is `true`). Rows 3, 5, 6, 12, 13, 16, 24, 72 and 1002 carry the prefix (:331-457).

**Unsure:**

- `repo:notes/Research/Unrouted Client Requests.md:342` cites this note at `:39`. Line 39 of this note is blank (the "Original facts" heading is at :38). That is a pointer in another note, so I did not change it here.
- The wiki claims (the Postman page's "30+ quest entries" and the trainer list) and the stock-locale hash IDs other than 388255 were not checked. The wiki and stock locale are lab-side files, and the hash spot-checks I ran in refs were consistent with the note.
- The status claim that the helper is wired into no path holds: `piece_075` is not referenced under `prototype/osfr-tools/src` outside the module itself (`restoration/` has no registration), and `tests/piece_075.rs` pulls the module in by `#[path]`. I did not run the test commands, so the "6 passed" and "10 OK" results are unconfirmed at the tip.
- The `repo:notes/Design/Build Ledger.md:136` entry ("075 postman") was not read, so I did not check any status it gives.
