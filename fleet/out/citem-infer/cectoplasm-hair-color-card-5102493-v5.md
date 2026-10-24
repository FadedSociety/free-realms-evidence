<!-- fleet job=citem-infer id=cectoplasm-hair-color-card-5102493-v5 status=no_submit turns=2 usd=0.0017 tokens(read,write,in,out)=[6175, 7077, 6, 1590] model=claude-haiku-5-5 -->
# Ectoplasm Hair Color Card

```json
{"item": {"name": "Ectoplasm Hair Color Card", "locale_id": 5102493, "kind": "card"},
 "sources": [
  {"type": "marketplace", "detail": "Hair color style card introduced in the Week #1 - 10/1/2013 update (Super Spooktacular); the wiki line names it among the cards sold in the Station Cash Marketplace", "where": "Station Cash Marketplace", "price": null, "currency": "station_cash", "source": "wiki: Super Spooktacular (Week #1 - 10/1/2013 line: 'New [Hair] [Color] [Style] [Cards] were introduced: Snowstorm, Pumpkin, Ectoplasm, Phantasm Blue, Bubblegum and Grape Frosting in the [Station] [Cash] [Marketplace]'); wiki: Template:News (Game Update 113, 10/01/2013, 'New [Hair] [Color] [Style] [Cards] have been added!')"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Ectoplasm Hair Color Card', description 'This style card allows you to change your hair color.', definition 79465, slot 3, class 1.", "source": "locale:5102493"},
  {"claim": "The wiki Super Spooktacular Week #1 - 10/1/2013 entry lists the Ectoplasm hair color style card as introduced in the Station Cash Marketplace, alongside Snowstorm, Pumpkin, Phantasm Blue, Bubblegum and Grape Frosting. The previous answer's cut-off quote omitted this tail.", "source": "wiki: Super Spooktacular"},
  {"claim": "Template:News for Game Update 113 (10/01/2013) announces new hair color style cards added, in the same update.", "source": "wiki: Template:News"},
  {"claim": "Wiki file page File:Ectoplasm Hair Color Card.PNG exists; its image transcription shows no price or label text.", "source": "freerealms-wiki/harvest/lists/image_text.json (Ectoplasm Hair Color Card.PNG)"},
  {"claim": "Store-data row for item 79465 (category 142, 180 coins, 162 member) is flagged no_sale: true and is one of a run of identical rows 79466-79480. Not treated as a coin vendor sale or a price.", "source": "repo:prototype/osfr-tools/data/content/stores.json:17185"}
 ],
 "confidence": 0.55,
 "open": [
  "Station Cash price for the card is not evidenced; price is null.",
  "No end-of-sale or retirement date is evidenced; retired is null.",
  "Live status unsure: the card is only dated to the 10/1/2013 update in the wiki.",
  "No vendor, drop, quest or event source found for this card.",
  "The 180-coin store row (stores.json:17185) is flagged no_sale and is not used as a source or price."
 ]}
```
