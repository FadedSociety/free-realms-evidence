<!-- fleet job=item-infer id=imega-growth-sprayer-v3 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[5711, 6939, 6, 1615] model=claude-haiku-5-5 -->
# Mega Growth Sprayer

{"item": {"name": "Mega Growth Sprayer", "locale_id": 436251, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Player farm Vending Machine (farm-lot fixture, not an NPC vendor). Freestyle Jobs Weapon slot item. Members get a 10% discount on the same listing.", "where": "Player farm Vending Machine (farm lot); requires owning a Rank 1 Farm to buy", "price": "2000 regular; 1800 for members (10% discount). Figures come from the wiki infobox coin field only; the wiki price sentence is blank.", "currency": "coins", "source": "wiki: Mega_Growth_Sprayer (rev 47552, infobox coins [2000, 1800]; text 'available for purchase through the Vending Machine'); wiki: Vending_Machine (Equipment list includes [Mega] [Growth] [Sprayer]); wiki: Farms (vending machine sells [Mega] [Growth] [Sprayer]); locale:436276 ('*Must own a Rank 1 Farm to buy.')"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Item name is client text locale 436251; tooltip locale 436276 says it is equipped to spray friends bigger and requires owning a Rank 1 Farm to buy.", "source": "locale:436251, locale:436276"},
  {"claim": "Wiki describes the sprayer as a Freestyle Jobs Weapon slot item available through the Vending Machine, and it cannot be traded.", "source": "wiki: Mega_Growth_Sprayer"},
  {"claim": "The Vending Machine Equipment list includes [Mega] [Growth] [Sprayer].", "source": "wiki: Vending_Machine (ns0)"},
  {"claim": "The Farms page says the farm vending machine sells clothes including [Mega] [Growth] [Sprayer].", "source": "wiki: Farms (ns0)"},
  {"claim": "Item tooltip shows Resell Value 200 and Cannot Trade. 200 is resale value, not the purchase price.", "source": "image:item_tooltip (wiki File:Mega growth sprayer.jpg)"},
  {"claim": "A news archive patch note lists the Mega Growth Sprayer among vending machine items, so it was live in that era. This is historical only.", "source": "wiki: Template:News/Archive (ns10)"}
 ],
 "confidence": 0.5,
 "open": [
  "Price is unverified. The wiki price sentence is blank ('at the regular price of , and to members at the 10% discount price of .'). The 2000 and 1800 figures and the 'coins' currency come only from the unlabeled infobox coin field [2000, 1800]. Verify against live vending data before treating as confirmed.",
  "Current live status is unverified. The only evidence is a historical patch-note mention, so retired is null. No removal source was found.",
  "No vendor_stock row for this item was found in the pack or repo, so vending stock was not checked in repo data.",
  "Pack's second price line (1800 member) is merged into one vendor source as a member discount on the same listing, not a separate source."
 ]}
