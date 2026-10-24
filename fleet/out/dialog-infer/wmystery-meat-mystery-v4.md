<!-- fleet job=dialog-infer id=wmystery-meat-mystery-v4 status=done turns=4 usd=0.0038 tokens(read,write,in,out)=[38304, 15891, 10, 2933] model=claude-haiku-5-5 -->
# Mystery Meat Mystery

{"quest": {"key": "mystery_meat_mystery", "title": "Mystery Meat Mystery"},
 "offer": {"locale_id": 428708, "speaker": "Sal Monella"},
 "progress": {"locale_id": 428728, "speaker": "Sal Monella"},
 "complete": null,
 "other_lines": [
  {"locale_id": 428710, "role": "other", "speaker": null},
  {"locale_id": 428713, "role": "objective_hint", "speaker": null},
  {"locale_id": 428714, "role": "objective_hint", "speaker": null},
  {"locale_id": 428715, "role": "objective_hint", "speaker": null},
  {"locale_id": 428716, "role": "objective_hint", "speaker": null},
  {"locale_id": 428720, "role": "objective_hint", "speaker": null},
  {"locale_id": 428721, "role": "objective_hint", "speaker": null},
  {"locale_id": 428722, "role": "followup", "speaker": null},
  {"locale_id": 428724, "role": "followup", "speaker": null},
  {"locale_id": 428726, "role": "followup", "speaker": "Sal Monella"},
  {"locale_id": 428732, "role": "followup", "speaker": null},
  {"locale_id": 428734, "role": "followup", "speaker": "Sal Monella"},
  {"locale_id": 428711, "role": "other", "speaker": null},
  {"locale_id": 428719, "role": "other", "speaker": null}
 ],
 "evidence": [
  {"claim": "Title is Mystery Meat Mystery", "source": "locale:428709 (quest_title, Blackspore)"},
  {"claim": "428708 is Sal's spoken plea ('Arg! I can't find any more mystery meat... Listen, you gotta help me'), an opening request that fits an offer; Sal is the Blackspore quest giver", "source": "locale:428708 full text; Sal Monella NPC answer (places him as giver of Mystery Meat Mystery)"},
  {"claim": "428708 is tagged quest_progress in the Sal NPC answer, which conflicts with the offer reading; kept as offer on text grounds, unresolved", "source": "npc answer sal monella dialog 428708"},
  {"claim": "428728 is Sal's reminder asking whether the player has talked to Chugilda yet, fitting the in-progress state", "source": "locale:428728 full text"},
  {"claim": "428710 is third-person journal narration, not spoken dialog, so it is not the offer", "source": "locale:428710 full text"},
  {"claim": "428724 is the Sacred Grove robgoblin girl's line sending the player back to Sal; speaker is not named as a quest NPC so speaker is null", "source": "locale:428724 full text"},
  {"claim": "428722 points to Chef Safrie in Shrouded Glade; speaker is unattributed in the pack", "source": "locale:428722 full text"},
  {"claim": "428732 is an unattributed neighbor reply ('Tell Sal Monella that there's a mystery meat shortage everywhere')", "source": "locale:428732 full text"},
  {"claim": "428726 is Sal's line sending the player to tell the Birthday Bash people the cake is late; 428734 is Sal's 'deliver the news about my cake being late' reminder", "source": "locale:428726, locale:428734 full text"},
  {"claim": "428711 (Bordon Cloo cakes, Birthday Bash won't be cancelled) and 428719 (narration before delivery) are not completion lines", "source": "locale:428711, locale:428719 full text"},
  {"claim": "No completion or reward line exists in the pack for this quest", "source": "absence across locale search of 'Mystery meat', 'Birthday Bash' and the Sal dialog cluster"}
 ],
 "confidence": 0.45,
 "open": [
  "Offer 428708 conflicts with the Sal NPC answer, which tags it quest_progress. Bound as offer on text reading only; verify against the NPC's first-contact dialog before wiring.",
  "Progress 428728 is the only Sal reminder that fits the in-progress state; 428734 is also a reminder but about the delivery step, so it is listed as followup rather than progress.",
  "Complete is null: no line thanks the player or pays out, and 428711/428719 are narration. The delivery recipient ('Birthday Bash people') is unnamed; Commander Kiggle (428680/428681) is only a candidate and is not confirmed, so the completion speaker cannot be set.",
  "Speaker for 428722, 428724 and 428732 is not named by any source; left null.",
  "Quest record does not exist in the pack (record_id omitted); objective order is inferred from dialog. Giver name locale id unverified. Chugilda's location conflicts (Nettleseed/Briarwood vs Bristlewood).",
  "Live status is wiki-only (Birthday Bash event) and unverified; previous/next quest-line placement unknown; no reward text found."
 ]}
