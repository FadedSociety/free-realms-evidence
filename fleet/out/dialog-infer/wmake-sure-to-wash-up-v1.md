<!-- fleet job=dialog-infer id=wmake-sure-to-wash-up-v1 status=done turns=4 usd=0.0029 tokens(read,write,in,out)=[22641, 9226, 10, 2971] model=claude-haiku-5-5 -->
# Make Sure to Wash up...

{"quest": {"key": "make_sure_to_wash_up", "title": "Make Sure to Wash up..."},
 "offer": null,
 "progress": null,
 "complete": {"locale_id": 90821, "speaker": "Milford"},
 "other_lines": [
  {"locale_id": 90818, "role": "objective_hint", "speaker": null},
  {"locale_id": 90827, "role": "objective_hint", "speaker": null},
  {"locale_id": 90829, "role": "objective_hint", "speaker": null},
  {"locale_id": 90832, "role": "objective_hint", "speaker": null},
  {"locale_id": 90820, "role": "other", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'Make Sure to Wash up...' (locale 90819, quest_objective, Blackspore, Milford).", "source": "locale:90819 / lookup client"},
  {"claim": "Collect objective: gather poison toad secretion from poisonous toads near water in Blackspore; text also warns to wash up afterwards.", "source": "locale:90818, 90827, 90828, 90829"},
  {"claim": "Turn-in objective: return to Milford in Blackspore.", "source": "locale:90832 (target name Milford, 45293)"},
  {"claim": "Milford is the task's description-holder per 90820: he needs alchemy components for his master Eggert.", "source": "locale:90820"},
  {"claim": "90821 ('Yes! Yes! Perfect! ... I wasn't kidding about the hands') is the only Milford line that reacts to a delivered item, so it is the best candidate for completion; attributed to Milford by its tag and by the NPC answer.", "source": "locale:90821 / npc answer milford"},
  {"claim": "90733 is the Idle Hands offer (Milford), a different quest; it is not used here.", "source": "locale:90733 / npc answer milford"}
 ],
 "confidence": 0.35,
 "open": [
  "No quest record, giver NPC, or reward exists in any source checked; quest key and giver are unknown.",
  "Offer and progress are null: no client line is tagged to this quest as an offer or reminder. 90818 reads like the request but is tagged as objective text with no speaker attribution, so it is kept as objective_hint.",
  "90821 is the weakest choice: it is tagged to Milford with no quest name, and it mentions 'the hands', which overlaps with Idle Hands (Milford's offer 90733). It is listed as complete only because it is the one Milford reaction to a delivered item. Confirm before live use.",
  "Reward is null: no reward line found (90838 belongs to the Cargug chain).",
  "Chain links (previous/next) are unconfirmed; Idle Hands and The Master's Components are not confirmed as neighbors.",
  "Collect target 'Poisonous toads' has no confirmed locale id; left in the objective text only.",
  "Previous answer's claim that Milford is Eggert's assistant was corrected to 'Milford needs components for his master Eggert' (90820)."
 ]}
