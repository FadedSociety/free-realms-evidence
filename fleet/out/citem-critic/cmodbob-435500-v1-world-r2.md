<!-- fleet job=citem-critic id=cmodbob-435500-v1-world-r2 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[3606, 9552, 6, 1034] model=claude-haiku-5-5 -->
# Modbob

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "kind", "issue": "The answer sets kind to 'clothing' by inference from slot 2 and the hair model. Its own open list says this is unconfirmed, and the evidence pack's first-pass tag was 'other'. The client shows only slot 2, class_id 1 and a hair model, which supports a hairstyle but not the 'clothing' label.", "fix": "Leave kind unconfirmed, or record it as a hairstyle (slot 2, model human_f_hair_FRCmodbob_<hairtype>.adr, client definition 78057, locale:435500) until the item class definition confirms it."}]}
