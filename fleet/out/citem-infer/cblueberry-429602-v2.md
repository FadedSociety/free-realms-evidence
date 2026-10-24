<!-- fleet job=citem-infer id=cblueberry-429602-v2 status=done turns=2 usd=0.0029 tokens(read,write,in,out)=[5732, 14329, 6, 2193] model=claude-haiku-5-5 -->
# Blueberry

{"item": {"name": "Blueberry", "locale_id": 429602, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Unidentified coin vendor. Only evidence is a coin-store price row: item_id 79479, category 142, purchase 180 coins, member price 162 coins (10% member discount), no_sale true. No NPC, vendor name or zone is evidenced for category 142.", "where": null, "price": "180 coins (member price 162 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 79479 (line 17199); row confirmed on read"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Blueberry' is locale 429602, item class.", "source": "locale:429602"},
  {"claim": "Client has two definitions for the name (77563 and 79479); slot 3; class ids 0 and 1; client coin store price 180 on one definition.", "source": "client definition pack"},
  {"claim": "Store row for definition 79479 is 180 coins, member 162, category 142, no_sale true, with no named vendor.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 79479 (line 17199)"},
  {"claim": "Adjacent rows 79465-79480 carry the same 180-coin / 162-member / category 142 / no_sale profile (checked 17185-17200). This shows a shared store profile only, not a vendor.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 17185-17200"},
  {"claim": "Clothing kind is inferred from slot 3 and the store block; client description is empty. Not confirmed by any wiki, article or video.", "source": "client definition pack"},
  {"claim": "Lookup of 'Blueberry' in client, wiki, articles and video returns only the item name locale 429602 and the unrelated food items 'VIP Blueberry Juice' (locale 29790) and 'Blueberry Juice Barrel' (locale 38101). No wiki page, article or video names this item.", "source": "lookup: client, wiki, articles, video"}
 ],
 "confidence": 0.3,
 "open": [
  "Vendor/NPC and zone for the 180-coin category-142 sale are unidentified. Nothing in the repo names what category 142 is or which coin vendor stocks it. Needs a named vendor or a stock listing before it is stated as a vendor source.",
  "Definition 77563 has no store row and is unresolved (possibly a tint or race variant). Only 79479 is linked to a price here.",
  "Kind 'clothing' is inferred from client slot 3 and class ids, not confirmed by a description.",
  "Live status is unsure. The first-pass 'yes' is not supported by any wiki, article or video, and a store row alone does not show the item is currently sold.",
  "The earlier claim that the 35950-35969 block is 'sold by coin vendors' was not verified and is dropped. The earlier 'VIP Blueberry Juice' locale ids (3305305666, 599388693, 87360, 78478, 47613) were not confirmed; lookup shows the juice items at 29790 and 38101, so those are not used as evidence.",
  "No quest reward, enemy drop, event, prize wheel, crafting, collection, membership or promotion source was found."
 ],
 "critiques_addressed": "Evidence and world critiques applied: the source is kept as a coin-store price row, the vendor is left unnamed and marked open, the sibling-block claim is narrowed to the stores rows, kind and live are marked inferred/unsure, and definition 77563 is left unresolved."}
