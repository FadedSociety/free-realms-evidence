<!-- fleet job=citem-infer id=cwhite-wedge-block-21715-v4 status=done turns=2 usd=0.0031 tokens(read,write,in,out)=[6284, 14759, 6, 2339] model=claude-haiku-5-5 -->
# White Wedge Block

{"item": {"name": "White Wedge Block", "locale_id": 21715, "kind": "furniture"},
 "sources": [
  {"type": "vendor", "detail": "Unnamed coin-store vendor, store category 147, purchase row for item 77093 (50 coins, member price 45, no sell price, no_sale true). Vendor/NPC not identified in any source.", "where": null, "price": "50 coins (member 45)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:16424 (item_id 77093, category_id 147); link 77093 -> locale 21715 taken from the evidence pack's client_definition, not confirmed by me in the client"},
  {"type": "vendor", "detail": "Unnamed coin-store vendor, store category 147, purchase row for item 77173 (350 coins, member price 315, sell price 35, no_sale false). Vendor/NPC not identified in any source.", "where": null, "price": "350 coins (member 315; sell-back 35)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json (item_id 77173 row; category 147 block, rows 77105-77124 are the 350-coin tier, the 77173 row is in the same file near line 16504); link 77173 -> locale 21715 from the evidence pack's client_definition, not confirmed by me in the client"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text: locale 21715 is 'White Wedge Block' (item), in the Wedge Block colour family 21710-21716, plus 30240 'White Wedge Tiger Block'.", "source": "locale:21715; locale:21710-21716; locale:30240"},
  {"claim": "Repo coin-store rows for category 147 exist for items 77093 (50 coins, member 45, no_sale true) and 77173 (350 coins, member 315, sell 35, no_sale false). I re-read stores.json lines 16418-16468 and confirmed the 77093 row at line 16424 and the 77105-77124 350-coin tier.", "source": "repo:prototype/osfr-tools/data/content/stores.json:16424"},
  {"claim": "Definition ids 77093 and 77173 are the pack's client definitions for locale 21715 (model hsg_block_wedge_01.adr, coin prices 50 and 350). My client search for those numbers only hit asset manifest and locale data, so I could not independently confirm the item-table link.", "source": "evidence pack client_definition; client search for 77093|77173"},
  {"claim": "No wiki page, article, video frame, quest, drop, prize wheel or crafting source names White Wedge Block.", "source": "lookup wiki/articles/video/client for 'White Wedge Block' (only locale:21715 and locale:30240 returned)"}
 ],
 "confidence": 0.4,
 "open": [
  "The vendor/NPC for store category 147 is not named in the repo or wiki; both vendor sources are unnamed coin-store sales.",
  "The item-definition link (77093 and 77173 -> locale 21715) rests on the evidence pack's client_definition. I could not confirm it in the client item table. It is the basis for both sources.",
  "The 77093 row has no_sale true with no sell price. I read this as no sell-back to the vendor, not as 'not for sale', but the field's meaning is not documented here. Both rows may be the same item at two prices or two SKUs; unresolved.",
  "Category 147 source tags (L1, L2, L4, R2, T633, R1, L3) are undecoded, so the sale channel is unknown.",
  "kind 'furniture' is a guess from the hsg_ model prefix and the 'Great for stackability' description; no category source confirms it.",
  "live is 'unsure': no dated source for current availability; retirement is unknown, not established.",
  "Quest, drop, prize wheel, crafting, Station Cash, event and holiday sources were checked only by absence; none found. The nearby client line locale:21717 ('Yummy! I can't wait for the queen to say we can eat!') is an NPC dialog line, not a source for this item."
 ]}
