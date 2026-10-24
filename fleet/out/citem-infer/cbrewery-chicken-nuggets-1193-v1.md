<!-- fleet job=citem-infer id=cbrewery-chicken-nuggets-1193-v1 status=nothing_found turns=3 usd=0.0029 tokens(read,write,in,out)=[12839, 13845, 8, 2040] model=claude-haiku-5-5 -->
# Brewery Chicken Nuggets

{"item": {"name": "Brewery Chicken Nuggets", "locale_id": 1193, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 4034: name 'Brewery Chicken Nuggets' (locale 1193). Description: eating it turns the player into a female chugawug mage for thirty minutes. Slot 0, item class 9, no models, no coin store price.", "source": "locale:1193"},
  {"claim": "Name sits in a cluster of Sasparilla Brewery food items (locale 1188-1196: Brewery Pizza, Crunchberry, Cookies, Crackers, Veal Sandwich, Toasted Sandwich, Monty Crispy Sandwich, Farmer's Special), plus Chewy Candy Horn (1197) and Illusion Food - Antelope (1198). The brewery food family is a transform-food set; the name itself is client text only.", "source": "locale:1188 through locale:1198"},
  {"claim": "Repo locale data lists 'Brewery Chicken Nuggets' as a ugdt string id 1281774394, and 'Brewery Pizza' as ucdt 237033106, in the copies under FreeRealmsLocaleTools test data and opening-* locale dumps. Those are text tables, not acquisition data.", "source": "search repo: FreeRealmsLocaleTools/test/FreeRealmsLocaleTools.Tests/data/en_us_data.dat:33917"},
  {"claim": "The wiki's Sasparilla Brewery and Wugachug NPC notes name the brewery staff and sasparilla quests but do not mention any brewery food item, nor any vendor selling it.", "source": "repo: notes/Build Guides/Content/NPCs/NPCs - Wugachug.md"},
  {"claim": "The 'Illusion Food' family (e.g. Illusion Food - Antelope, locale 1198) is the same transform-food kind; a robgoblin quest text describes illusion food as a transformation item.", "source": "locale:564218199 (quest dialog, robgoblin infestation)"}
 ],
 "confidence": 0.1,
 "open": [
  "No acquisition source found. Lookup of the wiki, articles and video returned no matches for 'Brewery Chicken Nuggets' or for brewery food in general. The client has no coin store price (coin_store_prices empty) and the pack has no vendor stock.",
  "Repo search for definition id 4034 in data/content stores, vendors, quests and recipes returned no hits. Check data/content/stores.json and recipe/crafting tables for item 4034 directly.",
  "The Sasparilla Brewery cooking/transform food is probably a Wugachug cook or event reward, or a Chugawug cooking-tent item, but nothing in the sources confirms it. Do not assign a vendor without a cited source.",
  "The live status is unconfirmed. The first-pass 'live: yes' tag is a hint only. The item is a transform food of the Brewery family and may be an event or limited item.",
  "No price, currency, retirement date or drop source is known."
 ]}
