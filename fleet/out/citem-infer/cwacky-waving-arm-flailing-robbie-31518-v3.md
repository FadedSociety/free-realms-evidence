<!-- fleet job=citem-infer id=cwacky-waving-arm-flailing-robbie-31518-v3 status=done turns=4 usd=0.0041 tokens(read,write,in,out)=[35565, 18572, 10, 2850] model=claude-haiku-5-5 -->
# Wacky Waving Arm Flailing Robbie

{"item": {"name": "Wacky Waving Arm Flailing Robbie", "locale_id": 31518, "kind": "furniture"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale, definition 16890 (tint group 1, category 57). Vendor/NPC not named in store data; category 57 is not mapped to a shop.", "where": "coin store (vendor unknown)", "price": "1000 coins (member price 900 coins; the 900 is the member discount, not a second sale price; sell-back 100 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 16890 (line 4253; no_sale false)"},
  {"type": "quest_reward", "detail": "Rob Robbie Daily, 7th Day Chest Items list (the buried chest that opens after 7 consecutive days of the daily). The list names '1 Wacky Waving Arm Flailing Robbie'. The per-chest chance is not stated. It is not a Robgoblin junkpile reward and is not tied to Day 1-6 junkpile tiers.", "where": "Camp Robbie (Robbie's Tent)", "price": null, "currency": null, "source": "wiki Quest:Rob Robbie Daily (page ns112, revision 23902, 2013-06-02; freerealms-wiki/quest-pages.json); quest-lines/packs.json line 92273 ('7th Day Chest Items')"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name text for locale 31518 is 'Wacky Waving Arm Flailing Robbie', description 'Inflatable tube mania!', model hsg_wavy_robby_01.adr; definitions 14315 and 16890", "source": "locale:31518"},
  {"claim": "Definition 16890 is a sold coin-store row: purchase 1000 coins, member 900, sell-back 100, no_sale false", "source": "repo:prototype/osfr-tools/data/content/stores.json item 16890 (line 4253)"},
  {"claim": "Definition 14315 is no_sale true (50 coins listed, no sell price). It is not a purchasable sale and is dropped as a source; it is a non-sale variant, not a second shop listing", "source": "repo:prototype/osfr-tools/data/content/stores.json item 14315 (line 3797)"},
  {"claim": "The Rob Robbie Daily reward list names this item in the 7th Day Chest Items list (with the Chatty companion item on the same wiki page)", "source": "wiki Quest:Rob Robbie Daily (page ns112, revision 23902); quest-lines/packs.json line 92273"},
  {"claim": "Rob Robbie Daily is a repeatable once-per-day errand at Robbie's Tent, Camp Robbie", "source": "wiki Quest:Rob Robbie Daily (freerealms-wiki/quest-pages.json)"},
  {"claim": "The earlier claim that the item is in the junkpile Day 1-6 pools is unsupported: the junkpile reward text names no item; Day 7 text is generic ('random Station Cash Item, housing items')", "source": "wiki Quest:Rob Robbie Daily, Reward section"}
 ],
 "confidence": 0.6,
 "open": [
  "Vendor/NPC for the 1000-coin store row (16890) is not named in the store data; category 57 is not mapped to a shop, so no place can be given.",
  "Per-chest chance for the 7th Day Chest Items list is not stated on the wiki.",
  "The 7th Day chest is reached only after 7 consecutive days of the errand; the streak rules are not fully stated.",
  "Definition 14315 is no_sale and was dropped as a sale source; its purpose is unknown.",
  "Retirement and current availability are not established. The 16890 row is sold in store data, but no wiki page or article says it was retired or still sold.",
  "Companion items Wacky Waving Arm Flailing Chatty (31517) and Camp Robbie Banner (31520) were not checked for their own sources."
 ]}
