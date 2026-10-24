<!-- fleet job=citem-infer id=ckey-to-the-city-67177-v2 status=done turns=2 usd=0.0018 tokens(read,write,in,out)=[5413, 7878, 6, 1433] model=claude-haiku-5-5 -->
# Key to the City

{"item": {"name": "Key to the City", "locale_id": 67177, "kind": "other"},
 "sources": [
  {"type": "quest_reward", "detail": "Snowhill quest 'Key to the City', reward from Mayor Crystalline (reward dialog: 'I'd like to reward you the Key to the City')", "where": "Snowhill", "price": null, "currency": null, "source": "locale:93195; locale:93197; wiki page 'Mayor Crystalline' (lists Quest:[Key] to the City)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Item name is 'Key to the City', locale 67177; item definition 23564; no coin store price in client data.", "source": "locale:67177; prototype/osfr-tools/data/content/collection_catalogue.json:15813"},
  {"claim": "The Snowhill quest reward dialog says the Mayor rewards the Key to the City, and the objective says the mayor will reward it.", "source": "locale:93195; locale:93197"},
  {"claim": "Wiki 'Mayor Crystalline' (Snowhill mayor, in front of town hall) lists 'Quest:[Key] to the City' among her quests.", "source": "wiki page 'Mayor Crystalline'"},
  {"claim": "Wiki 'Explorer Chests' says the key opens the Ayani chest and is 'the only key not obtainable through collection', so the Sacred Keys collection entry (collection 195, entry 2) is set membership only, not an acquisition path.", "source": "wiki page 'Explorer Chests'; prototype/osfr-tools/data/content/collection_catalogue.json:15789-15815"},
  {"claim": "Client text locale 141066 ('Brawler: Curious Key') describes a key to the city of Snowhill returned to the Mayor; this is a different quest and does not establish the reward path.", "source": "locale:141066; locale:141067"}
 ],
 "confidence": 0.6,
 "open": [
  "Quest body for 'Key to the City' not retrieved; the exact giver chain (Mayor Crystalline vs Tevin/Murphy) is unresolved in notes/Build Guides/Content/NPCs/NPCs - Snowhill.md lines 175 and 221.",
  "The collection entry is not counted as a source: the wiki says this key is the only one not obtainable through collection. The collection catalogue lists it only as set membership.",
  "The 'Key locations' File page wiki text lists the sacred keys as a group with no separate price; it does not confirm the quest source, so it is not cited as evidence.",
  "No coin store price, no vendor stock, no marketplace or drop evidence found.",
  "Retired/availability status not established by any source; live status is unsure."
 ],
 "critique_response": "Evidence critique: removed the collection source (contradicted by wiki Explorer Chests); kept the quest reward with locale and wiki citations; dropped the unverified Key locations citation; retired left null and live set to unsure."}
