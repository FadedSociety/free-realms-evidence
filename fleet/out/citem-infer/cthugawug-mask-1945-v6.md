<!-- fleet job=citem-infer id=cthugawug-mask-1945-v6 status=done turns=3 usd=0.0041 tokens(read,write,in,out)=[25110, 19198, 8, 2900] model=claude-haiku-5-5 -->
# Thugawug Mask

{"item": {"name": "Thugawug Mask", "locale_id": 1945, "kind": "clothing"},
 "sources": [
  {"type": "other", "detail": "Quest-step item in 'Unmasking the Bandits' (Glugmort sends the player into the Bandit Hideout to take Muggenstomp's bandit mask; the player then presents it to Wompugg). Name-matched only: the repo quest data names an item 'Thugawug Mask' (ucdt 1638456300) but nothing ties that ucdt to definition 2597 / locale 1945. Pickup mechanic (scripted on kill vs. drop roll) not recorded. Not a confirmed acquisition of this definition.", "where": "Bandit Hideout (Greenwood Forest); hand-in to Wompugg near Farnum Farmstead", "price": null, "currency": null, "source": "locale:38594 ('Enter the Bandit Hideout and retrieve Muggenstomp's bandit mask, then present it to Wompugg with my regards.'); locale:38599; locale:38601 (Wompugg: 'Why are you giving me this Thugawug mask?'); repo:prototype/osfr-tools/data/content/npcs/farnum_farmstead.json line 10470; repo:notes/Build Guides/Content/NPCs/NPCs - Farnum Farmstead.md line 155 (unconfirmed link)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Thugawug Mask' is locale 1945; definition 2597, class 69, slot 0; description 'A \"Qualitee\" Thugawug disguise.' (the same text pattern as locale 1969). It is a cosmetic disguise, not a consumable or quest-only object by its definition.", "source": "locale:1945; locale:1969; client definition"},
  {"claim": "'Qualitee' disguise set: 1967 Robgoblin, 1968 Plant, 1969 Thugawug, 1970 Baby Penguin.", "source": "locale:1967, locale:1968, locale:1969, locale:1970"},
  {"claim": "Locale 11569 says 'Donning this mask will temporarily turn the player into a thugawug bandit for a long time.' Its owning item is not identified, so it is not tied to 2597 here.", "source": "locale:11569"},
  {"claim": "The quest text names a Thugawug mask that Muggenstomp's bandit mask is taken from and handed to Wompugg; the item link is name-matched only.", "source": "locale:38594; locale:38601; repo:prototype/osfr-tools/data/content/npcs/farnum_farmstead.json line 10470"},
  {"claim": "No coin store price in the client definition and no vendor stock entry for 2597. Sibling-set vendor rows were NOT searched in stores.json in this pass, so this is not a verified negative for the set.", "source": "client definition"},
  {"claim": "Free-text search of the repo, client and wiki/articles finds no wiki page, article, or video for 'Thugawug Mask' or 'Qualitee' disguises.", "source": "repo search; locale search; lookup (no matches)"}
 ],
 "confidence": 0.3,
 "open": [
  "Quest link unconfirmed: ucdt 1638456300 is not mapped to definition 2597 / locale 1945 anywhere in the repo. Resolve before wiring the quest source.",
  "Locale 11569 (thugawug bandit mask effect) may belong to this item or to a different mask; if it is this item, it is a costume with a temporary effect.",
  "Qualitee set siblings (1967 Robgoblin, 1968 Plant, 1970 Baby Penguin) were not searched in stores.json/vendors.json for a vendor, prize or promotion row. The Robgoblin disguise is not verified as sold by any booth: the earlier cited locales 1462237798 and 2727499100 do not exist and were removed.",
  "Pickup mechanic for the quest mask (scripted on Muggenstomp kill vs. drop roll) is not recorded.",
  "Earlier-cited locales 38497 and 38596 did not resolve and were dropped.",
  "No source states the item is retired or currently available; live status is unsure.",
  "Price: none found. Wireable only after the quest link or a set vendor row is confirmed."
 ],
 "critiques_addressed": "Removed nonexistent locale citations (1462237798, 2727499100) and unresolved 38497/38596; kind changed from 'other' to 'clothing' per the disguise description and slot 0; quest source marked name-matched; no-vendor claim downgraded to unsearched; retired left null."}
