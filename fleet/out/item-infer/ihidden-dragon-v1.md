<!-- fleet job=item-infer id=ihidden-dragon-v1 status=nothing_found turns=2 usd=0.0013 tokens(read,write,in,out)=[3301, 4171, 6, 1513] model=claude-haiku-5-5 -->
# Hidden Dragon

{"item": {"name": "Hidden Dragon", "locale_id": 5102393, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "The wiki page 'Hidden Dragon' describes a Human NPC Merchant (not an item) on the mountain near the Shrouded Glade Cooking Table, introduced August 27, 2013, who sells Ninja Job Items.", "source": "https://freerealms.fandom.com/wiki/Hidden_Dragon (rev 33106)"},
  {"claim": "Client text locale:5102393 is tagged as an ability ('ability - Hidden Dragon'), not an item.", "source": "locale:5102393"},
  {"claim": "The wiki's Merchants list includes Hidden Dragon as an NPC merchant, consistent with the NPC reading.", "source": "wiki page 'Merchants'"},
  {"claim": "The NPC's stock (Soke Ninja Shoulderguard, Soke Ninja Hakama, Soke Ninja Cowl, Soke Ninja Wrist Guards, Soke Ninja Tabi Boots, Soke Ninja Gi, Ninja's Flair Shard of Prosperity, Ninja's Power Shard of Vitality V, Ninja's Necklace of Vitality V, Ninja's Ring of Regeneration V, and five Ninja's Shadow Blade variants) is listed on the wiki page, but no prices are given there and these are separate items, not 'Hidden Dragon'.", "source": "https://freerealms.fandom.com/wiki/Hidden_Dragon"}
 ],
 "confidence": 0.9,
 "open": [
  "The evidence pack is for the wrong subject. 'Hidden Dragon' is an NPC merchant (and a ninja ability name), not a purchasable item, so no item sources can be assigned. The job needs the correct item name.",
  "If the intended item is one of the NPC's stock items (e.g., a Soke Ninja piece or a Ninja's Shadow Blade), rerun with that item's own pack. The wiki page gives no prices or per-item sources for them.",
  "Wiki price/currency data, vendor stock, and quest/drop mentions for 'Hidden Dragon' are all empty in the pack. Nothing was found for this name as an item.",
  "Ability vs. item: the client tags locale:5102393 as an ability; if the rebuild needs the ability entry, that is a separate record and not an item source."
 ]}
