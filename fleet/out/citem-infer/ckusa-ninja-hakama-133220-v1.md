<!-- fleet job=citem-infer id=ckusa-ninja-hakama-133220-v1 status=done turns=3 usd=0.0027 tokens(read,write,in,out)=[8692, 8480, 8, 3172] model=claude-haiku-5-5 -->
# Kusa Ninja Hakama

{"item": {"name": "Kusa Ninja Hakama", "locale_id": 133220, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store vendor sale (exact NPC not identified; store category_id 104 in our store data)", "where": "Coin store (repo store category 104)", "price": "375 coins (member price 337 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 76212 (line 15903: purchase_price_coins 375, member_price_coins 337, sell_price_coins 37)"},
  {"type": "prize_wheel", "detail": "[Ninja] Prize Wheel reward table (Battle Item Mystery Pack / Ninja gear tier), listed on several wiki mission pages, e.g. Tavern Cellar, Snakes in a Maze!, Cursed Graveyard!, Hewey's Escape, King of the Ring!", "where": "Prize Wheel (Ninja class wheel), after completing the listed missions", "price": null, "currency": null, "source": "wiki pages: Tavern Cellar; Snakes in a Maze!; Cursed Graveyard!; Hewey's Escape; King of the Ring! (wiki text reads '[Kusa] [Ninja] [Hakama]' in the [Ninja] Prize Wheel list; the number before 'Coins' on those pages is the mission reward, not this item's price)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name locale 133220 is 'Kusa Ninja Hakama'; definition id 76212, slot 4 (legs), class 2, model ninja_<race>_<gender>_legs_skinny.adr", "source": "locale:133220"},
  {"claim": "Coin store sells item 76212 at 375 coins, member price 337, sell 37, in store category 104", "source": "repo:prototype/osfr-tools/data/content/stores.json item 76212"},
  {"claim": "Kusa Ninja Hakama appears in the [Ninja] Prize Wheel list (with Battle Item Mystery Pack, Kusa Ninja Armwraps, Ninja training sword and power shards) on wiki mission pages", "source": "wiki: Tavern Cellar; Snakes in a Maze!; Cursed Graveyard!; Hewey's Escape; King of the Ring!"},
  {"claim": "Kusa Ninja Hakama is shown in a video inventory frame alongside other Student/Ninja pants", "source": "video:98uNKkDRvQU/00266.jpg"},
  {"claim": "Sibling Kusa Ninja set pieces (Armwraps) are on the same [Ninja] Prize Wheel lists, so the set shares this source", "source": "wiki: Cursed Graveyard!; Hewey's Escape; Frostfang Snarlers!"}
 ],
 "confidence": 0.6,
 "open": [
  "Which NPC vendor stocks coin store category 104 is not confirmed; the coin price is evidence of a coin store sale, but the exact vendor/storefront name was not found.",
  "Prize Wheel listing is seen only as a wiki table fragment; the wheel's spin cost and drop odds for this item are unknown.",
  "No wiki page or article gives an explicit obtainability date; the store row carries live source tags (L1, L2, L4, R2, T633, R1) but no retirement record, so retired is left null.",
  "Prize-wheel price figures ('19 Coins', '49 Coins', '2 Coins', '8 Coins') on those wiki pages were not tied to this item and are not used as its price.",
  "Jev's first-pass 'vendor' guess is only partly supported: the coin price supports a coin-store sale; the prize wheel source is a separate, additional source."
 ]}
