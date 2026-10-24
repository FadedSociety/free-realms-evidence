<!-- fleet job=citem-infer id=cgleaming-honey-ring-96099-v1 status=nothing_found turns=8 usd=0.0064 tokens(read,write,in,out)=[112113, 24503, 18, 4401] model=claude-haiku-5-5 -->
# Gleaming Honey Ring

{"item": {"name": "Gleaming Honey Ring", "locale_id": 96099, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition: definition id 30693, Type 1, Slot 8, Class 67, NameId 96099, DescriptionId 96815, Cost 1500 (the in-game base Cost field, not a store price), NoTrade true, MemberDiscount 10, MinProfileRank 1, dyetint tint alias.", "source": "refs:Sanctuary/src/Resources/ClientItemDefinitions.json:633200-633215 (also FreeRealms-Legacy and Lxzxrus-Free-Realms-Server ClientItemDefinitions.json id 30693)"},
  {"claim": "Name is locale 96099 'Gleaming Honey Ring'; its placeholder stub line is locale 150438 'This is a Gleaming Honey Ring item.' (FLAG placeholder).", "source": "locale:96099; locale:150438; quest-lines/flags.tsv:10854"},
  {"claim": "Description text (locale 96815) is shared with a 'Flower ring' item: 'A beautiful flower ring that is blooming brightly. It increases your talent as a blacksmith, chef, miner, and postman when equipped.'", "source": "locale:96815"},
  {"claim": "The Gleaming ring/necklace family (Ocean, Jungle, Grape, Honey, Ruby, Pumpkin) has no wiki page, no vendor stock, no store price, and no quest or drop answer in any source checked.", "source": "lookup client/wiki/articles/video for 'Gleaming Honey Ring' and 'Gleaming ring necklace' (no wiki or article hits); quest-lines/citem-packs.json sibling packs (cgleaming-grape-necklace-96218, cgleaming-grape-ring-96098) also have empty vendor_stock and no sources"},
  {"claim": "No coin store price: stores data has no entry for definition 30693 (repo and refs search for 30693 finds only ClientItemDefinitions files and a citem pack id reference), so coin_store_prices is empty.", "source": "repo search '30693'; refs search '\\b30693\\b'"},
  {"claim": "The crafting guess from the first pass has no supporting evidence in any source checked.", "source": "jev_first_pass (hint only)"}
 ],
 "confidence": 0.15,
 "open": [
  "No source found. The first-pass 'crafting' guess is unsupported; no recipe in repo or refs produces 30693 or 96099.",
  "Unknown whether this ring was ever obtainable by players: the client and community definition files (Sanctuary, Legacy, Lxzxrus) ship it, and the placeholder flag suggests it is a haiku-era stub set. Needs a player source (wiki, forum, or a dated release/event note) before listing any source.",
  "Client Cost 1500 is the base item cost field; it is not a coin store price and was not treated as a sale price. Confirm whether it ever appeared in a coin shop.",
  "The description is shared with locale 96815 'Flower ring' (talent, crafting/gathering stats); confirm whether that is a separate item that was sold, which might relate to this ring's source.",
  "Live status unsure: the item is defined in the client but no source confirms that it was sold, dropped, or rewarded."
 ]}
