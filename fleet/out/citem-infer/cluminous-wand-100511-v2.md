<!-- fleet job=citem-infer id=cluminous-wand-100511-v2 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[5568, 10489, 6, 1879] model=claude-haiku-5-5 -->
# Luminous Wand

{"item": {"name": "Luminous Wand", "locale_id": 100511, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store row for client definition 48151 (store category 207). The store data names no vendor or NPC, and its source_tags (L1, L2, L4, R2, T633, R1) are not resolved to a location. Sibling rows in the same category carry the same tags.", "where": null, "price": "2204 coins purchase (member price 1983 coins, 10% member discount; sell-back 220 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:13207 (item_id 48151); also repo:prototype/osfr-tools/data/reference/weapons.json:27282 (cost 2204)"},
  {"type": "other", "detail": "Player-to-player trade only. The wiki says the wand can only be acquired through trade. No NPC, quest, drop or event source is documented.", "where": null, "price": null, "currency": null, "source": "wiki: Luminous Wand (https://www.freerealms.wiki/wiki/Luminous_Wand)"}
 ],
 "retired": true, "live": "unsure",
 "evidence": [
  {"claim": "Luminous Wand is a level 16 Wizard weapon, Blue Text, acquired only through trade.", "source": "wiki: Luminous Wand"},
  {"claim": "The wiki page carries Category:Retired Weapons. The category is undated, so retirement is not dated.", "source": "wiki: Luminous Wand (Category:Retired Weapons)"},
  {"claim": "Client name for the item is locale 100511 'Luminous Wand'. Sibling Blue Text Luminous weapons (Axe, Bow, Hammer, Shockrod, Shadowblade) sit at locales 100510-100515 and are listed on the wiki Blue Text weapon page.", "source": "locale:100511; locale:100510-100515; wiki: Blue Text weapon"},
  {"claim": "Store row for item 48151 lists purchase 2204 coins, member 1983, sell 220, no_sale false.", "source": "repo:prototype/osfr-tools/data/content/stores.json:13207"},
  {"claim": "Definition 29932 is in weapons.json at cost 2204 but has no store row.", "source": "repo:prototype/osfr-tools/data/reference/weapons.json:27275"}
 ],
 "confidence": 0.4,
 "open": [
  "Conflict: the wiki says trade-only, but stores.json lists definition 48151 in coin category 207 at 2204 coins. The row names no vendor, so the coin price is data-only and unverified against a named shop. Confirm the vendor and whether the listing ever went live before the rebuild sells it.",
  "stores.json row for 48151 has no_sale false, which does not match a withdrawn listing. Retired status rests only on the undated wiki Retired Weapons category. Treat retirement as unconfirmed by a dated source.",
  "Coin price applies to 48151 only. Definition 29932 has no store row, so its availability is unknown.",
  "No quest, drop, event or collection source was found in the pack.",
  "Client description is empty, so no in-game text states the source."
 ]}
