<!-- fleet job=citem-infer id=cscorch-swift-helmet-106354-v2 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[14167, 11882, 8, 2356] model=claude-haiku-5-5 -->
# Scorch Swift Helmet

{"item": {"name": "Scorch Swift Helmet", "locale_id": 106354, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Unnamed coin vendor. Only evidence is a coin store row (category 101 clothing, tint group 1). No vendor NPC or vendor stock row names this item; repo category 101 is shared by many clothing items with no vendor mapping found.", "where": null, "price": "320 coins (member price 288 coins, 10% member discount; sell price 32 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 33272 (line 11104); tints 33273 (line 11105) and 33274 (line 11106) also 320 coins"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 106354 'Scorch Swift Helmet'; helmet, slot 1, class 24, 36 definitions over ids 33272-33283, model freestyle_<race>_<gender>_head_motorcyclehelmet.adr.", "source": "client definition in pack; locale:106354"},
  {"claim": "Store row for item 33272: category 101, tint group 1, purchase_price_coins 320, member_price_coins 288, sell 32, no_sale false, source tags L1/L2/L4/R2/T633/R1. Rows for 33273 and 33274 (tints 2 and 3) match.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 11104-11106"},
  {"claim": "Row has no price_provenance block, so the 320 price is store-data reconstruction, not a wiki- or live-verified price. The 288 figure is the 10% member discount, not a promotion.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 11104"},
  {"claim": "Client flavor text: 'Make the other helmets self conscious about their lack of flames.' Descriptive only; says nothing about acquisition.", "source": "locale:109086"},
  {"claim": "No wiki page, image, article fact or video frame names this helmet (lookup of wiki, articles and video returned no matches). Repo search found no vendor stock row for it.", "source": "lookup wiki/articles/video 'Scorch Swift Helmet' (no matches); repo search for 33272 and motorcyclehelmet"},
  {"claim": "Critique applied: locale:150521 is a placeholder ('This is a ... item.') and is dropped as evidence. Vendor is not named, so it is not claimed as a specific NPC.", "source": "locale:150521 (FLAG placeholder); critique of previous answer"}
 ],
 "confidence": 0.4,
 "open": [
  "Vendor not identified. stores.json category 101 is a generic clothing category shared by many items, and no stock row maps this helmet to an NPC. Needs a vendor stock lookup before the rebuild wires it.",
  "The 320-coin price comes from our store data only. No wiki, article or video confirms it.",
  "Tints 33275-33283 (other definitions) have no store rows checked here. Items 33307-33309 in category 101 are different ids and are not confirmed as this helmet's tints.",
  "Retirement status unknown: no source says whether it left the coin store later.",
  "Quest reward, drop, event, prize wheel, crafting and collection sources not checked; none are cited anywhere in the pack.",
  "Live status is 'unsure': the only sources are legacy-derived store rows and the client definition, with no current-server confirmation."
 ]}
