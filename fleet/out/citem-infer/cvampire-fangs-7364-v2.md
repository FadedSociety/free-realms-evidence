<!-- fleet job=citem-infer id=cvampire-fangs-7364-v2 status=done turns=2 usd=0.0028 tokens(read,write,in,out)=[6599, 12946, 6, 2284] model=claude-haiku-5-5 -->
# Vampire Fangs

{"item": {"name": "Vampire Fangs", "locale_id": 7364, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store listing for definition 79138 (store category 101), purchase price 50 coins, member price 45 coins (10% member discount). The store data does not name the vendor or shop, so the exact channel is unconfirmed.", "where": null, "price": "50 coins (member price 45 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 79138 (line 16915)"},
  {"type": "promotion", "detail": "Team Vampire Bundle: locale 432411 says it comes with a Black Vampire Outfit, a Black Bat Pet, 'exclusive Vampire Fangs' and a Team Vampire T-Shirt. Sale channel and dates are not stated.", "where": null, "price": null, "currency": null, "source": "locale:432411; locale:432410"},
  {"type": "event", "detail": "Vampires vs. Werewolves dance-off: '[Vampire] [Fangs]' is listed among the Team [Vampire] items on the dance-off wiki page. The page does not give a price, and the year is unknown. The item-list entry is single-sourced, so treat it as unverified against client text.", "where": null, "price": null, "currency": null, "source": "wiki page 'Vampires vs. Werewolves Dance-off' (Items section)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition 79138 is named Vampire Fangs (locale 7364), clothing slot 1, with a 50-coin store price (member 45).", "source": "locale:7364; repo:prototype/osfr-tools/data/content/stores.json item 79138 (line 16915)"},
  {"claim": "Vampire Fangs are a Super Spooktacular costume item that cannot be worn together with the Werewolf Tail. This describes event association only; the source gives no acquisition method.", "source": "http://www.freerealms.com/article/detail.action?articleId=1860; locale:7366"},
  {"claim": "The Team Vampire Bundle contains 'exclusive Vampire Fangs'.", "source": "locale:432411"},
  {"claim": "The dance-off wiki page lists '[Vampire] [Fangs]' under Team [Vampire] items and is in Category:Super Spooktacular and Category:Seasonal.", "source": "wiki page 'Vampires vs. Werewolves Dance-off'"}
 ],
 "confidence": 0.5,
 "open": [
  "Conflict: the 50-coin store listing (stores.json 79138) and locale 432411 ('exclusive Vampire Fangs' in the Team Vampire Bundle) are not reconciled. It is unresolved whether the standalone listing is live or the item is bundle-only. Neither is settled.",
  "The store category 101 is not mapped to a named vendor or Coin Shop page, so the coin channel is unconfirmed.",
  "The dance-off source rests on one wiki item list with no price, date or explicit acquisition text. The earlier claim that the Pumpkin Prince hands out the Fangs was not verified in client text (locale 432069 is not linked to Fangs). Year unknown.",
  "The Super Spooktacular link is event association only (articleId=1860; locale:7366). Acquisition is unknown and no event source is claimed for it.",
  "Live status and retirement are unknown: no source says whether the Super Spooktacular or the Team Vampire Bundle is still sold."
 ],
 "critique_response": "Evidence critique: the Super Spooktacular row is now an association note, not an acquisition source. World critique: the coin-store row is kept as evidenced, but the 'exclusive' wording in locale 432411 is flagged as a conflict rather than resolved. The dance-off row is marked single-wiki-sourced and unverified against client text."
}
