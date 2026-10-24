<!-- fleet job=citem-infer id=cyellow-snowball-134459-v1 status=done turns=6 usd=0.0059 tokens(read,write,in,out)=[72503, 27718, 14, 3498] model=claude-haiku-5-5 -->
# Yellow Snowball

{"item": {"name": "Yellow Snowball", "locale_id": 134459, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definitions 76629 and 76640 are both named Yellow Snowball (NameId 134459, DescriptionId 134566 'Snowball fight..?'). Type 1 (usable), class 69, SingleUse, NoSale, NonMiniGame, CategoryId 3, ActivatableAbilityId 5089 (76629) and a second definition with the same name/text. The item is a single-use throwable used in snowball fights.", "source": "FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json lines 1236778-1237010 (ids 76629, 76640); locale:134459; locale:134566"},
  {"claim": "The item's own description and ability are tied to the Snowball Fight minigame. Its NoSale and NonMiniGame flags mean it cannot be sold to vendors and is not a standard drop or store item.", "source": "FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json ids 76629/76640 flags; locale:134564 'Snowball fight!'"},
  {"claim": "Snowballs in the game come from Snowball Piles in Snowhill during Snow Days, and players scoop them up for snowball fights and the Abominable Snowman defense. The wiki says the piles are clickable and give snowballs, but does not name Yellow Snowball specifically.", "source": "https://freerealms.fandom.com/wiki/Snow_Days (wikitext freerealms-wiki/wikitext/2502-48701-940c11a846d2.wiki lines 31-38); https://freerealms.fandom.com/wiki/Abominable_Snowman"},
  {"claim": "Snow Days event content is a seasonal event in Snowhill; the 2010 and 2012 lists do not mention Yellow Snowball, and the Snow Days page lists only the Snowball Fight day and the snowball piles.", "source": "freerealms-wiki/wikitext/2502-48701-940c11a846d2.wiki lines 40-58, 81-116"},
  {"claim": "No coin store price (coin_store_prices is empty) and no coin vendor stock in the pack. The 120 'Cost' field is a client value, not a store price.", "source": "evidence pack; FreeRealms-Legacy ClientItemDefinitions.json id 76629 'Cost': 120"}
 ],
 "confidence": 0.3,
 "open": [
  "No acquisition source found. No wiki article, article fact, video frame, vendor stock or quest reward names Yellow Snowball. It is probably handed out by the Snowball Fight / Snowball Pile mechanic in Snowhill during Snow Days, but that is inferred, not documented. Verify against the Snowball Fight minigame code or Snow Days snowball pile tables before adding a source.",
  "Live status is unclear. The Snow Days event has run in several years (2009-2013 wiki notes) and the minigame text is still in the locale table, but the item is not confirmed as live or retired. The first-pass tag said live 'yes' with no evidence; treated as a hint only.",
  "Duplicate definitions: 76629 and 76640 share the name, description and class, and differ in icon. Confirm whether both are live variants (different tints or teams) or one is a leftover.",
  "The 'Cost' 120 field is a client value; it is not evidence of a coin store price.",
  "The client cluster items (Snowflake Fireworks, Tacky Sweaters, Gingerbread Cookie) are Snow Days gift-box items. Their sources are documented on the Snow Days wiki page, but no source for Yellow Snowball itself is shown there."
 ]}
