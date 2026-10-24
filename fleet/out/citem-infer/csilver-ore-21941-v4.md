<!-- fleet job=citem-infer id=csilver-ore-21941-v4 status=done turns=2 usd=0.0031 tokens(read,write,in,out)=[6980, 12836, 6, 2856] model=claude-haiku-5-5 -->
# Silver Ore

{"item": {"name": "Silver Ore", "locale_id": 21941, "kind": "other"},
 "sources": [
  {"type": "other", "detail": "Miner job gathering: common 'Silver Mining' minigame node (client #97, difficulty 4) yields Silver Ore, used in the Silver Bar recipe (Silver Ore x5 + Braze x3). Gathering has no schema source type; 'other' is used. The yield is from the Miner table; no quantity per node is documented.", "where": "Quagmire Quarry, Blackspore Swamp", "price": null, "currency": null, "source": "wiki page 'Miner' Locations table (Silver row: Common Quagmire Quarry); repo:notes/Build Guides/Content/Jobs/Miner.md:197 [client] [wiki]. Video GTvT_mVuq3U/00004 shows only the label 'Silver Mining' in Blackspore near the Haunted Mines (repo Miner.md:217); it is not location proof for Quagmire Quarry."},
  {"type": "other", "detail": "Miner job gathering: 'Rich Silver Mining' minigame node (client #98), members-only. The yield of Silver Ore is inferred from the node name and the Silver row of the wiki table; no source states the rich node's ore yield directly (it may yield Ruby gems).", "where": "Outside Blackspore Swamp and the eastern Wilds", "price": null, "currency": null, "source": "wiki page 'Miner' Locations table (Silver row: Rich outside Blackspore and eastern Wilds); repo:notes/Build Guides/Content/Jobs/Miner.md:197, :215 (client 2292639008: 'This rich mining vein is for Free Realms members only.')"},
  {"type": "other", "detail": "Miner 'Silver Vein' / 'Rare Silver Vein' node family (client names; not yet tied to a yield). Listed as a location-unknown node form, not a confirmed source.", "where": "Unknown", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Jobs/Miner.md:212 ; video 6yyOfeOsq80/00360 and yGlsrXeHD7c/00028 (label only)"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Client item 'Silver Ore' is name locale 21941, definition id 2742, description 'This item is useable in recipes.', no coin store price.", "source": "client definition in evidence pack; no entry in repo:data/content/stores.json"},
  {"claim": "No coin vendor stocks Silver Ore.", "source": "evidence pack vendor_stock (empty)"},
  {"claim": "Silver Ore is the input for the Silver Bar recipe (Silver Ore x5 + Braze x3).", "source": "wiki page 'Miner'"},
  {"claim": "Wiki has an article 'Silver Miner Ore' describing it as an ore the player clicks to mine.", "source": "wiki page 'Silver Miner Ore'"},
  {"claim": "Common silver nodes are at Quagmire Quarry (Blackspore Swamp); rich silver nodes are outside Blackspore and the eastern Wilds, members-only.", "source": "wiki page 'Miner' Locations table; repo:notes/Build Guides/Content/Jobs/Miner.md:197, :215; locale:2292639008"},
  {"claim": "Quest texts 'Collect 12 silver ore!' (locale:92877) and 'Collect 8 silver ore!' (locale:102514) ask the player to gather ore they already mine; they are not a separate source.", "source": "locale:92877, locale:102514"},
  {"claim": "Silver Ore is an input to Miner's Silver Ore job-material collection (client 2431256147); Block of Silver Ore is the reward of the Copper Ore collection, a different item.", "source": "repo:notes/Build Guides/Content/Jobs/Miner.md:233-235; wiki 'Job Specific (Collections)'"},
  {"claim": "The wiki says the mining minigames were later removed in favour of traditional vein nodes, so the minigame-node sources may no longer be live.", "source": "repo:notes/Build Guides/Content/Jobs/Miner.md:239; wiki 'Miner'"},
  {"claim": "Sunstone Silver Vein is a node label only; the Sunstone yield is tied to Sunstone Copper Vein, so no Silver Ore source there.", "source": "repo:notes/Build Guides/Content/Jobs/Miner.md:213, :217"}
 ],
 "confidence": 0.5,
 "open": [
  "No sale price: not in client definition, repo:data/content/stores.json, or wiki; not sold for coins or Station Cash. No coin shop or marketplace evidence.",
  "Retirement unresolved: the wiki says the mining minigames were removed; the vein-node form (Silver Vein) is seen in video but no yield frame exists. Whether the minigame sources are live today needs a check of the live wiki.",
  "Rich-node ore yield is inferred from the node name, not stated by a source.",
  "Gathering is not a schema source type; Bryce should decide whether to add a 'gathering' type. Under the current schema the item has no wireable priced source.",
  "Drop quantity per node and rich-node yield rate are not documented.",
  "Miner level gate unresolved: wiki and client Set A say 15, Set B says 12, Set C says 4 (Miner.md:228-231).",
  "Haunted Mines objective (locale:384775) and Drake Boneyard collect objective not counted; no quest tie in the pack.",
  "Whether Silver Ore is a quest reward is unconfirmed; no evidence found.",
  "ID check: definition id 2742 (pack) vs name hash 2316483463 (Miner.md:200) are different identifier types and were not reconciled."
 ]
}
