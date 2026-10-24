<!-- fleet job=citem-infer id=cpet-trainer-legs-bubblegum-123157-v1 status=done turns=6 usd=0.0050 tokens(read,write,in,out)=[79121, 22389, 14, 2917] model=claude-haiku-5-5 -->
# Pet Trainer legs bubblegum

{"item": {"name": "Pet Trainer legs bubblegum", "locale_id": 123157, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 43158 is a slot-4 (legs) clothing item in class 1, model freestyle_<race>_<gender>_legs_longcargopantsdecal.adr, with no coin store price (no coin vendor sale in stores data).", "source": "client definition in pack; no repo:data/content/stores.json match found for this item"},
  {"claim": "The name is one of a colour-variant family: 'Pet Trainer head / chest / legs <colour>' in 16 colours (barndoor, bubblegum, charcoal, grape, honey, jungle, latte, mahogany, mudpie, ocean, pumpkin, rosepetal, saphire, skyblue, snow, sweetpea). The head, chest and legs bubblegum pieces are locale 123156, 123155 and 123157.", "source": "locale:123157; locale:123155; locale:123156; repo:notes/Build Guides/Content/Jobs/Pet Trainer.md:231"},
  {"claim": "The Pet Trainer job clothing set is a freestyle job outfit, filtered to job id 121 (Pet Trainer). Its clothing pieces have no stat tiers or level requirement text in the client, and no source line for the colour variants.", "source": "repo:notes/Build Guides/Content/Jobs/Pet Trainer.md:220-234; repo:notes/Build Guides/Gameplay/Character and Customization.md:130"},
  {"claim": "The client names an L1-only tier for these colour pieces (pettrainer_L1_<slot>_<colour>); no L2 to L5 exists in the client text.", "source": "repo:notes/Build Guides/Content/Jobs/Pet Trainer.md:231"},
  {"claim": "The wiki has no page, image, article fact or video frame that names this item, and no vendor stocks it in the pack.", "source": "lookup (client, wiki, articles, video) for 'Pet Trainer bubblegum' returned only the client locale lines 123155, 123156, 123157; refs search found no wiki or community-server mention of 'Pet Trainer ... bubblegum'"},
  {"claim": "The only Pet Trainer clothing sources documented anywhere are the Cow Spot Apron (wiki: redemption code MILKRULES) and the Pet Trainer Cap (client text: given only to the best Pet Trainers in Sacred Grove, source unknown). Neither names the bubblegum legs piece.", "source": "repo:notes/Build Guides/Content/Jobs/Pet Trainer.md:224-226; wiki Pet Trainer Cow Spot Apron"}
 ],
 "confidence": 0.3,
 "open": [
  "No source found. The item may be a Pet Trainer job-outfit colour piece issued through job progression, a new-member pack (client line 3755074429 'If you join now, you'll receive this special new member pack of pet trainer items!' has unknown contents), a code reward, or a retired or never-released variant. Each needs a wiki, forum or video check before any source is written.",
  "Live status is unverified. The first-pass 'live: yes' is a hint from a cheap model, not evidence. The item is in the client, but the client alone does not show that it was ever sold, dropped or granted.",
  "Client definition 43158 was not cross-checked against FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json (the Legacy file has Pet Trainer chest/head/legs colour comments near line 609142); that file might carry extra fields (price, source tag) and should be checked.",
  "The client description is empty, so no in-game text links the piece to a source.",
  "Whether the L1 colour pieces unlock by Pet Trainer job level is unknown (the client shows no level requirement).",
  "The pack's vendor_stock, mentioned_by_other_answers, article_facts and video are all empty, so there are no critiques to resolve."
 ]}
