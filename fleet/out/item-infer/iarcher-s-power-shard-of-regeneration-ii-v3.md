<!-- fleet job=item-infer id=iarcher-s-power-shard-of-regeneration-ii-v3 status=done turns=5 usd=0.0036 tokens(read,write,in,out)=[45181, 14285, 12, 2808] model=claude-haiku-5-5 -->
# Archer's Power Shard of Regeneration II

{"item": {"name": "Archer's Power Shard of Regeneration II", "locale_id": 130958, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Sold to all players as a Coin Shop Power Shard (Level 4 Archer, Power 2, +40 health regen). Standard (non-member) price inferred as 806 coins from the wiki coins field [806, 725]; the wiki price text was stripped in the pack.", "where": "Coin Shop", "price": "806 coins (price unverified; mapping inferred)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Archer's_Power_Shard_of_Regeneration_II (rev 32635; categories 'Coin Shop', 'Coin Power Shards'; coins field [806, 725]; page text 'acquired from the Coin Shop')"},
  {"type": "coin_shop", "detail": "Members price of the same Coin Shop item, stated on the wiki as a 10% member discount", "where": "Coin Shop", "price": "725 coins for Members (inferred; 806 x 0.9 = 725.4; sale price, not the standard price)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Archer's_Power_Shard_of_Regeneration_II (page text: 'Members at the 10% discount price'; coins field 725)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Item name and client text ID 130958", "source": "locale:130958"},
  {"claim": "Wiki page says the shard is acquired from the Coin Shop, sold to everyone and to Members at a 10% discount", "source": "https://freerealms.fandom.com/wiki/Archer's_Power_Shard_of_Regeneration_II"},
  {"claim": "Wiki coins field holds two values, 806 and 725; 725 is about 90% of 806", "source": "https://freerealms.fandom.com/wiki/Archer's_Power_Shard_of_Regeneration_II (coins field)"},
  {"claim": "Tooltip: Level 4 Archer, Power 2, increases health regen by 40; Resell Value 80 with no currency stated (not used as a price)", "source": "https://freerealms.fandom.com/wiki/Archer's_Power_Shard_of_Regeneration_II (item_tooltip image)"},
  {"claim": "Sibling Regeneration shards (I, III, IV, V) exist as client items", "source": "locale:130957, locale:130959, locale:130960, locale:130961"}
 ],
 "confidence": 0.5,
 "open": [
  "Wiki price text is stripped in the pack. Which coin figure is the everyone price and which is Members is inferred from order and the 10% arithmetic. Confirm from the unstripped wiki text or the live Coin Shop before wiring the numbers.",
  "Coin Shop sale is evidenced by wiki category and page text only. No stock row, date range, or price-change history is in the pack.",
  "Archer prize wheel at the Feisty Floren! battle is NOT counted as a source. The only support is repo:prototype/osfr-tools/data/content/dungeons/feisty_floren.json:846 (a wiki-derived guide list, Rewards > Prize wheel by job > Archer). The guide's wheel list is flagged partly verified and possibly copied from Petty Yetis! (the same shard also appears in petty_yetis.json:779 and other dungeon files), the battle's location is unresolved, the wheel's coin cost and odds are unknown, and the item's own wiki page does not list the battle. Treat as an unconfirmed lead until the wheel list is checked against this item's page.",
  "enemies.json:13828 uses a generic 'Archer Power Shard of Regeneration II' wording in a multi-job wheel list; not confirmed as this item.",
  "Resell Value 80 has no currency; not used as a price.",
  "No Station Cash, Marketplace listing, quest reward, enemy drop, crafting, or collection source is evidenced. The 'Marketplace Items' category alone does not prove a Station Cash or marketplace listing.",
  "Retired status unknown: no removal date in the pack. Live status unsure."
 ]}
