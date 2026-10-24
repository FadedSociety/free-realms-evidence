<!-- fleet job=citem-infer id=cflat-square-cheese-block-147668-v1 status=done turns=3 usd=0.0019 tokens(read,write,in,out)=[7835, 7544, 8, 1769] model=claude-haiku-5-5 -->
# Flat Square Cheese Block

{"item": {"name": "Flat Square Cheese Block", "locale_id": 147668, "kind": "furniture"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop purchase of the cheese-material housing block (store item 36469, store category 147, tint group 3); the client's Coin Shop record gives the purchase price", "where": "Coin Shop", "price": "1000 coins (store list price); 900 coins for members (10% member discount, from the same store record); store sell-back price 100 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:11940 (item_id 36469); articles: http://www.freerealms.com:80/article/detail.action?articleId=1435 (\"All the standard block shapes made out of cheese can be found on the Coin Shop\")"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item name 'Flat Square Cheese Block' is locale 147668, description 'Great for stackability.', model hsg_block_flatsquare_01.adr, one definition (36469)", "source": "client definition in the evidence pack; locale:147668"},
  {"claim": "Store data lists item 36469 in category 147 with purchase price 1000 coins, member price 900 coins, sell price 100 coins, no_sale false, so it is sold for coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:11940"},
  {"claim": "Developer article states cheese versions of all standard block shapes were added and are sold on the Coin Shop", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1435"},
  {"claim": "Sibling items 147663-147673 (Half Cylinder, Flat Rectangle, Flat Square, Ramp, Wedge cheese and blue polka dot blocks) form one block-shape set", "source": "client_cluster locale:147663..147673"}
 ],
 "confidence": 0.6,
 "open": [
  "No wiki page covers this item, so the Coin Shop source rests on the store record and the developer article, not a wiki listing. The specific NPC or shop screen is not named in any source.",
  "The store record's source_tags (L1, L2, L4, R2, T633, R1) are not decoded here; I did not confirm what they mean for the sale window.",
  "Retirement and later availability are unknown; no source in the pack says whether the cheese block shapes were later removed.",
  "The 1000-coin price comes from our store data, not from a wiki or live price check. The wiki has no price to cross-check against.",
  "Kind is set to furniture from the housing-block context and the cheese-material block set, not from a class or slot field (slot 0, class 0)."
 ]}
