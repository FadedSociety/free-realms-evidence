<!-- fleet job=citem-infer id=ctempest-woven-long-cloak-5832-v1 status=done turns=5 usd=0.0034 tokens(read,write,in,out)=[25394, 12543, 12, 3084] model=claude-haiku-5-5 -->
# Tempest Woven Long Cloak

{"item": {"name": "Tempest Woven Long Cloak", "locale_id": 5832, "kind": "clothing"},
 "sources": [
  {"type": "other", "detail": "Wizard job gear progression: 'Tempest Woven' is listed in the Wizard clothing list at Level 15 (the wiki lists the set name only, not the cloak piece, and gives no vendor or price)", "where": null, "price": null, "currency": null, "source": "wiki page Wizard (Clothing, Level 15); refs freerealms-wiki/wikitext/2021-46067-7800a9f3f1fa.wiki lines 170-171"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name is locale:5832 'Tempest Woven Long Cloak'; the same name family includes Tempest Woven Fez (5828), Tempest Woven Shoes (5838), Tempest Woven Skirt (5848), Tempest Woven Slacks (5852).", "source": "locale:5832; locale:5828; locale:5838; locale:5848; locale:5852"},
  {"claim": "Wizard wiki page lists 'Tempest Woven' as a Level 15 Wizard clothing item, with no acquisition method given.", "source": "refs freerealms-wiki/wikitext/2021-46067-7800a9f3f1fa.wiki lines 170-171; wiki page Wizard (lookup result)"},
  {"claim": "The 'Tempest Woven' name on the Blacksmith recipe list and Wand is a weapon (Tempest Woven Wand, Level 12 Wizard weapon, Blacksmith recipe). It does not cover the cloak.", "source": "wiki page Tempest Woven Wand; wiki page Blacksmith"},
  {"claim": "Client-side 'Elite Black Tempest Woven Long Cloak' (locale:25851) is a separate variant name, not this item.", "source": "lookup locale:25851"}
 ],
 "confidence": 0.3,
 "open": [
  "No vendor, coin shop, marketplace or drop source is documented for this cloak. The first-pass 'vendor' guess is unsupported.",
  "The client coin_store_prices [715, 9453] are not verified. In repo, id 715 is 'Copper Mining' (an activity/leaderboard entry in notes/Research/original-activity-coverage.json:13494), not a store item. repo data/content/stores.json was not found at the path searched, so the store prices 715 and 9453 could not be checked against a store item. Do not cite them as coin vendor sales until stores.json is found.",
  "The wiki's Level 15 Wizard clothing entry is 'Tempest Woven' with no piece name. It may refer to the full set or one piece; the cloak's exact tie to that Level 15 entry is unconfirmed.",
  "Retired status and later availability are unknown: no wiki or article source in the pack says the piece was retired.",
  "Client shows 15 definitions across races and genders; the pack gives no per-variant price or source.",
  "Wiki and client searches found no article, video frame, or image for this cloak. Check the Wizard job's clothing vendors and the Wizard job trainer before finalizing a source."
 ]}
