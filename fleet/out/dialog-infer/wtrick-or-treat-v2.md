<!-- fleet job=dialog-infer id=wtrick-or-treat-v2 status=done turns=3 usd=0.0025 tokens(read,write,in,out)=[16960, 10843, 8, 1925] model=claude-haiku-5-5 -->
# Trick-or-Treat

{"quest": {"key": "Trick-or-Treat", "title": "Trick-or-Treat"},
 "offer": {"locale_id": 415049, "speaker": null},
 "progress": null,
 "complete": {"locale_id": 415052, "speaker": null},
 "other_lines": [
  {"locale_id": 415051, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'Trick-or-Treat'", "source": "locale:415050 (quest_title, hint Trick-or-Treat)"},
  {"claim": "Offer: greeting/ask explaining candy is given only for a /scare ('Have you ever trick-or-treated before?'), unflagged npc_dialog tagged Trick-or-Treat", "source": "locale:415049"},
  {"claim": "Objective: find people with the Halloween icon and /scare them for treats", "source": "locale:415051 (quest_objective, hint Trick-or-Treat)"},
  {"claim": "Complete-style thanks for a candy stash, tagged exactly Trick-or-Treat, unflagged, Sanctuary. Tie to quest state is inferred from wording ('That's quite a stash of candy')", "source": "locale:415052 (quest_dialog, Sanctuary, hint Trick-or-Treat)"},
  {"claim": "Giver is Halloween Harry, npc_id 9500000493, locale 415047", "source": "quest answer; locale:415047 npc_name"}
 ],
 "confidence": 0.6,
 "open": [
  "Progress left null. 415825 ('Remember, some folks won't part with their candy unless you give them a good scare!') is tagged to the title 'Trick-or-Treat around Sanctuary' (locale:415821), a different quest title, so it is not this quest's line.",
  "Excluded 415822 and 415824 (candy-collection and show-Harry objectives). Both are tagged 'Trick-or-Treat around Sanctuary', i.e. the sibling quest, not 'Trick-or-Treat'. The earlier answer's Harry attribution of 415824 as progress does not change that tag. Not used as followup.",
  "Offer speaker null: 415049 has no speaker name in its text and its hint is the quest title, not an NPC. Halloween Harry is the giver, but no source attributes 415049 to him.",
  "Complete speaker null for the same reason. 415052 completion status is inferred from wording, not from a quest-state link. Its 'every day' / 'See you tomorrow' wording points to repeatable daily gating, which is unverified.",
  "Reward: no reward line in client text. Candy item id and amount not recovered, so no reward entry.",
  "Zone: Sanctuary (Pixiewood area) per the giver's NPC answer and locale:436401. Exact spawn point (Pixiewood Hills vs. main street) still needs a spawn check.",
  "Halloween Fanatic next link and the A Formal Report conflict from the earlier answer are unverified and not wired here."
 ]
}
