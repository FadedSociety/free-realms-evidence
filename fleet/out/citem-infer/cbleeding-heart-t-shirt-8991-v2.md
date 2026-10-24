<!-- fleet job=citem-infer id=cbleeding-heart-t-shirt-8991-v2 status=done turns=4 usd=0.0026 tokens(read,write,in,out)=[21516, 8702, 10, 2649] model=claude-haiku-5-5 -->
# Bleeding Heart T-Shirt

{"item": {"name": "Bleeding Heart T-Shirt", "locale_id": 8991, "kind": "clothing"},
 "sources": [
  {"type": "event", "detail": "Random reward from the Gifting Basket, a Festival of Hearts 2011 housing item; the basket's reward list names the '[Bleeding Heart] T-Shirt, in all 22 colors'", "where": "Festival of Hearts 2011 (basket opened from the player's lot)", "price": null, "currency": null, "source": "wiki: Gifting Basket (Rewards: '[Bleeding Heart] T-Shirt, in all 22 colors'); wiki: Festival of Hearts"},
  {"type": "marketplace", "detail": "Gifting Basket, the item that carried the reward above, sold through the Station Cash Marketplace", "where": "Station Cash Marketplace", "price": "not stated on the wiki page", "currency": "station_cash", "source": "wiki: Gifting Basket ('previously sold through the Station Cash Marketplace during the 2011 Festival of Hearts event')"},
  {"type": "vendor", "detail": "Coin store entry, tint group 1 (definition 17881); the link from this row to the shirt is by definition id only, no vendor NPC or live sale is confirmed", "where": "Coin store, category 103 (clothing)", "price": "100 coins (member price 90)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 17881 (line 6972)"},
  {"type": "vendor", "detail": "Coin store entry, tint group 2 (definition 76827); same unconfirmed status as above", "where": "Coin store, category 103 (clothing)", "price": "375 coins (member price 337)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 76827 (line 16339)"}
 ],
 "retired": true,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Bleeding Heart T-Shirt' and description 'This heart pumps love, not blood.'", "source": "locale:8991, locale:8997"},
  {"claim": "Wiki Gifting Basket reward list includes '[Bleeding Heart] T-Shirt, in all 22 colors'", "source": "wiki: Gifting Basket"},
  {"claim": "Gifting Basket was previously sold through the Station Cash Marketplace during 2011 Festival of Hearts and can no longer be acquired", "source": "wiki: Gifting Basket; wiki: Festival of Hearts"},
  {"claim": "Two client definitions (17881, 76827) with the same name; slot 3 (chest), class 1; coin store prices 100 and 375", "source": "client definition; repo:prototype/osfr-tools/data/content/stores.json items 17881 and 76827"},
  {"claim": "Same festival set (Deathly Love, Friendless, Kisses, Lovely, No Love T-Shirts) sits in the client text cluster", "source": "locale:8989-8996"},
  {"claim": "Shirt appears on screen in gameplay video frames (chest slot / equipped)", "source": "video:6mmERh2D8yc/00236.jpg; video:143KUZ0jREc/00234.jpg; video:98uNKkDRvQU/00290.jpg"}
 ],
 "confidence": 0.5,
 "open": [
  "The wiki's 22-colour reward covers 22 variants, but only two client definitions (17881, 76827) appear in stores.json. The mapping from the other colours to definitions is unresolved.",
  "The coin store rows (17881 at 100, 76827 at 375) share the generic category-103 source tags L1,L2,L4,R2,T633,R1 with many unrelated shirts. Nothing confirms a live coin-vendor sale of this shirt, so the vendor rows are candidates, not confirmed sources.",
  "No wiki page gives the Gifting Basket's Station Cash price or the drop odds for this shirt.",
  "No wiki page gives an exact retirement date. The 'can no longer be acquired' statement applies to the basket; retirement of the shirt is inferred from it.",
  "Festival of Hearts 2014 ran from February 4, 2014. Not checked whether this shirt was offered again then."
 ]}
