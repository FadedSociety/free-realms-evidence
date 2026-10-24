<!-- fleet job=item-infer id=ishadowblade-v1 status=done turns=2 usd=0.0015 tokens(read,write,in,out)=[3410, 4644, 6, 1813] model=claude-haiku-5-5 -->
# Shadowblade

{"item": {"name": "Shadowblade", "locale_id": 3635, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Yoko (weapon vendor, Ninja weapon)", "where": "Lakeshore", "price": "1656 coins", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Shadowblade (rev 47425: 'previously sold by Yoko in Lakeshore for coins'; category Vendor Weapons); repo:prototype/osfr-tools/data/content/npc_spawns_extra.json:28178 (NPC 'Yoko' exists in spawn data)"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Shadowblade is a level 16 Ninja weapon sold by Yoko in Lakeshore for coins until retired on December 14, 2009.", "source": "https://freerealms.fandom.com/wiki/Shadowblade"},
  {"claim": "Wiki lists a single coin price of 1656.", "source": "https://freerealms.fandom.com/wiki/Shadowblade (infobox coins field)"},
  {"claim": "Categories include Vendor Weapons, Retired Weapons, Level 16 Weapons, Power 5 Weapons, Ninja, Dragonstrike.", "source": "https://freerealms.fandom.com/wiki/Shadowblade (categories)"},
  {"claim": "Client name string for Shadowblade is locale 3635.", "source": "locale:3635"},
  {"claim": "Shadowblade is a collection prize only as 'Magical Essence Shadowblade' (level 20), a different item.", "source": "repo:notes/Build Guides/Content/Jobs/Ninja.md:174; repo:prototype/osfr-tools/data/content/collections.json:4196"}
 ],
 "confidence": 0.6,
 "open": [
  "Single wiki price 1656 coins is not marked as regular or sale price; the pack gives no second price, so treat as the only stated price.",
  "Tooltip image conflicts with the wiki page: tooltip shows Power 2, 'Deals 488 damage' and Resell Value 33, while the wiki text says Power 5 category with 2372 and 10674 damage. Likely a different rank/version; not resolved.",
  "No vendor stock data for Yoko in the pack and no repo vendor entry confirming Shadowblade is in her stock list; the sale is supported only by the wiki text.",
  "Exact date of Yoko's sale start is not given; only the retirement date (December 14, 2009) is stated.",
  "Wiki page has broken file links (category 'Pages with broken file links'); the image evidence is partial."
 ]}
