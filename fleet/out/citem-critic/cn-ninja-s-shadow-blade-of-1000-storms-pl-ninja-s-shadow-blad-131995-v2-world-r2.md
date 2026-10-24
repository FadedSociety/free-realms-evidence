<!-- fleet job=citem-critic id=cn-ninja-s-shadow-blade-of-1000-storms-pl-ninja-s-shadow-blad-131995-v2-world-r2 status=no_submit turns=3 usd=0.0019 tokens(read,write,in,out)=[11918, 7919, 8, 1671] model=claude-haiku-5-5 -->
# {n}Ninja's Shadow Blade of 1000 Storms{pl="Ninja's Shadow Blade of 1000 Storms"}

{"lens": "world", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "sources[1] (prize_wheel)", "issue": "The Snowy Canyon wheel is a random-reward source with no per-item price. The 117 Coins figure is the wheel spin cost, which the answer already labels. The source is still accurate, but a builder should not read 117 as this item's price.", "fix": "Keep the wheel as a random-reward source with no item price. Evidence: wiki page 'Snowy Canyon' lists 'Ninja's Shadow Blade of 1000 Storms' under Ninja Prize Wheel > Battle Item Mystery Pack, with a 117 Coins spin cost."}]}

I checked the world-lens claims directly:
- **Coin Shop:** `stores.json:15127` has item 75111 at 2152 purchase, 10% member discount, 1936 member price, and 215 sell price. 2152 × 0.9 ≈ 1936, so the figures agree. The wiki page says the blade is sold in the Coin Shop, with the price blank in the extract, so the repo row is the only price evidence. The client's coin store price (2152) matches.
- **Snowy Canyon wheel:** the wiki listing confirms the blade is in the Ninja Prize Wheel's Battle Item Mystery Pack.
- **Briarwood vendor:** correctly left out. It appears only in the unresolved file with no price or confirmed stock.
- **Retired:** null is honest, since no source gives a retirement status.
