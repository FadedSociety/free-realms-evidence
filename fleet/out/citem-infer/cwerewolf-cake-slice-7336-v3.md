<!-- fleet job=citem-infer id=cwerewolf-cake-slice-7336-v3 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[6618, 8422, 6, 2265] model=claude-haiku-5-5 -->
# Werewolf Cake Slice

{"item": {"name": "Werewolf Cake Slice", "locale_id": 7336, "kind": "consumable"},
 "sources": [
  {"type": "event", "detail": "Vampires vs. Werewolves dance-off, Super Spooktacular (Halloween event). Reward is one of two cake slices depending on the winning team: Vampire Cake Slice or Werewolf Cake Slice. Which team yields the Werewolf slice is inferred, not stated by any source.", "where": "Blackspore Swamp (Super Spooktacular dance-off)", "price": null, "currency": null, "source": "wiki page: Super Spooktacular (\"the reward is either a Vampire [Cake] [Slice] or a [Werewolf] [Cake] [Slice], depending on which team wins\"); locale:7336"},
  {"type": "prize_wheel", "detail": "Listed on the Vampire Dance Practice battle page under the Brawler Prize Wheel (the page's wheel lists include Werewolf Cake Slice with 150 Coins). Wiki-only, unconfirmed; the Medic Prize Wheel heading is truncated in the wiki text.", "where": "Blackspore Swamp (Vampire Dance Practice battle)", "price": null, "currency": null, "source": "wiki page: Vampire Dance Practice; repo:notes/Build Guides/Content/Dungeons/Vampire Dance Practice.md:60 (same list, 'Werewolf Cake Slice' common to all six wheels)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Item name 'Werewolf Cake Slice' (locale 7336), description 'Full moon optional.' (locale 7337).", "source": "locale:7336; locale:7337"},
  {"claim": "Super Spooktacular dance-off reward is either a Vampire Cake Slice or a Werewolf Cake Slice, depending on winning team.", "source": "wiki page: Super Spooktacular"},
  {"claim": "Werewolf Cake Slice is listed on the Vampire Dance Practice wheels (Brawler Prize Wheel). The Werewolf Dance Practice page does NOT list it; it lists Vampire Cake Slice under the Archer Prize Wheel, so that page cannot support this item.", "source": "wiki page: Vampire Dance Practice; wiki page: Werewolf Dance Practice; repo:prototype/osfr-tools/data/content/dungeons/vampire_dance_practice.json:530"},
  {"claim": "Madam Zelda 'A Dark Future' quest panel names both cake slices, but no reward text was found, so it is not a reward source.", "source": "video:yWuHe_jYyc4/00190.jpg"}
 ],
 "confidence": 0.5,
 "open": [
  "Team-to-cake mapping (Werewolves win -> Werewolf Cake Slice) is inferred from the wiki's 'depending on which team wins' wording; no article states which team yields which slice.",
  "Event year unconfirmed, so retirement after that event is unknown.",
  "Prize-wheel membership is wiki-only; the exact wheel mapping is unconfirmed. Correction to prior answer: Werewolf Dance Practice lists Vampire Cake Slice, not Werewolf Cake Slice.",
  "No coin store price (no repo stores entry for item 16537), no vendor stock, no enemy drop, crafting, Station Cash, Coin Shop or membership source found. The '150 Coins' on dance-practice pages is a battle payout line, not a price.",
  "Prior answer's 'A Dark Future' quest source dropped: no reward text found. Cited locale 1417037571 does not exist.",
  "Critique cited quest-lines/schedules.json line 12307 for the team mapping; I did not verify that line, so it is not used as evidence."
 ]}
