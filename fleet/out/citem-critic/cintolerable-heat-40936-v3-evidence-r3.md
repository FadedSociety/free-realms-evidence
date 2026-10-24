<!-- fleet job=citem-critic id=cintolerable-heat-40936-v3-evidence-r3 status=done turns=2 usd=0.0011 tokens(read,write,in,out)=[4091, 4906, 6, 976] model=claude-haiku-5-5 -->
# Intolerable Heat

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "open[4]", "issue": "Still cites locale:1630222957, which does not exist (automatic id check). The answer says it removed this citation from the evidence, but the open note keeps it. It is a data-file key, not a locale id.", "fix": "Delete the locale:1630222957 reference from open[4]. Cite only the verified facts: the ucdt/ugdt keys are in opening-anvil-placement-v1/locale/en_us_data.dat, not the locale table."}]}
