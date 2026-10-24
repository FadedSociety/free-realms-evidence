<!-- fleet job=citem-infer id=cdoggy-western-bandana-12634-v1 status=done turns=5 usd=0.0046 tokens(read,write,in,out)=[48134, 17648, 12, 3873] model=claude-haiku-5-5 -->
# Doggy Western Bandana

{"item": {"name": "Doggy Western Bandana", "locale_id": 12634, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop sale of the Doggy Western Bandana pet clothing (store item 6063, tint group 1); member price 243 coins (10% member discount), sell-back 27 coins", "where": "Coin Shop", "price": "270 coins (member 243 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:1604 (item_id 6063, purchase_price_coins 270); client definition coin_store_prices [270]"},
  {"type": "coin_shop", "detail": "Second store row for the same item (store item 6093, tint group 1, marketing item 6093) at the same price; no resale", "where": "Coin Shop", "price": "270 coins (member 243 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:1634 (item_id 6093, purchase_price_coins 270, no_sale true)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item name 'Doggy Western Bandana' is locale 12634, with description line locale 150220 'This is a Doggy Western Bandana item.'", "source": "locale:12634; locale:150220"},
  {"claim": "Client definition: 35 variants, 12 definition ids listed, slot 6, item class 31, model pet_dog_<descriptor>_shoulders_bandana.adr; a pet dog shoulder accessor", "source": "quest-lines/citem-packs.json cdoggy-western-bandana-12634 (client definition)"},
  {"claim": "Store bundle 'Doggy Western Bandana' (Id 2334, NameId 12634, GameItemId 812, MarketingItemId 6093, Status 1, IsTintable, launch 2009-04-22, expire 2040-08-15, StoreId 1, CategoryGroupId 84) is present in the legacy store data", "source": "refs FreeRealms-Legacy/src/Resources/StoreBundles.json:1767-1797"},
  {"claim": "Sibling pieces of the same 'Doggy Western' set (Shirt, Boots, Hat) appear in the same legacy store bundle list, so the bandana is one of a set sold together", "source": "refs FreeRealms-Legacy/src/Resources/StoreBundles.json:1086, 1396, 1644 (Comments); locale:150571 'The bandana for the doggy western costume.'"},
  {"claim": "Not listed in the Sanctuary pet clothing merchant Brent's stock (Kitty/Doggy sweaters, pirate and leather collars only)", "source": "notes/Build Guides/Content/NPCs/NPCs - Sanctuary.md:86; repo prototype/osfr-tools/data/content/npcs/sanctuary.json:8893"}
 ],
 "confidence": 0.6,
 "open": [
  "Only the Coin Shop source is evidenced. No wiki page, article, video, or quest/drop answer names the bandana, so no other sources are claimed.",
  "The legacy StoreBundles entry shows CurrencyType 1 with Price 1 and AltCurrencyPrice 1, and the repo gives 270 coins. The currency mapping for CurrencyType 1 was not confirmed, so the 270-coin price rests on the repo stores.json row.",
  "Store rows 6063 and 6093 both sit at 270 coins. Whether the two rows are separate listings (one sale, one bundle) is unresolved.",
  "The 2040 expiry in the legacy bundle is not evidence of a current sale. Live status rests on the first-pass tag and the Status 1 field, which is weak evidence.",
  "The 'Crimson Doggy Western Outfit' (locale 37926/37927, 'Bandana, Shirt, Boots, Hat') is a separate bundled outfit and is not evidence for this single item's price or source.",
  "Kind is set to clothing (pet accessory, slot 6, pet_dog shoulders model). The first pass said 'pet', but that reads as the pet itself, not this item."
 ]}
