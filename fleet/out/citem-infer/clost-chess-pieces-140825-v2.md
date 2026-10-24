<!-- fleet job=citem-infer id=clost-chess-pieces-140825-v2 status=nothing_found turns=2 usd=0.0021 tokens(read,write,in,out)=[6042, 10107, 6, 1617] model=claude-haiku-5-5 -->
# Lost Chess Pieces

{"item": {"name": "Lost Chess Pieces", "locale_id": 140825, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text 'Lost Chess Pieces' is locale 140825; lookup over client text returns only that entry, with no quest, wiki, article or video hit.", "source": "locale:140825; lookup (client)"},
  {"claim": "The item definition exists in the client item table (NameId 140825, comment 'Lost Chess Pieces'), with no coin store price, so it is not a coin vendor sale.", "source": "Sanctuary/src/Resources/ClientItemDefinitions.json:991317-991320; Lxzxrus-Free-Realms-Server/src/Resources/ClientItemDefinitions.json:991317-991320; repo:data/content/stores.json (no entry)"},
  {"claim": "Across the repo and community refs, 140825 appears only in item definition tables and builder quest-line/citem files (quest-lines/citem-packs.json 'clost-chess-pieces-140825'), not in any quest reward, vendor, drop or event table.", "source": "search of refs and repo for 'Lost Chess' and 140825"},
  {"claim": "The 14082x cluster (140820 Empty Coffee Cup, 140823 Chewed-Up Shoe, 140824 Old Rusty Spoon, 140826 Old Hanger, 140827 Rusty Nails, 140828 Metal Button, 140829 Spoiled Eggs, 140830 Petrified Leaf) groups the item by name and ID adjacency only; this is an inference, not a shared-source fact.", "source": "locale:140820-140830"},
  {"claim": "The earlier Brawler 'One Man's Junk' (quest 3030028, locale 141010) lead is unconfirmed: its record has empty objectives and rewards in brawler.json, and no client text ties the item to it. The previous 'Find the Robgoblin junk' citation (locale 18751-18774) belongs to NOT LIVE quest 18774 and is not used as live evidence.", "source": "locale:141010; prototype/osfr-tools/data/content/quests/brawler.json (3030028 rewards [] objectives [])"}
 ],
 "confidence": 0.15,
 "open": [
  "No acquisition source is confirmed. The Brawler 'One Man's Junk' quest is only a thematic/ID-proximity lead; do not list it as a quest_reward or drop until its collect or reward items are read from the client quest record.",
  "Whether the item drops from Robgoblin Troublemakers or is a quest-only collect item is unknown. No enemy drop table in the pack names it.",
  "Live and retired status are unknown. The item has a client definition but no live source; it may be unobtainable.",
  "No price, vendor, coin store entry, Station Cash listing or Coin Shop entry was found, so there is no currency source."
 ]}
