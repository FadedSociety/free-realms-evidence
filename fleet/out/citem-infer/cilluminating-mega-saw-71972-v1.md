<!-- fleet job=citem-infer id=cilluminating-mega-saw-71972-v1 status=done turns=3 usd=0.0020 tokens(read,write,in,out)=[8858, 8118, 8, 1766] model=claude-haiku-5-5 -->
# Illuminating Mega Saw

{"item": {"name": "Illuminating Mega Saw", "locale_id": 71972, "kind": "weapon"},
 "sources": [
  {"type": "other", "detail": "Player trade only (Blue Text weapon); no NPC vendor, quest, drop or event source is documented", "where": null, "price": null, "currency": null, "source": "wiki page 'Illuminating Mega Saw' (\"can only be acquired through trade\"); wiki 'Blue Text weapon' table lists it under Medic"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Illuminating Mega Saw is a level 8 Medic Blue Text weapon, acquirable only through trade", "source": "wiki page: Illuminating Mega Saw"},
  {"claim": "Page is categorized Category:Retired Weapons", "source": "wiki page: Illuminating Mega Saw (categories)"},
  {"claim": "Listed in the Blue Text weapon table (Medic column, Illuminating line alongside Illuminating Bow, Drill, Scythe, Hammer, Wand)", "source": "wiki page: Blue Text weapon"},
  {"claim": "Client name locale 71972 is 'Illuminating Mega Saw', the same name as the wiki page", "source": "locale:71972"},
  {"claim": "Jev's first-pass 'vendor' source guess is not supported: no wiki, article, or vendor data names a coin vendor selling this item", "source": "evidence pack vendor_stock empty; wiki page"}
 ],
 "confidence": 0.5,
 "open": [
  "Coin store price 1236 in the client definition could not be tied to this item. repo stores.json has many entries with purchase_price_coins 1236 (for example item_id 4148, 4149, 6863), but none is confirmed as definition 22222 or 48127. Not cited as a coin vendor source until the item id is matched.",
  "Client definition has two definition ids (22222, 48127); the wiki does not say which variant(s) were traded or whether tints differ.",
  "Wiki page lists the Medic weapon's effects (Incision 1492 damage; Triage heals 1357, deals 4750) but gives no date for when trade was closed or whether it was ever sold on the SC Marketplace or Coin Shop.",
  "Trade is player-to-player, which is not one of the listed source types; recorded as 'other'.",
  "Wiki page's 'Blue Text' wording and the placeholder-flagged sibling descriptions (locale 71974-71977) were not used as evidence for this item."
 ]}
