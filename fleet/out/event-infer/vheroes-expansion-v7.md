<!-- fleet job=event-infer id=vheroes-expansion-v7 status=done turns=3 usd=0.0025 tokens(read,write,in,out)=[15604, 8874, 8, 2385] model=claude-haiku-5-5 -->
# Heroes expansion

{
 "event": {"name": "Heroes expansion (Free Realms Trading Card Game Set 4: Heroes)", "aliases": ["Heroes", "TCG Set 4: HEROES", "Heroes Booster Pack", "Series 4 Heroes Expansion"]},
 "kind": "update",
 "live": "unsure",
 "occurrences": [],
 "recurring": null,
 "zones": [],
 "npcs": ["Baron von Darkcheat (villain, named in article 2733 and locale:17471)"],
 "quests": ["A True Hero"],
 "activities": ["Open Heroes booster packs", "Complete the Heroes Questline"],
 "items": [
  {"name": "Heroes Booster Pack", "price": null, "currency": null, "source": "locale:17471 (10 random TCG cards plus one loot card per pack); locale:17472 ('TCG Set 4: HEROES Available Now!'). Store price frames conflict (249 vs 224 station_cash) and are undated and unverified, so price is null."},
  {"name": "Heroes Booster Bundle (25 Pack)", "price": null, "currency": null, "source": "locale:9403 (store line 'Save on TCG Set 4: Heroes Booster Bundles!'); name only, no price or date in the pack."}
 ],
 "rewards": ["Heroes TCG cards", "One loot card per Heroes booster pack (locale:17471)"],
 "evidence": [
  {"claim": "Heroes is the fourth set of the Free Realms Trading Card Game and introduces the Realmkeepers; each pack has 10 random cards plus one loot card.", "source": "locale:17471"},
  {"claim": "'TCG Set 4: HEROES Available Now!' is a store/announcement line naming the set.", "source": "locale:17472"},
  {"claim": "Heroes, the newest expansion for the Free Realms Trading Card Game, was released (English SOE news post; no absolute date in the pack).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2733"},
  {"claim": "The Heroes expansion had arrived when the Spanish SOE post was written; it is the TCG's fourth set (no absolute date; relative date only).", "source": "http://www.freerealms.com/article/detail.action?articleId=2738"},
  {"claim": "French SOE post: Heroes (Héros) has arrived, with Baron von Darkcheat, Madam Zelda and four child Guardians (no absolute date).", "source": "http://www.freerealms.com/article/detail.action?articleId=2742"},
  {"claim": "Heroes booster packs were sold inside the Pumpkin Prince seasonal bundle (two Darkcheat packs, two Heroes packs), so Heroes packs were on sale by the October 2012 seasonal update.", "source": "locale:9922; wiki Template:News/Archive ('Update of October 4, 2012') - the wiki entry is not yet re-read in this pass"},
  {"claim": "Quest title 'A True Hero' with objective 'Complete the Heroes Questline.'", "source": "locale:441609 (title); locale:441610 (objective). locale:441612 is duplicate-flagged and not cited."}
 ],
 "confidence": 0.4,
 "open": [
  "Launch date unknown. Articles 2733, 2738, 2742 say the set has arrived or was released but give no absolute date in the pack. The wiki Sirdo date (Aug 23, 2012) was not fetched and is not used as evidence; the earlier 2012-08-25 date is dropped.",
  "End date and current availability unknown, so live is 'unsure'.",
  "Kid names conflict: article 2733 lists Kade; article 2737 lists Onofre. Not used as a fact.",
  "Possible merge: Baron von Darkcheat questline and '[Heroes] Journal' entries (wiki Chugzy, Necronomicus) are not yet tied to this set; locale:9922 bundles Darkcheat and Heroes packs together. Kept as separate candidates.",
  "Heroes Booster Pack price conflicts across store frames (video:1LjCvhboCkQ/00190.jpg, video:9NOkMosko1E/00024.jpg) and those video refs were not verified here.",
  "Quest 'A True Hero' is tied to Heroes by locale:441610 only; the quest answer set was not cross-checked.",
  "Article 2737 and 2734 are summaries only in the pack; 2734 is not used as a Heroes fact.",
  "Kind 'update' (card-set release); 'other' is also defensible."
 ],
 "critique_fixes": "Dropped unverified citations to articles 2738/2733 as launch-date sources (kept only for 'released/arrived' text, with no date), removed the '(TCG)' qualifier from the activity, and cited locale:17472 and 9403 for the set name. Launch date left open."
}
