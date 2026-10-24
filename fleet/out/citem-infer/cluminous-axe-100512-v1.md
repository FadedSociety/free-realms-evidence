<!-- fleet job=citem-infer id=cluminous-axe-100512-v1 status=done turns=10 usd=0.0073 tokens(read,write,in,out)=[170896, 25956, 22, 4668] model=claude-haiku-5-5 -->
# Luminous Axe

{"item": {"name": "Luminous Axe", "locale_id": 100512, "kind": "weapon"},
 "sources": [{"type": "other", "detail": "Player-to-player trade only (wiki: 'can only be acquired through trade'). No vendor, quest, drop or event source is documented.", "where": null, "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Luminous_Axe (rev 39342); refs freerealms-wiki/wikitext/17011-39342-dcc6073b8742.wiki:3"}],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Wiki page: level 16 Warrior weapon, Blue Text weapon, 'can only be acquired through trade'; Sweeping Slash 2609 dmg, Spinning Attack 4732 dmg.", "source": "https://freerealms.fandom.com/wiki/Luminous_Axe; freerealms-wiki/wikitext/17011-39342-dcc6073b8742.wiki:3"},
  {"claim": "Wiki categories include 'Retired Weapons' and 'Blue Text Weapons', so the item is retired per the wiki.", "source": "https://freerealms.fandom.com/wiki/Luminous_Axe (Category:Retired Weapons); freerealms-wiki/harvest/lists/items.json:14930-14935"},
  {"claim": "Client definition: Id 29933, NameId 100512, Type 1, Class 17, Slot 7, MinProfileRank 16, Cost 2204, MemberDiscount 10, model warrior-doublebladed / axe_ar_ag_weapon_warlordsaxe.adr.", "source": "refs Lxzxrus-Free-Realms-Server/src/Resources/ClientItemDefinitions.json:617364-617380"},
  {"claim": "Wiki Blue Text weapon list puts Luminous Axe in the Luminous set at level 16 with Luminous Bow, Hammer, Shockrod, Shadowblade and Wand.", "source": "freerealms-wiki/wikitext/3831-21850-8a08ba4573a2.wiki:44; lookup wiki page 'Blue Text weapon'"},
  {"claim": "Tooltip image shows Value 220, Power Rating 33, Required: Membership, Level 15, Warrior. Value 220 is a resell value, not a store price.", "source": "image:item_tooltip Download.jpg via freerealms-wiki/harvest/lists/items.json:14908-14920"}
 ],
 "confidence": 0.5,
 "open": [
  "The pack's coin_store_prices [2204] is not a store price. Client definition 29933 has 'Cost': 2204, which is the definition's Cost field. stores.json item_id 2204 is a different item (Doggy Island Lei, Id 2204, Cost 10, Lxzxrus ClientItemDefinitions.json:42076-42090). The repo stores.json has no entry for item 29933 or 48142, so no coin vendor sale is evidenced. Coin store sources are therefore omitted.",
  "Level conflict: wiki says level 16 and the definition's MinProfileRank is 16, but the tooltip says Level 15 and Membership. The tooltip may come from a different variant or a later patch. Left unresolved; the membership requirement is not confirmed by another source.",
  "Definition 48142 (the pack's second definition id) was not found in the Lxzxrus definitions file (no 'Id': 48142 match). The second variant and its source are unverified.",
  "The 'trade' source is player-to-player trading, not a vendor. The wiki gives no trader NPC, price, or date, and no article or video confirms how the trade worked. The 'Retired' category means it is no longer obtainable; the date of retirement is not given.",
  "The pack's 'Graawwrrrr!' and 'Bogwart' lines are unrelated neighbours in the locale table, not part of the Luminous set text. No promotion or code evidence was found.",
  "No vendor stock, quest reward, drop, event, or prize-wheel source was found in the pack or the repo search. Those source types were not searched further."
 ]}
