<!-- fleet job=citem-infer id=cbubbleburst-wand-46854-v1 status=done turns=4 usd=0.0028 tokens(read,write,in,out)=[18460, 10396, 10, 2667] model=claude-haiku-5-5 -->
# Bubbleburst Wand

{"item": {"name": "Bubbleburst Wand", "locale_id": 46854, "kind": "weapon"},
 "sources": [{"type": "other", "detail": "Player-to-player trade only. Blue Text weapon; no vendor, quest, drop or event source is documented. The first-pass 'event' guess is not supported by any evidence.", "where": null, "price": null, "currency": null, "source": "wiki: Category:Blue Text Weapons (\"They are currently only acquired through trade\"); wiki: Blue Text weapon list entry '[Bubbleburst] Wand'; wiki: Bubbleburst Bow / Scalpel / Kendama Hammer / Blade pages (sibling Bubbleburst weapons: 'can only be acquired through trade')"}],
 "retired": true, "live": "unsure",
 "evidence": [{"claim": "Client item 'Bubbleburst Wand' is locale:46854, item class 10, equip slot 7, model wand_ar_ag_weapon_bolt.adr, definition id 22104, single definition.", "source": "client definition (locale:46854; definition_ids 22104)"},
  {"claim": "The Bubbleburst Wand appears in the wiki's Blue Text weapon list as '[Bubbleburst] Wand', alongside the other Bubbleburst weapons.", "source": "wiki page: Blue Text weapon"},
  {"claim": "Blue Text weapons were retired on December 14, 2009; their names changed to white font, membership requirement dropped; they are currently only acquired through trade.", "source": "wiki: Category:Blue Text Weapons"},
  {"claim": "Sibling Bubbleburst weapons (Bow, Scalpel, Kendama Hammer, Blade) are each documented as Blue Text weapons that can only be acquired through trade.", "source": "wiki: Bubbleburst Bow; Bubbleburst Scalpel; Bubbleburst Kendama Hammer; Bubbleburst Blade"},
  {"claim": "Client cluster locale:46850-46860 (Juiced/Bubbleburst/Nature's set) shares naming with Bubbleburst weapons; no coin store price exists for the wand.", "source": "client_cluster in pack; repo:data/reference/weapons.json (Bubbleburst entries, lines 9614-9761)"}],
 "confidence": 0.6,
 "open": ["No wiki page exists for the Bubbleburst Wand itself; its acquisition is inferred from the Blue Text category and sibling Bubbleburst pages, not a direct source.",
  "Wiki list format for the wand ('[Bubbleburst] [Wand] 1 5' in the Blue Text list) does not clearly give level/power; level and power for the wand are unverified (the Blade is level 4, power 3).",
  "The 'live' value is unsure: the item is defined in the client and the wiki says trade is the only way to get it, but no evidence shows whether trades of it still occur on the live game.",
  "No vendor stock, coin store price, quest, drop, or event evidence was found. The jev first-pass 'event' guess is unsupported and was not used.",
  "Pack critique: none supplied. The 'Juiced' and 'Nature's' cluster items were not individually researched."]}
