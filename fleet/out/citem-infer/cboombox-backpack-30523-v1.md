<!-- fleet job=citem-infer id=cboombox-backpack-30523-v1 status=done turns=5 usd=0.0050 tokens(read,write,in,out)=[45534, 22978, 12, 3417] model=claude-haiku-5-5 -->
# Boombox Backpack

{"item": {"name": "Boombox Backpack", "locale_id": 30523, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Unidentified coin vendor (stock list not recorded). Store row for item 9284 (tint group 1), 10891 (tint group 2), 10932 (tint group 3), all in store category 106 at 1761 coins (member price 1584 coins, 10% member discount).", "where": null, "price": "1761 coins (member 1584 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 9284 (line 2708); item 10891 (line 3196); item 10932 (line 3217)"}],
 "retired": null, "live": "unsure",
 "evidence": [{"claim": "Client name 'Boombox Backpack' is locale 30523; a second client line 42267 carries the same name, and locale 150499 is a placeholder ('This is a Boombox Backpack item.') that should not be used as the description.", "source": "locale:30523; locale:42267; locale:150499"},
 {"claim": "The client definition has 3 definitions (ids 9284, 10891, 10932), slot 6, class 7, model military_<race>_<gender>_shoulders_backpack.adr. The three ids are the three tints of one backpack.", "source": "client definition pack; repo:prototype/osfr-tools/data/content/stores.json item 9284 tint_group 1, item 10891 tint_group 2, item 10932 tint_group 3"},
 {"claim": "Each of the three store rows lists a coin price of 1761 with a member price of 1584 and no_sale true. The row is a coin store price for a coin vendor sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json items 9284, 10891, 10932"},
 {"claim": "The wiki 'Boombox' pages (Clockwork, Robot, Hootenanny, Chiller and others) are about boomboxes, a different item type. The name match does not cover this backpack, so they are not evidence for it.", "source": "lookup wiki 'Boombox' (Items, Boomboxes, Chiller Boombox pages)"},
 {"claim": "No wiki page, image, article fact, video frame, quest reward, drop or other answer names this backpack. The neighbouring client items (Skull Strike Hoodie, Flame Spike Helmet, Oni Shoulderguard, Horned Mask) have no source either.", "source": "lookup client/wiki/articles/video for the cluster names; pack vendor_stock and mentioned_by_other_answers empty"}],
 "confidence": 0.4,
 "open": ["Which coin vendor stocks it is not recorded. The store row gives a price and category 106 but no vendor name, and no wiki or client source names the vendor. Find the vendor that sells store category 106 rows in vendors.json, or a wiki Coin Shop/Mysterious Merchant page.",
 "Live status is unclear. no_sale=true on all three rows could mean it is no longer sold, but no source says it was retired. Confirm with a dated wiki or forum source.",
 "The 'levels up with you' description suggests a later-era armor; no wiki page confirms a release date.",
 "The three tints (ids 9284, 10891, 10932) are assumed to be one item in three colours from the shared name, slot and store price; no source confirms the tint names.",
 "The Boombox name overlap is coincidental: the wiki boombox articles are about a different item type and were not used.",
 "The first-pass tag said vendor, live yes. The vendor is supported only by the store price, and live is only partly supported, so it is marked unsure."]}
