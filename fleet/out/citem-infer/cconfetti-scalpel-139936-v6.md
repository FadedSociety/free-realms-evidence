<!-- fleet job=citem-infer id=cconfetti-scalpel-139936-v6 status=done turns=3 usd=0.0042 tokens(read,write,in,out)=[19682, 20696, 8, 2825] model=claude-haiku-5-5 -->
# Confetti Scalpel

{"item": {"name": "Confetti Scalpel", "locale_id": 139936, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store price tier, category 207, definition 48186. No named vendor, NPC or dated sale in the data; the wiki says this item can only be acquired through trade. Listed only because the client carries a coin store price for it; unconfirmed.", "where": null, "price": "811 coins (member price 729 coins, 10% member discount; sell price 81 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:13235 (item 48186, category 207, purchase 811, member 729, sell 81, no_sale false); client coin_store_prices [811] for definition 48186; wiki page 'Confetti Scalpel' says 'can only be acquired through trade' (conflict, see open)"},
  {"type": "other", "detail": "Player-to-player trade only (Blue Text weapon). No trade price recorded.", "where": null, "price": null, "currency": null, "source": "wiki page 'Confetti Scalpel' ('can only be acquired through trade'); wiki Category:Blue Text Weapons ('They are currently only acquired through trade')"}
 ],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Client name is locale 139936 'Confetti Scalpel' (ucdt/ugdt string entries in the client locale file); it sits in an 11-item cluster of locale 139931-139941 (Gemstone, Confetti and Party weapons). No description.", "source": "locale:139936; client_cluster in pack; client en_us_data.dat string entries"},
  {"claim": "Wiki: level 5 Medic weapon, Blue Text weapon, 'can only be acquired through trade'; categories include Retired Weapons and Blue Text Weapons.", "source": "wiki page 'Confetti Scalpel'"},
  {"claim": "Wiki Category:Blue Text Weapons: Blue Text weapons were members-only weapons acquired in dungeons, dropped at random by certain boss enemies; on December 14 (year truncated in the retrieved text; 2009 per the pack's quote of the category page) they were retired, names changed to white font, membership requirement dropped, and they are currently only acquired through trade.", "source": "wiki Category:Blue Text Weapons (lookup returned 'On December 14..'; full sentence quoted in pack)"},
  {"claim": "Store row exists for item 48186: category 207, purchase 811, member 729 (10%), sell 81, no_sale false. Rows 48172-48196 share these values (checked 48172-48196 directly); rows 48168-48171 are 640.", "source": "repo:prototype/osfr-tools/data/content/stores.json:13222-13245"},
  {"claim": "Category-level acquisition (boss drops in dungeons) applies to Blue Text weapons in general, but no item-specific drop source for Confetti Scalpel was found.", "source": "wiki Category:Blue Text Weapons"}
 ],
 "confidence": 0.4,
 "open": [
  "Conflict: the client coin price [811] and stores.json row 48186 suggest a coin store listing, but the wiki says the item is trade-only and retired. No named vendor, shop page or dated sale for category 207 was found. The coin_shop entry is kept as unconfirmed; resolve with a named vendor or dated sale, or remove it.",
  "Blue Text category says these weapons dropped at random from dungeon boss enemies while members-only. This is a category-level statement, not an item-specific drop record; no boss name was found for this item, so no drop source is listed.",
  "Retirement year: the retrieved category text is truncated at 'On December 14'; the 2009 year comes from the pack's quote and was not re-verified in full.",
  "Trade price unknown: no trade partner, price or market record found.",
  "No quest, event, prize-wheel or crafting source found.",
  "Live 'no' rests on the wiki retirement and trade-only text."
 ]}
