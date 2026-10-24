<!-- fleet job=item-infer id=iarcher-s-power-shard-of-regeneration-ii-v2 status=done turns=4 usd=0.0043 tokens(read,write,in,out)=[35813, 20347, 10, 2873] model=claude-haiku-5-5 -->
# Archer's Power Shard of Regeneration II

{"item": {"name": "Archer's Power Shard of Regeneration II", "locale_id": 130958, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Sold to all players as a Coin Shop Power Shard (Level 4 Archer, Power 2); standard price for everyone (inferred mapping of the coins field)", "where": "Coin Shop", "price": "806 coins", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Archer's_Power_Shard_of_Regeneration_II (rev 32635; categories 'Coin Shop', 'Coin Power Shards'; coins field [806, 725]). The price text was stripped in the pack, so the 806 = everyone reading is inferred from the 10% member wording (806 x 0.9 = 725.4)."},
  {"type": "coin_shop", "detail": "Members price of the same Coin Shop item (10% member discount)", "where": "Coin Shop", "price": "725 coins (Members)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Archer's_Power_Shard_of_Regeneration_II (page text: 'Members at the 10% discount price'; coins field 725). Inferred mapping; live shop not checked."},
  {"type": "prize_wheel", "detail": "Archer prize wheel of the Feisty Floren! battle (battle reward wheel, not a shop sale; wheel cost and odds unknown)", "where": "Feisty Floren! battle (Pixie Woods / Northern Wilds per conflicting sources)", "price": null, "currency": null, "source": "repo:quest-lines/enemies.json:13509 (cites wiki 'Feisty Floren!' battle page, Archer Prize Wheel section, listing 'Archer's Power Shard of Regeneration II' among Archer prize wheel items); see also enemies.json:13828 listing 'Archer Power Shard of Regeneration II' in a multi-job wheel reward. The wheel list itself is flagged in enemies.json:13613/13632 as only partly verified."}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Item name and client text ID 130958", "source": "locale:130958"},
  {"claim": "Wiki page says the shard is acquired from the Coin Shop, sold to everyone and to Members at a 10% discount; Coin Shop and Marketplace Items categories", "source": "https://freerealms.fandom.com/wiki/Archer's_Power_Shard_of_Regeneration_II"},
  {"claim": "Coin values 806 and 725 on the wiki coins field; 725 is about 90% of 806, so 806 read as everyone and 725 as Members", "source": "https://freerealms.fandom.com/wiki/Archer's_Power_Shard_of_Regeneration_II (coins field)"},
  {"claim": "Tooltip: Level 4 Archer, Power 2, increases health regen by 40; Resell Value shows 80 with no currency stated", "source": "https://freerealms.fandom.com/wiki/Archer's_Power_Shard_of_Regeneration_II (item_tooltip image)"},
  {"claim": "Archer prize wheel at the Feisty Floren! battle lists this shard", "source": "repo:quest-lines/enemies.json:13509 (wiki Feisty Floren! battle page, Archer Prize Wheel section)"},
  {"claim": "Tiered series: Regeneration I, III, IV, V also exist as client items; Regeneration III appears on the same wiki Coin Shop lists", "source": "locale:130957, locale:130959, locale:130960, locale:130961; repo:freerealms-wiki/wikitext/10448-49839-8c2fe6de054d.wiki:21"}
 ],
 "confidence": 0.6,
 "open": [
  "Wiki price text was stripped in the pack; 806 = everyone and 725 = Members is inferred from the coins field and the 10% wording, not read from the page text. Not checked against the live shop.",
  "Coin Shop sale is evidenced by wiki category and page text only; no date range for when it was sold or whether the price changed over time.",
  "Feisty Floren! prize wheel: the list at enemies.json:13509 is attributed to the wiki battle page but enemies.json:13613 and :13632 flag the wheel list as only partly verified and possibly copied from Petty Yetis!. The wheel's coin cost, spin odds and the battle's location (Pixie Nursery vs Northern Wilds vs south-west of Wugachug) are unresolved. enemies.json:13828 uses a generic 'Archer Power Shard of Regeneration II' wording in another wheel list; that is not confirmed as the same item.",
  "Resell Value of 80 has no currency; not used as a price.",
  "No Station Cash, Marketplace listing, quest reward, enemy drop, crafting, or collection source is evidenced; station_cash is empty in the wiki record even though the page carries a Marketplace Items category.",
  "Retired status unknown: no removal date in the pack. Live status is unsure."
 ]}
