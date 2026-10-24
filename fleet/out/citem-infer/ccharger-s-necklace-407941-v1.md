<!-- fleet job=citem-infer id=ccharger-s-necklace-407941-v1 status=nothing_found turns=5 usd=0.0040 tokens(read,write,in,out)=[36287, 16843, 12, 3148] model=claude-haiku-5-5 -->
# Charger's Necklace

{"item": {"name": "Charger's Necklace", "locale_id": 407941, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name and description: 'This necklace increases your tackle power.' Slot 8, class 136, one definition (id 67932), no coin store price.", "source": "locale:407941; locale:407953 (generic 'necklace' description); repo search found no stores.json entry for 67932"},
  {"claim": "Same-set family in client text: Jolter's Necklace (407940), Charger's Necklace (407941), Champion's Necklace (407942), Jolter's/Charger's/Champion's Ring (407943-407945), and Power Shards/Square Shards (407934-407939, 407946).", "source": "locale:407936-407946; locale:407934"},
  {"claim": "Closest sibling text, 'Blasting Necklace', is a soccer tackle-power necklace; the Charger line is probably the same tackle/soccer-style accessory family, but no source confirms that.", "source": "locale:407799"},
  {"claim": "Wiki search finds no page, image or article naming Charger's Necklace or the Jolter/Charger/Champion family; lookup for the name returned only client text.", "source": "lookup wiki/articles/video, queries 'Charger Necklace', 'Jolter', 'tackle power necklace'"},
  {"claim": "No vendor, quest, drop or event in the repo ties item 67932 to a source.", "source": "repo search for 67932 / 407941 / Jolter / Charger's (no hits in data or notes)"}
 ],
 "confidence": 0.1,
 "open": [
  "No source found. The first-pass 'drop' guess has no evidence behind it and is not used.",
  "Client text lists 'Jolter', 'Charger' and 'Champion' tiers (necklaces, rings, shards) that look like a tiered set, possibly a soccer/tackle-power or Daily Wheel set. The Champion tempered circle shard is a Daily Wheel item (wiki), but that is a different item and does not prove the Charger's Necklace source. Check the Daily Wheel and the soccer/sports prize lists for these names.",
  "Kind is a guess: a worn necklace in slot 8 is closest to 'clothing'; confirm against how the rebuild classes accessories.",
  "Live status unknown: the client defines it, but no store, wiki or drop evidence says it was sold or dropped, and the 'live: yes' first pass is not evidence."
 ]}
