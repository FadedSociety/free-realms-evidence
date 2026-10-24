<!-- fleet job=citem-infer id=chunk-of-gold-ore-67253-v2 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[5418, 6286, 6, 1648] model=claude-haiku-5-5 -->
# Hunk of Gold Ore

{"item": {"name": "Hunk of Gold Ore", "locale_id": 67253, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Entry in the Miner's Gold Ore collection (8 entries: Piece, Chunk, Gold Ore Nugget, Block, Sliver, Hunk, Ounce, Pile of Gold Ore). It counts toward the set; it is not sold or given by a vendor. Set completion reward per the wiki: Onyx Gems.", "where": null, "price": null, "currency": null, "source": "freerealms-wiki/wikitext/2190-27853-ba6c0a72b278.wiki lines 327-345 (Miner's Gold Ore, CollectInfobox, reward Onyx Gems, spawn Job Material); repo:prototype/osfr-tools/data/content/collections.json:3815-3880 (name at 3819, 'Hunk of Gold Ore' at 3856); locale:132463 'This item can be added to the Miner's Gold Ore Collection'; lookup wiki page 'Job Specific (Collections)' lists Miner's [Gold] [Ore] with Hunk among its entries"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item 67253 'Hunk of Gold Ore' (definition 23640) has the description 'This item can be added to the Miner's Gold Ore Collection'.", "source": "locale:67253; locale:132463"},
  {"claim": "The wiki's Miner's Gold Ore collection lists Hunk of Gold Ore among its 8 entries, with reward Onyx Gems.", "source": "freerealms-wiki/wikitext/2190-27853-ba6c0a72b278.wiki:327-345; repo:prototype/osfr-tools/data/content/collections.json:3819-3880"},
  {"claim": "The collection appears on the wiki's Job Specific (Collections) page under Miner's [Gold] [Ore].", "source": "lookup wiki page 'Job Specific (Collections)'"},
  {"claim": "The client definition has no coin store price and no model files, so there is no coin vendor sale.", "source": "client definition (coin_store_prices empty, models empty)"},
  {"claim": "The repo notes describe the Miner collections as 'Cascading' Job Material collections, but the per-item rule is not documented.", "source": "notes/Build Guides/Content/Jobs/Miner.md:235"}
 ],
 "confidence": 0.7,
 "open": [
  "No wiki page, client line or repo record names the enemy, node, gathering action or drop rate that yields Hunk of Gold Ore. The 'Job Material' spawn type applies to the whole collection and is not a per-item source, so no drop source is listed.",
  "The 'Cascading' rule (whether entries must be obtained in order) is not documented in the evidence; do not treat it as settled.",
  "The previous answer's note about 'Sliver of Gold Ore' being a reward for Miner's Silver Ore is unrelated to this item and was not used.",
  "Onyx Gems is the set completion reward, not a source of Hunk of Gold Ore itself.",
  "No recipe in the repo uses Hunk of Gold Ore; recipes.json uses a different 'Gold Ore' item for gold bars."
 ]}
