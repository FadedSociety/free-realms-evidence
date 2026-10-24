<!-- fleet job=citem-infer id=clifeguard-shirt-105728-v1 status=done turns=5 usd=0.0034 tokens(read,write,in,out)=[29450, 13037, 12, 2886] model=claude-haiku-5-5 -->
# Lifeguard Shirt

{"item": {"name": "Lifeguard Shirt", "locale_id": 105728, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Coin store sale (category 103, unnamed vendor/shop in the store data; the exact NPC or shop is not identified)", "where": null, "price": "270 coins (member price 243 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 32646 (line 7748: purchase_price_coins 270, member_price_coins 243, sell_price_coins 27, no_sale false)"}],
 "retired": null, "live": "yes",
 "evidence": [{"claim": "Client defines 'Lifeguard Shirt' as item name locale 105728, definition 32646, chest slot 3, one definition, model freestyle_<race>_<gender>_chest_swimshirt.adr", "source": "locale:105728; client definition in pack"},
  {"claim": "Store data lists definition 32646 as a coin store item at 270 coins, member price 243, sellable (no_sale false)", "source": "repo:prototype/osfr-tools/data/content/stores.json item 32646"},
  {"claim": "Asset manifest has a lifeguard swim-shirt tint (adventurer-lifeguard icon and a 'lifeguardtcg' texture), so the shirt is a costume tint of the swimshirt chest model", "source": "osfr-asset-manifest/Assets_manifest.txt lines 127957-127961 and 27718"},
  {"claim": "A 2010 freerealms.com article ('Add A Pool To Your Home', 2010-06-26) offered a Lifeguard Station housing item alongside the pool; this is a related lifeguard-theme housing item, not the shirt itself", "source": "articles/facts.json (article-1573, locale 1068)"}],
 "confidence": 0.5,
 "open": ["No wiki page, article, video, or quest/drop source names the Lifeguard Shirt; the only source is the coin store price row, and the store data does not name which coin vendor or shop sells category 103.",
  "The source_tags (L1, L2, L4, R2, T633, R1) in the store row are not decoded here; T633 may point to a specific time-limited or seasonal coin release, which would make this a retired/event item, but this is unverified.",
  "Sale window, release date and retirement status are unknown; retired is left null.",
  "Whether the shirt was also a promotion, TCG or event reward (the 'lifeguardtcg' texture name hints at a Trading Card Game tie-in) is unverified; no other source found.",
  "Jev's first-pass 'vendor' guess is consistent with the store row but was not independently confirmed beyond it."]}
