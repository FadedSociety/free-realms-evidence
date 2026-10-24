<!-- fleet job=citem-infer id=cconfetti-wand-139939-v1 status=done turns=4 usd=0.0027 tokens(read,write,in,out)=[19511, 9041, 10, 2721] model=claude-haiku-5-5 -->
# Confetti Wand

{"item": {"name": "Confetti Wand", "locale_id": 139939, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale listing (vendor not identified in our data); purchase price 811 coins, member price 729 coins (10% member discount)", "where": null, "price": "811 coins (member price 729 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48189 (line 13238); client definition coin_store_prices [811]"},
  {"type": "drop", "detail": "Original Blue Text weapon source: members-only dungeon 'boss' enemy drops, before the Blue Text weapons were retired on 2009-12-14. Item-specific drop not confirmed.", "where": "dungeons (unspecified)", "price": null, "currency": null, "source": "wiki: Blue Text weapon; wiki: Category:Blue Text Weapons"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Confetti Wand is a level 5 Wizard weapon, Blue Text, Power 3, Zap 488 dmg and Lightning Blast 1998 dmg", "source": "wiki: Confetti Wand; image:item_tooltip Confetti Wand item.jpg"},
  {"claim": "Confetti Wand is in Category:Retired Weapons and Category:Blue Text Weapons", "source": "wiki: Confetti Wand (categories)"},
  {"claim": "Blue Text weapons were retired on December 14, 2009; names changed to white, membership requirement dropped; currently only acquired through trade", "source": "wiki: Blue Text weapon"},
  {"claim": "Blue Text weapons were members-only and dropped at random by certain boss enemies in dungeons", "source": "wiki: Category:Blue Text Weapons"},
  {"claim": "Store row for item 48189 with purchase_price_coins 811, member_price 729, sell_price 81", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48189"},
  {"claim": "Wiki resell value 81 matches the store sell price 81", "source": "wiki image:item_tooltip Confetti Wand item.jpg; repo stores.json item 48189"},
  {"claim": "Client name locale 139939 and sibling Confetti set (Bow, Kendama Hammer, Scalpel, Blade, Axe) and Party set share a cluster", "source": "locale:139939; locale:139934-139944"}
 ],
 "confidence": 0.6,
 "open": [
  "Conflict: jev first-pass tag says live=yes, but the wiki says the Blue Text weapons were retired 2009-12-14 and the item is only obtainable through trade. Treated as not live (retired).",
  "The coin store row (item 48189, 811 coins) is in our data, but the vendor NPC and zone that sells it are not identified. The wiki names no coin vendor for it. Whether it was sold in the store after the 2009 retirement is not confirmed by any source here; the wiki's 'only through trade' line suggests the store listing is no longer active.",
  "Wiki says 'can only be acquired through trade' as a current state. Trade is a player-to-player source, not a listed source type, so it is not recorded as a source here.",
  "Specific boss enemy that dropped the Confetti Wand is not named in any source.",
  "Price 811 coins is the store purchase price, not a wiki-stated price. The wiki gives only the resell value (81)."
 ]}
