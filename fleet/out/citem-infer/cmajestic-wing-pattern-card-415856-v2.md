<!-- fleet job=citem-infer id=cmajestic-wing-pattern-card-415856-v2 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[5766, 8146, 6, 1657] model=claude-haiku-5-5 -->
# Majestic Wing Pattern Card

{"item": {"name": "Majestic Wing Pattern Card", "locale_id": 415856, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store listing for Majestic Wing Pattern Card (definition 69002), store category 146, at 270 coins (243 coins for members, 10% member discount). Listing is flagged no_sale: true, so a current sale is not confirmed.", "where": "Coin store (category 146)", "price": "270 coins (member price 243 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:14745 (item 69002); corroborated by FreeRealms-Legacy/src/Resources/CoinStoreItems.json:66580 (Id 69002, CategoryId 146) and client coin_store_prices [270]"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Majestic Wing Pattern Card', locale 415856; description says the wings show nobility and cannot be used by Humans; one definition (69002), slot 7, class 1", "source": "locale:415856"},
  {"claim": "Store record for item 69002: category 146, purchase 270 coins, member discount 10%, member price 243 coins, sell_price null, no_sale true", "source": "repo:prototype/osfr-tools/data/content/stores.json:14745"},
  {"claim": "Independent coin store listing for 69002 in category 146", "source": "FreeRealms-Legacy/src/Resources/CoinStoreItems.json:66580"},
  {"claim": "Client coin store price for 69002 is 270", "source": "client definition coin_store_prices [270] in pack"},
  {"claim": "Sibling wing pattern cards 68991-69008 carry the same store row (270 / 243, no_sale true)", "source": "repo:prototype/osfr-tools/data/content/stores.json:14738-14750"},
  {"claim": "No wiki page, wiki image, article fact or video frame names this card", "source": "lookup of 'Majestic Wing Pattern Card' across wiki, articles, video: no matches"}
 ],
 "confidence": 0.4,
 "open": [
  "no_sale: true on stores.json:14745 (and on all sibling rows) is undocumented. It may mean the card is no longer sold, or that it is listed but not resold. The coin store sale is therefore not confirmed as live.",
  "Retirement status is unknown. No retirement source was found, so retired is null and live is 'unsure'.",
  "The wiki 'Coin Shop' category is not confirmed for this card; no wiki page covers it.",
  "The store source_tags (L1, L2, L3, L4, R2) are undocumented and are not used as evidence of any source.",
  "The first-pass tag 'marketplace' is not supported: no Station Cash Marketplace price or category was found.",
  "Which wing pattern the card applies is not stated in the pack."
 ]}
