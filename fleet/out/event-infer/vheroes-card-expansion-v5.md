<!-- fleet job=event-infer id=vheroes-card-expansion-v5 status=done turns=3 usd=0.0037 tokens(read,write,in,out)=[20971, 12881, 8, 3842] model=claude-haiku-5-5 -->
# Heroes (card expansion)

{"event": {"name": "Heroes (TCG Set 4 card expansion)", "aliases": ["TCG Set 4", "TCG Set 4: HEROES", "Heroes Booster Pack", "Heroes Booster Bundle (25 Pack)", "Heroes questline", "Heroes (fourth series, per article 2734)"]},
 "kind": "update",
 "live": "yes",
 "occurrences": [
  {"year": 2012, "when": "Launch in 2012; exact day not verified (tentonhammer summary field gives Aug 25 but its body was not retrieved)", "source": "http://www.tentonhammer.com:80/free-realms/news/free%20Relams%20Gets%20a%20New%20Trading%20Card%20Game (summary field only; lookup for the article title returned no match, so unverified)"}
 ],
 "recurring": null,
 "zones": ["Blackspore Swamp (Madam Zelda starts the series there, per article 2734 fact summary)"],
 "npcs": ["Madam Zelda (article 2734; locale:439496 'In her Crystal Ball, Madam Zelda saw four heroes defeat Baron von Darkcheat')", "Baron von Darkcheat (villain; article 2734; locale:439496; wiki page 'Baron von Darkcheat (character)')"],
 "quests": ["Heroes questline (objective text 'Complete the Heroes Questline.', locale:441610; quest title not verified in the pack)"],
 "activities": ["Play Heroes TCG cards, including solo scenarios (article 2742 summary, per prior pack; not re-retrieved here)", "Buy Heroes booster packs and bundles (locale:17470; locale:7973; locale:9403)", "Complete the Heroes questline: keep Baron von Darkcheat's cronies busy while the Realmkeepers train, then the final reckoning with the Baron (article 2734 quest summary)"],
 "items": [
  {"name": "Heroes Booster Pack", "price": "unresolved: 249 station_cash (video:1LjCvhboCkQ/00188.jpg, video:fjZluIfbUIo/00058.jpg) vs 224 (video:9NOkMosko1E/00024.jpg)", "currency": "station_cash", "source": "locale:17470; video:1LjCvhboCkQ/00188.jpg; video:9NOkMosko1E/00024.jpg"},
  {"name": "Heroes Booster Bundle (25 Pack)", "price": null, "currency": null, "source": "locale:7973; locale:9403 ('Save on TCG Set 4: Heroes Booster Bundles!'). Generic Digital Booster Bundle frames are not tied to Heroes."}
 ],
 "rewards": ["Sparky, a ride, earned by completing the Heroes TCG questline (wiki pages 'Sparky' and 'Rides'; not re-verified here)", "Tournament promo cards and new loot cards (article 2742 summary, per prior pack)"],
 "evidence": [
  {"claim": "Heroes is the newest Free Realms TCG expansion ('ist da!').", "source": "http://www.freerealms.com/article/detail.action?articleId=2744 (German; relative date only)"},
  {"claim": "Heroes is the fourth series; Madam Zelda starts it in Blackspore Swamp after Baron von Darkcheat is defeated; players keep the Baron busy while four Heroes called the Realmkeepers train, ending in a final reckoning.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2734 (quest and fact summaries)"},
  {"claim": "Client: 'TCG Set 4: HEROES Available Now!' (availability only, no date).", "source": "locale:17472"},
  {"claim": "Client names Heroes Booster Pack and Heroes Booster Bundle (25 Pack).", "source": "locale:17470; locale:7973"},
  {"claim": "Client objective 'Complete the Heroes Questline.'", "source": "locale:441610"},
  {"claim": "Client text ties Madam Zelda and Baron von Darkcheat to four heroes training.", "source": "locale:439496"},
  {"claim": "Heroes booster bundles were sold in a store promotion ('Save on TCG Set 4: Heroes Booster Bundles!'); no date given.", "source": "locale:9403"},
  {"claim": "Article 2733 summary: announces the Heroes expansion; names the four Realmkeeper kids as Bryce, Nathan, Kade, Jessica; lists new TCG mechanics.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2733 (summary only)"}
 ],
 "confidence": 0.5,
 "open": [
  "Launch date: only the tentonhammer summary field gives Aug 25, 2012; its body and date were not retrieved, and lookup for its title found nothing. Treat as '2012, day unverified'. Article 2744 gives only a relative date.",
  "End date and any window: no source. Single release, no recurrence stated.",
  "Quest title: 'A True Hero' came from the earlier answer but no source in the pack gives it. Left out of quests; only the objective text is sourced.",
  "Price conflict: 249 (three captures) vs 224 (one capture). Unresolved; could be a sale or a different date. Bundle price unknown.",
  "Realmkeeper naming conflict, not resolved: article 2733 summary says Bryce, Nathan, Kade, Jessica; article 2744 says Geisterschatten, Magotron, Wildkralle, Adlersehne; the wiki says Crackshot, Magetech, Ghostshadow, Wildclaw. Do not treat as the same four. locale:440112 is a flagged dev note and is excluded.",
  "Articles 2738, 2736, 2746 and 2732 were not retrieved; not cited. Article 2736 is an undated pre-launch teaser, not a live occurrence.",
  "Zones: only Blackspore Swamp is tied to the series (article 2734 summary). No other zone is sourced.",
  "Seasonal bundles containing Heroes packs (locale:9922, Pumpkin Prince; a Snow Days bundle unverified) are separate events. 'Black Friday' bundle sale (locale:9403) has no year, not counted as an occurrence.",
  "Excluded generic strings: locale:391785, 391790, 392044, 392159, 392209 (Wild Card Showdown), 384002 (stat label), 4419490-4419502 (achievement), 441612 (duplicate of 441610, flagged).",
  "Kind 'update' is the nearest enum fit for a card-set release; a TCG or card-set category may be wanted instead.",
  "Sirdo (card 4R5) was in the earlier answer as a Heroes reward; the link is only a 'Trading Card Game Series 4' appearance, so it is dropped."
 ]
}
