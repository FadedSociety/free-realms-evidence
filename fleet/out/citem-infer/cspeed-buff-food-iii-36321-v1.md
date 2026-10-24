<!-- fleet job=citem-infer id=cspeed-buff-food-iii-36321-v1 status=nothing_found turns=4 usd=0.0031 tokens(read,write,in,out)=[30102, 14287, 10, 1959] model=claude-haiku-5-5 -->
# Speed Buff Food III

{"item": {"name": "Speed Buff Food III", "locale_id": 36321, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Speed Buff Food III' is locale 36321 (item type); the set is Speed Buff Food I-V (locale 36319-36323).", "source": "locale:36321; locale:36319; locale:36320; locale:36322; locale:36323"},
  {"claim": "Client definition: definition id 2985, class 9, slot 0, no model files, no coin store price in stores data. Description text 'Eating this food will temporarily increase the run speed of the player.' is in the client definition pack.", "source": "client definition pack (definition_ids 2985)"},
  {"claim": "Other food buff descriptions in the client text: 'Eating this food temporarily increases your maker's speed.' (locale:97392), 'Eating this food temporarily increases your maker's reach and maker's speed.' (locale:97382), 'Eating this food temporarily increases your maker's sense and maker's speed.' (locale:97391), 'Eating this food will temporarily increase the speed health is regained when not fighting.' (locale:442508). These are different foods, not this item's text.", "source": "locale:97392; locale:97382; locale:97391; locale:442508"},
  {"claim": "Lookup of the wiki, articles, video and client text for 'Speed Buff Food' found no wiki page, article fact, or video frame naming this item. Repo search for definition id 2985 and the name found only locale dumps and unrelated NPC ids, with no vendor, recipe, quest or drop entry.", "source": "lookup (wiki, articles, video, client); repo search"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found. The name is client-defined and the item has no store price, wiki article, quest, drop, recipe or vendor entry in our data. The first-pass 'source_guess: unknown' is not confirmed.",
  "The 'run speed' description with a 'Charge' ability client cluster (locale 36324-36325, Frostfang Cavern) may hint at a Frostfang or cooking-food context, but no source supports this.",
  "Live status is unverified. The first pass says live 'yes', but no evidence supports it. Check the live client's food/cooking recipe lists or the Cook job's recipe data for food IDs 2985 and nearby.",
  "The description text also needs checking: the client description for this item may differ from the 'run speed' line in the pack. Confirm with locale id for the item description.",
  "Pack gave 'mentioned_by_other_answers' and 'vendor_stock' empty; no cross-check available."
 ]}
