<!-- fleet job=citem-infer id=cthe-wilds-stamp-1471-v1 status=done turns=9 usd=0.0064 tokens(read,write,in,out)=[111590, 22515, 20, 4889] model=claude-haiku-5-5 -->
# The Wilds Stamp

{"item": {"name": "The Wilds Stamp", "locale_id": 1471, "kind": "collection"},
 "sources": [
  {"type": "other", "detail": "Cascading collection entry of the Postman Stamps collection (spawn type 'Job Material', quality Rare). The wiki gives no exact acquisition method for the stamp itself; the Postman Stamps collection's reward is Rudolfo's Speedy Kicks. Stamp Fever: South Wilds quests (locale 442011, 442012) may be involved, but no quest data in the repo confirms it.", "where": "The Wilds (Southern Wilds)", "price": null, "currency": null, "source": "wiki: Job Specific (Collections) > Postman Stamps; freerealms-wiki/wikitext/2190-27853-ba6c0a72b278.wiki lines 501-519 (rev 27853, 2013-07-13); repo:prototype/osfr-tools/data/content/collections.json:4538-4596 (entry 'Wilds Stamp', collection wiki:2:62)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "The Wilds Stamp is item name locale 1471 (client definition 3323, description 'This item can be added to a collection.', no coin store price, no models).", "source": "client definition in task pack; locale:1471"},
  {"claim": "The same stamp is also a client item 'Wilds Stamp' at locale 40962, linked as entry 1 of collection 95 (Postman Stamps, name_id 7746) with item_definition_id 3746.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:7513-7530; locale:40962"},
  {"claim": "Postman Stamps is a cascading Rare Job Material collection listing Wilds Stamp, Briarwood, Chugawug, Penguin, Free Realms, Robgoblin, Ayani and Snowhill Stamps; reward is Rudolfo's Speedy Kicks; Penguin Stamp is the reward for completing Postman Postcards.", "source": "freerealms-wiki/wikitext/2190-27853-ba6c0a72b278.wiki lines 501-519; wiki page 'Job Specific (Collections)'"},
  {"claim": "Postman Stamps is a Postman job collection; the Postman job is unlocked via Felipe in Sanctuary.", "source": "wiki: Postman (freerealms-wiki/wikitext/2105-48036-db0daf5727b3.wiki lines 20-21, 70)"},
  {"claim": "Articles describe the Stamps collection set as including a stamp from the Wilds and one with a Robgoblin on it, which ties the set to the Wilds stamp.", "source": "http://www.freerealms.com:80/collections.vm"},
  {"claim": "Client text for 'Stamp Fever: South Wilds II' and 'III' exists, suggesting a Southern Wilds stamp quest chain, but no quest data links it to the stamp.", "source": "locale:442011, locale:442012"}
 ],
 "confidence": 0.5,
 "open": [
  "Exact acquisition for the Wilds Stamp is not documented: the wiki only says Job Material spawn. Need the Postman job material spawn or Stamp Fever quest reward data to confirm whether it drops, is a quest reward, or is picked up.",
  "Two definitions exist: the pack's definition 3323 (locale 1471, 'The Wilds Stamp', place type) and the collection catalogue's item definition 3746 (locale 40962, 'Wilds Stamp'). Whether they are the same item or a duplicate is unconfirmed; sources were attributed to the collection name only.",
  "No coin vendor stock, coin store price, or wiki price was found for the stamp.",
  "Live status is inferred from the 2013 wiki collection listing and the client text; no retirement evidence was found either way."
 ]}
