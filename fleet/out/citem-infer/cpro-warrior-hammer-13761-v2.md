<!-- fleet job=citem-infer id=cpro-warrior-hammer-13761-v2 status=done turns=2 usd=0.0028 tokens(read,write,in,out)=[5886, 12581, 6, 2365] model=claude-haiku-5-5 -->
# Pro Warrior Hammer

{"item": {"name": "Pro Warrior Hammer", "locale_id": 13761, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Unidentified coin vendor: listed in the coin store data (category 207, tint group 1) at 715 coins, 643 with member discount. No vendor name or location is in our data.", "where": null, "price": "715 coins (member price 643 coins, 10% discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 7074 (line 1927)"},
  {"type": "quest_reward", "detail": "Warrior: Knocking Some Sense In (Aster, road south of Merry Vale). Wiki says the hammer was previously acquired by completing this quest. Not confirmed in code: the repo's quest-lines record says no reward source was found.", "where": "Merry Vale road (Aster); Band 3, level 10 to 15", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Pro_Warrior_Hammer ; locale:71265 (quest title)"}
 ],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Wiki: Pro Warrior Hammer is a level 8 Warrior weapon, no longer able to be acquired, previously acquired by completing Warrior: Knocking Some Sense In. Cannot Trade.", "source": "https://freerealms.fandom.com/wiki/Pro_Warrior_Hammer"},
  {"claim": "Wiki categories include Retired Weapons and Unobtainable Weapons. Effects: Sweeping Slash 853 damage, Spinning Attack 1548 damage.", "source": "https://freerealms.fandom.com/wiki/Pro_Warrior_Hammer"},
  {"claim": "The Warrior wiki page lists Pro Warrior Hammer under Level 10 weapons, which conflicts with the item page's level 8 (verified: the Warrior page has 'Level 10 / Pro Warrior Hammer').", "source": "https://freerealms.fandom.com/wiki/Warrior"},
  {"claim": "Client name is 'Pro Warrior Hammer' (locale 13761); the weapon family cluster is 13757 Smasher, 13762 Elite Pink Smasher, 13763 Elite Black Smasher.", "source": "locale:13761"},
  {"claim": "Client definition 7074 has coin store price 715 coins (643 member price), category 207, not no_sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 7074 (line 1927)"},
  {"claim": "The quest title 'Warrior: Knocking Some Sense In' is in the client as locale 71265. Its title id cell in the repo is ucdt 2111744232 / ugdt 3588410217 (warrior.json:702). The earlier citation locale:2111744232 was wrong and is withdrawn.", "source": "locale:71265; prototype/osfr-tools/data/content/quests/warrior.json:702"},
  {"claim": "Repo notes record the item level as 8 on the item page and 10 on the Warrior job page, and the quest-reward link is listed as unresolved.", "source": "notes/Build Guides/Content/Jobs/Warrior.md:226; prototype/osfr-tools/data/content/quests/warrior.json:702-710"}
 ],
 "confidence": 0.6,
 "open": [
  "Vendor unknown: the stores.json row (category 207) names no vendor, zone or sale dates. It shows a price, not a confirmed sale. The wiki names no coin vendor, and no 'Coin Shop' category is cited for this item.",
  "Quest reward is wiki-only. The repo's quest-lines record says no reward source was found, so the reward link is unconfirmed in code.",
  "Level conflict is real but unresolved: item page says level 8, Warrior page says level 10 (both wiki). The repo's piece_033 record also has MinProfileRank 8.",
  "No retirement date. The wiki says only that the hammer is no longer acquirable, so the end of sale is unknown.",
  "The 715-coin price comes from our store data only; the wiki gives no price for this weapon.",
  "No drop, event, prize wheel, crafting, collection or membership source is evidenced."
 ]}
