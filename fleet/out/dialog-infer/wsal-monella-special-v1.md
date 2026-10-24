<!-- fleet job=dialog-infer id=wsal-monella-special-v1 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[6750, 8108, 6, 2256] model=claude-haiku-5-5 -->
# Sal Monella Special

{"quest": {"key": "Sal Monella Special", "title": "Sal Monella Special"},
 "offer": {"locale_id": 77281, "speaker": null},
 "progress": null,
 "complete": null,
 "other_lines": [
  {"locale_id": 91861, "role": "objective_hint", "speaker": "Sal Monella"},
  {"locale_id": 91859, "role": "objective_hint", "speaker": "Sal Monella"},
  {"locale_id": 91858, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'Sal Monella Special'", "source": "locale:77280 (quest_title, tagged to Sal Monella Special)"},
  {"claim": "77281 is the offer-style text: it tells the player to grab the bowls of stew and hand them out before they get cold, which is an instruction/explanation fitting an offer", "source": "locale:77281 full text (tagged hint Sal Monella Special)"},
  {"claim": "91855 has the same text as 77281 but is zone-tagged Mire's Edge; kept 77281 as the offer because the pack chose it and it carries the quest hint tag, but 91855 is a credible alternate id", "source": "locale:91855 vs locale:77281"},
  {"claim": "Speak to Sal Monella objective is 91861, attributed to Sal Monella", "source": "locale:91861 + npc answer 'sal monella' dialog list"},
  {"claim": "Deliver Sal Monella's food before time runs out objective is 91859, attributed to Sal Monella; target item is Sal Monella's Special", "source": "locale:91859 + npc answer 'sal monella'; locale:3967 item name"},
  {"claim": "Deliver Sal's food to the citizens of Mire's Edge objective is 91858; recipients not named in text", "source": "locale:91858"},
  {"claim": "Giver is Sal Monella (locale 45300); NPC answer lists Sal Monella at Mire's Edge (Donovan's camp) as giver of this quest", "source": "locale:45300 / npc answer 'sal monella'"},
  {"claim": "No progress, completion or reward dialog for this quest exists in client text", "source": "client lookup for 'Sal Monella Special' returned only offer and objective lines for this hint; locale:6343/6344/6346 are item-description dialog, not this quest"}
 ],
 "confidence": 0.4,
 "open": [
  "Live status unresolved: activity 231 is missing-implementation, no source shows the quest being played; treat as unverified.",
  "Offer speaker left null: 77281 refers to Sal in third person ('Sal wants', 'Sal's got'), so it is not clearly Sal's line, and no NPC answer attributes it to Sal. Giver is Sal per locale 45300, but that does not attribute this text.",
  "Offer id ambiguity: 91855 has identical text tagged to Mire's Edge; choice between 77281 and 91855 is not settled by source.",
  "Progress and complete slots are null: no client line for this hint reads as a reminder or thank-you/payment.",
  "No reward line found; reward and repeatability unknown.",
  "giver npc_id left null (9000000450 disputed; NPC name id 3178725636 unverified).",
  "No quest record exists; previous/next line placement unknown.",
  "Recipient NPCs for 91858 and the 91859 timer value are not in the client."
 ]}
