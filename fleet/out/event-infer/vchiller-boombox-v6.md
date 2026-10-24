<!-- fleet job=event-infer id=vchiller-boombox-v6 status=done turns=2 usd=0.0028 tokens(read,write,in,out)=[9801, 11297, 6, 2618] model=claude-haiku-5-5 -->
# Chiller Boombox

{
 "event": {"name": "Chiller Boombox (not a standalone event; name ties to Super Spooktacular)", "aliases": ["Chiller Boombox dance party", "Chiller Boombox Quest Pack", "[Chiller] [Boombox]"]},
 "kind": "other",
 "live": "unsure",
 "occurrences": [
  {"year": 2010, "when": "October 2010 (inferred from the 'second annual' Super Spooktacular wording; the article date is null)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1864 (summary: Community Trick or Treat party in Sanctuary during the 2010 Super Spooktacular; Community Team to bring Chiller Boomboxes)"},
  {"year": null, "when": "Undated 'Chiller Boombox dance party', held before the Costume Parade (article 516, Oct 23, 2009)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=516 (quote: 'We've done the Chiller Boombox dance party...')"}
 ],
 "recurring": null,
 "zones": ["Sanctuary", "Pixiewood Hills"],
 "npcs": ["Dani"],
 "quests": ["Challenge Dani in Pixiewood in a TCG game to win her cool Chiller Boombox! (quest text, locale:3686406336)"],
 "activities": ["Community Chiller Boombox dance party (undated)", "Trick or Treat party in Sanctuary with Chiller Boomboxes (2010, article 1864)", "TCG challenge from Dani to win the Chiller Boombox (client text locale:3686406336)"],
 "items": [
  {"name": "Chiller Boombox", "price": null, "currency": "reward", "source": "locale:4027028141 and locale:2477647389 (item names); wiki page Super Spooktacular (TCG reward from Dani, requires the Chiller Boombox Quest Pack)"},
  {"name": "Chiller Boombox Quest Pack", "price": "500", "currency": "station_cash", "source": "locale:1637022464 and locale:2987946831 (name only); price from video:1LjCvhboCkQ/00190.jpg, undated"}
 ],
 "rewards": ["Chiller Boombox (TCG reward from Dani)"],
 "evidence": [
  {"claim": "Chiller Boombox is an item won from Dani's TCG challenge in Pixiewood Hills, tied to Super Spooktacular", "source": "wiki page Super Spooktacular; locale:3686406336"},
  {"claim": "A Chiller Boombox dance party was held before the Costume Parade", "source": "http://www.freerealms.com:80/article/detail.action?articleId=516"},
  {"claim": "Community Team was to bring Chiller Boomboxes to a Sanctuary Trick or Treat party in the 2010 Super Spooktacular", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1864 (date null)"}
 ],
 "confidence": 0.35,
 "open": [
  "MERGE: 'Chiller Boombox' is a name shared by an item (TCG reward, part of Super Spooktacular), an undated community dance party (article 516 mentions it only in passing), and the 2010 Trick or Treat party (article 1864). The pack does not show a standalone Chiller Boombox event. Recommend wiring it as an item of Super Spooktacular, not as its own calendar entry.",
  "Article 516 (Costume Parade, Oct 23, 2009) is a separate community event and is not part of Chiller Boombox. The dance party has no date in any source.",
  "No dated source for the dance party. The 2010 year for article 1864 rests on the date-null summary and 'second annual' wording.",
  "The 500 Station Cash price belongs to the Quest Pack, from an undated video frame. The Boombox reward itself has no price.",
  "Wiki 'Boomboxes' list tags [Chiller] [Boombox] as a Card Duelist Reward, which conflicts with the Dani TCG reward. Resolve before wiring.",
  "Article 1854 is not cited: its summary does not name the Chiller Boombox as a reward.",
  "No wiki category members and no quest answers were found for this name. Live status is unverified for any dated occurrence."
 ]
}
