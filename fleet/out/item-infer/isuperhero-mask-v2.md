<!-- fleet job=item-infer id=isuperhero-mask-v2 status=done turns=2 usd=0.0015 tokens(read,write,in,out)=[4774, 5602, 6, 1427] model=claude-haiku-5-5 -->
# Superhero Mask

{"item": {"name": "Superhero Mask", "locale_id": 143214, "kind": "clothing"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace, sold to everyone (All Jobs, head slot clothing)", "where": "Station Cash Marketplace", "price": "49 Station Cash (regular); 44 Station Cash for Members (10% member discount). Infobox values only; the wiki price sentence is blank in the pack, so the figures are unconfirmed in text.", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Superhero_Mask (rev 37195; categories SC Marketplace, SC Marketplace Clothing, Marketplace Items; infobox station_cash [49, 44])"},
  {"type": "vendor", "detail": "Cragara, the roaming Mysterious Merchant; wiki says the mask is also sold through her. Stock is rotating, so this is conditional.", "where": "Random town spawn (Seaside, Merry Vale, Snowhill, Blackspore Swamp, Briarwood, Sunstone Valley)", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Superhero_Mask (text 'through Cragara'; category Mysterious Merchant). No Superhero Mask stock row in repo vendors.json; price not verified."}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name string is 'Superhero Mask'", "source": "locale:143214"},
  {"claim": "Wiki: available to everyone on the Station Cash Marketplace and through Cragara; Members get a 10% discount", "source": "https://freerealms.fandom.com/wiki/Superhero_Mask"},
  {"claim": "Wiki categories include SC Marketplace and Mysterious Merchant", "source": "https://freerealms.fandom.com/wiki/Superhero_Mask"},
  {"claim": "Related client items exist: Doggy Superhero Mask (locale:12494), Kitty Superhero Mask (locale:80887), Blue Superhero Mask (locale:151302); the doggy pet mask is in notes/Research/Pets Service.md:119, which is a different item", "source": "locale:12494; locale:80887; locale:151302; repo notes/Research/Pets Service.md:119"}
 ],
 "confidence": 0.5,
 "open": [
  "Price 49/44 Station Cash comes only from the wiki infobox; the price sentence is stripped in the pack. Confirm on a second source.",
  "Cragara source has no price evidence and rests on the wiki text alone; it is rotating stock, so it is not a standing acquisition. The earlier 49/44 Cragara price was an assumption and was removed.",
  "No retirement or unobtainable note found; retired left null, live 'unsure'.",
  "Critique fixes applied: Cragara price removed and marked conditional; infobox-only price flagged."
 ]}
