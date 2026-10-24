<!-- fleet job=citem-infer id=cbleeding-heart-t-shirt-8991-v1 status=done turns=4 usd=0.0029 tokens(read,write,in,out)=[18739, 10850, 10, 2720] model=claude-haiku-5-5 -->
# Bleeding Heart T-Shirt

{"item": {"name": "Bleeding Heart T-Shirt", "locale_id": 8991, "kind": "clothing"},
 "sources": [
  {"type": "prize_wheel", "detail": "Gifting Basket (2011 Festival of Hearts) random reward; the basket's reward list names the Bleeding Heart T-Shirt in all 22 colors", "where": "Station Cash Marketplace (basket was sold there)", "price": "Gifting Basket sold for Station Cash (price not stated in the pack)", "currency": "station_cash", "source": "wiki: Gifting Basket (reward list: '[Bleeding Heart] T-Shirt, in all 22 colors'); wiki: Gifting Basket ('previously sold through the Station Cash Marketplace during the 2011 Festival of Hearts')"},
  {"type": "vendor", "detail": "Coin store entry, tint group 1 (definition 17881)", "where": "Coin store, category 103 (clothing)", "price": "100 coins (member price 90)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 17881 (line 6972)"},
  {"type": "vendor", "detail": "Coin store entry, tint group 2 (definition 76827)", "where": "Coin store, category 103 (clothing)", "price": "375 coins (member price 337)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 76827 (line 16339)"}
 ],
 "retired": true,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name 'Bleeding Heart T-Shirt' and description 'This heart pumps love, not blood.'", "source": "locale:8991, locale:8997"},
  {"claim": "Two client definitions (17881, 76827) with the same name, slot 3 (chest), class 1; coin store prices 100 and 375", "source": "client definition; repo:prototype/osfr-tools/data/content/stores.json items 17881 and 76827"},
  {"claim": "Gifting Basket was a Festival of Hearts 2011 Station Cash Marketplace item whose rewards include the Bleeding Heart T-Shirt in all 22 colors; it can no longer be acquired", "source": "wiki: Gifting Basket; wiki: Festival of Hearts (Lovely T-Shirt also only via Gifting Basket)"},
  {"claim": "Same festival set (Deathly Love, Friendless, Kisses, Lovely, No Love T-shirts) sits next to it in client text, consistent with Festival of Hearts issue", "source": "locale:8989-8996 (client cluster)"},
  {"claim": "Bleeding Heart T-Shirt shows in gameplay video frames (equipped/chest slot)", "source": "video:6mmERh2D8yc/00236.jpg; video:143KUZ0jREc/00234.jpg; video:98uNKkDRvQU/00290.jpg"}
 ],
 "confidence": 0.6,
 "open": [
  "The coin store entries (100 and 375 coins) are in stores.json but no wiki page or vendor NPC confirms a coin-vendor sale; the stores.json tags (L1, L2, L4, R2, T633, R1) do not name a vendor. Verify whether the coin-store listing was live or only a Gifting Basket reward price.",
  "The wiki names the shirt only as a Gifting Basket reward list entry; no wiki page gives the basket's Station Cash price or the drop odds for this shirt.",
  "No wiki page states the exact retirement date for the shirt; retirement is inferred from the basket being unavailable since 2011 Festival of Hearts.",
  "Festival of Hearts 2014 also ran; not checked whether the shirt was re-offered then."
 ]}
