<!-- fleet job=citem-infer id=cchef-s-flair-shard-of-magma-132130-v1 status=done turns=6 usd=0.0031 tokens(read,write,in,out)=[40988, 12224, 14, 2371] model=claude-haiku-5-5 -->
# Chef's Flair Shard of Magma

{"item": {"name": "Chef's Flair Shard of Magma", "locale_id": 132130, "kind": "other"},
 "sources": [{"type": "coin_shop", "detail": "Coin store sale (vendor/shop not named in any source; store data lists it under category 124, the same category as the other flair shards in the 75672-75689 block)", "where": null, "price": "1500 coins (purchase); member price 1350 coins (10% member discount); sell price 150 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75684 (line 15482)"}],
 "retired": null,
 "live": "unsure",
 "evidence": [{"claim": "Client name is 'Chef's Flair Shard of Magma', locale 132130, one definition (75684), slot 13, class 21.", "source": "locale:132130"}, {"claim": "Store data sells item 75684 for 1500 coins, member price 1350, sell price 150.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75684"}, {"claim": "Sibling set: Chef's flair shards of Magma, Gourmet Pizazz, Glamour, Valentines, Smoldering, Cleanliness, Charbroiled, Music for your Mouth and others are listed in the wiki chef NPC sell lists (Nadia, Mikael, Ingrid, Zamzani, Rachael, Skye); the Magma one is not named in any of those lists.", "source": "wiki pages: Nadia, Mikael, Ingrid, Zamzani, Rachael, Skye"}, {"claim": "Other Magma flair shards exist for Archer, Brawler, Medic, Ninja, Warrior, Wizard and Blacksmith (locale 130983-132094), so the Magma line is a multi-job set.", "source": "locale:130983, locale:131048, locale:131113, locale:131178, locale:131243, locale:131308, locale:132094"}],
 "confidence": 0.35,
 "open": ["The coin vendor that stocks item 75684 is unidentified. No repo vendor file references 75684, and no wiki page, article, or video names 'Shard of Magma'. The 1500-coin price is the only source.",
   "Which NPC or shop sells it, and whether it is a Coin Shop item or a Chef-specific vendor, is unverified. The wiki Coin Shop page's Flair Shards section was not fully read.",
   "Whether it is still sold or was retired is unknown. The store row's source tags (L1, L2, L4, R2, T633, R1) are not decoded here.",
   "Its in-game effect and level requirement are unknown; the client description is empty.",
   "The first-pass guess of 'vendor' is consistent with the store price but is not independently confirmed."]}
