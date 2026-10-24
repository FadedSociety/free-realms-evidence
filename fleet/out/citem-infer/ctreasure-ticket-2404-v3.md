<!-- fleet job=citem-infer id=ctreasure-ticket-2404-v3 status=no_submit turns=3 usd=0.0029 tokens(read,write,in,out)=[17204, 11683, 8, 2629] model=claude-haiku-5-5 -->
# Treasure Ticket

```json
{"item": {"name": "Treasure Ticket", "locale_id": 2404, "kind": "other"},
 "sources": [
  {"type": "other", "detail": "Minigame goal and score rewards (cooking, tile-matching, tower-upgrade, mining and similar goals) that award one or more Treasure Tickets on completion, alongside coins, stars or accessories", "where": "Minigames (cooking, tile-matching, tower-upgrade, mining goals); exact zone not stated in the evidence", "price": null, "currency": null, "source": "locale:77871; locale:78617; locale:102457; locale:102629; locale:92897; locale:102455; video:3xJCVp5gGF4/00078.jpg; video:w-9vtebjou4/00100.jpg"},
  {"type": "event", "detail": "'Four million players' celebration, July 2-8, 2009: Treasure Ticket rewards were doubled", "where": null, "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=134 (per the articles fact 'receiving Treasure Tickets was doubled'; not re-read in this pass)"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Client item 2404 'Treasure Ticket'; description locale 2408 'This ticket is awarded for doing good work in the Sacred Realms!'; locale 2407 'Use these tickets at the Royal Vault.'; no coin store price and no models in the client definition", "source": "locale:2404; locale:2407; locale:2408"},
  {"claim": "Tickets were the entry currency for the Royal Vault chest game: 'It costs 60 Treasure Tickets to play.'", "source": "locale:116418; locale:116737; locale:14993817; locale:140956 ('Come back when you have 60 Treasure Tickets!')"},
  {"claim": "Minigame goal texts promise a treasure ticket on completion", "source": "locale:77871 ('Complete this goal and you'll earn a treasure ticket!'); locale:78617 ('Obtain this score and you'll earn a treasure ticket!'); locale:102457 ('Upgrade these towers and you'll earn a treasure ticket...'); locale:102629 ('Complete this objective and a treasure ticket!'); locale:92897 ('Complete this goal and you'll earn a treasure ticket and maybe an accessory!')"},
  {"claim": "Jan 26, 2010 patch ended treasure ticket rewards; remaining tickets were redeemable via Gulsh in Sanctuary", "source": "http://www.freerealms.com:80/article/detail.action?articleId=892"},
  {"claim": "Treasure Isle trade: the Royal family paid 10 coins per ticket traded in (a redemption sink, not an acquisition source)", "source": "locale:426840 ('Royal family say I give 10 coins for every ticket you got'); locale:426851; locale:426843"},
  {"claim": "Wiki: tickets were 'no longer acquirable in the game' shortly after the Royal Vault closed; page is in Category:Unobtainable; Cannot Trade; tooltip Resell Value 10 (a vendor sell value, not a store price)", "source": "wiki page 'Treasure Ticket'; image:item_tooltip 'Treasure ticket.jpg'"},
  {"claim": "Royal Vault closed; vault items moved to the Coin Shop. This is a client notice, so it supports the closure but not live availability.", "source": "locale:116706 ('Dis is Royal Vault, but vault closed... you can get vault stuff from Coin Shop now!')"}
 ],
 "confidence": 0.7,
 "open": [
  "No vendor sells Treasure Tickets (vendor_stock empty) and no coin store price exists in the client definition or stores data, so no price is given. The wiki 'Resell Value: 10' is a sell-to-vendor value, not a store price.",
  "The Daily Wheel prize (article fact: 'prizes include potions, treasure tickets, karts and pets') is undated and names no event. It is left out of sources and needs a dated source before wiring.",
  "Locale 92897 is tagged quest_reward in the client, but its text is minigame goal copy. It is cited only as minigame goal wording, not as a quest.",
  "The 'Sanctuary / Sacred Grove era' location is not evidenced by any cited line, so the minigame 'where' is left general.",
  "The exact end date is 01/25/2010 per the wiki file page, while the patch notes are dated January 26, 2010. The sources differ by one day.",
  "The July 2009 double-ticket event was taken from the pack's articles fact and not re-read here. Confirm articleId 134 before wiring.",
  "Earlier citations locale:557467341, locale:602382834 and locale:1333236145 do not exist and have been removed. locale:116706 is flagged not_live, so it is used only for the closure note.",
  "The Seaside Sticker chest UI frame concerns a different item and is not evidence for this one."
 ]}
```
