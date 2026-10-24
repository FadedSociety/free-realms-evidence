<!-- fleet job=dialog-infer id=wsal-monella-special-v2 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[8954, 11698, 6, 2116] model=claude-haiku-5-5 -->
# Sal Monella Special

{"quest": {"key": "Sal Monella Special", "title": "Sal Monella Special"},
 "offer": {"locale_id": 91855, "speaker": null},
 "progress": null,
 "complete": null,
 "other_lines": [
  {"locale_id": 91861, "role": "objective_hint", "speaker": "Sal Monella"},
  {"locale_id": 91859, "role": "objective_hint", "speaker": "Sal Monella"},
  {"locale_id": 91858, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'Sal Monella Special'", "source": "locale:77280 (quest_title, hint Sal Monella Special)"},
  {"claim": "91855 is the offer text: it instructs the player to grab the bowls of stew and hand them out before they get cold. It is the same text as 77281 without the opening 'Respect!' reaction line, and it is zone-tagged Mire's Edge like the other 918xx-91861 objectives of this quest", "source": "locale:91855 vs locale:77281 (verified by direct lookup)"},
  {"claim": "77281 is rejected as offer: it opens with 'Respect! That's what Sal wants', a reaction line, and has no zone tag; its body duplicates 91855", "source": "locale:77281"},
  {"claim": "Speak to Sal Monella is objective 91861, attributed to Sal Monella", "source": "locale:91861 + npc answer 'sal monella' dialog list"},
  {"claim": "Deliver Sal Monella's food before time runs out is 91859, attributed to Sal Monella; it names item Sal Monella's Special (3967)", "source": "locale:91859, locale:3967, npc answer 'sal monella'"},
  {"claim": "Deliver Sal's food to the citizens of Mire's Edge is 91858; recipients are not named", "source": "locale:91858"},
  {"claim": "Giver is Sal Monella (locale 45300), Mire's Edge / Blackspore Swamp", "source": "locale:45300; npc answer 'sal monella' (quests_given list)"},
  {"claim": "No progress, completion or reward line tagged to this quest exists in the client; 77084-77088 (Deliver the Sal Monella Special, Darci/Bart) and 6343/6344/6346 (item-description dialog) are different quests or items and are excluded", "source": "lookup of 'Sal Monella Special' in client; locale:77084, 77085, 77086, 77088"},
  {"claim": "390253 and 428708 are other quests' dialog (Fresh Ingredients, Mystery Meat Mystery) and are not bound here", "source": "locale:390253, locale:428708"}
 ],
 "confidence": 0.45,
 "open": [
  "Live status unresolved: activity 231 is missing-implementation and no source shows the quest being played.",
  "Offer speaker is null: the text speaks of Sal in third person ('Sal wants', 'Sal's got'), so it is not clearly Sal's own line, and no NPC answer attributes 91855 or 77281 to Sal. The speaker of the offer is unknown.",
  "Offer choice between 91855 and 77281 is a judgment: both carry the same instruction; 91855 chosen for zone match and absence of the 'Respect!' reaction opener. Confirm before wiring.",
  "No completion/thank-you line and no progress reminder found for this quest; complete and progress left null. The quest is not wireable as a full dialog set until one is found.",
  "No reward line found in client or wiki; reward and repeatability unknown.",
  "giver npc_id left null (9000000450 disputed in repo; NPC name id 3178725636 unverified).",
  "No quest record; previous/next line placement unknown.",
  "Recipient NPCs for 91858 and the 91859 timer value are not in the client."
 ]}
