<!-- fleet job=citem-infer id=cemergency-medic-cap-133107-v2 status=done turns=3 usd=0.0031 tokens(read,write,in,out)=[17271, 12684, 8, 2676] model=claude-haiku-5-5 -->
# Emergency Medic Cap

{"item": {"name": "Emergency Medic Cap", "locale_id": 133107, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Spratt (pixie NPC merchant who sells exclusively Medic job items), listed in the Sells section as 'Emergency Medic Cap'", "where": "Snowhill", "price": null, "currency": null, "source": "wiki page 'Spratt' (https://freerealms.fandom.com/wiki/Spratt, Sells section, CC BY-SA); repo:prototype/osfr-tools/data/content/vendors.json:36019-36042 (stock_source kind wiki, page Spratt)"},
  {"type": "coin_shop", "detail": "Generic coin-store reference price for item 76099 (category 101). Not a price captured at the Spratt NPC; vendors.json marks it '(R) reference price, not captured NPC quote'. Treat as unconfirmed.", "where": "coin store data", "price": "528 coins (member price 475 coins, 10% member discount) – reference", "currency": "coins", "source": "repo:data/content/stores.json item 76099 (purchase_price_coins 528, member_price_coins 475); repo:prototype/osfr-tools/data/content/vendors.json:36023-36027"},
  {"type": "prize_wheel", "detail": "'[Medic] Prize Wheel' reward listing (with Battle Item Mystery Pack, Medic's Bonesaw of Triage, Medic's Power Shard of Vitality III, Medic's Ring of Energy III) on the dungeon pages for Return to Sender! and Mushroom Cavern. The item's own price on this wheel is not stated.", "where": "Return to Sender! (northeast Wilds battle) and Mushroom Cavern (Nettleseed, Briarwood)", "price": null, "currency": null, "source": "wiki page 'Return to Sender!'; wiki page 'Mushroom Cavern'"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name locale 133107 is 'Emergency Medic Cap'; one definition (76099), slot 1 (head), class 7", "source": "locale:133107"},
  {"claim": "Spratt sells exclusively Medic job items and her Sells list includes '[Emergency] [Medic] [Cap]' alongside the other Emergency Medic pieces", "source": "wiki page: Spratt"},
  {"claim": "Spratt is an NPC in Snowhill", "source": "wiki page: Spratt; wiki page: Howling Hills (Snowhill category)"},
  {"claim": "Coin store reference price 528 coins / 475 member for item 76099; vendors.json marks this as a reference price, not an NPC quote", "source": "repo:data/content/stores.json item 76099; repo:prototype/osfr-tools/data/content/vendors.json:36027"},
  {"claim": "Cap appears on the [Medic] Prize Wheel listing on the Return to Sender! and Mushroom Cavern wiki pages", "source": "wiki pages: Return to Sender!, Mushroom Cavern"},
  {"claim": "The 8 Coins and 80 Coins figures on those pages sit beside the dungeon reward block, not against the cap; they are not the cap's price", "source": "wiki pages: Return to Sender!, Mushroom Cavern"},
  {"claim": "Cap is listed in the Emergency Medic set alongside Backpack, Fatigues, Gloves, Boots, Shirt", "source": "wiki page: Spratt; locale:133102-133112"}
 ],
 "confidence": 0.6,
 "open": [
  "Spratt price not captured from the NPC. The 528 / 475 coin figures are a repo reference price from stores.json, not a confirmed Spratt quote.",
  "Prize wheel row: the 8 Coins / 80 Coins figures on the two dungeon pages are not explained in the captured text (they may be dungeon coin rewards rather than spin costs). The cap's price on the wheel is unknown.",
  "Dungeon reward rows (repo:data/content/dungeons/return_to_sender.json:1078, mushroom_cavern.json:1211) were not read and are not listed as sources.",
  "Retirement not verified. The Spratt entry dates from 27 Aug 2013 in repo data; the wiki Spratt revision was 2025-07-04, which still lists the cap, so it appears live on that date. Whether later removed is unknown.",
  "Medic level-10 skill 'Pro [Medic] [Cap]' is a skill, not this item; excluded."
 ]
}
