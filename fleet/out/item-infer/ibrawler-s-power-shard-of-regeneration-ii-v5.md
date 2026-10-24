<!-- fleet job=item-infer id=ibrawler-s-power-shard-of-regeneration-ii-v5 status=done turns=3 usd=0.0018 tokens(read,write,in,out)=[12266, 6796, 8, 1722] model=claude-haiku-5-5 -->
# Brawler's Power Shard of Regeneration II

{"item": {"name": "Brawler's Power Shard of Regeneration II", "locale_id": 131023, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Fraz (pixie Brawler job merchant); Sells section lists Brawler's Power Shard of Regeneration II", "where": "Wugachug", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Fraz (text: 'can be found in Wugachug'; 'sells exclusively Brawler Job items'; Sells list includes the shard)"},
  {"type": "coin_shop", "detail": "Coin Shop listing; wiki says acquired from the Coin Shop, sold to everyone, Members get a 10% discount", "where": "Coin Shop", "price": "806 coins (everyone) / 725 coins (Members) per wiki coins field; UNVERIFIED reference values, wiki price text is blank", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Brawler's_Power_Shard_of_Regeneration_II (categories: Coin Shop, Coin Power Shards, Marketplace Items; text 'acquired from the Coin Shop')"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name is client locale text 131023.", "source": "locale:131023"},
  {"claim": "Level 4 Brawler shard; passive increases health regen by 40; acquired from the Coin Shop; Members get 10% discount.", "source": "https://freerealms.fandom.com/wiki/Brawler's_Power_Shard_of_Regeneration_II"},
  {"claim": "Fraz is a pixie NPC merchant found in Wugachug who sells exclusively Brawler Job items; the Sells list includes Brawler's Power Shard of Regeneration II.", "source": "https://freerealms.fandom.com/wiki/Fraz"},
  {"claim": "Repo maps the Fraz stock listing to item_id 75279 / name_id 131023; its 806/725 purchase and member prices and 403 sell price come from stores.json reference data, not a captured NPC quote.", "source": "repo:prototype/osfr-tools/data/content/vendors.json:45946-45982; repo:prototype/osfr-tools/data/content/stores.json:15224"}
 ],
 "confidence": 0.6,
 "open": [
  "Coin Shop prices 806 (everyone) and 725 (Members, 10% off 806) are unverified: wiki price text is blank and the same numbers appear in repo stores.json as reference values. Confirm against client Coin Shop data before wiring prices.",
  "Fraz vendor price not captured; price unknown. Do not use the repo 806/403 values as Fraz prices.",
  "stores.json source_tags (L1, L2, L4, R1, R2, R3) are unexplained in the pack; not used as sources.",
  "repo vendors_unresolved.json:10258 (75279) is unconfirmed and not used.",
  "Danger Peaks Brawler prize wheel lead has no item ID or wiki/client confirmation; not used.",
  "No retirement notice found; live status unverified."
 ]}
