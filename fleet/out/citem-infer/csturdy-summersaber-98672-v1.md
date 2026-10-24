<!-- fleet job=citem-infer id=csturdy-summersaber-98672-v1 status=done turns=5 usd=0.0048 tokens(read,write,in,out)=[45541, 18192, 12, 4090] model=claude-haiku-5-5 -->
# Sturdy Summersaber

{"item": {"name": "Sturdy Summersaber", "locale_id": 98672, "kind": "weapon"},
 "sources": [
  {"type": "crafting", "detail": "Blacksmith recipe 'Sturdy Summersaber' (wiki: 'It is acquired from the Blacksmith recipe Sturdy Summersaber'; wiki category 'Blacksmith Recipe Weapons'; listed under Blacksmith's crafted weapons on the wiki Blacksmith and Ninja pages)", "where": "Blacksmith (anvil crafting)", "price": null, "currency": null, "source": "wiki page 'Sturdy Summersaber'; wiki page 'Blacksmith'; wiki page 'Ninja' ('Sturdy Summersaber [Blacksmith Crafted Weapon]')"},
  {"type": "vendor", "detail": "Coin store sale of definition 37003 (tooltip-matching variant: resell 64)", "where": "coin store (vendor not named in our data)", "price": "640 coins (member price 576 coins)", "currency": "coins", "source": "repo:data/content/stores.json item 37003 (purchase_price_coins 640, category 207); wiki image item_tooltip 'Resell Value: 64'"},
  {"type": "vendor", "detail": "Coin store sale of definition 38111 (second variant)", "where": "coin store (vendor not named in our data)", "price": "995 coins (member price 895 coins)", "currency": "coins", "source": "repo:data/content/stores.json item 38111 (purchase_price_coins 995, category 207); notes/Autopilot/T633.md line 163 (38111 Sturdy Summersaber 995 / sell 99)"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Name 'Sturdy Summersaber' is locale 98672 (item) and also locale 4419913 (item)", "source": "locale:98672; locale:4419913"},
  {"claim": "Wiki: level 16 Ninja weapon, acquired from the Blacksmith recipe, cannot trade, Flame Flash 2372 damage, Dragonstrike 10674 damage", "source": "wiki page 'Sturdy Summersaber'"},
  {"claim": "Wiki tooltip: Resell Value 64, Power 5, Cannot Trade", "source": "image:item_tooltip 'Sturdy summersaber item.jpg'"},
  {"claim": "Two client definitions (37003, 38111) share the name, each with a coin store price of 640 and 995", "source": "client definition; repo:data/content/stores.json items 37003 and 38111"},
  {"claim": "Legendary Summersaber quest (Anata Caliburn, row 30) is a separate quest, forging the legendary blade; it does not name Sturdy Summersaber as its reward", "source": "repo:notes/Build Guides/Content/Jobs/Blacksmith.md:137; repo:notes/Build Guides/Content/Jobs/Blacksmith.md:272"},
  {"claim": "Blacksmith recipe item id for Sturdy Summersaber is unresolved in our data", "source": "repo:prototype/osfr-tools/data/content/recipes_unresolved.json:3640"}
 ],
 "confidence": 0.6,
 "open": [
  "Coin vendor NPC and zone are not named: no vendors.json row cites item 37003 or 38111, and no wiki or client text names the coin store seller. The 'where' is unknown.",
  "Price mapping: the wiki tooltip (Resell 64) matches definition 37003 at 640 coins; definition 38111 at 995 coins (resell 99) is unverified as a wiki price. Whether both variants are sold in-game at the same time is not confirmed.",
  "Wiki gives no coin price itself; the 640/995 figures come only from our store data, not a wiki price, so no sale-price comparison is available.",
  "Blacksmith recipe: the recipe's item id and ingredients are unresolved (recipes_unresolved.json:3640); the wiki gives no materials.",
  "Retirement status is not stated by any source. The wiki page does not say it was retired or unobtainable later.",
  "Client definition has an empty description; the wiki's Ninja and Blacksmith category pages are the only text sources."
 ]}
