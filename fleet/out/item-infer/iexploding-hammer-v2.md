<!-- fleet job=item-infer id=iexploding-hammer-v2 status=done turns=3 usd=0.0032 tokens(read,write,in,out)=[17572, 12591, 8, 2942] model=claude-haiku-5-5 -->
# Exploding Hammer

{"item": {"name": "Exploding Hammer", "locale_id": 31649, "kind": "weapon"},
 "sources": [
  {"type": "marketplace", "detail": "New School Exploding Hammer (Level 1 Brawler, power 5), sold on the Station Cash Marketplace; cannot sell or trade", "where": "SC Marketplace", "price": null, "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Exploding_Hammer (wiki text: 'acquired from the Station Cash Marketplace'; categories SC Marketplace, SC Marketplace Weapons, Retired Weapons, Unobtainable Weapons). Price not shown in the wiki text; see open."},
  {"type": "marketplace", "detail": "Old School Exploding Hammer (Level 1 Brawler, Glancing Blow / Leg Sweep), previously sold on the Station Cash Marketplace; no longer obtainable", "where": "SC Marketplace", "price": null, "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Exploding_Hammer (Old School section: 'previously sold through the Station Cash Marketplace. It can no longer be acquired.')"},
  {"type": "event", "detail": "Treasure Trader Exploding Hammer (Level 16 Brawler, Bash), prize from the Facebook application Free Realms Treasure Trader; no longer obtainable", "where": "Facebook app: Free Realms Treasure Trader (active Sept 8-28, 2010)", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Exploding_Hammer (Treasure Trader section: 'previously acquired from the Facebook application, Free Realms Treasure Trader. It can no longer be acquired.'); https://freerealms.fandom.com/wiki/Treasure_Trader (prize list includes Exploding Hammer; application active September 8 to September 28, 2010); refs freerealms-wiki/harvest/lists/weapons.json:36650"}
 ],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Exploding Hammer is three different Brawler weapons: New School L1 (SC shop), Old School L1 (formerly SC shop), Treasure Trader L16.", "source": "https://freerealms.fandom.com/wiki/Exploding_Hammer"},
  {"claim": "New School version is acquired from the Station Cash Marketplace; cannot sell or trade.", "source": "https://freerealms.fandom.com/wiki/Exploding_Hammer; refs freerealms-wiki/harvest/lists/items.json:19280-19300"},
  {"claim": "Old School version was previously sold on the Station Cash Marketplace and can no longer be acquired.", "source": "https://freerealms.fandom.com/wiki/Exploding_Hammer"},
  {"claim": "Treasure Trader was a Facebook application active September 8 to 28, 2010; its prize list includes Exploding Hammer.", "source": "https://freerealms.fandom.com/wiki/Treasure_Trader (wiki lookup); refs freerealms-wiki/harvest/lists/weapons.json:36650"},
  {"claim": "Treasure Trader Exploding Hammer is a Level 16 Brawler weapon, no longer acquirable.", "source": "https://freerealms.fandom.com/wiki/Exploding_Hammer; tooltip in pack (Level 16, Brawler, Bash)"},
  {"claim": "Name 'Exploding Hammer' is client locale 31649 (also 386328 has the same text; 31649 chosen as canonical).", "source": "locale:31649; locale:386328"},
  {"claim": "The pack's station_cash values 199 (regular) and 179 (Members, 10% off) are NOT in the wiki text (blank) and the harvest record shows station_cash [] and price null for the same page.", "source": "refs freerealms-wiki/harvest/lists/weapons.json:14735-14738; refs freerealms-wiki/harvest/lists/items.json:19294-19297"}
 ],
 "confidence": 0.5,
 "open": [
  "New School SC price is unverified: 199 SC and the Members price 179 SC (10% off) come only from the pack's station_cash field; the wiki text is blank there and the harvest record has null prices. Left as null until a revision shows the number.",
  "Old School SC price is not given anywhere in the pack.",
  "Date the New School and Old School listings left the SC Marketplace is not known; the page marks them Retired and Unobtainable, so live status for the New School listing is treated as no.",
  "Locale 386328 also reads 'Exploding Hammer' with no clear role; 31649 is used as canonical.",
  "Treasure Trader prize-list count mismatch noted by another answer (events) is unresolved; the Exploding Hammer inclusion itself is supported by the Treasure_Trader page text."
 ]}
