<!-- fleet job=citem-infer id=cn-knockdown-brawler-shoulderpads-pl-knockdown-brawler-should-132920-v2 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[6160, 7454, 6, 1714] model=claude-haiku-5-5 -->
# {n}Knockdown Brawler Shoulderpads{pl="Knockdown Brawler Shoulderpads"}

{"item": {"name": "Knockdown Brawler Shoulderpads", "locale_id": 132920, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store listing, definitions 75912 (tint group 2) and 900023 (tint group 1); stores.json category 106. No NPC vendor stock row was checked.", "where": "Coin store (stores.json category 106)", "price": "1500 coins purchase; 1350 coins member price (10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75912 (line 15665) and item 900023 (line 17225)"},
  {"type": "prize_wheel", "detail": "[Brawler] Prize Wheel, dungeon wheel list on the Tanglewood Fort page, listed as '[Knockdown] [Brawler] [Shoulderpads]'. The page shows a 77 Coins figure next to the wheel list; this is the wheel's spin cost as shown, not the item's price. How the wheel is reached (chest, purchase) is not verified.", "where": "Tanglewood Fort (dungeon prize wheel)", "price": null, "currency": null, "source": "wiki page Tanglewood Fort"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name locale 132920 is 'Knockdown Brawler Shoulderpads'", "source": "locale:132920"},
  {"claim": "Coin store entries for 75912 and 900023: purchase 1500 coins, member 1350 (10%), sell 150, no_sale false", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75912; item 900023"},
  {"claim": "Tanglewood Fort Brawler Prize Wheel list includes '[Knockdown] [Brawler] [Shoulderpads]' with a 77 Coins figure on the page", "source": "wiki page Tanglewood Fort"},
  {"claim": "Haunted Mines wheel list has '[Knockdown] [Brawler] Jersey' and a separate 'Power Punch [Brawler] [Shoulderpads]'. The Power Punch entry is not named as this item and is not used as a source here.", "source": "wiki page Haunted Mines"}
 ],
 "confidence": 0.6,
 "open": [
  "Prize wheel: the 77 Coins figure is the wheel's listed cost as shown on the wiki; it is not this item's price, and the wheel's spin mechanics and access are unverified.",
  "Wiki gives no date for the wheel listing, so the wheel source is not confirmed as live; retired is null.",
  "Haunted Mines 'Power Punch [Brawler] [Shoulderpads]' may be a different piece; not counted as a source for this item.",
  "Briarheart Caverns claim from the earlier answer was not found in lookup and is dropped.",
  "No NPC vendor stock row checked; the stores.json category 106 label as a 'coin shop' is taken from the pack and not separately verified.",
  "The tint split between 75912 and 900023 comes only from the stores file.",
  "Preheated/Toaster Chef cluster items are a separate set and were not traced."
 ]}
