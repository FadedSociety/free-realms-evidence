<!-- fleet job=dialog-infer id=wunwanted-guests-v4 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[20372, 11066, 8, 2470] model=claude-haiku-5-5 -->
# Unwanted Guests

{"quest": {"key": "unwanted_guests", "title": "Unwanted Guests"},
 "offer": {"locale_id": 5100946, "speaker": "Kai"},
 "progress": null,
 "complete": null,
 "other_lines": [],
 "evidence": [
  {"claim": "Locale 5100946 is an unflagged quest_dialog tagged Seaside / Unwanted Guests, and it explains the quest premise (ghost ninjas exposed as Gloam, Kai moving to clear the Dojo), which fits an offer role.", "source": "locale:5100946 (lookup client, re-confirmed)"},
  {"claim": "Kai is named in the text of 5100946 and is listed as giver of Unwanted Guests in the NPC answer, so he is the speaker by the text/NPC-answer rule.", "source": "locale:5100946; npc answer kai quests_given"},
  {"claim": "The text is third-person narration ('Kai is ready to...'), not clearly spoken dialog. Kai's attributed dialog lines (5100938, 5100942) are objective-style and not in the offer slot, so the offer binding is low-confidence.", "source": "locale:5100946; npc answer kai dialog list"},
  {"claim": "Title 5100945 is Seaside-tagged; 5101584 and 5101811 have identical text, one with no zone tag. 5100945 chosen as the working title.", "source": "locale:5100945 / 5101584 / 5101811"},
  {"claim": "No progress or completion line is tagged to Unwanted Guests in the pack. 5100949 'Defeat the Kraken', 5100950 and 5100951 belong to Stop Orchid Eventide and are not used.", "source": "locale search; client cluster"},
  {"claim": "5101585 'Have you collected the needed ingredients?' has no zone or hint link and is not attributed to this quest, so it is excluded.", "source": "locale:5101585"},
  {"claim": "5101827 'Unwanted Guests Desc' is tagged to this quest but its text is a label, not an objective sentence, so it is not bound as an objective.", "source": "locale:5101827"},
  {"claim": "Wiki Heroes Journal lists [Unwanted Guests] between Not the Ghosts You're Looking For and Defeat the Kraken, but no reward line was found for this quest.", "source": "wiki: Heroes Journal: The Seaside Gloam Invasion"}
 ],
 "confidence": 0.35,
 "open": [
  "Offer 5100946 is third-person summary text naming Kai. Bound per the speaker rule, but it may be a journal/summary entry rather than a spoken NPC line. Verify with a full Kai dialog dump before wiring.",
  "Progress and complete are null: no line in the pack is tagged to Unwanted Guests for those roles. Do not borrow from Stop Orchid Eventide or Not the Ghosts You're Looking For.",
  "No reward line found in client, wiki or repo.",
  "Quest record_id is null. Live title is ambiguous among 5100945 / 5101584 / 5101811 (identical text); 5100945 chosen as the Seaside-tagged one.",
  "Kai's npc_id and client NPC locale id are not confirmed.",
  "No objective bound: 5101827 is a label-style placeholder and 5101585 is untagged; the previous 510186 attribution was dropped.",
  "Previous-link 'Not the Ghosts You're Looking For' and next-link 'Defeat the Kraken' come from wiki order only; the client does not confirm them as quest links."
 ]}
