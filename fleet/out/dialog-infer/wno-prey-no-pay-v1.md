<!-- fleet job=dialog-infer id=wno-prey-no-pay-v1 status=no_submit turns=3 usd=0.0023 tokens(read,write,in,out)=[12043, 7966, 8, 2410] model=claude-haiku-5-5 -->
# No Prey, No Pay

```json
{"quest": {"key": "No Prey, No Pay", "title": "No Prey, No Pay"},
 "offer": {"locale_id": 427879, "speaker": "Admiral Fishfinder"},
 "progress": {"locale_id": 427892, "speaker": "Jolly Roger"},
 "complete": null,
 "other_lines": [
  {"locale_id": 427881, "role": "objective_hint", "speaker": null},
  {"locale_id": 427887, "role": "objective_hint", "speaker": null},
  {"locale_id": 427885, "role": "objective_hint", "speaker": null},
  {"locale_id": 427889, "role": "followup", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'No Prey, No Pay' (quest_title, Seaside).", "source": "locale:427880"},
  {"claim": "Offer-stage text: a pirate challenges the player to test skills, says the player must register a ship and crew, and sends them to Jolly Roger. This is the only quest-tagged line that reads as a first-encounter offer.", "source": "locale:427879"},
  {"claim": "Admiral Fishfinder is the first-encounter giver of No Prey, No Pay.", "source": "wiki Admiral Fishfinder page (ns0); npc answer 'admiral fishfinder' quests_given"},
  {"claim": "Progress reminder points the player to Jolly Roger for ship/crew registration and pointers; tagged Seaside / Jolly Roger.", "source": "locale:427892 (npc_dialog, hint Jolly Roger)"},
  {"claim": "Objectives: Speak to Jolly Roger; Learn about Pirate's Plunder; Find Jolly Roger in Seaside and challenge a pirate.", "source": "locale:427887, 427885, 427881"},
  {"claim": "427882 (registration sign-in book) and 427889 (bookstand register prompt) are tutorial/bookstand lines, not this quest's hand-in or dialog slot.", "source": "locale:427882, 427889; 427915 teleport line also not used"},
  {"claim": "Jolly Roger's NPC page lists the quest, and the Pirate's Plunder ship dock is in Seaside.", "source": "npc answer 'jolly roger'; wiki Jolly Roger page"}
 ],
 "confidence": 0.4,
 "open": [
  "Offer speaker is inferred: 427879 is tagged to this quest and matches the first-encounter wording, but no NPC answer attributes it to Admiral Fishfinder. The line also says 'Go talk to Jolly Roger', so it could be a redirect rather than the offer.",
  "Progress speaker is from the tag hint only. 427892 refers to Jolly Roger in the third person ('Talk to Jolly Roger...'), so the actual speaker may be a bystander or a different NPC.",
  "No complete (hand-in) line found in the client. No client line is confirmed as a thank-you or payout for this quest.",
  "No reward data found in the client, wiki or articles.",
  "Giver NPC id and zone are unresolved: two Admiral Fishfinder placements (Briarwood and an unknown zone), and the wiki places the first encounter in Nettleseed/Briarwood while the quest tags say Seaside.",
  "Record id is not known. The previous and next quest links are not confirmed.",
  "Objective 427881 has no count in its text, so the count is null."
 ]}
```
