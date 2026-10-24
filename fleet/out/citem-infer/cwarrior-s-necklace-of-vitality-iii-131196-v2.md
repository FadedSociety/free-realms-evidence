<!-- fleet job=citem-infer id=cwarrior-s-necklace-of-vitality-iii-131196-v2 status=done turns=7 usd=0.0053 tokens(read,write,in,out)=[85394, 19928, 16, 3912] model=claude-haiku-5-5 -->
# Warrior's Necklace of Vitality III

{"item": {"name": "Warrior's Necklace of Vitality III", "locale_id": 131196, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Sonja, NPC Merchant (Warrior job gear); her wiki Sells list names Warrior's Necklace of Vitality III", "where": "Snowhill", "price": "1055 coins (stores.json reference; member 949; sell-back 105). Not an NPC quote or wiki price for this necklace.", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Sonja (wikitext freerealms-wiki/wikitext/11231-33648-3e7f126b8b78.wiki line 24); repo:prototype/osfr-tools/data/content/stores.json item 75452 (line 17370); repo:prototype/osfr-tools/data/content/vendors.json item 75452 (line 35190)"},
  {"type": "coin_shop", "detail": "Coin Shop sale, inferred from sibling Warrior/Brawler Vitality items with the same 1055/949 price. The Warrior necklace has no page of its own confirming this.", "where": "Coin Shop", "price": "1055 coins (everyone); 949 coins (Members, 10% discount)", "currency": "coins", "source": "Wiki Brawler's Necklace of Vitality III (freerealms-wiki/wikitext/10533-32100-978658e7eafa.wiki line 1); Warrior's Power Shard of Vitality III (freerealms-wiki/wikitext/10515-32660-51ec539edfd0.wiki line 1). Both say Coin Shop at 1055/949."}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name for locale 131196 is \"Warrior's Necklace of Vitality III\", in the Vitality I-V and Energy I-III cluster (131194-131201).", "source": "locale:131196"},
  {"claim": "Sonja is a Snowhill Merchant selling Warrior job items, introduced 1 Oct 2013. Her Sells list includes Warrior's Necklace of Vitality III, so the earlier 'not in wiki text' concern is resolved.", "source": "https://freerealms.fandom.com/wiki/Sonja (freerealms-wiki/wikitext/11231-33648-3e7f126b8b78.wiki lines 14, 24)"},
  {"claim": "Store reference price 1055 / member 949 / sell 105 for item 75452. Category 108 and the source tags are unresolved, so this is a reference price, not confirmed Sonja stock pricing.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75452 (line 17370)"},
  {"claim": "Sibling Warrior Power Shard of Vitality III and Brawler's Necklace of Vitality III wiki pages both state Coin Shop sale at 1055 (everyone) and 949 (Members). The Warrior necklace price matches them, so a Coin Shop channel is likely but not directly documented for this item.", "source": "freerealms-wiki/wikitext/10515-32660-51ec539edfd0.wiki; freerealms-wiki/wikitext/10533-32100-978658e7eafa.wiki"},
  {"claim": "Sell-back value 105 matches the Archer Power Shard of Vitality III wiki resell value.", "source": "freerealms-wiki/harvest/lists/image_text.json (Archer's Power Shard of Vitality III, Resell Value 105)"},
  {"claim": "Field-battle title id 75452 is an unrelated id namespace, so no battle reward is claimed.", "source": "repo:prototype/osfr-tools/data/content/field_battles.json:545"}
 ],
 "confidence": 0.5,
 "open": [
  "Live status is unverified. The Sonja page is a 2013-10 revision and no source confirms current sale. Live is set to 'unsure', not 'yes'.",
  "The Coin Shop channel is inferred from sibling items with the same price. Whether this necklace was also sold through the Coin Shop, or only by Sonja, is not confirmed by any page for it.",
  "Whether the Sonja price is 1055 or a different wiki sale price is unverified. No wiki price for this necklace was retrieved.",
  "stores.json category_id 108 and tags R118/T633 are not decoded, so the store row cannot be tied to Sonja's stock or to the Coin Shop directly.",
  "No drops, quest rewards, prize wheel, or crafting sources were found. None are claimed.",
  "The client definition has empty description and models []. Slot 8 and class 15 were not checked against the Warrior armor set."
 ]}
