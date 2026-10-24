<!-- fleet job=item-critic id=iisles-of-the-moon-v1-world-r2 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[3248, 9518, 6, 936] model=claude-haiku-5-5 -->
# Isles of the Moon

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "item.kind", "issue": "The subject is a map region (wiki LocationInfobox, type Region), not an item. Setting kind to \"other\" on an item record is a category mismatch, though the answer's own claim that it is not an item is correct.", "fix": "Mark it as not an item (no item record), or keep kind \"other\" only with the note that it is an unused location. Sources: wiki Isles_of_the_Moon rev 50071 (LocationInfobox, Categories Locations and Unused)."}]}
