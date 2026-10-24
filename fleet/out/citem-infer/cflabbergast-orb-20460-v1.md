<!-- fleet job=citem-infer id=cflabbergast-orb-20460-v1 status=done turns=5 usd=0.0034 tokens(read,write,in,out)=[39464, 12952, 12, 2742] model=claude-haiku-5-5 -->
# Flabbergast Orb

{"item": {"name": "Flabbergast Orb", "locale_id": 20460, "kind": "consumable"},
 "sources": [
  {"type": "prize_wheel", "detail": "Battle Item Mystery Pack (opened from combat prize wheels; a wheel landing on the pack grants three battle items). The wiki says Flabbergast Orb is acquired from Battle Item Mystery Packs; the pack's own contents list is not confirmed in the evidence.", "where": "combat dungeon and minigame prize wheels", "price": null, "currency": null, "source": "wiki page 'Flabbergast Orb' (\"It is acquired from Battle Item Mystery Packs\"); wiki page 'Battle Item Mystery Pack'; locale:6667 'This prize grants the winner 3 battle items!'"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name and description: 'Flabbergast Orb' / 'A magical orb that stuns your target.'", "source": "locale:20460; locale:20459 (description on the placeholder II sibling)"},
  {"claim": "Wiki tooltip shows Required: Any Job, Power 1, Activatable Effect: stuns target for 5 seconds, Resell Value 19 (resell value, not a store price).", "source": "image:item_tooltip for 'Flabbergast Orb' (wiki)"},
  {"claim": "Wiki says the orb is a level 1 battle item acquired from Battle Item Mystery Packs.", "source": "wiki page 'Flabbergast Orb'"},
  {"claim": "Battle Item Mystery Pack is granted by combat prize wheels (3 battle items per pack).", "source": "wiki page 'Battle Item Mystery Pack'; locale:6666; locale:6667"},
  {"claim": "Nekark (Western Seaside kraken boss) chest drops 3 each of 'Flabbergast' among other battle items.", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Seaside.md:156 (wiki Nekark; client)"},
  {"claim": "Client has no coin store price for this item (coin_store_prices empty), so no coin vendor sale is evidenced.", "source": "client definition, definition_id 11017"}
 ],
 "confidence": 0.5,
 "open": [
  "Mystery Pack source rests on the wiki item page alone; the pack's item list (Battle Item Mystery Pack page) was not shown to include the Orb, so verify the pack's contents.",
  "Nekark chest drop lists 'Flabbergast' with no suffix; repo also has 'Flabbergast Spheres' (piece_057). Not established whether that is this Orb. Treat the Nekark drop as unconfirmed for this item.",
  "Resell value 19 is not a purchase price; no Station Cash or coin price is known.",
  "The client cluster has 'Flabbergast Orb 1' (20455) and 'Flabbergast Orb II (PH)' (20458) with placeholder flags; tier relationship to this item is unconfirmed.",
  "No retirement evidence found; retired left null. 'Live' is yes from the wiki tooltip showing a player-owned count, but no date or patch source."
 ]}
