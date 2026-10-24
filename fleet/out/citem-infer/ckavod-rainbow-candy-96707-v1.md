<!-- fleet job=citem-infer id=ckavod-rainbow-candy-96707-v1 status=nothing_found turns=5 usd=0.0041 tokens(read,write,in,out)=[36063, 19427, 12, 2686] model=claude-haiku-5-5 -->
# Kavod Rainbow Candy

{"item": {"name": "Kavod Rainbow Candy", "locale_id": 96707, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 31301 is named Kavod Rainbow Candy (locale 96707). Description: temporarily increases talent as blacksmith, chef, miner and postman. One definition, no models, no coin store price.", "source": "FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:639153-639154 (Comment and Id 31301); locale:96707"},
  {"claim": "Name appears in the client locale tables (ucdt/ugdt) across several builds, so it is a shipped client string.", "source": "FreeRealmsLocaleTools/test/FreeRealmsLocaleTools.Tests/data/en_us_data.dat:18102 and :44342 (ucdt/ugdt 686237671, 1676341206)"},
  {"claim": "A client icon asset exists named icon_activateable_micro_kavod_rainbow_candy (32/64/128 dds). The 'activateable_micro' naming suggests a consumable buff item, not a store item.", "source": "osfr-asset-manifest/Assets_manifest.txt:101140-101142"},
  {"claim": "Cluster siblings (Sparkling Assorted Cookies 96704, Sparkling Hot Dog 96705, Chrono Cupcake 96706, Western Charred Beef 96710, A Variety Gumdrop Pack 96711) are in the same client text block, so this is probably a food set. No source for any of them was found either.", "source": "locale:96704-96711; quest-lines/citem-packs.json:173648 (same pack entry, no sources)"},
  {"claim": "No wiki page, article, video frame, vendor stock line, quest reward, drop or recipe mentions Kavod Rainbow Candy. The only other hits are the same client definition in other server copies.", "source": "lookup (client, wiki, articles, video) returned only locale:96707; repo search found no vendor, store, quest or recipe reference"}
 ],
 "confidence": 0.15,
 "open": [
  "No acquisition source found. Needs a wiki page, a video, or a quest/event that names it (likely a holiday or promotional food, but unproven).",
  "No coin store price in stores.json for definition 31301; no coin vendor evidence.",
  "Live status is unsure. The client defines it and the locale carries it, but no source confirms it was sold or given in live play, so it may be unobtainable or retired.",
  "Repo hit 'Wizard's Flair Shard of Valentines' uses name_locale_id 131301, which is a different item. The 31301 match in ClientActivityDefinitions.json is a NameId coincidence, not this item. Do not merge them.",
  "Jev's first pass said source_guess 'unknown'; no evidence in the pack supports a specific source."
 ]}
