<!-- fleet job=citem-infer id=cusa-wrecker-chassis-3726-v1 status=nothing_found turns=3 usd=0.0029 tokens(read,write,in,out)=[13590, 13939, 8, 2093] model=claude-haiku-5-5 -->
# USA Wrecker Chassis

{"item": {"name": "USA Wrecker Chassis", "locale_id": 3726, "kind": "part"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name string is 'USA Wrecker Chassis' (locale 3726); description 'The chassis for the USA Wrecker.' is locale 114648; definition id 60681, slot 0, item class 121.", "source": "locale:3726; locale:114648; pack client_definition"},
  {"claim": "Part of the USA Wrecker kart's part set: sibling client strings USA Wrecker (locale 3649), USA Wrecker Engine (403151), USA Wrecker Turbo (403152), USA Wrecker Steering Mod (403153), USA Wrecker Shock Absorbers (403154). Item is a kart part, not a kart itself.", "source": "lookup client results; refs opening-harvesting-native-20261009T142624Z/locale/en_us_data.dat"},
  {"claim": "The client also carries a 'USA Wrecker' item label (ugdt 1695113607 / ucdt 60319678, locale 3649), which the pack's sibling chain does not link to a source.", "source": "refs locale en_us_data.dat lines 1569, 44828"},
  {"claim": "Kart parts in the game are progression items for the Racing/Demolition Derby job; wiki and notes describe Racing Kart parts (engines, tires, turbos) with power ratings but no per-part source list.", "source": "notes/Build Guides/Gameplay/Kart Racing.md:24; notes/Research/Pieces/041 Racer and derby progression.md:44-52"},
  {"claim": "Not found in any wiki page, article, video frame, coin vendor stock, or store row. No coin store price in the client definition.", "source": "lookup wiki/articles/video 'USA Wrecker' returned no matches beyond client text; pack coin_store_prices []"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found. Vendor stock, quest rewards, drops, crafting, and store listings for this chassis are all unknown; do not assume it is a vendor sale because the first-pass guess said 'vendor'.",
  "Sibling part 'Cutlass Wrecker' and other derby karts are sold in the Station Cash Marketplace (per notes/Build Guides/Content/Jobs/Demolition Derby Driver.md:197), but that is for complete karts, not chassis parts; no evidence links those listings to the USA Wrecker chassis.",
  "Whether the USA Wrecker kart and its parts were ever sold, rewarded, or retired is unknown. Check the Station Cash/promotional history for the USA Wrecker kart (locale 3649) first; the parts may follow that kart's source.",
  "The client cluster (Raylen, Farmer Darrel, Farmer Brambleback, 'Doggy Costume Pieces') sits next to this item in the string table, but no string ties the chassis to any of those NPCs or quests. Do not treat that as a source.",
  "The item is labeled 'live: unsure'. Whether it is in the live catalogue at all is unverified."
 ]}
