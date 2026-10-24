<!-- fleet job=item-infer id=iarcher-s-power-shard-of-vitality-ii-v3 status=done turns=4 usd=0.0044 tokens(read,write,in,out)=[35830, 18677, 10, 3354] model=claude-haiku-5-5 -->
# Archer's Power Shard of Vitality II

{"item": {"name": "Archer's Power Shard of Vitality II", "locale_id": 130969, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop sale to all players at 806 coins; Members get a 10% discount to 725 coins", "where": "Coin Shop", "price": "806 coins (everyone); 725 coins (Members)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Archer's_Power_Shard_of_Vitality_II (rev 32639); wikitext freerealms-wiki/wikitext/16818-32639-4672bc45b2d6.wiki line 3: 'acquired from the [[Coin Shop]] where it sells to everyone at price of {{Coin|806}} and to [[Members]] at the 10% discount price of {{Coin|725}}'. Categories: Coin Shop, Coin Power Shards, Marketplace Items."},
  {"type": "prize_wheel", "detail": "Archer prize wheel, Arachnia's Lair (dungeon); one of several per-job wheels", "where": "Arachnia's Lair (dungeon)", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/dungeons/arachnia_s_lair.json:786 (wiki-cited to notes/Build Guides/Content/Dungeons/Arachnia's Lair.md > Rewards > Prize wheel by job > Archer). Wiki-derived; no raw wheel page in pack."},
  {"type": "prize_wheel", "detail": "Archer prize wheel, The Mushroom Gigas (dungeon)", "where": "The Mushroom Gigas (dungeon)", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Dungeons/The Mushroom Gigas.md:64 (wiki-based prize-wheel table)"},
  {"type": "prize_wheel", "detail": "Archer prize wheel, Sweetwater Climb (dungeon)", "where": "Sweetwater Climb (dungeon)", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Dungeons/Sweetwater Climb.md:70 (wiki-based table; the note cites a lobby video frame l-KJnbZShSk/00018 for the wheel, and flags that frame's prize text as medium confidence, reading 'Treasure Shard' instead of 'Power Shard')."}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Archer's Power Shard of Vitality II' is locale 130969.", "source": "locale:130969"},
  {"claim": "Level 4 Archer power shard (Power 2), requires Level 4 Archer, increases health by 133 in combat.", "source": "https://freerealms.fandom.com/wiki/Archer's_Power_Shard_of_Vitality_II; image:item_tooltip in wiki pack"},
  {"claim": "Coin Shop price 806 coins for everyone, 725 for Members (10% discount), confirmed in the page wikitext at rev 32639 (the rendered text in the pack had dropped the numbers). Sibling Medic's Power Shard of Vitality II uses the same 806/725 pair.", "source": "freerealms-wiki/wikitext/16818-32639-4672bc45b2d6.wiki line 3; freerealms-wiki/wikitext/10351-32656-052357253276.wiki line 3"},
  {"claim": "Archer prize-wheel listing in Arachnia's Lair dungeon data.", "source": "repo:prototype/osfr-tools/data/content/dungeons/arachnia_s_lair.json:786"},
  {"claim": "Archer prize-wheel listing in The Mushroom Gigas notes.", "source": "repo:notes/Build Guides/Content/Dungeons/The Mushroom Gigas.md:64"},
  {"claim": "Archer prize-wheel listing in Sweetwater Climb notes.", "source": "repo:notes/Build Guides/Content/Dungeons/Sweetwater Climb.md:70"},
  {"claim": "Resell value 80 is not an acquisition source.", "source": "image:item_tooltip in wiki pack"}
 ],
 "confidence": 0.6,
 "open": [
  "Coin Shop price is now confirmed in the wikitext (806/725 at rev 32639), but it is a wiki figure, not a live client check. Current listing status is unknown.",
  "Prize-wheel sources rest on repo notes that cite the wiki; no raw wiki wheel page or video confirmation was checked. Drop rate, wheel cost, and whether the wheels are still live are unknown.",
  "Sweetwater Climb's lobby frame reads 'Archer's Treasure Shard of Vitality II' (medium confidence); this may be an OCR error, but it is unresolved.",
  "The Mushroom Gigas note gives example loc id 3832684316 for this item. A prior critique says that is a ugdt id for the same name, not a conflicting name id; I did not verify this. 130969 is the name id from the client lookup.",
  "The prior critique said refs/freerealms-wiki/harvest/lists/items.json shows price null for this item; I could not open that path, so this is unchecked.",
  "Category 'Marketplace Items' does not by itself show Station Cash or coin-marketplace sale; no station_cash price is listed, so no SC Marketplace source is added.",
  "No retirement or removal date in the pack; retired is null."
 ]}
