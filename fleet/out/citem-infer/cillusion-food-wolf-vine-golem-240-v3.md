<!-- fleet job=citem-infer id=cillusion-food-wolf-vine-golem-240-v3 status=nothing_found turns=2 usd=0.0019 tokens(read,write,in,out)=[5712, 8535, 6, 1523] model=claude-haiku-5-5 -->
# Illusion Food - Wolf Vine Golem

{"item": {"name": "Illusion Food - Wolf Vine Golem", "locale_id": 240, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name confirmed: locale 240 = 'Illusion Food - Wolf Vine Golem'.", "source": "locale:240"},
  {"claim": "Client description confirmed: 'Eating this food will temporarily change the player into a Wolf Vine Golem.'", "source": "locale:3154"},
  {"claim": "Enemy name 'Wolf Vine Golem' is locale 5369.", "source": "locale:5369"},
  {"claim": "Briar Patch Chugilda quest asks the player to collect haunches of meat from the Wolf Vine Golems. It names no illusion food and no reward for it.", "source": "locale:16903; locale:17066; locale:24905"},
  {"claim": "Repo stores.json has no row for item_id 2945 (search for 'Illusion Food' and '\"item_id\": 2945' found nothing), so no coin vendor sale is verified. The client definition has an empty coin_store_prices list.", "source": "repo:prototype/osfr-tools/data/content/stores.json"},
  {"claim": "Lookup of the client, wiki, articles and video for 'Illusion Food' found only sibling client locale entries (Penguin 233, Floren 236, Yeti 237, Owl 243, Bat 244, and others). No wiki page, article or video frame names the Wolf Vine Golem variant. The one wiki hit is an unrelated Bark Chocolate tooltip.", "source": "lookup 'Illusion Food' (client, wiki, articles, video)"},
  {"claim": "Earlier pack's locale ids 693851549 and 3370537470 do not exist and were dropped. Legacy Cost 180 is a definition field, not a store price, and is not used here.", "source": "id check; refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:54774-54793 (unverified this pass)"}
 ],
 "confidence": 0.2,
 "open": [
  "No source found. No vendor, quest reward, drop, event, prize wheel, crafting, or store row names item 2945 or locale 240. Sources stay empty.",
  "Legacy Cost 180 is not a verified coin price; do not wire it as one.",
  "Lead, unverified: the Briar Patch Chugilda meat quest (locales 16903, 17066, 24905) hunts Wolf Vine Golems. Check whether it rewards or the golems drop illusion food. No source says so.",
  "Sibling illusion foods (Penguin, Floren, Yeti, Owl, Bat, and others) have no wiki coverage either. A sibling-wide source, if one is found, may cover this item too.",
  "Live status unknown; no wiki, video, or store evidence shows it live in 2009-2014 or retired.",
  "One definition, no models or tints, so variant count is 1."
 ]}
