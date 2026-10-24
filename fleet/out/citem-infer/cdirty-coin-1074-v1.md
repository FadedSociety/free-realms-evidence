<!-- fleet job=citem-infer id=cdirty-coin-1074-v1 status=done turns=4 usd=0.0036 tokens(read,write,in,out)=[27292, 15899, 10, 2670] model=claude-haiku-5-5 -->
# Dirty Coin

{"item": {"name": "Dirty Coin", "locale_id": 1074, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition: name 'Dirty Coin' (locale 1074), definition_ids [58], description 'This item can be added to a collection.', no coin store price, no models.", "source": "locale:1074; quest-lines/citem-packs.json cdirty-coin-1074 (client_definition block)"},
  {"claim": "Client item definition comment is 'Dirty Coin' in the community server resource files, so the item is a real client definition, not a placeholder.", "source": "FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:1209; Sanctuary-main-20261019/src/Resources/ClientItemDefinitions.json:1209"},
  {"claim": "It sits in a cluster of coin items with Shiny Coin (1075), Wooden Coin (1076), Briarwood Coin (1077), Snowhill Coin (1078) and Ayani Coin (1079). The cluster also includes 'Old Fabled Realms' (locale 1069, flagged not_live old area name) and Trauma Support Backpack items (1071, 1073).", "source": "locale:1069, 1071, 1073, 1075-1079 (client_cluster in quest-lines/citem-packs.json)"},
  {"claim": "The wiki's Collections page describes Rare Exploration coins: floating coins in the world that carry an area's collection name, and that count toward that area's coin collection. Dirty Coin's collection is not named in any source found.", "source": "wiki: Collections; wiki: Spawn Types; wiki: Exploration (Collections)"},
  {"claim": "No wiki article, video frame, article fact, vendor stock entry, or quest/enemy reference names Dirty Coin. A lookup for the name returned only the client locale line.", "source": "lookup (client, wiki, articles, video) for 'Dirty Coin'"}
 ],
 "confidence": 0.3,
 "open": [
  "No acquisition source is evidenced. The likely source is a Rare Exploration coin spawn in the world (Collections system), but no source names Dirty Coin or the zone or collection it belongs to, so I did not list one.",
  "The collection that Dirty Coin counts toward is unknown. The description only says 'can be added to a collection', and the cluster suggests a Fabled Realms or old-area collection.",
  "No coin store price exists in stores.json or the client definition, so no coin shop or marketplace source applies.",
  "Live status is unclear. The only neighbouring place name is flagged not_live (Old Fabled Realms), and the first-pass 'live: yes' tag is a hint only.",
  "Check the Collections wiki page's coin list, or the Fabled Realms collection data, for a Dirty Coin entry before marking a source."
 ]}
