<!-- fleet job=citem-infer id=cayani-medal-41101-v3 status=nothing_found turns=2 usd=0.0024 tokens(read,write,in,out)=[6007, 12535, 6, 1561] model=claude-haiku-5-5 -->
# Ayani Medal

{"item": {"name": "Ayani Medal", "locale_id": 41101, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 41101 is 'Ayani Medal'. Its description, 'This item can be added to the Unique Medals Collection', is the standalone line locale:132371, which names the 'Unique Medals Collection'.", "source": "locale:41101; locale:132371"},
  {"claim": "Item definition 3885 is entry of collection 'Unique Medals' (name locale:7763), in the repo's collection catalogue (id 817, name_id 41101, item_definition_id 3885; collection id 112).", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:9305-9312; repo:prototype/osfr-tools/data/content/collections.json:10318-10345"},
  {"claim": "The wiki's 'List of Collections' page lists '[Unique] [Medals]' as a collection. This shows the collection exists; it gives no acquisition, entry list or reward, so it is an existence source only.", "source": "wiki: List of Collections (https://freerealms.fandom.com/wiki/List_of_Collections)"},
  {"claim": "No coin store price, vendor stock, quest reward, drop, event, prize wheel, or video frame names the Ayani Medal or the Unique Medals collection. A fresh lookup and a repo search for 'Ayani|3885' found no acquisition text for either.", "source": "lookup (client, wiki, articles, video); search repo 'Ayani|3885'"},
  {"claim": "Client strings 'NOT LIVE - hidden collection key: ayani' and 'NOT LIVE: hidden collection key: memorial caves' are flagged not_live. They are a lead that this collection key may be hidden, not evidence of sale or of live status; they do not name the medal.", "source": "locale:100819 (not_live flag); locale:103283 (not_live flag). Not live evidence."}
 ],
 "confidence": 0.15,
 "open": [
  "No acquisition source found. The item stays unsourced and not wireable until a quest, vendor, event or collection-NPC source names the medal or the Unique Medals collection.",
  "Live status is unsure. The first-pass live=yes has no source. The only status text (locale:100819) is flagged NOT LIVE, which points toward hidden or not-live, but it is not live evidence and does not establish retirement.",
  "The earlier citation locale:922644909 does not exist and has been dropped. The correct id for the hidden-key string is locale:100819.",
  "The medal family (locale 41096-41106: Silver Lining, Shooting Star, Star Cluster, Snowflake, Life Energy, Sun Touched, Hard Worker, Helping Hand, Never Giving Up, Giving 110%) shares the same gap. Sibling medals also lack sources, so the family needs one search together.",
  "The Sanctuary collection NPC (item_link 'sanctuary') is a possible route, but no NPC or quest text ties it to these medals."
 ],
 "critiques_addressed": "Evidence critique: bad id locale:922644909 removed; sources kept empty; locale:132371 claim kept as accurate. World critique: not_live strings moved out of positive evidence into a not_live note; live set to unsure with reason; wiki collection entry described as existence-only; retired left null."}
