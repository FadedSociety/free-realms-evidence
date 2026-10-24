<!-- fleet job=citem-infer id=ccooker-wind-necklace-96605-v1 status=nothing_found turns=5 usd=0.0034 tokens(read,write,in,out)=[33409, 15606, 12, 2324] model=claude-haiku-5-5 -->
# Cooker Wind Necklace

{"item": {"name": "Cooker Wind Necklace", "locale_id": 96605, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name is locale:96605 'Cooker Wind Necklace' (definition 31199, slot 9 = necklace, class 64, no model files, no coin store price).", "source": "locale:96605; pack client_definition"},
  {"claim": "Sibling client names form a cooking-themed family: Cooker Air/Void/Fire/Light/Sun Necklace and Cooker Wind/Air/Void/Fire/Light/Sun Ring, plus Bordon's Air/Wind/Void/Fire/Sun/Light Necklace (locale:96619, 96620, 96621, 96607, 96610, 96611). Names alone do not give a source or a live status.", "source": "locale:96604, locale:96606, locale:96619-96621; opening-native-lobby locale en_us_data.dat lines 9066, 505, 71825"},
  {"claim": "Bordon Cloo is the Royal Chef who runs Cloo's Cooking Academy in Sanctuary and sells cooking ingredients and recipes; the family's 'Cooker' naming suggests a chef-related set, but no source states that this necklace is sold, dropped, or rewarded.", "source": "articles/articles.json 'Meet Bordon Cloo' summary; articles/facts.json line 58372"},
  {"claim": "No wiki page, image, article fact, video frame, vendor stock entry (repo prototype/osfr-tools/data/content/vendors.json has no item 31199 match; the 131199 hit is a different ID), quest reward or drop names this item.", "source": "lookup client/wiki/articles/video; search repo and refs for 'Cooker' and '31199'"}
 ],
 "confidence": 0.1,
 "open": [
  "No acquisition source found. Needs a wiki page, a vendor/quest/drop record, or a player report for the Cooker necklace family (Cooker Wind Necklace, locale 96605).",
  "Retired status and live status are unknown; the client defines the item, but nothing confirms it was ever obtainable.",
  "Whether the Cooker family belongs to a Bordon Cloo cooking vendor, a crafting recipe, or a holiday/event set is unverified; do not infer a source from the name.",
  "Pack's first-pass tag (live unsure, source unknown) is consistent with the evidence; it was not used as evidence.",
  "No critiques were carried in the pack to fix."
 ]}
