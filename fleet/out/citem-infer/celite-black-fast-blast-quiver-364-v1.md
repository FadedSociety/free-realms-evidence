<!-- fleet job=citem-infer id=celite-black-fast-blast-quiver-364-v1 status=done turns=15 usd=0.0116 tokens(read,write,in,out)=[321664, 39586, 32, 6871] model=claude-haiku-5-5 -->
# Elite Black Fast Blast Quiver

{"item": {"name": "Elite Black Fast Blast Quiver", "locale_id": 364, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store listing for the quiver at 9453 coins (member price 8507 coins, 10% member discount; sell-back 945 coins). Store entry keyed to item_id 364, which matches this item's name locale id. No vendor NPC or location is named in the store data.", "where": null, "price": "9453 coins (member 8507 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:184 (item_id 364, category_id 102, purchase_price_coins 9453)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Elite Black Fast Blast Quiver' is locale 364, an item name; the Elite Black Fast Blast set (Boots, Gloves, Leggings, Cap, Tunic at locales 25213, 25329, 25561, 25503, 25126) is also in the client.", "source": "locale:364; locale:25213; locale:25329; locale:25561; locale:25503; locale:25126"},
  {"claim": "Same coin store price 9453 on the quiver; the other Elite Black Fast Blast pieces (store item_ids 25126, 25213, 25329, 25503, 25561) are listed at 270 coins, category 6.", "source": "repo:prototype/osfr-tools/data/content/stores.json:184, 5187, 5274, 5390, 5564, 5622"},
  {"claim": "The wiki Archer page lists the Fast Blast clothing set (level 5), which the quiver belongs to, and names Sanctuary and Greenwood Camp as Archer clothing vendors, but does not name Elite Black variants or a price.", "source": "freerealms-wiki/wikitext/16430-46065-fb3ad83055a6.wiki lines 115-133 (Archer page)"},
  {"claim": "Client also has a base Fast Blast Quiver (locale 367) and an Elite Pink variant (locale 8280); the Elite Pink quiver has no store entry in stores.json.", "source": "locale:367; locale:8280; repo stores.json search (no match for 8280)"},
  {"claim": "The client definition for this item is definition 3026, and stores.json item 3026 is a separate category-106 listing at 9453 coins. The price match is therefore not confirmed as the same item; store item_id 364 matches the name locale id instead.", "source": "repo:prototype/osfr-tools/data/content/stores.json:783 (item_id 3026, category 106); stores.json:184 (item_id 364)"}
 ],
 "confidence": 0.4,
 "open": [
  "Mapping of store item_id to client definition: the pack lists definition 3026 but the 9453 store record is keyed to item_id 364 (the name locale id). The store file has another 9453 listing under item_id 3026 (category 106). Confirm which key the coin store uses before the rebuild relies on it.",
  "The store category meanings (102 and 106) are not documented in the repo, so the vendor or shop name is unknown. No NPC, zone, or Coin Shop wiki page names this quiver.",
  "No wiki page, article, video frame, or quest/drop answer mentions the Elite Black Fast Blast Quiver. Its live status is unsure: the store record has no_sale false, but there is no dated source.",
  "The 'Elite' tier pricing (9453 for the quiver vs 270 for the rest of the set) is not explained by any source here.",
  "Retired status is unknown: no source states that it was retired or made unobtainable."
 ]}
