<!-- fleet job=citem-infer id=cn-storm-strike-boots-pl-storm-strike-boots-628-v1 status=nothing_found turns=3 usd=0.0022 tokens(read,write,in,out)=[12091, 9218, 8, 1856] model=claude-haiku-5-5 -->
# {n}Storm Strike Boots{pl="Storm Strike Boots"}

{"item": {"name": "Storm Strike Boots", "locale_id": 628, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name text: locale:628 is '{n}Storm Strike Boots{pl=\"Storm Strike Boots\"}', kind item.", "source": "locale:628"},
  {"claim": "Set siblings in client text: Storm Strike Hoodie (locale:623), Storm Strike Gloves (locale:633), Storm Strike Leggings (locale:638), Storm Strike Quiver (locale:643). Savage Sting set is the neighbouring set (locale:625, 630, 25271).", "source": "locale:623, locale:633, locale:638, locale:643, locale:625, locale:630"},
  {"claim": "The coin price 291 in stores.json is shared by dozens of unrelated item_ids (e.g. 109, 112, 113, 115, 135); none of the 12 definition_ids (431, 1225, 1283, 1341, 11356, 11357, 11363, 11366, 11368, 11369, 11371, 11372) appears as an item_id in the store data. The price link to this item is therefore not verified.", "source": "repo:prototype/osfr-tools/data/content/stores.json (lines 86-222)"},
  {"claim": "No wiki page, article fact, video frame, vendor stock line, or other answer names Storm Strike Boots. The only wiki hit is an unrelated Hess/Savage Sting Bow Recipe page, which mentions a Savage Sting recipe, not these boots.", "source": "lookup wiki query 'Storm Strike Boots' (no page); wiki page Hess"}
 ],
 "confidence": 0.2,
 "open": [
  "No source for any acquisition route. The coin_store_prices 291 field is not tied to this item in stores.json, so the 'coin_shop' guess from the first pass is unconfirmed. Do not record a 291-coin price without a store row for one of the definition_ids.",
  "Live status unknown. The first-pass 'live: yes' is a hint only; no wiki or article evidence confirms it.",
  "Storm Strike set (Hoodie, Gloves, Leggings, Quiver) appears in the client text beside this item. Check whether the set is a Savage Sting-era crafting or promotion set (the Savage Sting Bow Recipe on the Hess wiki page is a possible lead) before assigning a source.",
  "The 18 definitions (12 listed IDs) are tints/races; the client does not say which variant was sold where.",
  "The first-pass critiques were not in the pack, so none were fixed."
 ]}
