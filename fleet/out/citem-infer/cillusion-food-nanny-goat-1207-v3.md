<!-- fleet job=citem-infer id=cillusion-food-nanny-goat-1207-v3 status=nothing_found turns=2 usd=0.0024 tokens(read,write,in,out)=[5457, 11442, 6, 1827] model=claude-haiku-5-5 -->
# Illusion Food - Nanny Goat

{"item": {"name": "Illusion Food - Nanny Goat", "locale_id": 1207, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 4048 is named 'Illusion Food - Nanny Goat' (NameId 1207), with description 'Eating this food will temporarily change the player into a Nanny Goat.' The client definition has an empty coin_store_prices list, so no coin vendor sale is recorded for it.", "source": "client definition in pack (definition_ids [4048], coin_store_prices []); locale:1207"},
  {"claim": "Belongs to a family of Illusion Food transformation items (233-257, 1162-1169, 1198-1228, including 1208 Snow Hog, 1209 Wart Hog, 1213 Robgoblin Female Mage).", "source": "locale lookup 'illusion food' (locale:233-1228)"},
  {"claim": "Locale 118981 is an npc_name 'Nanny Goat'. A transformation target NPC with this name exists in the client, so the food's name matches a transform form rather than a shop item.", "source": "lookup client locale:118981"},
  {"claim": "Locale 3116 'Nanny Goat' is a separate item-typed string whose description is the same transformation text. It is not item 4048 and should not be merged with it without checking the item id.", "source": "lookup client locale:3116"},
  {"claim": "Farmer Chug's robgoblin dialog mentions 'some illusion food here that'll transform you into a big scary monster'. It does not name Nanny Goat or item 4048, so it is only a loose candidate giver.", "source": "locale:134991"},
  {"claim": "Robgoblin quest steps about scaring robgoblins off Farmer Chug's pigs use Chug's illusion spell, not a named food.", "source": "locale:41974, locale:41982"},
  {"claim": "No store entry exists for item 4048. stores.json item_id 24048 is a different item (540 coins).", "source": "repo:prototype/osfr-tools/data/content/stores.json:6925"},
  {"claim": "No wiki page, article, video frame, coin vendor, Station Cash listing, drop, event, or prize-wheel entry names this item.", "source": "lookup wiki/articles/video/client; search of repo content JSON for 4048"}
 ],
 "confidence": 0.15,
 "open": [
  "No source confirmed. Farmer Chug's robgoblin dialog (locale:134991) is only a loose candidate giver for illusion food in general. It does not name Nanny Goat or item 4048.",
  "Locale:134992 was dropped because the id check flags it as a duplicate near-repeat of 134991.",
  "Locale:42002 (Chug's Illusion Potion), named as a competitor in the previous answer, was not found in locale search, so it is unverified and not used.",
  "The previous answer's client flags (NoSale, NoTrade) and cost 180 came from a Sanctuary repo file that was not re-verified. Cost 180 is a server value, not a coin price, and is not used as a price.",
  "Quest title and reward step for the robgoblin arc remain unconfirmed. 'Scaring Robgoblins' (locale:74488) is unverified.",
  "Whether item 4048 was ever obtainable, or retired, is unknown. Do not mark wireable until a giver or quest step is confirmed.",
  "No vendor, Station Cash, drop, event, prize-wheel, or crafting source was found."
 ]}
