<!-- fleet job=item-infer id=ielves-v1 status=nothing_found turns=2 usd=0.0012 tokens(read,write,in,out)=[3211, 5036, 6, 1162] model=claude-haiku-5-5 -->
# Elves

{"item": {"name": "Elves", "locale_id": null, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "no",
 "evidence": [
  {"claim": "The wiki page 'Elves' is a race article (Category:Races, Category:Elves), not an item page. It has no prices, no sale info, and no acquisition info.", "source": "https://freerealms.fandom.com/wiki/Elves"},
  {"claim": "The page states Elves are a race native to Silver Hills, sealed behind the Crystal Barrier, and that players cannot choose them as a race.", "source": "https://freerealms.fandom.com/wiki/Elves"},
  {"claim": "The client text for 'Elves' is NPC dialog only (e.g. Elves npc_dialog locale:45142, locale:45148; Silversnow quest_dialog locale:45141). No item name matches.", "source": "locale:45141"},
  {"claim": "The only repo hit for 'Elves' is a name string inside prototype/osfr-tools/data/content/vendors_unresolved.json:5946, an unresolved vendor entry with no item attached in the pack.", "source": "repo:prototype/osfr-tools/data/content/vendors_unresolved.json:5946"},
  {"claim": "No coin vendor, Marketplace, Coin Shop, quest reward, drop, event, or prize wheel entry in the pack names an Elves item.", "source": "vendor_stock empty; mentioned_by_other_answers empty"}
 ],
 "confidence": 0.9,
 "open": [
  "The input asks for an item's sources, but 'Elves' is a fictional race, so there is no item to source. Likely the wrong page was passed in; check whether an item such as an Elf costume, pet, or Chugzy-related item was intended.",
  "vendors_unresolved.json:5946 contains the string 'Elves'. Check what that entry is before treating it as an item, since it is unresolved and may be a race or NPC tag."
 ]}
