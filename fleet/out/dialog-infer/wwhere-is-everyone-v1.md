<!-- fleet job=dialog-infer id=wwhere-is-everyone-v1 status=done turns=3 usd=0.0023 tokens(read,write,in,out)=[13407, 8316, 8, 2219] model=claude-haiku-5-5 -->
# Where is Everyone?

{"quest": {"key": null, "title": "Where is Everyone?"},
 "offer": null,
 "progress": null,
 "complete": {"locale_id": 9899, "speaker": null},
 "other_lines": [
  {"locale_id": 10166, "role": "other", "speaker": null},
  {"locale_id": 10167, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'Where is Everyone?'", "source": "locale:10166 (quest_title, no hint conflict)"},
  {"claim": "Objective: find the Sanctuary guards who are slacking off", "source": "locale:10167 (quest_objective, tagged Sanctuary, same quest title)"},
  {"claim": "9899 is a thank-you for finding the lazy guards, matching the objective's wording, so it is the best candidate for completion", "source": "locale:9899 (quest_dialog, hint 'lazy guards', no quest title tag)"},
  {"claim": "General Glowlight is the giver (quest-giver NPC listing includes Where is Everyone?)", "source": "npc answer: General Glowlight, quests_given"},
  {"claim": "Guard lines 15191/15193 ('General Glowlight sent you?') belong to the Find Guard Banee quest, not this one", "source": "locale:15191, 15193 (tagged 'Sanctuary Find Guard Banee')"},
  {"claim": "locale:46305 is Glowlight's completion line for A Profitable Package, not this quest", "source": "npc answer: General Glowlight dialog 46305 (quest A Profitable Package)"}
 ],
 "confidence": 0.3,
 "open": [
  "No offer line found: no client quest_dialog is tagged to 'Where is Everyone?' that asks or explains the quest.",
  "No progress line found for this quest.",
  "complete = 9899 is inferred from wording only; it has no quest-title tag and no NPC attribution. Speaker left null; the text implies General Glowlight ('my lazy guards') but nothing in the pack confirms it.",
  "The four guard names (Slashi, Banee, Snapdragon, Hardin) are not linked to this quest by any client line; 15178 and 73231 belong to a Find Guard quest, so they are not used.",
  "No reward line found.",
  "locale:38440 and 38439 belong to the Nettleseed 'X Marks the...' quest, not this one.",
  "Previous/next quest chain not confirmed; quest key left null because no record id exists.",
  "General Glowlight npc_id not confirmed, so it is not stated here."
 ]}
