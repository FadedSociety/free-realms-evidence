<!-- fleet job=dialog-infer id=whouse-cleaning-v1 status=done turns=3 usd=0.0029 tokens(read,write,in,out)=[20005, 11849, 8, 2507] model=claude-haiku-5-5 -->
# House Cleaning

{"quest": {"key": "House Cleaning", "title": "House Cleaning"},
 "offer": {"locale_id": 438871, "speaker": null},
 "progress": null,
 "complete": {"locale_id": 438874, "speaker": null},
 "other_lines": [
  {"locale_id": 438873, "role": "objective_hint", "speaker": null},
  {"locale_id": 438872, "role": "other", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'House Cleaning' (quest_title, Sunstone Valley)", "source": "locale:438872"},
  {"claim": "Offer-stage line: explains the Skullz traps are handled and directs the player to Headmaster Merk about the Gloam influence in the Rumbledome", "source": "locale:438871 (full text confirmed via locale lookup)"},
  {"claim": "Completion line: Gloam influence gone, new gear ready, 'Good job, [*player*]!'", "source": "locale:438874 (full text confirmed)"},
  {"claim": "Objective text: talk to Headmaster Merk for a way to purge the Gloam influence", "source": "locale:438873 (confirmed); purge objective wording also at 439088"},
  {"claim": "Giver Golmie Greasebeard and the Golmie-to-Merk handoff are consistent with repo notes (NPCs - Sunstone Valley.md:199, The Rumbledome.md:84)", "source": "repo notes; not a client attribution"},
  {"claim": "No reward line exists for this quest in client text", "source": "tagged client lines 438871-438874 contain none"}
 ],
 "confidence": 0.5,
 "open": [
  "Speakers of 438871 and 438874 are not named in the text and no NPC answer attributes them; per the rules they are null. Golmie as giver is only from repo/wiki attribution.",
  "438873 is a quest_objective string, not NPC dialog, so it is not used as Merk's progress line; progress is null because no in-progress NPC dialog line exists for this quest in the pack.",
  "Merk's npc answer lists 438873 as quest_progress, which conflicts with its objective-string tag; treated as objective text.",
  "Purge-step lines 439094 and 439089 were not confirmed as this quest's lines (hint names the purge but the pack did not verify the tie); repo cites loc 2628119525 which was not checked. Left out.",
  "Successor 'Enter the Rumbledome' (438876 is an objective string; 438877 is Dorn's line for the next quest) is not this quest's line. Its quest_title record was not found.",
  "Immediate predecessor Better Threads is from wiki/repo list order; Better Treads not ruled out.",
  "No quest record exists, so no record_id; NPC ids (Golmie 9500000821, Merk 9500000690) are from repo JSON only."
 ]}
