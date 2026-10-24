<!-- fleet job=citem-infer id=cayani-medal-41101-v2 status=nothing_found turns=4 usd=0.0028 tokens(read,write,in,out)=[26731, 11731, 10, 2118] model=claude-haiku-5-5 -->
# Ayani Medal

{"item": {"name": "Ayani Medal", "locale_id": 41101, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 41101 is 'Ayani Medal'; its description is 'This item can be added to the Unique Medals Collection'. The same sentence is standalone line 132371, which names the collection 'Unique Medals Collection'.", "source": "locale:41101; locale:132371"},
  {"claim": "Item definition 3885 is entry index 7 of collection 'Unique Medals' (name_id 7763, wiki key wiki:6:189), with item_link 'sanctuary'. Neighbouring medals 41096-41106 (Silver Lining, Shooting Star, Star Cluster, Snowflake, Life Energy, Sun Touched, Hard Worker, Helping Hand, Never Giving Up, Giving 110%) form one cluster of client names.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:9305-9312 (id 817, name_id 41101, item_definition_id 3885) and :9249 (collection id 112); repo:prototype/osfr-tools/data/content/collections.json:10318-10345"},
  {"claim": "The wiki's 'List of Collections' page lists '[Unique] [Medals]' as a collection, but the entry has no entry list, reward or acquisition text (entries_known false, entry_count null).", "source": "wiki: List of Collections (https://freerealms.fandom.com/wiki/List_of_Collections); repo:prototype/osfr-tools/data/content/collections.json:10318-10345"},
  {"claim": "No coin store price, vendor stock, quest reward, drop, event, or video frame names the Ayani Medal. Searches of the repo, client locale, wiki and articles returned no acquisition text for it or for the Unique Medals collection.", "source": "lookup (client, wiki, articles, video) and search of repo, 'Ayani|Unique Medals|Sun Touched' results"},
  {"claim": "The client has a hidden-key string 'NOT LIVE - hidden collection key: ayani'. It is a lead only: it does not name the Ayani Medal, and it is a per-collection flag like 'NOT LIVE: hidden collection key: memorial caves' (103283).", "source": "locale:100819; locale:103283"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found. The item stays unsourced and not wireable until a quest, vendor, event or collection-NPC source names the medal or the Unique Medals collection.",
  "The critique's cited locale:922644909 does not exist. The correct id for the 'NOT LIVE - hidden collection key: ayani' string is locale:100819 (verified). The claim is kept as a lead only.",
  "How the medal family (41096-41106) is earned is unknown. Sibling medals also lack sources here, so the family needs one search together.",
  "Whether the Unique Medals collection and the Ayani Medal were live or retired is unverified. The first-pass live=yes is not backed by a source, so live is 'unsure'.",
  "The Sanctuary collection NPC linked by item_link 'sanctuary' is a possible route, but no NPC or quest text ties it to these medals."
 ]}
