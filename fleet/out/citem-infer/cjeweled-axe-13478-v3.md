<!-- fleet job=citem-infer id=cjeweled-axe-13478-v3 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[6982, 9364, 6, 1842] model=claude-haiku-5-5 -->
# Jeweled Axe

{"item": {"name": "Jeweled Axe", "locale_id": 13478, "kind": "weapon"},
 "sources": [
  {"type": "other", "detail": "Player-to-player trade only. Blue Text weapon (Level 5 Warrior, Power 3). Wiki says Blue Text weapons were retired and 'are currently only acquired through trade'. No vendor, quest, drop, event or crafting source is evidenced.", "where": null, "price": null, "currency": null, "source": "wiki Category:Blue Text Weapons (ns14); wiki page Jeweled Axe"}
 ],
 "retired": true, "live": "unsure",
 "evidence": [
  {"claim": "Jeweled Axe is a level 5 Warrior, Power 3 Blue Text weapon in Category:Retired Weapons, and can only be acquired through trade.", "source": "wiki page Jeweled Axe"},
  {"claim": "On December 14, 2009, Blue Text weapons were retired; their names changed to white font, membership requirement was dropped, and they are currently only acquired through trade.", "source": "wiki Category:Blue Text Weapons (ns14); also wiki Blue Text weapon (ns0)"},
  {"claim": "stores.json items 6791, 6792, 6793 (category 207, tint groups 1-3) list purchase 3522 coins, member 3169, sell 352, no_sale false. No vendor or shop name is attached to category 207 in the data, so this is an unresolved lead, not a sourced vendor sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 1838-1840"},
  {"claim": "The 'Ceremonial Jeweled Axe' tooltip, render images and video frames belong to locale 11441 (a different item), so they are not evidence for 13478.", "source": "locale:11441; wiki page Ceremonial Jeweled Axe"}
 ],
 "confidence": 0.5,
 "open": [
  "Coin price lead: stores.json category 207 rows 6791-6793 show 3522 coins (member 3169, sell 352). No vendor is named for category 207 and the wiki says trade-only, so no coin_shop source is listed. Tie category 207 to a vendor before adding one.",
  "Live status unsure: the store rows are live-tagged with no no_sale flag, which conflicts with the retired, trade-only wiki status. Verify against a live client or server store feed.",
  "Lookup for locale 13478 by the locale tool returned no match in this check; the name and id come from the evidence pack's client definition.",
  "The Blue Text wiki says these weapons dropped from certain dungeon bosses, but no specific boss, drop row or quest for 13478 is named, so no drop source is listed.",
  "The other definitions in the 52-definition set (6794-6812 and beyond) were not checked individually for price or tint."
 ]}
