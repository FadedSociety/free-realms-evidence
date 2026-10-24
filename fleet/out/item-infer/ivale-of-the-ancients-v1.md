<!-- fleet job=item-infer id=ivale-of-the-ancients-v1 status=nothing_found turns=2 usd=0.0025 tokens(read,write,in,out)=[4250, 12735, 6, 1786] model=claude-haiku-5-5 -->
# Vale of the Ancients

{"item": {"name": "Vale of the Ancients", "locale_id": 18143, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "'Vale of the Ancients' is a place: a difficulty 4 dungeon (combat instance) started by clicking the barrier in Bristlewood, Briarwood, with an Atlas icon.", "source": "https://freerealms.fandom.com/wiki/Vale_of_the_Ancients (rev 49124); locale:18143 [place]; locale:30430 [place]"},
  {"claim": "Client strings name it as a place and a combat encounter ('Win Combat Encounter Vale of the Ancients', 'Complete the Vale of the Ancients encounter', group 'Vale of the Ancients'), not as a tradeable item.", "source": "locale:119176; locale:30467; locale:31080; locale:140186"},
  {"claim": "The wiki page lists dungeon rewards (Prize Wheel items per job, a 202 Coins prize, 316 Stars or less, Members Only 238 Coins bonus, and clothing from the Corrupted Artifacts bonus goal). These are rewards of the dungeon, not sources of the dungeon itself.", "source": "https://freerealms.fandom.com/wiki/Vale_of_the_Ancients"},
  {"claim": "The place name is used in the Mother Lode Quarry, Shattered Past quest (Sir Wellington) and Briarwood vendor descriptions only as a location reference.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1339; http://www.freerealms.com:80/article/detail.action?articleId=2734"},
  {"claim": "locale:76687 'vale_of_the_ancients' is an internal map id label flagged dev_note, not a player-facing item name.", "source": "locale:76687"}
 ],
 "confidence": 0.9,
 "open": [
  "The input names a dungeon, not an item, so no item sources were recorded. The item-level question was not answered. If you meant one of the dungeon's rewards (for example Archer's Recurve Bow of Booming, Brawler's Drill Hammer of Chucking, Ninja's Jagged Scythe of Mysticism, or the Battle Item Mystery Pack), send that item's name and it can be researched with its own evidence.",
  "Prize Wheel rewards for this dungeon are listed on the wiki page only; no prize-wheel odds or per-wheel price were in the pack.",
  "The wiki's Bonus Rewards clothing set (Corrupted Artifacts goal) is cut off in the pack and its item names are not given.",
  "Repo notes (prototype/osfr-tools/data/content/dungeons_unresolved.json, enemies_unresolved.json) already map Vale of the Ancients as a dungeon owner for reward and boss rows; these are unresolved and were not verified here.",
  "Whether the dungeon itself is live or retired in the revival is not stated in the pack."
 ]}
