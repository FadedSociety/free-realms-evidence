<!-- fleet job=event-infer id=vrealmskeepers-missing-in-sunstone-valley-v9 status=done turns=2 usd=0.0034 tokens(read,write,in,out)=[6228, 10647, 6, 3985] model=claude-haiku-5-5 -->
# Realmskeepers missing in Sunstone Valley

```json
{"event": {"name": "Rumbledome! (Free Realms Trading Card Game Set 5)", "aliases": ["Rumbledome!", "Rumbledome", "Rumbledome TCG Set 5", "TCG Series 5", "Series 5 Rumbledome! Expansion"]},
 "kind": "update",
 "live": "yes",
 "occurrences": [
  {"year": 2013, "when": "launched Thursday, March 21, 2013 (launch date stated in the wiki blog as 'launches on Thursday, March 21st, 2013'; articleId=2877 says 'launched Thursday, March 21, 2013')", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2877; wiki blog 'User blog:Soe amnerys/Rumbledome Officially Opens On March 21st'"}
 ],
 "recurring": null,
 "zones": ["Sunstone Valley", "Blackspore Swamp (Madame Zelda's camp, where the Realmskeepers search starts, per articleId=2877)"],
 "npcs": ["Madame Zelda (sends the player to search for the Realmskeepers, per articleId=2877)"],
 "quests": [],
 "activities": [
  "Collect and open Rumbledome! booster packs (per 'First Look: TCG Set 5 Rumbledome! Loot' blog)",
  "Play Set 5 Trading Card Game cards, including the Plunder mechanic (per the articles.json announcement post captured 2013-03-18 and 'Are You Ready To Plunder?' blog)",
  "Follow the Rumbledome TCG questline in Sunstone Valley, whose story hook is the missing Realmskeepers (articleId=2877; client string 'Complete the Rumbledome TCG Questline.' ties the questline to the set)"
 ],
 "items": [
  {"name": "Rumbledome Lot", "price": null, "currency": "reward", "source": "wiki page 'Rumbledome Lot' (housing lot redeemed from the Series 5 Virtual Reward loot card of the same name)"},
  {"name": "Skullz Choppa", "price": null, "currency": "reward", "source": "'First Look: TCG Set 5 Rumbledome! Loot' blog: the new Rumbledome! questline gives the Skullz Choppa as its reward at conclusion (preview wording)"},
  {"name": "Rumbledome housing lot (mirrors the arena, can be filled with traps)", "price": null, "currency": "reward", "source": "'First Look: TCG Set 5 Rumbledome! Loot' blog (preview wording)"},
  {"name": "Rumbledome skater outfit set (by piece, three colors)", "price": null, "currency": "reward", "source": "'First Look: TCG Set 5 Rumbledome! Loot' blog (preview wording)"},
  {"name": "Rumbledome hats for TCG player lobbies", "price": null, "currency": "reward", "source": "'First Look: TCG Set 5 Rumbledome! Loot' blog (preview wording)"}
 ],
 "rewards": [
  "Rumbledome Lot (Series 5 virtual reward, via booster packs)",
  "Skullz Choppa (questline reward at conclusion, preview wording)",
  "Other Series 5 virtual rewards randomly packed in booster packs: rides, housing, clothing, hats, a pet, building materials (articles.json Set 5 Loot preview summary; not itemised beyond the above)"
 ],
 "evidence": [
  {"claim": "Rumbledome! is the fifth Free Realms Trading Card Game set, set in Sunstone Valley, with new game cards, virtual rewards and a new quest line; it launched Thursday, March 21, 2013.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2877 (summary: 'which launched Thursday, March 21, 2013'); wiki blog 'User blog:Soe amnerys/Rumbledome Officially Opens On March 21st' ('launches on Thursday, March 21st, 2013')"},
  {"claim": "The articleId=2877 post uses past tense ('launched') and is captured about 1 week 19 hours before 2013-03-27, i.e. after the launch date, which supports a live run. Its exact posting date is not shown.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2877"},
  {"claim": "An announcement post captured 2013-03-18 introduced the fifth TCG set Rumbledome! and its Plunder mechanic, before the launch date.", "source": "articles.json announcement post captured 2013-03-18 (URL not restated in this pack; treat as pre-launch context)"},
  {"claim": "The Realmskeepers left for Sunstone Valley to investigate the Skullz and disappeared; after a week without word, Madame Zelda asked the player to search for and rescue them.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2877"},
  {"claim": "Rumbledome Lot is a housing lot obtained by redeeming the Series 5 Virtual Reward loot card.", "source": "wiki page 'Rumbledome Lot'"},
  {"claim": "Set 5 virtual rewards are randomly packed in Rumbledome! booster packs.", "source": "wiki blog 'User blog:Soe amnerys/ First Look: TCG Set 5 Rumbledome Loot'"},
  {"claim": "The client has the string 'Complete the Rumbledome TCG Questline.', tying a questline to the set.", "source": "locale:125173215"}
 ],
 "confidence": 0.6,
 "open": [
  "Live status: the articleId=2877 summary uses past tense for the March 21, 2013 launch and was captured after that date, so live is set to 'yes' at moderate confidence. The blog and the 2013-03-18 announcement are pre-launch. No article states a close date or confirms the set's end, so the run length is unknown.",
  "The 2013-03-21 date is stated in the blog ('launches on Thursday, March 21st, 2013') and in articleId=2877's wording. articleId=2877 itself is undated; its date is inferred from capture timing only.",
  "The pack's title 'Realmskeepers missing in Sunstone Valley' is a story beat of the Set 5 questline (articleId=2877), not a separate event. It is merged here by judgement. Bryce should decide whether to split it.",
  "Quest titles: no source gives an exact title for the Realmskeepers search or the Rumbledome questline. The client string 'Complete the Rumbledome TCG Questline.' is a task description, not a title, so quests is left empty.",
  "Items from the 'First Look' blog (Skullz Choppa, housing lot, skater outfit, hats) and the Set 5 loot preview (rides, pet, clothing, building materials) are preview wording. They describe a plan, not confirmed live contents, and are not verified against a post-launch source. Rumbledome Lot is the only item sourced to a wiki page.",
  "Client strings 'Replica of the Rumbledome's Shock Trap' and 'Flame Trap' are not tied to Set 5 by any source and are left out.",
  "Prices and currencies: no source gives prices, so all are null. Items are typed 'reward' rather than a purchase currency.",
  "Arena content (Rumbledome arena, Goldcrusher, Bronzeknuckles, Silverfist, Rumbledome Duel) predates Set 5 and is not counted as part of this event.",
  "The HEROES prerequisite (articleId=2876) was not confirmed in lookup and is left out.",
  "The 'First Look' blog's story tie-in claim was dropped: the retrieved text only says the rewards are randomly packed in booster packs."
 ]}
```
