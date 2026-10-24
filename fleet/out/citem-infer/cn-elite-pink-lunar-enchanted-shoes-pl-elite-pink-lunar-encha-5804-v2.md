<!-- fleet job=citem-infer id=cn-elite-pink-lunar-enchanted-shoes-pl-elite-pink-lunar-encha-5804-v2 status=done turns=3 usd=0.0037 tokens(read,write,in,out)=[20667, 17544, 8, 2506] model=claude-haiku-5-5 -->
# {n}Elite Pink Lunar Enchanted Shoes{pl="Elite Pink Lunar Enchanted Shoes"}

{"item": {"name": "Elite Pink Lunar Enchanted Shoes", "locale_id": 5804, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale, category 105, vendor/NPC not named in data. Definitions 1649 and 1699 both carry this row. The 9453 price is a shared tier price, not item-specific.", "where": null, "price": "9453 coins (member price 8507 coins, 10% member discount; sell price 945 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 1649 (line 497) and item 1699 (line 508)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 5804 'Elite Pink Lunar Enchanted Shoes'; slot 5 (feet), class 8; two definitions 1649 and 1699; models caster_<race>_f_feet_maryjanewstalking.adr and caster_<race>_m_feet_squaretip.adr", "source": "locale:5804 and client definition pack"},
  {"claim": "Coin store rows for definitions 1649 and 1699 are category 105, tint_group_id null, purchase 9453, member 8507, sell 945", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 497 and 508"},
  {"claim": "The same 9453/8507/945 row is shared by dozens of unrelated items across categories 101, 104 and 105 (e.g. items 122, 150, 174, 359, 633, 634), so the price is a tier, not proof of this item's price", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 93-508"},
  {"claim": "Sibling client names exist: Lunar Enchanted Shoes (locale 5802), Elite Black Lunar Enchanted Shoes (locale 26199), Elite Pink Lunar Enchanted Cap (locale 5799). The 'Elite Pink' tint is inferred from the name only; stores.json gives no tint split for 1649 or 1699", "source": "locale:5802, locale:26199, locale:5799, repo:stores.json lines 497 and 508"},
  {"claim": "No wiki page, article, video frame, image or vendor stock list names this item (lookup over client, wiki, articles, video). Category 105 is not mapped to any vendor or location in the repo", "source": "lookup results; repo search for category 105 mapping returned none"},
  {"claim": "Removed from evidence: the Lunar Enchanted Wand / Blacksmith link from the previous answer. It concerns a different item and does not bear on the shoes", "source": "critique 'evidence' lens and 'world' lens"}
 ],
 "confidence": 0.3,
 "open": [
  "Single source only: the stores.json coin-store row. No vendor, NPC, location or stock list is named, so the item is not wireable as a vendor sale. Mapping category 105 to a seller or shop is needed.",
  "The 9453 coin price is a shared tier price across dozens of category 101/104/105 items, so it cannot be attributed to these shoes specifically.",
  "The 'Elite Pink' tint is name-based only; stores.json does not separate definition 1649 from 1699 or tie either to the pink colour.",
  "Retirement status unknown: no source says whether it left the store. live is 'unsure' because the only confirmation is the data row.",
  "Client description is empty. No quest reward, enemy drop, event, prize wheel, crafting, collection or membership source was found.",
  "Previous answer's vendor label was changed to coin_shop because no vendor is named. Neighbouring items (Elite Pink Lunar Enchanted Cap 5799, Charm Infused Shoes 5800) were not checked and are not used."
 ]}
