<!-- fleet job=item-infer id=iwizard-v2 status=nothing_found turns=3 usd=0.0027 tokens(read,write,in,out)=[15794, 12243, 8, 2057] model=claude-haiku-5-5 -->
# Wizard

{"item": {"name": "Wizard", "locale_id": null, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "The wiki page 'Wizard' describes the Wizard job (Members Only ranged combat class), not an item. Its categories are Jobs, Members Only, Wizard, ZAM Credits. 'ZAM Credits' is only a category label with no price, vendor or currency row, so it does not source anything.", "source": "wiki page Wizard (rev 46067)"},
  {"claim": "Client name matches for the bare word 'Wizard' are job/ability strings: locale:2280 [ability] and locale:4420001 [other]. locale:4420031 is a duplicate of 4420001 and is not used.", "source": "locale:2280; locale:4420001"},
  {"claim": "Wizard is a Members Only job, per the official article.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=70"},
  {"claim": "Wizard's Flair Shard of Necromancy is a level 12 Wizard flair shard, acquired from the Coin Shop. The wiki gives no price (the price field is blank). Its tooltip reads 'Be spooky all year round', Resell Value 150, Required Level 12, Wizard.", "source": "wiki page Wizard's Flair Shard of Necromancy (ns0); image:item_tooltip Wizard's Flair Shard of Necromancy item.jpg"},
  {"claim": "Wizard's Flair Shard of Smoldering has Resell Value 75 and Required Level 1, Wizard. Its tooltip reads 'Casts a red glow over your wand. Ominous!'. No wiki article page was found for it, so its source is unknown.", "source": "image:item_tooltip Wizard's Flair Shard of Smoldering item.jpg"},
  {"claim": "Many other Wizard's Flair Shard variants exist in the client (Ice, Forest, Valentines, Gifted, Subtlety, Spheres, Magic Feet, Power, Magma, Wight, Intimidation, Whirlwind, Prosperity, Glamour, Honey, Forestry, Ragnarok, Dark Magic). Their sources were not checked.", "source": "locale:131298-131313, 442046-442940, 442293; repo:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json (Wizard's Flair Shard comments)"}
 ],
 "confidence": 0.3,
 "open": [
  "The request names an item called 'Wizard', but the only wiki page with that title is the Members Only job. A job is not an item, so no item sources are given for it. Confirm which item was meant. If it is a Wizard's Flair Shard, name the exact variant.",
  "Wizard's Flair Shard of Necromancy: the Coin Shop source is from the wiki page's own text, but its price is blank on that page. Fetch the Coin Shop listing for the exact price and currency, and check whether it is still sold or retired.",
  "Wizard's Flair Shard of Smoldering: no wiki article page or vendor data is in the pack. Its source is unknown.",
  "The earlier remark that Necromancy is 'probably a Halloween item' has no evidence behind it. Ignore it unless a source is found.",
  "The wiki Wizard job page is truncated before the end of the quest list; the rest of its content was not checked."
 ]}
