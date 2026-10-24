<!-- fleet job=citem-infer id=cbrewery-chips-1186-v1 status=done turns=4 usd=0.0028 tokens(read,write,in,out)=[24326, 12328, 10, 2049] model=claude-haiku-5-5 -->
# Brewery Chips

{"item": {"name": "Brewery Chips", "locale_id": 1186, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 4027 is named 'Brewery Chips' (locale 1186), a food consumable (class 9, slot 0). Description: eating it changes the player into a male Chugawug miner for thirty minutes.", "source": "locale:1186; client definition 4027"},
  {"claim": "Client has a generic transform-food description line: 'Eating this food will change the player into a Chugawug Male Miner for 30 minutes.'", "source": "locale:150076"},
  {"claim": "Sibling client lines 1181-1191 (Grotto Noodles, Grotto Lollipop, Grotto Creampuffs, Grotto Casserole, Chugawug Steak, Brewery Fizzpop, Brewery Pizza, Brewery Crunchberry, Brewery Cookies, Brewery Crackers) form one food-transform set with no sources of their own in the pack.", "source": "locale:1181-1191"},
  {"claim": "Wugachug/Sasparilla Brewery NPCs (Brockoom, Oggy, Cook Yumtumlot) are in the repo, but no repo or wiki text ties any of them to selling or giving Brewery Chips.", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Wugachug.md (lines 38-58)"}
 ],
 "confidence": 0.2,
 "open": [
  "No vendor source found: no coin-store price in the client definition (coin_store_prices empty), no vendor_stock entry, and no repo hit for item 4027 or the name 'Brewery Chips' in stores, vendors, quests or recipes. The first-pass 'vendor' guess is unsupported and was not used.",
  "No wiki page, article fact or video frame names the item, so no marketplace, coin shop, prize wheel, quest, drop, event or crafting source can be cited.",
  "Unknown how a player obtains the food at all: it may be a Chugawug/Brewery food-transform item granted by a quest, event, or cooking/vendor path not present in our data. Needs a lookup of Brewery or Chugawug cooking quests and the Chugawug Festival/holiday event.",
  "Live status and retirement are unknown; no source states whether it was sold, retired, or limited to an event.",
  "Client text 150076 is generic transform-food wording; it does not name Brewery Chips and only shows the item class exists."
 ]}
