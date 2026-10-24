<!-- fleet job=item-critic id=igloam-council-v1-evidence-r1 status=done turns=2 usd=0.0012 tokens(read,write,in,out)=[3540, 5901, 6, 825] model=claude-haiku-5-5 -->
# Gloam Council

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "evidence[1].source", "issue": "Cites locale:75635 as an example of Gloam Council lore, but that string is just the NPC line 'Right.' and says nothing about the faction. The other cited ids (37882, 37885, 427753) do describe the Council.", "fix": "Drop locale:75635 from the list, or replace it with locale:37883 ('The Gloam Council was secretive, hidden in shadow...'), which describes the faction. The lookup confirms the wording of 37882, 37885 and 427753."}]}
