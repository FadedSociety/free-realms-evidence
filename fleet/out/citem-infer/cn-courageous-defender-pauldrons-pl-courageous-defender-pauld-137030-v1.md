<!-- fleet job=citem-infer id=cn-courageous-defender-pauldrons-pl-courageous-defender-pauld-137030-v1 status=blocked turns=5 usd=0.0026 tokens(read,write,in,out)=[25191, 9039, 12, 2502] model=claude-haiku-5-5 -->
# {n}Courageous Defender Pauldrons{pl="Courageous Defender Pauldrons"}

{"item": {"name": "Courageous Defender Pauldrons", "locale_id": 137030, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 137030, '{n}Courageous Defender Pauldrons'; it is one of seven Courageous Defender pieces/weapons (Axe 98991, Tunic 136190, Helm 136715, Hightops 136295, Gauntlets 136470, Breeches 136820, Pauldrons 137030).", "source": "locale:137030; locale:136190; locale:136295; locale:136470; locale:136715; locale:136820; locale:98991"},
  {"claim": "Courageous Defender Axe is a Level 4 Warrior Green Text weapon that can only be acquired through trade. It is listed among Green Text weapons with 'Blacksmith made, Trade only'. The set is part of the Warrior level-progression gear (Courageous Defender is the Level 8 Warrior title).", "source": "wiki page:ns0 Courageous Defender Axe; wiki page:ns0 Green Text weapon; wiki page:ns0 Warrior"},
  {"claim": "Pack's coin store price 433 cannot be tied to this item: repo stores.json has 433-coin rows (e.g. item_id 9932, 9998, 10584-10586, 10664-10666), but none is keyed to the Pauldrons' definition ids 48030-48041, and no store row matches those ids.", "source": "repo:prototype/osfr-tools/data/content/stores.json (price rows); search for item_id 48030-48041 returned no matches"},
  {"claim": "No wiki page, article, or video covers the Pauldrons; the lookup for set pieces returned only the Axe wiki page.", "source": "lookup: 'Courageous Defender' (wiki, articles, video); no matches for pauldrons/tunic/helm/breeches set-piece queries"}
 ],
 "confidence": 0.25,
 "open": [
  "Coin shop source is unproven: the pack's price 433 is not linked to a store item id for definition 48030-48041; the 'coin_shop' guess should not be accepted until a stores.json row with these definitions is found.",
  "Source is likely the same trade-only/crafted route as the Courageous Defender Axe (Green Text, 'trade only'), but no wiki or article states how the Pauldrons are obtained. Needs a wiki page or a Warrior/Blacksmith/Tailor trade source to confirm.",
  "Retired/live status unverified: no source states whether the set is still obtainable. Live status is 'unsure'.",
  "The 433 price cannot be assigned a currency-backed source; keep it out of sources until a store row maps to this item.",
  "Pack's 'definitions: 35' and 12 definition ids do not show per-tint breakdown or which variant maps to which race; not verified."
 ]}
