<!-- fleet job=citem-infer id=cblack-licorice-hair-color-card-414073-v6 status=nothing_found turns=2 usd=0.0029 tokens(read,write,in,out)=[6309, 11829, 6, 2698] model=claude-haiku-5-5 -->
# Black Licorice Hair Color Card

{"item": {"name": "Black Licorice Hair Color Card", "locale_id": 414073, "kind": "card"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text: locale:414073 is 'Black Licorice Hair Color Card'. The client definition for Id 35968 (Type 12, Slot 3, Class 1, NoTrade true, SingleUse true) carries the same name, and its description is locale:414087.", "source": "refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:593492-593512"},
  {"claim": "The client definition has \"Cost\": 180 (line 593502). The pack's coin_store_prices [180] matches this client Cost. It is a client-side cost value, not a verified store sale.", "source": "refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:593502"},
  {"claim": "Item 35968 is a member of coin-store category 142 (CoinStoreItems), the category that also holds 35967 and 35969. Category membership gives no price, date, or sale row.", "source": "refs:FreeRealms-Legacy/src/Resources/CoinStoreItems.json:35694-35697"},
  {"claim": "stores.json rows 35951 through 35980 (category 142) all read purchase 180, member 162, sell null, no_sale true, with identical source_tags [L1,L2,L4,R2,L3,L3]. This is a category-wide block, not an item-specific sale; no_sale true argues against a current sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json:7901"},
  {"claim": "The wiki 'Super Spooktacular' page (Oct 2013) lists the Spooktacular-era hair color cards Snowstorm, Pumpkin, Ectoplasm, Phantasm Blue, Bubblegum. Black Licorice is not named there, so the card's era is not established by that page.", "source": "wiki: Super Spooktacular"},
  {"claim": "Sibling cards in the same locale block (Sugarplum 414069, Stargazer 414070, Strawberry 414071, Raspberry 414072, Deadwood 414075) appear only as client text in lookups; no wiki page or article names a seller, drop, or event for any of them in this pack.", "source": "lookup(client, wiki) 'hair color card'"},
  {"claim": "No wiki page, article, video frame, quest, enemy drop, or vendor stock row names Black Licorice Hair Color Card. The earlier StoreBundles Id 3485 record (MarketingItemId 35968) is unpriced and undecoded, so it is not used.", "source": "pack: wiki_page null, vendor_stock [], mentioned_by_other_answers []; refs:FreeRealms-Legacy/src/Resources/StoreBundles.json:11145-11165"}
 ],
 "confidence": 0.15,
 "open": [
  "No acquisition source is verified. No vendor, Marketplace, Coin Shop, quest, drop, event, or prize-wheel row names this card. Do not record a coin-shop or vendor sale from the 180 price alone.",
  "Cost 180 (ClientItemDefinitions:593502) and CoinStoreItems category 142 membership suggest a coin-store candidate, but the stores.json rows are a category-wide block with no_sale true and no item-specific sale. Needs a real sale row or a seller to confirm.",
  "Retirement and current availability are unknown. The Super Spooktacular claim from the earlier answer was removed because the wiki page names other cards, not this one. Retired stays null.",
  "StoreBundles Id 3485 (MarketingItemId 35968, launch 2009-11-29) is unpriced; CurrencyType and Price are undecoded. Decode before counting it as a marketplace or Station Cash source.",
  "stores.json source_tags [L1,L2,L4,R2,L3,L3] are not decoded in the repo schema here; they are block-wide and not used as seller evidence.",
  "Duplicate definition 68835 (and 698182 noted earlier) is unconfirmed as a tint or race variant. Black Licorice (locale 429596) is a separate hair-tint name and is not this card.",
  "The earlier claim that the Legacy record has no coin_store_prices or Cost field was wrong: Cost 180 is present at line 593502. Corrected above."
 ]}
