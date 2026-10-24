<!-- fleet job=citem-infer id=cbrittle-ethereal-triangle-shard-69777-v2 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[4888, 10497, 6, 1457] model=claude-haiku-5-5 -->
# Brittle Ethereal Triangle Shard

{"item": {"name": "Brittle Ethereal Triangle Shard", "locale_id": 69777, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Unidentified coin store, category 121 (no NPC or vendor name found in the repo or client text). Store row for item 22875.", "where": null, "price": "811 coins purchase; 729 coins with 10% member discount; sell-back 81 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 22875 (line 6730)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale:69777 'Brittle Ethereal Triangle Shard', one of a nine-item set (locale 69772-69780) of Brittle/Burning/Eternal shard names.", "source": "locale:69777"},
  {"claim": "The client definition's definition_id 22875 has a coin store row in category 121: purchase 811 coins, member discount 10%, member price 729, sell price 81, not no_sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 22875 (line 6730)"},
  {"claim": "Neighbouring category-121 rows 22856-22885 carry purchase prices of 811, 1149, 1656 or 2363 coins, so this is a priced shard family in one store category.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 6711-6735"},
  {"claim": "Lookup of the item name returns only the client text line locale:69777; no wiki page, article, image or video names this item.", "source": "lookup (client, wiki, articles, video), checked for this brief"},
  {"claim": "The source_tags R1, R2, T633 and L1-L4 are data-source tags and do not establish a live date.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 22875"}
 ],
 "confidence": 0.4,
 "open": [
  "The vendor NPC and zone for store category 121 are not identified. The only evidence is the internal store row, so the vendor type rests on store data alone.",
  "Live status is unconfirmed. The first-pass tag 'yes' is a hint only and was not used. No wiki or forum source confirms it is or was sold.",
  "Retirement date is unknown; no source states one.",
  "The client definition has an empty description and no models. Its use (crafting input, collection, or other) is undocumented, so kind 'other' is a placeholder.",
  "No quest reward, enemy drop, crafting recipe, prize wheel, or event source was found."
 ]}
