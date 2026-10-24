<!-- fleet job=dialog-infer id=wa-luau-v1 status=done turns=3 usd=0.0024 tokens(read,write,in,out)=[15462, 8587, 8, 2336] model=claude-haiku-5-5 -->
# A Luau

{"quest": {"key": "A Luau", "title": "A Luau"},
 "offer": {"locale_id": 422864, "speaker": "Tiger the Party Animal"},
 "progress": {"locale_id": 422851, "speaker": "Tiger the Party Animal"},
 "complete": {"locale_id": 422849, "speaker": "Tiger the Party Animal"},
 "other_lines": [
  {"locale_id": 422865, "role": "other", "speaker": null},
  {"locale_id": 422866, "role": "objective_hint", "speaker": "Tiger the Party Animal"},
  {"locale_id": 422874, "role": "objective_hint", "speaker": null},
  {"locale_id": 422875, "role": "objective_hint", "speaker": null},
  {"locale_id": 422876, "role": "other", "speaker": null},
  {"locale_id": 4548, "role": "reward", "speaker": null}
 ],
 "evidence": [
  {"claim": "Offer line: 'Dude, isn't this party chill? ... If you put on a luau outfit, I'll give you a special party favor. What do you say?'", "source": "locale:422864 (tagged A Luau, npc_dialog, Seaside; NPC answer attributes it to Tiger)"},
  {"claim": "Progress/reminder line: 'Where's your luau outfit? Dude, totally NOT cool.' fits a reminder to someone not yet in outfit", "source": "locale:422851 (tagged A Luau, npc_dialog, Seaside; NPC answer attributes it to Tiger)"},
  {"claim": "Completion line: 'Stellar luau outfit! Dude, take a party favor.' pays the reward", "source": "locale:422849 (tagged A Luau, npc_dialog, Seaside; NPC answer attributes it to Tiger)"},
  {"claim": "Quest title is 'A Luau'", "source": "locale:422865 (quest_title, A Luau)"},
  {"claim": "Objective text: 'Equip a luau outfit and speak to Tiger the Party Animal during a Luau Party.'", "source": "locale:422874"},
  {"claim": "Luau Party start announcement for Seaside exists, supporting the event gate but not a quest condition", "source": "locale:419938"},
  {"claim": "Party favor item name 'Luau Party Favor'", "source": "locale:4548 (name only; link to A Luau is wiki-only)"},
  {"claim": "Lines 422864, 422849, 422851, 422865 were re-checked in the client locale table and match the pack text", "source": "locale lookup"},
  {"claim": "Tiger is the giver; Winter Party and Party for Pets are sibling quests, not this quest", "source": "NPC answer for Tiger; locale:422869 and 422868 tagged Party for Pets"}
 ],
 "confidence": 0.6,
 "open": [
  "record_id not set: no quest record exists; one must be created with title_locale_id 422865 and giver Tiger (locale 420171).",
  "npc_id not set: Tiger's name id 2807361043 is shared across Seaside, Sanctuary, Blackspore and Snowhill files, so no Seaside-specific key was chosen. Builder should pick the Seaside spawn from the luau event system.",
  "Gating unconfirmed: Tiger appears only during Luau Community Events (wiki only). The client has only zone start announcements (419938 Seaside). The spawn/firing condition is not in the evidence.",
  "live set to unsure (not yes): the firing condition is not in the client, and the enum has no 'likely' option.",
  "Repeatability is wiki/repo-only and not confirmed by a client string.",
  "Reward: 'Luau Party Favor' (4548) is a name only. Quantity, item id and the link to A Luau are not confirmed by client data. The wiki image was not used.",
  "Line order: no established order with sibling quests Party for Pets and Winter Party, so previous/next are empty.",
  "Excluded: 422852 'Sorry!' is a FLAGged fragment. 422880 and 422877 belong to the separate 'Obtain a pet' quest. 422874 is an objective, not dialog, so it is not used as progress.",
  "Repo fix still needed: NPCs - Seaside.md:281 lists 986709886 for A Luau; the client id is 422865. Not edited here (repo not writable from this pass).",
  "Critique from pack: the Blackspore Swamp zone guess conflicts with the client's Seaside tags and was not used."
 ]}
