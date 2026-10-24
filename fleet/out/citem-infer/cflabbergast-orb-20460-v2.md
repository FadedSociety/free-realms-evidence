<!-- fleet job=citem-infer id=cflabbergast-orb-20460-v2 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[5912, 8357, 6, 1511] model=claude-haiku-5-5 -->
# Flabbergast Orb

{"item": {"name": "Flabbergast Orb", "locale_id": 20460, "kind": "consumable"},
 "sources": [
  {"type": "prize_wheel", "detail": "Battle Item Mystery Pack: granted by most combat mini-game prize wheels; a landing on the pack yields three battle items. The Orb is listed by the wiki as one of those battle items; the pack's own item list is not in the evidence, so this is wiki-attributed.", "where": "combat dungeon and minigame prize wheels", "price": null, "currency": null, "source": "wiki page 'Flabbergast Orb' (\"is acquired from Battle Item Mystery Packs\"); wiki page 'Battle Item Mystery Pack'; locale:6666; locale:6667"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Flabbergast Orb' with description 'A magical orb that stuns your target.' (live name id)", "source": "locale:20460; wiki image:item_tooltip 'Flabbergast Orb.jpg' (description and tooltip text match)"},
  {"claim": "Tooltip: Required Any Job, Power 1, stuns target for 5 seconds, Resell Value 19 (a resell value, not a store price), You Own 115", "source": "wiki image:item_tooltip 'Flabbergast Orb.jpg'"},
  {"claim": "Wiki: level 1 battle item usable in any job, acquired from Battle Item Mystery Packs", "source": "wiki page 'Flabbergast Orb'"},
  {"claim": "Battle Item Mystery Pack is a prize granted by combat prize wheels and yields three battle items", "source": "wiki page 'Battle Item Mystery Pack'; locale:6667"},
  {"claim": "Client has no coin store price for definition 11017, so no coin vendor sale is evidenced", "source": "client definition, coin_store_prices empty"}
 ],
 "confidence": 0.4,
 "open": [
  "The Mystery Pack source rests on one wiki sentence. The pack's contents list was not found to include the Orb, so per-pack odds and the exact outcome list are unverified.",
  "Nekark chest 'Flabbergast' claim removed: the bare name is ambiguous and the wiki's separate 'Flabbergast Sphere' (sold 50 coins at the Coin Shop) is a different item. Not counted as a source.",
  "Locale 20459 ('(PH)' placeholder) is not used as live evidence. Locale 20456 belongs to the 'Flabbergast Orb 1' sibling; tier relationship to 20460 is unconfirmed. Locale 36520 'Flabbergast Orb IV (PH)' also exists as a placeholder.",
  "Live status is 'unsure': 'You Own: 115' shows the item exists in player inventories, not that it is currently obtainable. No acquisition date or patch source was found, so retired stays null.",
  "Resell value 19 is not a purchase price; no Station Cash or coin price is known."
 ]}
