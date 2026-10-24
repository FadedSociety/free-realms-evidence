<!-- fleet job=citem-infer id=c500-stars-potion-archer-412872-v1 status=nothing_found turns=5 usd=0.0035 tokens(read,write,in,out)=[35634, 14139, 12, 2691] model=claude-haiku-5-5 -->
# 500 Stars Potion - Archer

{"item": {"name": "500 Stars Potion - Archer", "locale_id": 412872, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text 412872 is '500 Stars Potion - Archer', with the line 'This potion gives 500 stars to your Blacksmith job.'-style description; the description for the Archer variant is locale 412872's paired line in quest-lines/line-packs.json (the pack's description is 'This potion gives 500 stars to your Blacksmith job.' for the Blacksmith family; the Archer line itself was not located in repo text).", "source": "locale:412872; quest-lines/line-packs.json:66857-66862 (sibling job-star potion lines, same family)"},
  {"claim": "The same '500 Stars Potion - <Job>' family exists for about 20 jobs (Adventurer, Blacksmith, Brawler, Card Duelist, Chef, Demo Derby Driver, Kart Driver, Medic, Miner, Ninja, Pet Trainer, Postman, Warrior, Wizard, etc.), each a client item that grants 500 job stars (job XP) and is not sold or dropped by any documented source in the repo notes.", "source": "notes/Build Guides/Content/Jobs/Postman.md:236; notes/Build Guides/Content/Jobs/Pet Trainer.md:236; notes/Build Guides/Content/Jobs/Demolition Derby Driver.md:217; notes/Build Guides/Content/Jobs/Adventurer.md:264"},
  {"claim": "The client definition (definition 68787, slot 0, class 9) has no coin store price, so no coin vendor sale is evidenced by stores.json.", "source": "client definition in evidence pack; repo:data/content/stores.json (no matching row)"},
  {"claim": "No wiki page, article, video frame, quest reward, enemy drop or event names this potion. Repo search for 68787 and 'Stars Potion' finds only locale dumps and job-note mentions with no acquisition text.", "source": "repo search results (notes/Build Guides/Content/Jobs/*.md, quest-lines/*.json); lookup wiki/articles/video: no hits"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found for 500 Stars Potion - Archer. Do not assume vendor: the first-pass 'vendor' guess has no evidence, and the pack's vendor_stock is empty.",
  "Live status unverified: the client defines the item, but no store row, wiki page or sighting confirms it was obtainable. Jev's 'live: yes' is a hint only.",
  "Locale 412872 description text for the Archer variant was not found in repo text; the sibling Blacksmith line is 'This potion gives 500 stars to your Blacksmith job.' The Archer description in the pack ('...Blacksmith job') appears to be a copy error in the client definition and should be checked against the locale table.",
  "Need: a wiki search for 'Archer' job items, the Archer job page, or a Station Cash / Coin Shop / event listing for the 500 Stars Potion family to see whether any of these potions were sold (e.g. as a job-boost item) and when they were retired."
 ]}
