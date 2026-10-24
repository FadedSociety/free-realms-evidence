<!-- fleet job=quest-infer id=wfarewell-feast-v2 status=done turns=4 usd=0.0029 tokens(read,write,in,out)=[27185, 10339, 10, 2628] model=claude-haiku-5-5 -->
# Farewell Feast

{"quest": {"record_id": null, "title": "Farewell Feast", "title_locale_id": 428200},
 "live": "unsure",
 "live_reason": "Title 428200 and its objective/dialog lines are unflagged quest_title/quest_objective/quest_dialog strings, and the wiki and our NPC dossier both list the quest under Diggy. Nothing shows it shipped in a live build, and no record exists in our 660 records.",
 "zone": "Seaside",
 "giver": {"name": "Diggy", "npc_id": "9000000070", "locale_id": 21302},
 "line": {"name": null, "previous": [], "next": []},
 "objectives": [
  {"kind": "talk", "text": "Tell Diggy what food the pirates want for the party", "text_locale_id": 428218, "target": "Diggy", "target_locale_id": 21302, "count": null},
  {"kind": "other", "text": "Help Diggy prepare a feast for Jolly Rogers' crew that will make these retiring pirates happy.", "text_locale_id": 428201, "target": "Jolly Rogers' crew", "target_locale_id": null, "count": null},
  {"kind": "use", "text": "Cook the steak dinner at the pan next to Diggy (cooking step inferred; not tied to this quest by a locale id)", "text_locale_id": null, "target": "pan next to Diggy", "target_locale_id": 100280, "count": null}
 ],
 "dialog": {"offer": 428199, "progress": 428203, "complete": null},
 "rewards": [],
 "evidence": [
  {"claim": "Quest title is Farewell Feast", "source": "locale:428200"},
  {"claim": "Objective to help Diggy prepare a feast for Jolly Rogers' crew", "source": "locale:428201"},
  {"claim": "Objective to tell Diggy what food the pirates want", "source": "locale:428218"},
  {"claim": "Opening dialog: Diggy asked to cater the old captain's homecoming party", "source": "locale:428199"},
  {"claim": "Question prompt about what the scurvy searats want to eat", "source": "locale:428203"},
  {"claim": "Steak dinner decision, thanks, and mention that Jolly Rogers gave Diggy an old treasure map that Diggy thinks the player could put to better use (the map is not a stated reward)", "source": "locale:428202"},
  {"claim": "Diggy says he will cook a sample of the entree", "source": "locale:428207"},
  {"claim": "Pirates reject seafood and approve the steak ('Me buckos are sure to love it!')", "source": "locale:428221, locale:428219"},
  {"claim": "Giver is Diggy at Ocean Treasures Cafe, Seaside, with Farewell Feast title 3030398973", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Seaside.md:45 and :231"},
  {"claim": "Wiki lists Farewell Feast under Diggy, not repeatable", "source": "wiki Diggy"},
  {"claim": "Diggy's NPC id 9000000070 and name 21302; pan services entry and 'Click pan next to Diggy' text", "source": "repo:prototype/osfr-tools/data/content/npcs/seaside.json:12107, :12114, :12143, :12149-12150; locale:100280"}
 ],
 "confidence": 0.4,
 "open": [
  "No quest record exists; record_id is null, so this needs a new record.",
  "Line position is unknown: no sourced previous or next quest was found. Hasty Food Delivery (title 1798567334) is another Diggy quest, but its order is not established.",
  "Reward: no coin, XP or item reward is sourced. The treasure map in locale:428202 is described as given to Diggy, not as a player reward.",
  "dialog.complete is not established. 428202 (Diggy's thanks) is the only candidate; 428219 and 428207 are pirate or cook lines. The dialog flow is unverified.",
  "The previous answer cited locale 3078444031 for 'Click pan next to Diggy'. That id does not exist in the client. The matching client string is locale 100280 ('Click pan next to Diggy to begin!'), and its link to Farewell Feast is inferred from the NPC dossier, not from the locale hint.",
  "Whether the cooking step is a single minigame or several steps, and the wrong-answer (Seaweed, 428204) branch, are unverified.",
  "live is unsure: the text is unflagged and the wiki lists the quest, but nothing confirms it shipped."
 ]}
