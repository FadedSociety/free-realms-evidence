<!-- fleet job=item-infer id=ininja-s-scythe-of-solar-flare-v4 status=done turns=2 usd=0.0030 tokens(read,write,in,out)=[7666, 10427, 6, 3223] model=claude-haiku-5-5 -->
# Ninja's Scythe of Solar Flare

{"item": {"name": "Ninja's Scythe of Solar Flare", "locale_id": 131985, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop sale of the level 8 Ninja weapon (Power 3). Price comes only from the wiki coins field and the 'Coin Shop' / 'Coin Shop Weapons' categories; not confirmed by a captured in-game quote.", "where": "Coin Shop", "price": "1055 coins", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Ninja's_Scythe_of_Solar_Flare (rev 32887, coins field; categories Coin Shop, Coin Shop Weapons)"},
  {"type": "vendor", "detail": "Dizzy Toad (Pixie NPC), Nusumi Ninja job set stock ('Scythes of Solar Flare'). Stock-only evidence: the wiki 'Sells' list is a 2013-10-03 snapshot noting 'Added 27 Aug 2013'. The 1055 figure is a stores.json reference price, not a captured NPC quote, so the NPC's actual price is unknown. May be the same 1055-coin sale as the Coin Shop row.", "where": "Snowhill (snowhill.json); exact zone not verified", "price": null, "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/vendors.json:33063 (stock description), :33173-:33178 (item_id 75101, name_id 131985, reference purchase 1055 / member 949 / sell 527); repo:prototype/osfr-tools/data/content/npcs/snowhill.json:11678; https://freerealms.fandom.com/wiki/Dizzy_Toad (Sells, rev 2013-10-03)"},
  {"type": "prize_wheel", "detail": "Prize wheel, Ninja job slot, at Bone Bog Cemetery. Wheel cost and odds not in evidence.", "where": "Bone Bog Cemetery", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Dungeons/Bone Bog Cemetery.md:82; repo:prototype/osfr-tools/data/content/dungeons/bone_bog_cemetery.json:1697; https://freerealms.fandom.com/wiki/Ninja's_Scythe_of_Solar_Flare (category Prize Wheel Weapons)"},
  {"type": "prize_wheel", "detail": "Prize wheel at Thugawug Bandits!. Wheel cost and odds not in evidence.", "where": "Thugawug Bandits!", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Ninja's_Scythe_of_Solar_Flare (page text; category Prize Wheel Weapons)"},
  {"type": "prize_wheel", "detail": "Prize wheel at Venemous Frogs!. Wheel cost and odds not in evidence.", "where": "Venemous Frogs!", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Ninja's_Scythe_of_Solar_Flare (page text; category Prize Wheel Weapons)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name matches client string id 131985", "source": "locale:131985"},
  {"claim": "Level 8 Ninja weapon, Power 3; Ashen Strike 853 dmg, Flaming Uppercut 2716 dmg", "source": "https://freerealms.fandom.com/wiki/Ninja's_Scythe_of_Solar_Flare (page text and item_tooltip image)"},
  {"claim": "Wiki lists a Coin Shop coin price of 1055 (coins field only; page body price blank)", "source": "https://freerealms.fandom.com/wiki/Ninja's_Scythe_of_Solar_Flare (rev 32887)"},
  {"claim": "Tooltip Resell Value is 105 (captured sell-back). The stores.json sell 527 is a reference value and conflicts with it; 527 is not used.", "source": "https://freerealms.fandom.com/wiki/Ninja's_Scythe_of_Solar_Flare (item_tooltip image)"},
  {"claim": "Dizzy Toad stock row maps item 75101 to name_id 131985 'Ninja's Scythe of Solar Flare'; price basis is stores.json reference, not a captured NPC quote", "source": "repo:prototype/osfr-tools/data/content/vendors.json:33063, :33173-:33180"},
  {"claim": "Bone Bog Cemetery Ninja prize-wheel row includes this scythe", "source": "repo:notes/Build Guides/Content/Dungeons/Bone Bog Cemetery.md:82; repo:prototype/osfr-tools/data/content/dungeons/bone_bog_cemetery.json:1697"},
  {"claim": "Thugawug Bandits! and Venemous Frogs! prize wheels include this scythe", "source": "https://freerealms.fandom.com/wiki/Ninja's_Scythe_of_Solar_Flare (page text)"},
  {"claim": "Ninja's Jagged Scythe of Solar Flare (locale:131991) and Ninja's Shadow Blade of Solar Flare are different items and are not used", "source": "locale:131991; repo:prototype/osfr-tools/data/content/vendors.json:6410, :9627"}
 ],
 "confidence": 0.6,
 "open": [
  "Live status unconfirmed. All vendor and Coin Shop evidence is from 2013-era wiki snapshots; no current client vendor table or live listing confirms it is still sold. Retired left null.",
  "Coin Shop 1055 coins rests on the undated wiki coins field only; no captured in-game quote.",
  "Dizzy Toad price is unknown. The 1055/949/527 values are stores.json reference prices, not captured NPC quotes. Whether the Dizzy Toad and Coin Shop entries are the same 1055-coin sale is unresolved; they may be one source listed twice.",
  "Dizzy Toad location 'Perry's Pastures, south of Snowhill' from the earlier draft is not supported by the cited evidence and was removed. Only snowhill.json:11678 links the NPC to Snowhill; exact zone unverified.",
  "Prize wheels (Bone Bog Cemetery, Thugawug Bandits!, Venemous Frogs!): wheel cost and odds are not in evidence. The Bone Bog row is the Ninja prize-wheel row, not a mystery pack.",
  "Resell value conflict: tooltip 105 vs stores.json 527. Tooltip value is reported; 527 is not confirmed.",
  "No Station Cash marketplace source. The page has 'Marketplace Items' but no 'SC Marketplace' category and no station_cash price.",
  "Wiki Dizzy Toad page and the wiki/articles lookups for this item returned FTS5 syntax errors on the apostrophe, so the wiki Sells list was not re-verified in this pass; the repo vendor row was verified directly."
 ]}
