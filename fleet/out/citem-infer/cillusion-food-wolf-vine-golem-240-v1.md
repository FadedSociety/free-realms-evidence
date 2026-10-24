<!-- fleet job=citem-infer id=cillusion-food-wolf-vine-golem-240-v1 status=nothing_found turns=5 usd=0.0059 tokens(read,write,in,out)=[58683, 28377, 12, 3442] model=claude-haiku-5-5 -->
# Illusion Food - Wolf Vine Golem

{"item": {"name": "Illusion Food - Wolf Vine Golem", "locale_id": 240, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition: item id 2945, NameId 240, DescriptionId 3154 ('Eating this food will temporarily change the player into a Wolf Vine Golem.'), class 9, SingleUse, CategoryId 10, ActivatableAbilityId 1992, NonMiniGame, MemberDiscount 10, Cost 180 (a definition field, not a store row).", "source": "refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:54774-54793; locale:240; client locale 309323398 (description)"},
  {"claim": "The same item is also defined in the Sanctuary PS3 build's client definitions (same ActivatableAbilityId 1992), so it shipped in more than one build.", "source": "refs:Sanctuary-PS3-20261009/src/Resources/ClientItemDefinitions.json:61737-61745"},
  {"claim": "Our store data has no row for item 2945. Stores.json has purchase rows for neighbouring ids 29450-29459 at 270 coins, but none for 2945, so the Cost 180 is not a verified coin vendor price.", "source": "repo:prototype/osfr-tools/data/content/stores.json (search for item_id 2945 returned no match)"},
  {"claim": "Illusion food is a family of items: Floren, Yeti, Bear Vine Golem, Man-Eating Plant, Owl, Bat, Buck, Hawk, Dove, Eagle, Snow Hog, Snake and others share the 'Illusion Food - ' naming and the same definition pattern.", "source": "locale:235-245; refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json lines 54626-56005, 72879-73020"},
  {"claim": "A Briar Patch NPC asks the player to get meat from the Wolf Vine Golems in the Briar Patch for cooking. This ties the enemy to a food theme but does not name this item or any reward for it.", "source": "locale:693851549 and locale:3370537470 (client dialog); repo:notes/Build Guides/Content/Dungeons/Briar Patch.md:50"},
  {"claim": "The wiki's illusion-food pages found so far are for other items (e.g., Bark Chocolate: 'large floppy eared dog'). No wiki page or category was found for this item.", "source": "lookup wiki: image:item_tooltip Bark chocolate.jpg"}
 ],
 "confidence": 0.2,
 "open": [
  "No source found. No vendor, quest, drop, event, or prize-wheel link names Illusion Food - Wolf Vine Golem. The only candidate, a coin price, is not in our store data (stores.json has no item 2945).",
  "Client Cost 180 (Legacy definition) is a possible coin price but is unverified and not a store row. Do not record it as a vendor price without a store or wiki source.",
  "The Briar Patch cooking NPC (dialog locale:693851549 / 3370537470) needs meat from Wolf Vine Golems. Check whether that quest rewards illusion food or whether the Briar Patch enemies drop it. Not verified here.",
  "Live status unknown. The item is in the Legacy and Sanctuary PS3 builds, but no wiki or video evidence shows it live in 2009-2014 or retired.",
  "The client has no tint or race variants (one definition, no models), so the variant count is 1.",
  "The wiki has no article for this item. Search the wiki category for illusion foods and check the 'Illusion Food' family for a shared vendor or event."
 ]}
