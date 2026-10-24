<!-- fleet job=item-infer id=ialyssa-eggelyn-v2 status=nothing_found turns=2 usd=0.0020 tokens(read,write,in,out)=[5163, 7523, 6, 1959] model=claude-haiku-5-5 -->
# Alyssa Eggelyn

{"item": {"name": "Alyssa Eggelyn", "locale_id": 5100004, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Alyssa Eggelyn is a pixie NPC and quest giver, not an item. The wiki infobox lists gender, race, hair and eye color, and location, with no price, sale, or item fields.", "source": "https://freerealms.fandom.com/wiki/Alyssa_Eggelyn (rev 50097)"},
  {"claim": "The client name entry is an npc_name string tagged to Sacred Grove.", "source": "locale:5100004"},
  {"claim": "The wiki calls her a pixie NPC found in Sanctuary 'around late March for Spring Eggstravaganza'. She is listed in the wiki's Quest Givers category and is linked to four quests. The page does not say which of those quests she gives.", "source": "https://freerealms.fandom.com/wiki/Alyssa_Eggelyn (rev 50097), Categories: Quest Givers"},
  {"claim": "Location conflict: the infobox and wiki page put her in Sanctuary. The Egg Hunt quest pages say to speak with her 'located in Pixiewood Hills in Sanctuary'. The client locale tags her to Sacred Grove.", "source": "page:ns112 Quest:The Spring Eggstravaganza, Quest:The Eggcellent Egg Hunt, Quest:The Eggcitingly Eggcellent Egg Hunt, Quest:The Eggxtremely Eggcitingly Eggcellent Egg Hunt (Notes); locale:5100004"},
  {"claim": "Date conflict: the in-game 'What's New?' panel says 'from March 28 - May 2'. The wiki Spring Eggstravaganza event page says the event was held 'everyday from the 28th of March to the 31st of March' (past tense). The client dialog locale:5100000 also says 'every day from the 28th through the 31st'. The window is not resolved.", "source": "image:ui_panel Slidereaster.png; page:ns0 Spring Eggstravaganza; page:ns0 Events; locale:5100000"},
  {"claim": "The quests tied to her (The Spring Eggstravaganza and the three Egg Hunt quests) are stated as 'only available during the time of Spring Eggstravaganza'. Her eggs and the quest rewards are the only item-type rewards she could be linked to, and the pack does not name any reward items.", "source": "page:ns112 Quest:The Spring Eggstravaganza, Notes; locale:5100089, locale:5100091, locale:5100093 (special egg rewards, not named)"}
 ],
 "confidence": 0.9,
 "open": [
  "Wrong subject for an item job: the pack describes an NPC, so no item sources, prices, or currency exist. Nothing was sourced as a purchasable or obtainable item.",
  "If Bryce meant an item, such as the special eggs given by Alyssa's quests (locale:5100089, 5100091, 5100093) or the Egg Hunt rewards, send that item's pack. Those rewards are not named in this pack, so they cannot be sourced here.",
  "Event dates conflict: the poster says March 28 - May 2, while the wiki event page and in-game dialog say March 28-31. Unresolved.",
  "Location conflicts: Sanctuary (wiki infobox), Pixiewood Hills in Sanctuary (quest pages), and Sacred Grove (client locale). Unresolved.",
  "The wiki does not say which quests she gives, so the quest-giver claim rests only on the Quest Givers category and the linked quests.",
  "No evidence shows whether the event is live on the rebuild, so live is marked unsure."
 ],
 "critic_fixes_applied": [
  "Dropped the word 'only' from the appearance claim.",
  "Removed the unsupported claim that she gives each quest; cited the category and linked quests instead.",
  "Reported both date sources as a conflict instead of choosing the poster's date.",
  "Added the Pixiewood Hills location from the quest pages and the Sacred Grove locale tag."
 ]
}
