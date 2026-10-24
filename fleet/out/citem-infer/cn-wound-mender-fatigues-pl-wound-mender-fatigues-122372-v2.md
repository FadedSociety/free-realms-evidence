<!-- fleet job=citem-infer id=cn-wound-mender-fatigues-pl-wound-mender-fatigues-122372-v2 status=done turns=3 usd=0.0036 tokens(read,write,in,out)=[19356, 15565, 8, 2909] model=claude-haiku-5-5 -->
# {n}Wound Mender Fatigues{pl="Wound Mender Fatigues"}

{"item": {"name": "Wound Mender Fatigues", "locale_id": 122372, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store listing (vendor and NPC unconfirmed): client definition carries coin_store_prices [828] for the Wound Mender Fatigues definitions", "where": null, "price": "828", "currency": "coins", "source": "client definition coin_store_prices [828] for definition ids 42373-42428 (pack client_definition); no matching store row found in repo:data/content/stores.json by item id 42373-42428 or by name (search for 'Wound Mender' in repo JSON returns only prototype/osfr-tools/data/reference/weapons.json:52020, the Bonesaw)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name for the item is locale 122372 '{n}Wound Mender Fatigues{pl=\"Wound Mender Fatigues\"}'", "source": "locale:122372"},
  {"claim": "Same-set client names: Wound Mender Jacket (122368), Boots (122369), Gloves (122370), Helmet (122371); the set also has a Backpack string in the locale file", "source": "locale:122368, locale:122369, locale:122370, locale:122371; en_us_data.dat 'Wound Mender Backpack' (1924069727, 4001081949)"},
  {"claim": "Client definition gives a coin store price of 828 for this item; 828 is also the purchase price of many unrelated stores.json rows (e.g. item_id 4, 576, 1986), so it looks like a shared price tier and does not by itself identify this item's vendor", "source": "client definition coin_store_prices [828]; prototype/osfr-tools/data/content/stores.json lines 65, 277, 542"},
  {"claim": "Wiki: Wound Mender Bonesaw is a level 16 Medic weapon, Green Text, 'can only be acquired through trade'. This is the only wiki page on the Wound Mender set; it does not name the fatigues", "source": "wiki page Wound Mender Bonesaw; wiki page Green Text weapon (lists Wound Mender Bonesaw as Green Text)"},
  {"claim": "Wiki Medic page lists '[Wound] [Mender]' at Level 17, which is a Medic ability name, not this item", "source": "wiki page Medic"},
  {"claim": "No wiki page, article, video, quest, enemy drop or vendor names Wound Mender Fatigues", "source": "lookup over client, wiki, articles, video for 'Wound Mender Fatigues' and 'Wound Mender'; repo and refs search for 42373 and Wound Mender"}
 ],
 "confidence": 0.25,
 "open": [
  "Vendor, location and store row for the 828-coin price are unidentified. The definition ids do not appear as item ids in repo:data/content/stores.json, so the price is client-only evidence and is not tied to a vendor.",
  "Definition count conflict: the client definition reports 16 definitions but lists only 12 ids (42373-42428). Do not treat the count as settled.",
  "Live status is unsure: the only sale signal is the client store price. No sighting, store row or wiki price confirms it is sold now.",
  "Whether the Wound Mender set (Bonesaw is trade-only, Green Text) is trade-only, sold by a coin vendor, or both is unresolved.",
  "Retirement status unknown; no source says it was retired or unobtainable later.",
  "Client definition description is empty; no set-bonus or flavour text available.",
  "Critique relabel: the 'coin_store' type is not in the schema, so the coin-store listing is recorded as type 'vendor' with vendor unknown. The critique's point that 'vendor' overstates the evidence is accepted; it is a price-only source."
 ]}
