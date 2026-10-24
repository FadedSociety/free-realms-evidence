<!-- fleet job=citem-infer id=creplenishing-potion-1-37541-v1 status=nothing_found turns=3 usd=0.0032 tokens(read,write,in,out)=[17315, 15799, 8, 2067] model=claude-haiku-5-5 -->
# Replenishing Potion 1

{"item": {"name": "Replenishing Potion 1", "locale_id": 37541, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Replenishing Potion 1' (locale 37541), description 'This potion restores health and energy.' (locale 37542), definition id 3080, slot 0, class 9, no coin store price in the client definition (coin_store_prices empty).", "source": "locale:37541; locale:37542; refs quest-lines/citem-packs.json creplenishing-potion-1-37541"},
  {"claim": "Sibling potion names sit in the same client block: 'Replenishing Potion II (PH)' (37543) and 'Replenishing Potion IV (PH)' (37545) are flagged placeholder; 'Replenishing Vial' (37544) and 'Replenishing Potion' (37546) are unflagged. Tier-numbered variants appear to be a potion ladder, but the pack does not confirm which tiers shipped.", "source": "locale:37543; locale:37544; locale:37545; locale:37546; refs quest-lines/flags.tsv:6658-6659"},
  {"claim": "The nearby dialog (locale 37536-37539: 'it was probably just a... squirrel', 'no need to tell Cal about that!') is from the Roaming Sasquatch NPC (locale 37540). The client does not tie the potion to that dialog or quest.", "source": "locale:37536-37540"},
  {"claim": "Repo searches for definition id 3080 and the name found no store, vendor, quest, recipe or drop entry for this item. Lookup of the name in client, wiki, articles and video returned no wiki page, article fact or video frame for it.", "source": "repo search; lookup (client, wiki, articles, video)"},
  {"claim": "Related but different item: 'Jumbo Replenishing Potion' (locale 1942) is a Trading Card Game virtual reward (wiki: acquired from the Free Realms Trading Card Game virtual reward cards). It is not this item.", "source": "wiki page Jumbo Replenishing Potion; refs quest-lines/citem-packs.json"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found. The item is not in any coin vendor stock, has no coin store price, and no wiki page, article, or video names it.",
  "Live status is unverified: the first-pass 'live: yes' is a hint only. The PH-flagged siblings suggest the potion ladder was partly placeholder content.",
  "Possible links to check: the Roaming Sasquatch NPC and its quest (locale 37536-37539 dialog) for a quest reward; the 'Potion vendor' NPC dialog (locale 70415, 'Replenishing potions, here!') for a vendor sale. Neither is tied to item 3080 in the sources checked.",
  "Check the repo's crafting recipes and collection catalogue for item definition 3080 (not found by a plain-text search)."
 ]}
