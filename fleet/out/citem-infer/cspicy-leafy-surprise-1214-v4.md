<!-- fleet job=citem-infer id=cspicy-leafy-surprise-1214-v4 status=done turns=3 usd=0.0021 tokens(read,write,in,out)=[12998, 7462, 8, 2090] model=claude-haiku-5-5 -->
# Spicy Leafy Surprise

{"item": {"name": "Spicy Leafy Surprise", "locale_id": 1214, "kind": "consumable"},
 "sources": [{"type": "marketplace", "detail": "Station Cash store bundle 100077 (Comment 'Spicy Leafy Surprise', NameId 1214, DescriptionId 3128): one entry, GameItemId 4055 x3 per purchase", "where": "Station Cash store (StoreId 1)", "price": null, "currency": "station_cash", "source": "refs FreeRealms-Legacy/src/Resources/StoreBundles.json:41007-41036 (re-read this pass); CurrencyType 1 = Station Cash is not verified against an enum in this pass"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item 4055 is named 'Spicy Leafy Surprise' at locale:1214.", "source": "locale:1214"},
  {"claim": "Description: 'Eating this food will change the player into a male robgoblin mage for thirty minutes.' Confirmed in the client text table at DescriptionId 3128.", "source": "locale:3128"},
  {"claim": "Store bundle 100077 sells GameItemId 4055 (quantity 3) under NameId 1214, StoreId 1, Status 1, CurrencyType 1, LaunchTime 2009-04-22T04:00Z, ExpireTime 2040-08-15T07:00Z, DiscountType 306, MemberDiscount 10.", "source": "refs FreeRealms-Legacy/src/Resources/StoreBundles.json:41007-41036"},
  {"claim": "Price 1, MembersOnlyPrice 1 and AltCurrencyPrice 1 are placeholder-looking values; no real price is evidenced.", "source": "refs FreeRealms-Legacy/src/Resources/StoreBundles.json:41010-41014"},
  {"claim": "The 2040 ExpireTime is far-future and is not evidence of retirement.", "source": "refs FreeRealms-Legacy/src/Resources/StoreBundles.json:41017"},
  {"claim": "Lookup of the item name in wiki, articles and video returned no matches; the only client hit is locale:1214.", "source": "lookup (client, wiki, articles, video)"},
  {"claim": "Earlier claim of a robgoblin-infestation / opening-NPC context is withdrawn: it rested on locale:564218199, which does not exist. No quest, drop or vendor source was found.", "source": "id_check; locale lookup"}
 ],
 "confidence": 0.5,
 "open": [
  "Station Cash price of the 3-pack is unknown. Price, MembersOnlyPrice and AltCurrencyPrice are all 1 in the file, so no real price can be stated. Check a store page or wiki for the price.",
  "CurrencyType 1 = Station Cash is asserted from an earlier critique's reference and is not verified against a client or server enum here.",
  "Whether the bundle was actually sold live, and when it was pulled, is not evidenced. The 2040 ExpireTime is not a retirement date, so retired is null.",
  "Because the only source has no evidenced price, this entry is not wireable with a price yet.",
  "Sibling Illusion Food items (locale 1209, 1213, 1217) and related Spicy foods (1210-1212) were not checked against StoreBundles.json.",
  "Whether the item is obtainable singly outside the 3-pack bundle is not evidenced."
 ]}
