<!-- fleet job=citem-infer id=cshimmering-sun-triangle-shard-96320-v2 status=done turns=4 usd=0.0029 tokens(read,write,in,out)=[31414, 13350, 10, 1902] model=claude-haiku-5-5 -->
# Shimmering Sun Triangle Shard

{"item": {"name": "Shimmering Sun Triangle Shard", "locale_id": 96320, "kind": "other"},
 "sources": [{"type": "vendor", "detail": "Unnamed coin store, store category 121 (store row only; vendor/NPC not identified; no stock list names it)", "where": null, "price": "866 coins (779 coins for members, 10% discount); sell price 86 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:8081 (item_id 30914)"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Shimmering Sun Triangle Shard', locale 96320, definition 30914, slot 12, class 68, no description, no models.", "source": "locale:96320"},
  {"claim": "Store row for item 30914 in category 121: purchase 866 coins, member 779 coins, sell 86 coins, no_sale false.", "source": "repo:prototype/osfr-tools/data/content/stores.json:8081"},
  {"claim": "Item 30923 (Shimmering Air Triangle Shard) sits in the same category at the same price (stores.json:8083), so category 121 is a shared price tier, not a single-vendor listing.", "source": "repo:prototype/osfr-tools/data/content/stores.json:8083"},
  {"claim": "The Shimmering Air Triangle Shard is the Peep's Missing Bowl quest reward from Uncle Irving at Farnum Farmstead; the video frame shows it. This does not extend to the Sun variant.", "source": "video:3JXpHghLOTs/00014.jpg; notes/Build Guides/Content/Jobs/Adventurer.md:92; repo:prototype/osfr-tools/data/content/quests/adventurer.json:1451"},
  {"claim": "Sibling shard names (locale 96315-96321) are in the client text table; no wiki page, video, article, or other answer names the Sun variant. Repo search finds no 'Sun Triangle' text.", "source": "locale:96315-96321; repo search"}
 ],
 "confidence": 0.3,
 "open": [
  "Vendor not identified: stores.json gives only a store category and price, with no NPC or stock list. The vendor source is a price fact, not a confirmed NPC sale; wireable is false until a stock list names the vendor.",
  "The 866-coin price tier is shared with the Air shard (a quest reward), so the price alone does not separate a coin vendor from a quest-reward family.",
  "No wiki, video, or article shows the Sun shard being obtained, so whether it is sold, quest/event-only, or retired is unknown.",
  "Job shard tables (Postman, Fisherman, Soccer Star) were checked for the family but do not name the Sun variant; tier and job are unconfirmed.",
  "Client definition has no description and no model files."
 ]}
