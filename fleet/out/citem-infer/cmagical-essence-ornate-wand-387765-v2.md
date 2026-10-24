<!-- fleet job=citem-infer id=cmagical-essence-ornate-wand-387765-v2 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[5928, 7165, 6, 1860] model=claude-haiku-5-5 -->
# Magical Essence Ornate Wand

{"item": {"name": "Magical Essence Ornate Wand", "locale_id": 387765, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store row for item 55821 (category 207, the same row shape as sibling items 55818-55820, all priced identically); vendor NPC not mapped from the store row", "where": null, "price": "2363 coins (member price 2126 coins, 10% member discount); sell-back 236 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:13983 (item_id 55821, purchase_price_coins 2363, member_price_coins 2126, sell_price_coins 236, no_sale false); matches client coin_store_prices 2363"},
  {"type": "collection", "detail": "Wizard Magical Wand Essences collection (name locale 67599); reward on completion: 1x item 55821", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:17586, 17630-17637; repo:prototype/osfr-tools/data/content/collections.json:4888; wiki page 'Magical Essence Ornate Wand' ('acquired by completing the collection Wizard Magical Wand Essences'); wiki page 'Wizard Magical Wand Essences'; locale:67599"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item 55821 has a coin store row: purchase 2363 coins, member price 2126 coins (10% discount), sell-back 236 coins, not marked no_sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json:13983"},
  {"claim": "The client's coin_store_prices value 2363 matches the store row price for 55821.", "source": "client definition (definition_ids 55821, coin_store_prices [2363]); repo:prototype/osfr-tools/data/content/stores.json:13983"},
  {"claim": "Item 55821 is the reward of the Wizard Magical Wand Essences collection (reward count 1).", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:17630-17637"},
  {"claim": "Wiki: Level 20 Wizard weapon, acquired by completing the collection Wizard Magical Wand Essences, Cannot Trade; Zap 2609 damage, Lightning Blast 10674 damage (wiki figures, unchecked against client).", "source": "wiki page: Magical Essence Ornate Wand"},
  {"claim": "Sibling Magical Essence weapons (Shadowblade, Shockrod, Warlords Axe, Crystal Hammer) sit beside it in the client locale table.", "source": "locale:387760-387765"}
 ],
 "confidence": 0.6,
 "open": [
  "Vendor NPC and zone for the stores.json coin row (category 207, item 55821) are not mapped; the NPC name is left unknown.",
  "The pack's image tooltip (Batty Wand / Balloon Wand, Membership, Level 16, Cakenstein Attacks!) is a different item and was discarded; no evidence links it to this wand.",
  "No retirement or end-of-sale note found for either the coin row or the collection; current availability is unverified, so live is 'unsure'.",
  "Membership requirement is not confirmed for this item.",
  "The collection's required essence items and their drop/vendor sources were not traced; cost to finish the collection is unknown.",
  "Wiki damage figures (2609 / 10674) were not checked against the client."
 ]}
