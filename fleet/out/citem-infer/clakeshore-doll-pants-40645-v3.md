<!-- fleet job=citem-infer id=clakeshore-doll-pants-40645-v3 status=done turns=3 usd=0.0018 tokens(read,write,in,out)=[13125, 7359, 8, 1540] model=claude-haiku-5-5 -->
# Lakeshore Doll Pants

{"item": {"name": "Lakeshore Doll Pants", "locale_id": 40645, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Piece of the Lakeshore Human Doll collection. Adding pieces, this one included, completes the collection for the reward 'Human Lakeshore Doll' plus 21 Gold Coins. The 21 coins is a collection-completion reward, not a purchase price.", "where": null, "price": null, "currency": null, "source": "freerealms-wiki/harvest/lists/catalog.json:1777-1785 (CollectInfobox 'Lakeshore Human Doll', text 'Lakeshore wear for the Human doll.', reward 'Human Lakeshore Doll' + 21 Gold Coins); wiki 'Toys (Collections)' lists '[Lakeshore] [Doll] [Pants]'; locale:132314 ('This item can be added to the Lakeshore Human Doll Collection')"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item locale 40645 'Lakeshore Doll Pants' exists; clothing-slot item with no model files and no coin store price", "source": "locale:40645 (client definition)"},
  {"claim": "Description 'This item can be added to the Lakeshore Human Doll Collection' is locale 132314 (verified by lookup)", "source": "locale:132314"},
  {"claim": "Wiki page 'Toys (Collections)' lists '[Lakeshore] [Doll] [Pants]' as a piece of the Lakeshore Human Doll collection", "source": "wiki page 'Toys (Collections)' (lookup result)"},
  {"claim": "Collection reward is 'Human Lakeshore Doll' plus 21 Gold Coins; collection-level spawn Robgoblin, area Central Wilds, quality Common", "source": "freerealms-wiki/harvest/lists/catalog.json:1777-1785"}
 ],
 "confidence": 0.35,
 "open": [
  "No per-piece acquisition source is evidenced. The Robgoblin/Central Wilds spawn is collection-level in the wiki and is not attributed to the pants piece, so it is not listed as a drop. Verify in game or by video.",
  "Client coin_store_prices is empty and vendor_stock is empty, so no coin vendor or Coin Shop sale is evidenced.",
  "No quest reward, crafting, event, prize-wheel, or Station Cash marketplace source found.",
  "Live status and retirement are unconfirmed; the wiki collection data may reflect an older revision.",
  "Critique fix applied: the earlier cited locale id 3078398434 was dropped in favour of locale:132314; the drop source was removed; the 21 coins was moved out of the price fields."
 ]}
