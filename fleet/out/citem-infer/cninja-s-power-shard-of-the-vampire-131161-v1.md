<!-- fleet job=citem-infer id=cninja-s-power-shard-of-the-vampire-131161-v1 status=done turns=8 usd=0.0067 tokens(read,write,in,out)=[117562, 29017, 18, 3884] model=claude-haiku-5-5 -->
# Ninja's Power Shard of the Vampire

{"item": {"name": "Ninja's Power Shard of the Vampire", "locale_id": 131161, "kind": "other"},
 "sources": [
  {"type": "prize_wheel", "detail": "Ninja Prize Wheel from the Mushroom Mania! battle (node battle started by clicking a Nettleseed Pest in Nettleseed, Briarwood); the wheel lists it alongside Battle Item Mystery Pack, Chunin Ninja Wristguards and Ninja's Necklace of Vitality V", "where": "Mushroom Mania! (Nettleseed, Briarwood)", "price": null, "currency": null, "source": "wiki: Mushroom Mania! (Ninja [Prize] [Wheel] section); notes/Build Guides/Content/Dungeons/Mushroom Mania.md"},
  {"type": "coin_shop", "detail": "Coin store listing for item 75417 (category 121), the store row that carries this shard; the client definition's coin price is 2435 coins (member price 2191 coins, 10% member discount; sell price 243 coins)", "where": "coin store (category 121)", "price": "2435 coins (member 2191 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75417 (line 15301)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name exists as locale 131161 \"Ninja's Power Shard of the Vampire\"; it is one of six job variants (Archer, Brawler, Medic, Ninja, Warrior, Wizard) of the same Power Shard of the Vampire", "source": "locale:131161; lookup client locale:130966, 131031, 131096, 131226, 131291"},
  {"claim": "Mushroom Mania! wiki page lists \"[Ninja]'s [Power] [Shard] of the [Vampire]\" on the Ninja Prize Wheel", "source": "wiki: Mushroom Mania! (page text, Ninja [Prize] [Wheel])"},
  {"claim": "Mushroom Mania! wiki page also lists the Archer's Power Shard of the Vampire on the Archer Prize Wheel, so the shard is a wheel reward for each job", "source": "wiki: Mushroom Mania! (Archer Prize Wheel)"},
  {"claim": "The client definition for item 75417 carries a coin store price of 2435 coins in stores.json (category 121), the only store price for this item", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75417"},
  {"claim": "Mushroom Mania! is a node battle (difficulty 5) started from a Nettleseed Pest in Nettleseed, Briarwood", "source": "notes/Build Guides/Content/Dungeons/Mushroom Mania.md (line 11, wiki: Mushroom Mania!)"}
 ],
 "confidence": 0.5,
 "open": [
  "The 2435-coin store price is far above the other coin prices the wiki shows for Ninja shards and wheel gear, and no wiki page names a Coin Shop sale for this shard. The coin_shop row rests only on the stores.json row; the price needs checking against the live store before it is trusted.",
  "The wiki page for Mushroom Mania! shows a '77 Coins' figure beside the Archer wheel and '..108 Coins' on another wheel page; this is an unexplained per-wheel number, not a price for this shard, and was not used as a price.",
  "Whether the Mushroom Mania! battle still runs live (and so whether the wheel reward is still obtainable) is not confirmed by any source in the pack; retired is left null.",
  "No video frame, article or quest names this shard; the only evidence is the wiki wheel list and the store row.",
  "The Mushroom Mania! battle has no confirmed quest that starts it (per notes/Build Guides/Content/Dungeons/Mushroom Mania.md), so the trigger for the wheel is unclear.",
  "The client description is empty; no model files or extra slot info beyond slot 12 and class 2."
 ]}
