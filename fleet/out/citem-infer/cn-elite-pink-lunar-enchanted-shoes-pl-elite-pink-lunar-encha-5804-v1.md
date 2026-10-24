<!-- fleet job=citem-infer id=cn-elite-pink-lunar-enchanted-shoes-pl-elite-pink-lunar-encha-5804-v1 status=done turns=5 usd=0.0049 tokens(read,write,in,out)=[45222, 20514, 12, 3804] model=claude-haiku-5-5 -->
# {n}Elite Pink Lunar Enchanted Shoes{pl="Elite Pink Lunar Enchanted Shoes"}

{"item": {"name": "Elite Pink Lunar Enchanted Shoes", "locale_id": 5804, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Coin store sale, vendor/NPC not identified (stores.json lists it under category 105 for definition ids 1649 and 1699, both at the same price)", "where": "coin store (vendor not named in data)", "price": "9453 coins (member price 8507 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 1649 (line 497) and item 1699 (line 508); per the pack's coin_store_prices field, 9453"}],
 "retired": null, "live": "unsure",
 "evidence": [{"claim": "Client name is locale 5804, 'Elite Pink Lunar Enchanted Shoes', slot 5 (feet), class 8, two definitions (1649, 1699), models caster_<race>_f_feet_maryjanewstalking.adr and caster_<race>_m_feet_squaretip.adr", "source": "locale:5804 and client definition pack"},
 {"claim": "Coin store entries for definitions 1649 and 1699 both list purchase_price_coins 9453, member_price_coins 8507, sell_price_coins 945", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 497 and 508"},
 {"claim": "Same-set items Lunar Enchanted Shoes (locale 5802), Lunar Enchanted Cap (5797/5799 cluster), Lunar Enchanted Slacks (5822), Lunar Enchanted Skirt (5817) and Lunar Enchanted Short Cloak (5812) exist in the client text, so this is a Lunar Enchanted gear set with an Elite Pink tint", "source": "locale:5802, locale:5822, locale:5797, locale:5817, locale:5812"},
 {"claim": "The Lunar Enchanted Wand is a Wizard level 4-5 weapon obtainable from the Blacksmith recipe; the set's own vendor is not confirmed", "source": "wiki page 'Lunar Enchanted Wand'; wiki page 'Blacksmith'"},
 {"claim": "No wiki page, article, video frame or vendor stock list names Elite Pink Lunar Enchanted Shoes", "source": "lookup over client, wiki, articles, video returned no matches for the item name"}],
 "confidence": 0.35,
 "open": ["The coin vendor that sells item 1649/1699 is not named in the repo data; stores.json only gives a category id (105). Need the Coin Shop/vendor mapping for category 105 to name the seller and location.",
 "Pack says the coin store price is evidence of a coin vendor sale; I cite it, but the vendor identity and whether this is the Coin Shop or a vendor stall are unresolved.",
 "No wiki page or article confirms the Elite Pink Lunar Enchanted Shoes; the 'Elite Pink' tint may be a separate definition (1699) from the base (1649), and which definition each price applies to is not split in the data.",
 "Retirement status unknown: no source states whether the item left the store. The 9453 price appears on many category 105 items, so it is a tier price, not item-specific evidence.",
 "Whether the set's Blacksmith link (Wand recipe) applies to the shoes is unverified.",
 "Client description is empty; no quest, drop, event, prize wheel, or crafting source was found.",
 "Pack's client_cluster lists the Elite Pink Lunar Enchanted Cap (5799) and the Charm Infused Shoes (5800) as neighbours; their sources were not checked and are not used here."]}
