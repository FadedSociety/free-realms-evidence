<!-- fleet job=dialog-infer id=wmystery-meat-mystery-v1 status=done turns=4 usd=0.0037 tokens(read,write,in,out)=[25804, 11299, 10, 4064] model=claude-haiku-5-5 -->
# Mystery Meat Mystery

{"quest": {"key": "mystery_meat_mystery", "title": "Mystery Meat Mystery"},
 "offer": {"locale_id": 428710, "speaker": "Sal Monella"},
 "progress": {"locale_id": 428708, "speaker": "Sal Monella"},
 "complete": null,
 "other_lines": [
  {"locale_id": 428713, "role": "objective_hint", "speaker": null},
  {"locale_id": 428714, "role": "objective_hint", "speaker": null},
  {"locale_id": 428715, "role": "objective_hint", "speaker": null},
  {"locale_id": 428716, "role": "objective_hint", "speaker": null},
  {"locale_id": 428724, "role": "followup", "speaker": null},
  {"locale_id": 428720, "role": "objective_hint", "speaker": null},
  {"locale_id": 428721, "role": "objective_hint", "speaker": null},
  {"locale_id": 428726, "role": "followup", "speaker": "Sal Monella"},
  {"locale_id": 428734, "role": "followup", "speaker": "Sal Monella"},
  {"locale_id": 428732, "role": "followup", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'Mystery Meat Mystery'", "source": "locale:428709 (quest_title, Blackspore)"},
  {"claim": "Offer text explains Sal's shortage and sends the player to visit neighboring chefs; it is the only quest_dialog line tagged to the 'Sal Monella Mystery Meat' hint that reads as an offer", "source": "locale:428710"},
  {"claim": "Sal's reply directs the player to Chugilda at Briarwood; he is the mid-quest reminder speaker", "source": "locale:428708 + Sal Monella NPC answer (quest_progress for Mystery Meat Mystery)"},
  {"claim": "Chugilda objective: talk to Chugilda", "source": "locale:428714"},
  {"claim": "Nettleseed travel objective", "source": "locale:428715"},
  {"claim": "Talk to Chef Safrie objective", "source": "locale:428716; Chef Safrie NPC answer lists it"},
  {"claim": "Robgoblin girl in Sacred Grove says she took the mystery meat and tells the player to return to Sal with bad news", "source": "locale:428724 (Sacred Grove)"},
  {"claim": "Deliver-the-news objective and its description", "source": "locale:428720, locale:428721"},
  {"claim": "Sal's line about the cake being late and that the Birthday Bash people must be told", "source": "locale:428726, locale:428734 (Sal Monella hint)"},
  {"claim": "No reward text exists in the client pack for this quest", "source": "absence in client lookup; wiki Birthday Bash page gives no reward"}
 ],
 "confidence": 0.4,
 "open": [
  "Live status is unverified: the only support is wiki text saying the quest is once per character in Birthday Bash. Treat as unsure.",
  "No complete line was found. 428724 is the Sacred Grove robgoblin girl's dialog, not a payout or thanks, and 428734 and 428726 are reminders/followups, so complete is null.",
  "Offer 428710 is third-person narration naming Sal; speaker 'Sal Monella' rests on the quest-hint tag, not on the text itself. Progress 428708 is attributed to Sal by the NPC answer.",
  "Speaker is null for 428713, 428714, 428715, 428716, 428720, 428721, 428724 because they are objective text or narration, not spoken by a named NPC in the pack.",
  "428732 ('Tell Sal Monella there's a mystery meat shortage everywhere') and 428722 ('Mystery Meat? I had a little...') are unattributed; they likely belong to the chefs visited, but no NPC answer claims them, so they are listed without a speaker.",
  "428730 (Shrouded Glade, 'Like I said, I don't have any more of that stuff') likely belongs to Chef Safrie but is not claimed by her NPC answer; excluded.",
  "428711 (Bordon Cloo, 'the Birthday Bash won't be cancelled') is not tied to this quest's steps and has no speaker link; excluded.",
  "Delivery recipient is not named in the text. 'Birthday Bash people' is unresolved; Commander Kiggle (locale:428680) is a candidate only, not confirmed. Do not wire as a targetable NPC until checked.",
  "Giver name locale id is unverified; Sal Monella's NPC id 3178725636 relies on repo NPC data.",
  "Chugilda's location conflicts between sources (Nettleseed/Briarwood vs. Bristlewood); unresolved.",
  "Previous/next quest-line placement is unknown.",
  "Reward is none found."
 ]}
