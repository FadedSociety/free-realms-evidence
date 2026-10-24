<!-- fleet job=citem-critic id=corange-tulip-37377-v1-world-r2 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[3635, 8090, 6, 1324] model=claude-haiku-5-5 -->
# Orange Tulip

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "evidence[0].source", "issue": "The item's description is cited as locale 132285, but in the client text table that id is tagged as a ui string (ui - Tulips Collection), not an item description. The collection-membership reading still holds, but the citation type is loose.", "fix": "Cite locale 132285 as the UI collection text ('This item can be added to the Tulips Collection') and keep the item-kind inference labelled as inferred from that text."}]}
