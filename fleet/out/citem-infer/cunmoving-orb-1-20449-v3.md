<!-- fleet job=citem-infer id=cunmoving-orb-1-20449-v3 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[7088, 8992, 6, 1946] model=claude-haiku-5-5 -->
# Unmoving Orb 1

{"item": {"name": "Unmoving Orb 1", "locale_id": 20449, "kind": "consumable"},
 "sources": [
  {"type": "other", "detail": "Battle Item Mystery Pack. Wiki page 'Unmoving Orb' says the item is a level 1 battle item usable in any job and 'is acquired from Battle Item Mystery Packs'. The page is titled 'Unmoving Orb' (locale 20453), not 'Unmoving Orb 1' (20449). Which wheels award the pack, and the pack's contents, were not verified.", "where": null, "price": null, "currency": null, "source": "wiki page 'Unmoving Orb' (ns0); wiki image:item_tooltip 'Unmoving Orb.jpg'"},
  {"type": "quest_reward", "detail": "Quest 'Cook-off Catastrophe' (Teaspoon Tarisa), quest run reward at New Goal 'Return to Teaspoon Tarisa': 'You receive 3 Unmoving Orbs'. Plural name matches locale 20453 'Unmoving Orb'; the reward item id is not confirmed as 20449.", "where": "Seaside (Teaspoon Tarisa), Prince of Low Tide run", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/dungeons/prince_of_low_tide.json:602; notes/Build Guides/Content/Dungeons/Prince of Low Tide.md:57; video 506rO_mhaSs/00152"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Unmoving Orb 1' is locale 20449; its description is locale 20450 'A magical orb that roots your target.'", "source": "locale:20449, locale:20450"},
  {"claim": "Locale 20453 is the plain name 'Unmoving Orb' and carries the same description; the wiki page and tooltip are titled 'Unmoving Orb'", "source": "locale:20453; wiki page 'Unmoving Orb'; wiki image Unmoving Orb.jpg"},
  {"claim": "Wiki tooltip: Resell Value 19, Required Any Job, Power 1, roots target 10 seconds. Resell value is not a sale price. No coin or Station Cash price is listed.", "source": "wiki image:item_tooltip Unmoving Orb.jpg"},
  {"claim": "Client definition 11012 has empty coin_store_prices, so no coin vendor sale is evidenced", "source": "client definition in pack"},
  {"claim": "Wiki 'Unmoving Sphere' sells at the Coin Shop for 50 coins; this is a different item and does not apply here", "source": "wiki page 'Unmoving Sphere'"}
 ],
 "confidence": 0.35,
 "open": [
  "ID mismatch: every wiki and quest source names 'Unmoving Orb' (locale 20453). Nothing in the evidence links 20449 'Unmoving Orb 1' to those sources beyond the shared description text. The sources above are for the 'Unmoving Orb' name and are attached to 20449 only provisionally. Confirm whether 20449 and 20453 are the same item or separate builds before wiring.",
  "The Prince of Low Tide reward id is unconfirmed; the plural name points to 20453.",
  "Battle Item Mystery Pack: prize wheels that award the pack and its contents (3 items claimed in the earlier pack) are not verified. The wiki line says only 'acquired from Battle Item Mystery Packs'.",
  "No coin vendor, Station Cash or Coin Shop price found. The wiki gives only Resell Value 19.",
  "Current live status is unconfirmed. The wiki 'You Own: 56' is a snapshot. Retired status is not documented."
 ]}
