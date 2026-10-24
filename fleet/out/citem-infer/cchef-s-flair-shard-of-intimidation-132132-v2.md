<!-- fleet job=citem-infer id=cchef-s-flair-shard-of-intimidation-132132-v2 status=done turns=4 usd=0.0026 tokens(read,write,in,out)=[19824, 9029, 10, 2512] model=claude-haiku-5-5 -->
# Chef's Flair Shard of Intimidation

{"item": {"name": "Chef's Flair Shard of Intimidation", "locale_id": 132132, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale, coin category 124 (a generic coin-store category shared with many non-flair items; not confirmed as a flair-shard section)", "where": "Coin Shop", "price": "1500 coins (member price 1350 coins with 10% member discount; sell price 150 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:15484 (item_id 75686); client coin_store_prices = 1500"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name is Chef's Flair Shard of Intimidation, locale 132132, one definition (75686), slot 13, class 21, no description text", "source": "locale:132132"},
  {"claim": "Store data sells item 75686 for 1500 coins, 10% member discount to 1350, sell price 150, source tags L1, L2, L4, R2, T633, R1 (tags not decoded)", "source": "repo:prototype/osfr-tools/data/content/stores.json:15484"},
  {"claim": "Wiki Category:Coin Flair says it is 'a list of flair shards currently sold in the Coin Shop' and sibling shards (Warrior's Valentines, Ninja's Discipline, Medic's Miracles, Warrior's Focus) carry Category:Coin Shop and Category:Marketplace Items; the Chef shard itself is not named on that category page", "source": "wiki: Category:Coin Flair"},
  {"claim": "Sibling 'of Intimidation' shards exist for Archer, Brawler, Medic, Ninja, Warrior, Wizard, Blacksmith, so this is one job variant of a set", "source": "locale:130985, locale:131050, locale:131115, locale:131180, locale:131245, locale:131310, locale:132096"},
  {"claim": "Chef NPC wiki sell lists (Nadia, Skye, Mikael, Ingrid, Zamzani, Rachael) show other Chef's Flair Shards (Valentines, Smoldering, Charbroiled, Gourmet Pizazz, Glamour, Cleanliness, Music for your Mouth) but do not list the Intimidation shard, so they do not confirm an NPC source for it", "source": "wiki: Nadia; wiki: Skye; wiki: Mikael; wiki: Ingrid; wiki: Zamzani; wiki: Rachael"},
  {"claim": "Previous answer's claim that the Coin Shop wiki page has a 'Flair Shards' section was not confirmed; the Coin Shop page hit was a news template only", "source": "wiki: Template:News; wiki: Coin Shop (search)"}
 ],
 "confidence": 0.5,
 "open": [
  "The coin-shop channel rests on repo store data alone (stores.json line 15484). No wiki page names the Chef's Intimidation shard or gives its price, so no wiki price exists to compare against.",
  "Coin category 124 is not confirmed to be a Flair Shards section; it also holds unrelated items at very different prices.",
  "Wiki Category:Coin Flair lists shards sold in the Coin Shop but does not name this Chef shard. Support for the Coin Shop channel is the store row plus the category, not a page for this item.",
  "Live status and retirement unknown. No source confirms whether it is still sold or was retired. Store source tags (L1, L2, L4, R2, T633, R1) are not decoded.",
  "No quest, drop, event or other NPC source found. The Chef NPC sell lists on the wiki do not include the Intimidation shard."
 ]}
