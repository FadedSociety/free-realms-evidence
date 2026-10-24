<!-- fleet job=citem-infer id=csuper-piggie-pie-116319-v1 status=nothing_found turns=4 usd=0.0028 tokens(read,write,in,out)=[24840, 12193, 10, 2053] model=claude-haiku-5-5 -->
# Super Piggie Pie

{"item": {"name": "Super Piggie Pie", "locale_id": 116319, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is 'Super Piggie Pie' (locale 116319); 'Piggie Pie' is locale 116318, in the same pet-food cluster (116314-116324: Mystery Meat Treats, Munchie Cake, Succulent Squeaky Snacks, Protein Pup Pops, Basic Pet Food and their Super/plain variants).", "source": "locale:116319; locale:116318; locale:116314-116324"},
  {"claim": "Client description 'A high quality pet food. Your pet will get full faster when eating this food.' matches the top food tier of the Pet Trainer food family (Simple/Basic/Super Pet Food), which the Pet Trainer guide records as client-only, with no sources.", "source": "locale:3963728243 (cited in notes/Build Guides/Content/Jobs/Pet Trainer.md line 247)"},
  {"claim": "Pet food is used up on feeding (not kept), per the Pet Trainer guide.", "source": "notes/Build Guides/Content/Jobs/Pet Trainer.md line 251"},
  {"claim": "Repo search for 'Piggie' and 'Pet Food' in data stores found no vendor, store, recipe or quest entry for this item; the only hit is a pet label 'Simple Pet Food' in pets.json.", "source": "repo:prototype/osfr-tools/data/content/pets.json:1495"},
  {"claim": "Lookup of the name in wiki, articles and video returned only the client text lines; no wiki page, article fact or video frame names this item.", "source": "lookup (client, wiki, articles, video), 'Piggie Pie'"}
 ],
 "confidence": 0.2,
 "open": [
  "No real source found. Client definition 37056 has no coin store price (coin_store_prices empty), so no coin vendor sale is evidenced.",
  "No wiki article, vendor, quest, drop, or event names Super Piggie Pie; the Pet Trainer guide's food family lists the tier names without sources.",
  "Live status unverified: the first-pass 'live: yes' is only a hint and is not backed by any source; the client text exists, but that does not show it was sold or dropped.",
  "Likely candidates to check: the Pet Trainer/pet-food vendors and the Cobblestone pet vendors (Jennifer, Gloria) noted in the guide, the Forest Friends pet-food quest, and the Pets guide. None of these have been confirmed to stock this item.",
  "Tier words in the description ('high quality') suggest it sits above Basic Pet Food; the exact price tier and whether it was a Coin Shop or Station Cash item remain unknown."
 ]}
