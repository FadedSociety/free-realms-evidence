<!-- fleet job=citem-infer id=cserbia-soccer-shirt-31635-v2 status=done turns=3 usd=0.0026 tokens(read,write,in,out)=[15146, 10837, 8, 2238] model=claude-haiku-5-5 -->
# Serbia Soccer Shirt

{"item": {"name": "Serbia Soccer Shirt", "locale_id": 31635, "kind": "clothing"},
 "sources": [
  {"type": "marketplace", "detail": "2010 FIFA World Cup national soccer shirt set, inferred from sibling wiki pages (Brazil, Spain, Italy, Mexico, Korea DPR, New Zealand Soccer Shirt). No Serbia-specific page exists; this is an inference from the set, not a direct record.", "where": "Station Cash Marketplace", "price": null, "currency": "station_cash", "source": "wiki: Brazil Soccer Shirt; Spain Soccer Shirt; Italy Soccer Shirt; Mexico Soccer Shirt; Korea DPR Soccer Shirt; New Zealand Soccer Shirt (all say 'acquired during the 2010 FIFA World Cup through the Station Cash Marketplace', Category:Unobtainable)"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Client name 'Serbia Soccer Shirt', description 'Show support of your favorite country's team!', chest slot 3, class 143, one definition 16318.", "source": "locale:31635; client definition from evidence pack"},
  {"claim": "Sibling national soccer shirts (Brazil, Spain, Italy, Mexico, Korea DPR, New Zealand) are wiki pages stating they were unobtainable, acquired during the 2010 FIFA World Cup via the Station Cash Marketplace, Category:Unobtainable.", "source": "wiki: Brazil Soccer Shirt; Spain Soccer Shirt; Italy Soccer Shirt; Mexico Soccer Shirt; Korea DPR Soccer Shirt; New Zealand Soccer Shirt"},
  {"claim": "stores.json row for item 16318 gives purchase 50 coins, member 45 coins (10%), no_sale true, category 103. The row carries only source_tags and no vendor/NPC owner; the same shape is used for neighbouring items 16294-16325 and other unrelated items in category 103.", "source": "repo:prototype/osfr-tools/data/content/stores.json:6630 (item 16318); rows 6606-6637"},
  {"claim": "Client lookup for the name returns only the client text line; no wiki page, article, or video names the Serbia shirt.", "source": "lookup client locale:31635"},
  {"claim": "First-pass tag 'live: yes, source event' is contradicted by the sibling wiki evidence and was not used.", "source": "jev first pass (hint only)"}
 ],
 "confidence": 0.5,
 "open": [
  "No vendor source is listed. The 50-coin price (stores.json item 16318, no_sale true, matches client coin_store_prices [50]) has no owning NPC or store in the data; the category-103 row shape is shared with unrelated items, so it cannot be tied to a coin vendor. Needs the owning vendor or a confirmed coin shop listing before adding a coin_shop/vendor source.",
  "Station Cash Marketplace price for the Serbia shirt is not stated in any source. Sibling pages also give no price.",
  "Marketplace source and Unobtainable status are inferred from sibling pages (Brazil, Spain, Italy, Mexico, Korea DPR, New Zealand); no Serbia-specific wiki page, article, or video was found.",
  "Not wireable yet: no source has both an evidenced price and an owning vendor or event.",
  "Jev's 'live: yes' tag is unsupported and was not used; live 'no' rests on the sibling Unobtainable category."
 ]}
