<!-- fleet job=quest-critic id=wore-survey-v3-lines-r4 status=no_submit turns=4 usd=0.0038 tokens(read,write,in,out)=[35032, 17867, 10, 2474] model=claude-haiku-5-5 -->
# Ore Survey

{"lens": "lines", "pass": true, "score": 4, "problems": [{"field": "line", "issue": "Previous and next are empty and placement is marked unconfirmed. The answer does not check the chain notes that put Vrock's quarry quests in the Miner line's third and fourth bands (NPCs - Blackspore Swamp.md:216). The text at 91789 ('So far we've been pullin' ore from the hills around the old mine') suggests an earlier step that was not looked for.", "fix": "Check Blackspore Swamp.md:216 and the Miner line bands to see whether Ore Survey sits in the third or fourth band, and record the neighbouring quests if they are found. Otherwise keep the honest 'unconfirmed' label."}, {"field": "objectives[1].count", "issue": "The collect objective has no count. The offer text 91789 says only 'gather a few samples', so the count is a builder decision, not a client value. The answer already says this in 'open'.", "fix": "Leave count null and mark it as a builder choice. Do not present any number as sourced."}]}

I checked the lines that matter, and they hold:
- 91790 is 'Ore Survey', 91789 is the offer ('gather a few samples'), 91791 is the purpose, 91801–91804 are the objectives, and 91792 is the completion.
- 45557 is 'Vrock Gravelfist'. 5700 is 'Haunted Mines'.
- NPC 9500000078 is 'Vrock Gravelfist' at blackspore_swamp.json:39447, with name_string_id 45557.
- The Miner.md entry (line 179) matches the giver and zone. Its title ids are not locale ids, and the answer correctly does not use them.
