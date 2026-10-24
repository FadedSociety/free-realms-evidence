<!-- fleet job=citem-infer id=cn-upsetting-blacksmith-gloves-pl-upsetting-blacksmith-gloves-132812-v2 status=done turns=3 usd=0.0017 tokens(read,write,in,out)=[12195, 7087, 8, 1462] model=claude-haiku-5-5 -->
# {n}Upsetting Blacksmith Gloves{pl="Upsetting Blacksmith Gloves"}

{"item": {"name": "Upsetting Blacksmith Gloves", "locale_id": 132812, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Seppa (human NPC merchant; wiki says she sells exclusively Blacksmith job items; listed under Sells)", "where": "Dartmoor Quarry, Northern Wilds", "price": "reference 403 coins (stores.json; not a captured Seppa quote); member reference 362 coins; sell-back 40 coins", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Seppa (Sells list, includes 'Upsetting [Blacksmith] [Gloves]'); repo:prototype/osfr-tools/data/content/vendors.json line 43463 (price_basis: '(R) stores.json reference price; no captured retail NPC quote.')"}
 ],
 "retired": null,
 "live": "likely",
 "evidence": [
  {"claim": "Client text id 132812 is the name 'Upsetting Blacksmith Gloves'", "source": "locale:132812"},
  {"claim": "Wiki Seppa page: 'She sells exclusively [Blacksmith] Job items' and its Sells list includes Upsetting [Blacksmith] [Gloves]", "source": "wiki page Seppa (ns0)"},
  {"claim": "Seppa is placed at Dartmoor Quarry in the wiki Merchants list", "source": "wiki page Merchants (per prior answer; not re-fetched)"},
  {"claim": "stores.json record for item 75804: category 102, purchase 403, member 362, sell 40", "source": "repo:prototype/osfr-tools/data/content/stores.json line 15578"},
  {"claim": "vendors.json lists 75804 under Seppa's stock with the price basis marked as a stores.json reference price", "source": "repo:prototype/osfr-tools/data/content/vendors.json line 43463-43471"}
 ],
 "confidence": 0.7,
 "open": [
  "The 403-coin price is a stores.json reference price, not a captured Seppa quote, and the wiki gives no coin price. Treat it as unverified.",
  "stores.json category 102 is not confirmed as a coin-store category, so it is not cited as a separate Coin Shop source; the stores.json record is only a price note on the Seppa vendor entry.",
  "No wiki or article fact states retirement or a later unobtainable date; retired is null.",
  "The Punching Blacksmith Gloves (locale 132817) is a separate item and was not checked here.",
  "No quest reward, drop, event, or crafting source was found for this item. The client description is empty."
 ]}
