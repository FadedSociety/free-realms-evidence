<!-- fleet job=citem-infer id=candy-hair-style-card-114550-v2 status=done turns=4 usd=0.0024 tokens(read,write,in,out)=[18683, 10361, 10, 1919] model=claude-haiku-5-5 -->
# Andy Hair Style Card

{"item": {"name": "Andy Hair Style Card", "locale_id": 114550, "kind": "card"},
 "sources": [{"type": "coin_shop", "detail": "Coin store listing for definition 35937 (category 141, hair-card style block). No vendor, shop or NPC is named in the store data; acquisition method unresolved. The entry is flagged no_sale, so it is not evidenced as a current sale.", "where": null, "price": "540 coins (member price 486 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:11693 (item 35937)"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale:114550 'Andy Hair Style Card', description \"You'll be a Sites for sore eyes.\", slot 2, class 1, two definitions (6841 and 35937). The 540-coin store price comes from definition 35937.", "source": "locale:114550; client definition pack"},
  {"claim": "The store entry for 35937 is category 141, 540 coins, member price 486, sell price null, and no_sale true. It is not evidenced as a live sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json:11693"},
  {"claim": "Category 141 holds a run of 540-coin entries (sell 54, no_sale false) from item 6826 through at least 6852, with 6841 absent from the run. This shows a 540-coin category but does not price 6841 or name a vendor. The earlier claim that the block ends at 6846 was wrong.", "source": "repo:prototype/osfr-tools/data/content/stores.json:1841-1866"},
  {"claim": "Sibling hair style cards (Spacey 114545, Jubei 114546, Mane 114547, Sassy 114548, Silky 114549, Mohawk 114552, Reagan 114553, Bob 114554, Curly 114555, plus Afro 114535 through Frosty 114544) share the 'Hair Style Card' naming in the client text table. Andy is not named among them in any source.", "source": "lookup client: 'Hair Style Card' cluster (locale:114535-114555)"},
  {"claim": "Wiki Super Spooktacular (Week #1, 10/1/2013) says new hair color/style cards were introduced: Snowstorm, Pumpkin, Ectoplasm, Phantasm Blue, Bubblegum. Andy is not named, so this is background only and does not date the Andy card.", "source": "wiki: Super Spooktacular"}
 ],
 "confidence": 0.3,
 "open": [
  "The vendor, shop or NPC that sells the Andy card is not named in any source. No wiki page covers it. A wiki Coin Shop or hair-card category check is needed.",
  "Whether the card is still sold is unknown. Entry 35937 is no_sale. Definition 6841 has no store row, so its price and status are unknown.",
  "No second price source (wiki or article) confirms the 540-coin price or a sale price.",
  "No quest, drop, event, prize wheel, crafting or collection source found.",
  "Release date unknown. The Super Spooktacular claim does not name Andy.",
  "Critique fixes applied: vendor type downgraded to coin_shop with no vendor named; the 6841 block claim corrected to a range with 6841 absent; the release-window claim kept as background only; wireable is false, since no live acquisition with a named source exists."
 ]}
