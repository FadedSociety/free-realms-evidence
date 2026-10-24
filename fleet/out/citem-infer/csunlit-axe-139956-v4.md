<!-- fleet job=citem-infer id=csunlit-axe-139956-v4 status=done turns=1 usd=0.0016 tokens(read,write,in,out)=[0, 6421, 4, 1562] model=claude-haiku-5-5 -->
# Sunlit Axe

{"item": {"name": "Sunlit Axe", "locale_id": 139956, "kind": "weapon"},
 "sources": [],
 "retired": true,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Sunlit Axe' is locale 139956, item definition 48206, slot 7, class 17, model axe_ar_ag_weapon_battleaxe.adr", "source": "locale:139956; client definition"},
  {"claim": "Sunlit Axe is a level 5 Warrior weapon, Blue Text, and 'can only be acquired through trade'; Sweeping Slash 853 damage, Spinning Attack 1548 damage", "source": "wiki page Sunlit Axe"},
  {"claim": "Sunlit Axe is in Category:Retired Weapons, with no retirement date given", "source": "wiki page Sunlit Axe (categories)"},
  {"claim": "Store row for item 48206 (purchase 811 coins, member 729, sell-back 81, no_sale false) is the same row shared by items 48181-48219 in category 207, so it is a category default and not evidence of a sale of this axe", "source": "prototype/osfr-tools/data/content/stores.json:13255 (rows 13230-13268)"},
  {"claim": "Items 48220-48221 carry a different row (1431 / 1287 / 143)", "source": "prototype/osfr-tools/data/content/stores.json:13269-13270"},
  {"claim": "Wiki Blue Text weapon page lists Sunlit Axe with its Sunlit siblings; the excerpt gives no acquisition source", "source": "wiki page Blue Text weapon"},
  {"claim": "Wiki files File:Sunlit Axe held.jpg and File:Sunlit Axe item.jpg exist with no transcribed acquisition text", "source": "wiki File:Sunlit Axe held.jpg; File:Sunlit Axe item.jpg"}
 ],
 "confidence": 0.3,
 "open": [
  "No vendor sale is evidenced. The 811-coin row (stores.json item 48206, category 207) is shared by items 48181-48219 and has no vendor, NPC, shop or zone resolved, so it is left unresolved and not listed as a source. If a later pass resolves category 207 to a vendor, that vendor could be added with the price 811 coins (member 729).",
  "Acquisition conflict: the wiki says the item can only be acquired through trade (player-to-player), while the store data carries a coin price. Unresolved.",
  "Retired status rests only on the wiki category Retired Weapons. No retirement date and no end date for any coin listing was found.",
  "No quest reward, enemy drop, event, prize wheel, crafting, collection, membership, promotion or video source names this item.",
  "Not wireable: no evidenced in-game source exists. The earlier claim that Blue Text weapons were members-only dungeon drops is not supported and is removed.",
  "Critique fix applied: the store row path was corrected to prototype/osfr-tools/data/content/stores.json:13255, and the shared range is 48181-48219 (not 48187-48219)."
 ]}
