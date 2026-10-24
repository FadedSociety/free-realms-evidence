<!-- fleet job=dialog-infer id=wgrave-blossoms-v1 status=done turns=4 usd=0.0027 tokens(read,write,in,out)=[20888, 8635, 10, 2770] model=claude-haiku-5-5 -->
# Grave Blossoms

{"quest": {"key": "Grave Blossoms", "title": "Grave Blossoms"},
 "offer": {"locale_id": 93874, "speaker": null},
 "progress": null,
 "complete": {"locale_id": 93877, "speaker": null},
 "other_lines": [
  {"locale_id": 93879, "role": "objective_hint", "speaker": null},
  {"locale_id": 93880, "role": "objective_hint", "speaker": null},
  {"locale_id": 93881, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "93874 is the offer: it asks 'Are you interested?' about grave blossom, tagged quest_dialog to Blackspore / Grave Blossoms.", "source": "locale:93874 / client tag"},
  {"claim": "93877 is the completion/thanks line: 'Ah, you have the smell of the grave about you! ... these are perfect', tagged quest_dialog to Grave Blossoms.", "source": "locale:93877 / client tag"},
  {"claim": "93875 is the quest title 'Grave Blossoms'.", "source": "locale:93875"},
  {"claim": "93879 and 93880 are the go/collect objectives; 93881 is a hint about where the plant grows ('These tend to grow around fresh graves'), tagged to this quest.", "source": "locale:93879, 93880, 93881"},
  {"claim": "No progress line is tagged to Grave Blossoms. Milford's 90821 ('Yes! Yes! Perfect!... take care of that [hands]') concerns the Idle Hands chain, not this quest, so it is rejected as progress.", "source": "locale:90821 / npc_answers.milford"},
  {"claim": "Milford is the giver per the earlier pass and the Milford NPC answer lists Grave Blossoms among quests_given, but no source attributes 93874 or 93877 to him by name or speaker link.", "source": "npc_answers.milford (quests_given only)"},
  {"claim": "Locale 94006 is an npc_name ('Grave Blossom'), and 435658 is a different quest's objective ('He Told You So'); neither is dialog for this quest.", "source": "locale:94006 / locale:435658"},
  {"claim": "No reward line exists in the pack for this quest.", "source": "absence in pack"}
 ],
 "confidence": 0.6,
 "open": [
  "Speakers for offer 93874 and complete 93877 are null: the text names no speaker, and the only Milford link is the repo quest_giver role, which the rules do not accept as attribution. If the builder accepts the giver role, Milford is the likely speaker.",
  "No progress line is tagged to this quest; progress is null rather than guessed.",
  "93877 says 'I have one last thing I need help with', which points to the next step (purple toads, locale 90827). It is still the completion line for this quest, since it thanks the player for the samples.",
  "Reward not in evidence. Collect count not in evidence.",
  "Previous/next chain and the Milford return step (repo ID 3383934881, no located client title) are unverified and are not part of the dialog slots.",
  "The earlier pass's wiki 'mentioned' claim was dropped, as its critique asked."
 ]}
