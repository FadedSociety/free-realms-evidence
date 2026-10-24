<!-- fleet job=citem-infer id=cveggie-surprise-1226-v1 status=nothing_found turns=6 usd=0.0037 tokens(read,write,in,out)=[58345, 14790, 14, 2542] model=claude-haiku-5-5 -->
# Veggie Surprise

{"item": {"name": "Veggie Surprise", "locale_id": 1226, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Veggie Surprise' is locale 1226, tagged item; description: 'Eating this food will temporarily change the player into a Fungal Man-Eating Plant.' Definition 4067, class 9, slot 0, no models, no coin store price.", "source": "locale:1226; client definition pack"},
  {"claim": "It sits in a contiguous food cluster (locale 1221-1231: Troll Porridge, Troll Dream Mix, Troll Fruit Snack, Forest Troll Lemonade, Vine Noodles, Veggie Surprise, Illusion Food - Fungal Vinegolem Wolf/Bear, Illusion Food - Evil Wolf, Shambler Cake, Shambler Pie). The cluster shows it is a transformation food, not that it has a source.", "source": "locale:1221-1231"},
  {"claim": "Its name/description is a transformation food ('change the player into'), the same family as the Illusion Food and Shambler food items; the wiki 'Items' list page names 'Vine Noodles' among food items, but that list gives no source, price, or vendor for this item.", "source": "wiki page:ns0 'Items' (Vine Noodles entry)"},
  {"claim": "Repo stores (data/content/stores.json) have no coin store price for item 4067; no vendor, quest, recipe or drop mentions it. Lookups for 'Shambler Pie', 'Shambler Cake', 'Troll Porridge', 'Illusion Food' and 'Fungal Man-Eating Plant' returned no wiki article or article fact covering the item; no video frames found.", "source": "repo search for 4067; lookup wiki/articles/video; refs search"}
 ],
 "confidence": 0.15,
 "open": [
  "No evidence for any source. The first-pass guess of 'drop' is unsupported and is not used.",
  "No wiki article, article fact, video frame, vendor stock line, quest reward, or enemy drop names Veggie Surprise.",
  "Unknown whether it is live, retired, or was ever sold. Needs a check of the food-item family (Troll/Shambler/Illusion foods) in the live-era sources or a player-report source.",
  "The 'Items' wiki list names Vine Noodles, so the food family may have a wiki page or a crafting/cooking source that was not found under this name."
 ]}
