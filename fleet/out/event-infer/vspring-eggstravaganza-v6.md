<!-- fleet job=event-infer id=vspring-eggstravaganza-v6 status=done turns=2 usd=0.0038 tokens(read,write,in,out)=[8075, 13134, 6, 4064] model=claude-haiku-5-5 -->
# Spring Eggstravaganza

```json
{"event": {"name": "Spring Eggstravaganza", "aliases": ["Spring Eggstravaganza 2013", "Eggstravaganza (wiki: 'Spring Eggstravaganza 2013' in Bunny Goggles page)"]},
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2013, "when": "Event window March 28 - May 2, 2013 per the 'What's New?' slider. Daily egg-hunt days March 28-31. Spring Eggstravaganza Day (egg opening) March 31 per wiki image caption. Quest dates: The Eggcellent Egg Hunt March 29; The Eggcitingly Eggcellent Egg Hunt March 30; Basket quest March 31.", "source": "wiki image:ui_panel Slidereaster.png (from March 28 - May 2); locale:5100000, locale:5100569 (every day from the 28th through the 31st); wiki Spring Eggstravaganza (image caption 'Opening the eggs on March 31st'); wiki Jack the Rabbit (March 29th, 2013); wiki Bunny Goggles (March 30th, 2013); wiki Spring Eggstravaganza Basket (March 31st, 2013)"}
 ],
 "recurring": null,
 "zones": ["Sacred Grove", "Sanctuary (Pixiewood Hills)"],
 "npcs": ["Alyssa Eggelyn"],
 "quests": ["The Spring Eggstravaganza", "The Eggcellent Egg Hunt", "The Eggcitingly Eggcellent Egg Hunt", "The Eggxtremely Eggcitingly Eggcellent Egg Hunt"],
 "activities": ["Find the hidden egg in Sacred Grove each day from the 28th through the 31st and color it in (locale:5100000, locale:5100569)", "Crack open the collected eggs on Spring Eggstravaganza Day (locale:5100569)", "Return Alyssa Eggelyn's stolen eggs from robgoblins, which she then gives as special eggs to open on Spring Eggstravaganza day (locale:5100089, 5100091, 5100093)", "Throw a Spring Eggstravaganza Basket (Egg Toss) (locale:5100057)"],
 "items": [
  {"name": "Big Bunny Suit", "price": null, "currency": "reward", "source": "wiki Spring Eggstravaganza ('only one possible reward' from the Big Egg: Big Bunny Suit). Conflicts with wiki Big Bunny Suit page, which says it comes from completing all four daily quests; see open."},
  {"name": "Jack the Rabbit", "price": null, "currency": "reward", "source": "wiki Jack the Rabbit (pet pal, Eggcellent Egg Hunt completion prize during Spring Eggstravaganza)"},
  {"name": "Bunny Goggles", "price": null, "currency": "reward", "source": "wiki Bunny Goggles (Eggcitingly Eggcellent Egg Hunt completion prize, Spring Eggstravaganza 2013)"},
  {"name": "Spring Eggstravaganza Basket", "price": null, "currency": "reward", "source": "wiki Spring Eggstravaganza Basket (Eggxtremely Eggcitingly Eggcellent Egg Hunt completion; Freestyle Jobs non-combat weapon); locale:5100051 names the item"}
 ],
 "rewards": ["Big Bunny Suit (from Big Egg, per wiki Spring Eggstravaganza)", "Jack the Rabbit (pet pal)", "Bunny Goggles", "Spring Eggstravaganza Basket"],
 "evidence": [
  {"claim": "Event ran March 28 - May 2, 2013 per the 'What's New?' slider text 'The Spring Eggstravaganza is Here... from March 28 - May 2'. The slider gives no year.", "source": "wiki image:ui_panel Slidereaster.png"},
  {"claim": "Daily egg hunt in Sacred Grove every day from the 28th through the 31st; eggs cracked open on Spring Eggstravaganza Day.", "source": "locale:5100000; locale:5100569"},
  {"claim": "Wiki describes the event as held every day from March 28th to March 31st.", "source": "wiki Spring Eggstravaganza; wiki Events"},
  {"claim": "Egg-opening on March 31 per wiki image caption; the client says only 'Spring Eggstravaganza Day'.", "source": "wiki Spring Eggstravaganza (image 'Opening the eggs on March 31st'); locale:5100569"},
  {"claim": "Year 2013 comes from wiki dated pages (Jack the Rabbit, Bunny Goggles, Basket), not from the slider or the client.", "source": "wiki Jack the Rabbit; wiki Bunny Goggles; wiki Spring Eggstravaganza Basket"},
  {"claim": "Alyssa Eggelyn is the event NPC, found in Sanctuary (Pixiewood Hills).", "source": "wiki Alyssa Eggelyn; wiki Quest:The Spring Eggstravaganza"},
  {"claim": "Quest titles: The Spring Eggstravaganza (locale:5100005), The Eggcellent Egg Hunt and The Eggcitingly Eggcellent Egg Hunt are named in the wiki Quest pages.", "source": "locale:5100005; wiki Quest:The Eggcellent Egg Hunt; wiki Quest:The Eggcitingly Eggcellent Egg Hunt"},
  {"claim": "The Eggxtremely Eggcitingly Eggcellent Egg Hunt is named by the wiki Basket page and the wiki quest page. Client locale 5100013 is FLAGGED as a duplicate and is not used as evidence.", "source": "wiki Spring Eggstravaganza Basket; wiki Quest:The Eggxtremely Eggcitingly Eggcellent Egg Hunt"},
  {"claim": "Official News post 'Wiki Wednesday: Spring Eggstravaganza' calls the event recently held. It gives no absolute date and is not a date source.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2902"},
  {"claim": "Quest chain order: Spring Eggstravaganza, then Eggcellent, then Eggcitingly, then Eggxtremely (each requires the previous).", "source": "wiki Quest:The Eggcellent Egg Hunt; wiki Quest:The Eggcitingly Eggcellent Egg Hunt; wiki Quest:The Eggxtremely Eggcitingly Eggcellent Egg Hunt"}
 ],
 "confidence": 0.7,
 "open": [
  "Live status is 'yes' for the 2013 run only (wiki and client text). The article pack gives no absolute date; article 2902 is undated and its capture date is not used.",
  "Recurrence unknown: only 2013 is evidenced. Wiki event text says 'every year a group of robgoblins...' as lore, which is not a dated occurrence. Recurring left null until other years are checked.",
  "Big Bunny Suit source conflict: wiki Spring Eggstravaganza says the Big Egg's only possible reward is the Big Bunny Suit; wiki Big Bunny Suit page says completing all four of Alyssa's daily quests. The Big Egg path is cited here; the all-four-quests claim is unresolved. A user blog (ns500 'free realms ~ easter') also names the Bunny Suit as the grand egg prize.",
  "The March 28 start is from the locale's '28th through the 31st' sequence and the wiki's 'March 28th to March 31st' text; no dated article confirms it. The May 2 end is from the slider only.",
  "The Eggxtremely quest title rests on wiki pages only; client locale 5100013 is FLAGGED as a duplicate of 5100012 and may be one quest rather than two.",
  "Egg-opening date (March 31) rests on one wiki image caption.",
  "Locales 5100082-5100085 ('Egg Hunt Day 1-4') are unresolved; their text does not name Spring Eggstravaganza. Not included.",
  "Handful of Jelly Beans x20 is on the wiki page list but its reward status is unconfirmed; excluded from rewards and items.",
  "Pre-event quest offers: locales 5100007 and 5100090 say the event is 'around the corner'; no dated source, so no pre-launch offer is claimed.",
  "Prices are null for all items: no price data in the pack, and the items are reward-only per wiki.",
  "Item-to-quest links for Jack, Bunny Goggles and Basket are wiki-sourced and not checked against client reward data.",
  "Pack may merge the Egg Hunt chain with another event under one name; not verified. The Easter blog suggests the egg hunt was tied to an Easter theme; not verified as a separate event."
 ]}
```
