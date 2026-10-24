<!-- fleet job=citem-infer id=cstalking-panther-cowl-490-v2 status=done turns=2 usd=0.0024 tokens(read,write,in,out)=[5756, 9839, 6, 2133] model=claude-haiku-5-5 -->
# Stalking Panther Cowl

{"item": {"name": "Stalking Panther Cowl", "locale_id": 490, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale of definition 476 (tint group 1). The store/vendor NPC is not named in any repo or wiki source checked.", "where": "Coin store, stores.json category_id 101", "price": "715 coins (member price 643 coins, 10% member discount; sell price 71 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 230 (item_id 476)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Stalking Panther Cowl' is locale 490, item type, no client description.", "source": "locale:490"},
  {"claim": "stores.json line 230 has item_id 476, category_id 101, tint_group_id 1, purchase_price_coins 715, member_price_coins 643, sell_price_coins 71. I re-read the row and it matches.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 230"},
  {"claim": "stores.json line 233 has item_id 479 (tint group 2) at 9453 coins, member 8507, sell 945. That is the same price block as item_ids 462, 464, 468 and 481 (lines 220-224, 235), all with null tint, so it looks like a generic or placeholder price and is not used as a source.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 220-235"},
  {"claim": "The wiki has no page for the cowl. The sibling Stalking Panther Scythe is a Ninja weapon crafted by Blacksmith, which is a different item and is not a source for the cowl.", "source": "notes/Build Guides/Content/Jobs/Blacksmith.md line 260 (Stalking Panther Scythe)"},
  {"claim": "A lookup of the name in client, wiki, articles and video returns only the client locale entry 490. No quest, drop, event, or collection link was found.", "source": "lookup 'Stalking Panther Cowl' (client, wiki, articles, video)"},
  {"claim": "The 'category 101 = head/clothing' gloss from the earlier answer is unsupported. Category 101 is shared by many store rows, so it is only the store category id.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 228-239"}
 ],
 "confidence": 0.4,
 "open": [
  "The coin vendor or store NPC that sells item 476 is not named in the repo or wiki. The source is the coin store row only, so the 'vendor' type rests on the store data.",
  "The 9453-coin tint-2 row for definition 479 is excluded as a suspected generic price block shared with unrelated items. It should be re-checked against the original store before anyone relies on it.",
  "Definition ids 19565-19583 (the other variants) have no store rows, so their sources are unknown.",
  "No wiki page exists for the cowl, so retirement is unknown. The coin-store row suggests a legacy sale, but live status is unconfirmed.",
  "Sibling items locale 485-494 (Wristguards, Hakama) were not checked for sources."
 ]}
