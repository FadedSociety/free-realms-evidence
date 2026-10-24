<!-- fleet job=citem-critic id=cgrowling-mud-pie-1204-v3-evidence-r3 status=done turns=2 usd=0.0016 tokens(read,write,in,out)=[4440, 7887, 6, 1127] model=claude-haiku-5-5 -->
# Growling Mud Pie

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "sources[0].source", "issue": "The CurrencyType 1 = Station Cash claim cites Sanctuary WelcomeScreenHelper.cs:14. I did not open that file in this check, so the constant is unverified here. The bundle's own CurrencyType field is 1 (StoreBundles.json line 771), which matches the claim.", "fix": "Keep the currency as station_cash, but confirm WelcomeScreenHelper.cs:14 (StationCashCurrencyType = 1) before relying on it. Otherwise the citation is only as strong as the bundle field itself."}]}
