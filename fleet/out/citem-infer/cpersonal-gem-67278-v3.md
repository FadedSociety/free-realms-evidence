<!-- fleet job=citem-infer id=cpersonal-gem-67278-v3 status=done turns=3 usd=0.0019 tokens(read,write,in,out)=[11447, 7072, 8, 1706] model=claude-haiku-5-5 -->
# Personal Gem

{"item": {"name": "Personal Gem", "locale_id": 67278, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Member of the Miner's Special Gems collection (Cascading, Rare, Job Material; collection reward Magical Summoning Ore). Membership only: no per-item acquisition source is evidenced.", "where": null, "price": null, "currency": null, "source": "wiki: Job Specific (Collections) (lists [Personal Gem] under Miner's Special Gems, between Memorable Gem and Peculiar Gem); repo:prototype/osfr-tools/data/content/collections.json:4116-4121 and 4131"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item 'Personal Gem', locale 67278, description 'This item can be added to the Miner's Special Gems Collection'.", "source": "locale:67278"},
  {"claim": "The wiki's Job Specific (Collections) page lists Personal Gem under Miner's Special Gems.", "source": "wiki: Job Specific (Collections)"},
  {"claim": "collections.json lists Personal Gem (source_tag 'wiki') in the Miner's Special Gems collection, whose spawn_type is 'Job Material'.", "source": "repo:prototype/osfr-tools/data/content/collections.json:4116-4121, 4131"},
  {"claim": "No coin store price exists for this item; no vendor stock, quest, enemy drop, event, prize wheel, or promotion source was found.", "source": "repo:data/content/stores.json (no entry; client coin_store_prices empty)"},
  {"claim": "The previous answer's 'Miner job material node' spawn is not evidenced for this item. The collection's spawn_type describes the collection, and Miner.md:235 gives only the general rule that job-material spawns appear in mines while the Miner job is active. Node type and zones are unknown.", "source": "repo:notes/Build Guides/Content/Jobs/Miner.md:235"}
 ],
 "confidence": 0.3,
 "open": [
  "Acquisition is unknown: no source names a node, zone, or spawn rate that yields Personal Gem. The earlier 'mined from gem nodes' claim is removed as unsupported.",
  "Wireable: false. Needs a zone list or per-item spawn evidence before a builder can wire an acquisition.",
  "Live status unsure: the wiki gives no retirement note, but no dated source confirms it is currently obtainable. retired left null.",
  "The critique's 'drop' classification was not adopted; the only evidenced relation is collection membership."
 ]}
