<!-- fleet job=item-infer id=ieerie-gi-v4 status=done turns=3 usd=0.0017 tokens(read,write,in,out)=[11687, 6417, 8, 1497] model=claude-haiku-5-5 -->
# Eerie Gi

{"item": {"name": "Eerie Gi", "locale_id": null, "kind": "clothing"},
 "sources": [
  {"type": "event", "detail": "Free Realms comic book issue code redemption: entered the code printed for Free Realms comic issues 1-4 (listed on the comic page's Collection Rewards)", "where": null, "price": null, "currency": null, "source": "wiki page: Free Realms (comic), Collection Rewards ('Eerie Gi (acquired by entering the codes for Free Realms comic issues 1-4)'); wiki page: Eerie_Gi (rev 47265): 'It acquired by entering the codes for Free Realms comic issues 1-4'"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Eerie Gi is a level 16 Ninja chest-slot clothing item, Cannot Trade, required Level 16 Ninja, Power 5", "source": "wiki page: Eerie_Gi (rev 47265); image:item_tooltip"},
  {"claim": "Obtained by entering the codes for Free Realms comic issues 1-4; the comic page lists the same mechanic for Nightmarish Gloves (issues 5-8) and Sinister Cowl", "source": "wiki page: Free Realms (comic), Collection Rewards; wiki page: Eerie_Gi (re-checked via lookup)"},
  {"claim": "Resell Value 118 is shown on the tooltip; it is a resell value, not a purchase price, and is not used as a price here", "source": "image:item_tooltip on Eerie_Gi wiki page"}
 ],
 "confidence": 0.55,
 "open": [
  "Name is sourced to the wiki only (Eerie_Gi rev 47265 and the Free Realms (comic) Collection Rewards line). locale:3952 is FLAGGED 'fragment: truncated name' by the automatic id check and is not used as evidence; locale_id is left null until flags.tsv is checked and the flag cleared. The earlier claim that en_us_data.dat contains the string was not verified and is dropped.",
  "No coin or Station Cash price: no vendor, marketplace, coin shop or prize wheel in the pack sells it, and the wiki gives no purchase price.",
  "Code redemption dates and validity are unknown: the wiki does not say when the comic codes were active or whether they still work, so live is 'unsure' and retired is null.",
  "The mechanic rests on a single wiki listing (Free Realms (comic) Collection Rewards). The individual comic codes are not in the pack.",
  "An earlier critique cited an internal note in quest-lines/events.json (around line 22540) marking the comic rewards as unverified. That file was not found in the repo, so the conflict is unresolved and the builder should check it."
 ]}
