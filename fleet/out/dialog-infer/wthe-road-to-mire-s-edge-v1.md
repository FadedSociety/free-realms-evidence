<!-- fleet job=dialog-infer id=wthe-road-to-mire-s-edge-v1 status=done turns=3 usd=0.0021 tokens(read,write,in,out)=[13592, 7514, 8, 2037] model=claude-haiku-5-5 -->
# The Road to Mire's Edge

{"quest": {"key": "the_road_to_mires_edge", "title": "The Road to Mire's Edge"},
 "offer": {"locale_id": 78700, "speaker": null},
 "progress": null,
 "complete": null,
 "other_lines": [
  {"locale_id": 78699, "role": "objective_hint", "speaker": null},
  {"locale_id": 78702, "role": "objective_hint", "speaker": null},
  {"locale_id": 78703, "role": "followup", "speaker": null}
 ],
 "evidence": [
  {"claim": "78698 is the quest title 'The Road to Mire's Edge', tagged to this quest, unflagged.", "source": "locale:78698 / client lookup tags"},
  {"claim": "78700 is the only unflagged quest_dialog tagged to this quest; its text ('I haven't seen you around before, you must be a new arrival...') is a newcomer greeting that fits an opener/offer, not progress or completion.", "source": "locale:78700 / client tag"},
  {"claim": "78699 and 78702 are go-objectives for this quest (find/follow the trail to Mire's Edge and speak to Donovan).", "source": "locale:78699, locale:78702"},
  {"claim": "78703 'Speak to Donovan Shadeweaver' is this quest's talk objective, attributed to this quest by the Donovan NPC answer.", "source": "locale:78703 / npc answer donovan shadeweaver"},
  {"claim": "78697 is NOT used: it is tagged to zone Mire's Edge with hint Donovan, not to this quest, and it refers to Donovan in the third person ('Donovan is the guy to see'), so it is not Donovan's own line and it names no quest task of this quest.", "source": "locale:78697 / client tag"}
 ],
 "confidence": 0.35,
 "open": [
  "Offer speaker unresolved: 78700 is not attributed to any named NPC in the client text, tag hint or NPC answers, so speaker is null. The giver NPC id is unknown.",
  "No progress or complete dialog tagged to this quest was found; progress and complete are null rather than guessed.",
  "No reward lines were found for this quest.",
  "No record id or previous/next chain is established; the Donovan quest list in the wiki does not include this quest.",
  "Mire's Edge place locale id was not verified."
 ]}
