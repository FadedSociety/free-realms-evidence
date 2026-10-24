<!-- fleet job=dialog-infer id=wglide-training-confidence-is-key-v1 status=done turns=3 usd=0.0027 tokens(read,write,in,out)=[16954, 9559, 8, 2713] model=claude-haiku-5-5 -->
# Glide Training: Confidence Is Key

{"quest": {"key": "Glide Training: Confidence Is Key", "title": "Glide Training: Confidence Is Key"},
 "offer": null,
 "progress": null,
 "complete": {"locale_id": 4419690, "speaker": null},
 "other_lines": [
  {"locale_id": 4419687, "role": "objective_hint", "speaker": null},
  {"locale_id": 4419725, "role": "objective_hint", "speaker": null},
  {"locale_id": 441975, "role": "reward", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 4419688 'Glide Training: Confidence Is Key' (quest_title, Snowhill).", "source": "locale:4419688 / client_lines_tagged_to_quest"},
  {"claim": "Complete line is 4419690: 'Good job! Your ride's confidence has been magically transferred to the Training Saddle... Come back tomorrow and we can continue the training!' It is the only quest_dialog line tagged to this quest, and it is not a title or objective.", "source": "locale:4419690 (verified by direct lookup)"},
  {"claim": "Long objective text 4419687 tells the player to jump through the fiery hoop above the Snowhill launch pad while riding the untrained glide-trainable ride.", "source": "locale:4419687 (verified)"},
  {"claim": "Short objective target 4419725 'Bounce through the Snowhill hoop' is an unflagged client line, but it belongs to the step-named set (4419703 family); listed as an alternate hint, not paired with 4419687.", "source": "locale:4419725 (verified)"},
  {"claim": "Reward item is Proof of Training - Part 3 of 5, a ticket with no effect, per wiki; the client name line 441975 matches.", "source": "locale:441975 (verified); wiki:Proof of Training - Part 3 of 5"},
  {"claim": "Giver and returning NPC is Troy Ridewrangler (name id 440997), located near the Seaside Warpstone per wiki.", "source": "locale:440997 (verified); wiki:Quest:Glide Training: Confidence Is Key; npc answer troy ridewrangler"},
  {"claim": "Troy's NPC answer lists quest dialog 4419688 and 4419690 is not among its attributed lines; no npc answer attributes 4419690 to any speaker.", "source": "npc answer troy ridewrangler"}
 ],
 "confidence": 0.5,
 "open": [
  "Offer and progress lines not identified: no quest_dialog line tagged to this quest besides 4419690. 4419689 ('Troy Ridewrangler in Seaside has asked me to...') is an objective-typed line and not used as an offer.",
  "Complete speaker left null: 4419690 names no speaker and no NPC answer attributes it. Troy is the quest's giver and return NPC per wiki, so Troy is the likely speaker, but the rules require attribution.",
  "Start objective ('Speak with Troy Ridewrangler near the Seaside Warpstone') is wiki-only; no client line for this quest. 4419677 belongs to Seaside Ride Training. Troy's location is unreconciled: wiki says Warpstone, 441985 says ride stable, 4419712 says ride corral.",
  "Return objective: 4419711 is quest_title-typed for 'Return to Troy Ridewrangler' and belongs to a different quest record, so it is not wired as this quest's objective. 4419712 is that record's progress line.",
  "Objective text set choice: 4419687 (long, step-set family) vs 4419725 (short, step-named family). Builder must pick one set; both are unflagged.",
  "Quest record id does not exist in the repo; a new record must be created. Repo citation of title 2253772618 does not match 4419688 and is unresolved.",
  "Coin reward not found in client lines. npc_id for Troy not confirmed in repo.",
  "Live status is 'unsure' in the earlier pass; this is a quest in the Glide Training series, which the wiki describes as offered by Troy, so it is likely live but unverified."
 ]}
