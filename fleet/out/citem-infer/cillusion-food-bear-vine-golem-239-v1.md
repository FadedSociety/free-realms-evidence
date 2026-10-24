<!-- fleet job=citem-infer id=cillusion-food-bear-vine-golem-239-v1 status=nothing_found turns=4 usd=0.0040 tokens(read,write,in,out)=[36507, 19902, 10, 2204] model=claude-haiku-5-5 -->
# Illusion Food - Bear Vine Golem

{"item": {"name": "Illusion Food - Bear Vine Golem", "locale_id": 239, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text for locale 239 is the item name 'Illusion Food - Bear Vine Golem'; the client defines one item (definition id 2944), slot 0, class 9, no model files, no coin store price.", "source": "client definition in pack; locale:239"},
  {"claim": "Item description: 'Eating this food will temporarily change the player into a Bear Vine Golem.' (a Illusion-type food that applies a timed transformation).", "source": "locale:2720"},
  {"claim": "The 'Bear Vine Golem' form is a real in-game creature: NPC 'Vine Golem Bear' (ability 'Vine Golem Bear - Plant Vines', 'CHOMP CHOMP CHOMP') and Croaking Vale quest objectives 'Defeat the Vine Golem Bears' / 'Knock out 5 Vine Golem Bears'.", "source": "locale:4192, locale:4193, locale:4195, locale:20474, locale:20475"},
  {"claim": "Sibling Illusion Food items in the same client cluster (Floren, Yeti, Owl, Bat, Man-Eating Plant, Wolf Vine Golem) are likewise transformation foods; the wiki has an item tooltip for a sibling 'Bark Chocolate' with the same mechanic (30-minute floppy-eared dog form), but no tooltip or page for this item.", "source": "lookup wiki image:item_tooltip 'Bark chocolate.jpg'; client cluster locale:234-244"}
 ],
 "confidence": 0.2,
 "open": [
  "No source found: no wiki page or tooltip, no article or forum fact, no video frame, no coin vendor (stores.json has no item_id 2944 entry), no quest reward, drop, event, or prize-wheel mention in the repo or refs.",
  "The client's 'Illusion Food' items may come from a holiday/event or a Station Cash/promotion pack; this cannot be confirmed from the evidence provided. Do not assign a source until one is found.",
  "Duration of the transformation is not given for this item (the sibling Bark Chocolate says 30 minutes); unverified.",
  "Live status is unverified: the cheap-model tag says 'live: yes' but nothing in the pack confirms it.",
  "Repo data mentions 'Bear Vinegolem' NPC model files (bear_vinegolem.adr, bear_vinegolem_fungus.adr) but these are NPC models, not this food's source."
 ]}
