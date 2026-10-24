<!-- fleet job=citem-infer id=ckitty-lion-ribbon-19269-v1 status=done turns=3 usd=0.0022 tokens(read,write,in,out)=[8355, 8927, 8, 2034] model=claude-haiku-5-5 -->
# Kitty Lion Ribbon

{"item": {"name": "Kitty Lion Ribbon", "locale_id": 19269, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Coin vendor sale (vendor NPC not identified in our data; stores.json lists the item with no vendor name)", "where": null, "price": "270 coins (member price 243 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 55014 (and item 55015, same price); client definition coin_store_price 270"}],
 "retired": null, "live": "yes",
 "evidence": [{"claim": "Client name is 'Kitty Lion Ribbon', locale 19269; description 'Any pet is sure to have a roaring good time in this ribbon.' is locale 19285.", "source": "locale:19269; locale:19285"},
  {"claim": "Two client definitions (55014, 55015), both in the coin store data at 270 coins, member price 243, no_sale true, no tint group.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 55014; item 55015"},
  {"claim": "Item sits in the same stores.json run as 55000-55013, all 270-coin category 6 items, so it is part of a batch of pet-clothing coin store items.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 13535-13548"},
  {"claim": "Slot 6 and class 61 with model pet_cat_<descriptor>_shoulders_ribbon.adr: a pet shoulder ribbon, so clothing.", "source": "client definition (pack)"},
  {"claim": "Locale 150712 calls it 'The ribbon for the kitty lion costume', which suggests it belongs to a Kitty Lion costume set.", "source": "locale:150712"},
  {"claim": "No wiki page, article, or video covers the item; no vendor stock list names it; the lookup of the name returned only client text.", "source": "lookup: client, wiki, articles, video (no wiki/article/video hits)"}],
 "confidence": 0.5,
 "open": ["The coin vendor that sells it is not named in our data. Stores.json gives the price and category but no NPC or shop, so the vendor source is real but its location is unknown.",
  "Whether the 270-coin price is the original launch price, or whether the item was later retired or moved to Station Cash, is not stated in any source. The no_sale flag is set, but its meaning is not documented here.",
  "Two definitions (55014, 55015) share the name; the pack does not say whether they are tints, races, or separate sexes. Both are at 270 coins.",
  "The 'kitty lion costume' link (locale 150712) suggests a costume set or bundle; no membership, promotion, or set source was found.",
  "No wiki page exists for the item, so the 'retired' flag cannot be checked against a wiki or article."]}
