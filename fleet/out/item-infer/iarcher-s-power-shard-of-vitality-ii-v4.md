<!-- fleet job=item-infer id=iarcher-s-power-shard-of-vitality-ii-v4 status=done turns=2 usd=0.0037 tokens(read,write,in,out)=[7040, 14618, 6, 3560] model=claude-haiku-5-5 -->
# Archer's Power Shard of Vitality II

{"item": {"name": "Archer's Power Shard of Vitality II", "locale_id": 130969, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop sale to all players", "where": "Coin Shop", "price": "806 coins (everyone); 725 coins for Members (10% discount)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Archer's_Power_Shard_of_Vitality_II (rev 32639); wikitext freerealms-wiki/wikitext/16818-32639-4672bc45b2d6.wiki:3 ('sells to everyone at price of {{Coin|806}} and to [[Members]] at the 10% discount price of {{Coin|725}}'); wiki categories 'Coin Shop', 'Coin Power Shards'"},
  {"type": "prize_wheel", "detail": "Archer prize wheel, Arachnia's Lair (dungeon)", "where": "Arachnia's Lair (dungeon)", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Dungeons/Arachnia's Lair.md:67; repo:prototype/osfr-tools/data/content/dungeons/arachnia_s_lair.json:786 (wiki-derived)"},
  {"type": "prize_wheel", "detail": "Archer prize wheel, The Mushroom Gigas (dungeon)", "where": "The Mushroom Gigas (dungeon)", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Dungeons/The Mushroom Gigas.md:64 (wiki-based table)"},
  {"type": "prize_wheel", "detail": "Archer prize wheel, Sweetwater Climb (dungeon); medium confidence, the lobby frame reads 'Archer's Treasure Shard of Vitality II'", "where": "Sweetwater Climb (dungeon)", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Dungeons/Sweetwater Climb.md:70 and :104 (conflict note); video l-KJnbZShSk/00018 cited there"},
  {"type": "prize_wheel", "detail": "Archer prize wheel, Robgoblin Creek (dungeon)", "where": "Robgoblin Creek (dungeon)", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Dungeons/Robgoblin Creek.md:62; repo:prototype/osfr-tools/data/content/dungeons/robgoblin_creek.json:673"},
  {"type": "prize_wheel", "detail": "Archer prize wheel, Robgoblin Treasure Trove (dungeon)", "where": "Robgoblin Treasure Trove (dungeon)", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Dungeons/Robgoblin Treasure Trove.md:87"},
  {"type": "prize_wheel", "detail": "Archer prize wheel, Pixie Hunters (dungeon)", "where": "Pixie Hunters (dungeon)", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Dungeons/Pixie Hunters.md:63; repo:prototype/osfr-tools/data/content/dungeons/pixie_hunters.json:737"},
  {"type": "prize_wheel", "detail": "Archer prize wheel, Den of Secrets (dungeon)", "where": "Den of Secrets (dungeon)", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Dungeons/Den of Secrets.md:69; repo:prototype/osfr-tools/data/content/dungeons/den_of_secrets.json:821"},
  {"type": "prize_wheel", "detail": "Archer prize wheel, Ice Troll Scout (dungeon)", "where": "Ice Troll Scout (dungeon)", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Dungeons/Ice Troll Scout.md:60 ([wiki]); repo:prototype/osfr-tools/data/content/dungeons/ice_troll_scout.json:641"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Archer's Power Shard of Vitality II' is locale 130969.", "source": "locale:130969"},
  {"claim": "Level 4 Archer power shard (Power 2), requires Level 4 Archer, increases health by 133 in combat.", "source": "https://freerealms.fandom.com/wiki/Archer's_Power_Shard_of_Vitality_II; image:item_tooltip in wiki pack"},
  {"claim": "Coin Shop price 806 coins for everyone, 725 for Members (10% discount). The rendered wiki text in the pack had dropped the numbers, but the raw wikitext at rev 32639 has them. The first critique's claim that the figures are unsupported is wrong.", "source": "freerealms-wiki/wikitext/16818-32639-4672bc45b2d6.wiki:3"},
  {"claim": "Archer wheel lists this item in Arachnia's Lair, The Mushroom Gigas, Sweetwater Climb, Robgoblin Creek, Robgoblin Treasure Trove, Pixie Hunters, Den of Secrets and Ice Troll Scout. Each is a repo dungeon note (wiki-derived) with the same Archer row.", "source": "repo notes listed in the prize_wheel sources above"},
  {"claim": "Sweetwater Climb's wheel has an 80 Coins slot and the Archer row matches the wiki and video frame, but the video frame's prize name reads 'Archer's Treasure Shard of Vitality II', so the row is medium confidence.", "source": "repo:notes/Build Guides/Content/Dungeons/Sweetwater Climb.md:66, :70, :104"},
  {"claim": "Resell value 80 is not an acquisition source.", "source": "image:item_tooltip in wiki pack"},
  {"claim": "Archer's Power Shard of Vitality III is a different item (not this one). The Vitality II wheel rows in the notes are separate from the III rows.", "source": "repo notes Snatching Snappers.md:66, Seaside Swoopers.md:66 and others"}
 ],
 "confidence": 0.7,
 "open": [
  "The Coin Shop price is confirmed by the rev 32639 wikitext, but it is a wiki figure, not a live client check. Current listing status is unknown.",
  "All prize-wheel sources come from repo dungeon notes that cite the wiki and video. No raw wiki wheel page was checked. Wheel cost, drop rate and whether the wheels are still live are unknown.",
  "The Sweetwater Climb wheel row relies on a frame that reads 'Treasure Shard' (medium confidence). It may be an OCR error.",
  "The Mushroom Gigas note lists 3832684316 as an example loc id. A critique says it is a ugdt id for the same name, not a conflicting name id. I did not verify this, so 130969 stays the name id.",
  "The Archer wheel list may be incomplete. Other dungeon notes not checked might also carry this item.",
  "No Station Cash price is listed, so no SC Marketplace source is added.",
  "No retirement date in the pack, so retired is null."
 ]}
