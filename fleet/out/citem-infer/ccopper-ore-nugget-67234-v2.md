<!-- fleet job=citem-infer id=ccopper-ore-nugget-67234-v2 status=done turns=3 usd=0.0023 tokens(read,write,in,out)=[12878, 8323, 8, 2173] model=claude-haiku-5-5 -->
# Copper Ore Nugget

{"item": {"name": "Copper Ore Nugget", "locale_id": 67234, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Miner's Copper Ore job-material collection (entry 3 of 8: Piece, Chunk, Copper Ore Nugget, Block, Sliver, Hunk, Ounce, Pile of Copper Ore). Obtained as a Job Material from Miner job spawns; it is a collection entry, not a purchasable item. The specific node or spawn that yields the Nugget is not evidenced.", "where": "Mines (Miner job material spawns, while the player is using the Miner job)", "price": null, "currency": null, "source": "locale:67234; repo:prototype/osfr-tools/data/content/collections.json key wiki:2:51 (\"Miner's Copper Ore\", entry_count 8, entry \"Copper Ore Nugget\"); repo:notes/Build Guides/Content/Jobs/Miner.md:235 (job material spawns appear in mines only while using the Miner job)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Copper Ore Nugget (locale 67234) is client text 'This item can be added to the Miner's Copper Ore Collection' and has no coin store price and no vendor stock in the pack.", "source": "locale:67234; client definition in evidence pack"},
  {"claim": "The repo collection Miner's Copper Ore (wiki:2:51) lists 8 entries, including 'Copper Ore Nugget', each tagged source 'wiki'.", "source": "repo:prototype/osfr-tools/data/content/collections.json:3646-3675"},
  {"claim": "Miner collections are Job Material collections; job material spawns appear in mines only while the player is using the Miner job.", "source": "repo:notes/Build Guides/Content/Jobs/Miner.md:235"},
  {"claim": "Mining minigames were later removed in favour of traditional nodes; no source in the pack says whether the Miner collections were removed.", "source": "repo:notes/Build Guides/Content/Jobs/Miner.md:239 (citing wiki)"}
 ],
 "confidence": 0.4,
 "open": [
  "Live wiki lookup returned no page for 'Copper Ore Nugget' or the Miner's Copper Ore collection in this session, so the wiki 'Job Specific (Collections)' listing cited in the pack is not re-verified here.",
  "The Snowhill copper vein example from the previous answer is removed: no source names Snowhill or any node as the Nugget's spawn.",
  "Drop rate and which node or spawn yields the Nugget are unknown.",
  "The collection reward (Miner.md:235 says Copper Ore gives Block of Silver Ore) is cited to the wiki but not verified against a wiki page; it is not a source for this item and is omitted.",
  "Whether the Miner collections (and so the Nugget's acquisition path) still exist in the live game is unsettled; the wiki says mining minigames were removed, but that does not settle the collection.",
  "No price, vendor, quest, enemy or event source exists, so the item is not wireable as a purchasable or rewarded item yet."
 ],
 "wireable": false}
