<!-- fleet job=citem-infer id=carchmagus-wizard-hat-133462-v1 status=done turns=4 usd=0.0036 tokens(read,write,in,out)=[28146, 15692, 10, 2747] model=claude-haiku-5-5 -->
# Archmagus Wizard Hat

{"item": {"name": "Archmagus Wizard Hat", "locale_id": 133462, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale, store item 76454 (store category 101); the vendor/NPC is not named in the store data", "where": null, "price": "1276 coins (member price 1148 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 76454 (line 16104)"},
  {"type": "prize_wheel", "detail": "Wizard Prize Wheel reward, listed on the Snowy Canyon dungeon page (Combat Mini-game, difficulty 5). The same wheel list appears on other Wizard dungeon pages (Dark Spore Depths, Briarheart Caverns, Haunted Mines, Cray Caves, Trail of Betrayal, Tanglewood Fort) for the Archmagus Wizard Hat.", "where": "Snowy Canyon (Snowhill); wheel also listed on other Wizard dungeon pages", "price": "117 Coins (the wiki's dungeon entry price for a run on Snowy Canyon; wheel cost, not the item price)", "currency": "coins", "source": "wiki: Snowy Canyon; wiki: Dark Spore Depths; wiki: Briarheart Caverns; wiki: Haunted Mines; wiki: Cray Caves; wiki: Trail of Betrayal; wiki: Tanglewood Fort"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name locale 133462 is 'Archmagus Wizard Hat', definition 76454, slot 1, class 8, model caster_<race>_<gender>_head_fez.adr", "source": "locale:133462"},
  {"claim": "Store data lists item 76454 at purchase_price_coins 1276, member price 1148, sell price 127", "source": "repo:prototype/osfr-tools/data/content/stores.json item 76454"},
  {"claim": "Snowy Canyon wiki page lists '[Archmagus] [Wizard] Hat' under its '[Wizard] [Prize] [Wheel]' reward list, with a 117 Coins entry", "source": "wiki: Snowy Canyon"},
  {"claim": "Wizard Prize Wheel lists on the Dark Spore Depths, Briarheart Caverns, Haunted Mines, Cray Caves, Trail of Betrayal and Tanglewood Fort pages include other Archmagus Wizard pieces, confirming the same wheel pool", "source": "wiki: Dark Spore Depths; wiki: Briarheart Caverns; wiki: Haunted Mines; wiki: Cray Caves; wiki: Trail of Betrayal; wiki: Tanglewood Fort"},
  {"claim": "Client cluster: the Archmagus Wizard set items (Robe, Shoes, Gloves, Slacks, Skirt, Talisman) sit at adjacent locale ids 133458-133467, consistent with one set", "source": "locale:133457-133467"}
 ],
 "confidence": 0.6,
 "open": [
  "The store entry 76454 does not name a coin vendor; the vendor NPC and zone for the 1276-coin sale are not confirmed. Store category 101 was not decoded.",
  "The Snowy Canyon wiki entry is a dungeon-run wheel list; the wiki does not state whether the Archmagus Wizard Hat drops only from the wheel or also appears in a sale. Treated as prize_wheel, not as a dungeon drop.",
  "Wiki prices (117 / 214 / 77 / 307 Coins) are per-dungeon wheel run costs, not this hat's price; no wiki article gives a price for the hat itself.",
  "Retired status not found in any source; the coin store listing is the only price, so live status is inferred from the store data and the wiki, not confirmed by a date.",
  "The jev first pass tagged 'vendor'; the store data supports a coin sale and the wiki supports a prize wheel. The vendor claim is not verified beyond the store entry."
 ]}
