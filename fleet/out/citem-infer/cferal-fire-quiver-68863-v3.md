<!-- fleet job=citem-infer id=cferal-fire-quiver-68863-v3 status=nothing_found turns=4 usd=0.0035 tokens(read,write,in,out)=[34636, 15183, 10, 2551] model=claude-haiku-5-5 -->
# Feral Fire Quiver

{"item": {"name": "Feral Fire Quiver", "locale_id": 68863, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text: locale 68863 is 'Feral Fire Quiver' (ucdt 1072094256, ugdt 2054442898); no description text.", "source": "locale:68863; FreeRealmsLocaleTools/test/FreeRealmsLocaleTools.Tests/data/en_us_data.dat:28408 and :54098"},
  {"claim": "Client item definitions: 16 blocks with Comment 'Feral Fire Quiver' in ClientItemDefinitions.json, starting at line 199086 (Id 10603, Cost 828, MemberDiscount 10, MinProfileRank 17, Slot 6, Class 16) and last at line 199418. The 12-id range 10603-10614 in the pack was not checked against the other four blocks.", "source": "repo ref FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json lines 199086-199418"},
  {"claim": "No store row carries the 828 price or any id in the quiver range: a repo-wide search for a price/cost of 828 in JSON found only collection_catalogue.json id 828, which is unrelated. So the coin price is a client definition field only, not a coin vendor sale.", "source": "repo search prototype/osfr-tools/data/content, pattern for 828 price/cost"},
  {"claim": "Wiki Archer page: '[Feral] [Fire] (17)' is a skill entry, and the Vendors list (Sanctuary lvl 20 clothing, Greenwood Camp lvl 20 clothing, Briarwood) does not name the quiver.", "source": "wiki page Archer (skills and Vendors sections)"},
  {"claim": "The wiki's Feral Fire Bow page (a level 16 Archer weapon, 'can only be acquired through trade') concerns the Bow, not the Quiver.", "source": "wiki page Feral Fire Bow"},
  {"claim": "Wiki OCR 'Feral Fire Boots' coin-balance screen (File:Gg.jpg) is about Boots, not the Quiver.", "source": "wiki image File:Gg.jpg"}
 ],
 "confidence": 0.2,
 "open": [
  "Coin price 828 (client Cost, MemberDiscount 10) has no vendor, shop or stores.json row; the previous coin_shop source is removed because it had no evidence. Needs a CoinStoreItems row keyed to definition ids 10603-10614 or a wiki/video listing before a coin source can be stated.",
  "Member price ~745 (828 x 0.9) is arithmetic from the definition field, not a store price; do not list it as a price.",
  "Definition ids: the 16 blocks are confirmed by Comment at lines 199086-199418, but ids 10615-10618 (or whichever four ids are the rest) were not read. The 10603-10614 list is only partly checked.",
  "No quest reward, drop, event, prize-wheel, collection, crafting or membership source found in the wiki, articles, video, or repo.",
  "Retirement and live status unknown; the first-pass 'live yes' is not supported by a source beyond the client definition.",
  "Critique fixes applied: the coin_shop source was dropped (evidence critique and world critique), the 16-definition count was kept but ids were not all listed, and the Bow and Boots evidence was marked as a neighbour only, not used for the Quiver."
 ]}
