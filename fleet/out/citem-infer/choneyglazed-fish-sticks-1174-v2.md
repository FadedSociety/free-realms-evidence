<!-- fleet job=citem-infer id=choneyglazed-fish-sticks-1174-v2 status=done turns=4 usd=0.0045 tokens(read,write,in,out)=[40985, 20853, 10, 3040] model=claude-haiku-5-5 -->
# Honeyglazed Fish Sticks

{"item": {"name": "Honeyglazed Fish Sticks", "locale_id": 1174, "kind": "consumable"},
 "sources": [{"type": "marketplace", "detail": "Store bundle 100031 (NameId 1174), one item (GameItemId 4015 x3) in the Station Cash-style store listing (StoreId 1, CategoryGroupId 42); a listing in the store data, not a coin vendor sale", "where": "Station Cash Marketplace (StoreId 1; mapping to the Marketplace is inferred, not confirmed)", "price": "1 (Price and MembersOnlyPrice both 1; AltCurrencyPrice 1); no currency name in the data", "currency": null, "source": "refs:Sanctuary/src/Resources/StoreBundles.json:39955-39984 (Id 100031); same bundle in refs:Lxzxrus-Free-Realms-Server/src/Resources/StoreBundles.json:39906-39911 and refs:FreeRealms-Legacy/src/Resources/StoreBundles.json:39644-39649"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client text: locale:1174 is the item name 'Honeyglazed Fish Sticks', in a food cluster with locale 1169-1179.", "source": "locale:1174; locale:1169-1179"},
  {"claim": "Client definition: definition 4015, class 9, slot 0, no models, no coin store price in the pack. Description: eating it changes the player into a male bixie warrior for thirty minutes.", "source": "client definition in evidence pack; refs:Sanctuary/src/Resources/ClientItemDefinitions.json:73132 (Comment 'Honeyglazed Fish Sticks')"},
  {"claim": "Store bundle 100031 has NameId 1174, Comment 'Honeyglazed Fish Sticks', one entry GameItemId 4015 with Quantity 3, Price 1, MembersOnlyPrice 1, AltCurrencyPrice 1, CurrencyType 1, Status 1, StoreId 1, CategoryGroupId 42, LaunchTime 2009-04-22, ExpireTime 2040-08-15, DescriptionId 2726.", "source": "refs:Sanctuary/src/Resources/StoreBundles.json:39955-39984"},
  {"claim": "The same bundle appears in the other community server dumps (Lxzxrus and FreeRealms-Legacy), so it is not a one-off.", "source": "refs:Lxzxrus-Free-Realms-Server/src/Resources/StoreBundles.json:39906-39911; refs:FreeRealms-Legacy/src/Resources/StoreBundles.json:39644-39649"},
  {"claim": "Sibling food bundles in the same block (100029 Honey Fruit Stick, 100030 Honey Hex Cereal) use the same price, currency, StoreId and launch date, so Honeyglazed Fish Sticks is one of a set of food listings sold together.", "source": "refs:Sanctuary/src/Resources/StoreBundles.json:39900-39954"},
  {"claim": "All 1,267 StoreBundles rows use CurrencyType 1, and the repo's Coin Shop research says those rows are not mapped as coin prices. The currency for this bundle is therefore not established.", "source": "repo:notes/Research/Coin Shop.md:32"},
  {"claim": "No wiki page, article, video frame, quest reward, drop or coin-vendor stock names this item. The repo's stores.json has no entry for item 4015.", "source": "lookup (client, wiki, articles, video) returned no match for 'Honeyglazed Fish Sticks' or sibling food names; repo search for '4015' in stores.json"}
 ],
 "confidence": 0.45,
 "open": [
  "Currency is unresolved. CurrencyType 1 is not mapped to Station Cash or coins in the repo, so the price '1' has no confirmed unit. Calling it a Station Cash Marketplace listing is inferred from StoreId 1 and the store-bundle format, not from a wiki category.",
  "Live status is unsure. The bundle has Status 1 and ExpireTime 2040, but the data is a community dump, and no wiki page confirms the listing was on sale in the live game or when it was retired.",
  "No wiki 'SC Marketplace' or 'Coin Shop' category was found for this item in the lookup, so the marketplace source rests on the store data alone.",
  "Quantity 3 per purchase is from the bundle entry; the price per purchase is unclear from the data alone.",
  "The description's bixie-warrior transformation is the item's in-game effect only; it does not establish a source.",
  "Not wireable yet until the currency and the store mapping are confirmed."
 ]}
