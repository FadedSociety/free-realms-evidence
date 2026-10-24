<!-- fleet job=item-infer id=iarctic-frostfang-painting-v2 status=done turns=3 usd=0.0023 tokens(read,write,in,out)=[13518, 9904, 8, 1840] model=claude-haiku-5-5 -->
# Arctic Frostfang Painting

{"item": {"name": "Arctic Frostfang Painting", "locale_id": 13936, "kind": "furniture"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace, regular price 99 Station Cash; members get a 10% discount price of 89 Station Cash (sale price)", "where": "Station Cash Marketplace", "price": "99 (regular); 89 (members, 10% off)", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Arctic_Frostfang_Painting (rev 47291; raw wikitext freerealms-wiki/wikitext/16843-47291-3c42e6f2bf4e.wiki line 4: {{SC|99}} and {{SC|89}}; categories SC Marketplace, Marketplace Items)"},
  {"type": "vendor", "detail": "Edwin, human NPC merchant in western Pixiewood Hills (Sanctuary), whose Sells list includes Arctic Frostfang Painting", "where": "Sanctuary, western Pixiewood Hills", "price": null, "currency": null, "source": "Edwin wiki text, refs quest-lines/npc-packs.json line 40919 (also item-packs.json line 62056): 'He sells Premium Painting housing items' and Sells list entry 'Arctic Frostfang Painting'"}
 ],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Item name is client text id 13936 'Arctic Frostfang Painting'", "source": "locale:13936"},
  {"claim": "Sold in the Station Cash Marketplace at a regular price of 99 Station Cash, members 10% discount price 89 Station Cash", "source": "https://freerealms.fandom.com/wiki/Arctic_Frostfang_Painting (raw wikitext {{SC|99}}, {{SC|89}})"},
  {"claim": "Wiki describes it as a limited-time offering ('was for a limited amount of time available'), so no longer sold in the Marketplace", "source": "https://freerealms.fandom.com/wiki/Arctic_Frostfang_Painting"},
  {"claim": "Housing furniture; art of the Arctic Frostfang Trading Card Game card, Original Premium Painting 9/237", "source": "image:item_tooltip on https://freerealms.fandom.com/wiki/Arctic_Frostfang_Painting"},
  {"claim": "Edwin, a Sanctuary merchant in western Pixiewood Hills, sells Premium Painting housing items including Arctic Frostfang Painting", "source": "refs quest-lines/npc-packs.json:40919 (Edwin wiki page text)"}
 ],
 "confidence": 0.7,
 "open": [
  "Edwin's vendor price and currency are not in the pack; do not assume Station Cash. Confirm from Edwin's price data before wiring the vendor source.",
  "The Edwin page is a Sanctuary-era NPC page; whether Edwin still sold this painting at the end of the live service is not dated in the pack.",
  "Retired status is inferred from past-tense wording ('was for a limited amount of time available'); no removal date is in the pack."
 ]}
