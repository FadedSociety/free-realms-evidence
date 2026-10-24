<!-- fleet job=citem-infer id=csuper-coin-booster-2443-v1 status=nothing_found turns=5 usd=0.0046 tokens(read,write,in,out)=[49333, 18082, 12, 3605] model=claude-haiku-5-5 -->
# Super Coin Booster

{"item": {"name": "Super Coin Booster", "locale_id": 2443, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines 'Super Coin Booster' as locale 2443 (ucdt 3290511622 / ugdt 3821494337 in en_us_data), with description 'When playing your favorite Job, use this scroll for great luck earning extra money for a while.' (locale:2443, locale:2449 text).", "source": "locale:2443; FreeRealmsLocaleTools/test/FreeRealmsLocaleTools.Tests/data/en_us_data.dat:86915"},
  {"claim": "Legacy client item definitions carry a Comment label 'Super Coin Booster', so the item existed in the 2009-2014 data set.", "source": "refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:1619"},
  {"claim": "Sibling scrolls in the same name cluster are sold or dropped: Super Star Booster is an SC Shop item at 200 SC (wiki), Wheeler Coin Booster Scroll comes from the Daily Wheel (wiki), and Super Star Booster appeared as a Trick or Treat / Super Spooktacular 2013 reward (wiki 'Super Spooktacular', 'Items' pages).", "source": "wiki: Super Star Booster (SC Shop, 200 SC); wiki: Super Spooktacular; wiki: Wheeler Coin Booster Scroll"},
  {"claim": "No wiki page, image, article, video frame, vendor stock list, quest reward, or drop names 'Super Coin Booster'. Lookups across wiki, articles, client, and video return only the locale line and the Wheeler/Super Star scrolls.", "source": "lookup results for 'Super Coin Booster' and 'Coin Booster scroll'"},
  {"claim": "stores.json has a category-103 entry with item_id 2443 at purchase_price_coins 9453, but the key does not match this item's definition id (81), and the same 9453 price is also on item_id 2444, a different cluster item. Store item_id values 2438-2447 track the locale-id range, so the entry cannot be tied to this scroll with confidence. Not used as a source.", "source": "repo:prototype/osfr-tools/data/content/stores.json:5881 (item 2443) and :5882 (item 2444)"}
 ],
 "confidence": 0.15,
 "open": [
  "No real acquisition source found. The first-pass guess of 'marketplace' has no evidence behind it; the pack's coin_store_prices is empty and no wiki page covers the item.",
  "stores.json item_id 2443 (9453 coins, category 103) may be a store entry for this scroll, but the id mismatch with definition id 81 and the duplicate price on 2444 make it unreliable. Needs a check of how stores.json item_id maps to definitions before treating it as a coin-vendor sale.",
  "Live status and retirement unknown. Check the SC Marketplace and Coin Shop wiki categories and the 2009-2014 promo/holiday pages for 'Super Coin Booster' by name; it may be a retired SC item like Super Star Booster.",
  "Description says it boosts coins for a while, same effect as Wheeler Coin Booster Scroll (+25% coins per wiki tooltip). Effect size for this item not confirmed."
 ]}
