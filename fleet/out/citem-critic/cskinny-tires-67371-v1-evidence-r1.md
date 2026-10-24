<!-- fleet job=citem-critic id=cskinny-tires-67371-v1-evidence-r1 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[18666, 15231, 8, 1368] model=claude-haiku-5-5 -->
# Skinny Tires

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "item.kind", "issue": "Labelled 'collection', but Skinny Tires is a single member item (definition 23758) of the 'Kart Race Tires' collection (219). The answer's own open note says so. 'collection' describes the container, not this item.", "fix": "Use a standalone item kind (e.g. 'item' or 'collection member') and keep the collection as a membership fact. Source: client definition pack (definition_ids [23758], description locale:132476 'This item can be added to the Kart Race Tires Collection')."}]}
