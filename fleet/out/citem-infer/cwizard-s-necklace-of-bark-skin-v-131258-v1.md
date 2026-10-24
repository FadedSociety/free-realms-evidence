<!-- fleet job=citem-infer id=cwizard-s-necklace-of-bark-skin-v-131258-v1 status=done turns=5 usd=0.0039 tokens(read,write,in,out)=[33128, 14307, 12, 3648] model=claude-haiku-5-5 -->
# Wizard's Necklace of Bark Skin V

{"item": {"name": "Wizard's Necklace of Bark Skin V", "locale_id": 131258, "kind": "clothing"},
 "sources": [
  {"type": "prize_wheel", "detail": "[Wizard] Prize Wheel (Battle minigame prize wheel; the item is one of the wheel's listed prizes next to Battle Item Mystery Pack and Wizard jewelry/gear)", "where": "Bergram Stumpfinger's Ghost (wiki Battle page); also listed on Cray Caves, Tanglewood Fort and Falemicent wiki pages", "price": null, "currency": null, "source": "wiki pages 'Bergram Stumpfinger's Ghost', 'Cray Caves', 'Tanglewood Fort', 'Falemicent' (Wizard Prize Wheel lists containing \"[Wizard]'s Necklace of [Bark] [Skin] [V]\")"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name is locale 131258, \"Wizard's Necklace of Bark Skin V\", slot 8 / class 8 (jewelry), one definition (ID 75514).", "source": "client definition in task pack; locale:131258"},
  {"claim": "Wiki Battle-minigame pages list a [Wizard] Prize Wheel containing \"[Wizard]'s Necklace of [Bark] [Skin] [V]\".", "source": "wiki: Bergram Stumpfinger's Ghost; Cray Caves; Tanglewood Fort; Falemicent"},
  {"claim": "Our store data has a coin store row for item 75514 at purchase_price_coins 2152, member price 1936 (10% member discount), sell price 215. The row's price_provenance is 'reconstructed' from the Legacy reference Cost and MemberDiscount, with no captured retail NPC quote, so it is not confirmed as a live vendor sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json:17383"},
  {"claim": "Correction to the pack's mention: the 'Bergram Stumpfinger' entry called this an enemy drop from the prize wheel. The wiki source is a Battle minigame page's Wizard Prize Wheel list, not an enemy drop table. Bergram Stumpfinger's Ghost is the page title that lists the wheel; no enemy-drop evidence was found.", "source": "wiki: Bergram Stumpfinger's Ghost (page lists Wizard Prize Wheel); pack entry 'enemy Bergram Stumpfinger (final)'"},
  {"claim": "Sister items (Archer's and Brawler's Necklace of Bark Skin II/IV) have wiki pages saying they are sold at the Coin Shop; no wiki page was found for the Wizard V necklace.", "source": "wiki: Archer's Necklace of Bark Skin II; Brawler's Necklace of Bark Skin IV"}
 ],
 "confidence": 0.5,
 "open": [
  "Coin Shop: the store row for 75514 (2152 coins, 1936 member) is reconstructed from the Legacy reference, not captured from the live shop, and no wiki Coin Shop page names this item. Not listed as a source. Needs a live price check or a wiki Coin Shop citation.",
  "Prize wheel: the wiki pages give the number 'N Coins' next to each wheel list (e.g. 26, 77, 214). The pages do not say whether this is the wheel's spin cost or the coin reward, so no item price is taken from them.",
  "Drop-rate and wheel-odds data for this prize are not in the pack.",
  "Retired/live status: no source states retirement; the wiki lists it on wheels, but not with dates. Set live as 'unsure' and retired as null.",
  "The 'enemy drop' claim in the mentioned-by-other-answers entry was not supported and was replaced with the prize-wheel source above."
 ]}
