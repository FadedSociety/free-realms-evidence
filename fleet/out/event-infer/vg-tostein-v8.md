<!-- fleet job=event-infer id=vg-tostein-v8 status=done turns=2 usd=0.0032 tokens(read,write,in,out)=[9265, 9641, 6, 3877] model=claude-haiku-5-5 -->
# Gâtostein

```json
{
 "event": {
   "name": "Birthday Bash (Free Realms launch-anniversary party; boss Cakenstein, French name Gâtostein)",
   "aliases": ["Birthday Bash", "Cakenstein (English client name, locale:707)", "Gâtostein as boss name in French articles (1293, 1267, 2100)", "Kuchenstein (German, article 2099)"]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
   {"year": 2010, "when": "Ran until May 10, 2010 (anniversary April 29, 2010; start = launch-day kickoff per 1268 summary, the start date is not printed)", "source": "http://www.freerealms.com/article/detail.action?articleId=1267 ; http://www.freerealms.com:80/article/detail.action?articleId=1268"},
   {"year": 2011, "when": "Ran from the post date until May 18, 2011 (anniversary April 28 per 2107; exact post date not stated)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2099 ; http://www.freerealms.com/article/detail.action?articleId=2107"},
   {"year": 2012, "when": "Third-anniversary Birthday Bash, through May 24, 2012", "source": "http://www.freerealms.com/article/detail.action?articleId=2580"}
 ],
 "recurring": "Yearly around the April 29 launch anniversary, running into May (dated 2010, 2011, 2012). The 2013 4th-birthday Sanctuary Birthday Bash area (article 2924) has no boss named and no end date, so it is noted but not counted as a boss-party occurrence.",
 "zones": ["Sanctuary (party hub, bake-off, party prep per 2580)", "Sacred Grove (Cakenstein disruption, article 2580)"],
 "npcs": ["Cakenstein / Gâtostein (party boss; articles 1293, 1267, 2100)", "Cakeling / Gâtolin (helpers; wiki Cakeling, article 1306)", "Camellia (bake-off start; locale:707)", "Queen Valerian (article 2580)"],
 "quests": ["Cakenstein Attacks! (locale:4917)"],
 "activities": [
   "Defeat Cakenstein/Gâtostein seven times during the birthday event, using fireworks (article 1293)",
   "Daily birthday party prep and bake-off in Sanctuary (article 2580)",
   "Stop cakelings from bringing cake to the boss, which makes it invulnerable for a short time (article 1306; the mechanic is undated, applied here only by name match to the boss)"
 ],
 "items": [
   {"name": "Balloon Hammer", "price": null, "currency": "reward", "source": "wiki page Balloon Hammer; locale:6792-6797 ('from the Cakenstein Attacks! combat encounter')"},
   {"name": "Balloon Bow", "price": null, "currency": "reward", "source": "wiki page Balloon Bow; locale:6792-6797"},
   {"name": "Balloon Axe", "price": null, "currency": "reward", "source": "wiki page Balloon Axe; locale:6792-6797"},
   {"name": "Balloon Sword", "price": null, "currency": "reward", "source": "wiki page Balloon Sword; locale:6792-6797"},
   {"name": "Balloon Saw", "price": null, "currency": "reward", "source": "wiki page Balloon Saw; locale:6792-6797"},
   {"name": "Balloon Wand", "price": null, "currency": "reward", "source": "wiki page Balloon Wand; locale:6792-6797"},
   {"name": "Cupcake Hat", "price": null, "currency": null, "source": "wiki page Cupcake Hat (Birthday Bash item; no price or year in source)"}
 ],
 "rewards": ["Balloon weapons from the Cakenstein Attacks! prize wheel (wiki; locale:6792-6797; no year attached)", "Cupcake Hat (wiki; no year attached)"],
 "evidence": [
   {"claim": "Gâtostein is the French name of the client's Cakenstein, the Birthday Bash boss; defeat it seven times during the birthday event with fireworks", "source": "http://www.freerealms.com/article/detail.action?articleId=1293"},
   {"claim": "The 2010 party ran until May 10, 2010, held from the anniversary (April 29, 2010)", "source": "http://www.freerealms.com/article/detail.action?articleId=1267 ; http://www.freerealms.com:80/article/detail.action?articleId=1268"},
   {"claim": "The 2011 party ran until May 18, 2011, with Kuchenstein and cakelings", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2099 ; http://www.freerealms.com/article/detail.action?articleId=2107"},
   {"claim": "The 2012 Birthday Bash ran through May 24, 2012, with Cakenstein in Sacred Grove and a Sanctuary bake-off", "source": "http://www.freerealms.com/article/detail.action?articleId=2580"},
   {"claim": "The 2013 4th birthday had a Birthday Bash area in Sanctuary with dancing and socialising; no boss named", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2924"},
   {"claim": "Cakenstein Attacks! is the quest name for the Cakenstein encounter", "source": "locale:4917 ; locale:707 ; locale:4732 ; locale:4918 ; locale:4949"},
   {"claim": "Balloon weapons are prize-wheel rewards of the Cakenstein Attacks! encounter", "source": "wiki Balloon Hammer / Balloon Bow / Balloon Axe / Balloon Sword / Balloon Saw / Balloon Wand; locale:6792-6797"}
 ],
 "confidence": 0.5,
 "open": [
   "MERGE, not resolved in favour of one event: the roaming Gâtostein (articles 1306 and 1300: 'appears everywhere', unpredictable times, Gâtolin helpers, Prés des Fées battle at Sanctuary) is undated and has no party, birthday or zone link in the pack. It is a separate candidate event, kind 'other', live 'unsure', not wireable. Only the boss-name mapping ties it to the party (1267, 2100, 1293).",
   "Verification gap: a lookup of 'Birthday Bash Cakenstein Gâtostein' against the articles and wiki indexes returned no matches, so the article texts above (1267, 1268, 1293, 2099, 2107, 2580, 2924) and the wiki balloon/cupcake pages were not re-read here. They rest on the evidence pack as supplied. The wiki category 'Birthday Bash' listing is also empty in the pack.",
   "2010 start date: April 29 is inferred from the anniversary in 1267 and the 1268 summary; only 'until May 10' is printed. The 2011 post date (2011-04-21) from the earlier draft is dropped as unsourced.",
   "Article 2106 cited earlier is not in the index and is dropped.",
   "2013: article 2924 describes a 4th-birthday Birthday Bash area with no boss and no end date; not counted as a boss-party occurrence.",
   "Balloon weapons and Cupcake Hat have no year in any source; they are not placed in a specific occurrence.",
   "Birthday Cake Hat: only the item name (locale:694) is supported; the free-login reward claim is removed.",
   "Quests not added (undated or unchecked): General Glowlight birthday prep (locale:428094), Queensfields Cakenstein fight (locale:428092, 428096), Cakenstein's Last Stand (locale:428064/428065). Their year is open.",
   "Zones: Queensfields is from the first-anniversary guide only and is not verified. Boss presence in 2013 unconfirmed.",
   "Helper naming: 'Gâtolin' appears only in French articles; 'cakeling' in English articles, wiki and client. Probably the same helper.",
   "Prices: no source gives prices; all null. Cakeling pet and Birthday T-shirts are excluded (not tied to the event here).",
   "NPCs Queen Valerian, Camellia, Glerga and General Luminaire Prés des Fées are tied only by cited articles/locale; NPC records not checked. Glerga belongs to the roaming-Gâtostein origin story, not to the party."
 ]
}
```
