<!-- fleet job=event-infer id=vheroes-rewards-v8 status=done turns=4 usd=0.0038 tokens(read,write,in,out)=[25924, 12222, 10, 4000] model=claude-haiku-5-5 -->
# Heroes rewards

{"event": {"name": "Heroes (Free Realms Trading Card Game expansion, TCG Set 4)", "aliases": ["TCG Set 4: HEROES", "TCG Set 4", "Heroes Booster Pack", "Heroes Booster Bundle (25 Pack)"]},
 "kind": "update",
 "live": "unsure",
 "occurrences": [
  {"year": 2012, "when": "August 25, 2012 (reported launch date; secondary source only, SOE original not checked)", "source": "http://www.tentonhammer.com:80/free-realms/news/free%20Relams%20Gets%20a%20New%20Trading%20Card%20Game (Ten Ton Hammer, dated 2012-08-25; refs articles/articles.json:19147-19150, articles/quests.json:1400-1458, articles/facts.json:42433-42443)"}
 ],
 "recurring": null,
 "zones": ["Blackspore Swamp (locale:117000; the Gypsy who hands out Heroes starter Mystery Chests, per the Ten Ton Hammer 2012-08-25 article)"],
 "npcs": ["Gypsy (hands out Heroes starter Mystery Chests in Blackspore Swamp; Ten Ton Hammer 2012-08-25 via articles/facts.json:42433). Name not given beyond 'the Gypsy'."],
 "quests": ["Card Duelist: Heart of Darkness", "Card Duelist: Slow and Steady", "Card Duelist: Stinky Feet", "Card Duelist: Meet the Boss"],
 "activities": ["Playing single-player TCG scenarios (http://www.freerealms.com/article/detail.action?articleId=2744)", "Entering TCG tournaments for promo cards (articleId=2744)", "Opening Heroes booster packs and bundles", "Completing the Card Duelist quest series (Ten Ton Hammer 2012-08-25)", "Collecting the Heroes starter Mystery Chests from the Gypsy in Blackspore Swamp"],
 "items": [
  {"name": "Heroes Booster Pack", "price": null, "currency": null, "source": "locale:17470 (name only)"},
  {"name": "Heroes Booster Bundle (25 Pack)", "price": null, "currency": null, "source": "locale:7973 (name only); locale:9403 ('Save on TCG Set 4: Heroes Booster Bundles!')"}
 ],
 "rewards": ["Exclusive single-player scenario rewards (articleId=2744)", "Tournament promo cards (articleId=2744)", "New loot cards (articleId=2744)", "Heroes starter Mystery Chests (Ten Ton Hammer 2012-08-25)"],
 "evidence": [
  {"claim": "Heroes is the newest TCG expansion, adding single-player scenarios with exclusive rewards, promo cards at major tournaments and new loot cards (German text, relative date only).", "source": "http://www.freerealms.com/article/detail.action?articleId=2744"},
  {"claim": "Heroes headline 'Heroes ... is here!' (article 2733; the 'was released' wording was not verified, so only the headline is cited).", "source": "http://www.freerealms.com/article/detail.action?articleId=2733 (headline quote in facts.json:68459)"},
  {"claim": "Heroes reported as launched 2012-08-25 as a TCG with 76 cards (54 booster, 22 promo) and four quests ending in a boss fight against Baron von Darkcheat. Secondary source only.", "source": "http://www.tentonhammer.com:80/free-realms/news/free%20Relams%20Gets%20a%20New%20Trading%20Card%20Game (dated 2012-08-25; articles/articles.json:19147-19150)"},
  {"claim": "Four Card Duelist quests are tied to the Heroes launch article dated 2012-08-25: Heart of Darkness (locale:7947), Slow and Steady (locale:7951), Stinky Feet (locale:7955), Meet the Boss (locale:7959).", "source": "articles/quests.json:1400-1458 (Ten Ton Hammer 2012-08-25)"},
  {"claim": "The Gypsy who gives out the Heroes starter Mystery Chests is in Blackspore Swamp (locale:117000).", "source": "articles/facts.json:42433-42443 (Ten Ton Hammer 2012-08-25)"},
  {"claim": "Heroes Booster Pack and Heroes Booster Bundle (25 Pack) are client item names; the store text ties Heroes Booster Bundles to TCG Set 4.", "source": "locale:17470, locale:7973, locale:9403"},
  {"claim": "The Pumpkin Prince seasonal bundle includes two Heroes packs. It is a separate seasonal promotion and is not counted as a Heroes occurrence.", "source": "locale:9922"}
 ],
 "confidence": 0.5,
 "open": [
  "The 2012-08-25 date rests on one secondary source (Ten Ton Hammer, 2012-08-25). It is not confirmed against the SOE original or against article 2733's posting date.",
  "Articles 2744 and 2733 carry no absolute date in the pack (2744 gives a relative 'ago' date).",
  "Live status is 'unsure'. The in-game quests and Gypsy chests are dated to the same 2012-08-25 secondary article, but no independent dated in-game window was found, and it is still a product launch rather than a timed event window.",
  "Heroes item prices are unverified: the 249 vs 224 Station Cash conflict is unresolved, and StoreBundles.json:24963 was not opened. Currency is null because no source gives it.",
  "Realm Guardians (Geisterschatten, Magotron, Wildkralle, Adlersehne; articles 2744, 2742) have no matching client NPC entries, so they are not listed as npcs.",
  "Possible conflation: the Heroes launch has a boss fight against Baron von Darkcheat, who also appears in the Series 3 TCG set. They are treated as separate events. The pack does not confirm which set the Darkcheat quests belong to.",
  "Pre-launch teaser (articles.json:19136) and 'Meet Free Realms' Newest Heroes' (articles.json:19164) are undated previews and are not counted as occurrences.",
  "Excluded: article 2876 (Rumbledome), article 2764 (Sets 1-3 sale), 'Hero of Heroes' (locale 4419490-4419502, not_live), generic 'hero' tournament text (locale 391785), locale:17473 (banner covering Sets 1-4), and Madam Zelda/Darkcheat strings (locale 7948, 7960, 7961, 7966, 439496) not tied to Heroes by name.",
  "The pack's Heroes quest chain (German quest-pack-free post, articles.json:20158) and the 'Stinky Feet' / 'Meet the Boss' naming still need confirmation against the article text beyond the quests.json record."
 ]
}
