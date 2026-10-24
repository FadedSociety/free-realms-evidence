<!-- fleet job=event-infer id=vheroes-card-expansion-v7 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[6972, 7551, 6, 2456] model=claude-haiku-5-5 -->
# Heroes (card expansion)

{"event": {"name": "Heroes (Free Realms Trading Card Game expansion, TCG Set 4)", "aliases": ["TCG Set 4", "TCG Set 4: HEROES", "Heroes Booster Pack", "Heroes Booster Bundle (25 Pack)", "Heroes questline"]},
 "kind": "update",
 "live": "unsure",
 "occurrences": [],
 "recurring": null,
 "zones": [],
 "npcs": ["Madam Zelda (locale:439496; article 2742 summary)", "Baron von Darkcheat (locale:439496; article 2742 summary; article 2720 summary)"],
 "quests": ["A True Hero (locale:441609 title; objective locale:441610 'Complete the Heroes Questline.')"],
 "activities": ["Play Heroes TCG cards, including single-player scenarios (article 2733 summary)", "Buy Heroes booster packs and bundles (locale:17470; locale:7973)", "Complete the Heroes questline (locale:441610)"],
 "items": [
   {"name": "Heroes Booster Pack", "price": null, "currency": "station_cash", "source": "locale:17470 (names the pack). Price conflict: video:1LjCvhboCkQ/00188.jpg shows 249 and video:9NOkMosko1E/00024.jpg shows 224; unresolved, so price is null."},
   {"name": "Heroes Booster Bundle (25 Pack)", "price": null, "currency": null, "source": "locale:7973; locale:9403 ('Save on TCG Set 4: Heroes Booster Bundles!', undated)"}
 ],
 "rewards": ["Tournament promo cards and new loot cards (article 2733 summary)"],
 "evidence": [
   {"claim": "Heroes is the newest expansion of the Free Realms TCG and was released (undated).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2733 ('was released and adds new features'); http://www.freerealms.com/article/detail.action?articleId=2744 ('ist da!', relative date only)"},
   {"claim": "Heroes had arrived when the post was written and is the TCG's fourth set (undated).", "source": "http://www.freerealms.com/article/detail.action?articleId=2738"},
   {"claim": "Heroes has arrived (French post, undated).", "source": "http://www.freerealms.com/article/detail.action?articleId=2742"},
   {"claim": "Story: Baron von Darkcheat, Madam Zelda and four child Guardians; each Guardian has a deck, weapon and mount.", "source": "http://www.freerealms.com/article/detail.action?articleId=2742 (summary); http://www.freerealms.com/article/detail.action?articleId=2744 (summary)"},
   {"claim": "Client text: four heroes defeat Baron von Darkcheat; Madam Zelda ties to the story.", "source": "locale:439496"},
   {"claim": "Pre-launch teaser with new cards and four new characters. A plan, not a live event; not used for occurrences.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2720 (summary)"},
   {"claim": "Client: 'TCG Set 4: HEROES Available Now!' (undated client text).", "source": "locale:17472"},
   {"claim": "Quest title and objective.", "source": "locale:441609 (title); locale:441610 (objective)"}
 ],
 "confidence": 0.3,
 "open": [
   "Launch date unverified. No article in the pack gives an absolute date for Heroes; 2733, 2738, 2742 and 2744 say 'released' or 'has arrived' only, and 2744 gives a relative date ('2 Monate, 6 Tage'). The earlier 2012 / Aug 25 claim had no retrieved source and is dropped. occurrences is empty, so this is not wireable as a timed entry.",
   "End date, availability window and recurrence: no source. Treated as a single release.",
   "Price conflict 249 vs 224 station_cash is unresolved. Bundle price unknown.",
   "Realmkeeper naming conflicts: article 2733 summary names Bryce, Nathan, Kade, Jessica; article 2744 names Geisterschatten, Magotron, Wildkralle, Adlersehne; wiki names Crackshot, Magetech, Ghostshadow, Wildclaw. Not listed as NPCs.",
   "Baron Trampaoscura (article 2735 summary) is an unresolved villain-name conflict with Baron von Darkcheat. Removed from npcs; the 2735 text retrieved does not name the villain.",
   "Blackspore Swamp removed: the only source was an article 2734 summary that was not re-read, and no retrieved text places the story there.",
   "Locale 441611 and 441612 are flagged duplicates and are not cited. Locale 440112 is a flagged dev note and is excluded.",
   "Sparky and Sirdo rewards removed: no source in the pack ties them to this questline.",
   "Seasonal bundles containing Heroes packs (locale:9922 Pumpkin Prince; Snow Days unverified) are separate events and are not counted.",
   "kind 'update' is a guess for a TCG card-set release; a TCG or card-set category may be wanted.",
   "live 'unsure': the articles call it a past release, but the pack does not show current availability."
 ]
}
