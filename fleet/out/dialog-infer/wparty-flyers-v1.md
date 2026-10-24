<!-- fleet job=dialog-infer id=wparty-flyers-v1 status=done turns=3 usd=0.0025 tokens(read,write,in,out)=[15001, 8699, 8, 2460] model=claude-haiku-5-5 -->
# Party Flyers

{"quest": {"key": "party_flyers", "title": "Party Flyers"},
 "offer": {"locale_id": 77534, "speaker": null},
 "progress": {"locale_id": 77545, "speaker": null},
 "complete": {"locale_id": 77537, "speaker": null},
 "other_lines": [
  {"locale_id": 77541, "role": "objective_hint", "speaker": null},
  {"locale_id": 77542, "role": "objective_hint", "speaker": null},
  {"locale_id": 77543, "role": "followup", "speaker": null}
 ],
 "evidence": [
  {"claim": "Offer is the flyer-cleanup request: 'We made all these pretty flyers... do you think you could help me pick up the flyers around town? Pick up that flyer next to me.'", "source": "locale:77534 (quest_dialog, tag Merry Vale | Party Flyers)"},
  {"claim": "Progress reminder asks whether the player will still help pick up the thrown flyers, starting with the one next to the speaker", "source": "locale:77545 (quest_dialog, tag Merry Vale | Party Flyers)"},
  {"claim": "Completion thanks the player for helping keep the party going", "source": "locale:77537 (quest_dialog, tag Merry Vale | Party Flyers)"},
  {"claim": "Click-the-flyer-next-to-Mayor objective step", "source": "locale:77541 (quest_objective, tag Merry Vale | Party Flyers)"},
  {"claim": "Minigame objective, then speak with the Mayor afterwards", "source": "locale:77542 and 77543 (quest_objective, tag Merry Vale | Party Flyers)"},
  {"claim": "Quest title Party Flyers", "source": "locale:77535"},
  {"claim": "Giver is Mayor McFairy (npc 9500000405, name locale 41231)", "source": "earlier quest answer; npc answer lists Party Flyers among Mayor McFairy's quests"},
  {"claim": "No reward text exists for this quest", "source": "client lookup; 77537 is completion dialog only, no quest_reward line tagged Party Flyers"}
 ],
 "confidence": 0.5,
 "open": [
  "Speaker left null on all three dialog lines: the text is first-person ('me', 'next to me') and fits Mayor McFairy, but no tag hint or NPC answer attributes these lines to him (the NPC answer's dialog list is empty), so the speaker rule forbids naming him.",
  "Live variant unsettled. Click-to-begin 77540/77541 wording, the run-around set (388236/431260) and the Interact set (431047/431048/431050) conflict. Do not enable until the live giver's variant is confirmed.",
  "Line position in any chain is unsourced; previous/next left empty.",
  "Minigame objective 77542 has no client target locale id and no collect count in any source.",
  "No reward line exists; reward left out of other_lines.",
  "Locale 77540 (click the flyer on the ground) and 76527/76528 (collect extra flyers) are other variants or a different collect step, not used as the offer/progress/complete lines.",
  "Locale 116428 was cited by an earlier critic but not re-verified; not used."
 ]}
