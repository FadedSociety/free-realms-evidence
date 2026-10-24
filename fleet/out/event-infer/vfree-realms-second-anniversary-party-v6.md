<!-- fleet job=event-infer id=vfree-realms-second-anniversary-party-v6 status=done turns=3 usd=0.0041 tokens(read,write,in,out)=[23491, 15164, 8, 4019] model=claude-haiku-5-5 -->
# Free Realms second anniversary party

```json
{
 "event": {
  "name": "Free Realms second anniversary party (2011)",
  "aliases": [
   "2nd Birthday Party For Free Realms (article 2106 title)",
   "Aniversário do FreeRealms! (article 2107 Portuguese title)",
   "Cakenstein birthday cake party (boss named 'Kuchenstein' in article 2099, 'Cakenstein' in client and articles 2106/2107)"
  ]
 },
 "kind": "holiday",
 "live": "no",
 "occurrences": [
  {"year": 2011, "when": "Posted around 2011-04-21 (date field; approximate, inferred from 'Posted 1 week, 1 day ago' at capture 2011-04-30); ran from the post date until May 18, 2011. Anniversary April 28.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2106 (date 2011-04-21, captured 2011-04-30, refs articles/articles.json:14747-14754); corroborated by http://www.freerealms.com/article/detail.action?articleId=2107 ('Começando hoje e marcado para terminar dia 18 de maio', captured 2011-06-04)"}
 ],
 "recurring": null,
 "zones": ["Merry Vale", "Seaside", "Snowhill", "Shrouded Glade", "Wugachug", "Blackspore Swamp", "Briarwood", "Sanctuary"],
 "npcs": [
  "Camellia (party contact in Sanctuary; article 2107 says 'Camellia/Camilla')",
  "Cakenstein (cake creature boss; article 2106 and 2107 text)",
  "Cakelings (cake helpers; article 2106 'cakeling helpers', 2107 'ajudantes bolomorfos')"
 ],
 "quests": [],
 "activities": [
  "Complete daily and subscriber-only party quests given in Sanctuary (article 2107 summary; 2106 'Speak-to-Camellia quest hub')",
  "Collect the eight zone birthday cakes; collecting all eight gives a free Boss Birthday Cake (locale:14419)",
  "Battle Cakenstein and his cakelings (article 2106 and 2107)",
  "Eat the Boss Birthday Cake to become a holiday event boss for 10 minutes (locale:30127)"
 ],
 "items": [
  {"name": "Shrouded Glade Birthday Cake", "price": null, "currency": null, "source": "locale:9392; zone cake list in article 2107 (summary only)"},
  {"name": "Seaside Birthday Cake", "price": null, "currency": null, "source": "locale:9393; article 2107 summary"},
  {"name": "Snowhill Birthday Cake", "price": null, "currency": null, "source": "locale:9394; article 2107 summary"},
  {"name": "Merry Vale Birthday Cake", "price": null, "currency": null, "source": "locale:9395; article 2107 summary"},
  {"name": "Sanctuary Birthday Cake", "price": null, "currency": null, "source": "locale:9396; article 2107 summary"},
  {"name": "Wugachug Birthday Cake", "price": null, "currency": null, "source": "locale:9397; article 2107 summary"},
  {"name": "Blackspore Swamp Birthday Cake", "price": null, "currency": null, "source": "locale:9398; article 2107 summary"},
  {"name": "Briarwood Birthday Cake", "price": null, "currency": null, "source": "locale:9399; article 2107 summary"},
  {"name": "Boss Birthday Cake", "price": null, "currency": "reward", "source": "locale:30109 (name); locale:14419 (free for collecting all eight)"},
  {"name": "Cakeling pet", "price": null, "currency": null, "source": "article 2106 per quest-lines/enemy-packs.json fact ('Cakeling and Balloon Animal pets can be purchased individually', articleId=2106); Marketplace sale, not a reward"}
 ],
 "rewards": [
  "Boss Birthday Cake, free for collecting all eight zone birthday cakes (locale:14419)",
  "Birthday gifts from daily and subscriber party quests (article 2107 summary: balloon weapons, t-shirts, illusions; not dated to 2011 by a specific source)"
 ],
 "evidence": [
  {"claim": "Second-anniversary party announced with a 2011-04-21 date (approximate), running from the post date until May 18; anniversary April 28", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2106 (refs articles/articles.json:14747-14754)"},
  {"claim": "Party ran to May 18 and was 'starting today' in the Portuguese post", "source": "http://www.freerealms.com/article/detail.action?articleId=2107 (quote 'Começando hoje e marcado para terminar dia 18 de maio')"},
  {"claim": "Party events held in eight zones: Merry Vale, Seaside, Snowhill, Shrouded Glade, Wugachug, Blackspore, Briarwood, Sanctuary", "source": "http://www.freerealms.com/article/detail.action?articleId=2107 (quote 'Vale Feliz, Litoral, Colina Nevada, Clareira Encoberta, Wugachug, Semente Negra, Floresta de Espinhos e Santuário')"},
  {"claim": "Cakenstein and cakelings must be fought during the party", "source": "http://www.freerealms.com/article/detail.action?articleId=2107 (quote 'Você também vai ter que lutar com Cakenstein')"},
  {"claim": "Collecting all eight zone cakes gives a free Boss Birthday Cake", "source": "locale:14419"},
  {"claim": "Eating the Boss Birthday Cake turns the eater into a holiday event boss for 10 minutes", "source": "locale:30127"},
  {"claim": "Cakeling pets were sold individually in the Marketplace during this party", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2106 (via quest-lines/enemy-packs.json fact)"}
 ],
 "confidence": 0.6,
 "open": [
  "Live status: 'no'. The 2011 window ended May 18, 2011. Do not schedule as a current event.",
  "Start date: 2011-04-21 is the article's date field but the summary calls it approximate (inferred from 'Posted 1 week, 1 day ago' at capture 2011-04-30). The exact posting day is not printed.",
  "Article 2107's full text was not in the refs tree; its zone list, quest-giver and cake details are from the pack summary and quotes only. Article 2106's full text was also not read; its claims come from its summary.",
  "Locale 9392-9399 and 30109 confirm names but carry no dates; the 2011 tie for the cakes rests on articles 2106/2107.",
  "Recurrence: null. Around-April-28 parties are observed for 2010 (article 1330 / tentonhammer), 2011 (this record) and 2012 (article 2578), but no source says they recur and the content is not shown to match, so no yearly claim is made. The 2010 bake-off (locale:707) and the 2012 birthday event are separate records and are not evidence for this one.",
  "The 'Birthday Bash' name is a multi-year family name, not an alias of this 2011 occurrence.",
  "Balloon Animal pet, Birthday Party Crate, Balloon Pet Pumper and anniversary firework/ring/spray/arrow: not tied to 2011 by a dated source here; excluded. The balloon weapons in locale 6792-6797 belong to the 'Cakenstein Attacks!' encounter and are not dated to 2011.",
  "Prices: no source gives a price for any cake, so price and currency are null for the zone cakes.",
  "Quest titles: none verified. No exact quest titles are given; 'A Piece of Cake', 'Undelivered Confections' and 'Birthday Cake Bake-off' are not used.",
  "Boss name conflict: article 2099 says 'Kuchenstein'; client and articles 2106/2107 use 'Cakenstein'.",
  "Pre-launch webcast (article 2098, possibly 2011-04-21) is a separate pre-launch item, not a live party activity, and is not included here.",
  "Pack gaps: wiki category members empty; no quest answers mention this event."
 ]
}
```
