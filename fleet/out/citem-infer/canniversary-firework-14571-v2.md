<!-- fleet job=citem-infer id=canniversary-firework-14571-v2 status=done turns=4 usd=0.0044 tokens(read,write,in,out)=[43376, 20771, 10, 2679] model=claude-haiku-5-5 -->
# Anniversary Firework

{"item": {"name": "Anniversary Firework", "locale_id": 14571, "kind": "consumable"},
 "sources": [
  {"type": "quest_reward", "detail": "Cakenstein's Treasure (Active Quest; the step that grants it is not confirmed). Caption reads 'You receive 1 Anniversary Firework' next to 'Cakenstein's Treasure'; NPC Alyssa Eggelyn shown.", "where": "Birthday Bash event zones (stone path landmark; zone not confirmed by the frame)", "price": null, "currency": null, "source": "video:mAyN-7xjr8s/00028.jpg; locale:9049 (Cakenstein's Treasure); quest-lines/schedule-packs.json:10854"},
  {"type": "prize_wheel", "detail": "Possible prize on the 'YOU WIN! Cakenstein Attacks!' minigame results screen, listed under a 'Birthday Gifts' block. Unconfirmed whether guaranteed, random, or a paid prize.", "where": "Birthday Bash minigame (Cakenstein Attacks!)", "price": null, "currency": null, "source": "video:0feIhpgdWOc/00126.jpg (possible reward list, unconfirmed)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name 'Anniversary Firework' with description 'Fire it off to help celebrate the Free Realms Birthday Bash.'", "source": "locale:14571; locale:14576"},
  {"claim": "Fireworks are the tool used against Gâtostein (Cakenstein) and its cakelings during the birthday event. Theme only, not an acquisition source.", "source": "http://www.freerealms.com/article/detail.action?articleId=1293"},
  {"claim": "Video frame shows 'You receive 1 Anniversary Firework' under the Cakenstein's Treasure Active Quest caption", "source": "video:mAyN-7xjr8s/00028.jpg"},
  {"claim": "Anniversary Firework is listed in the Cakenstein Attacks! results screen block 'Birthday Gifts'", "source": "video:0feIhpgdWOc/00126.jpg"},
  {"claim": "No coin store price in the client definition (coin_store_prices empty); no coin vendor sells it; no Station Cash or Coin Shop listing found", "source": "client definition 77436; lookup (no vendor or store hit)"},
  {"claim": "Earlier schedule work in the repo excluded this item from the dated event rewards because no source ties it to a year, and flagged the drop tie as inference only", "source": "quest-lines/schedule-packs.json:10866, 32171; quest-lines/schedules.json:23610"}
 ],
 "confidence": 0.35,
 "open": [
  "Exact quest step that grants Anniversary Firework from Cakenstein's Treasure is not confirmed; only one caption frame ties them together.",
  "Whether the Cakenstein Attacks! minigame grants it as a guaranteed prize, a random prize, or not at all is unconfirmed.",
  "The Birthday Party Crate frame (video:C3fysVLxrMg/00540.jpg) shows the item name next to the crate name but does not show it inside. Not listed as a source. Check the crate's contents before adding it.",
  "The 'Sanctuary / Queensfields' location from the prior answer is not supported by any frame; removed. The zone of the Cakenstein's Treasure quest is unknown.",
  "No coin, Station Cash, Coin Shop or prize-wheel price is sourced. Any price stays null.",
  "The birthday event dates (2010-2012, festivities ending around 10 May 2010) are unverified in this pass; the year of the frames is not shown. Schedule notes conflict on the anniversary day (April 28 vs 29).",
  "Retired status is unknown. The event ended, but no source says this item was removed. Keep retired null until checked.",
  "Wiki has no page for this item; the prior answer's 'Birthday Bash party zones' claim is not verified."
 ]
}
