<!-- fleet job=dialog-infer id=wlike-scavengers-in-a-barrel-v1 status=done turns=3 usd=0.0027 tokens(read,write,in,out)=[15243, 10273, 8, 2556] model=claude-haiku-5-5 -->
# Like Scavengers in a Barrel

{"quest": {"key": "Like Scavengers in a Barrel", "title": "Like Scavengers in a Barrel"},
 "offer": {"locale_id": 29611, "speaker": "Wheelie Pete"},
 "progress": null,
 "complete": {"locale_id": 29612, "speaker": "Wheelie Pete"},
 "other_lines": [
  {"locale_id": 439806, "role": "objective_hint", "speaker": null},
  {"locale_id": 439808, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "29611 is this quest's offer: tagged to the quest, and its text asks the player to bring back the Barrels of Sasparilla", "source": "locale:29611 (quest_dialog, hint Like Scavengers in a Barrel); NPC answer for Wheelie Pete lists 29611 as quest_offer for this quest"},
  {"claim": "29612 is this quest's completion: tagged to the quest, first-person sasparilla recovered, then a follow-up favor (the Hog Wild Harley handoff)", "source": "locale:29612 (quest_dialog, hint Like Scavengers in a Barrel)"},
  {"claim": "Speaker of 29612 is Wheelie Pete (inferred from text: the sasparilla is his, and he is the quest giver); no NPC answer attributes it", "source": "locale:29612 text; locale:29611 NPC attribution"},
  {"claim": "Objective 439806 'Find Barrels of Sasparilla' and 439808 'Return to Wheelie Pete' exist as client objective text", "source": "locale:439806; pack objective list (439808 not re-verified in this pass)"},
  {"claim": "Progress line 440048 names this task but is tagged to a different hint group, so it is excluded", "source": "locale:440048 hint mismatch per pack"},
  {"claim": "Untagged 29631/29632 (Stolen Sasparilla) have no speaker attribution and are not tagged to this quest, so not used", "source": "locale:29631, locale:29632 (hint '-')"}
 ],
 "confidence": 0.6,
 "open": [
  "Start (offer) speaker is confirmed by NPC answer; offer line is tagged to this quest.",
  "Complete speaker Wheelie Pete is inferred from text, not an explicit NPC attribution.",
  "No progress line is tagged to this quest; 440048 is excluded because its tag is another hint group.",
  "Reward: 10 coins is wiki-only; no client reward line found, so no reward locale id is listed.",
  "Kill step 439804 (Defeat Sandscale Scavengers) dropped: no wiki kill step and not in this quest's objective group.",
  "Count 5 is wiki-only; objective 439806 carries no number. Item 439947 'Barrel of Sasparilla' is not confirmed as this objective's target.",
  "Untagged 29631 and 29632 (Stolen Sasparilla) may be the true start/finish lines, but they carry no quest tag or speaker attribution, so they are left out.",
  "No NPC record id for Wheelie Pete; npc_id unknown.",
  "Wiki calls Hog Wild Harley repeatable; the linear-chain relation to this quest is unconfirmed."
 ]}
