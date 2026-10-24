<!-- fleet job=dialog-infer id=wfriend-or-foe-the-savage-v1 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[9689, 10422, 6, 1724] model=claude-haiku-5-5 -->
# Friend or Foe: The Savage

{"quest": {"key": "friend_or_foe_the_savage", "title": "Friend or Foe: The Savage"},
 "offer": null,
 "progress": null,
 "complete": {"locale_id": 438886, "speaker": null},
 "other_lines": [
  {"locale_id": 438885, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'Friend or Foe: The Savage', Sunstone Valley, quest_title type", "source": "locale:438884"},
  {"claim": "438886 is tagged quest_dialog to this quest, not FLAGged, and reads as a thank-you/payoff ('Good job! Their help will be invaluable') after the Manguanas were recruited, which matches the complete slot", "source": "locale:438886 (lookup confirmed tag and text)"},
  {"claim": "438885 is the quest's objective text (enlist the other inhabitants, starting with the Sandscale Leader); it is an objective, not an offer dialog", "source": "locale:438885 (quest_objective)"},
  {"claim": "Giver Dorn Geargrinder is attributed to the quest only by the NPC answer/wiki; no client line ties a Dorn dialog to this quest", "source": "npc answer dorn geargrinder (quests_given list)"},
  {"claim": "Headmaster Merk is named as the one who suggested enlisting help, but that is in the 438885 objective text, not in a speaker-attributed dialog line", "source": "locale:438885 text; npc answer headmaster merk"}
 ],
 "confidence": 0.5,
 "open": [
  "No quest record exists in the repo; quest key is derived from the title.",
  "Offer slot is null: no quest_dialog line offering this quest was found. 438885 is an objective line, and using it as an offer would break the offer/objective type split.",
  "Progress slot is null: no client reminder line for this quest was found.",
  "Complete speaker is null: 438886 carries no speaker name in its text, tag hint or NPC answer. Dorn and Merk are plausible but unattributed, so neither is set.",
  "Other objectives (talk to Peace-guana Joe, defeat 10 Skullz in Sandscale Territory, return to Joe, talk to Merk, return to Merk) have no client lines tied to this quest. Left unlinked. 439128/439130/439132 were not re-verified and are not attributed here.",
  "Sandscale Leader target is unresolved. The client names no NPC for it, and linking it to Peace-guana Joe is not client-confirmed.",
  "Giver npc_id and locale are null: Dorn's client name locales are not confirmed for this quest.",
  "Reward: Mini-Manguana is wiki-only with no client reward line. Not wired as live.",
  "Critiques: the pack carried no separate critique list, so none were applied beyond the checks above."
 ]}
