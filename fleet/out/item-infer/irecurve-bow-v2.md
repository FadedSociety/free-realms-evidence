<!-- fleet job=item-infer id=irecurve-bow-v2 status=done turns=3 usd=0.0029 tokens(read,write,in,out)=[19092, 15104, 8, 1736] model=claude-haiku-5-5 -->
# Recurve Bow

{"item": {"name": "Recurve Bow", "locale_id": 13617, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Shiny Straightshot (archer bow seller); sold the Recurve Bow, the wiki says, until retirement", "where": "Farnum's Farm", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Recurve_Bow (prose: 'previously sold by Shiny Straightshot at Farnum's Farm for  coins, until retired on December 14, 2009'; amount blank in the wiki text; category Vendor Weapons); repo:notes/Build Guides/Content/NPCs/NPCs - Farnum Farmstead.md:79 (vendor name, place, retirement date only, no price)"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Recurve Bow is a level 4 Archer weapon (Power 2) with Barrage 488 damage and Volley 885 damage.", "source": "https://freerealms.fandom.com/wiki/Recurve_Bow"},
  {"claim": "Wiki prose says the bow was sold by Shiny Straightshot at Farnum's Farm 'for  coins' with the amount blank; the wiki gives no sale price.", "source": "https://freerealms.fandom.com/wiki/Recurve_Bow (verified by lookup on the wiki page text)"},
  {"claim": "Retired December 14, 2009; the wiki says it can now be acquired only through trade.", "source": "https://freerealms.fandom.com/wiki/Recurve_Bow"},
  {"claim": "Client name 'Recurve Bow' is locale 13617.", "source": "locale:13617"},
  {"claim": "Shiny Straightshot's name is in the client text (ugdt 3190862422), but no client data confirms stock or location.", "source": "repo:prototype/osfr-tools/data/content/vendors_unresolved.json:2911-2940 (stock unresolved, 'no prices', no item-level stock evidence)"}
 ],
 "confidence": 0.4,
 "open": [
  "Price is unverified. The wiki prose has the amount blank. The earlier answer's 640 coins has no visible source: the pack's coins field [640] is unexplained and the infobox is null. Do not use 640 until a source is found.",
  "Vendor stock is unverified: vendors_unresolved.json lists Shiny Straightshot's stock as unresolved with no prices, and the only stock evidence is the wiki's retired-item mention.",
  "Wiki says the item is now obtainable only through player trade. Trade is not a listed source type, so it is not recorded as a source.",
  "The wiki image tooltips (Archer's Recurve Bow of Volleys / of Flame, level 12, 1492 damage) are upgraded variants, not this base item, and are not evidence here.",
  "No quest, drop, event, prize-wheel, or coin-shop source found in the pack."
 ]}
