<!-- fleet job=event-infer id=vcake-fights-v8 status=done turns=2 usd=0.0037 tokens(read,write,in,out)=[8865, 11674, 6, 4328] model=claude-haiku-5-5 -->
# Cake fights

```json
{
 "event": {
  "name": "Free Realms Birthday Bash (anniversary celebration)",
  "aliases": ["Birthday Bash", "birthday party", "anniversary celebration", "Free Realms birthday event"]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "April 29, 2010 anniversary; party from the announcement until May 10, 2010 (start is the announcement date, exact day not stated)", "source": "articles fact:event, http://www.freerealms.com/article/detail.action?articleId=1267 (\"fell on April 29, 2010 ... until May 10, 2010\"); end also in articleId=1330"},
  {"year": 2011, "when": "Second anniversary party, ran to May 18, 2011 (start not confirmed; April 28 anniversary is inferred from a 2011-04-30 capture, not stated)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2099; articleId=2107; articleId=2106"},
  {"year": 2012, "when": "Third-anniversary Bash, April 28, 2012 (Station Cash tripled on 4/28/2012) through May 24, 2012", "source": "http://www.freerealms.com/article/detail.action?articleId=2580 (\"ran through May 24, 2012\"); articleId=2578"},
  {"year": 2013, "when": "4th birthday, April 29, 2013 (start only; end not in pack)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2924 (title \"Happy 4th Birthday, Free Realms!\")"}
 ],
 "recurring": "Annual. Wiki describes it as \"an annual event held throughout the month of April\" tied to the April 29, 2009 launch day (wiki:Birthday Bash; wiki:Events). Dated windows for 2010-2013 all start in late April and end in May (May 10, 18, 24), so the wiki's April framing and the articles' May end dates conflict; both are recorded.",
 "zones": ["Sanctuary", "Sacred Grove"],
 "npcs": ["Camellia (Sanctuary; articleId=1267, 2107)", "Queen Valerian (Sanctuary, 2012 cake bake-off storyline; articleId=2580)", "Cakenstein (boss; locale:9043; wiki:Cakenstein)", "Cakelings, Cakenstein's minions (locale:428041; wiki:Cakeling)", "Chef Jarvie (locale:428045)", "Glerga (locale:428065)", "General Glowlight (Sanctuary, sends players to defeat Cakenstein outside Queensfields; locale:428094)"],
 "quests": ["Cakenstein Attacks!", "Defeat Cakenstein!", "Cakenstein's Last Stand (locale:428064)"],
 "activities": [
  "Fight Cakenstein and his cakelings in Sacred Grove and around Sanctuary (articleId=2580; wiki:Cakeling; wiki:Birthday Bash)",
  "Daily party-prep quests from Camellia and Sanctuary residents, plus subscriber-only party quests (articleId=2106, 2107)",
  "Log in during the Bash for a free Birthday Cake hat (articleId=2580, 2578)",
  "Cake bake-off competition for Sacred Grove chefs (locale:707)"
 ],
 "items": [
  {"name": "Balloon Bow", "price": null, "currency": null, "source": "locale:6792 (must own from the Cakenstein Attacks! encounter to buy)"},
  {"name": "Balloon Hammer", "price": null, "currency": null, "source": "locale:6793"},
  {"name": "Balloon Saw", "price": null, "currency": null, "source": "locale:6794"},
  {"name": "Balloon Sword", "price": null, "currency": null, "source": "locale:6795"},
  {"name": "Balloon Axe", "price": null, "currency": null, "source": "locale:6796"},
  {"name": "Balloon Wand", "price": null, "currency": null, "source": "locale:6797"},
  {"name": "Birthday Cake Hat", "price": null, "currency": "reward", "source": "articleId=2580; articleId=2578"},
  {"name": "Boss Birthday Cake", "price": null, "currency": "reward", "source": "locale:14419 (collect area cakes); articleId=2107, 2106 (not re-verified here)"},
  {"name": "Birthday Crates (party supplies)", "price": null, "currency": null, "source": "articleId=2106; articleId=1261"},
  {"name": "Birthday Bash Marketplace furniture (Wall Sconce, Chair, Floor Lamp, Dining Table, Bed)", "price": null, "currency": null, "source": "wiki:Template:News/Archive (April 24, 2012 Marketplace update)"}
 ],
 "rewards": [
  "Balloon weapons from Cakenstein Attacks! (Bow, Hammer, Saw, Sword, Axe, Wand; locale:6792-6797)",
  "Birthday Cake Hat (2012; articleId=2580, 2578)",
  "Boss Birthday Cake for collecting area cakes (locale:14419)",
  "Different t-shirt per party area and illusions (articleId=2106)"
 ],
 "evidence": [
  {"claim": "The 2010 anniversary fell on April 29, 2010, with a birthday party in game from the announcement until May 10, 2010.", "source": "articles fact:event, http://www.freerealms.com/article/detail.action?articleId=1267"},
  {"claim": "A 2010-04-02 pre-launch repost said large-scale cake fights would come soon and the anniversary celebration was planned for April 28, 2010. This is a plan, not a confirmed live run.", "source": "http://www.tentonhammer.com:80/node/83041"},
  {"claim": "The 2012 Bash ran through May 24, 2012; Cakenstein disrupted the celebration across Sacred Grove; Queen Valerian led a cake bake-off storyline in Sanctuary.", "source": "http://www.freerealms.com/article/detail.action?articleId=2580"},
  {"claim": "Sacred Grove is a Bash zone: Cakelings appear throughout Sacred Grove during the Birthday Bash, and the Sacred Grove cake competition and Cakenstein are tied to the birthday event.", "source": "wiki:Cakeling; locale:707; articleId=2580"},
  {"claim": "Balloon Bow and the other balloon weapons can be bought only after owning them from the Cakenstein Attacks! encounter.", "source": "locale:6792-6797"},
  {"claim": "Cakenstein is the boss; 'Cakenstein Attacks!' and 'Defeat Cakenstein!' are client quest titles.", "source": "locale:9043; locale:4917; locale:4948; wiki:Cakenstein"},
  {"claim": "The 2013 4th birthday was April 29, 2013.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2924 (title only)"},
  {"claim": "The Bash is an annual event anchored on the April 29, 2009 launch day.", "source": "wiki:Birthday Bash; wiki:Events"}
 ],
 "confidence": 0.6,
 "open": [
  "Name merge: 'Cake fights' (the pack's original title) is not a separate event. It is a feature of the anniversary Bash. The 2010-04-02 tentonhammer 83041 item is a pre-launch plan.",
  "Roaming Cakenstein is excluded. Client strings locale:6707-6713 ('Cakenstein has risen in' Shrouded Glade, Briarwood, Blackspore, Merry Vale, Seaside, Wugachug, Snowhill) describe a separate roaming world event. No source ties it to the April-May window. wiki:Cakenstein's 'only Birthday Bash and Treasure War' line is unreliable and unexplained.",
  "Boss Birthday Cake count (eight zone cakes, locale:14419) is not reconciled with the undated seven-Mystery-Meat-cake Glerga storyline (articles/articles.json:21124). I did not verify the count of eight. The seven-cake storyline is treated as a separate, undated feature and not counted as a Bash occurrence.",
  "2010 start day is not exact (announcement date unknown). The April 28 plan in tentonhammer 83041 is not a confirmed live date.",
  "2011 start: April 28 is inferred from a 2011-04-30 capture, not stated in articleId=2099.",
  "2013 end date not in pack. The Sanctuary dancing detail from the earlier draft is removed because articleId=2924's summary does not confirm it.",
  "Recurrence conflict: wiki says the Bash runs through April, while dated articles run to May 10-24. Both are recorded; end date varies by year.",
  "Prices and currency for Birthday Crates, the zone cakes and the furniture are not in evidence (price null).",
  "Excluded name-only matches: Cake-Fight Cake (locale 428147), Cake-Fight Pile Spawner (locale 4852), Mystery Cake, Shrouded Glade Birthday Cake. Article 1306 (Gétostein) and article 1282 (Queensfields, undated) are not tied to the event.",
  "Zones beyond Sanctuary and Sacred Grove are not confirmed. Happy Valley and Robgoblin Camp are removed for lack of a source.",
  "'Kuchenstein' is the German boss name, not an alias. 'Anniversary Bash' and '1st birthday celebration' are removed as guesses."
 ]
}
```
