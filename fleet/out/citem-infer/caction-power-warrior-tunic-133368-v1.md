<!-- fleet job=citem-infer id=caction-power-warrior-tunic-133368-v1 status=done turns=6 usd=0.0066 tokens(read,write,in,out)=[84491, 27306, 14, 4699] model=claude-haiku-5-5 -->
# Action Power Warrior Tunic

{"item": {"name": "Action Power Warrior Tunic", "locale_id": 133368, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store item 76360 (store category 103, tint group 1); the vendor that stocks category 103 is not named in the repo data, so the specific vendor is open", "where": null, "price": "1076 coins (member price 968 coins, 10% member discount; sell-back 107 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 76360 (line 8612)"},
  {"type": "prize_wheel", "detail": "Forest Troll Fort, Warrior Prize Wheel (listed as 'Action Power Warrior Tunic'). The wheel is a random reward from the dungeon, not a purchase; the wiki gives no per-spin cost for this item", "where": "Forest Troll Fort (Northern Wilds dungeon, difficulty 5)", "price": null, "currency": null, "source": "freerealms-wiki/wikitext/2603-49339 'Forest Troll Fort' (Prize Wheels, Warrior Prize Wheel, line 73)"},
  {"type": "drop", "detail": "Forest Troll Fort bonus reward: killing all Elite Sneak Scouts grants each player a clothing piece from the job set. The Warrior set is 'Action Power', and the tunic fits that set, but the wiki does not list the exact pieces, so this is probable and not confirmed for the tunic", "where": "Forest Troll Fort", "price": null, "currency": null, "source": "freerealms-wiki/wikitext/2603-49339 'Forest Troll Fort' (Bonus Rewards, line 96)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item 'Action Power Warrior Tunic' is locale 133368, item definition 76360, slot 3, class 15, with a coin store price of 1076", "source": "locale:133368; repo:prototype/osfr-tools/data/content/stores.json item 76360"},
  {"claim": "Store row for item 76360 is in category 103 with purchase 1076, member 968 and sell-back 107 coins, not marked no_sale", "source": "repo:prototype/osfr-tools/data/content/stores.json line 8612"},
  {"claim": "Forest Troll Fort Warrior Prize Wheel lists Action Power Warrior Tunic", "source": "freerealms-wiki/wikitext/2603-49339 'Forest Troll Fort' line 73"},
  {"claim": "Forest Troll Fort bonus clothing for Warrior is the 'Action Power' set", "source": "freerealms-wiki/wikitext/2603-49339 'Forest Troll Fort' line 96"},
  {"claim": "Wiki prize-wheel pages for other dungeons (Cracked Claw Caverns, Robgoblin Creek, Haunted Mines, Cray Caves and others) list Warrior tunics from the Battle Item Mystery Pack and the Warrior Prize Wheel with coin figures; they do not name this item", "source": "lookup wiki results for '[Action] [Power] [Warrior] [Tunic]' (Forest Troll Fort, Cray Caves, Claudia pages)"},
  {"claim": "Item appears in a Demo Derby: Tucker's Troubles player-trade screen at Adventurer level 20. This shows it being traded, not a source", "source": "video:eqV_FzElXSE/00384.jpg"},
  {"claim": "Name appears in the locale data and in the other community item definitions (Sanctuary, Lxzxrus, Legacy, TCG-Files)", "source": "refs ClientItemDefinitions.json 'Action Power Warrior Tunic' comment lines; locale en_us_data.dat"}
 ],
 "confidence": 0.6,
 "open": [
  "Which coin vendor sells store item 76360 (category 103). The repo gives the price but no NPC or shop name, and no wiki page names it. Check the category-103 vendor mapping in stores data.",
  "The Forest Troll Fort Warrior Prize Wheel and the bonus Elite Sneak Scouts reward both point to this item, but neither gives its drop odds or per-spin cost. The '214 Coins' line on each wheel may be a wheel cost or a coin reward, which the wiki does not say.",
  "Whether the Elite Sneak Scouts bonus gives this exact tunic or another Action Power piece is not confirmed.",
  "Retired status is unknown. The store row is not marked no_sale, which suggests it was still sold, but no date or retirement note is given.",
  "The wiki states no date for the Forest Troll Fort prize wheels or bonus rewards. Check whether they are still active in the rebuilt content.",
  "The client description is empty, so the tunic's stats and tints are unknown beyond the one tint group in the store data."
 ]}
