<!-- fleet job=citem-critic id=cshiny-jungle-ring-96087-v1-world-r2 status=done turns=2 usd=0.0015 tokens(read,write,in,out)=[4072, 8004, 6, 970] model=claude-haiku-5-5 -->
# Shiny Jungle Ring

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "evidence[4].source", "issue": "Cites locale:150436, which is FLAGGED placeholder (generic 'This is a ... item' stub). The auto id check rejects it as live evidence. The answer does label it as non-evidence, but it should not sit in the evidence list as a source-bearing line.", "fix": "Drop the locale:150436 citation or move it to a note marked 'FLAGGED placeholder, not evidence'. Only the client definition (ClientItemDefinitions.json id 30681) and locale:96087 are real support."}]}
