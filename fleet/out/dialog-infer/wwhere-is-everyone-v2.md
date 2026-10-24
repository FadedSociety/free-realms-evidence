<!-- fleet job=dialog-infer id=wwhere-is-everyone-v2 status=done turns=4 usd=0.0026 tokens(read,write,in,out)=[25670, 9966, 10, 2235] model=claude-haiku-5-5 -->
# Where is Everyone?

{"quest": {"key": "Where is Everyone?", "title": "Where is Everyone?"},
 "offer": null,
 "progress": null,
 "complete": null,
 "other_lines": [
  {"locale_id": 10166, "role": "other", "speaker": null},
  {"locale_id": 10167, "role": "objective_hint", "speaker": null},
  {"locale_id": 9899, "role": "followup", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'Where is Everyone?'", "source": "locale:10166 (quest_title, no hint)"},
  {"claim": "Objective: find the Sanctuary guards who are slacking off", "source": "locale:10167 (quest_objective, tagged Sanctuary, same title)"},
  {"claim": "15178 (four missing guards Slashi, Banee, Snapdragon, Hardin) is tagged 'Sanctuary Find Guard Banee', so it is not this quest's offer", "source": "locale:15178 via lookup tag"},
  {"claim": "15189 ('Aw man, you found me!') is tagged Find Guard Banee, so the guard-search chain belongs to that quest", "source": "locale:15189 via lookup tag"},
  {"claim": "9899 ('You found my lazy guards? ... Thank you for your help, citizen.') is an untagged quest_dialog with only the hint 'lazy guards'; it is a thank-you that fits a guard-return story, but no tag or NPC answer links it to this quest or names its speaker", "source": "locale:9899; lookup tag shows no title"},
  {"claim": "General Glowlight is the giver per the wiki/NPC list; no client dialog line tagged to this quest was found", "source": "npc answer: General Glowlight quests_given; locale:16840 is an untagged NPC greeting, not an offer"},
  {"claim": "No reward line found", "source": "search of client lines tagged to this quest"}
 ],
 "confidence": 0.2,
 "open": [
  "No offer, progress or complete line is tagged to 'Where is Everyone?'. Slots left null rather than guessed.",
  "9899 is kept only as a followup candidate with speaker null. It is untagged and the guard-search line family (15178, 15189) is tagged to Find Guard Banee, so 9899 more likely belongs to that quest's completion. Do not wire it as this quest's complete without confirmation.",
  "15178 is the four-guard search offer but is tagged to Find Guard Banee, so it is excluded here.",
  "16840 is an untagged Glowlight NPC greeting, not a quest offer; excluded.",
  "General Glowlight npc_id unconfirmed; speaker names left null where no line attributes one.",
  "Previous/next quest chain and reward unknown; quest key uses the title because no record id exists.",
  "38440/38439/38441 belong to the Nettleseed 'X Marks the... Where is Everyone?' quest, not this one."
 ]}
