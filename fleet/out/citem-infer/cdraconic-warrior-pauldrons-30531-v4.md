<!-- fleet job=citem-infer id=cdraconic-warrior-pauldrons-30531-v4 status=nothing_found turns=2 usd=0.0018 tokens(read,write,in,out)=[5763, 7564, 6, 1607] model=claude-haiku-5-5 -->
# Draconic Warrior Pauldrons

{"item": {"name": "Draconic Warrior Pauldrons", "locale_id": 30531, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 30531 'Draconic Warrior Pauldrons'; one client definition (definition_ids [9292]), slot 6 (shoulders), item class 173, model warrior_<race>_<gender>_shoulders_thickflaredpauldron.adr.", "source": "locale:30531; client definition (from evidence pack)"},
  {"claim": "Store row for item_id 9292: category 106, tint_group 1, purchase_price_coins 1761, member_price_coins 1584 (10% member discount), sell_price_coins null, no_sale true. This is a price record for a row marked no-sale, not evidence of a sale or vendor.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 2712 (re-read and confirmed)"},
  {"claim": "Client definition coin_store_prices lists 1761, matching the stores.json row price.", "source": "client definition coin_store_prices (from evidence pack)"},
  {"claim": "Neighbouring store rows 9284, 9286, 9288, 9291 share the 1761 price and tint_group 1 with no_sale true. Not mapped to names, so no set is asserted.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 2708-2711"},
  {"claim": "Client text lookup returns only locale 30531, 42271 (rich-text duplicate of the name) and 150505 (generic placeholder 'This is a ... item.'). No wiki page, article, image or video names the item. Adjacent locale 30526-30534 items are adjacency only.", "source": "lookup client/wiki/articles/video for \"Draconic Warrior Pauldrons\""}
 ],
 "confidence": 0.3,
 "open": [
  "No acquisition source is evidenced. The 1761-coin price is a no-sale store record (no_sale:true, sell_price_coins null) and must not be wired as a coin vendor sale. The earlier 'vendor' source is withdrawn.",
  "No vendor NPC, shop or zone is named; the store data gives only category 106. vendor_stock is empty.",
  "No wiki price, retirement date or live-status source found; retired is null and live is unsure. The cheap-model 'live: yes' hint is not supported.",
  "No quest reward, enemy drop, event, prize wheel, crafting, collection, membership or promotion source found.",
  "wireable: false. Acquisition stays unknown until a sold row, vendor NPC or other source is found.",
  "Set grouping of ids 9284-9292 is inferred from store rows only and needs a name mapping before it is asserted."
 ],
 "critique_response": "Both critiques (world, evidence) are accepted: the vendor source was removed because the store row is no_sale with no sale or NPC evidence, the 1761 price is kept as an unconfirmed price record corroborated by coin_store_prices, and wireable is set false."}
