<!-- fleet job=citem-infer id=cjack-o-lantern-outfit-119203-v1 status=done turns=3 usd=0.0023 tokens(read,write,in,out)=[8242, 7360, 8, 2636] model=claude-haiku-5-5 -->
# Jack-O-Lantern Outfit

{"item": {"name": "Jack-O-Lantern Outfit", "locale_id": 119203, "kind": "clothing"},
 "sources": [
  {"type": "quest_reward", "detail": "Special TCG Halloween quest, unlocked by purchasing a TCG Quest Pack (the quest can instead reward the Chiller Boombox; the quest reward is one of two, the glow-in-the-dark Jack O' Lantern costume or the Chiller Boombox)", "where": "Super Spooktacular (Halloween event)", "price": null, "currency": null, "source": "http://www.freerealms.com/article/detail.action?articleId=476; http://www.freerealms.com:80/article/detail.action?articleId=1854; wiki page Jack-O-Lantern Outfit"},
  {"type": "coin_shop", "detail": "Coin store sale listed in the client store data (item 69832, category 201); not confirmed as a live sale, see open", "where": "Coin store (category 201 unverified)", "price": "50 coins (member price 45 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 69832 (line 14918, purchase_price_coins 50, member_price_coins 45, no_sale true)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "The outfit is the reward of a special TCG Halloween quest unlocked by buying a TCG Quest Pack; the quest gives either the glow-in-the-dark Jack O' Lantern costume or the Chiller Boombox", "source": "http://www.freerealms.com/article/detail.action?articleId=476; http://www.freerealms.com:80/article/detail.action?articleId=1854"},
  {"claim": "The wiki page says the outfit is earned from purchasing the TCG Quest Pack in Spooktacular and completing the quest, and the Chiller Boombox is earned the same way", "source": "wiki page Jack-O-Lantern Outfit; wiki page Chiller Boombox"},
  {"claim": "Client name 'Jack-O-Lantern Outfit' is locale 119203, with one definition (id 69832), chest slot 17, model freestyle_<race>_<gender>_chest_pumpkin.adr", "source": "locale:119203; client definition"},
  {"claim": "Store data lists item 69832 at 50 coins, member price 45 coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 69832"},
  {"claim": "Halloween outfit items (Jack-O-Lantern Mask) were released in one Halloween update, placing the outfit in the same seasonal set", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2306"}
 ],
 "confidence": 0.6,
 "open": [
  "Not verified: the 50-coin store entry (stores.json category 201) has not been matched to a named coin vendor or Coin Shop page; the category was not resolved, so treat the coin price as a store-data record, not a confirmed sale.",
  "The 'no_sale': true flag in stores.json may mean the item can't be resold, or that it is no longer sold; this could not be confirmed, so the live status is unsure.",
  "The TCG Quest Pack's own price and whether it was a Station Cash marketplace item was not found in the evidence; the wiki and articles only say it was 'purchased'. Add a marketplace source if a price is confirmed.",
  "Retirement date not found. Super Spooktacular is seasonal, so the outfit is likely out of rotation, but no source states it was retired.",
  "The pack's article 1860 cites a 'Frost boombox' and a 'glow-in-the-dark Flashlight' from a Spanish-language version of the same quest; not used as the outfit's evidence.",
  "The pack's client cluster and vendor stock are empty; no separate coin vendor was found for this item beyond the store entry."
 ]}
