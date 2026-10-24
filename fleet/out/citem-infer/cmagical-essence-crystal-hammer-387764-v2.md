<!-- fleet job=citem-infer id=cmagical-essence-crystal-hammer-387764-v2 status=done turns=2 usd=0.0027 tokens(read,write,in,out)=[6356, 12762, 6, 2013] model=claude-haiku-5-5 -->
# Magical Essence Crystal Hammer

{"item": {"name": "Magical Essence Crystal Hammer", "locale_id": 387764, "kind": "weapon"},
 "sources": [
  {"type": "collection", "detail": "Brawler Magical Hammer Essences collection (collection id 227, name locale 67593). Completing it grants item 55820 x1. Entries are the four hammer essences: Essence of Fire, Wind, Water, Earth (item definitions 23819-23822).", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:17328-17387 (id 227, reward items item_definition_id 55820 count 1); wiki page 'Magical Essence Crystal Hammer' ('acquired by completing the collection Brawler Magical Hammer Essences'); wiki page 'Brawler Magical Hammer Essences' (Rewards: 20); locale:67593"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Item is a level 20 Brawler weapon, Cannot Trade, acquired by completing the Brawler Magical Hammer Essences collection", "source": "wiki page: Magical Essence Crystal Hammer"},
  {"claim": "Collection 227 'Brawler Magical Hammer Essences' rewards item definition 55820 (this item) x1 and lists four essence entries", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:17328-17387"},
  {"claim": "Collection exists in client and wiki with reward at level 20", "source": "locale:67593; locale:132484; wiki page: Brawler Magical Hammer Essences"},
  {"claim": "stores.json has a coin row for item 55820 (category 207, purchase 2363 coins, member 2126, sell 236). It is one of a block of identical 2363-coin rows (55815-55821) with no named vendor, so it is not counted as a vendor source.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 13977-13983"},
  {"claim": "Cluster siblings 387759 (Bow), 387760 (Shadowblade), 387761 (Shockrod), 387763 (Warlords Axe), 387765 (Ornate Wand) are essence-named weapons of the same set. 387762 Slag Hammer is not an essence weapon and is excluded.", "source": "locale:387759-387765"}
 ],
 "confidence": 0.75,
 "open": [
  "Coin store row for item 55820 (stores.json line 13982, category 207, 2363 coins / 2126 member, sell 236) is unverified: no vendor NPC is named, the wiki gives only the collection as acquisition, and the row shares its price with 55815-55821. Excluded as a vendor source until a named vendor or a wiki price confirms it. Client coin_store_prices value 2363 comes from the same row.",
  "The row's sell price (236 coins) conflicts with the wiki's Cannot Trade note; sellability is unresolved.",
  "Essence item acquisition (the four essences, Fire/Wind/Water/Earth, and where they drop or are bought) was not checked. Collection turn-in mechanics were not verified beyond the reward list.",
  "No wiki price, retirement date, or availability date was found for the item.",
  "Image text in the pack (trader list naming Rowdy Rumbler Hammer, Candy Cane Hammer) is a forum/chat fragment and is not evidence for this item."
 ]}
