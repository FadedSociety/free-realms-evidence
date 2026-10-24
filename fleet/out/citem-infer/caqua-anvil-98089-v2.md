<!-- fleet job=citem-infer id=caqua-anvil-98089-v2 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[5607, 9239, 6, 1686] model=claude-haiku-5-5 -->
# Aqua Anvil

{"item": {"name": "Aqua Anvil", "locale_id": 98089, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store listing, coin store category 207 (shared category; no weapon or Blue Text grouping evidenced). Vendor/NPC not named in any source.", "where": "coin store (vendor unknown)", "price": "1431 coins purchase; 1287 coins member price (10% member discount); 143 coins sell-back", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 37528 (line 12272). Single-source, unverified against live sources. FreeRealms-Legacy CoinStoreItems.json Id 37528 (line 55187) shows category 207 only, no price."}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item definition: name 'Aqua Anvil', locale 98089, definition 37528, slot 7, class 5, model hammer_ar_ag_weapon_anvil.adr, one variant", "source": "locale:98089; repo ClientItemDefinitions (Id 37528)"},
  {"claim": "Coin store row for item 37528: purchase 1431, member 1287 (10%), sell 143, category 207, no_sale false", "source": "repo:prototype/osfr-tools/data/content/stores.json line 12272"},
  {"claim": "Level 12 Brawler Blue Text weapon, Power 5; Glancing Blow 2372 damage, Leg Sweep 8302 damage; tooltip Resell Value 143", "source": "wiki page 'Aqua Anvil'; image:item_tooltip 'Aqua Anvil item.jpg'"},
  {"claim": "Wiki lists it in Category:Retired Weapons and Category:Blue Text Weapons; no retirement date given", "source": "wiki page 'Aqua Anvil' categories"},
  {"claim": "Wiki text says the weapon 'can only be acquired through trade'. This conflicts with the coin store row and is not reconciled.", "source": "wiki page 'Aqua Anvil' (ns0) body text"}
 ],
 "confidence": 0.4,
 "open": [
  "Coin vendor/NPC or Coin Shop sub-category for item 37528 is not named in any source in the pack.",
  "Conflict: wiki says 'only acquired through trade' (player-to-player) while stores.json lists a 1431-coin purchase price. Not resolved; the store row may be data-only or from a period the wiki does not cover.",
  "Retirement: only evidence is the wiki 'Retired Weapons' category. No retirement date or last-sale date in any source, so retired is left null.",
  "No wiki or live price exists; the 1431-coin price rests only on the repo store data.",
  "Legacy CoinStoreItems.json line 55187 carries category 207 without a price, so it is not evidence for the price."
 ],
 "critiques_addressed": "Evidence critique applied: price cited only to stores.json line 12272; Blue Text placement claim dropped; wiki trade-only claim recorded as a conflict, not a source; retired left unsettled, live kept as unsure."}
