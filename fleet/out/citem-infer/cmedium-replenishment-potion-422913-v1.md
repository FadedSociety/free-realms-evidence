<!-- fleet job=citem-infer id=cmedium-replenishment-potion-422913-v1 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[3987, 10691, 6, 1831] model=claude-haiku-5-5 -->
# Medium Replenishment Potion

{"item": {"name": "Medium Replenishment Potion", "locale_id": 422913, "kind": "consumable"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop vendor sale (wiki: 'acquired from the Coin Shop where it sells for 50 coins'; video frame shows the same Coin Shop listing at 45 coins, likely a sale or a later price)", "where": "Coin Shop (Supplies > Potions)", "price": "50 coins (wiki); 45 coins (video frame, probable sale price)", "currency": "coins", "source": "wiki page 'Medium Replenishment Potion' (ns0); video:Sy-W_AHbwcw/00334.jpg"},
  {"type": "other", "detail": "Battle Item Mystery Packs (random pack contents; the wiki names this as a second acquisition route, no pack rates or pack name given)", "where": null, "price": null, "currency": null, "source": "wiki page 'Medium Replenishment Potion' (ns0)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Name and description match client locale 422913 and the tooltip text: restores health and energy instantly; Power 3, Resell Value 5, Level 1 any job, Cannot Trade", "source": "locale:422913; image:item_tooltip 'Medium Replenishment Potion'"},
  {"claim": "Sold in the Coin Shop for 50 coins, and acquired from Battle Item Mystery Packs", "source": "wiki page 'Medium Replenishment Potion'"},
  {"claim": "Coin Shop listing shows Medium Replenishment Potion at 45 coins alongside Medium Health Potion 33 and Medium Energy Potion 22", "source": "video:Sy-W_AHbwcw/00334.jpg"},
  {"claim": "Player purchase of 16 units seen during Den of Secrets (Warrior 7), so the potion was buyable in play", "source": "video:Sy-W_AHbwcw/00342.jpg"},
  {"claim": "Wiki Items > Potions list includes Medium-tier potions alongside the Coin Supplies category", "source": "wiki page 'Items' (ns0)"},
  {"claim": "Two client definitions (3084, 60563) share the name; the client cluster is the Health/Energy/Replenishment potion family, sized Small/Medium/Large", "source": "client definition; locale:422908-422917"}
 ],
 "confidence": 0.75,
 "open": [
  "No coin_store_prices in the client definition and no match for ids 3084 or 60563 in repo data/content/stores.json, so the 50 coin price is wiki-only and cannot be cited as repo store evidence.",
  "Price conflict: wiki says 50 coins, video frame says 45 coins. Treated as a probable sale; the base price is unconfirmed.",
  "Which of the two definitions (3084 vs 60563) is the sold item is not resolved; the second may be a tint or a variant.",
  "Battle Item Mystery Packs: only the wiki names this source. Pack name, drop rate and contents are not verified.",
  "No retirement or removal date found in the sources; retired status left null."
 ]}
