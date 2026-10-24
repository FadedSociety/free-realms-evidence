<!-- fleet job=citem-infer id=cbriarheart-bandage-square-shard-413443-v3 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[7102, 10681, 6, 2168] model=claude-haiku-5-5 -->
# Briarheart Bandage Square Shard

{"item": {"name": "Briarheart Bandage Square Shard", "locale_id": 413443, "kind": "other"},
 "sources": [
  {"type": "other", "detail": "Redeemed from the Trading Card Game Series 2 Virtual Reward loot card of the same name (card ID 2L6)", "where": null, "price": null, "currency": null, "source": "wiki page: Briarheart Bandage Square Shard; wiki page:ns6 File:Briarheart bandage square shard tcg.png (virtual reward, series 2, unredeemed)"},
  {"type": "coin_shop", "detail": "Coin store row for item 3998 (category 121). No vendor or NPC is named in the store data, vendor_stock is empty, and no wiki or video source places it in a shop. Unverified as a live sale: the wiki and tooltip say Cannot Sell, which conflicts with no_sale false in the row.", "where": null, "price": "500 coins purchase; 450 coins member price (10% off); 50 coins sell price", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 803 (item_id 3998); client definition coin_store_prices 500"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name and description: 'Briarheart Bandage Square Shard'; 'A powerful shard that increases a Medic's health.'", "source": "locale:413443; locale:413445"},
  {"claim": "Level 1 Medic power shard, effects identical to Medic's Power Shard of Vitality V; acquired by redeeming TCG Series 2 Virtual Reward card 2L6; Cannot Sell, Cannot Trade; +712 health in combat", "source": "wiki page: Briarheart Bandage Square Shard"},
  {"claim": "Item tooltip: Resell Value 50, Power 5, Required Medic, Stats +712, Cannot Sell, Cannot Trade", "source": "wiki image:item_tooltip Briarheart bandage square shard.jpg"},
  {"claim": "Item render text reads 'Health by 220', which conflicts with the tooltip and wiki value of +712", "source": "wiki image:item_render Briarheart bandage square shard tcg.png"},
  {"claim": "Card File page: virtual reward from TCG series 2, unredeemed", "source": "wiki page:ns6 File:Briarheart bandage square shard tcg.png"},
  {"claim": "Store row confirmed on re-read: item 3998, category 121, purchase 500, member 450, sell 50, no_sale false, source tags L1,L2,L4,R2,T633,R1", "source": "repo:prototype/osfr-tools/data/content/stores.json line 803"},
  {"claim": "Item appears on the in-game Virtual Rewards cards collection page; supports the card tie-in only, not a coin price", "source": "video:eS3bRs9fR5k/00038.jpg"}
 ],
 "confidence": 0.5,
 "open": [
  "Conflict: wiki and tooltip say Cannot Sell and Cannot Trade, but stores.json item 3998 has no_sale false and a 500-coin purchase price. No vendor names the item, so the coin_shop row stays unverified until a vendor or NPC listing is found.",
  "The tooltip 'Resell Value: 50' likely matches the store sell price of 50; it supports the row's existence but not a vendor sale.",
  "Stat value conflict: render says Health by 220; tooltip and wiki say +712. Unresolved. The client definition has no stat data to settle it.",
  "No retirement date is given for the TCG Series 2 card or the store row. Retired is unknown; live is unsure because the support is undated (wiki and collection page).",
  "The client definition has no model files, and no quest, drop, or event answer mentions the item."
 ]}
