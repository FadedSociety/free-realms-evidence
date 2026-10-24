<!-- fleet job=citem-infer id=cflannel-shirt-106950-v1 status=done turns=4 usd=0.0040 tokens(read,write,in,out)=[23082, 19230, 10, 2822] model=claude-haiku-5-5 -->
# Flannel Shirt

{"item": {"name": "Flannel Shirt", "locale_id": 106950, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Coin-store clothing sale, vendor not identified (store record only; no NPC vendor stocks it in our data)", "where": null, "price": "270 coins (member price 243 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 7297 (purchase_price_coins 270, tint_group 1); also item 33868 (tint 3) at 270 coins; the other variants in the 37-definition family share the same 270-coin record"}],
 "retired": null, "live": "yes",
 "evidence": [{"claim": "Client name 'Flannel Shirt' is locale 106950, item class 1, slot 3 (chest), model freestyle_<race>_m_chest_rolledslvshirt.adr", "source": "locale:106950"},
  {"claim": "Coin store record exists for definition 7297 at 270 coins, member price 243, sell value 27 coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 7297 (line 6254)"},
  {"claim": "Same 270-coin price and 27-coin resell for definition 33868 (tint 3)", "source": "repo:prototype/osfr-tools/data/content/stores.json item 33868 (line 7765)"},
  {"claim": "Video frame shows Flannel Shirt tooltip: resell value 27 coins, Boys only, Required Level 1, Freestyle Jobs", "source": "video:zNMmxK6l5jI/00136.jpg"},
  {"claim": "Video frame lists Flannel Shirt beside Fan Faire 2011 T-Shirt and Camp Robbie Shirt, a shirt group, not a labelled source", "source": "video:zNMmxK6l5jI/00090.jpg"},
  {"claim": "Wiki Farmer and Adventurer job-clothing lists include [Flannel] [Shirt]; these are job-gear lists, not a vendor or acquisition source", "source": "lookup wiki page:ns0 Farmer; page:ns0 Adventurer"}],
 "confidence": 0.4,
 "open": ["Vendor is not named: no NPC vendor in our data stocks stores.json item 7297 or 33868, and vendor_stock was empty. The 270-coin sale is confirmed by store data only, so the vendor/zone is unknown.",
  "Store records for the other definitions in the 37-definition family were not checked one by one; only 7297 and 33868 were confirmed at 270 coins. Item 47 has a 270-coin record but is marked no_sale, so it may be a different item.",
  "Store source_tags (L1, L2, L4, R2, T633, R1) are not decoded here, so the 'live' call relies on the first-pass tag plus the video frame; no wiki page confirms the sale window or any retirement.",
  "Retired status is unknown: no source states that the coin sale ended.",
  "The 'Gender Boys only' note applies to one variant; girls' variants of the shirt family were not checked.",
  "No quest reward, enemy drop, event, prize wheel, or crafting source was found for this item."]}
