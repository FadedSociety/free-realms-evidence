<!-- fleet job=citem-infer id=cvampire-cake-slice-6628-v2 status=done turns=3 usd=0.0019 tokens(read,write,in,out)=[12234, 7024, 8, 1836] model=claude-haiku-5-5 -->
# Vampire Cake Slice

{"item": {"name": "Vampire Cake Slice", "locale_id": 6628, "kind": "consumable"},
 "sources": [{"type": "event", "detail": "Vampires vs. Werewolves dance-off (Super Spooktacular), winning-team reward; the reward is one of the two cake slices, depending on which team wins", "where": "Super Spooktacular event", "price": null, "currency": null, "source": "wiki: Super Spooktacular (\"Werewolves Dance-off -- the reward is either a Vampire Cake Slice or a Werewolf Cake Slice, depending on which team wins\"); video:yWuHe_jYyc4/00190.jpg (Madam Zelda quest 'A Dark Future' lists both slices)"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 6628 is 'Vampire Cake Slice'; client item definition 10433, class 9, slot 0, no coin store price.", "source": "locale:6628; client definition 10433"},
  {"claim": "Super Spooktacular reward line: the Vampires vs. Werewolves dance-off pays either a Vampire Cake Slice or a Werewolf Cake Slice depending on the winning team.", "source": "wiki: Super Spooktacular"},
  {"claim": "The Werewolf Dance Practice wiki page lists 'Vampire Cake Slice' among its reward pool entries, with a '150 Coins' line that appears adjacent in the same table and is not confirmed as this item's price.", "source": "wiki: Werewolf Dance Practice"},
  {"claim": "The Vampire Dance Practice wiki page lists 'Werewolf Cake Slice' (not the Vampire slice) in its reward pool, so the per-team mapping is not confirmed by the practice pages.", "source": "wiki: Vampire Dance Practice"},
  {"claim": "Locale 6629 ('For midnight flight, day or night') is the description of Illusion: Black Bat (locale 6630), not of this item; this item's own description is not confirmed.", "source": "locale:6629; locale:6630"},
  {"claim": "No coin vendor, Station Cash Marketplace, or Coin Shop listing found: no coin_store_prices in client definition and empty vendor stock.", "source": "repo store data; client definition 10433"}
 ],
 "confidence": 0.5,
 "open": [
  "Year of the dance-off that paid this slice is not confirmed; no source dates it, so retirement status is unknown.",
  "Which team's win pays the Vampire slice is inferred, not stated: the Super Spooktacular line names both slices without naming the winning side. The Dance Practice pages do not settle it either (Vampire Dance Practice lists the Werewolf slice; Werewolf Dance Practice lists the Vampire slice).",
  "Bone Bog Cemetery / Blackspore Swamp location removed: no source in the pack places the dance-off there.",
  "Team-choice mechanic via Madam Zelda (article 1862) was not read; only the video frame supports the quest listing both slices.",
  "The '150 Coins' figure on the Dance Practice pages is not tied to this slice; no price recorded.",
  "No description for this item in the client; locale 6629 belongs to another item."
 ]}
