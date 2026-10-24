<!-- fleet job=citem-infer id=crobgoblin-cut-out-mask-119228-v1 status=done turns=8 usd=0.0045 tokens(read,write,in,out)=[71318, 14927, 18, 3910] model=claude-haiku-5-5 -->
# Robgoblin Cut-Out Mask

{"item": {"name": "Robgoblin Cut-Out Mask", "locale_id": 119228, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale of item 69231 (purchase price 50 coins; member price 45 coins, 10% member discount). Vendor/NPC not identified in the store data.", "where": "coin store (stores.json category 101)", "price": "50 coins (member price 45 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 69231 (line 14865)"},
  {"type": "prize_wheel", "detail": "Archer Prize Wheel reward from the Vampire Dance Practice battle (Super Spooktacular, Halloween event). Listed in the Vampire Dance Practice reward block.", "where": "Blackspore Swamp, Sinking Graveyard (Vampire Dance Practice battle, spawned only during Super Spooktacular)", "price": null, "currency": null, "source": "wiki page 'Vampire Dance Practice' (Rewards: 96 Stars; Archer Prize Wheel: Robgoblin [Cut-Out] Mask); wiki 'Super Spooktacular'"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name and client text: locale 119228 'Robgoblin Cut-Out Mask', description 'Be careful that you don't get your Robgoblin mask robbed by a Robgoblin.'", "source": "locale:119228"},
  {"claim": "Store data lists item 69231 at 50 coins purchase, 45 coins for members, sell 5 coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 69231"},
  {"claim": "Archer Prize Wheel rewards from the Vampire Dance Practice battle include the Robgoblin [Cut-Out] Mask, alongside Big Jack-O-Lantern, Black Cat Pail, Ghost Stand-Up and Spooktacular Balloons", "source": "wiki page 'Vampire Dance Practice'"},
  {"claim": "Wizard Prize Wheel also lists the Robgoblin [Cut-Out] Mask (with Cat Cut-Out Mask, Bat Pail, Big Jack-O-Lantern, Ghost Sticker, Small Jack-O-Lantern)", "source": "wiki page 'Werewolf Dance Practice' (block listing Wizard Prize Wheel)"},
  {"claim": "Dance Practice battles spawn only during the Super Spooktacular Halloween event; the event ran annually (first 2009 Oct 14 to Nov 11; fourth 2013 Oct 1 to Nov 12)", "source": "wiki 'Vampire Dance Practice'; wiki 'Super Spooktacular'; articles http://www.freerealms.com/article/detail.action?articleId=2949 and http://www.tentonhammer.com:80/node/75739"},
  {"claim": "Set siblings Cat/Treeble/Dog/Skeleton/Pumpkin Cut-Out and Paper Bag masks are in the same client cluster and the Wizard/Archer wheel lists, so the mask is part of the Halloween prize set", "source": "client_cluster in pack (locale 119223-119233); wiki 'Werewolf Dance Practice'"}
 ],
 "confidence": 0.6,
 "open": [
  "Coin store sale: the store data gives 50 coins but not which coin vendor/NPC sells it or whether it is seasonal; the pack's 'vendor_stock' is empty. Need the coin shop category 101 name and vendor.",
  "Prize wheel: the wiki lists it under Archer and Wizard Prize Wheels in Dance Practice rewards, but the exact wheel slot odds and whether it is a Super Spooktacular-only prize were not confirmed.",
  "Retirement: wiki 'Super Spooktacular' has a 2009-only list of items not in later years; the visible text did not show whether the Robgoblin mask is on it. Live status is unsure until that list or a 2013+ source is checked.",
  "Wiki 'Snow Days' and the 'A Deal with a Dust Devil' quest mention Robgoblins but not this mask; they were not used as sources.",
  "Pack gave no wiki category (Coin Shop / Prize Wheel Weapons / Holiday) for the mask; the prize wheel source relies on the dance practice reward lists alone."
 ]}
