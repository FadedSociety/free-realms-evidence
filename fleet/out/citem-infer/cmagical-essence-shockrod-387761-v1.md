<!-- fleet job=citem-infer id=cmagical-essence-shockrod-387761-v1 status=done turns=4 usd=0.0036 tokens(read,write,in,out)=[26041, 15364, 10, 2928] model=claude-haiku-5-5 -->
# Magical Essence Shockrod

{"item": {"name": "Magical Essence Shockrod", "locale_id": 387761, "kind": "weapon"},
 "sources": [
  {"type": "collection", "detail": "Completing the Medic Magical Essences collection (four Shock Rod Essence items: Earth, Fire, Water, Wind; the Shock Rod essences are clicked from Medic Materials crates in dungeons while in the Medic job)", "where": null, "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Magical_Essence_Shockrod; https://freerealms.fandom.com/wiki/Medic_Magical_Essences; repo:prototype/osfr-tools/data/content/collections.json:3418 (Medic Magical Essences, 4 entries)"},
  {"type": "coin_shop", "detail": "Coin store listing for client item 55816 (store category 207), purchase price 2363 coins, member price 2126 coins, sell price 236 coins. Vendor/location not identified in our store data.", "where": null, "price": "2363 coins (member price 2126 coins)", "currency": "coins", "source": "repo:data/content/stores.json item 55816 (line 13978); repo:prototype/osfr-tools/data/reference/weapons.json:27684-27688"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Magical Essence Shockrod is a level 20 Medic weapon, Power 5, Cannot Trade, acquired by completing the collection Medic Magical Essences", "source": "https://freerealms.fandom.com/wiki/Magical_Essence_Shockrod"},
  {"claim": "Client name string for the item is locale 387761 'Magical Essence Shockrod'; definition id 55816, slot 7, class 20, model club_ar_ag_weapon_shockrod.adr", "source": "locale:387761"},
  {"claim": "Wiki item tooltip shows Resell Value 236, Required Level 20 Medic, abilities Incision and Triage", "source": "image:item_tooltip Magical Essence Shockrod Axe item.jpg"},
  {"claim": "Medic Magical Essences collection is composed of four Shock Rod Essence items and lists this weapon as its reward (wiki Medic category lists Magical Essence Shockrod at Level 20)", "source": "https://freerealms.fandom.com/wiki/Medic_Magical_Essences; https://freerealms.fandom.com/wiki/Medic"},
  {"claim": "Store data lists definition 55816 at 2363 coins, with sell price 236 matching the wiki resell value", "source": "repo:data/content/stores.json item 55816"},
  {"claim": "Sibling essence weapons in the same client cluster (Bow, Shadowblade, Warlords Axe, Crystal Hammer, Ornate Wand) all carry the same 2363 coin store price and the same collection-reward pattern", "source": "repo:prototype/osfr-tools/data/reference/weapons.json:27457-27737"}
 ],
 "confidence": 0.6,
 "open": [
  "Conflict: the wiki says the weapon is a collection reward only (no vendor), yet our store data lists it at 2363 coins (member 2126). Which coin vendor/shop row this is, and whether it was sold in-game, is unverified. Reported as coin_shop from the store row only.",
  "Wiki gives no price or vendor for the coin listing; the store category 207 name is not resolved in our data.",
  "Collection requirements (how many essences, which crate drops) are not spelled out in the wiki; the collection page lists four essence items only.",
  "Retirement status not stated by any source; live is inferred from the existing wiki page, the store row, and the client definition."
 ]}
