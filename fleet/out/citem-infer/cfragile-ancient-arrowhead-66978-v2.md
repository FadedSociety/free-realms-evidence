<!-- fleet job=citem-infer id=cfragile-ancient-arrowhead-66978-v2 status=done turns=3 usd=0.0023 tokens(read,write,in,out)=[15290, 9752, 8, 1761] model=claude-haiku-5-5 -->
# Fragile Ancient Arrowhead

{"item": {"name": "Fragile Ancient Arrowhead", "locale_id": 66978, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name for definition 23365 is 'Fragile Ancient Arrowhead' (locale:66978); description (locale:132429) says it 'can be added to the Ancient Arrowhead Artifacts Collection'. It is a collection member, not the collection itself.", "source": "locale:66978; locale:132429; client definition 23365"},
  {"claim": "Definition 23365 is listed as index 3 (id 1240, name_id 66978) in the collection catalogue, item_link 'sanctuary', among the eight arrowhead variants (66976-66983).", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:13395"},
  {"claim": "Collection 'Ancient Arrowhead Artifacts' (locale:67536) is defined in the repo collections data and on the wiki page 'Ancient Arrowhead Artifacts', which lists the eight members and a collection reward of 20 Coins for completing the collection (not for this item).", "source": "repo:prototype/osfr-tools/data/content/collections.json:10854; wiki page: Ancient Arrowhead Artifacts"},
  {"claim": "Wiki 'List of Collections' places the collection under the 'Common' heading. This is a wiki category only and implies no drop source.", "source": "wiki page: List of Collections"},
  {"claim": "Video frame video:p5sDafXSQtQ/00116.jpg shows the collection progress overlay '[Ancient] [Arrowhead] [Artifacts] (4/8)' (corrected from 00114, which has the same text).", "source": "video:p5sDafXSQtQ/00116.jpg"},
  {"claim": "No coin store price (client coin_store_prices empty), no vendor stock, no quest reward, drop, event, or crafting source names this item in the pack or the searched repo/wiki/client text.", "source": "pack; repo search for 23365 / 'Fragile Ancient Arrowhead'"}
 ],
 "confidence": 0.35,
 "open": [
  "How players obtain the individual Fragile Ancient Arrowhead is not documented anywhere available. Sources list is empty, so it is not wireable as a sourced item.",
  "live is unsure: the first-pass 'yes' had no source. The collection appears in wiki and video, which shows the collection existed in-game, but that does not confirm this member is still obtainable.",
  "Retired status unknown; no source says retired or unobtainable.",
  "Corrections from critiques: the earlier cite locale:2373510970 does not exist and has been dropped (the 'Arrowhead' string in the client is locale:117095, unrelated). The mining quest 'Miner: Arrowheads for Lugabow' (locale:77600) makes iron/tin arrowheads, not Ancient Arrowheads, and is not used as a source. The 20-coin reward belongs to collection completion, not this item.",
  "Next step: check the Sanctuary/collection reward flow or a video showing an arrowhead drop/pickup (search video for 'Fragile Ancient Arrowhead') to find how members are earned."
 ]}
