<!-- fleet job=citem-infer id=cbrewery-veal-sandwich-1192-v1 status=nothing_found turns=4 usd=0.0045 tokens(read,write,in,out)=[36960, 22734, 10, 2486] model=claude-haiku-5-5 -->
# Brewery Veal Sandwich

{"item": {"name": "Brewery Veal Sandwich", "locale_id": 1192, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Brewery Veal Sandwich' is locale 1192, one of a set of Brewery food items (locale 1187-1197: Fizzpop, Pizza, Crunchberry, Cookies, Crackers, Veal Sandwich, Chicken Nuggets, Toasted Sandwich, Monty Crispy Sandwich, Farmer's Special), plus Chewy Candy Horn (1197).", "source": "locale:1192; locale:1187-1197"},
  {"claim": "Client definition 4033 has the description 'Eating this food will change the player into a female chugawug archer for thirty minutes' (locale 2741, untitled), matching the transform-food effect text also held as locale 150822 'Chugawug Female Archer' and locale 150082 'transform food'.", "source": "locale:2741; locale:150822; locale:150082"},
  {"claim": "The coin store data has no row for definition 4033. The only near match is item_id 14033 (purchase 358 coins, member price 322), a different item, so it is not a price for this sandwich.", "source": "repo:prototype/osfr-tools/data/content/stores.json:3714 (item 14033)"},
  {"claim": "No wiki page, article fact, video frame, vendor stock row, quest reward or drop names this sandwich. Searches of the wiki, articles and video returned no matches for 'Brewery Veal Sandwich' or 'transform food'.", "source": "lookup (wiki, articles, video) returned no matches"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found. The sandwich is probably a Wugachug/Sasparilla Brewery food or a Chugawug transform-food item, but nothing in the pack or repo names a vendor, quest, drop, event or crafting recipe for it. Do not assume a source without a citation.",
  "Live status is unconfirmed. The first-pass 'live: yes' tag is a hint only. The client has the text, but no store or wiki record shows it is sold now.",
  "The pack lists the client name as locale 1192 with no client_lines tagged beyond the name, and the description is locale 2741 (untagged). Both are consistent, but the description does not name the item.",
  "Next steps: check the Brewery food quests in Wugachug (NPCs Brockoom, Oggy, Wugawump), any Chugawug/transform-food event, and the crafting/cooking recipes for items 1187-1197 in repo recipe data, then search wiki pages for these sibling names."
 ]}
