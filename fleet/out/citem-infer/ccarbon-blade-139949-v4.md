<!-- fleet job=citem-infer id=ccarbon-blade-139949-v4 status=done turns=2 usd=0.0030 tokens(read,write,in,out)=[6513, 13904, 6, 2469] model=claude-haiku-5-5 -->
# Carbon Blade

{"item": {"name": "Carbon Blade", "locale_id": 139949, "kind": "weapon"},
 "sources": [
  {"type": "drop", "detail": "Blue Text weapon class: dropped at random by certain boss enemies in dungeons (category-level only; no specific boss, dungeon or drop rate named; conflicts with the item page's 'trade only' wording)", "where": "dungeons (unspecified)", "price": null, "currency": null, "source": "wiki: Category:Blue Text Weapons (members-only weapons acquired in dungeons, dropped at random by certain boss enemies; names retired 14 Dec 2009); wiki: Carbon Blade (carries Category:Blue Text Weapons)"},
  {"type": "other", "detail": "Player-to-player trade only (wiki status; no trade vendor or trade system source named)", "where": null, "price": null, "currency": null, "source": "wiki: Carbon Blade ('can only be acquired through trade')"}
 ],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Client name 'Carbon Blade' is locale 139949; weapon class 6, slot 7, definition 48199, model sword_ar_ag_weapon_twistedblade.adr", "source": "locale:139949; client definition in pack"},
  {"claim": "Carbon Blade is a level 5 Ninja Blue Text weapon with Flame Flash 776 and Dragonstrike 3492 damage; it is in Category:Retired Weapons and says it 'can only be acquired through trade'", "source": "wiki: Carbon Blade"},
  {"claim": "Blue Text weapons were members-only weapons acquired in dungeons, dropped at random by certain boss enemies; names retired 14 Dec 2009", "source": "wiki: Category:Blue Text Weapons"},
  {"claim": "Blue Text weapon page lists Carbon Blade among the Blue Text weapons", "source": "wiki: Blue Text weapon"},
  {"claim": "stores.json item 48199 is in a bulk category-207 block (items 48177-48219 share purchase 811, member 729, sell 81, source_tags L1,L2,L4,R2,T633,R1; line 13248 holds 48199). The block changes at 48220 (purchase 1431), so the block's start is earlier than 48177 and its end is 48219. It has no vendor id.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 13226-13270"},
  {"claim": "Client coin_store_prices for 48199 is 811, matching the bulk row price", "source": "client definition in pack"},
  {"claim": "No vendor NPC or vendor stock names item 48199", "source": "pack vendor_stock empty"}
 ],
 "confidence": 0.3,
 "open": [
  "data_anomaly: the 811-coin / 729 member / 81 sell price is a bulk category-207 store row with no vendor id, shared by about 43 items (48177-48219). It is not a vendor sale and is not listed as a source. The wiki gives no coin price for Carbon Blade. Treat as unverified legacy data.",
  "Conflict: the item page says 'can only be acquired through trade', but the Blue Text category says dungeon boss drops. The drop source is category-level for the whole Blue Text class, not evidenced for this item. Not wireable to any enemy table.",
  "wireable: false. No specific boss, dungeon, drop table, or trade system is evidenced for item 48199.",
  "Corrections to the earlier pack: the stores.json block range is wider than the 48183-48213 or 48179-48217 ranges given; verified rows 48177-48219 match. The earlier critique that the Blue Text category text could not be found is wrong: the category text was found (wiki Category:Blue Text Weapons).",
  "Retired: names retired 14 Dec 2009 per the category page; item is in Category:Retired Weapons. No later availability was found."
 ]}
