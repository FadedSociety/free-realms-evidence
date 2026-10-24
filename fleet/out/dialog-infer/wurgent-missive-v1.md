<!-- fleet job=dialog-infer id=wurgent-missive-v1 status=done turns=6 usd=0.0041 tokens(read,write,in,out)=[54623, 14314, 14, 3536] model=claude-haiku-5-5 -->
# Urgent Missive

{"quest": {"key": "gorg-urgent-missive", "title": "Urgent Missive"},
 "offer": {"locale_id": 36490, "speaker": "Gorg"},
 "progress": {"locale_id": 36491, "speaker": "Gorg"},
 "complete": {"locale_id": 9876, "speaker": "Gorg"},
 "other_lines": [
  {"locale_id": 36489, "role": "followup", "speaker": "Gorg"},
  {"locale_id": 36486, "role": "followup", "speaker": null},
  {"locale_id": 36487, "role": "followup", "speaker": null},
  {"locale_id": 36480, "role": "followup", "speaker": null},
  {"locale_id": 36439, "role": "objective_hint", "speaker": null},
  {"locale_id": 36440, "role": "objective_hint", "speaker": null},
  {"locale_id": 36495, "role": "objective_hint", "speaker": null},
  {"locale_id": 36493, "role": "objective_hint", "speaker": null},
  {"locale_id": 36441, "role": "objective_hint", "speaker": null},
  {"locale_id": 36496, "role": "objective_hint", "speaker": null},
  {"locale_id": 36497, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Completion line is Gorg's thanks for delivery: 'You delivered my Urgent Missive? Excellent! ... good soldier'", "source": "locale:9876; objective locale:36497 'Inform Gorg of your success'; npc answer gorg quests_given Urgent Missive"},
  {"claim": "Offer is Gorg explaining the missive and instructing the player to deliver the note to Snorg and Cargug (write-down / deliver this note)", "source": "locale:36490 (with 36489 'My tech-savvy brothers... how am I supposed to relay my top-secret orders'); speaker from giver tag and locale:36440 'Gorg has an Urgent Missive he must pass on'"},
  {"claim": "Progress reminder is 'Please hurry and deliver this important missive!'", "source": "locale:36491 (quest_dialog, Urgent Missive tag, Briarwood)"},
  {"claim": "36505 is a repeat-run variant of the completion line, not the base complete line", "source": "locale:36505 mentions 'keep trying to get better times at that challenge'"},
  {"claim": "36480 'You bring news from Gorg? Excellent!' is a recipient reaction (Snorg/Cargug side), not Gorg's complete line", "source": "locale:36480 text; speaker not attributed by any source, so speaker null"}
 ],
 "confidence": 0.5,
 "open": [
  "Offer (36490) and progress (36491) speakers are inferred from the giver (Gorg) and the quest's objective text; no NPC answer directly attributes these lines to Gorg. Treat as moderate confidence.",
  "36480 and 36486/36487 read as delivery-side reactions by Snorg or Sergeant Cargug, but no source names the speaker, so speaker is null and they are placed as followup rather than progress.",
  "Earlier pack had offer and progress null; this pass assigns them from the client text 36489-36491 which the earlier pass did not place. Verify against an in-game capture if available.",
  "Delivery order (Snorg and Cargug as one step or two) is unconfirmed; 36441 and 36442/36446 both kept as objective hints.",
  "Chugawug variants 36443 and 430930 are not used as required lines.",
  "Zone conflict: 36493 says Briarwood but Gorg's camp is in Bristlewood per locale:16139 and the wiki; Briarwood kept as the client-stated minigame location.",
  "Reward: no coin/item/xp reward text found; 9876 is the only payoff line (a praise line).",
  "Server npc_id and quest record id unknown; left null."
 ]}
