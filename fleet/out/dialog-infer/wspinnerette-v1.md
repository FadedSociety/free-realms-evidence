<!-- fleet job=dialog-infer id=wspinnerette-v1 status=done turns=3 usd=0.0031 tokens(read,write,in,out)=[15784, 9016, 8, 3689] model=claude-haiku-5-5 -->
# Find Spinnerette

{"quest": {"key": "find_spinnerette", "title": "Find Spinnerette"},
 "offer": {"locale_id": 16129, "speaker": "Gorg"},
 "progress": {"locale_id": 101789, "speaker": "Gorg"},
 "complete": {"locale_id": 16140, "speaker": "Gorg"},
 "other_lines": [
  {"locale_id": 16121, "role": "objective_hint", "speaker": null},
  {"locale_id": 16126, "role": "objective_hint", "speaker": null},
  {"locale_id": 16128, "role": "objective_hint", "speaker": null},
  {"locale_id": 16138, "role": "objective_hint", "speaker": null},
  {"locale_id": 16139, "role": "objective_hint", "speaker": null},
  {"locale_id": 16132, "role": "other", "speaker": null},
  {"locale_id": 16134, "role": "other", "speaker": null}
 ],
 "evidence": [
  {"claim": "Offer: Gorg asks player to dispatch Spinnerette and return when done", "source": "locale:16129 (quest_dialog, hint Gorg, FLAG none)"},
  {"claim": "Complete: Gorg asks if Spinnerette is gotten rid of and thanks player", "source": "locale:16140 (quest_dialog, hint 'Find Spinnerette | Return to Gorg')"},
  {"claim": "Progress: reminder to track down Spinnerette, same laundry excuse as Gorg's offer", "source": "locale:101789 (unattributed, matched to Gorg by the 'laundry' line in 16129; inference)"},
  {"claim": "Objectives: find Spinnerette in Bristlewood, then return to Gorg", "source": "locale:16121, 16126, 16128, 16139 (quest_objective)"},
  {"claim": "Title", "source": "locale:16127"},
  {"claim": "16132 and 16134 are combat/taunt speech from the target, not clearly Gorg's offer, progress or completion lines", "source": "locale:16132, 16134 (hint Gorg, speaker not named)"},
  {"claim": "Spinnerette is named as the target but her own quest dialog belongs to Untamed Spirit, not this quest", "source": "locale:23167, 23168, 36412, 36413, 37612"}
 ],
 "confidence": 0.6,
 "open": [
  "Progress speaker is inferred: 101789 has no speaker tag; attribution to Gorg rests on its laundry line matching 16129. Also 24895 is a similar unattributed nag line (speaker unknown) and was not chosen.",
  "16132 and 16134 are tagged to this quest but read like the target's combat speech; their speaker is not named, so they are left out of the progress/complete slots.",
  "The defeat step has no client line of its own; a builder must confirm whether combat is required.",
  "No reward line exists in client; rewards are none.",
  "Previous pass mislabeled 16121 and 16139 as quest_progress dialog; they are quest_objective lines, moved to objective hints here.",
  "Previous/next links unconfirmed; Untamed Spirit is a separate follow-on about Spinnerette's son, not linked by client text.",
  "Location conflict: 16139 says northern Bristlewood for Gorg's camp; 16121/16128 say southern Bristlewood for Spinnerette."
 ]}
