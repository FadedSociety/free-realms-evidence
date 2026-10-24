<!-- fleet job=citem-infer id=cprivateer-speedster-39225-v1 status=nothing_found turns=4 usd=0.0042 tokens(read,write,in,out)=[30503, 16691, 10, 3642] model=claude-haiku-5-5 -->
# Privateer Speedster

{"item": {"name": "Privateer Speedster", "locale_id": 39225, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Privateer Speedster is a racing-kart vehicle (client description: 'For stealing the win at the race track finish line.'), in the Speedster kart family of Kart Racing (Racing Karts list, Blast Speedster).", "source": "locale:39225; notes/Build Guides/Gameplay/Kart Racing.md:24"},
  {"claim": "The client has Privateer Speedster Chassis, Engine, Turbo, Tires, Steering Column and Mod parts, so it is a kart body with per-kart parts, not a single item.", "source": "lookup client: locale:114830, 117430, 117431, 117433, 117432, 117434; locale:117543-117547 (line texts tagged to the name)"},
  {"claim": "Speedster karts are in the 70-row vehicle catalogue (item Type 11, CategoryId 127) with a Cost of 540 on priced rows. The catalogue itself was not checked row by row for Privateer Speedster, so this does not show the item's price.", "source": "notes/Research/Pieces/041 Racer and derby progression.md:48-50"},
  {"claim": "The only Speedster kart with a confirmed source is Blast Speedster, a 1-item reward from Sandstorm's Grand Opening (Bill Riddly, Sandstorm Speedway, Seaside). This is not Privateer Speedster.", "source": "notes/Build Guides/Content/Jobs/Kart Driver.md:25 and :142; video MJkBn2nwbVU/00216 (as cited there)"},
  {"claim": "Bear Wrecker and Cutlass Wrecker (adjacent names in the same locale block 39229-39230) are Derby Karts sold in the Station Cash Marketplace, Cutlass Wrecker 700 Station Cash (630 for members). This is about derby karts, not Privateer Speedster, so it is not a source for it.", "source": "notes/Build Guides/Content/Jobs/Demolition Derby Driver.md:197 (wiki Derby Karts pages)"},
  {"claim": "No store row, coin vendor stock, wiki page, article fact, or video frame names Privateer Speedster. The client definition has no coin_store_prices.", "source": "lookup wiki/articles/client/video for 'Privateer Speedster' (no wiki or article hits); repo search for 'Privateer' (only locale data files and notes); refs search for 'Speedster' (no store or drop rows)"}
 ],
 "confidence": 0.15,
 "open": [
  "No source found. Nothing in the repo, wiki, articles, video or client names how Privateer Speedster is obtained. Do not add a source without evidence.",
  "Kind: the first-pass tag says 'mount', but this is a racing kart (vehicle). The schema has no vehicle kind, so 'other' is used here. The rebuild may need a vehicle category.",
  "Live status is unknown. The first-pass tag says 'yes' with no evidence; nothing confirms it is live or retired.",
  "The description ('stealing the win at the race track finish line') suggests a race reward or event, but no quest, race, or event names it. Check the Kart Racing quests (SG Tour 400, Tangletrack challenges, Lightning Cup) and race payout tables, if recovered, for this kart.",
  "Check the Speedster karts' store or vendor rows (Cost 540 in the vehicle catalogue) to see whether Privateer Speedster has a price. The catalogue row for definition 56981 was not verified; the note only says Cardie Racer 48318/7 and similar rows match the catalogue.",
  "The client name 'Privateer Speedster' also has Chassis, Engine, Turbo, Tires, Steering and Mod parts (locale 114830, 117430-117434). Those part items may have their own sources that are not recorded here.",
  "Definition 56981 is adjacent to Barbed Crusher 56995/40 in the vehicle catalogue (notes/Research/Pieces/041). Adjacent ids are not evidence of a shared source."
 ]}
