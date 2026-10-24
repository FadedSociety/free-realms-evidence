<!-- fleet job=citem-infer id=cgummyfruit-topped-sundae-38655-v3 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[7293, 9199, 6, 2164] model=claude-haiku-5-5 -->
# Gummyfruit Topped Sundae

{"item": {"name": "Gummyfruit Topped Sundae", "locale_id": 38655, "kind": "consumable"},
 "sources": [
  {"type": "crafting", "detail": "Chef cooking minigame recipe 43 (job Chef profile 45, min rank 1, minigame type 9). Ingredients: Bundle of Gummyfruit x4 (def 2875), Snowhill Ice Cream: Vanilla x3 (def 2895), Bundle of Starnut x3 (def 2886), Sugar x4 (def 2906). Output: 1 x Gummyfruit Topped Sundae (def 21817). Recipe pattern item: Gummyfruit Topped Sundae Recipe (def 55825, locale 387778). Pattern acquisition is not evidenced; the row is provisional. The recipe block's key is tagged 'reconstructed' in the data (recipes.json:1078-1080), so the output count and ingredients come from a reconstructed block.", "where": "Cooking table (Chef)", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/recipes.json:1044-1076 (recipe 1046 name, 1049 pattern def 55825, 1074 output def 21817); repo:notes/Build Guides/Content/Jobs/Chef.md:222 (ingredients, listed as [client] [wiki]); wiki: List of Recipes (Chef) per pack"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item def 21817 is named Gummyfruit Topped Sundae (locale 38655), food item class 9, slot 0. Client description: eating it temporarily increases talent as a Blacksmith, Chef, Miner and Postman.", "source": "locale:38655; client definition in pack (def 21817)"},
  {"claim": "Chef cooking recipe 43 produces def 21817 from the four listed ingredients; pattern item def 55825 is named in the same block.", "source": "repo:prototype/osfr-tools/data/content/recipes.json:1044-1076, 1117-1121 (pattern 55825, MinProfileRank 1)"},
  {"claim": "Wiki Chef page's Maker's Stats row lists the sundae with ingredients matching the recipe and effect 'Increases Maker's Reach', with 'none stated' for where-to-get. This conflicts with the client description and is unverified.", "source": "repo:notes/Build Guides/Content/Jobs/Chef.md:222; wiki: Chef (lookup)"},
  {"claim": "Pattern item name exists in client text: Gummyfruit Topped Sundae Recipe, locale 387778. No vendor, quest or other sale of the pattern was found.", "source": "locale:387778"},
  {"claim": "Bordon Cloo's 'Learning to Crave the Flave' (M3) asks for one sundae. This is a cooking task requirement, not a reward, so it is not listed as a source.", "source": "repo:notes/Build Guides/Content/Jobs/Chef.md:112; locale:384674, locale:384675"},
  {"claim": "Cooking objectives exist (Score 10,000 on Gummyfruit Topped Sundae; Mix up a Gummyfruit Topped Sundae!). These are objectives, not acquisitions.", "source": "locale:73332, locale:102367, locale:386045"},
  {"claim": "No coin store price, vendor stock, prize wheel, event, membership or promotion source was found in the pack or the lookup of client, wiki and articles.", "source": "client definition coin_store_prices empty; vendor_stock empty; lookup results"}
 ],
 "confidence": 0.4,
 "open": [
  "Wireable: NOT wireable. The only source is the crafting row, which has no price, quest, enemy or event, and the recipe pattern (def 55825, locale 387778) has no evidenced acquisition. The crafting row stays provisional until the pattern is sourced.",
  "Effect conflict is unresolved: client description says talent boost for Blacksmith, Chef, Miner and Postman; wiki Chef page says 'Increases Maker's Reach' (unverified). Both are kept; neither is chosen as final.",
  "Recipe block key is reconstructed (recipes.json:1078-1080), so ingredients and output count 1 are not confirmed by a live recipe source or a video frame.",
  "How the Gummyfruit Topped Sundae Recipe pattern (def 55825) is obtained (vendor, quest, or other) is unknown.",
  "Retired is null: no retirement or unobtainability source was found."
 ]}
