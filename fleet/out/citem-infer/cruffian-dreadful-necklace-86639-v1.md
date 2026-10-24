<!-- fleet job=citem-infer id=cruffian-dreadful-necklace-86639-v1 status=nothing_found turns=4 usd=0.0038 tokens(read,write,in,out)=[24052, 17305, 10, 2765] model=claude-haiku-5-5 -->
# Ruffian Dreadful Necklace

{"item": {"name": "Ruffian Dreadful Necklace", "locale_id": 86639, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is 'Ruffian Dreadful Necklace' (definition 22648, slot 9, class 42, no coin store price, no models listed).", "source": "locale:86639"},
  {"claim": "The 'Ruffian ___ Necklace/Ring' family (Dreadful, Fateful, Infernal, Spectral, Mystical, Phantasmal, Eternal, Celestial, Ethereal) is a set of client item names sitting in the same locale block as 'Shiny ___ Necklace' (86634-86638). This shows a set of variants, not a sourced item.", "source": "locale:86634-86647; repo:opening-harvesting-native-20261009T142624Z/locale/en_us_data.dat (ugdt 621343471 'Ruffian Dreadful Necklace')"},
  {"claim": "The word 'Ruffian' in the client ties to the Biker Ruffians at Wheelie Pete's in Rumble Ridge, Sunstone Valley (quest objective 'Knock some sense into those Biker Ruffians. They wrecked my diner!' 656083302; completion 329539895; objective 1137642790 'Knock out the Biker Ruffians'). No text links these necklaces to that quest, so this is only a name-level lead.", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Sunstone Valley.md:242; repo:opening-harvesting-native-20261009T142624Z/locale/en_us_data.dat lines 17378, 8739, 30151"},
  {"claim": "The jewelry family shares the name pattern 'X Dreadful Necklace' with many prefixes (Hardwood, Granite, Metallic, Jeweled, Dull, Rascal, Intern, Sneak, Grunt, Sage), so 'Dreadful' is likely a tier or rarity word. Its source is not shown in the data.", "source": "locale:69670, 69682, 69692, 69703, 86522-86567"},
  {"claim": "No wiki page, article, video frame, coin vendor stock, or other answer names this item. Lookups for 'Dreadful Necklace' in wiki, articles and video returned no matches.", "source": "lookup (wiki, articles, video) for 'Dreadful Necklace'"}
 ],
 "confidence": 0.1,
 "open": [
  "No source found. The pack has no vendor stock, quest reward, drop, event, or store price. Do not add a source until one is found.",
  "Possible lead, unconfirmed: the Ruffian set may come from the Biker Ruffian enemies or the Wheelie Pete's quest chain in Rumble Ridge (Sunstone Valley). Needs a drop table or reward check (e.g., quest rewards for 2871991629, 3144862928, 329539895) before use.",
  "The first-pass tag 'live: yes' is a cheap-model hint only. Live status is unconfirmed; the set's Dreadful/Fateful/Infernal variants may be a crafting or prize-wheel set, and that is also unchecked.",
  "Check the repo's stores.json and recipes for item id 22648 or the Ruffian family, and any prize-wheel or event tables, which were not found in this search."
 ]}
