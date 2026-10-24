<!-- fleet job=citem-infer id=cslag-scorched-shirt-5926-v1 status=nothing_found turns=5 usd=0.0044 tokens(read,write,in,out)=[45154, 18196, 12, 3396] model=claude-haiku-5-5 -->
# Slag Scorched Shirt

{"item": {"name": "Slag Scorched Shirt", "locale_id": 5926, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Slag Scorched Shirt' is locale 5926; it is one of a Blacksmith-job gear family (Slag Scorched / Blaze Branded / Ash Branded shirts, aprons, boots, gloves, goggles) with Elite Pink and Elite Black variants.", "source": "locale:5926; locale:5925; locale:5929; locale:5930; locale:5931; locale:5958; locale:5945; locale:5948; locale:35219"},
  {"claim": "Slot 3, class 14, model worker_<race>_<gender>_chest_rolledshortslvshirt.adr: a chest shirt used by worker/job gear.", "source": "client definition pack (15 definitions, ids 1374, 20946-20965)"},
  {"claim": "The wiki's Blacksmith job trainers (Seppa, Hess, Samune, Wayland, Masa, Keller, Fry) sell 'X Blacksmith Shirt' items (Punching, Upsetting, Welding, Refining, Drawing, Bending, Combining, Tempering, Forging). None of them is named 'Slag Scorched Shirt'.", "source": "wiki pages Seppa, Hess, Samune, Wayland, Masa, Keller, Fry (lookup wiki)"},
  {"claim": "Repo vendor data lists 'Refining Blacksmith Shirt' (item 75822) at 752 coins, a Hess sale. This is a different item and is not evidence for the Slag Scorched Shirt.", "source": "repo:prototype/osfr-tools/data/content/vendors.json:4067-4070"}
 ],
 "confidence": 0.2,
 "open": [
  "No source found. No wiki page, article, video frame, vendor stock row, quest, drop, or event names 'Slag Scorched Shirt'.",
  "The pack's coin_store_prices [464, 9453] are bare prices, not item ids. Searching stores.json for the 12 definition_ids (1374, 20946, 20949-20953, 20956, 20958, 20961, 20964, 20965) found no rows. Price 464 and 9453 occur in stores.json on many unrelated items, so they cannot be tied to this item. Not cited as a coin_shop source.",
  "Client shows Blacksmith-family shirts with tier names, so the Slag Scorched Shirt is probably a job-tier or crafted variant of the Blacksmith gear. This is a guess; it is not confirmed by any source.",
  "Pack's first-pass guess 'vendor' is unverified. The live status is unsure until a source is found.",
  "Check the Blacksmith job-gear crafting recipes and the Blacksmith job tier vendor stock for the Slag Scorched set, and check whether the Elite Pink variants came from a promotion or the Coin Shop."
 ]}
