<!-- fleet job=quest-critic id=q3080049-v1-evidence-r1 status=no_submit turns=4 usd=0.0038 tokens(read,write,in,out)=[36797, 17535, 10, 2572] model=claude-haiku-5-5 -->
# Kart Driver: Sacred Grove Gup: Frost Ridge

{"lens": "evidence", "pass": true, "score": 4, "problems": [{"field": "line", "issue": "The answer puts row 47 under 'SG Tour 400 (champion: Kade Carmichael)', which is accurate to the guide's section header. But the guide's row 47 itself gives Giver 'unknown' and Location 'unknown', so Kade is a section-level association, not a per-quest fact. The answer's evidence entry does say 'giver Kade Carmichael (inferred)' only for row 44, which is correct.", "fix": "Keep the section name, but state that row 47 has no giver or location of its own (Kart Driver.md:124). Kade is only the section champion."}, {"field": "evidence[5]", "issue": "The claim 'no wiki page or article covers it' is supported only by the client lookup. The wiki/articles lookup I ran for 'Gup Frost Ridge kart' returned no matches, so the claim holds, but the answer cites no wiki check.", "fix": "No change needed to the answer's conclusion. The claim is consistent with a wiki/articles search returning no matches."}]}

Checks I ran:
- locale:3526 is exactly 'Kart Driver: Sacred Grove Gup: Frost Ridge' (quest_title, no FLAG). The answer's title and id are correct.
- Kart Driver.md:124 is row 47 with the title, ucdt id 2595156650, and "unknown" for giver, location and objectives. The answer reports this accurately.
- Kart Driver.md:121 is row 44, 'Kart Driver: SG Tour 400: Frost Ridge', with objective locale 3975056715. The answer's cited id is real.
- npcs_unresolved.json:4852 has ref_id 9000000537 with name null and zone null. Its only context is "kart_driver:SG Tour 400 (champion: Kade Carmichael):47". The answer's giver id matches that source and is correctly marked unconfirmed.
- NPCs - Wilds.md:149 says Kade Carmichael is the reigning champion who starts the SG Tour 400 at Wildwood Speedway. The answer's citation is accurate.
- kart_driver.json:2336 already holds giver_npc_id 9000000537 for this record. The answer leaves the record disabled and does not overstate the giver, so its "unsure" status is the honest reading.

Overall the answer is sourced and does not treat a flagged line as live. Its conclusion that the record cannot be wired yet, because there are no objectives, dialog or rewards, is supported.
