<!-- fleet job=citem-infer id=carbor-buttercake-265-v2 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[5467, 11751, 6, 2053] model=claude-haiku-5-5 -->
# Arbor Buttercake

{"item": {"name": "Arbor Buttercake", "locale_id": 265, "kind": "consumable"},
 "sources": [
  {"type": "marketplace", "detail": "Marketplace bundle 'Arbor Buttercake' (StoreBundles Id 2207, NameId 265, MarketingItemId 2970): 3 units of GameItemId 570 per purchase", "where": "Marketplace (StoreId 1, CategoryGroupId 42)", "price": null, "currency": null, "source": "refs: FreeRealms-Legacy/src/Resources/StoreBundles.json lines 243-272 (also Sanctuary/src/Resources/StoreBundles.json); notes/Build Guides/Gameplay/Coin Store and Purchases.md (Marketplace is the Station Cash store)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is 'Arbor Buttercake' at locale 265; description says eating it causes leaves to fall around the player for thirty minutes.", "source": "locale:265; client definition id 2970"},
  {"claim": "Client item definition 2970: Type 1, Class 9, Cost 180, NoSale, NoTrade, SingleUse, CategoryId 10, ActivatableAbilityId 1968.", "source": "refs: FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json lines 55304-55326"},
  {"claim": "A Marketplace bundle sells 3 of GameItemId 570 under MarketingItemId 2970, named by NameId 265, StoreId 1. Bundle has CurrencyType 1, Price 1, AltCurrencyPrice 1, MemberDiscount 10, Launch 2009-04-22, Expire 2040-08-15 (open-ended placeholder).", "source": "refs: FreeRealms-Legacy/src/Resources/StoreBundles.json lines 243-272"},
  {"claim": "The wiki Items page lists '[Arbor] [Buttercake]' in the Food and Drink section beside Scrumptious Soup, Frosty Flakes, Pixiedust Pie and Hot Sauce Buns; no price or source given.", "source": "wiki page: Items (lookup result)"},
  {"claim": "No coin store row for item 2970 in data/content/stores.json, so no coin vendor sale is confirmed.", "source": "repo: prototype/osfr-tools/data/content/stores.json"}
 ],
 "confidence": 0.3,
 "open": [
  "Price is unknown. The bundle's Price 1 / CurrencyType 1 does not map to an amount; no source gives a Station Cash figure. Currency is left null: the Marketplace store is Station Cash in the repo notes, but CurrencyType 1 is not explicitly mapped to Station Cash by any source reviewed.",
  "ClientItemDefinitions Cost 180 is not a coin store price (no stores.json row) and is not used as a source.",
  "No quest reward, enemy drop, event, prize-wheel or crafting source names this item. The 'leaves fall' effect shows no seasonal or event tie, so the first-pass 'event' guess is not supported.",
  "Retired status is null: the 2040 expiry is a placeholder, and no source says when the bundle left the Marketplace.",
  "Live status is unsure: the bundle is in shipped data, but no source confirms it was on sale at shutdown.",
  "Critique fixes applied: the source is labelled as a Marketplace bundle rather than asserting Station Cash currency; price and currency left null; wiki evidence kept as existence/category only."
 ]}
