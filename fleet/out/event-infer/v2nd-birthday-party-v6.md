<!-- fleet job=event-infer id=v2nd-birthday-party-v6 status=done turns=1 usd=0.0024 tokens(read,write,in,out)=[0, 6805, 4, 3039] model=claude-haiku-5-5 -->
# 2nd Birthday Party

```json
{
 "event": {
  "name": "2nd Birthday Party (Free Realms 2nd anniversary, 2011)",
  "aliases": ["2nd Birthday Party For Free Realms", "2nd anniversary celebration"]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {
   "year": 2011,
   "when": "Party ran from about April 21-22, 2011 (start inferred, not stated) until May 18, 2011. The game's 2nd birthday was April 28.",
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=2106"
  }
 ],
 "recurring": null,
 "zones": ["Sanctuary"],
 "npcs": ["Camellia", "Cakenstein", "Cakeling"],
 "quests": [],
 "activities": [
  "Speak to Camellia in Sanctuary to start the party quest hub (article 2106 summary only)",
  "Battle Cakenstein, a cake creature, and his cakeling helpers (article 2106 summary; client objective text locale:4732)",
  "Visit party areas (article 2106 summary only; areas not named in the pack)",
  "Buy party items in the Marketplace (cakes, crates and pets, per article 2106 summary; no item names in the pack)"
 ],
 "items": [],
 "rewards": ["Birthday rewards (article 2106 summary only; unnamed in the pack)"],
 "evidence": [
  {
   "claim": "Free Realms' 2nd birthday party ran until May 18, 2011; the game turned 2 on April 28. Sourced from the article summary and one quote; the full article text was not checked.",
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=2106"
  },
  {
   "claim": "Start is not stated. The post is dated 2011-04-21 in the pack, but that date is inferred from 'Posted 1 week, 1 day ago' with a capture date of 2011-04-30, which gives about April 22. Treat the start as about April 21-22, 2011.",
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=2106"
  },
  {
   "claim": "The party covered party areas, a Speak-to-Camellia hub in Sanctuary, a Cakenstein battle, birthday rewards, and Marketplace cakes, crates and pets (summary wording only).",
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=2106 (article summary)"
  },
  {
   "claim": "The cakeling objective text is 'The cakelings are eating all of the birthday cake they stole! Defeat them all...' (locale:4732). locale:6215 is only the bare NPC name 'Cakeling' and is not used as objective text.",
   "source": "locale:4732 ; locale:6215"
  },
  {
   "claim": "The Camellia hub wording is supported only by the 2106 summary. The one client line about Camellia in Sanctuary (locale:707) is undated and describes a Sacred Grove cake competition that matches 2012, so it is not 2011 support.",
   "source": "locale:707 (undated, not used as 2011 support)"
  },
  {
   "claim": "A Stickam anniversary webcast is a separate broadcast, not a party activity. Its date conflicts: article 2098 gives Thursday April 21, 2011 at 20:00 Brasilia time (live on SOE's Stickam channel); article 2094 says a Thursday at 4:00 pm US Pacific before April 28; article 2093 gives Thursday April 2, 2011 at 4:00 pm PT. The pack does not confirm 2098's time or 2094's wording. It is not labelled pre-launch, because no source says the party had not started, and it is not in this event's occurrences or items.",
   "source": "http://www.freerealms.com/article/detail.action?articleId=2098 ; http://www.freerealms.com/article/detail.action?articleId=2094 ; http://www.freerealms.com/article/detail.action?articleId=2093"
  },
  {
   "claim": "Later Birthday Bash runs are separate records: 2012 through May 24, 2012 (article 2580) and the 4th birthday on April 29, 2013 (article 2924). The 2011 title is '2nd Birthday Party' (article 2106).",
   "source": "http://www.freerealms.com/article/detail.action?articleId=2580 ; http://www.freerealms.com:80/article/detail.action?articleId=2924"
  }
 ],
 "confidence": 0.4,
 "open": [
  "Start date is approximate (about April 21-22, 2011). Only the May 18, 2011 end is sourced, and only from the article 2106 summary and quote. The full article text was not checked.",
  "Live status is 'yes' because article 2106, captured 2011-04-30, describes the party as running until May 18. No dated 2011 source confirms the activities as they ran.",
  "The Stickam webcast dates conflict across 2093 (April 2), 2094 and 2098 (April 21). Unresolved. Not merged into this event.",
  "Items: none are tied to 2011 by a dated source. Birthday Cake Hat is 2012 (article 2580). Birthday Bash Furniture Bundle (locale:692), Birthday Invitation (locale:4951), wall sconce, party crate, balloons and T-shirts are undated. Birthday Pinata pet is a 3rd-birthday item. Anniversary gifts cite article 2107, which has no year in the pack. Prices and currency are unknown.",
  "Quests: 'Cakenstein Attacks!' (locale:4917) is client text with no dated 2011 source, so it is not listed. Undated wiki quests A Piece of Cake, Undelivered Confections and Birthday Cake Bake-off are unconfirmed for 2011.",
  "Zones: Sanctuary is sourced to article 2106. Sacred Grove has only 2012 support (locale:707 undated). Happy Valley, Robgoblin Camp and the German party areas (article 2099, undated) are unconfirmed for 2011.",
  "Rewards are unnamed. The Boss Cake tie is unconfirmed.",
  "Whether '2nd Birthday Party' and the later 'Birthday Bash' runs are one recurring event is undecided. recurring is null because only one occurrence is sourced to this record.",
  "The wiki category members and quest answers for this event were empty in the pack, so no wiki or quest source supports the NPCs or quests beyond the client text noted above.",
  "Activities and rewards are summary-level from one 2011 article (2106). A dated 2011 article naming items, quests or NPCs is needed to expand them."
 ]
}
```
