<!-- fleet job=citem-infer id=cmega-hammer-10717-v1 status=done turns=4 usd=0.0038 tokens(read,write,in,out)=[26736, 17008, 10, 2857] model=claude-haiku-5-5 -->
# Mega Hammer

{"item": {"name": "Mega Hammer", "locale_id": 10717, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale of the Mega Hammer tint variants (item ids 4575, 4576, 4577 in the coin-store category 207; the same 3522-coin price also appears on 4756-4758, 6791-6793, 6895-6901, 7140-7142, 7312-7314). Vendor NPC not identified in our data.", "where": null, "price": "3522 coins (member price 3169 coins, 10% member discount; sell-back 352 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:857-859 (item 4575-4577); the store's coin price is the evidence of a coin vendor sale per the pack rules"},
  {"type": "marketplace", "detail": "Coin Flow Mega Hammer and Star Flow Mega Hammer (2009-era Brawler weapon variants, level 1) were sold through the Station Cash Marketplace. The wiki gives no SC price (the Coin Flow text is blank: 'for , but can no longer be acquired').", "where": "SC Marketplace", "price": null, "currency": "station_cash", "source": "wiki: Coin Flow Mega Hammer; wiki: Star Flow Mega Hammer; wiki File:Coin flow mega hammer.png ('2009-era Brawler SC Marketplace weapon')"}
 ],
 "retired": true,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Mega Hammer' is locale 10717, item class, slot 7, model hammer_ar_ag_weapon_mega.adr, 51 definitions across tints", "source": "locale:10717"},
  {"claim": "Coin store price 3522 coins for Mega Hammer tint items 4575-4577 (category 207)", "source": "repo:prototype/osfr-tools/data/content/stores.json:857-859"},
  {"claim": "Coin Flow Mega Hammer and Star Flow Mega Hammer were SC Marketplace items and 'can no longer be acquired'", "source": "wiki: Coin Flow Mega Hammer; wiki: Star Flow Mega Hammer"},
  {"claim": "Coin Flow Mega Hammer and Star Flow Mega Hammer are client-text variants, flagged not_live as unused weapon variants with no quest context", "source": "locale:384380; locale:384390 (FLAG not_live)"},
  {"claim": "Coin Flow variant is the particle source for the Brawler's Flair Shard of Prosperity (Coin Shop, Coin Flair category)", "source": "wiki: Brawler's Flair Shard of Prosperity"}
 ],
 "confidence": 0.45,
 "open": [
  "Conflict: the store data lists the base hammer tints at 3522 coins (coin store), while the wiki describes the Coin Flow and Star Flow variants as Station Cash Marketplace items with no price. The coin price and the SC marketplace listing may refer to different tints or to a later change; not resolved.",
  "The coin-store vendor NPC and zone for item 4575-4577 are not named in vendors.json or any wiki page; the vendor stock check found no entry for this item.",
  "Wiki gives no retirement date; 'can no longer be acquired' is the only retirement statement. Whether the coin-store entries were ever live at 3522 coins is unverified.",
  "The 51 definitions (4575-4586 and others) include tints that are not each confirmed as sold; only the 4575-4577 group and the Coin/Star Flow variants have any source text.",
  "Client definition 'description' is empty; no quest, enemy drop, event or promotion source found for the base Mega Hammer."
 ]}
