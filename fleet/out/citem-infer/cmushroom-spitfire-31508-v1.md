<!-- fleet job=citem-infer id=cmushroom-spitfire-31508-v1 status=done turns=6 usd=0.0048 tokens(read,write,in,out)=[44174, 17591, 14, 4324] model=claude-haiku-5-5 -->
# Mushroom Spitfire

{"item": {"name": "Mushroom Spitfire", "locale_id": 31508, "kind": "furniture"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, vendor not identified (stores.json category 57, tint group 1). Purchase price 250 coins; member price 225 coins (10% member discount); sell-back 25 coins", "where": null, "price": "250 coins (member 225 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 14305 (line 3787)"},
  {"type": "prize_wheel", "detail": "Bigfoot's Lair prize wheel, Archer job (listed with Camp Chatty Banner, Camp Chatty Tent, Camp Robbie Flair Shard, Chugawug Totem, Tasty Marshmallow)", "where": "Bigfoot's Lair (dungeon, Southern Wilds)", "price": "Prize wheel spin listed as 990 Coins on the wiki page; the per-item cost is not stated", "currency": "coins", "source": "wiki: Bigfoot's Lair (Rewards > Prize wheel by job > Archer); video L27vxozHOls/00004; repo:notes/Build Guides/Content/Dungeons/Bigfoot's Lair.md line 79; repo:prototype/osfr-tools/data/content/dungeons/bigfoot_s_lair.json lines 792 and 2005"},
  {"type": "prize_wheel", "detail": "Bigfoot Defender prize wheel, Archer job (same Archer list as Bigfoot's Lair)", "where": "Bigfoot Defender (quest-triggered special-spawn battle, Southern Wilds, Camp Robbie side)", "price": "Prize wheel spin listed as 990 Coins on the wiki page; the per-item cost is not stated", "currency": "coins", "source": "wiki: Bigfoot Defender (Rewards > Prize wheel by job > Archer); repo:notes/Build Guides/Content/Dungeons/Bigfoot Defender.md line 65; repo:prototype/osfr-tools/data/content/dungeons/bigfoot_defender.json lines 656 and 1894"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name 'Mushroom Spitfire' is locale 31508, with description 'Mmm... slow roasted mushrooms.' Definition 14305, slot 0, class 0, model hsg_roastingspit_01.adr (housing-style model, so furniture)", "source": "locale:31508; client definition pack"},
  {"claim": "Item 14305 is in the coin store data at 250 coins purchase, 225 member price, 25 sell price, not no_sale, with source tags L1,L2,L4,R2,T633,R1", "source": "repo:prototype/osfr-tools/data/content/stores.json item 14305 (line 3787)"},
  {"claim": "Mushroom Spitfire is on the Archer prize wheel at Bigfoot's Lair and at Bigfoot Defender", "source": "wiki pages Bigfoot's Lair and Bigfoot Defender (Prize wheel by job > Archer); video L27vxozHOls/00004 for Bigfoot's Lair"},
  {"claim": "Client siblings Caterpillar Spitfire (31509) and Nutty Spitfire (31510) sit beside it in locale; the Brawler prize wheel lists Caterpillar Spitfire, so the Spitfire set shares prize wheels", "source": "locale:31509, locale:31510; wiki Bigfoot's Lair / Bigfoot Defender prize wheel lists"}
 ],
 "confidence": 0.6,
 "open": [
  "The coin vendor that sells item 14305 for 250 coins is not named in the repo data (stores.json gives only category 57). Find the vendor for category 57 before finalising the vendor entry.",
  "Per-spin prize wheel cost: the wiki's '990 Coins' line is the wheel spin price, not the price of this item. Per-item odds and cost are unknown.",
  "The pack's 'coin_store_prices' value (250) matches stores.json item 14305; the pack did not give the store item id, so this was checked against the repo file.",
  "The wiki cites the prize wheels for Bigfoot's Lair and Bigfoot Defender only through the Archer job list; no wiki source names a Brawler or other-job wheel for Mushroom Spitfire.",
  "Retirement status is not stated by any source. The item carries live-looking store tags but no date, so 'retired' is null.",
  "Kind is 'furniture' from the housing-style model name and the first-pass guess; the client does not state a category directly, so verify in-game."
 ]}
