<!-- fleet job=citem-infer id=cfaded-fire-necklace-89400-v1 status=nothing_found turns=5 usd=0.0027 tokens(read,write,in,out)=[23850, 11102, 12, 2213] model=claude-haiku-5-5 -->
# Faded Fire Necklace

{"item": {"name": "Faded Fire Necklace", "locale_id": 89400, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text 'Faded Fire Necklace' is locale:89400 (item name, definition_ids 10391, slot 8, class 68); the client also carries 'Faded Fire Necklace' under other ids (2866602779, 2957838417 in en_us_data.dat), so the name spans more than one client entry.", "source": "locale:89400; client en_us_data.dat entries 2866602779 and 2957838417"},
  {"claim": "It sits in a cluster of similar elemental jewelry names (Polished Air/Wind/Void Ring, Faded Sun/Light Necklace, plus Faded Fire Ring and Polished Air Necklace elsewhere in the client). No wiki page, article, video, or vendor covers any of them.", "source": "locale:89397, locale:89398, locale:89399, locale:89403, locale:89404; client en_us_data.dat"},
  {"claim": "The client definition has an empty description and no coin store price (coin_store_prices is empty), so no coin vendor sale is evidenced.", "source": "client definition in evidence pack; repo:data/content/stores.json has no matching item 10391"},
  {"claim": "Repo and refs searches for the name, its id, and its sibling names returned no content-store, quest, recipe, or drop entry.", "source": "search repo/refs/client for 'Faded Fire|Polished Air|10391|89400'"},
  {"claim": "The first-pass tag (live yes, clothing, drop) is a model guess and is not used as evidence.", "source": "jev_first_pass"}
 ],
 "confidence": 0.15,
 "open": [
  "No source found. Every candidate (drop, quest reward, crafting, collection, event, prize wheel) needs a wiki page, article, or in-game evidence to be listed. None exists in the available sources.",
  "Live status unknown. The client defines the item, but no source confirms it was ever obtainable.",
  "Check the elemental jewelry set (Polished Air/Wind/Void Ring, Faded Sun/Light/Fire Necklace) as a group. A source for one sibling may cover this item. The pack's 'mentioned_by_other_answers' and 'vendor_stock' were empty, so no cross-reference was possible.",
  "Ask for video frames or wiki captures that show the item in a player's inventory, a drop, or a reward window.",
  "The first-pass 'drop' guess is unverified."
 ]}
