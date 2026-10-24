<!-- fleet job=event-infer id=vcakenstein-attacks-v4 status=done turns=2 usd=0.0057 tokens(read,write,in,out)=[11852, 21993, 6, 5641] model=claude-haiku-5-5 -->
# Cakenstein Attacks!

```json
{
 "event": {
  "name": "Cakenstein Attacks!",
  "aliases": ["Cakenstein's Last Stand (quest)", "Cakenstein battle (quest)", "Gâtostein (Cakenstein) boss", "Kuchenstein (German name)"]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "First-anniversary Birthday Party; party ran from the posting day until May 10, 2010 (April 28 vs April 29 start unresolved, see open)", "source": "http://www.freerealms.com/article/detail.action?articleId=1293 (2010 guide, Cakenstein fight); articles.json summary of articleId 21096 and 15146 (party until May 10)"},
  {"year": 2011, "when": "Second-anniversary party; post says it runs from the posting date until May 18 (posting year inferred, see open)", "source": "http://www.freerealms.com/article/detail.action?articleId=2107 (fact:event, Cakenstein fought during the party)"},
  {"year": 2012, "when": "Third-anniversary Birthday Bash; ran through May 24, 2012", "source": "http://www.freerealms.com/article/detail.action?articleId=2580 (fact:event: Cakenstein loose in Sacred Grove); tentonhammer.com news 'free-realms-celebrates-its-3rd-birthday-with-new-events' (return of Cakenstein)"}
 ],
 "recurring": "Yearly with the Free Realms birthday party (2010, 2011, 2012 sourced); 2013 is wiki-only and unverified",
 "zones": ["Sanctuary", "Queensfields", "Sacred Grove", "Merry Vale", "Seaside", "Snowhill", "Shrouded Glade", "Wugachug", "Blackspore", "Briarwood"],
 "npcs": ["Cakenstein", "Cakeling", "Camellia", "General Glowlight", "Commander Kiggle", "Glerga", "Chef Jarvie"],
 "quests": ["Cakenstein Attacks!", "Cakenstein's Last Stand", "Defeat Cakenstein in Queensfields"],
 "activities": [
  "Fight Cakenstein and his cakelings, and stop them from stealing the birthday cake (articleId 1293; articleId 2580)",
  "Defeat Cakenstein by launching fireworks at him; Commander Kiggle says he can only be defeated this way (locale:428096; locale:428092; articles 1284)",
  "Defeat Cakenstein seven times in the 2010 guide (articleId 1293 summary; the 'seven' count is from the summary, not a quoted line)",
  "Go to Queensfields to start the battle with General Glowlight's quest (articles quests.json 'Cakenstein battle'; articleId 1282)",
  "Buy balloon weapons after completing the Cakenstein Attacks! encounter (locale:6792-6797)"
 ],
 "items": [
  {"name": "Balloon Bow", "price": null, "currency": null, "source": "locale:6792 ('Must own the Balloon Bow from the Cakenstein Attacks! combat encounter to buy')"},
  {"name": "Balloon Hammer", "price": null, "currency": null, "source": "locale:6793"},
  {"name": "Balloon Saw", "price": null, "currency": null, "source": "locale:6794"},
  {"name": "Balloon Sword", "price": null, "currency": null, "source": "locale:6795"},
  {"name": "Balloon Axe", "price": null, "currency": null, "source": "locale:6796"},
  {"name": "Balloon Wand", "price": null, "currency": null, "source": "locale:6797"}
 ],
 "rewards": [
  "Right to buy the Balloon weapons (Bow, Hammer, Saw, Sword, Axe, Wand) after the Cakenstein Attacks! encounter (locale:6792-6797)"
 ],
 "evidence": [
  {"claim": "'Cakenstein Attacks!' is a quest title (quest_title) with objective 'Defeat Cakenstein!' and a description telling the player to stop Cakenstein before he eats the birthday cake.", "source": "locale:4917; locale:4948; locale:4918; locale:4949"},
  {"claim": "The quest title is a sub-event inside the Birthday Bash party. The pack's name for the 2010-2013 party line is 'Birthday Bash' (wiki:Cakenstein, Category:Birthday Bash), so Cakenstein Attacks! is kept as the boss storyline, not a separate event.", "source": "wiki:Cakenstein; wiki:Cakeling; locale:695 ('Birthday Bash 2012'); articleId 2580"},
  {"claim": "Cakenstein is a cake monster from a baking accident in Glerga's kitchen, after she added Mystery Meat to a bake-off cake. Cakenstein appears wherever one of the seven cakes was sent.", "source": "http://www.freerealms.com/article/detail.action?articleId=1284 (fact:event)"},
  {"claim": "Cakenstein's cakelings try to steal the birthday cake; players must stop them with fireworks before they can be hit.", "source": "http://www.freerealms.com/article/detail.action?articleId=1293 (fact quote: 'Il faut d'abord les empêcher en utilisant le feu d'artifice.')"},
  {"claim": "A cakeling that returns cake to Cakenstein makes him invulnerable for a short time.", "source": "http://www.freerealms.com/article/detail.action?articleId=1284 (fact:mechanic); articles.json summary of articleId 21124"},
  {"claim": "Cakenstein rises in seven party zones: Shrouded Glade, Briarwood, Blackspore, Merry Vale, Seaside, Wugachug, Snowhill.", "source": "locale:6707-6713 ('Cakenstein has risen in ...')"},
  {"claim": "Sacred Grove hosts the birthday cake competition; Cakenstein and the cakelings disrupt it; Camellia near the great tree in Sanctuary starts it.", "source": "locale:707; articleId 2580"},
  {"claim": "General Glowlight in Sanctuary sends players to Queensfields to defeat Cakenstein.", "source": "locale:428094; locale:428092; articleId 1282 (quest: 'Go to Queensfields and find Cakenstein. Start the battle')"},
  {"claim": "Commander Kiggle says Cakenstein can only be defeated by launching fireworks at him.", "source": "locale:9043 area text; ucdt string 'Commander Kiggle challenges you to defeat Cakenstein. This monster can only be defeated by launching fireworks at him.' (FreeRealmsLocaleTools test data)"},
  {"claim": "Cakenstein was a 2010 first-anniversary boss, returned in 2011 (second anniversary) and 2012 (third anniversary).", "source": "articleId 1293 (2010); articleId 2107 (2011); articleId 2580 (2012)"},
  {"claim": "The 2010 party ran from its posting day to May 10, 2010.", "source": "articles.json summaries of articleId 21096 and 15146 ('running from the posting date until May 10th')"}
 ],
 "confidence": 0.6,
 "open": [
  "Anniversary start date conflict for 2010: April 28 (tentonhammer node 83041) vs April 29 (articleIds 1267, 1268, 1197 as cited in critique). Not resolved here; no single day is claimed.",
  "2011 end date May 18 and the 'second anniversary' year: the posting year is not printed; summary gives 'captured 2011-04-30; posted 1 week, 1 day ago'. Treat as approximate.",
  "2013 Cakenstein content is wiki-only (wiki:Birthday Bash 2013 section); no article ties Cakenstein to 2013. Not listed as an occurrence.",
  "Warpstone: the pack and wiki say 'has risen in Warpstone', but the client message lists seven zones (locale:6707-6713) and no article names Warpstone. Dropped.",
  "'Eight locations with fireworks in crates' is wiki-only (wiki:Cakenstein) and unverified against an article or client string. Not claimed.",
  "'Birthday Bash!' (locale:29341) was dropped as a quest title: no source ties it to this boss storyline.",
  "'Defeat seven times': the count comes from the articleId 1293 summary only; not seen in a quoted line. Treat as unverified.",
  "Fireworks item name, price and currency not found in the pack or client text; not listed as an item.",
  "Balloon weapon prices and currency not found; left null.",
  "articleId 1282 ('a second Cakenstein from Glerga's strange cakes', General Glowlight, Queensfields) is undated in the pack; its year is not confirmed.",
  "Boss Birthday Cake (locale:14419, collect eight zone cakes) belongs to the wider Birthday Bash, not to this boss storyline. Not listed here.",
  "Birthday Bash clothing, furniture, pets, crates and wall sconce/bed/chair/sofa/table are Birthday Bash items; name-only and not tied to Cakenstein Attacks!. Not listed here.",
  "Cakeling pet, Balloon Animal pet and Birthday Party Crate: sourced to Birthday Bash (wiki and articles 1261/2106/2107) but not to this boss storyline. Listed in the parent event record, not here.",
  "Pack merges the 2010-2013 Birthday Bash anniversary parties under one name, and the 2013 Cakenstein content may be a separate event. Not resolved.",
  "German zone names in articleId 2099 (Jubeltal, Sanddorf, etc.) are not mapped to English zones; the zone list uses only English client text.",
  "Quest 'Cakenstein's Last Stand' (locale:428064, Glerga's batch) and 'Defeat Cakenstein in Queensfields' are sourced as client strings but their exact quest-title status is not confirmed as a live quest title; kept with the client name source."
 ]
}
```
