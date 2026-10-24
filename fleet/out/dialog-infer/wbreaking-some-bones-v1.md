<!-- fleet job=dialog-infer id=wbreaking-some-bones-v1 status=done turns=3 usd=0.0021 tokens(read,write,in,out)=[13152, 9063, 8, 1767] model=claude-haiku-5-5 -->
# Breaking Some Bones

{"quest": {"key": "breaking_some_bones", "title": "Breaking Some Bones"},
 "offer": {"locale_id": 384295, "speaker": "Oberyn Duskshine"},
 "progress": null,
 "complete": {"locale_id": 384298, "speaker": "Oberyn Duskshine"},
 "other_lines": [
  {"locale_id": 384282, "role": "other", "speaker": null},
  {"locale_id": 384283, "role": "objective_hint", "speaker": null},
  {"locale_id": 384284, "role": "objective_hint", "speaker": null},
  {"locale_id": 384297, "role": "objective_hint", "speaker": "Oberyn Duskshine"}
 ],
 "evidence": [
  {"claim": "Offer line: Oberyn asks the player to bring the bones of a powerful elemental in exchange for a reward; text does not name the quest task explicitly beyond 'bones' and 'grave elementals'.", "source": "locale:384295 (quest_dialog, tag hint Oberyn Duskshine; confirmed by full-text lookup)"},
  {"claim": "Completion line: Oberyn takes the bones and says to take your reward; this is the turn-in thanks/pay line.", "source": "locale:384298 (quest_dialog, tag hint Oberyn Duskshine; confirmed by full-text lookup)"},
  {"claim": "Quest title is Breaking Some Bones, zone Sunken Graveyard / Blackspore Swamp.", "source": "locale:384282 (quest_title)"},
  {"claim": "Objective texts for the collect step.", "source": "locale:384283, locale:384284 (quest_objective tagged Breaking Some Bones)"},
  {"claim": "Giver is Oberyn Duskshine, npc_name locale 45301; wiki places him at Oberyn's Retreat, Blackspore Swamp, with Breaking Some Bones listed.", "source": "locale:45301; wiki page Oberyn Duskshine"},
  {"claim": "No progress/reminder line for this quest exists in the client tagged to it or attributed to Oberyn.", "source": "locale and lookup searches for the quest title and Oberyn's name"},
  {"claim": "No reward item or amount is named in the client for this quest.", "source": "locale:384298 only says 'take your reward'"}
 ],
 "confidence": 0.7,
 "open": [
  "Target conflict unresolved: collect objectives 384283/384284 say Grave Lord, while offer 384295 and objective 384297 say grave elemental. The Grave Lord wording is kept only as objective text; no target name is settled.",
  "Progress slot null: no reminder line identified for this quest.",
  "Reward null in the client: no named reward; 384298 is the only pay-style line.",
  "Kill step (388854, 385616) belongs to a different group (Blackspore Grave Lord) and is not used.",
  "Previous/next chain not established; 384288 and 408090 are not used as links.",
  "Item name and count are not in the client; left null.",
  "npc_id left null: the earlier 9500000054 was a reconstructed key and is withdrawn; giver is referenced by locale 45301."
 ]}
