<!-- fleet job=citem-infer id=cwhite-wedge-block-21715-v2 status=nothing_found turns=2 usd=0.0024 tokens(read,write,in,out)=[6195, 11225, 6, 1779] model=claude-haiku-5-5 -->
# White Wedge Block

{"item": {"name": "White Wedge Block", "locale_id": 21715, "kind": "furniture"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text: locale 21715 is 'White Wedge Block' (item). Same family in client text: Wedge Block (29985), Basic/Cheese/Polkadot/Tiger Wedge Block (8671-8704), Black/Blue/Green/Orange/Pink... Wedge Block (21707-21716).", "source": "locale:21715; locale:29985; locale:8671; locale:21707-21716 (lookup client)"},
  {"claim": "Store rows exist for item_id 77093 (category 147, purchase 50 coins, member 45, no_sale true) and item_id 77173 (category 147, purchase 350 coins, member 315, sell 35, no_sale false).", "source": "repo:prototype/osfr-tools/data/content/stores.json:16424 and :16504"},
  {"claim": "Definition ids 77093 and 77173 do not appear as item-definition or locale ids in the client. Searching the client for them only hits unrelated asset-manifest and locale strings, so the store rows are not linked to locale 21715.", "source": "search client '77093|77173' (Assets_manifest.txt, locale/en_us_data.dat)"},
  {"claim": "No wiki page, article, video frame, vendor, quest, drop or prize-wheel answer names White Wedge Block.", "source": "lookup wiki/articles/video; pack vendor_stock and mentioned_by_other_answers empty"}
 ],
 "confidence": 0.2,
 "open": [
  "No verified acquisition source. The two stores.json rows (items 77093 at 50 coins and 77173 at 350 coins, both category 147) are unlinked: nothing in the repo or client maps those definition ids to locale 21715. They are candidate coin-store SKUs only, not sources of this item. The previous answer's 'vendor' labels are withdrawn; no shop NPC or Coin Shop page names a vendor.",
  "The 50 and 350 coin split is unexplained. Do not treat them as two products of this item until a definition table row shows the mapping.",
  "kind 'furniture' is a first-pass guess from the model file hsg_block_wedge_01.adr and the 'Wedge Block' family naming. No category data or wiki source confirms housing decor.",
  "live is unsure: the store rows are present but unlinked, and no source confirms current availability. Retirement is unknown, not established.",
  "Quest, drop, prize wheel, crafting, Station Cash, and event sources were checked only by absence in the pack; none were found.",
  "Locale 21717 (queen/eating NPC dialog) sits in the cluster but is not an item and was not used.",
  "Next step: find the client item-definition table row for definitions 77093 and 77173 (name_locale_id) and any store or NPC data that names the shop selling category 147."
 ]}
