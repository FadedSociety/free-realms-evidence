<!-- fleet job=citem-critic id=chealth-potion-1-20425-v2-evidence-r3 status=no_submit turns=2 usd=0.0017 tokens(read,write,in,out)=[3681, 10224, 6, 835] model=claude-haiku-5-5 -->
# Health Potion 1

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "evidence[3]", "issue": "Automatic id check flags locale:20427 as a placeholder ('(PH)'). The answer says it is not used as evidence, so the claim is not wrong. But citing a flagged placeholder sibling in the evidence list invites misreading, and the claim adds nothing about this item.", "fix": "Drop evidence[3], or reword it to say the locale:20420-20429 cluster was checked and holds no acquisition source for 11000 / locale:20425. Do not cite locale:20427 as support."}]}
