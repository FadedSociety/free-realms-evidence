<!-- fleet job=item-infer id=icortez-v1 status=nothing_found turns=2 usd=0.0019 tokens(read,write,in,out)=[3237, 9646, 6, 1338] model=claude-haiku-5-5 -->
# Cortez

{"item": {"name": "Cortez", "locale_id": 5102562, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "'Cortez' is an NPC (npc_name), not an item. Locale 5102562 is the NPC name string.", "source": "locale:5102562"},
  {"claim": "Cortez is a human NPC merchant at the Briarwood Crafting Station near the Vale of the Ancients who sells Miner job items; the page has no coin, Station Cash, or Coin Shop prices.", "source": "https://freerealms.fandom.com/wiki/Cortez"},
  {"claim": "The wiki Cortez page lists the items he sells: Drift Miner Kerchief, Helmet, Gloves, Boots, Coveralls; Miner's Flair Shard of Prosperity; Miner's Power Shard, Necklace, Pickaxe of Timing V; Miner's Dynamite and Shovel of Talent V. Those are the real item sources, and they belong on those item pages, not on this one.", "source": "https://freerealms.fandom.com/wiki/Cortez"},
  {"claim": "Cortez was added in the 15 October 2013 update.", "source": "https://freerealms.fandom.com/wiki/Cortez"},
  {"claim": "Repo vendor records already hold Cortez's stock as a vendor entry with the wiki as its only source; no prices were found.", "source": "prototype/osfr-tools/data/content/vendors.json:9022"}
 ],
 "confidence": 0.9,
 "open": [
  "The evidence pack is for an NPC, not an item. No item-level sources were given for 'Cortez', so no sources are listed.",
  "Re-run this job on one of the items Cortez sells (for example, Drift Miner Kerchief or Miner's Pickaxe of Timing V) to get its real sources and prices.",
  "Cortez's stock prices are not on the wiki page (no coin, Station Cash, or Coin Shop price), so the vendor price is unknown.",
  "The wiki page's 'Sells' list has no prices or currency, so the vendor currency is unconfirmed."
 ]}
