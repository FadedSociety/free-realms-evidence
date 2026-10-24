<!-- fleet job=citem-infer id=ccelebration-conditioner-393213-v1 status=done turns=3 usd=0.0020 tokens(read,write,in,out)=[11076, 8002, 8, 1687] model=claude-haiku-5-5 -->
# Celebration Conditioner

{"item": {"name": "Celebration Conditioner", "locale_id": 393213, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 56780 is named 'Celebration Conditioner' (locale 393213), description 'This shampoo improves your pet's cleanliness and has other cool effects.', slot 201, class 73, no model files, one variant, no coin store price.", "source": "client definition (pack)"},
  {"claim": "Locale 393213 is also the only client line tagged to the name; the tag reads quest_title, but the same string sits in the client item-name table as ucdt 1375332461 'Celebration Conditioner' next to 'Super Cleansing Shampoo' (ucdt 1206841253) and 'Valentine Conditioner' (ucdt 1272224864).", "source": "opening-native-lobby-20261009T163603Z/locale/en_us_data.dat:36479; opening-mining-starter-20261009T180011Z/locale/en_us_data.dat:36479"},
  {"claim": "The quest_title tag on 393213 is a mis-tag: the string is an item name, and the quest-title use is a shared text id, not evidence of a quest reward.", "source": "locale:393213 (lookup returned it as quest_title only)"},
  {"claim": "No wiki page, article, video frame, vendor stock line (repo data/content/vendors.json, stores.json) or repo reference to item 56780 or this name was found.", "source": "lookup (wiki, articles, client, video); search repo and refs"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source is evidenced. The first-pass 'marketplace' guess has no support: there is no Station Cash price in the client definition and no SC Marketplace wiki entry.",
  "The neighbouring client lines (Super Cleansing Shampoo, 'Valentine Conditioner', test quest and devtest strings at locale 393208-393216) suggest a dev/test or seasonal pet-care set, but no source confirms it was ever sold, dropped or given out. Not confirmed live.",
  "Needs a check of the pet-care item sets (Super Cleansing Shampoo, Valentine Conditioner) and of any holiday pet item list before assigning a source.",
  "The locale tag quest_title for 393213 should be corrected to item in the client text table."
 ]}
