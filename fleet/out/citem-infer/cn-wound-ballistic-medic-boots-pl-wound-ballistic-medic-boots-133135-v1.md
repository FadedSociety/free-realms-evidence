<!-- fleet job=citem-infer id=cn-wound-ballistic-medic-boots-pl-wound-ballistic-medic-boots-133135-v1 status=done turns=9 usd=0.0050 tokens(read,write,in,out)=[72823, 17603, 20, 4133] model=claude-haiku-5-5 -->
# {n}Wound Ballistic Medic Boots{pl="Wound Ballistic Medic Boots"}

{"item": {"name": "Wound Ballistic Medic Boots", "locale_id": 133135, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Zaan (pixie Medic-job merchant, sells only Medic job items)", "where": "Shrouded Glade (near the Cooking Table)", "price": "1276 coins (reference purchase price); 1148 coins member price; sell-back 127 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 76127 (purchase_price_coins 1276, member_discount_percent 10, member_price_coins 1148); repo:prototype/osfr-tools/data/content/vendors.json item 76127 (stock_source: wiki page Zaan, section Sells, https://freerealms.fandom.com/wiki/Zaan); wiki page Zaan (Sells list, marked {{Member}})"},
  {"type": "prize_wheel", "detail": "Medic Prize Wheel, Briarheart Caverns dungeon (one of the wheel's listed rewards)", "where": "Briarheart Caverns, Briarheart, Briarwood", "price": "117 coins listed on the wheel section of the page (meaning of this figure unclear; see open)", "currency": "coins", "source": "wiki page Briarheart Caverns, Medic Prize Wheel section (freerealms-wiki/wikitext/2831-49146-33c508286627.wiki lines 47-54)"},
  {"type": "event", "detail": "Dungeon bonus reward for completing 'Defeat all enemies!' in Briarheart Caverns: a random Medic-set piece (Wound Ballistic set) matching the receiving player's job; color and body part random", "where": "Briarheart Caverns, Briarwood", "price": null, "currency": null, "source": "wiki page Briarheart Caverns, Bonus Rewards section (lines 83-88; Medic: Energy Transfer, Stopping Power, Wound Ballistic)"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Client name locale 133135 is 'Wound Ballistic Medic Boots' (one of 11 Medic-set items 133130-133140), slot 5, item class 7, model military_<race>_<gender>_feet_boots.adr", "source": "locale:133135; client definition definition_ids 76127"},
  {"claim": "Zaan sells Wound Ballistic Medic Boots; she sells exclusively Medic job items", "source": "wiki page Zaan (https://freerealms.fandom.com/wiki/Zaan, Sells section)"},
  {"claim": "Reference price 1276 coins, member price 1148 coins, sell price 127 coins; source tags say reference price, not a captured NPC quote", "source": "repo:prototype/osfr-tools/data/content/stores.json item 76127; repo:prototype/osfr-tools/data/content/vendors.json item 76127 (price_basis)"},
  {"claim": "Boots appear on Briarheart Caverns Medic Prize Wheel list and as a random bonus-reward piece for the 'Defeat all enemies!' goal", "source": "wiki page Briarheart Caverns (freerealms-wiki/wikitext/2831-49146-33c508286627.wiki)"},
  {"claim": "Catalogue row marks the item runtime_eligible: true", "source": "repo:prototype/osfr-tools/data/content/vendors.json item 76127"},
  {"claim": "Zaan was introduced in-game on August 27, 2013", "source": "wiki page Zaan, Trivia section"}
 ],
 "confidence": 0.7,
 "open": [
  "Coin price 1276 is a stores.json reference price, not a price seen on a captured Zaan NPC quote; the wiki page gives no price. Verify in game before using as the live price.",
  "Wiki Zaan list marks the boots with {{Member}}; the member-only meaning is inferred from the template name and the stores.json member price (1148). Confirm whether non-members can buy it.",
  "The 117 Coins line under the Briarheart Medic Prize Wheel is ambiguous (wheel spin cost or reward value); it is not a sale price for the boots.",
  "The Zaan page snapshot's revision date (2021-12-14) is older than the Briarheart snapshot; stock may have changed since. No retirement evidence was found, so retired is null.",
  "Could not verify the stores.json path at data/content (searched repo/data, which does not exist); used prototype/osfr-tools/data/content instead.",
  "Bonus-reward drop: the wiki does not say the chance of getting this specific piece (boots vs other Medic-set items), so it is recorded as an event source with no rate."
 ]}
