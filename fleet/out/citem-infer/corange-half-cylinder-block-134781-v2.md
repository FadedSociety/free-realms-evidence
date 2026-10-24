<!-- fleet job=citem-infer id=corange-half-cylinder-block-134781-v2 status=done turns=2 usd=0.0030 tokens(read,write,in,out)=[5332, 14575, 6, 2198] model=claude-haiku-5-5 -->
# Orange Half Cylinder Block

{"item": {"name": "Orange Half Cylinder Block", "locale_id": 134781, "kind": "furniture"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop furniture block, client definition 77188 (candidate for this colour; mapping to orange unconfirmed; store row marks no_sale=true, member price 45)", "where": "Coin Shop (category 147)", "price": "50 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 16519 (item_id 77188); client definition 77188 listed in the client's coin_store_prices"},
  {"type": "coin_shop", "detail": "Coin Shop furniture block, client definition 77245 (candidate for this colour; mapping to orange unconfirmed; store row sellable for 30 coins, member price 270)", "where": "Coin Shop (category 147)", "price": "300 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 16576 (item_id 77245); client definition 77245 listed in the client's coin_store_prices"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Orange Half Cylinder Block' is locale 134781; description 'Great for stackability.'; model hsg_block_cylinderhalf_01.adr.", "source": "locale:134781; client definition; repo Models.txt line 1926"},
  {"claim": "Two client definitions (77188, 77245) share the name and carry coin store prices of 50 and 300 coins, both in store category 147.", "source": "client definition coin_store_prices; repo:prototype/osfr-tools/data/content/stores.json lines 16519 and 16576"},
  {"claim": "The 50-coin rows form a long run of identical category-147 entries (about 77184 onward), and the 300-coin rows a similar run around 77245, so the store data alone does not say which row is the orange colour.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 16515-16580"},
  {"claim": "The same model has other surface variants in the client (cheese, polka dots, tiger stripes textures and 'Orange Half Cylinder Tiger Block' locale 134830, 'Orange Half Cylinder Down Block' locale 134791), so one shape and several named variants exist; the 77188/77245 pairing to colour is not resolved.", "source": "repo:Assets_manifest.txt lines 57916-58001; lookup locale:134791, locale:134830, locale:31877"},
  {"claim": "Sibling colour variants (locale 134776-134786) sit together in the client as one furniture set.", "source": "client cluster locale:134776 to locale:134786"},
  {"claim": "No wiki page, article, video frame, quest, drop or prize-wheel source names this item.", "source": "lookup of wiki/articles/video found no page for this item name"}
 ],
 "confidence": 0.4,
 "open": [
  "Which definition (77188 at 50 coins or 77245 at 300 coins) is the orange colour is unconfirmed; check the client definition files for the tint/colour field on each id before treating either price as this item's price.",
  "The earlier video frame yJ2KHN9I7EI/00978 shows a Basic Cylinder Block at 40 coins; it is a different item and is not used as a source here.",
  "Live status is unsure: store rows exist but there is no sale-date or listing evidence. Retirement is unknown; 77188 is flagged no_sale in store data, which does not by itself mean retired.",
  "No wiki or community evidence names the orange block; the coin-shop prices rest only on store data and the client's coin_store_prices.",
  "Whether the 50 and 300 coin prices reflect separate sizes, tints or sale periods is not evidenced."
 ]}
