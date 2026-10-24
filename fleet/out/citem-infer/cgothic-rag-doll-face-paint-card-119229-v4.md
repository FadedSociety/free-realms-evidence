<!-- fleet job=citem-infer id=cgothic-rag-doll-face-paint-card-119229-v4 status=done turns=4 usd=0.0023 tokens(read,write,in,out)=[21401, 7980, 10, 2104] model=claude-haiku-5-5 -->
# Gothic Rag Doll Face Paint Card

{"item": {"name": "Gothic Rag Doll Face Paint Card", "locale_id": 119229, "kind": "clothing"},
 "sources": [
  {"type": "drop", "detail": "Pumpkin Prince's Treasure chest, received when the Pumpkin Prince is defeated (a win by the Prince drops nothing). Drop rate and guarantee unknown.", "where": "Open-world Pumpkin Prince fight; wiki places the Prince in Bone Bog Cemetery, but no source confirms this card drops there", "price": null, "currency": null, "source": "video:nmT76ti9kyo/00264.jpg (chest prompt 'Pumpkin Prince's Treasure' reads 'You receive 1 Gothic Rag Doll Face Paint Card' plus 18 Ectoplasmic Goo); wiki Pumpkin Prince (defeat drops a treasure chest with a limited Super Spooktacular reward)"},
  {"type": "event", "detail": "Super Spooktacular, annual October Halloween event; the Pumpkin Prince chest carries this limited event reward", "where": "Open-world / Bone Bog Cemetery per wiki", "price": null, "currency": null, "source": "wiki Super Spooktacular (annual October event); wiki Pumpkin Prince"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Gothic Rag Doll Face Paint Card', description 'Ever feel like you woke up on the wrong side of the toy chest?', one definition (69549), slot 6, class 1", "source": "locale:119229"},
  {"claim": "Card sits in the Halloween block 119224-119234 with the other cut-out/paper bag masks and face paint cards", "source": "locale:119224 through locale:119234"},
  {"claim": "Wiki Pumpkin Prince: defeat drops a treasure chest with a limited Super Spooktacular reward; a win drops nothing; Prince appears in Bone Bog Cemetery", "source": "wiki Pumpkin Prince"},
  {"claim": "Chest prompt names the card and 18 Ectoplasmic Goo as the rewards", "source": "video:nmT76ti9kyo/00264.jpg"},
  {"claim": "Store row for item 69549 exists: category 145, purchase 180 coins, member 162, sell null, no_sale true. It names no vendor, zone or stock.", "source": "repo:prototype/osfr-tools/data/content/stores.json:14890 (verified by search)"},
  {"claim": "Super Spooktacular is an annual October event, so the chest reward is seasonal", "source": "wiki Super Spooktacular"}
 ],
 "confidence": 0.5,
 "open": [
  "Coin shop listing removed as a source: stores.json:14890 (item 69549, 180 coins / 162 member, category 145) has no_sale true, no sell price, and no vendor, zone or stock row. It is an unconfirmed listing, not evidence of a live coin sale. The item's only sourced acquisition is the Pumpkin Prince chest.",
  "Retirement not stated by any source. Inference only: the event is October-only and the store row is no_sale, so the card is probably retired or unobtainable outside the event. No retirement date is given. Left null.",
  "Drop rate and whether the chest is guaranteed on defeat are unknown.",
  "The Bone Bog Cemetery location is wiki-only; the video frame does not show the fight location.",
  "Video frame names the card on the chest, but the single frame does not show whether the chest is one-per-player or shared.",
  "Confirm 69549 is this exact card and not a sibling variant (69549-69554 are all category 145 coin rows).",
  "The cut-out and paper bag masks in the same locale block were not checked."
 ]
}
