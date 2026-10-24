<!-- fleet job=citem-infer id=coxidized-hair-color-card-414060-v3 status=done turns=4 usd=0.0033 tokens(read,write,in,out)=[30212, 12822, 10, 2775] model=claude-haiku-5-5 -->
# Oxidized Hair Color Card

{"item": {"name": "Oxidized Hair Color Card", "locale_id": 414060, "kind": "consumable"},
 "sources": [
  {"type": "coin_shop", "detail": "Hair color style card coin-store catalog listing (stores.json category 142). Catalog price only: row is no_sale:true with sell_price_coins null, so no confirmed live coin sale.", "where": "Coin store, style/hair color card category 142", "price": "180 coins (member price 162 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 35955 (line 7888); sibling rows 35950-35962 carry identical values (lines 7883-7895)"},
  {"type": "marketplace", "detail": "Station Cash Marketplace store bundle 'Oxidized Hair Color Card' (Id 3473, NameId 414060, MarketingItemId 35955, GameItemId 3033, Quantity 1). Launch 2009-11-29, Status 1. CurrencyType 1 and Price 1 are unresolved: the bundle does not say the price is coins or Station Cash, and the figure cannot be read as a real price.", "where": "Station Cash Marketplace (store id 1, category group 126)", "price": "unresolved (bundle Price 1, AltCurrencyPrice 1)", "currency": null, "source": "refs: Sanctuary-PC2009-20261009/src/Resources/StoreBundles.json lines 10770-10798 (same record in Sanctuary-PS3 and TCG-Files copies at line 10781)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 414060 is 'Oxidized Hair Color Card'; description 'This style card allows you to change your hair color.'", "source": "locale:414060"},
  {"claim": "Store row item 35955: category 142, purchase 180 coins, member 162, sell_price null, no_sale true", "source": "repo:prototype/osfr-tools/data/content/stores.json line 7888"},
  {"claim": "Sibling rows 35950-35962 in category 142 carry the same 180/162 values; the batch shares source_tags [L1,L2,L4,R2,L3,L3], which are not explained in the repo and are not used here", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 7883-7895"},
  {"claim": "StoreBundles record Id 3473 is a launch listing for MarketingItemId 35955 with Comment 'Oxidized Hair Color Card', LaunchTime 2009-11-29, ExpireTime 2040-08-15 (not evidence of retirement), CurrencyType 1, Price 1, MembersOnlyPrice 1", "source": "repo: Sanctuary-PC2009-20261009/src/Resources/StoreBundles.json lines 10770-10798"},
  {"claim": "Oxidized appears in the client text table only as the item name and as tint-type strings; no client line ties the card to a quest, drop, or event", "source": "locale:414060; locale:414055-414065 cluster"},
  {"claim": "No wiki page, article, video frame, vendor stock row, or other answer names this card. The Super Spooktacular hair-card set does not include Oxidized.", "source": "lookup wiki/articles/client: no hits beyond locale:414060; wiki: Super Spooktacular"}
 ],
 "confidence": 0.35,
 "open": [
  "Coin price 180 (member 162) is a no_sale catalog row, not proof of a live coin-shop sale. Whether it was ever sold for coins is unverified.",
  "The legacy StoreBundles record Price 1 / CurrencyType 1 conflicts with the 180-coin catalog row and is unresolved. Its currency meaning (coins vs Station Cash) is not stated in the repo. The earlier 'placeholder' dismissal had no source and is withdrawn.",
  "Retirement is not established. ExpireTime 2040 is a data default, not a retirement date. Live status stays unsure.",
  "source_tags [L1,L2,L4,R2,L3,L3] on the category 142 rows are unexplained; they may encode acquisition type but this was not verified.",
  "Definition 68822 (second of two definitions sharing this name) was not checked; it may be a tint or a separate item with its own price.",
  "The first-pass 'vendor' guess has no vendor_stock row and is not used."
 ]}
