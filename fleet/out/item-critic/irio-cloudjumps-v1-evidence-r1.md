<!-- fleet job=item-critic id=irio-cloudjumps-v1-evidence-r1 status=done turns=3 usd=0.0013 tokens(read,write,in,out)=[7949, 4927, 8, 1223] model=claude-haiku-5-5 -->
# Rio Cloudjumps

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "evidence[1].claim / open", "issue": "The answer says the Coin Clean-Up reward is 'coins from the Cloud World'. The client text (locale:430165) only says 'Keep what you find as your reward.' Calling it coins is an inference, not evidence. It is hedged in 'open', so this is minor.", "fix": "Say only that the reward is 'Keep what you find' (locale:430165, quest_objective Coin Clean-up). Do not name a reward item or currency."}]}
