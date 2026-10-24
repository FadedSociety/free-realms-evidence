<!-- fleet job=dialog-infer id=wno-bro-left-behind-v1 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[6899, 7798, 6, 1779] model=claude-haiku-5-5 -->
# No Bro Left Behind

{"quest": {"key": "no_bro_left_behind", "title": "No Bro Left Behind"},
 "offer": {"locale_id": 437798, "speaker": null},
 "progress": null,
 "complete": null,
 "other_lines": [
  {"locale_id": 437800, "role": "objective_hint", "speaker": null},
  {"locale_id": 437811, "role": "objective_hint", "speaker": null},
  {"locale_id": 437812, "role": "objective_hint", "speaker": null},
  {"locale_id": 437814, "role": "objective_hint", "speaker": null},
  {"locale_id": 437815, "role": "objective_hint", "speaker": null},
  {"locale_id": 437816, "role": "objective_hint", "speaker": "Dorn Geargrinder"}
 ],
 "evidence": [
  {"claim": "Offer line 437798 is a quest_dialog about finding the missing southern supply party and bringing them back, matching this quest; its tag hint is Building Our Way Home, and no speaker is named in the text or tag.", "source": "locale:437798 / lookup client"},
  {"claim": "437816 'Return to Dorn Geargrinder' is a quest_objective (a reminder of the objective), not a progress dialog line; the earlier pack's classification as quest_progress is rejected.", "source": "locale:437816 quest_objective tag"},
  {"claim": "Task text: southern supply party missing; find them and defeat the Gloamed Dwarf; return to Dorn.", "source": "locale:437800, 437811, 437812, 437814, 437815"},
  {"claim": "Dorn Geargrinder is the giver per the wiki quest list; no spawn/NPC id bound.", "source": "npc answer dorn geargrinder"},
  {"claim": "No reward, progress dialog or completion dialog line tagged to this quest was found in the client.", "source": "client tag search for No Bro Left Behind"}
 ],
 "confidence": 0.4,
 "open": [
  "Offer speaker is null: 437798 names no speaker and its tag points to Building Our Way Home; the NPC answer for Dorn does not attribute 437798 to him.",
  "Progress and complete dialog: none found for this quest; left null rather than using objective text (437816) as progress.",
  "Reward: none found; rewards list is empty.",
  "Defeat count unresolved: 437815 says 'the 1st Gloamed Dwarf' (single kill tagged); untagged 438397-438400 sequence not confirmed as this quest's.",
  "Giver npc_id unknown; Dorn Geargrinder name match only.",
  "Previous/next quest record ids not in the pack; chain linked by title only.",
  "The earlier pack truncated 437798 and called 437816 a quest_progress line; corrected here."
 ]}
