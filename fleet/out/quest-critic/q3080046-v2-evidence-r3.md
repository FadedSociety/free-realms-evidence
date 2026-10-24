<!-- fleet job=quest-critic id=q3080046-v2-evidence-r3 status=no_submit turns=4 usd=0.0032 tokens(read,write,in,out)=[28055, 12717, 10, 2563] model=claude-haiku-5-5 -->
# Kart Driver: SG Tour 400: Frost Ridge

{"lens": "evidence", "pass": true, "score": 4, "problems": [{"field": "giver.npc_id", "issue": "Left null, and the record's own giver_npc_id 9000000371 is only an inferred mapping from npcs_unresolved.json. The answer correctly flags this, but the giver is not wireable as it stands.", "fix": "Resolve Kade Carmichael's spawn/NPC id from the real NPC table (locale 101924 is confirmed as the name) before the builder wires the giver. Do not rely on 9000000371 until it is confirmed."}, {"field": "evidence[2] / dialog.progress", "issue": "The answer calls locale:395344 a 'progress text', but the client types it as quest_objective (zone '-', tag SG Tour 400). Its text is accurate ('You won the first race of the SG Tour 400! Only three more to go!...'), but it is an objective-style line that describes the Wildwood win and the handoff to Frost Ridge. Calling it progress is a loose label.", "fix": "Record 395344 as a quest_objective line on the Wildwood leg or the handoff, not as this quest's progress dialog. Leave dialog.progress null unless a Frost Ridge-specific progress line is found."}, {"field": "rewards", "issue": "Empty, with the series prize (Lightning Cup) correctly excluded. The client has no reward line for this leg, so this is an honest gap, not an error.", "fix": "No change required; keep rewards empty and note it as unknown."}]}

Checks I ran:
- 395343 is quest_title 'Kart Driver: SG Tour 400: Frost Ridge' with no FLAG. Matches.
- 398074 is 'Beat Kade Carmichael in a race at Frost Ridge Speedway.' Matches. Its siblings 397998, 398088 and 398215 also match.
- 101924 is 'Kade Carmichael'. Matches.
- 3511 (Wildwood) and 3580 (Thunder Falls) titles match the previous and next legs.
- 395342 offer text and 395349 ('After winning the race at Frost Ridge, only two races remain...') match.
- 395345 is the series-end line, so leaving dialog.complete null is reasonable.
- kart_driver.json has 3080045, 3080046 and 3080047, and jobs.json lists all three together. Matches.

Chain link: prerequisite_quest_ids on 3080046 is still empty. The builder must wire 3080045 as the prerequisite and 3080047 as the next leg.
