<!-- fleet job=citem-infer id=crainbow-bonesaw-139984-v1 status=done turns=5 usd=0.0029 tokens(read,write,in,out)=[22876, 11527, 12, 2527] model=claude-haiku-5-5 -->
# Rainbow Bonesaw

{"item": {"name": "Rainbow Bonesaw", "locale_id": 139984, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, store category 207 (vendor NPC not named in the store data)", "where": null, "price": "1431 coins (member price 1287 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48234 (line 13283); definition id 48234 at repo:prototype/osfr-tools/data/reference/weapons.json:34875"},
  {"type": "other", "detail": "Player-to-player trade only; the wiki says Blue Text weapons are now acquired only through trade", "where": null, "price": null, "currency": null, "source": "wiki: Rainbow Bonesaw; wiki: Category:Blue Text Weapons (retired 14 Dec 2009, currently only acquired through trade)"}
 ],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Client name 'Rainbow Bonesaw' is locale 139984, item class 28, slot 7, model sword_ar_ag_weapon_bonesaw.adr, one definition (48234)", "source": "locale:139984; client definition"},
  {"claim": "Rainbow Bonesaw is a level 13 Medic weapon, a Blue Text weapon, and can only be acquired through trade; listed in Category:Retired Weapons", "source": "wiki: Rainbow Bonesaw"},
  {"claim": "Blue Text weapons were retired on December 14, 2009; their names changed to white font and their membership requirement dropped; they are only acquired through trade", "source": "wiki: Category:Blue Text Weapons"},
  {"claim": "Store data lists item 48234 in category 207 at 1431 coins, member price 1287 coins, sell price 143 coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48234"},
  {"claim": "Wiki lists the Rainbow Bonesaw in the Blue Text weapon list alongside the other Rainbow and Spectrum weapons", "source": "wiki: Blue Text weapon"}
 ],
 "confidence": 0.5,
 "open": [
  "Conflict: the store data shows a 1431-coin sale, but the wiki says the weapon is trade-only and was retired in 2009. The store row may be a pre-retirement sale, or the store snapshot may be newer than the retirement. Needs a dated source for when the coin sale ended.",
  "The vendor NPC for store category 207 is not named in the data; the 'where' field is unknown. Category 207 covers many items, so it is not a single vendor.",
  "Wiki price data for coins is not given in the pack; the 1431 figure comes only from the repo store data.",
  "The 'Triage' effect text on the wiki page reads 'Heals 1357 damage. Deals 4750 damage.' and seems garbled; no effect is used for sourcing.",
  "No images, video, article facts, quest rewards, drops or crafting recipes were found for this item."
 ]}
