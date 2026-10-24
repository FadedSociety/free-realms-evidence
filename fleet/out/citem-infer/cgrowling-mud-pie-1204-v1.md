<!-- fleet job=citem-infer id=cgrowling-mud-pie-1204-v1 status=done turns=6 usd=0.0060 tokens(read,write,in,out)=[70695, 26001, 14, 4091] model=claude-haiku-5-5 -->
# Growling Mud Pie

{"item": {"name": "Growling Mud Pie", "locale_id": 1204, "kind": "consumable"},
 "sources": [{"type": "marketplace", "detail": "Station Cash Marketplace bundle Id 2253 'Growling Mud Pie' (NameId 1204, DescriptionId 3133), MarketingItemId 4045 = this item's definition, GameItemId 613, Quantity 3 per purchase, MemberDiscount 10%", "where": "Station Cash Marketplace (StoreId 1, CategoryGroupId not a coin vendor)", "price": "unknown: the bundle Price and AltCurrencyPrice fields are placeholder 1s in the store file", "currency": "station_cash", "source": "FreeRealms-Legacy/src/Resources/StoreBundles.json lines 753-775 (Id 2253; same MarketingItemId 4045 in Sanctuary/src/Resources/StoreBundles.json:764 and other snapshots); currency mapping CurrencyType 1 = Station Cash per Sanctuary-main-20261019/src/Sanctuary.Game/Helpers/WelcomeScreenHelper.cs:14 (StationCashCurrencyType = 1)"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item definition: Id 4045, NameId 1204, DescriptionId 3133, Class 9, SingleUse true, NoTrade true, Cost 180 (an item-definition cost field, not a store price)", "source": "FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json lines 73812-73825 (Comment 'Growling Mud Pie')"},
  {"claim": "Name and description: 'Growling Mud Pie'; 'Eating this food will change the player into a small floppy eared dog for thirty minutes.'", "source": "locale:1204; locale:3133"},
  {"claim": "A Station Cash bundle sells this item: Id 2253, launch 2009-04-22, expire 2040-08-15, Status 1, quantity 3, MarketingItemId 4045", "source": "FreeRealms-Legacy/src/Resources/StoreBundles.json lines 753-775"},
  {"claim": "Store bundle currency: CurrencyType 1 is Station Cash (same convention used for other SC Marketplace rows)", "source": "Sanctuary-main-20261019/src/Sanctuary.Game/Helpers/WelcomeScreenHelper.cs:14; the repo does not pin the enum, so this is inferred"},
  {"claim": "Item appears in the wiki Items index as 'Growling [Mud] [Pie]' alongside the same Illusion Food / food-set items (Bark Berries, Bitter Cherry Split, Woof Fondue, Fetching Some Ice Cream, Sharking Shaved Ice)", "source": "wiki page:ns0 Items (lookup result); the index gives no price, category or source"},
  {"claim": "Client cluster: the 1199-1209 'Illusion Food' / food-set family (locale 1199-1209) sits together in the client text table", "source": "locale:1199 through locale:1209"},
  {"claim": "No coin store price and no coin vendor stock for this item", "source": "coin_store_prices is empty in the pack; no vendor_stock rows; repo stores.json has no item 4045 row"}
 ],
 "confidence": 0.5,
 "open": [
  "Station Cash price is unknown: the bundle's Price=1 and AltCurrencyPrice=1 are placeholders, and no wiki price or dated SC listing was found for this item. Do not invent a price.",
  "Live status is unsure: the bundle is Status 1 with a 2040 expiry, but nothing confirms it is still on sale at revival launch.",
  "The first-pass tag said 'vendor'. No coin vendor sells it (no vendor_stock, no coin store price, no repo stores.json row), so the vendor guess is not supported.",
  "No wiki article, video, article fact or quest reward names this item. The wiki Items index entry has no category, so 'SC Marketplace' is not confirmed as a wiki category for it.",
  "Whether the item is a bundle item sold in quantity 3 for one purchase is from the bundle Quantity field; the wiki may state a different unit."
 ]}
