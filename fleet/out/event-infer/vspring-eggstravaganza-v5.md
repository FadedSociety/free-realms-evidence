<!-- fleet job=event-infer id=vspring-eggstravaganza-v5 status=done turns=2 usd=0.0029 tokens(read,write,in,out)=[8513, 9906, 6, 3150] model=claude-haiku-5-5 -->
# Spring Eggstravaganza

{"event": {"name": "Spring Eggstravaganza", "aliases": ["Spring Eggstravaganza 2013"]},
"kind": "holiday",
"live": "yes",
"occurrences": [{"year": 2013, "when": "Event window March 28 - May 2, 2013 (What's New slider). Daily egg-hunt days March 28-31 (28th-31st per locale; the wiki dates only 29, 30, 31). Egg-opening day March 31 (wiki image caption).", "source": "wiki image:ui_panel Slidereaster.png (\"What's New?\" panel: from March 28 - May 2); locale:5100000; locale:5100569; wiki Jack the Rabbit (March 29th, 2013); wiki Bunny Goggles (March 30th, 2013); wiki Spring Eggstravaganza Basket (March 31st, 2013); wiki Spring Eggstravaganza (image caption 'Opening the eggs on March 31st')"}],
"recurring": null,
"zones": ["Sacred Grove", "Sanctuary (Pixiewood Hills)"],
"npcs": ["Alyssa Eggelyn"],
"quests": ["The Spring Eggstravaganza", "The Eggcellent Egg Hunt", "The Eggcitingly Eggcellent Egg Hunt", "The Eggxtremely Eggcitingly Eggcellent Egg Hunt (wiki-named; client locale 5100013 is FLAGGED as a duplicate variant of The Eggcellent Egg Hunt, so it may be one quest, not two)"],
"activities": ["Find the hidden egg in Sacred Grove each day from the 28th through the 31st and color it in", "Crack open the collected eggs on Spring Eggstravaganza Day", "Complete Alyssa Eggelyn's daily egg quests (all four completes the Big Bunny Suit reward)"],
"items": [
 {"name": "Big Bunny Suit", "price": null, "currency": "reward", "source": "wiki Big Bunny Suit (completing all four of Alyssa's daily quests during the event)"},
 {"name": "Jack the Rabbit", "price": null, "currency": "reward", "source": "wiki Jack the Rabbit (pet pal; Eggcellent Egg Hunt completion prize during Spring Eggstravaganza)"},
 {"name": "Bunny Goggles", "price": null, "currency": "reward", "source": "wiki Bunny Goggles (Eggcitingly Eggcellent Egg Hunt completion prize, 2013 event)"},
 {"name": "Spring Eggstravaganza Basket", "price": null, "currency": "reward", "source": "wiki Spring Eggstravaganza Basket (Eggxtremely Eggcitingly Eggcellent Egg Hunt completion); locale:5100051 names the item"}
],
"rewards": ["Big Bunny Suit", "Jack the Rabbit", "Bunny Goggles", "Spring Eggstravaganza Basket"],
"evidence": [
 {"claim": "Event window March 28 - May 2, 2013 per the 'What's New?' slider: 'The Spring Eggstravaganza is Here... Help Alyssa Eggelyn! Find Her Missing Colored Eggs! from March 28 - May 2'. The slider gives no year; the year 2013 comes from the wiki dates.", "source": "wiki image:ui_panel Slidereaster.png; wiki Jack the Rabbit (March 29th, 2013)"},
 {"claim": "Daily egg hunt in Sacred Grove on the 28th through the 31st; eggs cracked open on Spring Eggstravaganza Day. The client gives no month.", "source": "locale:5100000; locale:5100569"},
 {"claim": "March 28 is not directly dated by the wiki; it comes from the locale's '28th through the 31st' sequence. Only March 29, 30 and 31 are dated by wiki pages.", "source": "locale:5100569 (inference); wiki Jack the Rabbit; wiki Bunny Goggles; wiki Spring Eggstravaganza Basket"},
 {"claim": "Egg-opening day is March 31, 2013 per a single wiki image caption; the client text says only 'Spring Eggstravaganza Day'.", "source": "wiki Spring Eggstravaganza (image caption 'Opening the eggs on March 31st'); locale:5100569"},
 {"claim": "Wiki names the 2013 run 'Spring Eggstravaganza 2013', the same event.", "source": "wiki Bunny Goggles"},
 {"claim": "Official News post 'Wiki Wednesday: Spring Eggstravaganza' calls it a recently held event; it gives no absolute date and is not used as a date source.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2902"},
 {"claim": "Alyssa Eggelyn is the event NPC in Sanctuary (Pixiewood Hills).", "source": "wiki Alyssa Eggelyn; wiki Quest:The Spring Eggstravaganza"},
 {"claim": "Quest titles in client: The Spring Eggstravaganza (locale:5100005), The Eggcellent Egg Hunt (locale:5100012), The Eggcitingly Eggcellent Egg Hunt (locale:5100014).", "source": "locale:5100005; locale:5100012; locale:5100014"},
 {"claim": "The Eggxtremely Eggcitingly Eggcellent Egg Hunt is named by the wiki Basket page. Client locale 5100013 has the same text but is FLAGGED as a duplicate alternate title, so it is not used as live evidence.", "source": "wiki Spring Eggstravaganza Basket; locale:5100013 (FLAG)"},
 {"claim": "Handful of Jelly Beans x20 appears on the wiki Spring Eggstravaganza page list; reward wording is unconfirmed, so it is not listed as a reward.", "source": "wiki Spring Eggstravaganza; locale:5100048"},
 {"claim": "Only one live occurrence (2013) is evidenced, so recurrence is unknown.", "source": "locale:5100569; wiki Bunny Goggles"}
],
"confidence": 0.7,
"open": [
 "Recurrence unknown: only 2013 is evidenced. Check other years before calling it yearly; recurring is left null.",
 "Locales 5100082-5100085 ('Egg Hunt Day 1-4') sit in the same quest_title group but their text does not name Spring Eggstravaganza. Left unresolved; they may belong to this event or another one.",
 "Per-quest live status for the Eggcitingly and Eggxtremely quests rests only on wiki dates (March 30 and 31, 2013); no article confirms it.",
 "Quest start: client dialogs (5100007, 5100090, 5100091) say the event is 'around the corner', so pre-event quest offers may exist. No dated source, so no pre-launch offer is claimed.",
 "The 28th is inferred from the 28th-31st sequence; the wiki dates only 29-31.",
 "Egg-opening date (March 31) rests on a single wiki image caption.",
 "Article 2902 gives no absolute date; its capture date is not used.",
 "Prices are null for all items; the pack has no price data and the items are reward-only per wiki.",
 "Handful of Jelly Beans x20 is unconfirmed as a reward; its currency and reward status need the wiki reward block.",
 "The pack may merge the Egg Hunt chain with another event under one name; not verified."
]}
