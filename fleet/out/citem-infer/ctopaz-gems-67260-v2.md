<!-- fleet job=citem-infer id=ctopaz-gems-67260-v2 status=done turns=6 usd=0.0028 tokens(read,write,in,out)=[37612, 9232, 14, 2488] model=claude-haiku-5-5 -->
# Topaz Gems

{"item": {"name": "Topaz Gems", "locale_id": 67260, "kind": "collection"},
 "sources": [
  {"type": "other", "detail": "Mined by the Miner job from tin veins/deposits (harvest node, Job Material spawn type); the Shimmer Shinyaxe and Surelytree tasks send players to mine topaz", "where": "Dartmoor (tin deposits / tin veins)", "price": null, "currency": null, "source": "locale:77074 'Mine Topaz from the tin deposits at Dartmoor for Shimmer Shinyaxe'; locale:77186 'Topaz can be found on tin veins.'; repo:prototype/osfr-tools/data/content/collections.json:3904 (Miner's Precious Gems, spawn_type Job Material)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Topaz Gems' is locale 67260; its client definition (definition 23647) description says it can be added to the Miner's Precious Gems Collection", "source": "locale:67260; client definition 23647"},
  {"claim": "Topaz Gems is an entry of the Miner's Precious Gems collection", "source": "repo:prototype/osfr-tools/data/content/collections.json:3935 (name 'Topaz Gems'); wiki page 'Job Specific (Collections)' lists '[Topaz] [Gems]' under [Miner]'s [Precious] [Gems] (verified by wiki search)"},
  {"claim": "Topaz is mined from tin veins at Dartmoor; Shimmer's task asks to mine topaz from tin deposits", "source": "locale:77074; locale:77186"},
  {"claim": "Anata's Summersaber enchantment quest consumes 10 Topaz gems; this is a consumer, not a source", "source": "locale:101270; locale:101283"},
  {"claim": "No coin store price exists and no coin vendor stocks Topaz Gems", "source": "client definition coin_store_prices []; vendor_stock []"},
  {"claim": "Onyx Gems, not Topaz, is the reward for completing Miner's Gold Ore", "source": "wiki 'Job Specific (Collections)'"},
  {"claim": "Excluded as not live: Gems for Pinkelug quest text (locale:23650, 23654 flagged not_live); placeholder collect-five-topaz blocks (locale:37781, 37782) flagged placeholder", "source": "client FLAG fields"}
 ],
 "confidence": 0.6,
 "open": [
  "Harvest-node drop rate and exact tin-vein node locations for Topaz were not confirmed; only client text and the collection listing support the mining source.",
  "Whether completing the Miner's Precious Gems collection gives a reward item was not established.",
  "No dated wiki or article source confirms Topaz is obtainable live; treated as live based on the collection listing and mining text only.",
  "Previous answer's cited locale ids 579285470, 2042261050, 53797, 157497688, 955863104 do not exist and were replaced with 77074, 77186, 101270, 101283 (verified) and the client definition."
 ]}
