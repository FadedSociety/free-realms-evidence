<!-- fleet job=citem-infer id=cn-action-power-warrior-pauldrons-pl-action-power-warrior-pau-133373-v1 status=done turns=4 usd=0.0043 tokens(read,write,in,out)=[27161, 17381, 10, 3771] model=claude-haiku-5-5 -->
# {n}Action Power Warrior Pauldrons{pl="Action Power Warrior Pauldrons"}

{"item": {"name": "Action Power Warrior Pauldrons", "locale_id": 133373, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale, Warrior-set pauldrons (store vendor not named in our data; category_id 106 is unnamed in the store file)", "where": "Coin store (vendor unnamed in repo data)", "price": "1076 coins (member price 968 coins with 10% member discount; sell price 107 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 76365 (line 16027)"},
  {"type": "prize_wheel", "detail": "[Warrior] Prize Wheel / Battle Item Mystery Pack reward lists on dungeon wiki pages (Mudshell, Chugawump, Tanglewood Fort area pages list '[Action] [Power] [Warrior] Pauldrons' under those headings). Exact wheel and per-spin odds not confirmed.", "where": "Dungeon/mini-game pages (Mudshell, Chugawump, Tanglewood Fort, Briarwood area)", "price": null, "currency": null, "source": "wiki pages: Mudshell; Chugawump!; Tanglewood Fort (lookup 'Action Power Warrior' hits, wiki namespace 0)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name locale 133373 is 'Action Power Warrior Pauldrons' (set of 6 Action Power Warrior pieces: Tunic, Hightops, Gauntlets, Helm, Breeches, Pauldrons, IDs 133368-133373)", "source": "locale:133373"},
  {"claim": "Store data lists item 76365 at purchase_price_coins 1076, member price 968, sell 107, not no_sale; tags L1,L2,L4,R2,T633,R1 suggest it was on sale across multiple live-era releases", "source": "repo:prototype/osfr-tools/data/content/stores.json item 76365"},
  {"claim": "The wiki lists '[Action] [Power] [Warrior] Pauldrons' as a reward in the [Warrior] Prize Wheel and Battle Item Mystery Pack entries on several dungeon pages", "source": "lookup wiki: Mudshell, Chugawump!, Tanglewood Fort, Hot Springs Haven pages"},
  {"claim": "Demo Derby: Tucker's Troubles video frame shows the Action Power Warrior Breeches, Hightops, Pauldrons and Tunic in a player's inventory/trade window (player-to-player trade, not a source)", "source": "video:eqV_FzElXSE/00384.jpg"},
  {"claim": "The 'Standard [Action] [Warrior] Pauldrons' is a separate, non-Power item also seen in prize-wheel lists", "source": "lookup wiki: Sheep Watch page"}
 ],
 "confidence": 0.6,
 "open": [
  "Coin vendor name/location for store item 76365 is not in the repo data; stores.json has category_id 106 but no vendor name. Need the NPC/shop that holds that category.",
  "Prize-wheel and Battle Item Mystery Pack lines are wiki snippets whose price lines (e.g. 10, 33, 214 Coins) belong to the page's wheel/pack, not confirmed per item; no per-item odds or price were found.",
  "Retirement status not confirmed: no wiki or article source states an end date. Store data flags it as on sale but gives no date.",
  "The client definition lists 1 coin price (1076) with no model per variant; variant count reported as 1 definition, so tint/race variants were not checked.",
  "Demo Derby video frame shows the item in trade, not a source; not used as a source.",
  "Wiki 'Action Power Warrior' article itself was not found; the set's sources are inferred from the store row and prize-wheel lists."
 ]}
