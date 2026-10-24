<!-- fleet job=item-infer id=iwarrior-s-power-shard-of-vitality-iii-v3 status=done turns=4 usd=0.0042 tokens(read,write,in,out)=[28303, 16917, 10, 3637] model=claude-haiku-5-5 -->
# Warrior's Power Shard of Vitality III

{"item": {"name": "Warrior's Power Shard of Vitality III", "locale_id": 131230, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop listing, sold to everyone at 1055 coins; Members pay 949 coins (10% member discount on the same listing, not a second sale)", "where": "Coin Shop", "price": "1055 coins (everyone); 949 coins (Members)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Warrior's_Power_Shard_of_Vitality_III (rev 32660; category 'Coin Shop'; structured coins array [1055, 949]). The rendered price text is blank in the pack, so the amounts are not read from visible text. The sibling Ninja, Brawler, Archer, Medic and Wizard shard pages use the same blank template and the same Coin Shop wording."},
  {"type": "vendor", "detail": "Sonja (female Human Warrior-job merchant, introduced Oct 1 2013), sells Warrior's Power Shard of Vitality III", "where": "Snowhill", "price": null, "currency": null, "source": "wiki page 'Sonja' (Sells list, which names Power Shard of Vitality III; also repo:quest-lines/npcs.json:133324 vendor_sells, citing that wiki page). The sale price is not shown in the pack."},
  {"type": "prize_wheel", "detail": "Warrior Prize Wheel reward table on the level/quest pages 'Return to Sender!', 'Seaside Swoopers' and 'Snatching Snappers!'", "where": "Warrior Prize Wheel (per wiki reward tables)", "price": null, "currency": null, "source": "wiki pages 'Return to Sender!', 'Seaside Swoopers', 'Snatching Snappers!' (lookup excerpts show the Archer Prize Wheel list containing Archer's Power Shard of Vitality III; the Warrior section of those tables is not in my excerpt, so this rests on the prior pack's reading and repo enemies.json 'prize wheel, Warrior (wiki)' row). Spin cost not shown."}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 131230 'Warrior's Power Shard of Vitality III'.", "source": "locale:131230"},
  {"claim": "Wiki page: level 8 Warrior power shard, Power 3, passive increases health by 233 in combat; acquired from the Coin Shop, sells to everyone at the price of [blank] and to Members at the 10% discount price of [blank]; categories include Coin Shop and Coin Power Shards.", "source": "https://freerealms.fandom.com/wiki/Warrior's_Power_Shard_of_Vitality_III"},
  {"claim": "Structured coins array on the page is [1055, 949], matching a 10% member discount.", "source": "https://freerealms.fandom.com/wiki/Warrior's_Power_Shard_of_Vitality_III (coins array, rev 32660)"},
  {"claim": "Wiki page 'Sonja' Sells list includes Power Shard of Vitality III (Warrior gear, Snowhill).", "source": "wiki page Sonja; repo:quest-lines/npcs.json:133324"},
  {"claim": "Warrior Prize Wheel tables on 'Return to Sender!', 'Seaside Swoopers' and 'Snatching Snappers!' list the Vitality III shard family (Archer version seen in excerpts).", "source": "wiki pages Return to Sender!, Seaside Swoopers, Snatching Snappers! (lookup excerpts)"},
  {"claim": "Sibling Archer and Medic Vitality III shards show Resell Value 105 on their tooltips; the Warrior tooltip is not in the pack.", "source": "wiki image:item_tooltip Archerpowervitaliiistats.jpg, Medicpowervitaliiistats.jpg"}
 ],
 "confidence": 0.55,
 "open": [
  "Coin Shop prices 1055 and 949 come from the coins array and the Coin Shop category; the visible price text is blank on this and sibling pages. Treat as likely, not read from text. The 949 figure is the Member price on the same listing, merged into one source (critique: no second sale).",
  "Sonja's sale price and currency are not in the pack, so the vendor source has price null.",
  "Prize Wheel: the Warrior section of the reward tables was not visible in my excerpts; the source rests on the prior pack and repo enemies.json. Spin cost and whether the item is still on the wheel are unconfirmed.",
  "'Marketplace Items' category is unexplained. No Station Cash price or SC Marketplace evidence was found, so no marketplace source is listed.",
  "Warrior tooltip (resell value) is not in the pack; 105 is shown only for Archer and Medic siblings.",
  "No retirement or removal evidence was found. Sonja's listing and the Coin Shop category are not dated, so live is 'unsure' and retired is null.",
  "Kind is 'other' because the schema has no power-shard category."
 ]}
