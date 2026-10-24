<!-- fleet job=dialog-infer id=wstoke-the-flames-v1 status=done turns=4 usd=0.0036 tokens(read,write,in,out)=[32546, 15849, 10, 2582] model=claude-haiku-5-5 -->
# Stoke the Flames

{"quest": {"key": "Stoke the Flames", "title": "Stoke the Flames"},
 "offer": {"locale_id": 72077, "speaker": "Babbina"},
 "progress": null,
 "complete": null,
 "other_lines": [
  {"locale_id": 72079, "role": "objective_hint", "speaker": null},
  {"locale_id": 72078, "role": "other", "speaker": null}
 ],
 "evidence": [
  {"claim": "72077 is the quest offer; its text is Babbina's voice ('still too scared to go out there') asking the player to stoke the flames and follow the path east to Gorg's camp", "source": "locale:72077 full text; npc answer for Babbina lists 72077 as quest_offer for Stoke the Flames"},
  {"claim": "Speaker of 72077 is Babbina", "source": "npc answer (babbina, dialog 72077 kind quest_offer); NameId 73994 = 'Babbina' confirmed by locale:73994"},
  {"claim": "72079 is the objective text 'Babbina would like you to throw coals on the braziers along the path, leading to Gorg's camp.'", "source": "locale:72079 (quest_objective, hint Stoke the Flames)"},
  {"claim": "72078 is the quest title 'Stoke the Flames'", "source": "locale:72078 (quest_title, hint Stoke the Flames)"},
  {"claim": "72080 is not Babbina's line and not a completion line: it refers to Babbina in the third person ('I was hoping Babbina would take care of that') and does not thank or pay", "source": "locale:72080 full text; npc answer labelled it 'other', not progress/complete"},
  {"claim": "Brazier lines 74569-74584 are not tied to this quest by any client hint", "source": "locale:74569-74584 (unlinked candidate steps; excluded)"},
  {"claim": "Locale 72140 is a route description, not a quest line", "source": "locale:72140"}
 ],
 "confidence": 0.6,
 "open": [
  "Liveness unconfirmed: nothing in the pack shows the quest shipped, so the whole binding is provisional.",
  "Progress left null: 72079 is tagged quest_objective and is objective text rather than an NPC reminder line. The Babbina NPC answer labels it quest_progress, but that does not make it a dialog line; no other reminder line exists for this quest.",
  "Complete left null: no thank-you or payment line for Stoke the Flames was found. 72080 does not fit (it is not Babbina's voice and does not thank). It is not listed as complete.",
  "Reward: none found in any source; other_lines carries no reward entry.",
  "Brazier steps 74569-74584 are unlinked to this quest by any hint (74569 is typed quest_title and the set is unresolved as to count), so they are excluded rather than used as objectives.",
  "The giver's NPC id 9500000089 is a reconstructed package key; the legacy source is Npcs.json Id 2586 with NameId 73994 (briarwood.json:3666-3672 per the pack). Placement is unverified. The name 'Babbina' itself is confirmed by locale:73994.",
  "Quest-line placement (previous/next) is unproven and left empty. The title 72078 and the guide key 1506001509 are not record ids; record_id is unknown."
 ]
}
