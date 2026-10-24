<!-- fleet job=citem-infer id=ctalon-speedster-tires-117428-v1 status=nothing_found turns=4 usd=0.0047 tokens(read,write,in,out)=[35499, 22722, 10, 2967] model=claude-haiku-5-5 -->
# Talon Speedster Tires

{"item": {"name": "Talon Speedster Tires", "locale_id": 117428, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition: id 60903, name 'Talon Speedster Tires', description 'The customized tires for the Talon Speedster.', slot 4, class 98, no coin store price (coin_store_prices empty).", "source": "locale:117428; repo:data/content/stores.json has no entry for it (search for 'Speedster' in repo JSON data finds only seaside.json prose)"},
  {"claim": "Same id 60903 and name appear in other community definition dumps: Lxzxrus-Free-Realms-Server ClientItemDefinitions.json (Id 60903, 'Talon Speedster Tires'), and the Sanctuary and FreeRealms-Legacy dumps list the same comment string.", "source": "refs:Lxzxrus-Free-Realms-Server/src/Resources/ClientItemDefinitions.json:1127257-1127258; refs:Sanctuary-PC2009-20261009/src/Resources/ClientItemDefinitions.json:1109674; refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:1127257"},
  {"claim": "Cluster context: it is one of a family of Speedster kart parts (Talon Speedster Engine 117425, Turbo 117426, Steering Column 117427, Mod 117429; Burster, Privateer tires/engine/turbo/column). The Talon Speedster chassis/kart itself is locale 39224 / 114643.", "source": "locale:117423-117433, locale:39224, locale:114643"},
  {"claim": "Kart parts are a kart-racing progression item (Engine, Boost, Steering, Traction, Slot A/B tabs, Power Rating). The only kart part reward confirmed anywhere is 1 Blast Speedster from Sandstorm's Grand Opening; Speedster tires/parts sources were never recovered.", "source": "notes/Build Guides/Gameplay/Kart Racing.md:24-25; notes/Build Guides/Content/Jobs/Kart Driver.md:25,142,152,203"},
  {"claim": "Card-themed and other Speedster parts exist in the client but how they are obtained is unknown.", "source": "notes/Build Guides/Content/Jobs/Card Duelist.md:247"},
  {"claim": "Lookup of the wiki, articles and video for 'Talon Speedster' / 'Speedster Tires' returned no wiki page, article fact, or video frame naming this tire item.", "source": "lookup queries 'Talon Speedster' (client hits only) and 'Speedster Tires kart part' (no matches in wiki/articles/video)"}
 ],
 "confidence": 0.2,
 "open": [
  "No source found: no vendor stock, coin store price, quest reward, drop, prize wheel, crafting or collection entry names item 60903. The evidence pack's vendor_stock and mentioned_by lists are empty, and the repo has no stores/quests/recipes row for it.",
  "The first-pass 'source_guess: unknown' is confirmed as unknown; it is not evidence. The 'live: yes' tag is a hint only; the item is defined in the client and several community dumps, but no live sale or award was found, so live status is 'unsure'.",
  "Likely a Kart Driver part (Talon Speedster set, sibling of the Blast Speedster Tires). Obtaining route for kart parts is unknown; check Kart Racing rewards, race prize payouts and the Talon Speedster kart's own unlock when more evidence arrives.",
  "Retired status unknown: no wiki or article statement either way.",
  "The kind is set to 'other' because the schema has no kart-part class; a kart part, not a clothing or weapon item."
 ]}
