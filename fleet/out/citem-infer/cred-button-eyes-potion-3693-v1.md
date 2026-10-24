<!-- fleet job=citem-infer id=cred-button-eyes-potion-3693-v1 status=done turns=7 usd=0.0047 tokens(read,write,in,out)=[55007, 13512, 16, 4846] model=claude-haiku-5-5 -->
# Red Button Eyes Potion

{"item": {"name": "Red Button Eyes Potion", "locale_id": 3693, "kind": "consumable"},
 "sources": [
  {"type": "collection", "detail": "Okay Buttons collection (catalogue id 98, name_id 7749): completion reward of 5x Red Button Eyes Potion (item 55404), plus 5x item 55406, 1x item 3776 and 3 coins. The reward block also adds collection 99 (Better Buttons).", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:7869-7896 (reward for collection 98); locale:7749 'Okay Buttons'; wiki page 'List of Collections' (Buttons set: Okay, Cool, Better, Awesome, then 'Button [Eyes] [Potion]' as Final Reward)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Red Button Eyes Potion' is locale 3693; description 'This potion gives humans button eyes!' is locale 3704; definition ids 55404 (red) and 55405 (matching variant).", "source": "locale:3693; locale:3704; pack client_definition"},
  {"claim": "Sibling potions Orange/Yellow/Green/Cyan/Blue/Purple/Magenta Button Eyes Potion are locales 3694-3700; pixie description for Blue is locale 3705.", "source": "locale:3694-3700, locale:3705"},
  {"claim": "Collection catalogue reward for the Okay Buttons collection grants item 55404 x5.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:7877-7878"},
  {"claim": "Wiki 'List of Collections' lists the Buttons set (Okay, Cool, Better, Awesome Buttons) ending in a 'Button [Eyes] [Potion]' final reward.", "source": "wiki: List of Collections"},
  {"claim": "Buttons collection names: locale 7749 Okay, 7750 Better, 7751 Cool, 7752 Awesome Buttons.", "source": "locale:7749-7752"}
 ],
 "confidence": 0.5,
 "open": [
  "Conflict: the wiki calls the Button Eyes Potion the Final Reward of the Buttons set, but the catalogue attaches the 5x potion reward to the Okay Buttons block (id 98), which unlocks Better Buttons (id 99). Either the catalogue reward is per-stage or the wiki column is misread; verify in-game before finalizing.",
  "No coin store price, vendor stock, quest reward, or drop found for the Red potion. Coin-shop/marketplace status is unknown.",
  "The catalogue reward is a count of 5 per completion; the wiki does not give a count. Whether the potion is repeatable from the collection is unverified.",
  "Pack says both definitions 55404 and 55405 share this name, but locale 3705 (pixie, Blue) suggests 55405 may be a different colour/race variant. Verify 55405's name and race split.",
  "Retired/live status not confirmed by any source. The item and collection exist in the shipped data, but no end date was found. Treat as live=unsure.",
  "The 'Okay Buttons' reward block also gives 5x item 55406 and 1x item 3776; these are not identified here."
 ]}
