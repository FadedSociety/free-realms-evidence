<!-- fleet job=citem-infer id=cvanilla-dream-hair-color-card-414068-v1 status=done turns=4 usd=0.0023 tokens(read,write,in,out)=[17351, 9621, 10, 1895] model=claude-haiku-5-5 -->
# Vanilla Dream Hair Color Card

{"item": {"name": "Vanilla Dream Hair Color Card", "locale_id": 414068, "kind": "clothing"},
 "sources": [{"type": "coin_shop", "detail": "Coin store sale of item 35963 (style card, hair color; store category 142), 180 coins before member discount; member price 162 coins (10% member discount)", "where": "coin store (category 142)", "price": "180 coins (member price 162 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 35963 (line 7896)"}],
 "retired": null, "live": "unsure",
 "evidence": [{"claim": "Client defines the item as 'Vanilla Dream Hair Color Card' (locale 414068), description 'This style card allows you to change your hair color.', slot 3, class 1; two definitions (35963, 68830).", "source": "locale:414068; client definition"},
  {"claim": "Store data lists item 35963 in category 142 at purchase_price_coins 180, member price 162, no_sale true, source tags L1/L2/L4/R2/L3.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 35963"},
  {"claim": "Sibling hair color cards (Rich Cocoa, Scorched Earth, Charred Oak, Tidal Wave, Super Nova, Sugarplum, Stargazer, Strawberry, Raspberry, Black Licorice; locales 414063-414073) are a single client-text cluster, and the store lists items 35950-35968 at the same 180-coin price in category 142.", "source": "locale:414063-414073; repo:prototype/osfr-tools/data/content/stores.json items 35950-35968"},
  {"claim": "Wiki reports hair color style cards were introduced in a 'Super Spooktacular' update (October 2013) as new Style Cards, but it does not name Vanilla Dream.", "source": "lookup wiki: Super Spooktacular"}],
 "confidence": 0.5,
 "open": ["No wiki page or article names this card, so the coin-shop source rests only on the store data row; the store file has no category name for id 142, so the exact storefront category label is unconfirmed.",
  "Store row says no_sale true; whether it was sold for coins only in a limited window or permanently is not confirmed.",
  "Definition 68830 has no store row; unclear whether it is a separate variant (tint/race) or a duplicate.",
  "The 'Sugarplum'/'Vanilla Dream' cluster may have been part of a membership or promotion release; no source checked this.",
  "Retirement status and live availability unknown; the first-pass 'unsure' stands."]}
