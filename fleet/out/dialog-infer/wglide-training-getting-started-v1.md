<!-- fleet job=dialog-infer id=wglide-training-getting-started-v1 status=done turns=3 usd=0.0031 tokens(read,write,in,out)=[16121, 9342, 8, 3467] model=claude-haiku-5-5 -->
# Glide Training: Getting Started

{"quest": {"key": "Glide Training: Getting Started", "title": "Glide Training: Getting Started"},
 "offer": null,
 "progress": null,
 "complete": {"locale_id": 4419682, "speaker": null},
 "other_lines": [
  {"locale_id": 4419679, "role": "objective_hint", "speaker": null},
  {"locale_id": 4419681, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Completion line tagged to Getting Started: 'Good job! Your ride's understanding of your commands has been transferred to the Training Saddle! Training is hard work. Come back tomorrow...'", "source": "locale:4419682 (quest_dialog, Sanctuary, tagged Glide Training: Getting Started); verified by direct locale lookup"},
  {"claim": "Full objective text: go to the launch pads outside Sanctuary and jump through the fiery hoop above while riding your untrained glide-trainable ride", "source": "locale:4419679 (quest_objective, verified)"},
  {"claim": "Quest title is Glide Training: Getting Started", "source": "locale:4419680 (quest_title)"},
  {"claim": "Objective summary naming Troy as the one who asked for the launch", "source": "locale:4419681 (quest_objective, Troy Ridewrangler in Seaside has asked me to use a launch pad...)"},
  {"claim": "Troy Ridewrangler is the giver of the five-step series; 4419680 and the NPC answer list him as giver", "source": "npc answer: troy ridewrangler quests_given"},
  {"claim": "Proof item 'Proof of Training - Part 1 of 5' exists, but client 441977 says Troy collects proofs only after all 5 steps, so the wiki per-quest reward is contradicted and not listed", "source": "locale:441973 / locale:441977 / wiki:Proof of Training - Part 1 of 5"},
  {"claim": "Quest-series opener text places Troy near the Seaside ride stable/corral", "source": "locale:441985, 4419712 (not used as dialog for this quest)"}
 ],
 "confidence": 0.5,
 "open": [
  "Live status unsure: a 'Glide Training: Step 1: Sanctuary' set (locale 4419703-4419705, repo-named) also exists. Set A (Getting Started, tagged 4419679-4419682) was used because 4419682 is tagged to this exact quest title and matches a step-1 completion. If Set B is the live set, the equivalent complete line would be different and must be re-checked.",
  "Offer: no client offer/ask line tagged to Getting Started was found, so offer is null.",
  "Progress: no reminder line tagged to Getting Started was found; 4419681 is a quest objective summary, not an NPC reminder, so progress is null.",
  "Complete speaker left null: 4419682 has no in-text name and no NPC answer attributes it to Troy. The wiki quotes it with a Troy Ridewrangler signature, but that is not an allowed attribution source here. Troy is the giver, so a builder may reasonably assign him.",
  "Next link conflicts: wiki says Glide Training: Basic Training (4419684), repo says Step 2: Merry Vale (4419717). Not settled, so no next link is listed.",
  "Reward: wiki says a 'Proof of Training - Part 1 of 5' ticket is granted on completion, but client 441977 says proofs are collected after all 5 steps. No coin amount was found. Reward left out.",
  "The 'To Start' location near the Seaside Warpstone is wiki-only; Troy's place is described three ways (Warpstone per wiki, ride stable per 441985, ride corral per 4419712), unreconciled.",
  "Return-to-Troy step appears only on the wiki and has no client objective string, so it is not listed.",
  "Hoop target has no separate locale id; the fiery hoop is named only inside 4419679.",
  "NPC id 1290590531 is only a name id from repo notes, not a verified NPC table id."
 ]}
