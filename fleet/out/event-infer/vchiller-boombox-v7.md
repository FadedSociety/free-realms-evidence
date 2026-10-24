<!-- fleet job=event-infer id=vchiller-boombox-v7 status=done turns=4 usd=0.0045 tokens(read,write,in,out)=[34610, 14915, 10, 4672] model=claude-haiku-5-5 -->
# Chiller Boombox

```json
{
 "event": {
  "name": "Chiller Boombox (item and TCG reward of Super Spooktacular, not a standalone event)",
  "aliases": ["Chiller Boombox Quest Pack (the purchase that unlocks the reward quest)", "[Chiller] [Boombox]", "Chiller Boombox dance party (undated, article 516)"]
 },
 "kind": "other",
 "live": "yes",
 "occurrences": [
  {"year": 2009, "when": "October 14 through November 11, 2009 (Super Spooktacular, the parent event; Quest Pack reward available in that run)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=476 (summary: 'First Annual Super Spooktacular, running October 14 through November 11 (2009)'; fact: 'Super Spooktacular is scheduled to run October 14 through November 11, and is free to all registered players')"},
  {"year": 2010, "when": "October 2010, inferred from 'second annual' wording (date null on the article). Article 1845 gives Ghostly Pet Party Thu Oct 7 / Fri Oct 8, 2010 on server 1, two slots, with no US/UK mapping.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1864 (Trick or Treat party with Chiller Boomboxes, date null); http://www.freerealms.com:80/article/detail.action?articleId=1845 (October 2010 Super Spooktacular dates)"},
  {"year": 2011, "when": "October 13 to November 23, 2011 (Super Spooktacular 'Spooktacular Returns' post; the Quest Pack Marketplace quest is described here)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2304 (summary: post announces the return of the event 'running October 13 to November 23, 2011'; the verbatim wording is not confirmed)"}
 ],
 "recurring": "Yearly in October for the parent Super Spooktacular (2009 and 2011 dated; 2010 inferred from 'second annual'). No source says the Boombox reward itself recurs on a schedule.",
 "zones": ["Pixiewood Hills", "Sanctuary"],
 "npcs": ["Dani (TCG challenger in Pixiewood Hills; offers the Chiller Boombox)", "Rose (Deck of Buzzing, Super Spooktacular; same event, not the Boombox)"],
 "quests": ["Challenge Dani in Pixiewood in a TCG game to win her cool Chiller Boombox! (quest objective 'Pixiewood Chiller Boombox Quest Pack', locale:115)", "Chiller Boombox Quest Pack (purchase item, locale:114)"],
 "activities": [
  "Buy the TCG Quest Pack from the Marketplace, then challenge Dani in Pixiewood Hills to a TCG game to win the Chiller Boombox (articleId=2304; locale:115)",
  "Buying a TCG Quest Pack unlocks one of two special Halloween TCG quests: Jack-O-Lantern Outfit or Chiller Boombox (articleId=1854, articleId=476)",
  "Community Trick or Treat party in Sanctuary, Community Team to bring Chiller Boomboxes, 2010 (articleId=1864, date inferred)",
  "Undated community 'Chiller Boombox dance party' mentioned in passing in the Costume Parade post (articleId=516; no date, not an occurrence)"
 ],
 "items": [
  {"name": "Chiller Boombox", "price": null, "currency": "reward", "source": "locale:16636 ('item - Chiller Boombox'); wiki page 'Chiller Boombox' (earned from the TCG Quest Pack in Super Spooktacular); articleId=476 and articleId=1854 (reward of the TCG Halloween quest)"},
  {"name": "Chiller Boombox Quest Pack", "price": "500", "currency": "station_cash", "source": "locale:114 (name only). Price 500 Station Cash comes from video:1LjCvhboCkQ/00190.jpg, undated, and is NOT verified by an article."}
 ],
 "rewards": ["Chiller Boombox (alternate reward of the Dani TCG quest bought with the Quest Pack)", "Jack-O-Lantern Outfit (glow-in-the-dark costume; the alternate reward of the same two-quest pair, articleId=476 and articleId=1854)"],
 "evidence": [
  {"claim": "Chiller Boombox is a reward from one of two special Halloween TCG quests unlocked by buying a TCG Quest Pack; the other reward is the glow-in-the-dark Jack-O-Lantern costume", "source": "http://www.freerealms.com:80/article/detail.action?articleId=476 ; http://www.freerealms.com:80/article/detail.action?articleId=1854 (fact: 'Buying a TCG Quest Pack unlocks one of two special TCG quests...')"},
  {"claim": "Quest text: challenge Dani in Pixiewood in a TCG game to win her Chiller Boombox, bought from the Marketplace", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2304 ; locale:115"},
  {"claim": "Chiller Boombox item name exists in the client", "source": "locale:16636; locale:114"},
  {"claim": "Wiki: Chiller Boombox is earned from the TCG Quest Pack in Super Spooktacular and completing the quest", "source": "wiki page 'Chiller Boombox'; wiki page 'Super Spooktacular' (Creepy Crawly Cards from Dani, requires the Chiller Boombox Quest Pack or the Deadman's Party Pack)"},
  {"claim": "Community Team was to bring Chiller Boomboxes to a Sanctuary Trick or Treat party in the second annual Super Spooktacular", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1864 (date null; year 2010 inferred)"},
  {"claim": "The parent Super Spooktacular ran October 14 to November 11, 2009 and October 13 to November 23, 2011", "source": "http://www.freerealms.com:80/article/detail.action?articleId=476 ; http://www.freerealms.com:80/article/detail.action?articleId=2304"}
 ],
 "confidence": 0.5,
 "open": [
  "MERGE: 'Chiller Boombox' is used for (a) a TCG reward item in Super Spooktacular, (b) an undated community dance party (articleId=516, passing mention only; not an occurrence), and (c) a 2010 Sanctuary Trick or Treat party with Boomboxes (articleId=1864). Only (a) is tied to a dated event. Recommend wiring it as an item of Super Spooktacular, not a standalone calendar entry.",
  "Chiller Boombox 2010 availability is inferred from 'second annual' wording (articleId=1864, date null) and from 1845's October 2010 dates. No article dates the Boombox reward in 2010.",
  "The 2010 US/UK slot mapping for the Ghostly Pet Party (Oct 7 / Oct 8) is not stated in the summary. Dates are given without slot labels.",
  "The 2011 quote for 'October 13 to November 23' is from the summary of articleId=2304 (title 'Spooktacular Returns'), not a verified verbatim quote.",
  "The 500 Station Cash price for the Quest Pack is from an undated video frame only. Verify before wiring. The Boombox reward has no price.",
  "Wiki 'Items' page lists '[Chiller] [Boombox] - Card Duelist Reward', which conflicts with the Quest Pack/Dani reward. Articles 476 and 1854 support the Quest Pack source, so it is preferred here; the wiki conflict is unresolved.",
  "Locale ids in the earlier draft (3686406336, 4027028141, 2477647389, 1637022464, 2987946831) do not exist. Corrected to locale:115, locale:16636 and locale:114.",
  "articleId=1854 does not name the Chiller Boombox in its summary as a reward. The reward claim is supported by articleId=476 and the 1854 fact text, not by the 1854 summary alone. Re-verify 1854's body before citing it alone.",
  "No wiki category members and no quest answers were found for this name. Live status for 2010 and later Boombox availability is unverified."
 ]
}
```
