<!-- fleet job=citem-infer id=cpet-cat-shorthair-calico-white-75176-v1 status=done turns=5 usd=0.0036 tokens(read,write,in,out)=[31643, 15434, 12, 2801] model=claude-haiku-5-5 -->
# Pet: Cat: Shorthair: calico_white

{"item": {"name": "Pet: Cat: Shorthair: calico_white", "locale_id": 75176, "kind": "pet"},
 "sources": [{"type": "coin_shop", "detail": "Coin Shop catalogue entry for item 24026 (regular coin price; no named vendor in the data)", "where": "Coin Shop", "price": "540 coins (member price 486 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:6903 (item 24026, purchase_price_coins 540, member_price_coins 486, sell_price_coins 54)"}],
 "retired": null, "live": "unsure",
 "evidence": [{"claim": "Client definition for item 24026 is named 'Pet: Cat: Shorthair: calico_white' (locale 75176), model cat_shorthair.adr, one definition, no tint variants.", "source": "locale:75176; client definition in pack"},
  {"claim": "Coin store catalogue lists item 24026 at 540 coins, member price 486, sell-back 54.", "source": "repo:prototype/osfr-tools/data/content/stores.json:6903"},
  {"claim": "The stores.json price is a Legacy-derived Cost carried into the Coin Shop catalogue; the note says it has not been checked against a real client transaction.", "source": "repo:notes/Research/Coin Shop.md:33"},
  {"claim": "The source tags L1, L2, L4, R2, T633, R1 are data-field and rule tags, not vendor names, so they do not identify a vendor.", "source": "repo:notes/Research/Coin Shop.md:33"},
  {"claim": "Sibling shorthair calico/tuxedo pets (locale 75171-75181) sit together in the client text table; the client cluster is not a source by itself.", "source": "locale:75171-75181"},
  {"claim": "A separate Longhair calico_white pet exists (locale 75212), so the name is not unique to this item.", "source": "lookup client locale:75212"}],
 "confidence": 0.5,
 "open": ["No wiki page, image, article, or video names this pet; the only source is the coin store catalogue row, so 'Coin Shop' is inferred from the data and not confirmed by a live listing.",
  "No coin vendor NPC is named as stocking it (vendor_stock empty); the 540-coin price is a regular price from the catalogue, not a confirmed vendor sale.",
  "Live status is unconfirmed: the stores.json row is marked sellable (no_sale false) but no current-era source confirms it still sells, so live is 'unsure' despite the first-pass 'yes'.",
  "The member price 486 (10% off) is arithmetic from the catalogue (R), not a price quoted by a wiki or article.",
  "Sibling calico/tuxedo pets were not individually checked for price or source; they may share the same entry but this was not verified.",
  "Client name also matches a Longhair calico_white pet (locale 75212); sources here apply only to the Shorthair definition 24026."]}
