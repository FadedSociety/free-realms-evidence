<!-- fleet job=citem-infer id=cswirls-429763-v1 status=nothing_found turns=6 usd=0.0047 tokens(read,write,in,out)=[46467, 20352, 14, 3430] model=claude-haiku-5-5 -->
# Swirls

{"item": {"name": "Swirls", "locale_id": 429763, "kind": "card"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Definition 77559 is the item 'Swirls Face Paint Card' (locale 414552, item name), not a plain 'Swirls' item. Locale 429763 'Swirls' is the face-paint style name used in CharacterCreateCustomizationFacePaint.txt (rows 1000007 Pixie and 1000019 Human, Female).", "source": "locale:414552; locale:429763; client Resources/CharacterCreate/CharacterCreateItemMappings.txt:98 ('44^5^1^2^Swirls Face Paint Card^77559^'); client Resources/CharacterCreateCustomizationFacePaint.txt:8,20"},
  {"claim": "The item is a face paint style card in the character creator's Face Paint category (TYPE 5), so it is a style-card item, which the client shows in the Style Cards panel (Face Paints).", "source": "repo: notes/Build Guides/Gameplay/Character and Customization.md:157; notes/Build Guides/Gameplay/Items and Inventory.md:90; video:1xtVveaQ3XI/00218.jpg"},
  {"claim": "No coin store price in the client definition or stores data for definition 77559 (coin_store_prices empty).", "source": "repo:data/content/stores.json (no entry for item 77559 found in search); client definition"},
  {"claim": "No wiki page, article, video frame, quest, drop or vendor names Swirls or Swirls Face Paint Card. The only wiki mention of face paint cards is Super Spooktacular (Troll, Phantom, Starry Moons Face Paint Cards), not Swirls.", "source": "lookup wiki search 'Swirls' and 'Swirls Face Paint Card'; wiki page Super Spooktacular"},
  {"claim": "Sibling face paint cards Gothic Rag Doll Face Paint Card came from a Pumpkin Prince's Treasure chest in the open world; this does not apply to Swirls.", "source": "repo:notes/Build Guides/Content/Dungeons/Bone Bog Cemetery.md:71"}
 ],
 "confidence": 0.2,
 "open": [
  "No source found for Swirls Face Paint Card: no vendor, coin shop, marketplace, quest, drop, event, prize wheel or crafting evidence in any root. Source list left empty rather than guessed.",
  "Live status unsure: the first-pass tag said live=yes, but that is a hint only; no wiki page or store entry confirms it is still obtainable or was retired.",
  "Pack item name vs definition mismatch: the pack names locale 429763 'Swirls' (a face paint style name), while the purchasable/inventory item is 'Swirls Face Paint Card' (locale 414552, def 77559). Confirm which name the rebuild should use.",
  "The pack's slot 6 and class 0 are consistent with a style card rather than clothing; the pack's kind 'clothing' guess is not supported by the client definition."
 ]}
