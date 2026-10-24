<!-- fleet job=citem-infer id=cfisher-s-biomass-triangle-shard-30656-v2 status=done turns=3 usd=0.0029 tokens(read,write,in,out)=[19101, 14099, 8, 1953] model=claude-haiku-5-5 -->
# Fisher's Biomass Triangle Shard

{"item": {"name": "Fisher's Biomass Triangle Shard", "locale_id": 30656, "kind": "other"},
 "sources": [{"type": "coin_shop", "detail": "Coin store listing, store category 121 (shard row; the NPC vendor for category 121 is not named in repo data)", "where": "Coin store, category 121 (vendor and zone unknown)", "price": "866 coins purchase; 779 coins for members (10% member discount); sell-back 86 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 609 (item_id 2139, category_id 121, purchase 866, member 779, sell 86, no_sale false)"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name for definition 2139 is \"Fisher's Biomass Triangle Shard\", locale 30656, in the shard cluster 30651-30661.", "source": "locale:30656"},
  {"claim": "stores.json line 609 has item_id 2139, category 121, purchase 866, member 779 (10% off), sell 86, no_sale false. I re-read the line and the values match the pack.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 609"},
  {"claim": "Neighbouring rows 2118-2143 are all category 121 with the same tag set, so the tag set does not show current sale. Live status is therefore not established by the tags.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 600-613"},
  {"claim": "The collection_catalogue entry with id 2139 (under collection 304) is a different item (name_id 6169), so it is not this shard.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json line 22893"},
  {"claim": "Lookup on the name returns only client locale lines (30655, 30656, 30657 and the Amatuer/All-Star shard names). No wiki page, article, video, quest or drop names this item.", "source": "lookup: \"Biomass Triangle Shard\" (client)"}
 ],
 "confidence": 0.4,
 "open": [
  "The store row is keyed item_id 2139, and the pack links it to definition 2139 and locale 30656. Nothing in the repo confirms that item_id is the definition id. Store rows for the neighbouring shards are keyed in the same 2118-2143 range, which supports the link but does not prove it. This is the main gap.",
  "The vendor NPC and zone for store category 121 are not in the repo data. The source type is set to coin_shop, not vendor, because no NPC stock row names a vendor.",
  "The 866-coin price has no wiki, forum or video confirmation. It comes only from our store data.",
  "Retired status is unknown. No source states whether the shard is still sold or was removed.",
  "Live is unsure. The store row exists, but the shared source tags do not show current sale.",
  "The client description is empty, so the item's use (crafting input, collection piece or other) is unknown. Kind stays other as a placeholder.",
  "Other shards in the same name cluster (30651-30655, 30657, 30661) are not verified here; the earlier claim that the whole family is sold together rests on the same unverified keying and is withdrawn."
 ]}
