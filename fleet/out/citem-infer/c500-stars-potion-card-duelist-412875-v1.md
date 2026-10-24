<!-- fleet job=citem-infer id=c500-stars-potion-card-duelist-412875-v1 status=nothing_found turns=5 usd=0.0042 tokens(read,write,in,out)=[43536, 18866, 12, 2778] model=claude-haiku-5-5 -->
# 500 Stars Potion - Card Duelist

{"item": {"name": "500 Stars Potion - Card Duelist", "locale_id": 412875, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name and description: 'This potion gives 500 stars to your Card Duelist job.' (locale 412889), consumable in class 9, slot 0, definition 68790, no coin store price.", "source": "locale:412875; locale:412889; pack client_definition"},
  {"claim": "The name exists in the client's text table as a ucdt entry (hash 256227039) and a ugdt entry (1867158258), so it is a shipped string.", "source": "opening-harvesting-native-20261009T142624Z/locale/en_us_data.dat:6728 and :49244"},
  {"claim": "It belongs to a family of '500 Stars Potion - <Job>' items, one per job (Adventurer, Archer, Blacksmith, Brawler, Card Duelist, Chef, Demo Derby Driver, Kart Driver, Medic, Miner, Ninja, Pet Trainer, Postman, Warrior, Wizard). The Postman, Pet Trainer, Demo Derby Driver and Adventurer job notes list their own sibling potions as client-only 'Experience helpers' or 'Job stars' with no source.", "source": "locale:412871-412885 range; notes/Build Guides/Content/Jobs/Postman.md:236; notes/Build Guides/Content/Jobs/Pet Trainer.md:236; notes/Build Guides/Content/Jobs/Demolition Derby Driver.md:217; notes/Build Guides/Content/Jobs/Adventurer.md:264"},
  {"claim": "No wiki page, article, video frame, vendor stock (repo data/content/stores), quest reward, drop or briefs entry names this potion or the 500 Stars potion family. Searches of the repo and refs, the wiki index and the articles index returned nothing for it.", "source": "lookup (client, wiki, articles, video) for '500 Stars Potion'; search repo/refs for 68790 and 'Stars Potion'; search briefs"},
  {"claim": "The Card Duelist job note also has no source for it.", "source": "notes/Build Guides/Content/Jobs/Card Duelist (no mention of the potion found by search)"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found for 500 Stars Potion - Card Duelist (definition 68790). It is not in any coin vendor stock, store price, quest, drop, event or wiki category we hold. Needs a live-era source check (wiki Card Duelist job page, a player forum post, or a video of the item in a shop or reward window).",
  "Live status is unsure: the client ships the string and the family is consistent, but no wiki or video confirms it was sold or granted live. The first-pass tag 'live: yes, vendor' is a hint only and is not supported by any repo or wiki evidence found.",
  "Vendor guess is unverified. Check whether the job-potion family was sold by a job trainer or a Card Duelist vendor, or granted as a job reward, before adding a vendor row.",
  "Price, currency and retirement status are unknown (no coin store price in client; no wiki price).",
  "The client definition has no models and no tints/variants beyond the single definition 68790."
 ]}
