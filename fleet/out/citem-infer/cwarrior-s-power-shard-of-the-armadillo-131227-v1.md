<!-- fleet job=citem-infer id=cwarrior-s-power-shard-of-the-armadillo-131227-v1 status=done turns=3 usd=0.0031 tokens(read,write,in,out)=[13477, 13282, 8, 2634] model=claude-haiku-5-5 -->
# Warrior's Power Shard of the Armadillo

{"item": {"name": "Warrior's Power Shard of the Armadillo", "locale_id": 131227, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Coin store row for store item_id 2435 (category 103, tint group 2): purchase 270 coins, member price 243 coins (10% member discount), sell-back 27 coins. The vendor/shop that stocks category 103 is not named in the data, so the specific vendor is open.", "where": null, "price": "270 coins (member price 243 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 5876 (item 2435)"},
  {"type": "prize_wheel", "detail": "Sibling variant Archer's Power Shard of the Armadillo is 'acquired from the prize wheel of the battle Wraiths of Wrath'. Applied to the Warrior variant by analogy only; no Warrior-specific source found.", "where": null, "price": null, "currency": null, "source": "wiki page: Archer's Power Shard of the Armadillo (ns0); File:Archer's Power Shard of the Armadillo.jpg (\"Obtained by completing Wraiths of Wrath! as an Archer.\")"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item name exists as locale 131227, one of six class variants (Archer 130967, Brawler 131032, Medic 131097, Ninja 131162, Warrior 131227, Wizard 131292) of the Power Shard of the Armadillo, each a level-1 class power shard with a Chance to boost armor when hit passive.", "source": "locale:131227; locale:130967; locale:131032; locale:131097; locale:131162; locale:131292; wiki image:item_tooltip Archer's Power Shard of the Armadillo.jpg"},
  {"claim": "Store data has a coin-store row for item 2435 at 270 coins, member price 243, sell 27, which matches the coin_store_prices field of the definition.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 5876"},
  {"claim": "Archer's variant is acquired from the prize wheel of the battle Wraiths of Wrath (wiki), and its tooltip shows Resell Value 243 and Required: Archer.", "source": "wiki page Archer's Power Shard of the Armadillo; wiki image:item_tooltip"},
  {"claim": "Warrior variant has a sibling cluster of Warrior's Power Shards (Precision, Smiting, Second Wind, Entangling, Vampire, Vitality I-V) at adjacent locale ids, so it belongs to the same shard family.", "source": "locale:131222-131232"}
 ],
 "confidence": 0.4,
 "open": [
  "The coin store price (270) is tied to store item_id 2435, but the definition id is 75483. The mapping between the store item id and definition 75483 was taken from the pack's coin_store_prices field and is not independently confirmed; the store row could be a different item.",
  "Store category 103 is not mapped to a named vendor in the repo, so the vendor location is unknown.",
  "The wiki's prize-wheel source (Wraiths of Wrath) is documented only for the Archer variant. The Warrior variant's source is inferred from the family, not from a wiki page or client text for this item.",
  "The sibling wiki tooltip lists Resell Value 243, which equals the member price, while the store row's sell-back is 27. The wiki resell figure may be a different measure; left unresolved.",
  "No wiki page exists for the Warrior variant; its retirement status is unknown. The Archer sibling page does not say it was retired.",
  "The Warrior variant's own item description is empty in the client definition, so the passive effect is assumed to match the Archer variant."
 ]}
