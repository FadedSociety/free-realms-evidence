<!-- fleet job=citem-infer id=cn-medic-s-megasaw-of-vitals-pl-medic-s-megasaw-of-vitals-131957-v1 status=done turns=5 usd=0.0023 tokens(read,write,in,out)=[23275, 7589, 12, 2189] model=claude-haiku-5-5 -->
# {n}Medic's Megasaw of Vitals{pl="Medic's Megasaw of Vitals"}

{"item": {"name": "Medic's Megasaw of Vitals", "locale_id": 131957, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop sale, Medic level 12 weapon (store item 75073, category 207)", "where": "Coin Shop", "price": "1504 coins (member price 1353 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:15089 item 75073; wiki page \"Medic's Megasaw of Vitals\" (Coin Shop mention, price field blank in the snippet)"},
  {"type": "prize_wheel", "detail": "Medic prize wheel; wiki lists Darvon's Descent among the locations (the list continues past the snippet, so other wheel locations are unconfirmed)", "where": "Darvon's Descent, plus further unread locations", "price": null, "currency": null, "source": "wiki page \"Medic's Megasaw of Vitals\" (snippet: 'acquired from the prize wheels at Darvon's Descent, Spawn...')"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name locale 131957 is Medic's Megasaw of Vitals, one of a 10-item Medic Megasaw/Bonesaw variant set (131952-131962)", "source": "locale:131957 and client cluster in evidence pack"},
  {"claim": "Store data lists item 75073 at 1504 purchase coins, 1353 member coins, sell 150 coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:15089"},
  {"claim": "Wiki item tooltip: Resell Value 150, Power 4, Required Level 12 Medic, ability Injure", "source": "wiki image File:Medic's Megasaw of Vitals item.jpg (image:item_tooltip)"},
  {"claim": "Wiki says it is sold in the Coin Shop and drops from Medic prize wheels, first listed at Darvon's Descent", "source": "wiki page \"Medic's Megasaw of Vitals\""},
  {"claim": "Sibling variants (Megasaw of Reflexes, Shock, Triage, Vitamins, Vitae, Alarm, Immunization) use the same Coin Shop + prize wheel pattern", "source": "wiki pages of the sibling Megasaw articles"}
 ],
 "confidence": 0.7,
 "open": [
  "Pack said no wiki page exists, but a wiki page 'Medic's Megasaw of Vitals' does exist; the pack's wiki_page field was wrong.",
  "The wiki's Coin Shop sale price is blank in the snippet; 1504 comes from the repo store data, not a confirmed wiki price. Store data may be older or newer than the wiki.",
  "Full prize wheel location list is truncated after Darvon's Descent ('Spawn...'); read the full wiki page to list all wheels.",
  "Pack's client cluster lists 11 names from 131952-131962 but the item-set/promo context is unverified. No retirement date found in the sources read; retired status unknown.",
  "The 'Medic Prize Wheel' snippets on the Stealthy Despoilers and Darvon's Descent pages are wheel contents, not this item's own source page; they were not counted as separate sources."
 ]}
