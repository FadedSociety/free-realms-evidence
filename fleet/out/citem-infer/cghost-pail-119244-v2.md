<!-- fleet job=citem-infer id=cghost-pail-119244-v2 status=done turns=2 usd=0.0032 tokens(read,write,in,out)=[6761, 12615, 6, 3148] model=claude-haiku-5-5 -->
# Ghost Pail

{"item": {"name": "Ghost Pail", "locale_id": 119244, "kind": "other"},
 "sources": [
  {"type": "prize_wheel", "detail": "Medic Prize Wheel, Vampire Dance Practice (Super Spooktacular battle, boss Ed Sullenfangs; one wheel spin per job, 150 Coins slot plus 7 items)", "where": "Blackspore Swamp, Sinking Graveyard (Vampire Dance Practice)", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Dungeons/Vampire Dance Practice.md:66 (Medic row, tagged [wiki]); wiki page 'Vampire Dance Practice' prize wheel lists (partial snippet only: Archer wheel confirmed, Medic wheel not seen in the retrieved snippet)"},
  {"type": "prize_wheel", "detail": "Ninja Prize Wheel, Werewolf Dance Practice (Super Spooktacular battle, boss Jake Blackforest; one wheel per job)", "where": "Blackspore Swamp, Sinking Graveyard (Werewolf Dance Practice)", "price": null, "currency": null, "source": "wiki page 'Werewolf Dance Practice' 'Ninja Prize Wheel' list (retrieved snippet shows [Ghost] [Pail] with Jack-O-Lantern Sticker and Skeleton Paper Bag Mask, matching the Ninja row); repo:notes/Build Guides/Content/Dungeons/Werewolf Dance Practice.md:68. The three 'Sticker' items are mapped to client 'Stand-Up' names by inference, which does not affect the Ghost Pail row."},
  {"type": "vendor", "detail": "Unidentified coin store sale: stores.json row for item 69596 (category 107, sellable). No vendor/NPC mapping exists in the repo or wiki.", "where": null, "price": "50 coins (member price 45 coins, 10% member discount; sell-back 5 coins)", "currency": "coins", "source": "repo:data/content/stores.json item 69596 (line 14903); client definition coin_store_prices [50]"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Ghost Pail', locale 119244, description 'Keep your candy in this spooky pail.'; 35 definitions, first ids 69596-69607; slot 7; class 1", "source": "locale:119244"},
  {"claim": "Ghost Pail sits in the Halloween cluster with Skull Pail, Black Cat Pail, Jack-O-Lantern Pail, Witch Pail, Bat Pail, Face Paint Cards, Spectral Spectacles, Skull Lantern and Paper Bag Candy Carrier", "source": "locale:119239 through locale:119249"},
  {"claim": "Each Dance Practice battle has one prize wheel per combat job, each with a 150 Coins slot plus 7 Halloween items; the wheels only spawn during the October Super Spooktacular", "source": "wiki page 'Vampire Dance Practice' (Rewards, Mobs/Goals); wiki page 'Werewolf Dance Practice'; repo:notes/Build Guides/Content/Dungeons/Vampire Dance Practice.md:20,54"},
  {"claim": "Ghost Pail appears on the Ninja wheel of Werewolf Dance Practice and on the Medic wheel of Vampire Dance Practice", "source": "wiki page 'Werewolf Dance Practice' Ninja Prize Wheel list (snippet); repo:notes/Build Guides/Content/Dungeons/Werewolf Dance Practice.md:68 and Vampire Dance Practice.md:66"},
  {"claim": "Coin store row for item 69596: purchase 50 coins, member 45 (10% discount), sell 5, no_sale false", "source": "repo:data/content/stores.json item 69596"}
 ],
 "confidence": 0.5,
 "open": [
  "Coin store sale (50 coins): the stores.json row has no vendor, NPC or shop name, so the vendor and location are unknown. Only item 69596 is priced; definitions 69597-69607 have no store rows, so their sale status is unknown. Not a named live vendor.",
  "Whether the 50-coin sale is live or was Halloween-only is unresolved; no source states retirement. The wheel sources are event-seasonal (Super Spooktacular only), so current availability is unconfirmed. live stays 'unsure' and retired stays null.",
  "Medic wheel (Vampire Dance Practice) rests on the repo note line 66, which is tagged [wiki]; the retrieved wiki snippet showed the Archer wheel only, so the Medic row is not independently verified on the wiki.",
  "Ninja wheel (Werewolf Dance Practice): the wiki snippet confirms the item list order, but the wheel header was cut off in the retrieved text; the repo note line 68 supplies the Ninja label.",
  "Wheel odds and coin cost per spin are not stated by any source.",
  "Model misc_ar_ag_weapon_palewshovel.adr with slot 7 looks inconsistent with a pail; verify the client model before wiring the item's appearance or slot."
 ]}
