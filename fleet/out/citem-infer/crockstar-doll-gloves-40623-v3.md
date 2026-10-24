<!-- fleet job=citem-infer id=crockstar-doll-gloves-40623-v3 status=done turns=2 usd=0.0027 tokens(read,write,in,out)=[6172, 12728, 6, 2141] model=claude-haiku-5-5 -->
# Rockstar Doll Gloves

{"item": {"name": "Rockstar Doll Gloves", "locale_id": 40623, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Entry (glove slot) in the [Rockstar] Pixie Doll collection (client 'Rockstar Pixie Doll', locale 7703). Completing it yields the Pixie Rockstar Doll (locale 66658). Membership only; no acquisition route for the glove itself is evidenced.", "where": null, "price": null, "currency": null, "source": "wiki:Toys (Collections) ('[Rockstar] [Doll] [Gloves]' listed under Rockstar Pixie Doll); wiki:List of Collections ('[Rockstar] Pixie [Doll]'); repo:prototype/osfr-tools/data/content/collections.json:7502 (wiki:4:117); locale:132311"},
  {"type": "collection", "detail": "Entry (glove slot) in the [Rockstar] Human Doll collection (client 'Rockstar Human Doll', locale 7709). Completing it yields the Human Rockstar Doll (locale 66664). Membership only; no acquisition route for the glove itself is evidenced.", "where": null, "price": null, "currency": null, "source": "wiki:Toys (Collections) ('[Rockstar] [Doll] [Gloves]' listed under the Human doll set); wiki:List of Collections ('[Rockstar] Human [Doll]'); repo:prototype/osfr-tools/data/content/collections.json:7410 (wiki:4:116); locale:132317"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Rockstar Doll Gloves' is locale 40623; client definitions 3407 and 3455; slot 0, class 0; no model files; no coin store price (repo stores has no entry).", "source": "locale:40623; client definition pack"},
  {"claim": "The wiki Toys (Collections) page lists '[Rockstar] [Doll] [Gloves]' in both the Rockstar Pixie Doll and Rockstar Human Doll sets; the List of Collections page lists both '[Rockstar] Human [Doll]' and '[Rockstar] Pixie [Doll]'.", "source": "wiki:Toys (Collections); wiki:List of Collections"},
  {"claim": "Client descriptions state the item can be added to the Rockstar Pixie Doll Collection (132311) and the Rockstar Human Doll Collection (132317).", "source": "locale:132311; locale:132317"},
  {"claim": "The 21 in the collection data sits in the reward block beside the finished doll name. It is not a glove price; its exact meaning is unconfirmed.", "source": "repo:collections.json:7438-7447 and :7524-7533"},
  {"claim": "No quest, enemy drop, vendor, event, crafting or prize-wheel source for the glove was found in client text, wiki, articles or video.", "source": "lookup over client, wiki, articles, video for 'Rockstar Doll Gloves' (only locale:40623 and the collection pages returned)"}
 ],
 "confidence": 0.4,
 "open": [
  "The glove's own acquisition path is not evidenced. The only sources are collection membership, which shows what the glove is used for, not how a player obtains it. No drop source is listed; the 'Robgoblin' spawn_type and the 'Central Wilds' / 'Northern Wilds' areas in collections.json (7436/7437, 7522/7523) are collection-level metadata and are not the glove's acquisition location.",
  "No coin price exists for the glove (coin_store_prices empty; no stores.json entry). Price null.",
  "The earlier Pear Jam quest-chain claim is removed. The ids locale:497711267 and locale:774116531 do not exist and are not cited.",
  "The two definitions (3407, 3455) are not mapped to the Pixie or Human collection; the name is shared across both sets.",
  "Retired and live status are not stated by any source. The wiki collection data dates from 2013 (revision 31048). Live: unsure.",
  "wireable: false. Collection membership is evidenced, but no price, quest, enemy or event source exists for the glove."
 ]}
