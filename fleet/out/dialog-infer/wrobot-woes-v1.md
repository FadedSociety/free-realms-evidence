<!-- fleet job=dialog-infer id=wrobot-woes-v1 status=done turns=4 usd=0.0030 tokens(read,write,in,out)=[29476, 11061, 10, 2600] model=claude-haiku-5-5 -->
# Robot Woes

{"quest": {"key": "robot_woes", "title": "Robot Woes"},
 "offer": {"locale_id": 29643, "speaker": "Rizzle"},
 "progress": {"locale_id": 439855, "speaker": "Rizzle"},
 "complete": {"locale_id": 29644, "speaker": "Rizzle"},
 "other_lines": [
  {"locale_id": 29641, "role": "other", "speaker": null},
  {"locale_id": 29642, "role": "followup", "speaker": "Rizzle"},
  {"locale_id": 439856, "role": "objective_hint", "speaker": null},
  {"locale_id": 439858, "role": "objective_hint", "speaker": null},
  {"locale_id": 440487, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'Robot Woes'", "source": "locale:29641 (quest_title, hint Robot Woes)"},
  {"claim": "Offer: player is asked to fix up the Broken Robot Guards; text is in Rizzle's voice ('I'm right in the middle of a nap') and tagged to Robot Woes", "source": "locale:29643 (quest_dialog, hint Robot Woes, no FLAG)"},
  {"claim": "Progress reminder 'Rizzle wants you to fix his Broken Robot Guards in Sunstone Valley' is tagged quest_dialog to Robot Woes, names Rizzle, and the Rizzle NPC answer attributes it as quest_progress for Robot Woes", "source": "locale:439855 / npc answer rizzle"},
  {"claim": "Complete: Rizzle thanks the player for fixing the robots and offers a reward", "source": "locale:29644 (quest_reward, speaker Rizzle, no FLAG); Rizzle NPC answer lists 29644 as quest_complete"},
  {"claim": "Background/story line on Rizzle's promotion and the robot guards; Rizzle NPC answer lists it as quest_offer for Robot Woes", "source": "locale:29642 / npc answer rizzle"},
  {"claim": "Objective texts: 'Fix Broken Robot Guards' and 'Return to Rizzle'; target 'Broken Robot Guard'", "source": "locale:439856, 439858, 440487"},
  {"claim": "Quest giver is Rizzle", "source": "locale:440140 via quest answer; npc answer rizzle"}
 ],
 "confidence": 0.6,
 "open": [
  "Reward is unresolved: 29644 names no item or coin amount and trails off ('Uh...'); wiki says 'Mystery Reward' only. No reward id is set, so reward stays null.",
  "Objective count of 4 is wiki-only; no client string gives the number, so it is not used here.",
  "Repeatability is unverified in the client and not stated.",
  "Speaker for 29643 is inferred from its first-person text (the napping robgoblin is Rizzle) and quest tag; no NPC answer attributes it directly.",
  "29643 is used as the offer although the NPC answer lists 29642 as the offer; 29642 is kept as a followup/story line. Builder should confirm which slot the NPC uses.",
  "Objective kind 'use' for fixing the guards is unconfirmed (interact on the guard object vs NPC).",
  "Rizzle npc_id is not confirmed in our record set; left out of this result.",
  "No separate in-progress dialog line beyond 439855 was found; 439855 is used as progress."
 ]}
