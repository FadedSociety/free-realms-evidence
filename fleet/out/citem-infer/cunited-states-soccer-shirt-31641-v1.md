<!-- fleet job=citem-infer id=cunited-states-soccer-shirt-31641-v1 status=done turns=4 usd=0.0031 tokens(read,write,in,out)=[16160, 11305, 10, 3008] model=claude-haiku-5-5 -->
# United States Soccer Shirt

{"item": {"name": "United States Soccer Shirt", "locale_id": 31641, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale, item definition 16324 (chest slot, tint group 1), listed at 50 coins with a 10% member price of 45 coins; flagged no_sale", "where": "coin store (stores.json category 103)", "price": "50 coins (member price 45 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:6636 (item_id 16324); client definition coin_store_prices [50]"},
  {"type": "marketplace", "detail": "Sold in the 2010 FIFA World Cup line of soccer shirts alongside the Brazil, Spain, Italy and Mexico shirts (sibling items; the wiki gives no price for them)", "where": "Station Cash Marketplace", "price": null, "currency": "station_cash", "source": "wiki: Brazil Soccer Shirt, Spain Soccer Shirt, Italy Soccer Shirt, Mexico Soccer Shirt (category: SC Marketplace per the 2010 FIFA World Cup text); unverified for the US shirt itself"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Client name and description: 'United States Soccer Shirt', 'Show support of your favorite country's team!', chest slot 3, class 143, one definition (16324), model freestyle_<race>_<gender>_chest_shortslvshirt.adr", "source": "locale:31641; locale:31643; client definition"},
  {"claim": "Sibling national shirts (Brazil, Spain, Italy, Mexico) are documented as unobtainable, All Jobs chest clothing acquired during the 2010 FIFA World Cup through the Station Cash Marketplace", "source": "wiki: Brazil Soccer Shirt; Spain Soccer Shirt; Italy Soccer Shirt; Mexico Soccer Shirt"},
  {"claim": "Coin store record for item 16324 at 50 coins, member price 45, no_sale true", "source": "repo:prototype/osfr-tools/data/content/stores.json:6636"},
  {"claim": "The wiki has a Thundercat's T-Shirt page: an unobtainable Freestyle/Soccer Star chest item given to US residents by a promo video from the log-in screen. It is a different name, so it is not confirmed as this shirt", "source": "wiki: Thundercat's T-Shirt"},
  {"claim": "Locale 31643 is tagged as the Uruguay shirt, but its text is the item description, so the tag is a labeling error", "source": "locale:31643"}
 ],
 "confidence": 0.5,
 "open": [
  "Conflict: our store data lists 16324 as a coin store item at 50 coins, but the wiki says the sibling 2010 World Cup shirts were Station Cash Marketplace items. Both may be true (a coin price record alongside an SC release), and no wiki page for the US shirt confirms either source. Verify which channel sold it before the rebuild sets prices.",
  "The 'Coin Shop' label is an inference from stores.json, not a wiki category. The wiki gives no coin price for the US shirt.",
  "Possible promotion: the Thundercat's T-Shirt promo (US residents, log-in video) may be the same or a related shirt. Not confirmed; needs a wiki page or video frames.",
  "Retired status comes from the sibling shirt pages (unobtainable), not from a page for this item. The first-pass 'live: yes' tag is a hint only and was not used.",
  "No quest, drop, or vendor stock entries mention this item, and no video frames show it."
 ]}
