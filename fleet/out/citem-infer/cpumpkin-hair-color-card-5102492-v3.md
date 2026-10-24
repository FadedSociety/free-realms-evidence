<!-- fleet job=citem-infer id=cpumpkin-hair-color-card-5102492-v3 status=nothing_found turns=3 usd=0.0018 tokens(read,write,in,out)=[12975, 7059, 8, 1666] model=claude-haiku-5-5 -->
# Pumpkin Hair Color Card

{"item": {"name": "Pumpkin Hair Color Card", "locale_id": 5102492, "kind": "card"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Pumpkin Hair Color Card', description 'This style card allows you to change your hair color.' (definition 79468, slot 3, class 1)", "source": "locale:5102492"},
  {"claim": "Store row for item 79468: category 142, purchase 180 coins, member 180 to 162 coins (10% discount), sell_price null, no_sale true, source_tags [L1,L2,L4,R2,L3,L3]. The row is a listing flagged as not sold; it is not a confirmed sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json:17188"},
  {"claim": "Wiki Super Spooktacular, Week #1 - 10/1/2013: 'New [Hair] [Color] Style Cards were introduced: Snowstorm, [Pumpkin], Ectoplasm, Phantasm Blue, Bubblegum.' This is a release date only; it names no sale, reward, or achievement.", "source": "wiki page: Super Spooktacular"},
  {"claim": "Wiki File:Pumpkin Hair Color Card.PNG exists; its transcribed text carries no price or source.", "source": "wiki File:Pumpkin Hair Color Card.PNG"},
  {"claim": "The October 2013 Monthly Member Pack items named on the wiki are Pinkeye and Toeny; this card is not named there.", "source": "wiki page: Super Spooktacular"},
  {"claim": "Client cluster locale:5102491 to 5102496 lists the sibling hair color cards by name.", "source": "locale:5102491 through locale:5102496"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found. The only coin price is a store-data row (180 coins, 162 member) with no_sale=true, so it is not a verified coin_shop route and is not listed under sources.",
  "The 10/1/2013 wiki entry is a release date only. It is not an acquisition route, and no end date or retirement is documented, so retired is null.",
  "The meaning of source_tags [L1,L2,L4,R2,L3,L3] on the store row is undocumented here and was not used as evidence.",
  "Needed to make this wireable: a vendor stock row, quest or event reward, or wiki/video price naming item 79468 or the card.",
  "Grape Frosting (locale:5102496) was not checked; it is outside this item's evidence."
 ]}
