<!-- fleet job=event-infer id=vf-te-d-anniversaire-birthday-party-v5 status=done turns=5 usd=0.0064 tokens(read,write,in,out)=[69621, 23274, 12, 5667] model=claude-haiku-5-5 -->
# Fête d'Anniversaire (Birthday Party event)

```json
{"event": {"name": "Birthday Bash (Free Realms anniversary party)", "aliases": ["Fête d'Anniversaire pour Free Realms! (French article titles, articleId=1267 and 2100)", "2nd Birthday Party For Free Realms (articleId=2106)", "Happy 4th Birthday, Free Realms! (articleId=2924)", "Birthday Party (generic; article titles only)"]},
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "From April 29, 2010 (1st anniversary); end May 10, 2010 per pack summary, body not re-read", "source": "http://www.freerealms.com/article/detail.action?articleId=1267 (quote: 'fêtera son premier anniversaire le 29 avril 2010'; article undated)"},
  {"year": 2011, "when": "Anniversary April 28, 2011; party announced April 21, 2011; end May 18, 2011 per pack summary, body not re-read", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2106 (dated 2011-04-21; quote 'On April 28th Free Realms will be two years old!')"},
  {"year": 2012, "when": "April 28 to May 24, 2012 (3rd anniversary Birthday Bash)", "source": "http://www.freerealms.com/article/detail.action?articleId=2580 (summary: 'ran through May 24, 2012'); locale:695 ('Birthday Bash 2012 marks the 3rd Anniversary of Free Realms.'); articleId=2578 for the April 28 free-hat day (window start from pack, not re-read)"},
  {"year": 2013, "when": "April 29, 2013 (4th anniversary post; Ambassadors dancing at the Birthday Bash area in Sanctuary)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2924 (summary; no rewards stated; no end date given)"}
 ],
 "recurring": "Yearly around the Free Realms launch/anniversary (April 28-29), observed 2010, 2011, 2012 and 2013. Wiki 'Birthday Bash' also calls it an annual April event (wiki-only wording).",
 "zones": ["Merry Vale", "Seaside", "Snowhill", "Shrouded Glade", "Wugachug", "Sanctuary"],
 "npcs": ["Camellia (starts the cake bake-off near the great tree in Sanctuary; locale:707; articleId=2106)", "Queen Valerian (2012 cake bake-off storyline in Sanctuary; articleId=2580)", "Cakenstein (boss; locale:428098; articleId=2106)"],
 "quests": ["Cakenstein Attacks! (locale:4917 per pack)", "Glerga's Birthday Cake (locale:5170 per pack; 2010 only per articleId=1293)"],
 "activities": ["Daily party-prep quests for the Sanctuary cake bake-off (articleId=2580)", "Defeat Cakenstein (fireworks required; locale:428098; articleId=2106 for cakelings and the boss)", "Collect the eight zone cakes to unlock the Boss Birthday Cake (articleId=1267, 2106 per pack)", "Log in on 4/28/2012 for the free Birthday Cake hat (articleId=2578)", "Ambassador dancing and socializing at the Birthday Bash area in Sanctuary (articleId=2924, 2013)"],
 "items": [
  {"name": "Birthday Bash Furniture Bundle", "price": "1350", "currency": "station_cash", "source": "locale:691 (name); price per locale:692 as cited in pack, not re-read"},
  {"name": "Birthday Cake Hat", "price": null, "currency": "reward", "source": "http://www.freerealms.com/article/detail.action?articleId=2578; wiki item 'Birthday cake hat'"},
  {"name": "Boss Birthday Cake", "price": null, "currency": "reward", "source": "locale:30109; articleId=1267 (pack-reported)"},
  {"name": "Birthday Bash Dining Table, Bed, Chair, Floor Lamp, Wall Sconce", "price": null, "currency": "station_cash", "source": "wiki Template:News/Archive 'Update of April 24, 2012' (Marketplace); client locale:436980, 436981, 436982, 437014, 666"}
 ],
 "rewards": ["Birthday Cake Hat (free on 4/28/2012; articleId=2578)", "Station Cash tripled on 4/28/2012 (articleId=2578, pack-reported)", "Boss Birthday Cake for collecting all eight zone cakes (articleId=1267; 2106 per pack)", "Birthday Party Crate (locale:5664)", "Birthday Party Balloons 4-Pack (video pJzcZTI1Pgk/00238.jpg, Cakenstein Attacks win screen)"],
 "evidence": [
  {"claim": "The 2010 first-anniversary party was tied to April 29, 2010.", "source": "http://www.freerealms.com/article/detail.action?articleId=1267"},
  {"claim": "Birthday parties in 2010 were set up in eight zones, including a Sanctuary party area (French names: Vallée joyeuse, Colline des Neiges, Clairière Embrumée, Spore Noire, Bois des Bruyères).", "source": "http://www.freerealms.com/article/detail.action?articleId=1267 (facts.json); articleId=2100 (French, undated, same title)"},
  {"claim": "The 2011 second-birthday party post is dated April 21, 2011 and lists eight areas: Merry Vale, Seaside, Snowhill, Shrouded Glade, Wugachug, Blackspore, Briarwood, Sanctuary.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2106"},
  {"claim": "The 2012 Bash ran through May 24, 2012 as the third anniversary celebration.", "source": "http://www.freerealms.com/article/detail.action?articleId=2580; locale:695"},
  {"claim": "Queen Valerian led a cake bake-off storyline in Sanctuary in 2012, with daily party-prep quests and Cakenstein.", "source": "http://www.freerealms.com/article/detail.action?articleId=2580"},
  {"claim": "The 4th-anniversary post is dated April 29, 2013 and invites players to the Birthday Bash area in Sanctuary for dancing with the Ambassadors.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2924"},
  {"claim": "Furniture named Birthday Bash was on the Marketplace in the April 24, 2012 update.", "source": "wiki Template:News/Archive"},
  {"claim": "Cakenstein is defeated with fireworks.", "source": "locale:428098"}
 ],
 "confidence": 0.6,
 "open": [
  "The 2010 end date (May 10) and the 2011 end date (May 18) come from the pack summary. I did not confirm them in the article bodies. Only the start dates are sourced (1267 quote; 2106 date 2011-04-21).",
  "The 2012 start (April 28) rests on articleId=2578, which I did not re-read. The end (May 24) is from the 2580 summary.",
  "2013 is a single anniversary post (2924). No event window or end date is sourced, so it is not counted as a verified run.",
  "Zone list is mixed across years. 2010 (1267) and 2011 (2106) both name eight areas, but the lists differ. The 2011 list (Merry Vale, Seaside, Snowhill, Shrouded Glade, Wugachug, Blackspore, Briarwood, Sanctuary) is the one tied to a dated article. Criqueville and Heather Moor/Wood have no English mapping and are left out. Zones are not year-tagged in the pack.",
  "Content lists are pooled across years. Glerga and Chef Jarvie are sourced only to 2010 (articleId=1293) and are dropped from the general NPC list. Queen Valerian is 2012 only. Cakelings are 2010-2011 only.",
  "Quest titles are pack-reported. Only the lines locale:707 (description), locale:428098 and locale:428708-428711 (Sal Monella / Bordon Cloo bake-off lines) were checked. The exact quest-title strings need a quest-table check before wiring.",
  "Zone Birthday Cakes (eight cakes, station_cash): wiki 'Cake' only, prices unknown. Balloon weapons (Hammer, Bow, Axe, Sword, Saw, Wand), zone birthday T-shirts and Piñata Pony are wiki-only (no dated article), so they are not counted as event items. Piñata Pony is sold during the Bash via the SC Marketplace per the wiki, but the price is unknown.",
  "Ambassador Hide and Seek: announced for the 2010 party (articleId=1308) only. Not confirmed for later years.",
  "Commander Kiggle (articleId=1282) is undated. No dated source ties him to a year, so he is left out of the NPC list.",
  "Treasure War listing for Cakenstein is not confirmed in any source I read, so it is not stated.",
  "The French article 2100 (undated) is treated as the same 2010 post as 1267 (same title). Its zone list is not independently dated.",
  "Name merge: the 2009 launch-day party is not the same as the anniversary Bash. The wiki says the Bash celebrates the April 29, 2009 launch; no launch-year Bash is sourced, so 2009 is not counted."
 ]
}
```
