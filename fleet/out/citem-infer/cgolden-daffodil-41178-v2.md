<!-- fleet job=citem-infer id=cgolden-daffodil-41178-v2 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[5322, 9134, 6, 1594] model=claude-haiku-5-5 -->
# Golden Daffodil

{"item": {"name": "Golden Daffodil", "locale_id": 41178, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Turn-in item for the Golden Flowers collection (Flora chain on wiki 'List of Collections': Tulips/Orchids/Carnations/Roses/Daisies/Lilies/Sunflowers/Daffodils -> Golden Flowers -> Exotic Golden Flower). This is a membership fact, not an acquisition path: no source names a vendor, quest, drop or price that gives the item.", "where": null, "price": null, "currency": null, "source": "locale:41178; client text 'This item can be added to the Golden Flowers Collection' (locale:2914400005); wiki page 'List of Collections' (revid 27852, https://freerealms.fandom.com/wiki/List_of_Collections), Flora section; locale:7773 'Golden Flowers'"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Golden Daffodil' is locale 41178; its description says it can be added to the Golden Flowers Collection", "source": "locale:41178; locale:2914400005"},
  {"claim": "Golden Flowers is a collection on the wiki's List of Collections, Flora chain, with Daffodils as a stage-1 entry", "source": "wiki page List of Collections, revid 27852"},
  {"claim": "Sibling items Golden Rose, Daisy, Sunflower and Tulip carry the same Golden Flowers description cluster", "source": "locale:41175-41179"}
 ],
 "confidence": 0.35,
 "open": [
  "No coin store price, vendor stock, quest reward, drop, event or prize-wheel source found for Golden Daffodil.",
  "Dropped the earlier quest_reward source: collection_catalogue.json entry 28 (item 3962) resolves to the 'Daffodils' collection (name_id 38691), a collection-completion reward. Its link to Golden Flowers is unconfirmed, and it is not a quest reward.",
  "Second definition 23030 has no name, slot or model data in the pack; unclear whether it is a tint/race variant.",
  "Wiki gives no price or drop rate for Golden Flowers stage rewards, and the '§' marker in the wiki table is unexplained.",
  "Live/retired status unconfirmed: the only dated source is the 2013 wiki revision. Whether the Golden Flowers collection stayed open after 2013 is unknown.",
  "Second locale-ID check: name locale 41178 and description locale 2914400005 are both in the client table; the description ID is the table hash, not a sequential locale number."
 ]}
