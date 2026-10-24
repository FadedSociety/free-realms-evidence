<!-- fleet job=pin-audit id=tests-starter-items-rs status=nothing_found turns=4 usd=0.0021 tokens(read,write,in,out)=[12438, 8308, 10, 1816] model=claude-haiku-5-5 -->
# tests/starter_items.rs

No findings in `prototype/osfr-tools/tests/starter_items.rs` for the screened lines 417, 426 and 434.

The prices come from the test's own fixture, not from a shipped data file:

- The fixture (`starter_items.rs` ~lines 293-302) writes its own `stores.json` into a temp content directory. It sets `store_row(STARTER_BOW, 10, STARTER_SELL_PRICE)` and `store_row(NORMAL_ITEM, 15, NORMAL_SELL_PRICE)`, so the purchase price of the starter bow is 10 and of the normal item is 15.
- **Line 417 and 426** (`coins_before - 10`): the 10 is the starter bow's purchase price in that fixture row.
- **Line 434** (`coins_before - 25`): this is the cumulative spend of the two merchant buys in the same test, 10 (bow, line 414) plus 15 (normal item, line 431). It is also fixture-set.
- The 375 sell price in the comments and `STARTER_SELL_PRICE` are fixture values too, and the sell-price asserts already read `sold.price` from the gateway reply.

Since the test writes the values it asserts against, retuning the shipped `data/content` files does not affect these lines. No change needed.
