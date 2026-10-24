<!-- fleet job=dialog-infer id=wunwanted-guests-v3 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[10008, 11252, 6, 2069] model=claude-haiku-5-5 -->
# Unwanted Guests

{"quest": {"key": "unwanted_guests", "title": "Unwanted Guests"},
 "offer": {"locale_id": 5100946, "speaker": "Kai"},
 "progress": null,
 "complete": null,
 "other_lines": [],
 "evidence": [
  {"claim": "Locale 5100946 is quest_dialog, Seaside, tagged to Unwanted Guests, with no FLAG. Its text explains the quest's premise (ghost ninjas exposed as Gloam, Kai moving to clear the Dojo), which fits an offer/explanation role.", "source": "locale:5100946 (confirmed via lookup client)"},
  {"claim": "Kai is named in 5100946 and is listed as giver of Unwanted Guests, so he is the attributed speaker. The text is third-person, so this is low-confidence.", "source": "locale:5100946; npc answer kai quests_given; wiki Kai quest list includes [Unwanted Guests]"},
  {"claim": "Title 5100945 is Seaside-tagged and sits in the quest's dialog cluster. 5101584 and 5101811 carry identical text, one untagged by zone, so the live title is not disambiguated.", "source": "locale:5100945 / 5101584 / 5101811 (confirmed via lookup client)"},
  {"claim": "No progress or completion line is tagged to Unwanted Guests. 5101585 ('Have you collected the needed ingredients?') has no zone or hint link and is not this quest's. 5100949 'Defeat the Kraken' and 5100951 'Thank you for defeating Nekark!' belong to Stop Orchid Eventide.", "source": "locale search; client cluster"},
  {"claim": "5101827 'Unwanted Guests Desc' is an unattributed placeholder-style objective and is not bound.", "source": "locale:5101827"},
  {"claim": "Wiki Heroes Journal lists [Unwanted Guests] between Not the Ghosts You're Looking For and Defeat the Kraken, so the next link is per wiki order and unverified in client data.", "source": "wiki: Heroes Journal: The Seaside Gloam Invasion"}
 ],
 "confidence": 0.35,
 "open": [
  "Offer 5100946 is third-person narration, not confirmed as spoken Kai dialog. It is not in Kai's attributed dialog list (5100938, 5100942, 417016, 419396, 101613). Speaker 'Kai' is inferred from the text and quests_given. Confirm from video or a full NPC dialog dump before wiring.",
  "Progress and complete are null: no quest-tagged line exists in the pack. Do not borrow lines from Stop Orchid Eventide or Not the Ghosts You're Looking For.",
  "No reward line found in client, wiki or repo.",
  "Quest record_id is null. Live title is ambiguous among 5100945 / 5101584 / 5101811; 5100945 chosen as Seaside-tagged.",
  "Kai's npc_id and client NPC locale id are not confirmed.",
  "Objectives unresolved: 5101827 is placeholder-style and unattributed; the prior 510186 attribution was removed.",
  "The critiques disagreed on the offer slot. This answer keeps 5100946 as a low-confidence offer, with the narration caveat stated above."
 ]}
