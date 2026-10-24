<!-- fleet job=citem-infer id=cassembly-button-41005-v2 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[5550, 9397, 6, 2085] model=claude-haiku-5-5 -->
# Assembly Button

{"item": {"name": "Assembly Button", "locale_id": 41005, "kind": "collection"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, store category 105, tint group 3 (repo data only; vendor NPC not identified in any source)", "where": null, "price": "618 coins (member price 556 coins, 10% member discount; sell-back 61 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 41005 (line 12548)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is 'Assembly Button' (locale 41005), in the 41000-41010 button cluster", "source": "locale:41005"},
  {"claim": "Client description reads 'This item can be added to the Cool Buttons Collection'", "source": "locale:132359"},
  {"claim": "The 'Cool Buttons' collection name exists in client text", "source": "locale:7751"},
  {"claim": "Assembly Button is entry index 7 (name_id 41005, item_definition_id 3789) of a collection, with item_link 'sanctuary'", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json line 8075"},
  {"claim": "Store record for item 41005: category 105, tint group 3, purchase 618 coins, member price 556 coins, sell 61 coins, no_sale false. Same 618-coin price as neighbouring button items 41000, 41001, 41006", "source": "repo:prototype/osfr-tools/data/content/stores.json item 41005 (line 12548) and lines 12538-12549"},
  {"claim": "The wiki's List of Collections is cited by the prior answer for the Cool Buttons collection; it was not confirmed by lookup (no wiki or article hit for 'Assembly Button')", "source": "https://freerealms.fandom.com/wiki/List_of_Collections (cited by prior answer, unverified here)"}
 ],
 "confidence": 0.4,
 "open": [
  "Client definition lists coin_store_prices as empty, which conflicts with the stores.json 618-coin record. The price is repo-data only and not confirmed by the client or any wiki, article or video source. Treat the vendor source as unverified.",
  "The vendor NPC and zone for store category 105 are not identified. Find the coin vendor that uses category 105 for the button line.",
  "stores.json item_id 41005 matches the name_id, while the item definition is 3789. Confirm that stores.json keys on the same id space as the definition before trusting the price link.",
  "Live status is not confirmed. The earlier 'source tags' (L1, L2, L4, R2, T633, R1) are opaque codes and were dropped as evidence.",
  "No wiki page or article covers Assembly Button. The collection's completion rule and final reward are not confirmed.",
  "Retirement is unknown. No source states whether the item was later retired.",
  "The Coin Shop and SC Marketplace categories were not checked for this item.",
  "The prior answer's citation locale:1038667084 does not exist. The correct description id is locale:132359."
 ]}
