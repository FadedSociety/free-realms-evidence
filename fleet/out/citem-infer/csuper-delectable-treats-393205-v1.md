<!-- fleet job=citem-infer id=csuper-delectable-treats-393205-v1 status=nothing_found turns=8 usd=0.0050 tokens(read,write,in,out)=[89949, 21015, 18, 3024] model=claude-haiku-5-5 -->
# Super Delectable Treats

{"item": {"name": "Super Delectable Treats", "locale_id": 393205, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition: definition_id 56782, slot 205, class 73, description 'A high quality pet food. Your pet will get full faster when eating this food.' (locale:3963728243 is the same description line, listed as the high-quality food tier in the Pet Trainer guide). No coin store price in the client definition (coin_store_prices empty), so no coin vendor sale is evidenced.", "source": "repo:notes/Build Guides/Content/Jobs/Pet Trainer.md:247 (food tier table, [client]); refs citem-packs.json entry csuper-delectable-treats-393205"},
  {"claim": "The item is a pet-care consumable in the same family as Super Pet Food, Basic Pet Food, and the Super Cat Food tiers; the Pet Trainer guide lists these as [client] only, with no vendor, quest or drop source.", "source": "repo:notes/Build Guides/Content/Jobs/Pet Trainer.md:247"},
  {"claim": "Name locale 393205 sits in a cluster with Heavy Duty Scrub Brush (393207), Super Cleansing Shampoo (393208) and Queen Valerian quest text (393200-393204), plus two NOT LIVE / devtest strings (393209, 393210). The cluster is a test-quest block, which suggests these items were not tied to a live Valerian quest reward, but this is not proven.", "source": "locale:393200..393210 (client_cluster in pack)"},
  {"claim": "No wiki page, article, video frame or other answer names Super Delectable Treats. Searches of the wiki, articles and video returned nothing, and the repo notes contain no source for it.", "source": "lookup wiki/articles/video; search repo notes"},
  {"claim": "The first-pass tag 'vendor' is a hint only. No vendor stock list in the pack includes it.", "source": "jev_first_pass; vendor_stock []"}
 ],
 "confidence": 0.2,
 "open": [
  "No verified source. The first-pass 'vendor' guess has no evidence; do not record a vendor sale until a store entry or wiki/video proof is found.",
  "Check the coin-store data (repo:data/content/stores.json) for definition 56782 or the item name; the pack's coin_store_prices is empty, which points away from a coin sale but does not rule out a station cash or other store.",
  "Check whether the pet food tiers (Basic, Super Pet Food) were sold by a Cobblestone pet vendor (Jennifer or Gloria, see Pet Trainer guide) and whether this high-tier food was ever in the same stock list.",
  "Live status is unsure. The name cluster includes NOT LIVE/devtest strings, but the food itself is not flagged not_live in the client.",
  "Description matches a food tier name in the Pet Trainer guide but the guide gives no sources; the Pets guide was not checked for food sources."
 ]}
