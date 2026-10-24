<!-- fleet job=citem-infer id=cpet-dog-large-floppy-solid-ivory-75149-v1 status=done turns=4 usd=0.0036 tokens(read,write,in,out)=[20189, 16903, 10, 2565] model=claude-haiku-5-5 -->
# Pet: Dog: Large Floppy: solid-ivory

{"item": {"name": "Pet: Dog: Large Floppy: solid-ivory", "locale_id": 75149, "kind": "pet"},
 "sources": [{"type": "vendor", "detail": "Coin store listing (unnamed vendor): 540 coins, member price 486 coins (10% member discount); sell-back 54 coins. No stocking NPC is named in the pack; the coin store row is the only source evidence.", "where": null, "price": "540 coins (member price 486 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 23999 (purchase_price_coins 540, member_price_coins 486, sell_price_coins 54, tint_group_id 1; source_tags L1,L2,L4,R2,T633,R1, derived from FreeRealms-Legacy CoinStoreItems.json)"}],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Pet: Dog: Large Floppy: solid-ivory' is locale 75149, one definition (definition id 23999), slot 0, model dog_large_floppy.adr.", "source": "client definition in pack; locale:75149"},
  {"claim": "The coin store has item 23999 at 540 coins, member price 486 coins, sell price 54 coins, not flagged no_sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 23999"},
  {"claim": "Item 23999 sits in a block of Large Floppy/dog-family coin store rows (23963-24000 range) with the same 540-coin price, so the pet is part of the coin-store pet batch.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 6840-6877"},
  {"claim": "The client has sibling Large Floppy pet variants (solid-gold, solid-brown, spots-gold, etc.) and an 'Illusion: Dog Large Floppy - 30 minutes' item, consistent with a family of dog pets sold together.", "source": "locale:75104-75110; FreeRealmsLocaleTools en_us_data.dat 'Illusion: Dog Large Floppy - 30 minutes'"},
  {"claim": "No wiki page, image, article or video in the pack names this item; no vendor stock list names it.", "source": "pack fields wiki_page null, images [], article_facts [], video [], vendor_stock []"}
 ],
 "confidence": 0.5,
 "open": [
  "Which coin vendor (NPC and zone) stocks item 23999 is not evidenced; the 540-coin store row is the only sourced price and does not name a vendor.",
  "Live status is unsure: the store row is not no_sale, but no wiki page or current source confirms it is still sold; the pack's first-pass 'live: yes' is a hint only.",
  "Retired status unknown: no source states retirement or removal.",
  "No Station Cash price found for this item (only the coin store row).",
  "Quest, drop, event, and prize-wheel sources not found in the pack.",
  "Description field equals the name, so no extra flavor or source text is available."
 ]}
