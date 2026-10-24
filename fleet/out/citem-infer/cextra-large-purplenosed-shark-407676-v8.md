<!-- fleet job=citem-infer id=cextra-large-purplenosed-shark-407676-v8 status=done turns=5 usd=0.0032 tokens(read,write,in,out)=[31317, 9671, 12, 3277] model=claude-haiku-5-5 -->
# Extra Large Purplenosed Shark

{"item": {"name": "Extra Large Purplenosed Shark", "locale_id": 407676, "kind": "other"},
 "sources": [
  {"type": "collection", "detail": "Entry in a fish collection (collection slot index 3, item definition 68077, name locale:407676). The parent collection is most likely 'Extra Large and in Charge' (locale:419595), which the wiki lists under Darklit Lagoon, but the parent link is not confirmed in the data.", "where": "Darklit Lagoon", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:23169-23173; locale:419595; wiki page Darklit Lagoon (Collections: 'Extra Large and in Charge')"},
  {"type": "drop", "detail": "Fishing catch of the Purplenosed Shark species (level 14+). The Extra Large grade being caught is NOT confirmed by any source; the species catch is what is evidenced.", "where": "Darklit Lagoon", "price": null, "currency": null, "source": "wiki page Darklit Lagoon ('Purplenosed Shark - Catchable at level 14'); repo:prototype/osfr-tools/data/content/fishing.json:767-771; repo:prototype/osfr-tools/data/content/fishing_spots.json:314-319 (68077 listed at line 318, positional only)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name for item 68077 is locale:407676 'Extra Large Purplenosed Shark'; Medium and Large grades are locale:407674 and 407675; species is locale:99932 'Purplenosed Shark'.", "source": "locale:407676; locale:407674; locale:407675; locale:99932"},
  {"claim": "Item 68077 sits in a collection catalogue entry with name_id 407676.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:23169-23173"},
  {"claim": "Wiki Darklit Lagoon lists the collection 'Extra Large and in Charge' and the species 'Purplenosed Shark - Catchable at level 14'. Wiki Fisherman page also lists the 'Extra Large and in Charge' collection.", "source": "wiki page Darklit Lagoon; wiki page Fisherman; locale:419595"},
  {"claim": "Quest 'Taking the Bait' (Darklit Lagoon Fisherman) asks the player to reel in the biggest / a large purplenosed shark at Darklit Lagoon. Objective and dialog text only; no reward recorded.", "source": "locale:409245; locale:409251; locale:409252"},
  {"claim": "Tiny Rib lure text is locale:412943 (10% higher chance for Spineless Stickleback, Calico Catfish, Purplenosed Shark). Locale 409564 has similar text.", "source": "locale:412943; locale:409564"},
  {"claim": "No coin store price, vendor stock, quest reward, enemy drop or event was found for item 68077.", "source": "client_definition coin_store_prices: []; vendor_stock: []; repo search for 68077"}
 ],
 "confidence": 0.35,
 "open": [
  "The XL grade being catchable is unverified. Only the collection slot (collection_catalogue.json:23169-23173) and the spot-list position (fishing_spots.json:318) point to it. No source gives a size threshold, catch rate or bait/level requirement for the XL grade.",
  "The parent collection of collection_catalogue entry 68077 is not confirmed; 'Extra Large and in Charge' is inferred from the name and the wiki.",
  "Previous answer's ids locale:2359191529 and locale:631467910 do not exist and are removed. Repo note repo:notes/Build Guides/Content/Jobs/Fisherman.md:277 still cites 631467910 and should be corrected to locale:412943 (not done here; notes are outside this job).",
  "Quest 'Taking the Bait' is an objective only. Wording ('biggest' purplenosed shark) hints the XL grade but is not a reward source; no quest-to-item link is recorded.",
  "Fishing is not a priced, quest, enemy or event source; the builder must decide how fishing catches are recorded. Not wireable as a priced source.",
  "Retirement unknown: wiki page undated, no retirement evidence found, so live is 'unsure'.",
  "Briarwood is not evidenced as a source for this item and is excluded."
 ]
}
