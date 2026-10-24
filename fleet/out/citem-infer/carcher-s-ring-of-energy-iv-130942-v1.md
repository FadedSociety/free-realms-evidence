<!-- fleet job=citem-infer id=carcher-s-ring-of-energy-iv-130942-v1 status=done turns=5 usd=0.0034 tokens(read,write,in,out)=[29751, 12720, 12, 3009] model=claude-haiku-5-5 -->
# Archer's Ring of Energy IV

{"item": {"name": "Archer's Ring of Energy IV", "locale_id": 130942, "kind": "clothing"},
 "sources": [
  {"type": "prize_wheel", "detail": "Archer Prize Wheel (listed as a wheel reward on the zone page; Archer-class ring of energy IV)", "where": "Frostfang Caverns", "price": null, "currency": null, "source": "wiki page: Frostfang Caverns (Archer Prize Wheel list containing \"Archer's Ring of Energy IV\"); the wheel spin cost shown on that page is ambiguous in the extract, so no price is attributed"},
  {"type": "prize_wheel", "detail": "Archer Prize Wheel (same listing)", "where": "Treeleaf's Retreat", "price": null, "currency": null, "source": "wiki page: Treeleaf's Retreat (Archer Prize Wheel list containing \"Archer's Ring of Energy IV\")"},
  {"type": "coin_shop", "detail": "Coin store listing for definition 75198 (sells to everyone at 1504 coins; members 1353 coins after 10% discount; resell 150 coins)", "where": "Coin Shop", "price": "1504 coins (Members: 1353 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:17304 (item_id 75198, category 108)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 75198 is named \"Archer's Ring of Energy IV\" (locale 130942), one variant, slot 8, class 16", "source": "locale:130942; client definition supplied in pack"},
  {"claim": "Archer's Ring of Energy IV is listed in the Archer Prize Wheel on the Frostfang Caverns and Treeleaf's Retreat wiki pages", "source": "wiki pages: Frostfang Caverns; Treeleaf's Retreat"},
  {"claim": "Sibling rings (Energy I, Regeneration I/III) are documented on wiki as Coin Shop items at 10% member discount; no wiki page confirms Coin Shop sale for Energy IV itself", "source": "wiki pages: Archer's Ring of Energy I; Archer's Ring of Regeneration III"},
  {"claim": "Store data prices Energy IV at 1504 coins, but its price provenance is 'reconstructed' from legacy reference costs with no captured retail NPC quote", "source": "repo:prototype/osfr-tools/data/content/stores.json:17304 price_provenance"},
  {"claim": "Sibling Brawler's Ring of Energy IV is on wiki as a Coin Shop item (level 12)", "source": "wiki page: Brawler's Ring of Energy IV"}
 ],
 "confidence": 0.5,
 "open": [
  "No wiki page for Archer's Ring of Energy IV itself; sources come from zone-page prize wheel lists.",
  "Coin Shop price 1504 is a reconstructed value from legacy reference data, not a captured retail quote; the wiki Coin Shop price for Energy IV was not found, so treat 1504 as unverified.",
  "Whether the Archer Prize Wheel listing is the current or a historical wheel is not stated; retired status unknown.",
  "Wheel spin cost on Frostfang Caverns / Treeleaf's Retreat pages is not clearly tied to this item in the extract.",
  "Level requirement for Energy IV not confirmed (siblings: Energy I level 1; Brawler Energy IV level 12).",
  "Jev's first-pass tag said vendor; the vendor claim is not supported by the pack (no vendor stock listed), only the store price entry."
 ]}
