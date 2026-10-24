<!-- fleet job=citem-critic id=celite-pink-wacky-crash-shirt-69354-v1-evidence-r1 status=no_submit turns=4 usd=0.0021 tokens(read,write,in,out)=[18166, 7944, 10, 1783] model=claude-haiku-5-5 -->
# Elite Pink Wacky Crash Shirt

{"lens": "evidence", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "sources[0].where", "issue": "The coin-store source is evidenced only by a pricing row in stores.json (item 619, category 103, purchase 9453, member 8507, sell 945). That row supports the price and currency, but nothing ties it to a vendor, shop page or sale location. The answer already flags this honestly, so it is a limitation, not an error.", "fix": "Keep 'vendor not identified'. Do not name a vendor unless a store page or NPC stock row confirms one."}, {"field": "evidence[1].claim", "issue": "The source tags are L1, L2, L4, R2, T633, R1. The claim describes them as only 'the Legacy coin store (L1) and the 2014-era re-export (T633, R1)', which leaves out L2, L4 and R2. Minor wording gap.", "fix": "State the full tag list from stores.json line 298: L1, L2, L4, R2, T633, R1."}]}

Checks I ran:
- stores.json line 298 matches the answer exactly: item 619, category 103, 9453 purchase, 10% discount, 8507 member, 945 sell, no_sale false.
- The 9453 price matches the client coin_store_prices in the pack. 9453 × 0.9 ≈ 8507, so the member price is consistent.
- piece_041.rs line 175 confirms rank 20 maps to item 599 (Elite Pink Wacky Crash Helmet, name 69379). Item 619 has no rank-gear row, as the answer says.
- The wiki Weekly Update 01/15/14 does say Demo Derby Driver is once again a Members-only job.

The answer makes no unsupported source claims. Its open items honestly flag the missing vendor, the unknown retired status and the unconfirmed sibling variant. It is wireable on the coin-store price alone.
