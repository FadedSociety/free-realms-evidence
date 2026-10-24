<!-- fleet job=citem-infer id=cillusion-food-nanny-goat-1207-v1 status=done turns=11 usd=0.0098 tokens(read,write,in,out)=[223942, 37513, 24, 5683] model=claude-haiku-5-5 -->
# Illusion Food - Nanny Goat

{"item": {"name": "Illusion Food - Nanny Goat", "locale_id": 1207, "kind": "consumable"},
 "sources": [{"type": "other", "detail": "Farmer Chug, in the robgoblin crop-theft quest arc (hint 'robgoblins'); he hands out illusion food so the player can transform into a Nanny Goat and scare off robgoblins. Probably a quest-given item, not a sold or dropped one. Exact quest title and step not confirmed.", "where": "Farmer Chug's area (Farmers Market / farm area; exact zone not confirmed)", "price": null, "currency": null, "source": "locale:134991 (quest_dialog, hint 'robgoblins', speaker Farmer Chug per quest-lines/lines.json:27071-27075: 'I've got some illusion food here that'll transform you into a big scary monster'); locale:134992 (same text, flagged duplicate); locale:74488 'Scaring Robgoblins' (quest_title, candidate title only, unverified)"}],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item 4048 is 'Illusion Food - Nanny Goat', NameId 1207, DescriptionId 3116, Class 9, SingleUse true, NoSale true, NoTrade true, Cost 180, Icon 927, dyetint tint alias", "source": "refs:Sanctuary/src/Resources/ClientItemDefinitions.json:73881-73895 (Id 4048, Comment 'Illusion Food - Nanny Goat')"},
  {"claim": "Description: 'Eating this food will temporarily change the player into a Nanny Goat.'", "source": "client definition (DescriptionId 3116), as supplied in the pack"},
  {"claim": "Item 1207 sits in a set of Illusion Food consumables (1198 Antelope, 1199 Buck, 1200 Doe, 1208 Snow Hog, 1209 Wart Hog, 1213 Robgoblin Female Mage, etc.), all transformation foods", "source": "locale:1198-1228 (client text table)"},
  {"claim": "Farmer Chug's robgoblin arc gives illusion food to scare robgoblins: 'I've got some illusion food here that'll transform you into a big scary monster. Once you've transformed you can just scare away all the robgoblins.'", "source": "locale:134991, locale:134992; quest-lines/lines.json:27071"},
  {"claim": "Related item Chug's Illusion Potion (locale:42002) transforms the user into a frightening monster for the Robgoblin scare quest", "source": "locale:42002, locale:74708"},
  {"claim": "The store data has no coin price for item 4048 (stores.json has item_id 24048, a different item); the client definition has an empty coin_store_prices list", "source": "repo:prototype/osfr-tools/data/content/stores.json:6925 (not a match); client definition in pack"},
  {"claim": "No vendor, marketplace, coin shop or wiki page names this item; no wiki page or video frame found", "source": "lookup wiki/client/articles/video; search repo and refs"}
 ],
 "confidence": 0.4,
 "open": [
  "Quest title and exact giver/step not confirmed. Candidate 'Scaring Robgoblins' (locale:74488) is unverified; lines.json says the quest title for the 134985-134999 robgoblin arc is not in the pack.",
  "Whether the food is a quest reward, a quest-given item, or was also sold is unknown. No wiki, article or video source names it.",
  "Cost 180 in the definition is a server-side item value, not a coin store price. It is not a sale source, and the wiki's Bark Chocolate tooltip shows a 'Resell Value' (18), so it may be a resell value. Do not treat it as a purchase price.",
  "Live status is unsure: the text is unflagged and the item is in the client, but no source confirms it was obtainable on the live server or whether it was retired.",
  "No drop, event or prize-wheel source found."
 ]}
