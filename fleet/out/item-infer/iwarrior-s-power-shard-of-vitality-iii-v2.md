<!-- fleet job=item-infer id=iwarrior-s-power-shard-of-vitality-iii-v2 status=done turns=4 usd=0.0036 tokens(read,write,in,out)=[30183, 14602, 10, 2919] model=claude-haiku-5-5 -->
# Warrior's Power Shard of Vitality III

{"item": {"name": "Warrior's Power Shard of Vitality III", "locale_id": 131230, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop, sold to everyone at 1055 coins; Members pay 949 coins (10% member discount, same listing)", "where": "Coin Shop", "price": "1055 coins (everyone); 949 coins (Members)", "currency": "coins", "source": "wiki page https://freerealms.fandom.com/wiki/Warrior's_Power_Shard_of_Vitality_III (rev 32660; category 'Coin Shop'; structured coins array [1055, 949]). Caveat: the visible price text on this page is blank in the pack, so the amounts rest on the coins array and the category, not on readable text."},
  {"type": "prize_wheel", "detail": "Warrior Prize Wheel (a reward table on several wiki level/quest pages, e.g. 'Return to Sender!', 'Seaside Swoopers', 'Snatching Snappers!')", "where": "Warrior Prize Wheel (per wiki page reward tables)", "price": null, "currency": null, "source": "wiki pages 'Return to Sender!', 'Seaside Swoopers', 'Snatching Snappers!' (wiki search: '[Warrior] [Prize] [Wheel]' lists \"[Warrior]'s [Power] [Shard] of [Vitality] III\"). Prize-wheel cost per spin not clearly shown on these excerpts."}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item is a level 8 Warrior power shard, Power 3, passive: increases health by 233 in combat.", "source": "https://freerealms.fandom.com/wiki/Warrior's_Power_Shard_of_Vitality_III"},
  {"claim": "Client name for the item is locale 131230 'Warrior's Power Shard of Vitality III'; sibling class versions are locale 130970 (Archer), 131035 (Brawler), 131100 (Medic), 131165 (Ninja), 131295 (Wizard).", "source": "locale:131230"},
  {"claim": "Wiki page lists the Coin Shop as the source, with categories Coin Shop and Coin Power Shards; coins array [1055, 949].", "source": "https://freerealms.fandom.com/wiki/Warrior's_Power_Shard_of_Vitality_III"},
  {"claim": "The shard appears in the Warrior Prize Wheel reward table on wiki pages 'Return to Sender!', 'Seaside Swoopers' and 'Snatching Snappers!'.", "source": "wiki pages Return to Sender!, Seaside Swoopers, Snatching Snappers! (lookup: Warrior Prize Wheel)"},
  {"claim": "Sibling Archer and Medic Vitality III shards show Resell Value 105 on their wiki item tooltips; the Warrior tooltip was not in the pack.", "source": "wiki image:item_tooltip Archerpowervitaliiistats.jpg, Medicpowervitaliiistats.jpg"}
 ],
 "confidence": 0.6,
 "open": [
  "Coin Shop prices 1055 and 949 are not visible in the wiki text (amounts blank); they come from the coins array plus the Coin Shop category. Treat as likely, not directly read. The 949 Member price is one listing's member discount, not a second source.",
  "Prize Wheel source is supported by wiki reward tables, but the wheel cost per spin and whether the item is still on the wheel are not confirmed.",
  "'Marketplace Items' category is unexplained: no Station Cash price or SC Marketplace evidence was found, so no marketplace source is listed.",
  "Repo vendor data: Sonja (Warrior gear merchant, Snowhill) sells a Warrior Power Shard, but the tier is not named in the notes, so it is not counted. Dempsy (Snowhill) sells a Brawler's Power Shard of Vitality III, not this item.",
  "Resell value for the Warrior version is not in the pack (105 is shown for the Archer and Medic versions only).",
  "No live or retirement date evidence was found; live is 'unsure' and retired is null.",
  "Kind is 'other' because the schema has no power-shard category."
 ]}
