<!-- fleet job=citem-infer id=ccheesy-bread-pudding-96658-v1 status=done turns=9 usd=0.0061 tokens(read,write,in,out)=[121186, 22500, 20, 4082] model=claude-haiku-5-5 -->
# Cheesy Bread Pudding

{"item": {"name": "Cheesy Bread Pudding", "locale_id": 96658, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Cheesy Bread Pudding' is locale:96658, description 'Eating this food temporarily increases your timing as a blacksmith, chef, miner, and postman.', definition id 31252, slot 0, class 9 (food/consumable), no coin store price in the client definition.", "source": "locale:96658; refs: FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json (Comment 'Cheesy Bread Pudding'); quest-lines/citem-packs.json key ccheesy-bread-pudding (pack data)"},
  {"claim": "Its client cluster (96656-96662: Cheese-stuffed Ham, Ground Veal Quesadillas, Hot Cheese Fondue, Carrot Cheesecake, Cheesy Ritzy Bits, Sparkling Banana) is a set of same-family cooking foods with the same blacksmith/chef/miner/postman buff text.", "source": "locale:96656-96662; quest-lines/citem-packs.json (Cheese-stuffed Ham pack, client_cluster)"},
  {"claim": "A wiki Station Cash food list (page id 2242 wikitext, 'Food and Drink' section) prices the sibling foods Cheese Stuffed Ham, Hot Cheese Fondue and Cheezy Rizty Bitz (= Cheesy Ritzy Bits) at SC 45 each. Cheesy Bread Pudding, Ground Veal Quesadillas, Carrot Cheesecake and Sparkling Banana are NOT on that list.", "source": "refs: freerealms-wiki/wikitext/2242-43382-0a935accf24e.wiki lines 585-618"},
  {"claim": "No repo vendor, store, quest, or recipe entry references this item's name or locale 96658; no wiki article, article fact, or video frame names it.", "source": "repo search 'Cheesy Bread Pudding|31252|96658' (only unrelated id hits); lookup over client/wiki/articles/video (no hits beyond locale:96658)"}
 ],
 "confidence": 0.2,
 "open": [
  "No verified acquisition source. The pack's 'vendor' guess is unsupported: no coin vendor stocks it in our repo data, and the client definition has no coin store price.",
  "Sibling foods (Cheese-stuffed Ham, Hot Cheese Fondue, Cheesy Ritzy Bits) appear on the Station Cash food list at SC 45, but Cheesy Bread Pudding is absent from that list. Whether it was ever sold on the SC Marketplace, or was a craft/quest/event food, is unknown.",
  "Wiki spelling differs from client name ('Cheezy Rizty Bitz' vs 'Cheesy Ritzy Bits'); matching by exact name will miss sibling entries.",
  "Retired status and live status are unknown; no source states either.",
  "Crafting is plausible (chef/blacksmith/miner/postman buffs) but no recipe in repo references this item; needs checking against recipe data or a wiki Cooking page.",
  "Client definition is in the 2009 client build; no later price or removal evidence was found."
 ]}
