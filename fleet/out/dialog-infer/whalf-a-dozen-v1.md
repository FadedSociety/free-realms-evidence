<!-- fleet job=dialog-infer id=whalf-a-dozen-v1 status=done turns=3 usd=0.0022 tokens(read,write,in,out)=[13797, 8437, 8, 2084] model=claude-haiku-5-5 -->
# Half a Dozen

{"quest": {"key": "Half a Dozen", "title": "Half a Dozen"},
 "offer": {"locale_id": 103043, "speaker": "Tozer"},
 "progress": {"locale_id": 103047, "speaker": null},
 "complete": null,
 "other_lines": [
  {"locale_id": 103040, "role": "objective_hint", "speaker": null},
  {"locale_id": 103045, "role": "objective_hint", "speaker": null},
  {"locale_id": 103041, "role": "objective_hint", "speaker": null},
  {"locale_id": 103042, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Offer text: 'I am really enjoying the view here at Seaside... Would you be willing to take it for me?' is the quest offer, and it is the only quest dialog Tozer is attributed with.", "source": "locale:103043 (full text confirmed via locale lookup); npc answer tozer dialog [103043 quest_offer]; wiki Quest:Half a Dozen 'Speak with Tozer located near the Seaside Information Center'"},
  {"claim": "Progress reminder 'Have you sent the picture yet? You can get it taken care of at the post office here in Seaside.' fits an in-progress reminder.", "source": "locale:103047 (tagged Seaside, hint 'Take the picture to the post office')"},
  {"claim": "No NPC is attributed to 103047: the tag hint is an objective title, not a speaker, and Tozer's answer lists only 103043.", "source": "npc answers tozer / tag hint"},
  {"claim": "Enve LeStamp is the hand-off target (postman at Seaside Post Office); 103041 and 103042 are objective text naming him.", "source": "locale:117342 npc_name; locale:103041; locale:103042; wiki Enve LeStamp"},
  {"claim": "No client line tagged to Half a Dozen states completion or thanks, so complete is null.", "source": "client_lines_tagged_to_quest scan; lookup 'Enve LeStamp' and 'picture' returned no completion line"},
  {"claim": "Excluded 117305, 388037, 387936 and 130190: they belong to the Postman quests, not this one.", "source": "npc answer enve lestamp quest tags"}
 ],
 "confidence": 0.7,
 "open": [
  "Offer speaker Tozer is supported by the NPC answer and the wiki start step, but no nameplate-to-line binding is confirmed in the client data.",
  "Progress 103047 has no named speaker, so speaker is null. A builder may attach it to Tozer, but that is not established by the sources.",
  "Complete is null: no client completion or thanks line is tagged to this quest. The wiki says the quest ends at Enve LeStamp, but no line for that hand-off was found.",
  "Reward of 15 coins is wiki-only (quest2 coin amount) and not found in a client reward table, so it is not included as a reward line.",
  "giver npc_id is unresolved; only the name hash is known from the repo.",
  "previous and next quest chain is unknown."
 ]}
