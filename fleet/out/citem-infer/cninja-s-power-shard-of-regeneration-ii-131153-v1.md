<!-- fleet job=citem-infer id=cninja-s-power-shard-of-regeneration-ii-131153-v1 status=done turns=3 usd=0.0016 tokens(read,write,in,out)=[8326, 5573, 8, 1607] model=claude-haiku-5-5 -->
# Ninja's Power Shard of Regeneration II

{"item": {"name": "Ninja's Power Shard of Regeneration II", "locale_id": 131153, "kind": "other"},
 "sources": [{"type": "coin_shop", "detail": "Coin Shop sale, sold to all players (Ninja power shard, level 4, Power 2)", "where": "Coin Shop", "price": "806 coins (standard); 725 coins for Members (10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75409 (purchase_price_coins 806, member_discount_percent 10, member_price_coins 725); wiki page \"Ninja's Power Shard of Regeneration II\" (Coin Shop, Category:Coin Shop)"}],
 "retired": null, "live": "unsure",
 "evidence": [{"claim": "Item is a level 4 Ninja power shard granting +40 health regen, requires Ninja level 4", "source": "wiki page \"Ninja's Power Shard of Regeneration II\""},
  {"claim": "Client defines the item as locale:131153 with definition 75409, slot 12, class 2, and a coin store price of 806", "source": "locale:131153; repo:prototype/osfr-tools/data/content/stores.json item 75409"},
  {"claim": "Store data lists a 10% member discount, member price 725 coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75409"},
  {"claim": "Sibling Medic/Archer/Brawler power shards of regeneration exist with the same I-V naming pattern, so this is one tier of a series sold as a set", "source": "lookup client locale:130957-131024; wiki image:icon entries"},
  {"claim": "Wiki page also carries Category:Marketplace Items, which may refer to the Station Cash Marketplace; no price in Station Cash was found", "source": "wiki page \"Ninja's Power Shard of Regeneration II\""}],
 "confidence": 0.7,
 "open": ["Wiki page's price text is blank in the cached copy; the 806 / 725 coin prices come from our store data, not the wiki text.", "Category:Marketplace Items is ambiguous: no Station Cash price was found, so no marketplace source is listed.", "No retirement or later-availability source was found; retired is left null and live is 'unsure' despite the first-pass 'yes' guess.", "Wiki page is a stub; no drop, quest, or crafting source found for this tier.", "Lookup for the exact item name failed on the apostrophe (FTS5 syntax error), so the client-side search used the shared 'Power Shard of Regeneration' phrase instead."]}
