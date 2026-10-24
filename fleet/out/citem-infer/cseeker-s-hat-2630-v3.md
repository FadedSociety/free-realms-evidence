<!-- fleet job=citem-infer id=cseeker-s-hat-2630-v3 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[7033, 9574, 6, 1862] model=claude-haiku-5-5 -->
# Seeker's Hat

{"item": {"name": "Seeker's Hat", "locale_id": 2630, "kind": "clothing"},
 "sources": [
  {"type": "drop", "detail": "Rare Exploration coin spawn (collection reward; the collection's own name is unrecovered). Reward block lists Seeker's Hat and Seeker's Backpack together.", "where": "world, Rare Exploration coin spawns (area not recorded, area: null)", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collections.json:1771-1785 (wiki_type Exploration, quality Rare, spawn_type Coin, reward.wiki_lines); wiki page Exploration (Collections) https://freerealms.fandom.com/wiki/Exploration_(Collections) (named as the provenance in collections.json:1786-1790, not read directly); video:Y_ANZvYraKI/00018.jpg (\"You receive 1 Seeker's Hat\" on a Rare Exploration Coin prompt, Adventurer 15)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 2630 is \"Seeker's Hat\"; it sits in the 2625-2632 Explorer/Seeker clothing cluster.", "source": "locale:2630"},
  {"claim": "Collection reward block names Seeker's Hat and Seeker's Backpack, spawn_type Coin, quality Rare, wiki_type Exploration; item_id and client_reward_id are null.", "source": "repo:prototype/osfr-tools/data/content/collections.json:1771-1785"},
  {"claim": "Video frame shows the hat received from a Rare Exploration Coin prompt at Adventurer 15.", "source": "video:Y_ANZvYraKI/00018.jpg"},
  {"claim": "Hat name appears in a later head-slot list; this shows presence in a list, not current availability.", "source": "video:S66oho43_CI/00048.jpg"},
  {"claim": "stores.json row item_id 262 has purchase 270 / member 243 / sell 27 coins, but the identical row is shared by about 20 unrelated item ids (251, 254, 256, 260, 264, 268, 270, 271, 273, 275, 279, ...), has no vendor, NPC, zone or store name, so it is not evidence of a specific coin-vendor sale of this hat.", "source": "repo:prototype/osfr-tools/data/content/stores.json:158-170"}
 ],
 "confidence": 0.4,
 "open": [
  "Coin store price (270 coins, member 243, sell 27) for definition 262 is NOT attributed as a source: the row has no vendor/store and is shared by ~20 unrelated items. Confirm which store, if any, sells this hat before adding a coin_shop or vendor source.",
  "Collection name and its zone/area are unrecovered (collections.json area null; header above line 1755 not read). The Exploration (Collections) wiki page was cited from the repo provenance field only; it was not read in this pass.",
  "Wiki Adventurer-page claim from the earlier answer was dropped: the snippet checked did not support rare-exploration sourcing.",
  "Client definition has 12 definition ids and 62 definitions across two models (big-brim and cowboy hats); only ids 262 and 273 were checked against stores.json, and tint/race variants were not individually confirmed as drops.",
  "Retired status unknown; no wiki retirement or later-availability note found. Live is unsure: one head-slot list frame shows the name, which is not proof of current availability.",
  "Client description is empty."
 ]}
