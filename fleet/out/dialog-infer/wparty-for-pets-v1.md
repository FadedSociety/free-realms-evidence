<!-- fleet job=dialog-infer id=wparty-for-pets-v1 status=done turns=3 usd=0.0029 tokens(read,write,in,out)=[15294, 8579, 8, 3287] model=claude-haiku-5-5 -->
# Party for Pets

{"quest": {"key": "Party for Pets", "title": "Party for Pets"},
 "offer": {"locale_id": 422868, "speaker": "Tiger the Party Animal"},
 "progress": {"locale_id": 422847, "speaker": null},
 "complete": {"locale_id": 422871, "speaker": "Tiger the Party Animal"},
 "other_lines": [
  {"locale_id": 422870, "role": "objective_hint", "speaker": "Tiger the Party Animal"},
  {"locale_id": 422880, "role": "objective_hint", "speaker": "Tiger the Party Animal"},
  {"locale_id": 4549, "role": "reward", "speaker": null}
 ],
 "evidence": [
  {"claim": "Offer text 422868 is tagged Party for Pets (quest_dialog, Seaside) and offers a party favor for bringing a pet; it is the offer line.", "source": "locale:422868; client tag"},
  {"claim": "Complete text 422871 is tagged Party for Pets (quest_dialog) and thanks the player and pays a party favor.", "source": "locale:422871; client tag"},
  {"claim": "Progress reminder 422847 is tagged Party for Pets (npc_dialog) and tells a player without a pet to come back with one; it fits an in-progress reminder.", "source": "locale:422847; client tag"},
  {"claim": "Tiger the Party Animal is the giver and speaker of the Party for Pets dialog: the NPC answer attributes objective lines 422870 and 422880 to him, and the sibling A Luau lines use the same 'I'll give you a party favor' voice.", "source": "npc answer (Tiger the Party Animal); locale:422864, 422849 for voice comparison"},
  {"claim": "Reward is the item Pet Party Favor; no quantity is sourced.", "source": "locale:4549; wiki Quest:Party for Pets"},
  {"claim": "Title is locale 422869 'Party for Pets'.", "source": "locale:422869"}
 ],
 "confidence": 0.6,
 "open": [
  "Live status unsure: no source confirms Pet Party events ran on the live server. Zone Seaside is from client zone tags; the wiki's Blackspore Swamp conflicts and is unconfirmed.",
  "No quest record exists, so no record_id or npc_id. Repo title id 2169798560 conflicts with client 422869; client id used. Tiger's name id 2807361043 in repo is not a locale id.",
  "Offer 422868 and complete 422871 are tagged to the quest but no NPC answer lists them under Tiger; Tiger is assigned from the quest giver and the 'I'll give you a party favor' voice. Moderate confidence.",
  "Progress 422847 is a pet-refusal reminder with no speaker named in its text or tag; speaker left null. Using it as progress is an inference, not confirmed.",
  "422845 is a near-duplicate of the complete line (npc_dialog, same text with no trailing space); not used as a separate slot.",
  "422877 'Speak to Tiger' is tagged to the Obtain a pet quest title, not this quest, so excluded. 422881 is a quest title for Obtain a pet, excluded. 422865/422864 belong to A Luau, excluded.",
  "The third objective (speak to Tiger during a Pet Party for the reward) and the 'Summon a Pet' step have no client locale id; they come from the wiki only and are not in other_lines.",
  "Reward quantity and any coin amount are not sourced.",
  "Quest ordering (previous/next) is not established; Winter Party is a possible sibling but unverified."
 ]}
