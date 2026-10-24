<!-- fleet job=citem-infer id=csmokey-hammer-72353-v1 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[3861, 7541, 6, 1978] model=claude-haiku-5-5 -->
# Smokey Hammer

{"item": {"name": "Smokey Hammer", "locale_id": 72353, "kind": "weapon"},
 "sources": [{"type": "vendor", "detail": "Coin store sale of Smokey Hammer (definition 48123), store category 207; the vendor NPC is not named in our store data", "where": null, "price": "2204 coins (member price 1983 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48123 (line 13179)"},
  {"type": "other", "detail": "Player-to-player trade only, per the wiki page; not a vendor, quest or drop source", "where": null, "price": null, "currency": null, "source": "wiki: Smokey Hammer (\"can only be acquired through trade\")"}],
 "retired": true, "live": "no",
 "evidence": [{"claim": "Smokey Hammer is a level 16 Brawler weapon, Blue Text weapon, power 5, listed in Retired Weapons", "source": "wiki: Smokey Hammer (categories Retired Weapons, Blue Text Weapons, Level 16 Weapons)"},
  {"claim": "Name is locale 72353 'Smokey Hammer'; locale 72359 gives its line 'Wearable by a level 5 or higher Brawler'", "source": "locale:72353; locale:72359"},
  {"claim": "Store row for item 48123 sells at 2204 coins, member 1983, sell-back 220, same as other category 207 items", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48123"},
  {"claim": "Sister Smokey weapons (Bow, Axe, Wand, Shockrod, Shadowblade) share the same Blue Text 'Smokey' set", "source": "locale:72350-72355; wiki: Blue Text weapon"}],
 "confidence": 0.5,
 "open": ["The wiki says this weapon can only be obtained through trade, which conflicts with the coin store row for 48123. The store row is the only vendor evidence; I could not confirm the store NPC or whether category 207 was on sale or retired.",
  "The client has two definitions (23023 and 48123); only 48123 has a store price. Which definition the 2204-coin store row belongs to needs checking against the client.",
  "The 2204 price is shared by many category 207 items, so the price alone does not prove this item was sold; it is treated as a vendor sale only because the store row names item 48123 directly.",
  "No wiki price, sale date or retirement date was found for the coin sale; the retired flag comes only from the wiki category 'Retired Weapons'.",
  "The description field is empty and the Jev first-pass 'live: yes' is contradicted by the wiki's Retired category; treated as not live."]}
