<!-- fleet job=citem-infer id=cwarrior-s-necklace-of-vitality-iv-131197-v2 status=done turns=4 usd=0.0042 tokens(read,write,in,out)=[35879, 18071, 10, 3142] model=claude-haiku-5-5 -->
# Warrior's Necklace of Vitality IV

{"item": {"name": "Warrior's Necklace of Vitality IV", "locale_id": 131197, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Marius (male Pixie merchant, Warrior job gear); wiki Marius 'Sells' section lists Warrior's Necklace of Vitality IV (repo record: stock_source kind wiki, page Marius, section Sells, revision 2013-10-08)", "where": null, "price": "unverified: 1504 coins reference price (member 1353 coins) from stores.json, reconstructed, not a captured in-game quote", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/vendors.json lines 12433-12474 (Marius, Sells listing); repo:prototype/osfr-tools/data/content/stores.json line 17371 item 75453 (price_provenance: reconstructed)"},
  {"type": "prize_wheel", "detail": "Warrior Prize Wheel, reward from the 'Prince of Low Tide!' battle (Cook-off Catastrophe quest area; the Prince is a difficulty 4 battle started by clicking him)", "where": "Seaside, north end near the Tide Pools", "price": null, "currency": null, "source": "wiki: https://freerealms.fandom.com/wiki/Prince_of_Low_Tide! (Warrior Prize Wheel list includes Warrior's [Necklace of] Vitality IV); wiki page text 'Prince of Low Tide! is a difficulty 4 battle ... found in the north end of the region, near the Tide Pools'"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name and locale ID 131197 match the client definition (definition 75453, slot 8, class 15).", "source": "locale:131197"},
  {"claim": "Marius's wiki Sells list includes Warrior's Necklace of Vitality IV; the repo record cites the wiki page revision 2013-10-08 (not an addition date).", "source": "repo:prototype/osfr-tools/data/content/vendors.json lines 12433-12474"},
  {"claim": "Coin store entry for item 75453: purchase 1504 coins, member 1353 coins, sell 150 coins; price basis is a legacy reference with no captured retail quote.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 17371"},
  {"claim": "Warrior Prize Wheel on the Prince of Low Tide! page lists Warrior's Necklace of Vitality IV.", "source": "wiki: Prince_of_Low_Tide! (wheel list snippet)"},
  {"claim": "Prince of Low Tide! is a difficulty 4 battle started by clicking the Prince in Seaside, north end near the Tide Pools.", "source": "wiki: Prince_of_Low_Tide!"},
  {"claim": "The Oasis of Peril!, Grexan's Camp and Mushroom Mania! wiki snippets list an Archer's Necklace of Vitality IV on the Archer wheel, not the Warrior entry; the earlier claim that those pages list this Warrior item is not confirmed.", "source": "wiki: Oasis_of_Peril!, Grexan's_Camp, Mushroom_Mania! (snippets)"}
 ],
 "confidence": 0.6,
 "open": [
  "Marius vendor price 1504 coins is not evidenced; it is a reconstructed store reference. Do not treat it as the vendor's real price until a captured quote exists.",
  "Marius's location (Briarwood, near the Warpstone) and the 'added 1 Oct 2013' date are not confirmed by the wiki text seen; the repo record only gives a 2013-10-08 revision timestamp.",
  "Prize wheel drop rate is unknown (random reward); no wheel price is given.",
  "Live/retired status not established: no source says the Marius stock or the Warrior wheel was removed, and no current check was made. Left as unsure.",
  "Oasis of Peril!, Grexan's Camp and Mushroom Mania! were cited by the prior answer for the Warrior wheel entry; the snippets show only the Archer wheel entry for this necklace, so those sources were dropped."
 ]}
