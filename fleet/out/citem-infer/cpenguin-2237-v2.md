<!-- fleet job=citem-infer id=cpenguin-2237-v2 status=done turns=2 usd=0.0034 tokens(read,write,in,out)=[6827, 18393, 6, 2085] model=claude-haiku-5-5 -->
# Penguin

{"item": {"name": "Penguin (unresolved; possibly the Child's Play 'Tack the Penguin' pet)", "locale_id": null, "kind": "pet"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition 70428 has model penguin.adr, slot 0, class 0, description 'Bring a little wildlife to your yard.', and no coin purchase price.", "source": "client definition (pack); repo:prototype/osfr-tools/data/content/stores.json:15002 (item 70428, category 57, purchase_price_coins null, sell_price_coins null, no_sale true, no price_provenance)"},
  {"claim": "Items 70426, 70428, 70431 share category 57 and have no coin price. Item 70430 (turtle.adr) is the only one in that band with a coin price (10000, Coin Shop, wiki page Turtle). 70429 is priced at 1000 coins. Neither source names 70428.", "source": "repo:prototype/osfr-tools/data/content/stores.json:15001-15005"},
  {"claim": "Child's Play 2010 promotion: a penguin pet, 'Tack the Penguin', bought with Station Cash, SOE donates $10 per purchase up to $50K. The article does not give a Station Cash price.", "source": "articles fact:pet http://www.freerealms.com/article/detail.action?articleId=1980 ; http://www.freerealms.com/article/detail.action?articleId=1981 ; http://www.freerealms.com/article/detail.action?articleId=2420"},
  {"claim": "Client text for the promo: 'Buy Tack the Penguin and SOE will donate $$10 for every one up to $$50K to Child's Play!'", "source": "locale:6858"},
  {"claim": "Locale 2237 'Penguin' is a one-word category-style fragment. It is not evidence of the item's display name, and the client has no string that ties 70428 to Tack the Penguin.", "source": "locale:2237 (flagged fragment)"},
  {"claim": "The Snowhill penguin NPCs, Penguin Defense mini-games and the Penguin Training Facility are quest content, not this item.", "source": "video frames and images in pack; not sources"}
 ],
 "confidence": 0.25,
 "open": [
  "Link between definition 70428 and the Child's Play pet 'Tack the Penguin' is NOT established. No client string or repo record names 70428 with that pet. The promo is therefore not listed as a source for 70428. If it is later linked, the source would be a Station Cash promotion (articles 1980/1981/2420), with the Station Cash price still unknown.",
  "No Station Cash price for Tack the Penguin appears in any source here. Price is null.",
  "Retirement is unknown. no_sale true with no coin price fits a non-purchasable or Station Cash item, but no source states it. The first-pass 'live: yes' is a cheap-model hint and was not used.",
  "No vendor, drop, quest reward, or prize-wheel source is evidenced. vendor_stock and mentioned_by_other_answers are empty.",
  "Critique fixes applied: the citation to locale 272204278 is removed, since that id does not exist. Locale 2237 is no longer used as the item name or as evidence; it is kept only as a flagged fragment. The promo is moved out of the item's sources. Price stays null, so the item is not wireable.",
  "Previous answer's 'sources' entry was wrong to attach the promo to 70428. It is dropped here."
 ]}
