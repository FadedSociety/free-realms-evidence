<!-- fleet job=citem-infer id=cfrozen-sunflower-17520-v2 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[5507, 8834, 6, 1876] model=claude-haiku-5-5 -->
# Frozen Sunflower

{"item": {"name": "Frozen Sunflower", "locale_id": 17520, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Piece of the Snowhill Sunflowers collection (client text: 'This item can be added to the Snowhill Sunflowers Collection'). How the piece itself is obtained is not documented.", "where": "Snowhill", "price": null, "currency": null, "source": "locale:17520; locale:132494; locale:17575 ('Snowhill Sunflowers'); wiki page 'List of Collections' (entry '[Snowhill] [Sunflowers]')"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item 'Frozen Sunflower' is locale 17520 (client definition id 9152, no client coin store price).", "source": "locale:17520"},
  {"claim": "Its description reads 'This item can be added to the Snowhill Sunflowers Collection'.", "source": "locale:132494"},
  {"claim": "'Snowhill Sunflowers' is the collection name (locale 17575).", "source": "locale:17575"},
  {"claim": "The wiki's List of Collections page has a '[Snowhill] [Sunflowers]' entry, and the 'Exploration (Collections)' page refers to completing [Snowhill] collections.", "source": "wiki page: List of Collections; wiki page: Exploration (Collections)"},
  {"claim": "repo stores.json row item_id 17520 (category 200, tint group 2, 10000 coins, member price 9000, no_sale true) sits in a block of similar rows (17514-17529). It is not used as a sale source because the client definition has no coin store price and the row's item_id/definition mapping and category 200 meaning are undocumented.", "source": "repo:prototype/osfr-tools/data/content/stores.json:4311"},
  {"claim": "Corrections from the prior critique applied: locale:1385340191 and locale:3166059484 do not exist and are dropped; the correct name locale is 17575.", "source": "locale:17575; locale:132494"}
 ],
 "confidence": 0.3,
 "open": [
  "Acquisition method for the Frozen Sunflower piece is undocumented in the pack: no wiki page, article, video, vendor, or drop evidence names how players obtained it. The collection is the only supported source, and the collection's reward or completion rules are not documented.",
  "Price conflict: stores.json row item_id 17520 shows 10000 coins (member 9000) with no_sale true, but the client definition lists no coin store price and uses definition id 9152. It is unresolved whether item_id 17520 is this item; no coin vendor sale is claimed.",
  "Category 200 meaning is not documented in the pack, so it is not characterized as a purchase or non-purchase source.",
  "Sister-item description pattern (locale 17515-17525) is inferred from names only; the descriptions were not verified.",
  "Live status and retirement are unverified: the first-pass 'live: yes' is a hint only and no source confirms 2009-2014 availability."
 ]}
