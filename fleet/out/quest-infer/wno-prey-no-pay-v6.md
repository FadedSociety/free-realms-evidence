<!-- fleet job=quest-infer id=wno-prey-no-pay-v6 status=done turns=3 usd=0.0032 tokens(read,write,in,out)=[19121, 11490, 8, 3232] model=claude-haiku-5-5 -->
# No Prey, No Pay

{"quest": {"record_id": null, "title": "No Prey, No Pay", "title_locale_id": 427880},
 "live": "yes",
 "live_reason": "Title locale:427880 is an unflagged quest_title tagged Seaside, and its objectives (427887, 427885, 427881) and the Fishfinder dialog (427879) are unflagged. The wiki page Admiral Fishfinder says she gives No Prey, No Pay at first encounter. Nothing marks it not_live. The repo title hash 2548613727 (NPCs - Seaside.md:264) is not a client id and is kept only as a cross-reference.",
 "zone": "Seaside",
 "giver": {"name": "Admiral Fishfinder", "npc_id": null, "locale_id": 427718},
 "line": {"name": "Pirate's Plunder introduction (Admiral Fishfinder, then Jolly Roger)", "previous": [], "next": ["Speak to Jolly Roger (locale:427887) step, then the Pirate's Plunder minigame teleport (locale:427915)"]},
 "objectives": [
  {"kind": "talk", "text": "Speak to Jolly Roger", "text_locale_id": 427887, "target": "Jolly Roger", "target_locale_id": 426870, "count": null},
  {"kind": "other", "text": "Learn about Pirate's Plunder", "text_locale_id": 427885, "target": "Pirate's Plunder", "target_locale_id": 427834, "count": null},
  {"kind": "minigame", "text": "Find Jolly Roger in Seaside and challenge a pirate to Pirate's Plunder!", "text_locale_id": 427881, "target": "Pirate's Plunder", "target_locale_id": 427834, "count": null}
 ],
 "dialog": {"offer": 427879, "progress": null, "complete": null},
 "rewards": [],
 "evidence": [
  {"claim": "Title 'No Prey, No Pay' is an unflagged quest_title tagged Seaside", "source": "locale:427880"},
  {"claim": "Objective 'Speak to Jolly Roger'", "source": "locale:427887"},
  {"claim": "Objective 'Learn about Pirate's Plunder'", "source": "locale:427885"},
  {"claim": "Objective 'Find Jolly Roger in Seaside and challenge a pirate to Pirate's Plunder!'", "source": "locale:427881"},
  {"claim": "Fishfinder's speech: she asks whether you have a ship and crew registered and sends you to Jolly Roger ('Go talk to Jolly Roger'); this is the first-encounter line and the best offer candidate", "source": "locale:427879"},
  {"claim": "Admiral Fishfinder name is locale 427718", "source": "locale:427718"},
  {"claim": "At first encounter Admiral Fishfinder has the quest No Prey, No Pay; after it she sends you to Pirate's Plunder and transports you to Seaside", "source": "wiki page:Admiral Fishfinder"},
  {"claim": "Jolly Roger's registration line 'Talk to Jolly Roger about registering your own ship and crew' is npc_dialog, not an objective", "source": "locale:427892"},
  {"claim": "Teleport offer to Jolly Roger for a round of Pirate's Plunder is 427915, the minigame step after the quest", "source": "locale:427915"},
  {"claim": "Title hash 2548613727 for No Prey, No Pay is recorded in repo notes with Fishfinder as giver and Jolly Roger as hand-in", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Seaside.md:264"},
  {"claim": "Two Fishfinder placements exist: 9500000083 (Briarwood) and 9500000547 (unknown zone)", "source": "repo:notes/Research/NPC Placement.md:68"},
  {"claim": "Jolly Roger receives No Prey, No Pay and registers ship and crew via the bookstand (2642857805)", "source": "repo:prototype/osfr-tools/data/content/npcs/seaside.json:22952"}
 ],
 "confidence": 0.6,
 "open": [
  "record_id is null: no quest record exists in our data; the repo title hash 2548613727 is not confirmed as the record key and no client id matches it.",
  "giver npc_id unresolved: two Admiral Fishfinder placements (9500000083 Briarwood per briarwood.json:7; 9500000547 zone unknown per seaside.json:336 and NPC Placement.md:68). Neither is matched to the client NPC table, so it stays null.",
  "Zone split: the giver is placed in Nettleseed/Briarwood but the quest's client tag and objectives are Seaside. Zone is recorded as Seaside from the client tag; builder should confirm against the giver placement.",
  "offer 427879 is inferred from its content (first-encounter speech that sends the player to Jolly Roger), not from a confirmed NPC dialog slot. progress and complete are unknown: no client line is confirmed as the hand-in. 427892 is Jolly Roger's registration hint, not a completion line.",
  "previous quest is not confirmed; next is the Jolly Roger step, and the Pirate's Plunder teleport (427915) is a minigame offer, not a quest title. Pirate's Plunder (427834) is a minigame name, not a quest.",
  "objective 427881 count is not stated in text, so it is null; the challenge target is a pirate NPC that the client text does not name.",
  "No reward data found in the client, wiki or articles.",
  "The wiki's repeatable:false flag is not confirmed by any client text."
 ]}
