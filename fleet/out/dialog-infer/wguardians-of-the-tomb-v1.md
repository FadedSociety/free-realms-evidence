<!-- fleet job=dialog-infer id=wguardians-of-the-tomb-v1 status=done turns=4 usd=0.0036 tokens(read,write,in,out)=[27715, 12449, 10, 3599] model=claude-haiku-5-5 -->
# Guardians of the Tomb

{"quest": {"key": "guardians-of-the-tomb", "title": "Guardians of the Tomb"},
 "offer": {"locale_id": 415330, "speaker": null},
 "progress": null,
 "complete": {"locale_id": 415333, "speaker": null},
 "other_lines": [
  {"locale_id": 415332, "role": "objective_hint", "speaker": "Lord William IV"},
  {"locale_id": 416044, "role": "objective_hint", "speaker": "Lord William IV"},
  {"locale_id": 416093, "role": "objective_hint", "speaker": "Lord William IV"},
  {"locale_id": 416067, "role": "objective_hint", "speaker": null},
  {"locale_id": 416060, "role": "other", "speaker": "Spectral Guardian"}
 ],
 "evidence": [
  {"claim": "Quest title is 'Guardians of the Tomb'", "source": "locale:415331 (quest_title, Blackspore)"},
  {"claim": "Offer text explains the Pumpkin Prince threat and the need for spectral guardians; it is quest_dialog tagged to this quest", "source": "locale:415330 (quest_dialog, Blackspore, Guardians of the Tomb)"},
  {"claim": "Completion-style line ('Your heroics will be remembered') tagged to this quest", "source": "locale:415333 (quest_dialog, Blackspore, Guardians of the Tomb)"},
  {"claim": "415332 is the quest objective text, not an offer dialog line; the NPC answer's 'quest_offer' label for it is wrong", "source": "locale:415332 is type quest_objective"},
  {"claim": "Objectives: speak to Lord William IV, find 7 spectral guardians, return to Lord William IV", "source": "locale:416044, 416093, 415332, 416067, 416069-416081"},
  {"claim": "Lord William IV is the giver; 416046 is his name", "source": "locale:416046 and NPC answer (Blackspore POI 16)"},
  {"claim": "416060 'Why have you disturbed me?' is attributed to Spectral Guardian by the NPC answer, but it is a generic greeting with no quest-specific content", "source": "locale:416060 via npc_answers spectral guardian"},
  {"claim": "Spectral guardian objective line 416067 names the target NPC", "source": "locale:416067 'Spectral Guardian'"}
 ],
 "confidence": 0.35,
 "open": [
  "Offer 415330 has no NPC attribution in the pack and its text does not name a speaker; speaker left null rather than guessed (Lord William IV is the giver by objective data, but he is not attributed to this line).",
  "Complete 415333 ('Do you have all the signets?...') is tagged to the quest but no NPC answer attributes it and the text names no speaker; speaker left null. Its wording reads as a check-in and thank-you, so it is used as complete only because it is the sole remaining tagged dialog.",
  "No progress dialog line is tagged to this quest. 416044 and 416093 are objective texts ('Speak to...', 'Return to...'), not spoken dialog, so progress is left null and they are listed as objective_hint.",
  "The pack's NPC answer labelled 415332 as the quest_offer; the locale shows it is a quest_objective, so it is not used as the offer.",
  "416060 'Why have you disturbed me?' is attributed to the Spectral Guardian by the agent but is generic; it is listed only as 'other' and should not be used as a quest line without confirmation.",
  "No reward line found; rewards are empty. The pack's previous/next chain (A Ghostly Discovery -> Guardians of the Tomb -> Sealed with a Signet) is not verified here.",
  "No quest record or NPC id exists in the data; quest key is derived from the title.",
  "The guardian count of 7 comes from the seven per-zone objective lines (416069-416081); whether all seven are required is unconfirmed."
 ]}
