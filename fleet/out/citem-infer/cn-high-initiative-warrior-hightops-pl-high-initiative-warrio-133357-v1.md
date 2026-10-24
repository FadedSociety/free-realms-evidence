<!-- fleet job=citem-infer id=cn-high-initiative-warrior-hightops-pl-high-initiative-warrio-133357-v1 status=done turns=5 usd=0.0024 tokens(read,write,in,out)=[23971, 8454, 12, 2128] model=claude-haiku-5-5 -->
# {n}High Initiative Warrior Hightops{pl="High Initiative Warrior Hightops"}

{"item": {"name": "High Initiative Warrior Hightops", "locale_id": 133357, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Hannibal (male human merchant, sells Warrior job items)", "where": "Mire's Edge, Blackspore Swamp", "price": "752 coins (member price 676 coins, 10% member discount)", "currency": "coins", "source": "wiki page 'Hannibal' (lists High Initiative Warrior Hightops among items sold); repo:prototype/osfr-tools/data/content/stores.json item 76349 (purchase_price_coins 752, member_price_coins 676, sell_price_coins 75)"}],
 "retired": null, "live": "yes",
 "evidence": [{"claim": "Item name locale 133357 is 'High Initiative Warrior Hightops', slot 5, class 15, model warrior_<race>_<gender>_feet_platedhightops.adr", "source": "locale:133357; client definition definition_ids 76349"},
  {"claim": "Hannibal in Mire's Edge (Blackspore Swamp) sells the High Initiative Warrior Hightops among Warrior job items", "source": "wiki page: Hannibal"},
  {"claim": "Coin store row for item 76349 lists purchase price 752 coins, member price 676, sell price 75; the first-pass 'vendor' guess is consistent", "source": "repo:prototype/osfr-tools/data/content/stores.json item 76349"},
  {"claim": "Same set sold by Hannibal: High Initiative Warrior Pauldrons, Breeches, Helm, Gauntlets, Tunic", "source": "wiki page: Hannibal"},
  {"claim": "Grexan's Camp wiki page links the High Initiative / Threat Range Warrior set to Kanja, Sensei (Warrior trainer area), a possible separate source not confirmed as a sale", "source": "wiki page: Grexan's Camp"}],
 "confidence": 0.8,
 "open": ["Wiki gives no price on the Hannibal page; the 752-coin price comes from the store data row, and the wiki price was not checked, so it is unconfirmed whether it is the live price.", "The 752 coins in the store row is the same number as the pack's coin_store_prices value; the stores.json row for item 76349 is the only store row found.", "Grexan's Camp / Kanja, Sensei listing is unclear: it may be a Warrior trainer reward or a quest reward, not checked.", "No dated retirement information found; retired status is unknown."]}
