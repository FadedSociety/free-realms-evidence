<!-- fleet job=item-infer id=iwalt-v2 status=blocked turns=2 usd=0.0022 tokens(read,write,in,out)=[5181, 7466, 6, 2390] model=claude-haiku-5-5 -->
# Walt

{"item": {"name": "Walt (NPC merchant, not an item)", "locale_id": 5102403, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Walt, Human Postman merchant (npc_id 9500000642). Wiki stock list: Postman's Power Shard of Timing II, Postman's Necklace of Timing II, Postman's Ring of Talent II, Parcel Postman Short Shorts, Parcel Postman Shorts, Parcel Postman Hat, Parcel Postman Wristbands, Parcel Postman Shoes, Parcel Postman Shirt. Prices are not stated on the wiki.", "where": "Seaside (near the Seaside Warpstone)", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Walt (rev 33641, Sells list and Category:Seaside)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "locale:5102403 is an npc_name entry for 'Walt', so the input is an NPC, not a sellable item", "source": "locale:5102403"},
  {"claim": "Walt is a Human Male Merchant and Postman NPC in Seaside, introduced in the 1 October 2013 update, selling Postman job items; no prices given", "source": "https://freerealms.fandom.com/wiki/Walt"},
  {"claim": "The wiki Sells list names the Postman shard, necklace and ring plus nine Parcel Postman pieces (Short Shorts, Shorts, Hat, Wristbands, Shoes, Shirt); each has its own client item locale (e.g. Parcel Postman Hat locale:132986, Parcel Postman Shirt locale:132983, Parcel Postman Shoes locale:132984, Parcel Postman Wristbands locale:132985, Parcel Postman Shorts locale:132987, Parcel Postman Short Shorts locale:132988)", "source": "https://freerealms.fandom.com/wiki/Walt; locale:132983-132988"},
  {"claim": "Repo vendor record for Walt lists 'Parcel Postman set, Postman shard, necklace, ring' with nine resolved_item_ids (75975-75980, 76509, 76510, 76520) on lines 7258-7268 and an empty unresolved_items list on line 7276. The 'partial' note and the '7 named stock rows remain unresolved' text are in prior_reason on line 7298 (a 2-unique-ID count there conflicts with the nine IDs listed)", "source": "repo:prototype/osfr-tools/data/content/vendors_unresolved.json:7255-7300"},
  {"claim": "Repo notes the stock list is partial evidence with no captured native merchant list", "source": "repo:prototype/osfr-tools/data/content/vendors_unresolved.json:7287"}
 ],
 "confidence": 0.3,
 "open": [
  "The input is the NPC Walt, not one item. No single item was selected. To produce a real item record, re-run with one of the stocked items (e.g. Parcel Postman Hat, locale:132986, or Postman's Ring of Talent II).",
  "Prices and currency for every Walt stock item are unknown. The wiki gives none, and nothing in the pack supports coins or Station Cash.",
  "Live status and retirement are unverified. The wiki page is a 2013-10-09 revision and says nothing about later removal.",
  "Repo conflict: prior_reason at line 7298 says 2 unique item IDs map, but resolved_item_ids lists 9. Count needs reconciling before wiring.",
  "The previous answer's citation of 'unresolved_items' as 7 rows was wrong; the 7 figure is only in prior_reason text. Corrected here."
 ]}
