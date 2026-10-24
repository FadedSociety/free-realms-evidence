<!-- fleet job=citem-infer id=ccandied-briarmelon-38669-v2 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[6041, 12293, 6, 1712] model=claude-haiku-5-5 -->
# Candied Briarmelon

{"item": {"name": "Candied Briarmelon", "locale_id": 38669, "kind": "consumable"},
 "sources": [
  {"type": "crafting", "detail": "Chef recipe 'Candied Briarmelon Recipe' (client item 867, recipe_id 57). Ingredients: Briarmelon x3, Gummyfruit x3, Rainleaf x3, Sugar x8. Requires Chef level 20. Output: item 21831 (Candied Briarmelon, 'Increases Attack').", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/recipes.json:255-286 (chef.candied_briarmelon); locale:1534; locale:1561; wiki 'List of Recipes (Chef)' ([Candied] [Briarmelon] row); wiki 'Chef' ('[Candied] [Briarmelon] - Increases Attack')"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 38669 'Candied Briarmelon' is a food item, description 'Eating this food temporarily increases your attack.', definition 21831, class 9, no coin store price.", "source": "client definition pack; locale:38669"},
  {"claim": "Recipe teaches creation of Candied Briarmelon and requires chef level 20.", "source": "locale:1561"},
  {"claim": "Wiki Chef recipe list gives the ingredients (Briarmelon x3, Gummyfruit x3, Rainleaf x3, Sugar x8) and effect 'Increases Attack'; the 'Where to find' heading is blank.", "source": "wiki 'List of Recipes (Chef)'; wiki 'Chef'"},
  {"claim": "Recipe acquisition (trainer, vendor, price) is not recorded in the pack, the wiki, or the repo; repo notes list the source as unknown for Candied Briarmelon.", "source": "notes/Build Guides/Content/Jobs/Chef.md:367; notes/Build Guides/Content/Jobs/Chef.md:236"},
  {"claim": "No coin vendor stocks the item; no video frames found.", "source": "lookup client/wiki/articles/video; repo search for 21831, 38669 and candied_briarmelon"},
  {"claim": "The Jack/Briarwood daily cooking request is text-only and its quest title is flagged NOT LIVE; it names no reward, so it is not used as a source.", "source": "locale:73265 (NOT LIVE); locale:73266; locale:73410; locale:102437; locale:47675 (Placeholder)"}
 ],
 "confidence": 0.5,
 "open": [
  "Recipe 867's own acquisition is unknown: no trainer, vendor, price, or quest is evidenced, so the crafting source has no confirmed purchase path and is not wireable as a full source yet.",
  "Dropped the prior quest_reward source (Jack's Briarwood daily cooking request). Its title locale:73265 is flagged NOT LIVE and locale:47675 is flagged Placeholder, and no locale line names an item reward. It stays unconfirmed.",
  "No price or currency is known: item 21831 has no coin store price in the client definition, and no wiki price was found.",
  "Retirement status is unknown; no source states whether the recipe or the food was removed later.",
  "Live status is unsure: the item and recipe exist in the client and wiki, but no live vendor or quest confirms how players obtained them."
 ]}
