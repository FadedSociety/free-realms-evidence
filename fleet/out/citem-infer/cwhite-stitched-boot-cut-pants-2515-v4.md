<!-- fleet job=citem-infer id=cwhite-stitched-boot-cut-pants-2515-v4 status=done turns=3 usd=0.0030 tokens(read,write,in,out)=[18242, 12980, 8, 2353] model=claude-haiku-5-5 -->
# White-Stitched Boot-Cut Pants

{"item": {"name": "White-Stitched Boot-Cut Pants", "locale_id": 2515, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Unidentified coin store/vendor. Only a price row exists: stores.json item 221, category 104, 150 coins, member price 135, sell price 15. Category 104 also holds items priced 9453 and 188, so the category does not name a store. Seller not identified.", "where": null, "price": "150 coins (member 135 coins, 10% member discount; sell-back 15 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:138; client coin_store_prices [150] on definition 221"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 2515 'White-Stitched Boot-Cut Pants', definition 221, slot 4 (legs), class 11, model freestyle_<race>_m_legs_bootcutpants.adr", "source": "locale:2515; client definition"},
  {"claim": "stores.json lists item 221 in category 104 at 150 coins, member 135, sell 15, matching the client's coin_store_prices [150]", "source": "repo:prototype/osfr-tools/data/content/stores.json:138"},
  {"claim": "Category 104 is mixed: items 137, 159, 187 are 9453 coins; the row does not identify one store", "source": "repo:prototype/osfr-tools/data/content/stores.json:101, 111, 118"},
  {"claim": "The wiki Farmer and Adventurer gear lists contain '[Boot Cut Pants]' and 'Small Stitched Pants' as separate entries. Neither shows 'White-Stitched' or '[White] [Stitched]' text, so the previous answer's bracket reading is not supported. Those lists are a different item (client locale:8602 'Boot-Cut Pants' is the nearest name), and they are not evidence for locale 2515.", "source": "wiki page:ns0 Farmer; wiki page:ns0 Adventurer; client locale:8602"},
  {"claim": "Other client names near 2515 are distinct items: locale:2879 'Flared Boot-cut Pants', locale:2895 'Plain Boot-cut Pants', locale:2851 'Small-stitch Boot-cut Pants'", "source": "lookup client '\"Boot-Cut Pants\"'"}
 ],
 "confidence": 0.3,
 "open": [
  "The seller behind the 150-coin price (stores.json category 104) is not identified. The 'vendor' type is kept only because the rules treat a client coin_store_price as coin vendor sale evidence; no NPC, store or vendor name is evidenced, so a builder cannot place it yet.",
  "The Coin Shop label is not confirmed: no repo note names category 104 as the Coin Shop.",
  "The previous answer's Farmer/Adventurer source is withdrawn: the wiki lists show '[Boot Cut Pants]', not this item. No job or outfit acquisition route is evidenced.",
  "Live and retired status are unknown. No wiki page, article or video gives a sale date or retirement. The client price row is the only live-leaning signal.",
  "Wiki lookup with the hyphenated name failed with FTS5 errors; the quoted search '\"Boot-Cut Pants\"' worked and found no page for locale 2515 itself. No video or image evidence names it.",
  "Vendor-stock, quest, drop and event lookups were not returned in the pack; none were found for this item."
 ]}
