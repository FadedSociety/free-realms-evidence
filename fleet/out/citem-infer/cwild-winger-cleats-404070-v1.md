<!-- fleet job=citem-infer id=cwild-winger-cleats-404070-v1 status=done turns=7 usd=0.0063 tokens(read,write,in,out)=[83638, 26127, 16, 4364] model=claude-haiku-5-5 -->
# Wild Winger Cleats

{"item": {"name": "Wild Winger Cleats", "locale_id": 404070, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Fred Futbol, the \"Soccer Star Gear\" vendor (client name 3922/ucdt 4036414402; video title). Stock is listed only as \"Soccer Star gear\"; the Cleats item itself is not confirmed in his stock.", "where": "Snowhill, Snowhill Soccer Field (next to the Left Side Soccer Gate, near Perry's Pasture)", "price": null, "currency": null, "source": "notes/Build Guides/Content/NPCs/NPCs - Snowhill.md row 126 (client + video X35ewgMjcAM/00036, WjpJl2U5OK0/00016); notes/Build Guides/Content/Jobs/Soccer Star.md line 42 and line 195; prototype/osfr-tools/data/content/npcs/snowhill.json:16210-16228; vendors_unresolved.json:305-320"}],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item 404070 is 'Wild Winger Cleats', with 34 definitions (variants) and a slot/class for feet cleats; Elite Pink and Elite Black versions exist (404075, 404076).", "source": "locale:404070; locale:404075; locale:404076; client definition in pack"},
  {"claim": "Wild Winger is a Soccer Star gear set: the client has Wild Winger Jersey, Shin Guards, Shorts, Bandana and Cleats pieces, and the Soccer Star note groups them under 'Soccer Star Gear' and 'Soccer Cleats'.", "source": "notes/Build Guides/Content/Jobs/Soccer Star.md lines 193-195; FreeRealmsLocaleTools en_us_data.dat (Wild Winger Cleats, 294484428; Elite Black Wild Winger Cleats, 2572333394)"},
  {"claim": "Fred Futbol at Snowhill Soccer Field is the only identified gear vendor for the set; his stock and prices were not captured.", "source": "notes/Build Guides/Content/Jobs/Soccer Star.md line 42 ('Stock and prices not see[n]')"},
  {"claim": "The pack's coin store prices (750, 752) are NOT evidence for this item. No stores.json entry uses item_id 61640-61653 (the definition ids). 752 is a generic price value that appears on many unrelated items (e.g. stores.json item_id 75762), and item 752 itself is a different item at 9453 coins.", "source": "repo:prototype/osfr-tools/data/content/stores.json (search of item_id 6164x-6165x; item 752 at line 350; purchase_price_coins 752 at lines 8501+)"},
  {"claim": "No wiki page, article, or video names Wild Winger Cleats; the lookup returned no matches.", "source": "lookup wiki/articles/video for 'Wild Winger Cleats' and 'Winger Cleats athletics' (no matches)"}
 ],
 "confidence": 0.35,
 "open": [
  "Price: no verified coin price. The client's 750/752 are not linked to these definitions in stores.json; do not use them. Fred Futbol's prices are not captured.",
  "Whether Fred Futbol actually sells the Cleats (vs. other Soccer Star gear, which is the only stock text) is unverified; the vendor stock is listed only as 'Soccer Star gear'. Needs a live check or a vendor stock capture.",
  "Level/rank requirement and whether the Cleats are a Soccer Star job reward or a Fred Futbol purchase are unknown (Soccer Star.md line 193 says level/rank is unknown for every piece).",
  "Retired status and whether the set is still sold later are unknown; no source states it.",
  "Other possible sources (quest rewards from the Soccer Star questline, drops, Coin Shop, Marketplace, prize wheel) were not found in the pack and are not sourced here.",
  "The 'Wild Winger' set has 34 variant definitions; only the base feet cleats model (athletics_<race>_<gender>_feet_cleats.adr) is confirmed, not each tint/race."
 ]}
