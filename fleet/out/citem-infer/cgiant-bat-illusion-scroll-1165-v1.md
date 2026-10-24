<!-- fleet job=citem-infer id=cgiant-bat-illusion-scroll-1165-v1 status=nothing_found turns=5 usd=0.0043 tokens(read,write,in,out)=[46342, 20063, 12, 2740] model=claude-haiku-5-5 -->
# Giant Bat Illusion Scroll

{"item": {"name": "Giant Bat Illusion Scroll", "locale_id": 1165, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines the item: locale 1165 'Giant Bat Illusion Scroll', definition id 4006, item class 9, no models, no coin store price, description 'Using this scroll will temporarily change the player into a Greater Screecher.' (ucdt 1281832156).", "source": "locale:1165; client definition pack; FreeRealmsLocaleTools/test/FreeRealmsLocaleTools.Tests/data/en_us_data.dat:33919 (ucdt 1281832156)"},
  {"claim": "Item is a shape-change illusion consumable. Its siblings in the client are 'Arboreal Giant Illusion Scroll' (locale 1159), 'Evil Snowman Illusion Scroll' (locale 36377), and the 'Illusion: Screecher Boss - 1 minute' string (ucdt 1107375821), so it belongs to the illusion-scroll family.", "source": "locale:1159; locale:36377; en_us_data.dat:29328"},
  {"claim": "The cluster around locale 1165 (Trader's Berries, Mushroom Souffle, Illusion Food - Man-Eating Plant, Sonic Sundae, Illusion Food - Dove/Eagle/Hawk/Raven, Honeydew Drop Cake) is the same family of transformation consumables. The text 'Eating this food will cause you to change into a Screecher!' (ucdt 669486100) is a related Screecher food line. No source is given for any of them.", "source": "client cluster from pack; en_us_data.dat:17710"},
  {"claim": "No coin vendor, wiki page, article, video frame, enemy drop, quest reward, or coin shop listing for this scroll was found. repo stores.json, vendors.json, and enemies.json have no item 4006 or name match. Searches of the wiki, articles, and video for 'Illusion Scroll' and 'Greater Screecher' returned nothing for it.", "source": "lookup (client, wiki, articles, video); search repo *.json for 'Illusion Scroll|Giant Bat|1165'"},
  {"claim": "'Giant Bat' is a real enemy in Frostfang Caverns (locale 1792121157 / 1041065255). The scroll's name links it to that bat, but nothing ties the scroll to a bat drop.", "source": "repo:prototype/osfr-tools/data/content/dungeons/frostfang_caverns.json:481"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found. Possible routes are an event (illusion/holiday scroll packs), a promotion, or a Frostfang Caverns bat drop, but none is evidenced, so none is listed.",
  "Live status is unknown. The first-pass tag 'live: yes' is only a hint. The client defines the item, but no store, vendor, or wiki listing confirms it was ever sold or given out.",
  "Retired status is unknown. No source states it was retired or unobtainable.",
  "Check the wiki for 'Giant Bat Illusion Scroll', 'Arboreal Giant Illusion Scroll', and 'Evil Snowman Illusion Scroll' together. If they share an event or vendor, the same source may cover this scroll.",
  "No model files or variants are listed (definitions: 1, models: []), so there is no variant check."
 ]}
