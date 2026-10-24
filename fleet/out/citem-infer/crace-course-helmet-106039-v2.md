<!-- fleet job=citem-infer id=crace-course-helmet-106039-v2 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[5104, 10771, 6, 2131] model=claude-haiku-5-5 -->
# Race Course Helmet

{"item": {"name": "Race Course Helmet", "locale_id": 106039, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale of the Race Course Helmet (head slot, class 24) in tint groups 1-3; store rows carry only numeric ids, so the link to this name is by client definition (coin_store_prices 270), not by name", "where": "Coin Shop, store category 101", "price": "270 coins regular; 243 coins with 10% member discount; sell price 27 coins; no_sale false", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 32957 (tint_group 1), item 32958 (tint_group 2), item 32959 (tint_group 3), lines 11077-11079"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition: name 'Race Course Helmet', locale 106039, slot 1, class 24, 35 definitions, model freestyle_<race>_<gender>_head_helmetwglasses.adr, coin_store_prices [270]", "source": "locale:106039; client definition as supplied in the pack"},
  {"claim": "stores.json has rows only for item_ids 32957, 32958, 32959 in this block (category 101, tint groups 1-3, 270 / 243 member / 27 sell, no_sale false). No stores.json rows exist for 32960-32968; a search of the data/content folder for those ids returned no store hits.", "source": "repo:prototype/osfr-tools/data/content/stores.json:11077-11079; search of repo data/content for 32957-32968"},
  {"claim": "The same 270-coin price and category 101 also appear on neighbouring clothing ids (32817, 32851, 32992-32994, 33027-33029), so the price alone does not identify the helmet; the id match rests on the client definition.", "source": "repo:prototype/osfr-tools/data/content/stores.json:11075-11085"},
  {"claim": "Article 2049 (French copy) says players were told to wear a helmet for the race and non-racers could join an off-track party beside the race. This is event context only; it does not mention a sale or name the event.", "source": "http://www.freerealms.com/article/detail.action?articleId=2049 (articles fact:event)"},
  {"claim": "No wiki page for Race Course Helmet was found; no vendor row in vendors.json, quest reward, drop or prize-wheel source names it.", "source": "lookup of wiki/client/articles for 'Race Course Helmet'; vendors.json search"}
 ],
 "confidence": 0.4,
 "open": [
  "The coin-shop source is an id-matched inference: stores.json rows have no names. Confirm that items 32957-32959 are the Race Course Helmet by checking the citem-packs definition list (refs quest-lines/citem-packs.json) before treating the price as settled.",
  "Only 3 of the 35 definitions (tint groups 1-3 of ids 32957-32959) have a store row. Ids 32960-32968, also listed in the client definition, have no store evidence, so their price and source are unknown.",
  "The wiki category 'Coin Shop Clothing' is real but lists clothes in general; it does not name this helmet, so no category mapping is claimed here.",
  "Article 2049 names no event, dates or sale. The race event that the helmet belonged to is unidentified; it is not a source.",
  "Retirement and current availability are unknown. no_sale false is a repo flag, not a live check. The first-pass 'live: yes' tag was not used as evidence.",
  "No vendor, quest, drop, prize-wheel or crafting source was found."
 ]}
