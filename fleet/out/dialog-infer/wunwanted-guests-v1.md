<!-- fleet job=dialog-infer id=wunwanted-guests-v1 status=done turns=3 usd=0.0024 tokens(read,write,in,out)=[14759, 8842, 8, 2218] model=claude-haiku-5-5 -->
# Unwanted Guests

{"quest": {"key": "unwanted_guests", "title": "Unwanted Guests"},
 "offer": {"locale_id": 5100946, "speaker": "Kai"},
 "progress": null,
 "complete": null,
 "other_lines": [],
 "evidence": [
  {"claim": "5100946 is the only quest_dialog tagged to Unwanted Guests (Seaside) and explains the quest's purpose (remove the Gloam from the Dojo, end Orchid Eventide's grab for power), which fits an offer role.", "source": "locale:5100946"},
  {"claim": "Speaker Kai is named in the text ('Kai is ready to...') and Kai is the giver in the earlier pass; the line is phrased as a narrative summary, not first-person speech, so the speaker attribution is inferred.", "source": "locale:5100946 / npc answer kai (quests_given includes Unwanted Guests)"},
  {"claim": "Kai's NPC dialog list does not include 5100946; his attributed lines are 5100938 and 5100942 (other quests).", "source": "npc answer kai"},
  {"claim": "Title 5100945 is the Seaside-tagged title and matches the dialog's quest; 5101584 and 5101811 are duplicate titles with no zone/hint match to the dialog.", "source": "locale:5100945 / 5101584 / 5101811"},
  {"claim": "Wiki page lists 'Defeat the Kraken' as the next step, matching objective locale 5100949 (tagged Stop Orchid Eventide, not this quest).", "source": "wiki: Heroes Journal: The Seaside Gloam Invasion; locale:5100949"},
  {"claim": "No progress or complete dialog is tagged to Unwanted Guests; 5101409 mentions a pants reward but describes the Cray Pearls/Nekark outcome, not this quest.", "source": "locale:5101409 (not attributed)"}
 ],
 "confidence": 0.4,
 "open": [
  "Offer 5100946 is inferred: it is the only quest-tagged dialog and reads as an explanation, but it is not in Kai's attributed dialog list, so the offer role and Kai as speaker are unconfirmed.",
  "Progress and complete lines: none found tagged to Unwanted Guests. Left null rather than borrowing lines from Stop Orchid Eventide or Not the Ghosts You're Looking For.",
  "Objective: 5101827 ('Unwanted Guests Desc') is the only quest-tagged objective, but its text is only the title plus 'Desc' (placeholder-like). 510186 is tagged to Dojo and is not used. No usable objective line is confirmed.",
  "Title ambiguity: 5100945, 5101584 and 5101811 all read 'Unwanted Guests'. Chose 5100945 (Seaside-tagged, matches the dialog). The live title is not confirmed.",
  "Reward: none attributed to this quest. The pants reward text 5101409 is not tied to it.",
  "Kai's npc_id and locale id are not confirmed in the pack; the earlier pass's record_id is null."
 ]}
