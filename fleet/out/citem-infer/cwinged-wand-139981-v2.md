<!-- fleet job=citem-infer id=cwinged-wand-139981-v2 status=done turns=3 usd=0.0027 tokens(read,write,in,out)=[14860, 10870, 8, 2416] model=claude-haiku-5-5 -->
# Winged Wand

{"item": {"name": "Winged Wand", "locale_id": 139981, "kind": "weapon"},
 "sources": [
  {"type": "drop", "detail": "Original acquisition, category-level only: Blue Text weapons were members-only weapons dropped at random by certain 'boss' enemies in dungeons. The specific dungeon and boss for Winged Wand are not named in any source.", "where": "dungeons (unnamed)", "price": null, "currency": null, "source": "wiki: Category:Blue Text Weapons (page text: 'acquired in dungeons where they were dropped at random by certain \"boss\" enemies'); wiki: Blue Text weapon page"},
  {"type": "other", "detail": "Post-retirement: no game source. Blue Text weapons were retired on December 14, 2009 and are only acquired through player trade (trade is not a schema source type; no trade price or volume evidence found).", "where": null, "price": null, "currency": null, "source": "wiki: Category:Blue Text Weapons ('They are currently only acquired through trade'); wiki: Winged Bow page (same)"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Client item 'Winged Wand', locale 139981, definition 48231, weapon slot 7, class 10, model wand_ar_ag_weapon_bone.adr", "source": "locale:139981; client definition in pack"},
  {"claim": "Winged Wand is in the Winged set of Blue Text weapons (Winged Bow, Anvil, Bonesaw, Scythe, Hammer, Wand); the set sits beside the Rainbow set in client text", "source": "wiki: Blue Text weapon page (list includes [Winged] [Wand]); locale:139976 to locale:139981"},
  {"claim": "Blue Text weapons were members-only weapons dropped at random by certain boss enemies in dungeons", "source": "wiki: Category:Blue Text Weapons"},
  {"claim": "On December 14, 2009 Blue Text weapons were retired; names changed to white font, membership requirement dropped; now only acquired through trade", "source": "wiki: Category:Blue Text Weapons; wiki: Blue Text weapon page"},
  {"claim": "stores.json row for item 48231 shows 1431 coins purchase, 1287 member, 143 sell, but the identical row repeats for neighbouring items 48227 to 48235 and beyond, and header tag R118 says it is a Legacy reference value, not a captured retail NPC price. Not used as a vendor source.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 13276-13284; header line 36 (R118)"}
 ],
 "confidence": 0.5,
 "open": [
  "No vendor source is recorded. The 1431/1287 coin price is a bulk category default (category 207) from the Legacy reference data, with no NPC, zone or retail sighting. Treat as an unverified reference price only, and do not wire a coin vendor sale from it. Category 207's name is not defined in the pack.",
  "The specific dungeon and boss that dropped the Winged Wand are not named; the drop source is category-level only (wiki: Category:Blue Text Weapons).",
  "No wiki page exists for Winged Wand itself; sourcing relies on the Blue Text category and sibling Winged pages.",
  "live is 'no' because the wiki says retirement on 2009-12-14 and trade-only since. The previous answer said 'unsure'; the wiki supports 'no' for any game acquisition path, but trade is not a schema type and no trade evidence was found.",
  "Rainbow Wand (139987) is referenced in the pack's previous answer; not verified here."
 ]}
