<!-- fleet job=dialog-infer id=wthis-glade-is-ours-v1 status=done turns=3 usd=0.0036 tokens(read,write,in,out)=[20994, 14943, 8, 3096] model=claude-haiku-5-5 -->
# This Glade is Ours!

{"quest": {"key": "This Glade is Ours!", "title": "This Glade is Ours!"},
 "offer": {"locale_id": 438260, "speaker": null},
 "progress": {"locale_id": 438258, "speaker": null},
 "complete": {"locale_id": 438261, "speaker": null},
 "other_lines": [
  {"locale_id": 438252, "role": "objective_hint", "speaker": null},
  {"locale_id": 438262, "role": "objective_hint", "speaker": null},
  {"locale_id": 438273, "role": "other", "speaker": null}
 ],
 "evidence": [
  {"claim": "Title is locale:438259, a clean quest_title tagged to Shrouded Glade / This Glade is Ours!", "source": "locale:438259"},
  {"claim": "438260 explains the offer: Sunspark rallying troops, join the final battle. Fits an offer, not a progress reminder.", "source": "locale:438260"},
  {"claim": "438258 is a ready-for-the-final-attack reminder that states the objective (defeat Gloam army, save Camellia). Fits progress.", "source": "locale:438258"},
  {"claim": "438261 is a quest_reward thank-you that names Gus of the Sunstone Dwarves and the druids. Fits complete. It has no coin or item amount, so reward is text only.", "source": "locale:438261"},
  {"claim": "Objectives: escort step 'Reach the third escort point' (438252) and 'Defeat Gloam constructs' (438262, target Gloam Construct 438264), both tagged to this quest.", "source": "locale:438252, locale:438262, locale:438264"},
  {"claim": "Captain Sunspark is the giver. The NPC answer lists This Glade is Ours! among his quests_given. His dialog attribution covers only 438268 and 438270, not the offer, progress or completion lines.", "source": "npc answers: captain sunspark"},
  {"claim": "438273 'Defeat General Drahk' is tagged to Save Arch Druid Camellia, so it is not this quest's objective. General Drahk is named in the wiki as appearing during this quest.", "source": "locale:438273 / wiki:Shrouded Gloam"}
 ],
 "confidence": 0.5,
 "open": [
  "Speakers are null for offer, progress and complete. The text is third-person or unattributed, and the NPC answer attributes only 438268/438270 to Sunspark. Sunspark is the giver by quest_answer and quests_given, but that does not name the speaker of these lines. Builders should confirm in-game.",
  "Finale boss unresolved. 438262 'Defeat Gloam constructs' is the tagged objective. The repo note cites 'Do you want to face General Drahk again in the final battle?', which is locale:438305 (the id behind hash 1046625125). It is a yes/no prompt, not a quest line of this quest, so it is not used. Whether Drahk is a second objective is open.",
  "438268 'Join Captain Sunspark for the final attack...' belongs to the group 'Final Attack on the Gloam' (438268-438270) in the client tags, not to this title. Left out. It may be a successor, so next is unknown.",
  "Escort objective kind 'go' and count are inferred from wording. No escort NPC or script was found.",
  "Previous 'Report to Sunspark' is weakly sourced (wiki order only). No record id or Sunspark npc_id/name locale id is verified.",
  "Next is unknown. No successor is confirmed.",
  "438266 is FLAGged not_live and was excluded. 438242 (Gloam is eternal) is a mid-quest line with no clear role and was not used."
 ]}
