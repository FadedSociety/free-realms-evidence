<!-- fleet job=citem-infer id=chooray-for-pixiewood-painting-147761-v2 status=done turns=3 usd=0.0022 tokens(read,write,in,out)=[13147, 8861, 8, 1996] model=claude-haiku-5-5 -->
# Hooray for Pixiewood Painting

{"item": {"name": "Hooray for Pixiewood Painting", "locale_id": 147761, "kind": "furniture"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale of a housing painting (store category 53); no named NPC confirmed for this item", "where": "Coin store (housing); Edwin in western Pixiewood Hills, Sanctuary is NOT confirmed for this item", "price": "50 coins (45 coins for members, 10% discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:12033 (item_id 36562, category_id 53, purchase_price_coins 50, member_discount_percent 10, member_price_coins 45, no_sale false)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 36562 / locale 147761 is named 'Hooray for Pixiewood Painting', a furniture painting (model hsg_painting_01.adr) with one definition and no variants", "source": "client definition; locale:147761"},
  {"claim": "Store row for item 36562 lists purchase price 50 coins, member price 45 coins, 10% member discount, not marked no_sale", "source": "repo:prototype/osfr-tools/data/content/stores.json:12033"},
  {"claim": "No wiki page, article, video frame or other answer names 'Hooray for Pixiewood Painting' beyond its client text entry", "source": "lookup of wiki, articles and client text for the name (only locale:147761 returned)"},
  {"claim": "Wiki page 'Edwin' says he sells Premium Painting housing items in western Pixiewood Hills, Sanctuary; the visible sell list (Wizard Wand, Sword-Wielding Ninja, Shifty the Shuffler, Shadow Talon Archer, Nurse Naia, ...) is truncated and does not name this item", "source": "wiki page 'Edwin'"},
  {"claim": "Sibling painting wiki pages (Nirvi, Wizard Wand, Nurse Naia, Mauthe Dog, Giant Eagle, Sword-Wielding Ninja, Shifty the Shuffler) say that as of December 18, 2013 the painting is available to everyone through Edwin at the regular price and to members at a 10% discount; the price figures are blank in the extracted text", "source": "wiki pages 'Nirvi Painting', 'Wizard Wand Painting', 'Nurse Naia Painting', 'Mauthe Dog Painting', 'Giant Eagle Painting', 'Sword-Wielding Ninja Painting', 'Shifty the Shuffler Painting'"}
 ],
 "confidence": 0.4,
 "open": [
  "Vendor identity unconfirmed: Edwin is not shown selling this item on any wiki page. The sibling paintings are Edwin's, but this one is only in the repo store data. Treat Edwin as a guess until a page or sell list names it.",
  "Price 50 coins comes only from repo stores.json row 12033; no wiki price was found (sibling pages have blank prices). The source_tags on the row (L1, L2, L4, R2, T633, R1) are unexplained; the row is treated as a coin store sale on the strength of the coin price field, not the tags.",
  "Retirement unknown: sibling pages give an availability start of December 18, 2013 but no end date; no source says the item was retired or is still sold.",
  "Not checked for other sources: quest reward, drop, prize wheel, event, promotion or crafting. No evidence in the pack for any of these."
 ]}
