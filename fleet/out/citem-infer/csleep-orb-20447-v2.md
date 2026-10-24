<!-- fleet job=citem-infer id=csleep-orb-20447-v2 status=done turns=5 usd=0.0030 tokens(read,write,in,out)=[38739, 12092, 12, 2242] model=claude-haiku-5-5 -->
# Sleep Orb

{"item": {"name": "Sleep Orb", "locale_id": 20447, "kind": "consumable"},
 "sources": [{"type": "prize_wheel", "detail": "Battle Item Mystery Pack: a prize-wheel prize from most combat mini-game prize wheels. Landing on it grants three identical battle items chosen at random; one of the 15 possible outcomes is Three Sleep Orbs (others: Sleep Sphere, Blast/Confusion/Flabbergast/Frag Orbs and Spheres, Unmoving Orb/Sphere, Medium Energy/Health/Replenishment Potions). Odds are not stated.", "where": "combat mini-game and dungeon prize wheels", "price": null, "currency": null, "source": "wiki page 'Battle Item Mystery Pack' (refs: freerealms-wiki/wikitext/4580-43972-d34b069e00e3.wiki, lines 3 and 6-24: 'Prizes' list including 'Three Sleep Orbs', line 21); wiki page 'Sleep Orb' (refs: freerealms-wiki/wikitext/12241-36163-63c64445c95c.wiki, line 4: 'acquired from Battle Item Mystery Packs')"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Sleep Orb is a level 1 battle item usable in any job; puts target to sleep for 10 seconds; hitting the target wakes them", "source": "wiki page 'Sleep Orb' (freerealms-wiki/wikitext/12241-36163-63c64445c95c.wiki); image:item_tooltip Sleep Orb.jpg"},
  {"claim": "Client name 'Sleep Orb' is locale:20447, description locale:20444 'A magical orb that puts your target to sleep.' (client definition 11011, class 9, no coin store price)", "source": "locale:20447; locale:20444; client definition 11011 (repo notes/Research/original-quest-coverage.json:600)"},
  {"claim": "Battle Item Mystery Pack grants three identical battle items at random; Sleep Orb is one of its 15 outcomes", "source": "wiki page 'Battle Item Mystery Pack' (freerealms-wiki/wikitext/4580-43972-d34b069e00e3.wiki, lines 3, 21)"},
  {"claim": "Sleep Orb's own tooltip shows Resell Value 19 coins; this is the item's resell value, not an acquisition price", "source": "image:item_tooltip Sleep Orb.jpg"},
  {"claim": "No coin store price for Sleep Orb (coin_store_prices empty in client definition; no stores.json entry found)", "source": "client definition 11011"}
 ],
 "confidence": 0.5,
 "open": [
  "Pack odds are not documented; the wiki lists 15 outcomes with no weights.",
  "The pack's own price (Resell Value 0 per the critique) is not verified here; no acquisition price is evidenced, so price is null.",
  "Whether battle item packs still drop from prize wheels in the live game, or were changed later, is not documented in the refs. Wiki pages are older freerealms.wikia-era pages, so 'live' stays unsure.",
  "Placeholder items Sleep Orb II (PH) (20445/20446, 20451/20452) and Sleep Orb IV (PH) are not this item and are not used as evidence.",
  "Critique said the 'Resell Value 19' figure belonged to gloves on the prize-wheel tables; not re-checked, but it is not used as a source price here.",
  "The wireable flag from the critique: this is a prize-wheel source with no evidenced price, so it should not be wired as a priced acquisition."
 ]}
