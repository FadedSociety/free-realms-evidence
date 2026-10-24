<!-- fleet job=event-infer id=vdefenders-storyline-v4 status=done turns=3 usd=0.0033 tokens(read,write,in,out)=[16309, 10446, 8, 3600] model=claude-haiku-5-5 -->
# Defenders storyline

{
 "event": {"name": "Free Realms Trading Card Game Series 4: Heroes (TCG Heroes set launch)", "aliases": ["Heroes", "TCG Set 4: HEROES", "Heroes expansion", "Heroes (Helden / Héros / Héroes)"]},
 "kind": "other",
 "live": "yes",
 "occurrences": [
  {"year": 2012, "when": "August 25, 2012 (launch day; single source)", "source": "http://www.tentonhammer.com:80/free-realms/news/free%20Relams%20Gets%20a%20New%20Trading%20Card%20Game (summary: 'launched on 2012-08-25 with 76 cards (54 booster, 22 promo)')"}
 ],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": ["Buy and open Heroes booster packs for TCG cards", "Play the Heroes TCG set (single-player scenarios, per article 2733)", "Collect tournament promo cards from the set"],
 "items": [
  {"name": "Heroes Booster Pack", "price": null, "currency": null, "source": "locale:17470 (type item); locale:17471 (10 random TCG cards plus one loot card per pack)"},
  {"name": "Heroes Booster Bundle (25 Pack)", "price": null, "currency": null, "source": "locale:7973; locale:9403 ('Save on TCG Set 4: Heroes Booster Bundles!')"}
 ],
 "rewards": ["Heroes TCG booster cards (10 per pack) and one loot card per pack (locale:17471)", "Tournament promo cards (article 2733 fact:release)"],
 "evidence": [
  {"claim": "Heroes is the fourth Free Realms TCG set and introduces the Realmkeepers, with Baron von Darkcheat as the villain.", "source": "locale:17471; locale:17473 ('TCG Set 4: HEROES'); http://www.freerealms.com/article/detail.action?articleId=2738 (fourth set)"},
  {"claim": "Heroes was released as a new expansion for the TCG, with new features, single-player scenarios, tournament promo cards and new loot cards.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2733 (fact:release)"},
  {"claim": "Heroes launched 2012-08-25 with 76 cards (54 booster, 22 promo) and four quests leading to a final boss.", "source": "http://www.tentonhammer.com:80/free-realms/news/free%20Relams%20Gets%20a%20New%20Trading%20Card%20Game (summary). Single source; no second article confirms the date."},
  {"claim": "Heroes booster packs are client item records (type item) sold as TCG product. Earlier wording that they are 'not an in-game item' is withdrawn: the client classifies them as items.", "source": "locale:17470 (item); locale:17471"},
  {"claim": "Article 2737 (Spanish, relative date 'Publié il y a 2 mois, 6 jours') is a pre-launch-style announcement with no absolute date, so it is not used for dating.", "source": "http://www.freerealms.com/article/detail.action?articleId=2737 (article summary, date null)"},
  {"claim": "Heroes is a free-to-play TCG release.", "source": "http://www.tentonhammer.com:80/free-realms/news/free%20Relams%20Gets%20a%20New%20Trading%20Card%20Game (summary); locale:17473 ('TCG Sets 1 - 4 Quests now free to play!')"}
 ],
 "confidence": 0.55,
 "open": [
  "Timing: the start is 2012-08-25 from one Ten Ton Hammer summary only; no second dated source was found in this pass. The end of sales is unknown. Earlier claims that Heroes packs appeared in the Pumpkin Prince bundle (locale:9922, October 2012) and the Abominable Snowman bundle (December 2012) could not be re-verified in this pass (lookups on wiki for those pages returned nothing), so they are not used as occurrences. Recheck wiki 'Pumpkin Prince' and 'Abominable Snowman' before extending the window.",
  "Price and currency for the booster pack and 25-pack bundle are not given in any source. Both are null. locale:7968/7974 wording is not a price.",
  "Wireable: NO. There is a start date but no sourced end date or recurrence, so it cannot be scheduled as a bounded event. Schedule as a dated product release only, pending a second source.",
  "The in-game Zelda / Realmkeepers quest line (quests 'Card Duelist: Zelda's Warning' locale:439671, 'Card Duelist: Heart of Darkness' locale:7948, 'Card Duelist: Meet the Boss' locale:7960; NPCs Madam Zelda, Ghostshadow, Magetech, Wildclaw) is NOT attached to this event. It is a separate candidate and has no dated source. Quests were content-matched only and are excluded from this record. Its zones conflict (Blackspore Swamp in article 2734 / locale 7948 vs Sporeshade Swamp in article 2740; Sunstone Valley in locale 5100175-5100176) and must be split by storyline before any entry.",
  "Naming conflict: pack title 'Defenders storyline' is not an alias here. Article 2737 names the child Defenders as Bryce, Nathan, Onofre and Jessica, while article 2733 names Ghostshadow (Bryce), Magetech (Nathan), Wildclaw (Kade) and Jessica. Onofre vs Kade is unresolved. Baron Trampaoscura (articles 2735/2736/2737/2740) is a Spanish/French alias of Baron von Darkcheat, and this is only the pack's quote, not separately verified.",
  "Series 3 vs Series 4: the Baron von Darkcheat booster and costume are Series 3 (wiki pages 'Baron von Darkcheat Costume', 'Bruce'; article 2739 Snow Hill storyline). Kept as a separate candidate; not merged with Heroes.",
  "Article 2735 is confirmed in this pass only as a fact:event and summary (Spanish promotional news for the expansion). Article 2742 is confirmed as a French release notice. Article 2744 (German) names the Realm Guardians. None of these is dated here.",
  "Pumpkin Prince bundle locale:9922 is a separate promotion, not this event. locale:7966 is a FLAGGED duplicate of 7960 and is not used.",
  "Special prize for beating the Baron's final challenge is not named in any source and is not listed."
 ]
}
