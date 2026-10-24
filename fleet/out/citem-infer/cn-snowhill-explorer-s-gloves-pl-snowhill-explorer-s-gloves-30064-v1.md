<!-- fleet job=citem-infer id=cn-snowhill-explorer-s-gloves-pl-snowhill-explorer-s-gloves-30064-v1 status=done turns=5 usd=0.0042 tokens(read,write,in,out)=[37013, 17127, 12, 3279] model=claude-haiku-5-5 -->
# {n}Snowhill Explorer's Gloves{pl="Snowhill Explorer's Gloves"}

{"item": {"name": "Snowhill Explorer's Gloves", "locale_id": 30064, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 30064, '{n}Snowhill Explorer's Gloves', item class 1, slot 2 (hands), two definitions (16256, 17630) with two model files (female gloves, male fingerless gloves).", "source": "locale:30064; client definition from pack"},
  {"claim": "Sibling pieces of the same Snowhill Explorer set exist in the client: Backpack (29164), Midriff Shirt (29402), Boots (29884), Hat (30273), Pants (30604), Shirt (31010), plus 'Elite Snowhill Explorer' (419916).", "source": "locale:29164, locale:29402, locale:29884, locale:30273, locale:30604, locale:31010, locale:419916"},
  {"claim": "The same explorer-set family (Blackspore Explorer's Gloves, Backpack, Hat, Boots, Midriff Shirt) appears in a Blackspore treasure chest reward screen, and Seeker's and Pathfinder's explorer pieces come from Rare Exploration rewards, so Snowhill Explorer pieces are likely chest/Rare Exploration rewards.", "source": "video:SdVAc6iTuK4/00000.jpg; video:Y_ANZvYraKI/00018.jpg; video:45PgwOt0gMI/00024.jpg (family pattern only, not a Snowhill gloves sighting)"},
  {"claim": "The Snowhill Rare Exploration collection exists on the wiki (collection coin 'Between the Peaks').", "source": "wiki Template:News (Game Update 115 Overview 10/15/2013)"},
  {"claim": "The pack's coin price of 270 does NOT belong to the gloves: repo stores.json lists 270-coin category-6 entries for item ids 29878-29888 and 29884 (Snowhill Explorer's Boots, 270 coins, member price 243, sell 27), but no entry for 30064 or 16256/17630 exists in the repo.", "source": "repo:prototype/osfr-tools/data/content/stores.json:11020-11026 (item 29884)"},
  {"claim": "The wiki has no article for the gloves; no vendor stock, quest reward, drop or prize-wheel entry naming them was found in the pack or repo.", "source": "lookup/search of repo, wiki, articles, video (no hits for 'Snowhill Explorer's Gloves')"}
 ],
 "confidence": 0.2,
 "open": [
  "Coin store price 270 in the evidence pack is unverified for these gloves: the only 270-coin Snowhill Explorer entry in stores.json is Boots (29884); gloves 30064 are not in stores.json. Treat as not a confirmed coin vendor sale until checked.",
  "No source confirmed. Likely source is the Snowhill Rare Exploration / chest reward family, but no direct evidence names the gloves; needs a wiki page, video frame of the reward, or a Snowhill chest/vendor check.",
  "Live status unsure: first-pass 'live: yes' is a hint only, and no article or wiki page confirms current availability or retirement.",
  "Definition ids 16256 and 17630 are two variants (female gloves and male fingerless gloves); not verified whether both are sold or rewarded.",
  "Repo reference data/reference/weapons.json line 6327 has an id 30064 entry; it appears unrelated to this glove and was not examined further."
 ]}
