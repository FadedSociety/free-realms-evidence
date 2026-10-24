<!-- fleet job=citem-infer id=cheart-shaped-roofing-shingles-19584-v1 status=done turns=10 usd=0.0083 tokens(read,write,in,out)=[160236, 28072, 22, 6277] model=claude-haiku-5-5 -->
# Heart-shaped Roofing Shingles

{"item": {"name": "Heart-shaped Roofing Shingles", "locale_id": 19584, "kind": "furniture"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store listing (roof category 55, tint group 1) in the 2009 PC build's CoinStoreItems; no price in that file", "where": "Coin store, roof category (category 55)", "price": null, "currency": null, "source": "refs:Sanctuary-PC2009-20261009/src/Resources/CoinStoreItems.json:8313 (Id 76783, CategoryId 55, TintGroupId 1)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition: definition Id 76783, NameId 19584, DescriptionId 19982 (description 'A heart-thatched roofing that makes every day sweet.'), CategoryId 55, Type 17, IsTintable true, MaxStackSize -1, MinProfileRank 1, Cost 10000, MemberDiscount 10.", "source": "refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:1240254-1240273"},
  {"claim": "Locale 19584 is the item name 'Heart-shaped Roofing Shingles'; the sibling roofing/flooring names (19579-19589) are the same furnishing family.", "source": "locale:19584"},
  {"claim": "Name id 19584 is shared by an unrelated item: definition Id 19584 is 'Pro Ninja Cowl' (store row item_id 19584, category 101, tint 2, 358 coins). That row is NOT this roofing item; the store row must not be used as this item's price.", "source": "repo:prototype/osfr-tools/data/content/stores.json:4710; refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:351225"},
  {"claim": "No repo store row exists for definition 76783 in prototype/osfr-tools/data/content/stores.json, and the Legacy CoinStoreItems.json has no 76783 row, so the pack's empty coin_store_prices is correct.", "source": "repo:prototype/osfr-tools/data/content/stores.json (no item_id 76783); refs:FreeRealms-Legacy/src/Resources/CoinStoreItems.json"},
  {"claim": "The 2009 PC build's CoinStoreItems lists 76783 in category 55 alongside neighbouring roof ids 76780 and 76785, so it was a coin-store stock item in that build; the file carries no price.", "source": "refs:Sanctuary-PC2009-20261009/src/Resources/CoinStoreItems.json:8307-8320"},
  {"claim": "The wiki Items page lists roofs Dragonscale Roofing Shingles and Natural Wooden Roofing but not Heart-shaped Roofing Shingles, so no wiki price or category is confirmed for this item.", "source": "wiki:Items (page:ns0 Items, Roofs section)"},
  {"claim": "The first-pass 'event' guess has no support in the pack, the client text, or the wiki; the only store-type evidence is the coin-store row above.", "source": "lookup client/wiki/articles for 'Roofing Shingles' (no event, drop, or quest text)"}
 ],
 "confidence": 0.35,
 "open": [
  "Price unknown: Legacy Cost 10000 is the client's cost field, but no store row in the repo or Legacy CoinStoreItems sells it, so no coin price is claimed. Confirm the real price from a wiki Coin Shop or Marketplace page or the 2009 store price list.",
  "Coin store source rests only on the 2009 PC CoinStoreItems row (no price, no vendor name). Confirm which coin vendor or store category stocked it.",
  "The 'live: yes / event' first-pass tag is unsupported; live status and whether it was retired are unknown (retired: null).",
  "No wiki article, video frame, or article fact names this item. The client text 'A heart-thatched roofing that makes every day sweet.' gives no source.",
  "Store row item_id 19584 in stores.json belongs to Pro Ninja Cowl (locale-id collision with this item's name id). Fix or flag that row before any join by name id."
 ]}
