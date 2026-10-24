<!-- fleet job=citem-infer id=cn-barnburner-brawler-gloves-pl-barnburner-brawler-gloves-132893-v3 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[7050, 7990, 6, 1721] model=claude-haiku-5-5 -->
# {n}Barnburner Brawler Gloves{pl="Barnburner Brawler Gloves"}

{"item": {"name": "Barnburner Brawler Gloves", "locale_id": 132893, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Evander (Brawler Job merchant, npc 9500000024); sells the six-piece Barnburner Brawler set including the Gloves", "where": "Blackspore Swamp (vendors.json npc 9500000024, npc_content_file blackspore_swamp.json)", "price": "unknown (no captured NPC quote)", "currency": null, "source": "wiki page 'Evander' (Sells list: '[Barnburner] [Brawler] [Gloves]', https://freerealms.fandom.com/wiki/Evander); repo:prototype/osfr-tools/data/content/vendors.json:1831, 2264-2288"},
  {"type": "prize_wheel", "detail": "[Brawler] Prize Wheel, Prince of Low Tide! dungeon reward wheel", "where": "Prince of Low Tide! (dungeon)", "price": "unknown (wheel spin cost blank in wiki excerpt)", "currency": null, "source": "wiki page 'Prince of Low Tide!' (Rewards list: '[Brawler] Prize Wheel' then '[Barnburner] [Brawler] [Gloves]')"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name Barnburner Brawler Gloves, locale 132893, item definition 75885, slot 2, class 25", "source": "locale:132893; client definition in pack"},
  {"claim": "Evander's wiki Sells list includes [Barnburner] [Brawler] [Gloves] with no price shown", "source": "wiki page 'Evander'"},
  {"claim": "Prince of Low Tide! wiki page lists [Barnburner] [Brawler] [Gloves] under the [Brawler] Prize Wheel", "source": "wiki page 'Prince of Low Tide!'"},
  {"claim": "Evander stock in the vendor data includes item 75885", "source": "repo:prototype/osfr-tools/data/content/vendors.json:1831, 2264-2288"},
  {"claim": "Video frame shows the gloves in a clothing inventory listing; not a source by itself", "source": "video:piWfe7lXZ9I/00108"}
 ],
 "confidence": 0.7,
 "open": [
  "Coin store reference price: stores.json item 75885 (category 102) lists purchase 752 coins, member 676, sell 75. This is a reference value only, not a captured Evander or Coin Shop quote, and no live Coin Shop listing was confirmed, so no coin_shop source is recorded.",
  "Evander's current sell price is unknown; no captured NPC quote exists.",
  "Prince of Low Tide! wheel spin cost is blank in the wiki excerpt; the 68/70 figures in the repo note are template inference and are not used.",
  "Croaking Vale, Treeleaf's Retreat and Stealthy Despoilers wheel claims were dropped: no checked page lists the gloves on those wheels. Briar Patch also has a Brawler Prize Wheel but does not show the gloves in the excerpt.",
  "Campfire location near Donovan Shadeweaver's home was not verified; only the Blackspore Swamp zone is supported by vendors.json.",
  "No retirement or removal date found; retired left null. Unknown whether Evander still sells the set today.",
  "Sibling Stick and Move and Rubber Match sets were not traced."
 ]}
