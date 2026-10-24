<!-- fleet job=citem-infer id=cstudent-postman-hat-27019-v2 status=nothing_found turns=2 usd=0.0028 tokens(read,write,in,out)=[5562, 13316, 6, 2125] model=claude-haiku-5-5 -->
# Student Postman Hat

{"item": {"name": "Student Postman Hat", "locale_id": 27019, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text: locale 27019 is 'Student Postman Hat' (item). Client definition 13137, slot 1, class 3, model courier_<race>_<gender>_head_safarihat.adr. No coin store price in the pack.", "source": "locale:27019; client definition in pack"},
  {"claim": "No wiki page, article, video frame, image, vendor stock, or other answer names this hat. The client's lookup shows only the name and its sibling Student Postman pieces (Shirt 26718, Shorts 27077, Short Shorts 27194, Shoes 26844).", "source": "lookup client/wiki/articles/video 'Student Postman'"},
  {"claim": "Definition 13137 appears in FreeRealms-Legacy's ClientItemDefinitions.json as 'Student Postman Hat' and in Legacy's Profiles.json Postman starter list. Legacy is a community server; the list is its proposal, not a retail grant record.", "source": "FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:245386-245387; FreeRealms-Legacy/src/Resources/Profiles.json:353; repo notes/Research/Job Starter Outfits.md:60 (every nonempty list marked R, selection from Legacy, no recovered retail default rule)"},
  {"claim": "Postman.md's table lists 'Hat 2557323136'. Checked: 2557323136 is a locale text-hash key ('Student Postman Hat' ucdt entry in en_us_data.dat), not a definition id, so it does not conflict with 13137. It also does not give a source.", "source": "FreeRealmsLocaleTools/test/FreeRealmsLocaleTools.Tests/data/en_us_data.dat:67357"},
  {"claim": "The earlier 'free once on Postman job unlock' claim is not supported. The autopilot notes (T201, T409) and F228/L040 are internal build decisions, not live-game evidence, and were dropped as sources.", "source": "critique 1 and 2 of the pack; notes/Research/Job Starter Outfits.md:60"},
  {"claim": "locale:26844 (Shoes) is flagged for raw template markup and is not cited as evidence.", "source": "lookup client flag on locale:26844"}
 ],
 "confidence": 0.1,
 "open": [
  "No independent source for how the Student Postman Hat was acquired. The only link to 13137 is Legacy's proposed Postman starter list (a community proposal). Do not wire a grant or price from it.",
  "The first-pass 'vendor' guess is unsupported: no coin store price (repo:data/content/stores.json has no entry for 13137 per the pack) and no vendor stock.",
  "Whether the hat was given free with the Postman job, sold, or part of a promotion is unknown. Needs a live-game or wiki source (e.g. a Postman job or costume page, or a player report).",
  "Retirement status unknown; no source says retired or unobtainable.",
  "Price: none evidenced."
 ]}
