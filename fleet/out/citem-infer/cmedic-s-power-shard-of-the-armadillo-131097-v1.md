<!-- fleet job=citem-infer id=cmedic-s-power-shard-of-the-armadillo-131097-v1 status=done turns=4 usd=0.0029 tokens(read,write,in,out)=[17962, 10161, 10, 2993] model=claude-haiku-5-5 -->
# Medic's Power Shard of the Armadillo

{"item": {"name": "Medic's Power Shard of the Armadillo", "locale_id": 131097, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale, listed at 2435 coins (member price 2191 coins, 10% member discount; resell 243 coins). Store row keyed to item_id 75353, store category 121. Category name is not labelled in the store data, so this is a store listing rather than a confirmed 'Coin Shop' wiki category.", "where": "Coin store (category 121)", "price": "2435 coins (member 2191 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75353 (line 15270)"},
  {"type": "prize_wheel", "detail": "Unverified for this variant. Sister Medic shards have wiki text saying they come from prize wheels: Smiting from the Trail of Betrayal battle, Entangling from the Mudshell battle. The Archer's Armadillo shard wiki says it comes from the prize wheel of the battle Wraiths of Wrath!. No wiki page names the Medic Armadillo's wheel.", "where": "Prize wheel (battle not confirmed for Medic)", "price": null, "currency": null, "source": "wiki: Medic's Power Shard of Smiting; wiki: Medic's Power Shard of Entangling; wiki: Archer's Power Shard of the Armadillo (sister pattern only)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name for this item is locale 131097, \"Medic's Power Shard of the Armadillo\", one of 11 Medic/Power Shard sibling names.", "source": "locale:131097"},
  {"claim": "Client definition 75353 maps to coin store row item 75353 at 2435 coins purchase, 2191 member, 243 sell.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75353"},
  {"claim": "Archer's Power Shard of the Armadillo is a level 1 power shard (Power 5, boosts armor when hit) acquired from the prize wheel of the battle Wraiths of Wrath!. Resell value 243 matches the coin store sell price.", "source": "wiki page: Archer's Power Shard of the Armadillo; wiki image item_tooltip Archer's Power Shard of the Armadillo.jpg"},
  {"claim": "Sister Medic shards Smiting and Entangling are listed as prize wheel rewards, both with resell 243.", "source": "wiki pages: Medic's Power Shard of Smiting; Medic's Power Shard of Entangling"},
  {"claim": "Medic's Shockrod of Vitals and Warrior's Warlord Axe are listed as Coin Shop items that also come from Wraiths of Wrath! prize wheels, so the Wraiths wheel carries coin-shop-level items.", "source": "wiki pages: Medic's Shockrod of Vitals; Warrior's Warlord Axe of Cleaving"}
 ],
 "confidence": 0.5,
 "open": [
  "No wiki page or video names the Medic's Armadillo shard directly. The prize-wheel battle is inferred from the Archer's version (Wraiths of Wrath!) and sister Medic shards. Verify before treating it as a source.",
  "The 2435-coin price is from the store data row only. No wiki page, article, or video confirms a Coin Shop sale for this item. Store category 121's name is not in the data.",
  "Whether the item is live: it has a live store row (tags L1, L2, L4, R2, T633, R1), which suggests it was sold, but no dated source confirms it was still on sale at the end of the game.",
  "Pack gave no description (empty) and no vendor stock, quest, or drop answers; no membership, crafting, collection, or promotion source was found.",
  "The client definition's coin_store_prices field lists 2435 (a price), not an item id. The store row is item 75353."
 ]}
