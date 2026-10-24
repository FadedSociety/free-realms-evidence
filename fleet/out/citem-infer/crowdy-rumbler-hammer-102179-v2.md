<!-- fleet job=citem-infer id=crowdy-rumbler-hammer-102179-v2 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[7388, 8109, 6, 1582] model=claude-haiku-5-5 -->
# Rowdy Rumbler Hammer

{"item": {"name": "Rowdy Rumbler Hammer", "locale_id": 102179, "kind": "weapon"},
 "sources": [
  {"type": "crafting", "detail": "Blacksmith recipe 'Rowdy Rumbler Hammer' (client recipe item 'Rowdy Rumbler Recipe', 301238581). Level 4 Brawler, Power 2 weapon, made at an Anvil. Materials and crafting rank not confirmed.", "where": null, "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Rowdy_Rumbler_Hammer; locale:386086; repo:prototype/osfr-tools/data/content/recipes_unresolved.json:3138-3146"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Wiki: Level 4 Brawler weapon, Green Text weapon, obtainable from the Blacksmith recipe Rowdy Rumbler Hammer; listed under Blacksmith Recipe Weapons.", "source": "https://freerealms.fandom.com/wiki/Rowdy_Rumbler_Hammer"},
  {"claim": "Client forging title 'Forging: Rowdy Rumbler Hammer'.", "source": "locale:386086"},
  {"claim": "Client item name, 10 definitions (30340-30349) sharing the name, slot 7, class 5, no coin store price.", "source": "client definition (pack)"},
  {"claim": "Recipe key blacksmith.rowdy_rumbler_hammer exists in the unresolved recipe data with minigame type 8 but no candidate recipe id, ingredients, or rank.", "source": "repo:prototype/osfr-tools/data/content/recipes_unresolved.json:3138-3150"},
  {"claim": "Quest consumers only (not acquisition sources): Dull Challenge (Derp Axemaker, Dartmoor) and Silver Appearance (Billie JoBob, Blackspore) ask the player to forge the hammer. Silver Appearance is conflicting in the notes.", "source": "locale:387885; notes/Build Guides/Content/Jobs/Blacksmith.md:100, :120, :372"},
  {"claim": "No coin vendor stock and no coin store price found.", "source": "client definition coin_store_prices empty; vendor_stock empty"}
 ],
 "confidence": 0.6,
 "open": [
  "Recipe materials, crafting rank gate, and the candidate recipe id are unresolved (recipes_unresolved.json:3141-3150); no price or ingredient cost can be stated.",
  "No dated source says whether the recipe is still live or was retired; the wiki's Green Text category does not by itself show retirement.",
  "Quest tie-ins (Dull Challenge, Silver Appearance) are consumers of the crafted hammer, not reward sources, so they are excluded from sources. Silver Appearance has a conflicting Scythes line in Blacksmith.md:372.",
  "Attack figures from the wiki (Glancing Blow 444, Leg Sweep 1554) were not checked against the client."
 ]}
