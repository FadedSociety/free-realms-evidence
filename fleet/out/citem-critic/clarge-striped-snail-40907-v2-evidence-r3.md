<!-- fleet job=citem-critic id=clarge-striped-snail-40907-v2-evidence-r3 status=done turns=2 usd=0.0012 tokens(read,write,in,out)=[3893, 4683, 6, 1061] model=claude-haiku-5-5 -->
# Large Striped Snail

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "evidence[1].claim", "issue": "The claim text still repeats the nonexistent id locale:122159565. The id check confirms it does not exist. The answer does withdraw it, but a bad id should not stay in an evidence claim.", "fix": "Drop the locale:122159565 mention from evidence[1] and open[4]. State only that the description is locale:132347, which I confirmed reads 'This item can be added to the Striped Snails Collection'."}]}
