<!-- fleet job=citem-infer id=ccamp-chatty-hat-16979-v2 status=done turns=3 usd=0.0029 tokens(read,write,in,out)=[16814, 11288, 8, 2604] model=claude-haiku-5-5 -->
# Camp Chatty Hat

{"item": {"name": "Camp Chatty Hat", "locale_id": 16979, "kind": "clothing"},
 "sources": [
  {"type": "quest_reward", "detail": "Confronting Bigfoot (title locale 394863758 / 3309872787), given by Counselor Edmond; turn-in 'Return to Chatty' (Campmeister Chatty)", "where": "Camp Chatty, Greenwood Forest (Southern Wilds); quest runs into Bigfoot's Lair", "price": null, "currency": null, "source": "video:L27vxozHOls/00326 (\"Quest Completed! Confronting Bigfoot. You receive 1 Camp Chatty Hat\"); repo:notes/Build Guides/Content/NPCs/NPCs - Greenwood Forest.md line 154 ('Reward Camp Chatty Hat'); repo:prototype/osfr-tools/data/content/npcs/greenwood_forest.json line 5149 (turn-in 'Return to Chatty', video L27vxozHOls/00280); repo:prototype/osfr-tools/data/content/dungeons/bigfoot_s_lair.json line 514 (reward text)"},
  {"type": "vendor", "detail": "Coin store listing (item 9052, category 101), vendor/NPC not identified in our data", "where": "Coin store (vendor unidentified)", "price": "370 coins (member price 333 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 9052 (line 2692: purchase_price_coins 370, member_price_coins 333, sell_price_coins 37)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Camp Chatty Hat' (locale 16979), description 'Make Campmeister Chatty proud by sporting his camp's uniform.' (locale 16983 is the matching quest_objective text), one definition 9052, slot 1, class 72", "source": "locale:16979; locale:16983; client definition as given in pack"},
  {"claim": "Quest reward: 'You receive 1 Camp Chatty Hat' on Confronting Bigfoot completion, shown in gameplay frame", "source": "video:L27vxozHOls/00326; repo:notes/Build Guides/Content/Dungeons/Bigfoot's Lair.md Rewards table"},
  {"claim": "Confronting Bigfoot is given by Counselor Edmond in Camp Chatty and its reward is the Camp Chatty Hat", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Greenwood Forest.md line 154; repo:prototype/osfr-tools/data/content/npcs/greenwood_forest.json line 5149 and 5156 ('Camp wearables carry his name (Camp Chatty Hat, ...)')"},
  {"claim": "Coin store listing for item 9052 at 370 coins, member 333 coins (10% discount), category 101", "source": "repo:prototype/osfr-tools/data/content/stores.json line 2692"},
  {"claim": "Camp Chatty Hat appears in gameplay inventory frames of head items", "source": "video:4pioItLqlU8/00160.jpg, 00166.jpg"}
 ],
 "confidence": 0.6,
 "open": [
  "Client id 3789252990 cited for the Bigfoot's Lair reward does not resolve in the locale table (locale lookup: no such id). The name link rests on locale 16979 and video L27vxozHOls/00326, not on that id. The id in bigfoot_s_lair.json line 514 and the Lair note line 70 should be corrected or flagged.",
  "Coin store vendor is unidentified: stores.json row 9052 names no NPC or shop, and vendor_stock in the pack is empty. The coin store price is recorded as a coin-store listing, not a confirmed vendor NPC.",
  "The claim that item 9052 sits in the same store tier as other camp items was dropped: no stores.json check of items 16977, 16978, 16980-16982 was made.",
  "No wiki page for the item; retired status and whether the coin store listing is still stocked are unknown. Live status is 'unsure' for that reason.",
  "Whether the quest-reward copy and the coin-store copy are the same item is inferred from the single client definition 9052 and the shared name; not separately confirmed.",
  "Camp Robbie set (16978, 16980, 16982) sources are out of scope for this answer."
 ]}
