<!-- fleet job=citem-infer id=cninja-s-power-shard-of-the-vampire-131161-v3 status=done turns=4 usd=0.0024 tokens(read,write,in,out)=[23824, 9209, 10, 1948] model=claude-haiku-5-5 -->
# Ninja's Power Shard of the Vampire

{"item": {"name": "Ninja's Power Shard of the Vampire", "locale_id": 131161, "kind": "other"},
 "sources": [
  {"type": "prize_wheel", "detail": "Ninja Prize Wheel, Mushroom Mania! battle (difficulty 5, started by clicking a Nettleseed Pest; the wheel also lists Battle Item Mystery Pack, Chunin Ninja Wristguards, Ninja's Necklace of Vitality V). Trigger beyond the pest click is not confirmed by any quest.", "where": "Mushroom Mania!, Nettleseed, Briarwood", "price": null, "currency": null, "source": "wiki: Mushroom Mania! (Archer Prize Wheel section confirmed by lookup, showing Archer's Power Shard of the Vampire; Ninja Prize Wheel section listed in the evidence pack, the returned snippet was truncated before it)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Mushroom Mania! is a difficulty 5 battle started by clicking a Nettleseed Pest in Nettleseed, Briarwood; rewards 40 Stars and Members Only Bonus 108 Coins", "source": "wiki: Mushroom Mania!"},
  {"claim": "The wiki Mushroom Mania! page lists Archer's Power Shard of the Vampire on the Archer Prize Wheel, so the shard is a per-job wheel reward", "source": "wiki: Mushroom Mania! (Archer Prize Wheel)"},
  {"claim": "The Ninja Prize Wheel listing of this shard is stated in the evidence pack and critiques but was not visible in my lookup snippet", "source": "wiki: Mushroom Mania! (Ninja Prize Wheel), per pack"},
  {"claim": "Repo store data has item 75417 in category 121 at purchase 2435 coins, member price 2191, sell 243; items 75413-75418 carry the same row. This is a repo data row only; category 121 is not confirmed as the live Coin Shop and no wiki, article or video confirms a live sale", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 15297-15302"},
  {"claim": "Client name locale 131161; sibling job variants at 130966, 131031, 131096, 131226, 131291; client description is empty, no model files, slot 12, class 2", "source": "locale:131161; client definition"}
 ],
 "confidence": 0.5,
 "open": [
  "Coin Shop sale is NOT listed as a sourced acquisition: the only support is an unverified stores.json row (2435 coins, member 2191, sell 243, category 121, items 75413-75418 identical). Confirm against the live store before adding a coin_shop source.",
  "Mushroom Mania! trigger: no confirmed quest starts the battle; the pest click is the only known trigger.",
  "Whether Mushroom Mania! and its wheel still run live is unconfirmed; retired left null, live 'unsure'.",
  "The 77 Coins and 108 Coins figures on the Mushroom Mania! page are battle rewards, not prices for this shard.",
  "Ninja wheel line should be re-checked on the full wiki page; the lookup snippet truncated before it."
 ],
 "cross_notes": [],
 "id_check": []}
