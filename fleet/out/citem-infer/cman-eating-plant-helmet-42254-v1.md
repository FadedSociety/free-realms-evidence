<!-- fleet job=citem-infer id=cman-eating-plant-helmet-42254-v1 status=done turns=6 usd=0.0048 tokens(read,write,in,out)=[43135, 18349, 14, 4051] model=claude-haiku-5-5 -->
# Man-Eating Plant Helmet

{"item": {"name": "Man-Eating Plant Helmet", "locale_id": 42254, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, tint group 1 (definition 10878), purchase price 9453 coins; member price 8507 coins (10% discount). Vendor NPC not identified in the repo data.", "where": null, "price": "9453 coins (member 8507 coins)", "currency": "coins", "source": "repo:data/content/stores.json item 10878 (category 101, tint_group_id 1, no_sale true)"},
  {"type": "vendor", "detail": "Coin store sale, tint group 2 (definition 10919), purchase price 1761 coins; member price 1584 coins. Vendor NPC not identified in the repo data.", "where": null, "price": "1761 coins (member 1584 coins)", "currency": "coins", "source": "repo:data/content/stores.json item 10919 (category 101, tint_group_id 2, no_sale true)"},
  {"type": "vendor", "detail": "Coin store sale, tint group 3 (definition 76726), purchase price 9453 coins; member price 8507 coins. Vendor NPC not identified in the repo data.", "where": null, "price": "9453 coins (member 8507 coins)", "currency": "coins", "source": "repo:data/content/stores.json item 76726 (category 101, tint_group_id 3, no_sale true)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Man-Eating Plant Helmet' is locale 42254, item-type text, with description 'Feeding instructions not included.' (locale:42337 is the same line on a sibling item, so the description is shared text).", "source": "locale:42254"},
  {"claim": "Three item definitions (10878, 10919, 76726) share the name and map to three tint groups (1, 2, 3) in the coin store data, each with a coin purchase price.", "source": "repo:data/content/stores.json items 10878, 10919, 76726"},
  {"claim": "Store records for all three variants carry no_sale true and source tags L1, L2, L4, R2, L3, which show they are store-sourced entries rather than drops.", "source": "repo:data/content/stores.json items 10878, 10919, 76726"},
  {"claim": "The placeholder locale 150514 ('This is a Man-Eating Plant Helmet.') is generic filler text and is not evidence of a source.", "source": "locale:150514"},
  {"claim": "Sibling items in the same locale block (Cyborg Eye, Ghost Driver Helmet, Super Happy Fun Sushi Apron, Chatty Suit) are wiki-documented as Station Cash Marketplace or event items, but no wiki page or source names this helmet, so the set grouping does not establish its source.", "source": "lookup client/wiki: Cyborg Eye, Chatty Suit"},
  {"claim": "No wiki page, article, or video frame names the Man-Eating Plant Helmet; the wiki's Chatty Suit and Cyborg Eye pages give Station Cash Marketplace prices but their price figures are blank in the extracted text.", "source": "lookup wiki 'Man-Eating Plant Helmet' (no hits)"}
 ],
 "confidence": 0.45,
 "open": [
  "The vendor NPC or shop that sells the three coin store entries is not named in the repo. Stores.json gives category 101 and prices but no vendor, so the sources are typed 'vendor' but the detail is only the store record.",
  "Coin store prices (9453 and 1761 coins) come from stores.json and were not confirmed by any wiki page, so they need a live check.",
  "No wiki page exists for this helmet, and the Station Cash Marketplace or Coin Shop category is not confirmed. The 'coin_store_prices' list in the pack gave 1761 and 9453 as prices, and the store file maps them to item ids 10919 and 10878 / 76726.",
  "Retired status is unknown; the store records carry no sale-end date, and no source says it was retired or still sold.",
  "Live status is 'unsure': store data has the items, but there is no wiki or article confirmation of current availability.",
  "The pack's cluster items (Chatty Suit, Cyborg Eye) are wiki-documented as SC Marketplace or event items; if the helmet shares that source it needs a wiki or article citation before it is listed."
 ]}
