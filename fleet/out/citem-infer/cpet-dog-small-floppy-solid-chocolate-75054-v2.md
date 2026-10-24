<!-- fleet job=citem-infer id=cpet-dog-small-floppy-solid-chocolate-75054-v2 status=done turns=2 usd=0.0028 tokens(read,write,in,out)=[5511, 13814, 6, 1971] model=claude-haiku-5-5 -->
# Pet: Dog: Small Floppy: solid-chocolate

{"item": {"name": "Pet: Dog: Small Floppy: solid-chocolate", "locale_id": 75054, "kind": "pet"},
 "sources": [
  {"type": "vendor", "detail": "Unnamed coin-store sale: no NPC or vendor is evidenced for definition 23904 (vendor_stock empty); the price comes only from the legacy store row", "where": null, "price": "540 coins (member price 486 coins at 10% member discount; sell-back 54 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 23904 (line 6781: purchase_price_coins 540, member_price_coins 486, sell_price_coins 54, category_id null, no price_provenance block); client definition 23904 coin_store_prices 540"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition 23904 is named 'Pet: Dog: Small Floppy: solid-chocolate' (locale 75054), model dog_small_floppy.adr, one definition, no tint or race variant under this name", "source": "locale:75054; client definition in pack"},
  {"claim": "stores.json row for 23904 carries a legacy coin price of 540 with no category, no vendor and no price_provenance block", "source": "repo:prototype/osfr-tools/data/content/stores.json item 23904 (line 6781)"},
  {"claim": "The repo clears the legacy 540 cost where no coin vendor stocks the item and reclassifies the row to Station Cash (T638). Items 23902, 23906, 23912 and 23913 were handled this way; 23904 has no such note, so its 540 is unreviewed legacy data, not a checked vendor price", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 42 and 6779 (price_provenance for 23902), lines 6783, 6789, 6790"},
  {"claim": "The same-named cluster 75050-75059 (solid and darkmark Small Floppy variants) shares the name prefix; no wiki page, image, article fact or video frame names any of them", "source": "locale:75050-75059; lookup of 'Small Floppy dog pet' returned client text only"}
 ],
 "confidence": 0.3,
 "open": [
  "Coin vendor and NPC unknown: no source names who sells 23904. The 540 coin price is a legacy store-table value only, and the repo's own convention clears such values where no vendor stocks the item (see 23902 provenance). Treat it as unverified until a vendor or wiki price is found.",
  "The earlier answer labelled this a 'Coin Shop' listing. The row has no category or Coin Shop provenance, so that label is removed here; it is recorded only as a coin-store row.",
  "The earlier answer used 'neighbours share 540' as support. The neighbours carry the same unreviewed legacy value, so that is not independent confirmation.",
  "No wiki, article, video or quest/drop/prize-wheel/promotion source found. Retirement and current availability are unknown; live is 'unsure' (the first-pass 'yes' has no source).",
  "Wireable only weakly: the sole price evidence is the unverified legacy store row."
 ],
 "wireable_note": "weak"}
