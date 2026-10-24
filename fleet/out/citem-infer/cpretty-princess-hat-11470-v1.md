<!-- fleet job=citem-infer id=cpretty-princess-hat-11470-v1 status=done turns=4 usd=0.0028 tokens(read,write,in,out)=[17104, 11292, 10, 2498] model=claude-haiku-5-5 -->
# Pretty Princess Hat

{"item": {"name": "Pretty Princess Hat", "locale_id": 11470, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale, item 2679 (tint group 3, store category 101). The store data does not name the vendor, so this is a coin store listing rather than a confirmed NPC vendor.", "where": null, "price": "270 coins (member price 243 coins with 10% member discount; sell-back 27 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:715 (item_id 2679)"},
  {"type": "event", "detail": "Wiki page 'Regal Princess Hat' describes the Regal Princess Hat as a variation of the Pretty Princess Hat, a 'Virtual Reward' tied to a #FreeRealms Twitter challenge. The page text is truncated, so the exact reward event and date are not confirmed.", "where": null, "price": null, "currency": null, "source": "wiki: Regal Princess Hat"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name 'Pretty Princess Hat' is locale 11470; description 'A pretty princess hat to wear!' (locale 11530 uses the same description text).", "source": "locale:11470; locale:11530"},
  {"claim": "Client definition 2679 has 1 definition, equip slot 1, class 1, model freestyle_<race>_f_head_princesshat.adr, and the item sits in a set of kitty/princess items (locale 11471-11475).", "source": "client definition in the evidence pack; locale:11471-11475"},
  {"claim": "Store data lists item 2679 at 270 coins, category 101, with a 10% member discount (243 coins) and sell-back 27 coins. Source tags L1, L2, L4, R2, T633, R1 match other live coin-store items.", "source": "repo:prototype/osfr-tools/data/content/stores.json:715"},
  {"claim": "Wiki says the Regal Princess Hat is a variation of the Pretty Princess Hat, a Virtual Reward from a #FreeRealms Twitter challenge, so the Pretty Princess Hat was also given as a promotional reward.", "source": "wiki: Regal Princess Hat"}
 ],
 "confidence": 0.5,
 "open": [
  "The store row does not name the vendor or the shop that sells item 2679 at 270 coins. Category 101 is shared by many items, so the NPC vendor is unknown. Check the vendor tables to find which NPC stocks it.",
  "Conflict: the store listing says a 270-coin sale, but the wiki calls the item a 'Virtual Reward' from a Twitter challenge. Both may be true (sold for coins and also given as a reward), but the wiki page text is cut off, so the exact challenge, date and any retirement cannot be confirmed.",
  "Retired status and any later removal from sale are unknown. The store source tags suggest it was live in the store data, but no dated source confirms when it was last sold.",
  "The wiki page for the Pretty Princess Hat itself is not in the cache, so details are taken only from the Regal Princess Hat page.",
  "Other pack items (Kitty Princess Collar/Tiara/Gown/Slippers, Pug Whistle) were not checked; they may share this source."
 ]}
