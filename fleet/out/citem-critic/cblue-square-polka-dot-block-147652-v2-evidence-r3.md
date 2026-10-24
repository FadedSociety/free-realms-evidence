<!-- fleet job=citem-critic id=cblue-square-polka-dot-block-147652-v2-evidence-r3 status=done turns=2 usd=0.0014 tokens(read,write,in,out)=[4081, 6609, 6, 1011] model=claude-haiku-5-5 -->
# Blue Square Polka Dot Block

{"lens": "evidence", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "item.kind", "issue": "'furniture' is inferred from slot 0, class 0 and the housing-block name cluster, not from a wiki or client category. The answer already marks this in open, so it is honest, but the item field states it flatly.", "fix": "Label kind as inferred (client slot/class and name cluster locale:147647-147657), or leave it unset until a client category confirms it."}]}
