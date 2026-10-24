<!-- fleet job=dialog-infer id=wknow-your-enemy-v1 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[7472, 9620, 6, 2132] model=claude-haiku-5-5 -->
# Know your Enemy

{"quest": {"key": "know_your_enemy", "title": "Know your Enemy"},
 "offer": null,
 "progress": null,
 "complete": null,
 "other_lines": [
  {"locale_id": 5100916, "role": "objective_hint", "speaker": null},
  {"locale_id": 5100918, "role": "objective_hint", "speaker": null},
  {"locale_id": 5100919, "role": "other", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'Know your Enemy', tagged Seaside.", "source": "locale:5100917 (quest_title)"},
  {"claim": "5100918 is the quest objective: learn about the Cray by defeating them in combat; the Seaspray suspicion of Orchid Eventide is stated in the text.", "source": "locale:5100918 (quest_objective)"},
  {"claim": "5100916 is a second objective-style line for this quest (the full text ends 'See what you can learn about them in a fight.'; the earlier pack truncated it). It is not NPC speech, so it is an objective hint, not an offer.", "source": "locale:5100916 (quest_objective, full text via lookup)"},
  {"claim": "5100919 is tagged quest_dialog to this quest, but its text is a player-side reaction ('The Cray are behaving like mindless attack drones?'), and no NPC is named or attributed to it. It is not a clear offer, progress reminder or thanks, so it is left unassigned.", "source": "locale:5100919 (quest_dialog, Seaside, Know your Enemy)"},
  {"claim": "Seaspray is the quest line's giver per the Seaside notes and the Heroes Journal wiki page (quest order: Tides of Change, Know Your Enemy, Meet Crabcake).", "source": "repo notes NPCs - Seaside.md:32,216; wiki Heroes Journal page"},
  {"claim": "Seaspray dialog ids 101061/101070/101064 in the earlier pack belong to Craving Something Tasty, not this quest, so they are rejected.", "source": "npc answer attribution, cross-checked against quest tags"}
 ],
 "confidence": 0.3,
 "open": [
  "No offer, progress or complete line for this quest is tagged or attributed in the client text. Slots left null rather than guessed.",
  "5100919 has no named speaker and reads as a reaction, so it is listed only as 'other' with speaker null.",
  "Seaspray's dialog ids in the earlier pack (101061, 101070, 101064) are for Craving Something Tasty and cannot be used here.",
  "Reward: none found in client text, wiki or repo.",
  "Objective kind 'defeat' is supported by the wording of 5100918 but not confirmed by quest data. The earlier pack's target id 90007 was not verified and is omitted.",
  "No quest record or npc_id linked to this quest was found; quest key is a slug from the title.",
  "Earlier pack's 'live: unsure' stands. Dialog cannot be bound until a quest record or stage-to-line link is found."
 ]}
