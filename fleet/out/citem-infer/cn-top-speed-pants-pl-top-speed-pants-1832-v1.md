<!-- fleet job=citem-infer id=cn-top-speed-pants-pl-top-speed-pants-1832-v1 status=done turns=5 usd=0.0057 tokens(read,write,in,out)=[54644, 26115, 12, 3799] model=claude-haiku-5-5 -->
# {n}Top Speed Pants{pl="Top Speed Pants"}

{"item": {"name": "Top Speed Pants", "locale_id": 1832, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, Top Speed Pants variant (store item 14999, tint group 2); vendor NPC not identified in the repo", "where": "coin store catalogue (repo stores.json, category 104)", "price": "715 coins (member price 643 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:3877 (item_id 14999, purchase_price_coins 715)"},
  {"type": "vendor", "detail": "Coin store sale, Top Speed Pants variants (store items 14998 and 15001, tint groups 1 and 3); vendor NPC not identified in the repo", "where": "coin store catalogue (repo stores.json, category 104)", "price": "1266 coins (member price 1139 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:3876 (item_id 14998) and :3878 (item_id 15001)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Locale 1832 is the name 'Top Speed Pants', shared by 12 client definitions (ids 2050, 2056, 14983, 14985, 14986, 14989, 14991, 14994, 14997, 14998, 14999, 15001), slot 4, class 24, model freestyle_<race>_<gender>_legs_bootcutpants.adr.", "source": "locale:1832; client definition in pack"},
  {"claim": "Three of those 12 definitions (14998, 14999, 15001) are in the coin store catalogue at 715 or 1266 coins with 10% member discount. The pack's two prices match these entries. The other nine definitions have no store entry.", "source": "repo:prototype/osfr-tools/data/content/stores.json:3876-3878"},
  {"claim": "The client name table has the set siblings Elite Pink Top Speed Pants (1830) and Elite Black Top Speed Pants (1834). Shoes, gloves, helmet and jacket share the Top Speed name but no source for any of them was found in this pack.", "source": "locale:1830, locale:1834; FreeRealmsLocaleTools en_us_data.dat"},
  {"claim": "The text cluster near locale 1832 (Rise of the Skullz, 1835-1837) is a comic book consumable rewarded by the Aiding our Allies quest. It is a different item and does not belong to Top Speed Pants.", "source": "wiki page 'Rise of the Skullz'; notes/Build Guides/Content/NPCs/NPCs - Shrouded Glade.md (Aiding our Allies row)"},
  {"claim": "No wiki page, image, article, video frame, quest reward, drop or event names Top Speed Pants.", "source": "lookup over client, wiki, articles, video; search of refs for 'Top Speed Pants'"}
 ],
 "confidence": 0.4,
 "open": [
  "The store entries do not name a vendor. Which NPC sells these variants, and where, is not in the repo or the wiki.",
  "The mapping from store item to definition is by id only. The pack did not say which tint is Top Speed, Elite Pink or Elite Black, so the 715 versus 1266 split per variant is not tied to a named colour.",
  "No wiki page exists, so the item's sale window and retirement are unknown. The member price is shown as 643 and 1139 coins; I did not find a separate sale price.",
  "The pack's first-pass 'live: yes' is only a hint. The store entries suggest it was sold, but I found no dated proof that it is live now.",
  "The 'Rise of the Skullz' cluster in the pack is unrelated to this item; I did not use it as a source."
 ]}
