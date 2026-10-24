<!-- fleet job=citem-infer id=ctiny-tincture-36359-v1 status=nothing_found turns=4 usd=0.0038 tokens(read,write,in,out)=[27503, 16428, 10, 2954] model=claude-haiku-5-5 -->
# Tiny Tincture

{"item": {"name": "Tiny Tincture", "locale_id": 36359, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Tiny Tincture' is locale 36359; the client definition is item 2997, class 9, slot 0, with no models and no coin store price in the client pack.", "source": "locale:36359; client definition pack"},
  {"claim": "Client description: 'Eating this food will decrease the size of the player.' Locale 11558 is a different shrink-food line ('temporarily shrink'), so it is not this item's text.", "source": "client definition pack; locale:11558"},
  {"claim": "The shrink/grow food family (Shrink Food I-IV, Grow Food I-V, Tiny Tincture; locale 36353-36364) is client-only in the text table. Grow Food II-V are tagged quest_reward in the client text, but no quest is linked to them in the repo or wiki.", "source": "locale:36353-36364 (lookup client)"},
  {"claim": "No wiki page, article, video frame, or other answer names Tiny Tincture or the Shrink/Grow Food items. Searches of refs (wiki raw, articles) and repo JSON found no quest, drop, or event record for them.", "source": "lookup wiki/articles/video 'Tiny Tincture', 'Shrink Food OR Grow Food'; search refs/repo"},
  {"claim": "Repo stores.json has a row item_id 36359, category 4, purchase 40 coins (member 36, sell 4), in a block with 36351-36364 at 60 or 40 coins. The row is keyed by 36359, which equals this item's locale id, not its definition id 2997. The client pack lists no coin store price, so the mapping is unconfirmed and I did not cite it as a source.", "source": "repo:prototype/osfr-tools/data/content/stores.json:11908 (and 11900-11912)"},
  {"claim": "The first-pass tag ('live: yes', 'source_guess: unknown') is a hint only and has no evidence behind it.", "source": "jev_first_pass"}
 ],
 "confidence": 0.2,
 "open": [
  "No confirmed acquisition source. The only lead is the stores.json row for id 36359 (40 coins, member 36), but it is keyed on the locale id rather than definition 2997 and the client shows no coin price. Confirm whether store item_ids use definition ids or locale ids, and which vendor sells category 4 in source tags L1, L2, L4, R2, T633, R1.",
  "No wiki article, and no quest or drop, is recorded for Tiny Tincture. Grow Food II-V carry quest_reward text, so the family may come from quests. Check quest data for locale 36361-36364 and 36359 before assigning a quest source.",
  "Retired status unknown. No wiki or article source says it was retired or still sold.",
  "The pack's critiques field was empty, so there were none to fix.",
  "Client definition has 1 definition (id 2997), 0 models, slot 0 and class 9. Check whether class 9 is a consumable class to confirm the kind."
 ]}
