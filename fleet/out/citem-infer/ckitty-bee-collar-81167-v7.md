<!-- fleet job=citem-infer id=ckitty-bee-collar-81167-v7 status=done turns=1 usd=0.0017 tokens(read,write,in,out)=[0, 6436, 4, 1766] model=claude-haiku-5-5 -->
# Kitty Bee Collar

{"item": {"name": "Kitty Bee Collar", "locale_id": 81167, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Marketing item 26389 (one of the collar's definitions) listed in the coin store under CategoryId 6. Membership-only listing; no per-item price found.", "where": "Coin Shop (category 6)", "price": null, "currency": null, "source": "refs:FreeRealms-Legacy/src/Resources/CoinStoreItems.json:41425-41428 (Id 26389, CategoryId 6)"},
  {"type": "other", "detail": "Component of the 'Kitty Bee Outfit' store bundle (Bundle Id 3086, NameId 72326), alongside marketing items 24604, 25619, 25514. Not a standalone collar sale.", "where": "StoreId 1 bundle", "price": null, "currency": null, "source": "refs:Lxzxrus-Free-Realms-Server/src/Resources/StoreBundles.json:7093-7139"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Kitty Bee Collar' (locale 81167); item description line 'This is a Kitty Bee Collar item.' (locale 150304). Client definition description string: 'There's a lot of buzz about this collar.'", "source": "locale:81167; locale:150304; client definition"},
  {"claim": "Set siblings: Kitty Bee Outfit 72326, Suit 79557, Boots 80397, Antennae 80502.", "source": "locale:72326; locale:79557; locale:80397; locale:80502"},
  {"claim": "Coin store rows 15697-15711 (category 6) all carry purchase 270, member 243, sell 27 with identical tags, so the 270/243 price is a category default, not a per-item price for this collar.", "source": "repo:prototype/osfr-tools/data/content/stores.json:4018-4029"},
  {"claim": "Kitty Bee Outfit bundle (Id 3086, StoreId 1, Status 1) contains MarketingItemId 26389; its price fields are placeholder 1 with an unmapped CurrencyType 1.", "source": "refs:Lxzxrus-Free-Realms-Server/src/Resources/StoreBundles.json:7093-7139"},
  {"claim": "CoinStoreItems lists Id 26389 under CategoryId 6 (membership, no price).", "source": "refs:FreeRealms-Legacy/src/Resources/CoinStoreItems.json:41425-41428"},
  {"claim": "Lookup of client, wiki, articles and video for 'Kitty Bee' finds only the client name and description lines; no wiki page, article, video, quest, drop or event names the collar.", "source": "lookup (client, wiki) 'Kitty Bee'"}
 ],
 "confidence": 0.3,
 "open": [
  "No confirmed per-item coin price. The 270 purchase / 243 member / 27 sell values are a category-6 default shared by about 15 rows (stores.json 15697-15711), so they were dropped as a source price. Needs a real coin-shop transaction or wiki price.",
  "Bundle 3086 (Kitty Bee Outfit) price is an unmapped placeholder (1, CurrencyType 1). Real bundle price and currency needed before wiring the outfit as a source. Whether the collar is sold alone is not evidenced.",
  "Retirement and current availability unknown. The 2040 bundle expiry is placeholder-like and does not prove availability. Live status unsure.",
  "Kind 'clothing' rests on slot 6, class 61 and the set name, not a wiki page.",
  "Other definitions of the 36 (26379-26388, 26390 and others) were not all checked against store rows.",
  "Wireable: false. No confirmed price or standalone source."
 ]}
