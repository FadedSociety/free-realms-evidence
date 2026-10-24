<!-- fleet job=dialog-infer id=wmake-sure-to-wash-up-v4 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[19733, 12247, 8, 2237] model=claude-haiku-5-5 -->
# Make Sure to Wash up...

{"quest": {"key": "make_sure_to_wash_up", "title": "Make Sure to Wash up..."},
 "offer": null,
 "progress": null,
 "complete": {"locale_id": 90821, "speaker": "Milford"},
 "other_lines": [
  {"locale_id": 90818, "role": "objective_hint", "speaker": null},
  {"locale_id": 90819, "role": "other", "speaker": null},
  {"locale_id": 90820, "role": "objective_hint", "speaker": null},
  {"locale_id": 90827, "role": "objective_hint", "speaker": null},
  {"locale_id": 90828, "role": "other", "speaker": null},
  {"locale_id": 90829, "role": "objective_hint", "speaker": null},
  {"locale_id": 90832, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "90819 is the quest title 'Make Sure to Wash up...' (quest_objective, hint Blackspore | Milford).", "source": "locale:90819 / lookup client"},
  {"claim": "90818 is the collect-step objective text: gather poisonous toad secretion near water, then wash up or hands shrivel. It is quest_objective text with no speaker, so it is not offer or progress dialog.", "source": "locale:90818"},
  {"claim": "90828 is the sub-quest title 'Gather poison toad secretion'; 90827 and 90829 are its objective hints (video frames show 'Find the poisonous purple toads in Blackspore Swamp. Gather poison toad secretion - 2/5').", "source": "locale:90827, 90828, 90829 / video:APmoVBnJt98 frames"},
  {"claim": "90832 'Return to Milford in Blackspore' is the turn-in objective, target Milford (45293).", "source": "locale:90832, 45293"},
  {"claim": "90820 says Milford needs alchemy components for his master Eggert; it is a task description, not dialog. Milford is Eggert's assistant per 90732/90941 (Idle Hands chain), not per 90820.", "source": "locale:90820, 90732, 90941"},
  {"claim": "90821 ('Yes! Yes! Perfect! ... I wasn't kidding about the hands, you should take care of that') is a quest_dialog tagged Blackspore | Milford, reacts to a delivered item, and echoes the wash-up warning. Bound as complete, speaker Milford, on the Milford hint match.", "source": "locale:90821 / npc answer milford"}
 ],
 "confidence": 0.4,
 "open": [
  "Complete 90821 is a candidate, not confirmed by a turn-in source or video frame. Its 'hands' remark could also belong to Idle Hands (90730, 90732, 90745, 90746). Verify before live use.",
  "Offer is null: no quest_dialog offer line tagged to this quest exists. 90818 is objective text, not an offer. Giver unknown; Milford as giver is plausible but unsourced.",
  "Progress is null: no reminder line tagged to this quest was found.",
  "Reward is null: no reward line found.",
  "previous/next are empty: the chain link to Idle Hands or The Master's Components is unsourced.",
  "Collect target 'Poisonous toads' has no confirmed locale id; target_locale_id left null.",
  "Wireable is false until the offer speaker and the complete line are confirmed."
 ]}
