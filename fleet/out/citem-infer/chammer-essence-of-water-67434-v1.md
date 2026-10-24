<!-- fleet job=citem-infer id=chammer-essence-of-water-67434-v1 status=done turns=4 usd=0.0029 tokens(read,write,in,out)=[18825, 9480, 10, 3011] model=claude-haiku-5-5 -->
# Hammer Essence of Water

{"item": {"name": "Hammer Essence of Water", "locale_id": 67434, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Entry in the Brawler Magical Hammer Essences collection (four essences: Fire, Wind, Water, Earth). The collection's wiki reward is the Magical Essence Crystal Hammer. Collection entries are Brawler job materials.", "where": null, "price": null, "currency": null, "source": "wiki page 'Brawler Magical Hammer Essences' (via 'List of Collections' and 'Job Specific (Collections)'); repo:prototype/osfr-tools/data/content/collections.json (entry 'Brawler Magical Hammer Essences', entries 3023-3046, reward 'Magical Essence Crystal Hammer'); repo:prototype/osfr-tools/data/content/collection_catalogue.json line 17358-17361 (name_id 67434, item_definition_id 23821)"},
  {"type": "quest_reward", "detail": "Wiki says Hammer Essence of Fire is the reward for completing Brawler Hammer Materials. The snippet is cut off before the Wind, Water and Earth lines, so the Water essence's own quest/reward link is not confirmed. Treat as probable, not verified.", "where": null, "price": null, "currency": null, "source": "wiki page 'Job Specific (Collections)' (https://freerealms.fandom.com/wiki/Job_Specific_(Collections)); repo:prototype/osfr-tools/data/content/collections.json line 3024-3028 (cascade_source 'Brawler Hammer Materials' on Fire only)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item 23821 is named 'Hammer Essence of Water' (locale 67434) and its description says it can be added to the Brawler Magical Hammer Essences Collection.", "source": "locale:67434"},
  {"claim": "The wiki lists Hammer Essence of Water as one of four entries of the Brawler Magical Hammer Essences collection; the collection image shows 'Rewards 20'.", "source": "wiki page 'Brawler Magical Hammer Essences'; image:collection 'Brawler Magical Hammer Essences.png'"},
  {"claim": "The wiki's Job Specific (Collections) page says Hammer Essence of Fire is the reward for completing Brawler Hammer Materials.", "source": "wiki page 'Job Specific (Collections)'"},
  {"claim": "The text 'Hammer Essence of Water' appears on screen in one Cracked Claw Caverns video frame, after the Lost Explorer Bones interaction. Its role there is unclear and it is not shown as a drop.", "source": "video:NtXTmB-wPW0/00028"},
  {"claim": "No coin store price, vendor stock, or enemy drop was found for this item.", "source": "repo:data/content/stores.json (no match); repo search for 23821/67434"}
 ],
 "confidence": 0.5,
 "open": [
  "The source for the Water essence specifically is not confirmed. The wiki excerpt for Fire is a quest reward (Brawler Hammer Materials). The Wind/Water/Earth lines were cut off, so it is unknown whether they share the same source.",
  "The Cracked Claw Caverns frame shows the text 'Hammer Essence of Water'. It may be a bonus-spirit reward, but this is not confirmed. Check the spirit bonus rewards in that video.",
  "The collection image shows 'Rewards 20'. It is unclear whether this is the number of items or the reward value. The wiki names 'Magical Essence Crystal Hammer' as the reward. This was not checked further.",
  "Retirement status is not stated in any source. The essence is listed on the 2013-era wiki, so it is probably live but unconfirmed.",
  "No prices: the item has no coin store price and no Station Cash listing was found."
 ]}
