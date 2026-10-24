<!-- fleet job=citem-infer id=cn-flat-color-skinny-jeans-pl-flat-color-skinny-jeans-29957-v2 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[5591, 7328, 6, 1844] model=claude-haiku-5-5 -->
# {n}Flat Color Skinny Jeans{pl="Flat Color Skinny Jeans"}

{"item": {"name": "Flat Color Skinny Jeans", "locale_id": 29957, "kind": "clothing"},
 "sources": [
  {"type": "other", "detail": "Reference coin-store catalogue listing (category 104, tint groups 1-3; items 76504, 77693, 77694). No vendor NPC, stock row, or shop name is attested in any source checked, so the seller is unknown.", "where": null, "price": "270 coins reference Cost (member price 243 coins at 10% member discount; sell price 27 per the T633 rule). Not verified against a real transaction.", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 76504 (line 16142), item 77693 (line 16778), item 77694 (line 16779); repo:notes/Research/Coin Shop.md line 33 (mapping of Cost to starting price not checked against a real client transaction)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 29957, '{n}Flat Color Skinny Jeans{pl=\"Flat Color Skinny Jeans\"}'", "source": "locale:29957"},
  {"claim": "Client definition has 3 tint variants (76504, 77693, 77694), slot 4 (legs), item classes 0 and 1, model freestyle_<race>_f_legs_skinnyjeans.adr", "source": "client definition in pack"},
  {"claim": "stores.json lists 76504 under category 104 with purchase_price_coins 270, member_price 243, sell 27, no_sale false, tint group 1", "source": "repo:prototype/osfr-tools/data/content/stores.json line 16142"},
  {"claim": "Lookup of the name across client, wiki, articles and video returns only the client text entry locale:29957; no wiki page, article or video names the item", "source": "lookup 'Flat Color Skinny Jeans' (all four sources)"},
  {"claim": "Category 104 is shared with other items at different prices (e.g. 9453, 715, 150), and 76501/77695/77696 share the 270 price, so the store data alone does not establish a set listing or a vendor", "source": "critique in pack; repo:stores.json line 16138-16146 (category 103/105/121 rows at 270/750/806)"},
  {"claim": "The T633 tag is a sell-back rule and the L/R tags mark source fields and defaults; they do not evidence a sale", "source": "repo:notes/Research/Coin Shop.md line 33"}
 ],
 "confidence": 0.3,
 "open": [
  "Vendor/NPC that sells the 270-coin listing is not named in any source; the earlier 'vendor' and Cragara attribution is unsupported by evidence for this item (Cragara is only linked to the sibling Torn Skinny Jeans).",
  "270 coins is a reference catalogue Cost, not an observed purchase price; the Coin Shop notes say the Cost-to-price mapping is unchecked.",
  "No wiki page, article, video, quest, drop, event, prize wheel, collection or membership source found for this item.",
  "Live status unknown: no_sale=false is a default, not a dated source that it is sold today. Retired status unknown.",
  "Whether 76504/77693/77694 form one listing or a set with 76501/77695/77696 is unconfirmed; no store-category name for category 104 was found.",
  "Sale/member price 243 is arithmetic (10% member discount) rather than a source-stated price; no wiki price to cross-check."
 ]}
