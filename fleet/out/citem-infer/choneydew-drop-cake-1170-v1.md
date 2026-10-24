<!-- fleet job=citem-infer id=choneydew-drop-cake-1170-v1 status=nothing_found turns=4 usd=0.0038 tokens(read,write,in,out)=[31091, 17891, 10, 2448] model=claude-haiku-5-5 -->
# Honeydew Drop Cake

{"item": {"name": "Honeydew Drop Cake", "locale_id": 1170, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 'Honeydew Drop Cake' (locale 1170), definition id 4011, one definition, slot 0, item class 9. Description: 'Eating this food will change the player into a female bixie gatherer for thirty minutes.' No model files and no coin store price.", "source": "client definition in evidence pack; locale:1170"},
  {"claim": "It belongs to the 'Illusion Food' family: the neighbouring client strings are locale 1166-1169 (Illusion Food - Dove/Eagle/Hawk/Raven) and 1165 (Giant Bat Illusion Scroll). The family is large (Illusion Food - Buck, Owl, Chick, Snake, Snow Hog, Man-Eating Plant and others), so the cake is most likely a sibling of these illusion consumables.", "source": "locale:1165-1175 (client cluster); repo locale dumps e.g. opening-mining-native-20261009T121330Z/locale/en_us_data.dat ids 51390001, 135164033, 236406148"},
  {"claim": "The wiki's illusion-food item tooltip format is shown for Bark Chocolate ('Eating this [food] will change the player into a large floppy eared dog for thirty minutes', Resell Value 18, Cannot Sell, Cannot Trade). This is a sibling item, not a source for Honeydew Drop Cake.", "source": "lookup wiki image:item_tooltip 'Bark chocolate.jpg'"},
  {"claim": "The only client text naming 'Honeydew' is an NPC (Honeydew, horse who minds foals in Pony Vale, Skysong Ledge) and her quests. None of those quest strings mention the cake, so they do not source it.", "source": "locale:1224692624 (Honeydew); locale:819268604; locale:453574182; repo:build guide notes/Build Guides/Content/NPCs/NPCs - Sunstone Valley.md:146"}
 ],
 "confidence": 0.2,
 "open": [
  "No wiki article, image, article fact, video frame, vendor stock, coin-store price, or other answer names Honeydew Drop Cake. No source can be cited, so the sources list is empty.",
  "Where the cake was obtained is unknown: illusion foods may come from vendors, drops, events or crafting, but no evidence in this pack shows which.",
  "The first-pass tag (live: yes) is a hint only. The client defines the item, but whether it is still obtainable is not shown; retired status is null.",
  "Check the wiki for an 'Illusion Food' category or a page for the bixie illusion foods (Dove, Eagle, Hawk, Raven) to see whether they share a source; if they do, the cake probably does too.",
  "Repo search for definition 4011 in stores/vendor/recipe JSON returned no matches, so no coin vendor stocks it in our data."
 ]}
