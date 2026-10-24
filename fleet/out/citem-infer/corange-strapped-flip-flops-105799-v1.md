<!-- fleet job=citem-infer id=corange-strapped-flip-flops-105799-v1 status=done turns=5 usd=0.0029 tokens(read,write,in,out)=[28112, 10711, 12, 2620] model=claude-haiku-5-5 -->
# Orange-Strapped Flip-Flops

{"item": {"name": "Orange-Strapped Flip-Flops", "locale_id": 105799, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Seaside merchant (unnamed on the wiki 'Flip Flops' page; the item is the orange-strapped variant of the Flip Flops feet clothing line)", "where": "Seaside", "price": "270 (coin store price in the client pack; not confirmed, see open)", "currency": "coins", "source": "wiki page 'Flip Flops' (\"can be brought from a merchant in Seaside\"); repo:prototype/osfr-tools/data/content/stores.json (purchase_price_coins 270 entries, e.g. line 78, but no entry for the pack's definition id 7291 was found)"},
  {"type": "quest_reward", "detail": "Quest 'Horrible Hiccups' (Slinky, Seaside), final reward", "where": "Seaside", "price": null, "currency": null, "source": "wiki Quest:Horrible Hiccups (first reward, per the pack; the wiki quest page excerpt returned did not show the reward list itself) and locale:101396"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Item name is client text locale:105799 'Orange-Strapped Flip-Flops', an item-class entry", "source": "locale:105799"},
  {"claim": "Flip Flops are a feet-slot clothing item obtainable from a merchant in Seaside", "source": "wiki page Flip Flops"},
  {"claim": "Wiki Farmer and Adventurer outfit lists include 'Orange Strapped [Flip Flops]' alongside other clothing, showing it is a wearable clothing item in the same line", "source": "wiki pages Farmer, Adventurer"},
  {"claim": "Quest Horrible Hiccups requires an active Membership, starts with Slinky in Seaside, and is followed by Scaredy Pants; the pack lists the Flip-Flops as its final reward", "source": "wiki Quest:Horrible Hiccups; wiki Slinky; wiki Cutes Dozen; locale:101396"},
  {"claim": "Client definition has 36 variants (12 listed IDs shown), feet/sandal model freestyle_<race>_<gender>_feet_sandals.adr, slot 5", "source": "client definition in pack"}
 ],
 "confidence": 0.45,
 "open": [
  "Coin price 270 is from the pack's client data but could not be tied to this item: no stores.json entry for definition id 7291 or 32717 was found, so the 270 may belong to another item. Treat the vendor price as unverified.",
  "The specific Seaside merchant who sells the item is not named in the sources; the wiki says only 'a merchant in Seaside'.",
  "Quest reward claim rests on the pack's quote of the wiki Horrible Hiccups page; the wiki page text I could read did not show its reward list, so it is unconfirmed by me.",
  "Whether the item was retired or is still sold is not stated by any source; live is marked yes from the first-pass tag and the wiki's present-tense wording, not from a dated source.",
  "Lifeguard Flip-Flops (locale:105834) is a separate client item and was not covered here."
 ]}
