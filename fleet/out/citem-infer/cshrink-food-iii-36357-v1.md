<!-- fleet job=citem-infer id=cshrink-food-iii-36357-v1 status=nothing_found turns=6 usd=0.0055 tokens(read,write,in,out)=[72134, 24037, 14, 3566] model=claude-haiku-5-5 -->
# Shrink Food III

{"item": {"name": "Shrink Food III", "locale_id": 36357, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text: locale 36357 = 'Shrink Food III'; description locale 3162 = 'Eating this food will decrease the size of the player.'", "source": "locale:36357; locale:3162"},
  {"claim": "Legacy item definition Id 2995, Type 1, Class 9, SingleUse true, CategoryId 10, ActivatableAbilityId 1943, NonMiniGame true, Cost 180, MemberDiscount 10, Icon 929. The 'Cost' field is a legacy item cost, not a Coin Shop or vendor price, and repo stores.json has no item 2995.", "source": "refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:55842-55861; repo data/content/stores.json (no entry for 2995)"},
  {"claim": "The same definition block (DescriptionId 3162) is shared by Shrink Food I, II, IV, and Grow/Tiny-type siblings, so the description is shared and not unique to this item.", "source": "refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:55807, 55827, 55867, 55887"},
  {"claim": "Sibling client text in the same cluster: Shrink Food I (36353), II (36356), IV (36358), Tiny Tincture (36359), Grow Food I (36360, item), Grow Food II-V (36361-36364, tagged quest_reward). The Tiny Tincture Potion (151307) text says it makes you smaller.", "source": "locale:36353; locale:36356; locale:36358; locale:36359; locale:36360-36364; locale:151307"},
  {"claim": "Sanctuary and Lxzxrus community servers define item 2995 the same way, but no vendor, quest, or drop row for it was found in any of them.", "source": "refs:Sanctuary-PC2009-20261009/src/Resources/ClientItemDefinitions.json:62806; refs:Lxzxrus-Free-Realms-Server/src/Resources/ClientItemDefinitions.json:55844"},
  {"claim": "Searches of the wiki, articles, video, and the client text tables found no page, article, or video frame naming Shrink Food III, and no source for how it was obtained. The only 'Shrink' hits in the repo are unrelated code comments.", "source": "lookup (wiki, articles, video, client) for 'Shrink Food'; search repo and refs"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found: no vendor stock, coin-shop price, marketplace listing, quest reward, drop, event, or prize-wheel evidence. The vendor_stock and mentioned_by lists in the pack are empty.",
  "Legacy 'Cost: 180' is not confirmed as a coin price. Treat it as unverified until a store row or wiki price shows it.",
  "Live status is unknown. The definition exists in client and community data, but that alone does not show the item was ever sold or given out.",
  "Needs a wiki page or player report for Shrink Food I-IV or Tiny Tincture (possible Grow/Shrink food sources, e.g. a cooking or alchemy recipe, or a quest reward for the Grow Food line). Check the Sacred Glade cooking mention for a food-recipe link; that is only a guess, not evidence.",
  "Activatable ability 1943 (the shrink effect) has no client text of its own in this pack; the effect's duration and whether it stacks with the Tiny Tincture are unverified."
 ]}
