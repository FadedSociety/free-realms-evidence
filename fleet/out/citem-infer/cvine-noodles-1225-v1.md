<!-- fleet job=citem-infer id=cvine-noodles-1225-v1 status=done turns=5 usd=0.0049 tokens(read,write,in,out)=[50346, 19361, 12, 4018] model=claude-haiku-5-5 -->
# Vine Noodles

{"item": {"name": "Vine Noodles", "locale_id": 1225, "kind": "consumable"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash bundle 'Vine Noodles' (bundle Id 2267, NameId 1225): 3 units of game item 627, keyed to MarketingItemId 4066; Price 1, CurrencyType 1, Status 1, store 1, category group 42; launch 2009-04-22, expire 2040-08-15", "where": "Station Cash marketplace (store 1)", "price": "1 (CurrencyType 1; the Price field is not a readable price, see open)", "currency": "station_cash", "source": "refs:Sanctuary-main-20261019/src/Resources/StoreBundles.json:873-900"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition id 4066, NameId 1225, DescriptionId 3149, Class 9, SingleUse true, NoSale true, NoTrade true, Cost 180 (client cost field, not a coin store price), ActivatableAbilityId 3066", "source": "refs:Sanctuary-main-20261019/src/Resources/ClientItemDefinitions.json:74276-74297"},
  {"claim": "Client name 'Vine Noodles' is locale:1225; description (locale 3149 per DescriptionId) says eating it changes the player into a vine golem wolf for thirty minutes", "source": "locale:1225; pack client_definition description"},
  {"claim": "Same bundle family as other troll/veggie foods (Troll Porridge, Shambler Cake, Veggie Surprise) which all have StoreBundles entries in the same file", "source": "refs:Sanctuary-main-20261019/src/Resources/StoreBundles.json:31219, 31369, 31429"},
  {"claim": "Wiki Items list page includes '[Vine] [Noodles]' among food items, but the snippet gives no price, source or sale detail", "source": "wiki page:ns0 Items"},
  {"claim": "No coin store price: repo stores.json has no entry for item 4066, and the client definition has no coin store price", "source": "repo:data/content/stores.json (no item 4066 match)"},
  {"claim": "Client definitions for Illusion Food - Fungal Vinegolem Wolf/Bear are the sibling items in the same cluster (locale 1227/1228)", "source": "locale:1227, locale:1228"}
 ],
 "confidence": 0.4,
 "open": [
  "Currency: CurrencyType 1 and Price 1 in the bundle are not decoded here. The bundle is in the Station Cash store (store 1), so station_cash is inferred, but the actual price is unverified. No wiki price found.",
  "Quantity/ID mismatch: the bundle grants GameItemId 627 (quantity 3), while the client definition is 4066 and MarketingItemId is 4066. Confirm that 627 is the same food or a different item before the rebuild uses this bundle.",
  "Live status: the bundle expires 2040, so the data does not show retirement. The wiki has no page for this item, so live is 'unsure'.",
  "Wiki Items list places Vine Noodles in the food group above the 'Members Only' heading. Membership status is not confirmed.",
  "No quest reward, enemy drop, event, prize wheel, crafting, or coin vendor source found in the pack or repo searches. Vendor, drop, and quest searches on 4066 and the item name returned nothing.",
  "Lookup of the wiki and articles for the name returned only the Items list, with no other pages, images, article facts, or video frames."
 ]}
