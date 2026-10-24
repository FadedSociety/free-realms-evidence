<!-- fleet job=citem-infer id=cstorm-charmed-wand-19526-v1 status=done turns=7 usd=0.0040 tokens(read,write,in,out)=[54037, 13983, 16, 3338] model=claude-haiku-5-5 -->
# Storm Charmed Wand

{"item": {"name": "Storm Charmed Wand", "locale_id": 19526, "kind": "weapon"},
 "sources": [
  {"type": "drop", "detail": "Dungeon boss enemies (general Green Text weapon source; the specific boss for this wand is not named in any source)", "where": "dungeons", "price": null, "currency": null, "source": "wiki Category:Green Text Weapons (\"acquired in dungeons where they were dropped at random by certain 'boss' enemies\"); wiki Green Text weapon page"},
  {"type": "crafting", "detail": "Some Green Text weapons were made by Blacksmiths; the wiki does not say this wand was one of them", "where": null, "price": null, "currency": null, "source": "wiki Category:Green Text Weapons (\"some were (and still are) made by Blacksmiths\") - unconfirmed for this item"},
  {"type": "other", "detail": "Player-to-player trade only (the wiki's acquisition line for this wand)", "where": null, "price": null, "currency": null, "source": "wiki Storm Charmed Wand page: \"can only be acquired through trade\""}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Storm Charmed Wand is a level 8 Wizard weapon, Green Text, Power 4, acquired only through trade", "source": "wiki Storm Charmed Wand"},
  {"claim": "Wiki category lists Retired Weapons and Green Text Weapons", "source": "wiki Storm Charmed Wand categories"},
  {"claim": "Green Text weapons were retired as dungeon drops on December 14, 2009", "source": "wiki Category:Green Text Weapons (text truncated after 'On December 14, 2009, Green Text weapons were retired as dungeon drops')"},
  {"claim": "Client name locale 19526 = 'Storm Charmed Wand', 10 client definitions (30425-30429, 38651, 38653, 38655, 38657, 38661), slot 7, class 10, model wand_ar_ag_weapon_bone.adr", "source": "locale:19526; repo:prototype/osfr-tools/data/reference/weapons.json:43063-43134"},
  {"claim": "Sibling Green Text wands/bows (Solar Charmed Wand, Storm Shot Bow, Trick Shot Bow, etc.) carry the same trade-only, retired wording", "source": "wiki Green Text weapon page; wiki Storm Shot Bow; wiki Trick Shot Bow"}
 ],
 "confidence": 0.5,
 "open": [
  "The pack's coin_store_prices [928, 1069] are NOT store prices. In weapons.json they are the 'cost' field on each client_items entry (1069 for most variants, 928 for 38655 and 30402). stores.json has no entry for item 928 and its entry for item 1069 is an unrelated item at 9453 coins. So there is no coin vendor sale evidence for this wand, and the pack's 'vendor' guess is unsupported. The meaning of the 'cost' field is unknown.",
  "No vendor stock, quest reward, or event source found for this item. The wiki 'trade' line and the Green Text dungeon-drop category are the only sources.",
  "The specific boss or dungeon that dropped this wand is not identified.",
  "Retirement date for this specific wand is not given; the category gives December 14, 2009 for Green Text weapons as dungeon drops. Whether trade-only is a separate later state is unclear.",
  "The wiki's Green Text category text was truncated in lookup; the full article may name the Blacksmith recipes and retirement details."
 ]}
