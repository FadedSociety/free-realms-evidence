<!-- fleet job=citem-infer id=cmedic-s-necklace-of-vitality-iv-131067-v2 status=done turns=3 usd=0.0020 tokens(read,write,in,out)=[12893, 8415, 8, 1700] model=claude-haiku-5-5 -->
# Medic's Necklace of Vitality IV

{"item": {"name": "Medic's Necklace of Vitality IV", "locale_id": 131067, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "River, human NPC merchant who sells Medic Job items (wiki 'River' page, Sells list)", "where": "Lakeshore, south of the Thunder Falls Raceway", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/River (Sells section, revision 2025-08-04); repo:prototype/osfr-tools/data/content/vendors.json:42801-42824"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name and locale id 131067 is 'Medic's Necklace of Vitality IV'; it sits in the Medic necklace family I-V (locale 131064-131068).", "source": "locale:131067; client cluster in pack"},
  {"claim": "River's wiki Sells list names Medic's Necklace of Vitality IV; the vendor record maps it to item 75323 and locale 131067 by exact display-name match.", "source": "repo:prototype/osfr-tools/data/content/vendors.json:42801-42824"},
  {"claim": "The wiki River page gives no captured price for the necklace.", "source": "repo:prototype/osfr-tools/data/content/vendors.json:42809 ('reference price, not captured NPC quote')"}
 ],
 "confidence": 0.5,
 "open": [
  "Coin store price 1504 (member 1353, sell 150) in repo:prototype/osfr-tools/data/content/stores.json:17337 is a reconstructed reference price from the Legacy cost, not a captured sale. It is not listed as a coin_shop source. No store evidence shows the item is sold in the Coin Shop.",
  "Medic prize wheel at Prince of Low Tide is unconfirmed. The wiki 'Prince of Low Tide!' page snippet shows only the Archer prize wheel section (Archer's Necklace of Vitality IV); the Medic section was not retrieved. The other answer's claim is unverified, so it is not listed.",
  "Enemy-drop claim in quest-lines/enemies.json:28605 is unverified against any wiki page and is not listed.",
  "River's price for the necklace is not on the wiki. A captured NPC quote is needed before a price is wired.",
  "Liveness and retirement are unknown: no dated source says whether River still sells it. The River page revision of 2025-08-04 is the only date anchor.",
  "Wireable: false. The only evidenced source (River) has no price, and the prize wheel and drop sources are unverified."
 ]}
