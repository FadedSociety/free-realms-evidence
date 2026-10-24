<!-- fleet job=item-infer id=ired-s-haven-v1 status=nothing_found turns=2 usd=0.0017 tokens(read,write,in,out)=[2874, 9015, 6, 1127] model=claude-haiku-5-5 -->
# Red's Haven

{"item": {"name": "Red's Haven", "locale_id": 8793, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Red's Haven is a location, not an item: the wiki infobox type is 'Crafting station' in Rumble Ridge, Sunstone Valley, and the page says it is 'a crafting station set-up behind Wheelie Pete's'.", "source": "wiki: Red's Haven (rev 50139)"},
  {"claim": "The client text entry is a place name (type place, Sunstone Valley), not an item name.", "source": "locale:8793"},
  {"claim": "Red's Haven is the location where the Sunstone crafting-station NPCs stand (Red Stonehammer, Fry, Kallie, Broheim Backfire). Those NPCs are the sellers, not the item source.", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Sunstone Valley.md#Part B. Red's Haven and the Sunstone crafting station"}
 ],
 "confidence": 0.9,
 "open": [
  "The pack asks for an item's acquisition sources, but 'Red's Haven' is a map location with no price, coin, or Station Cash listing. No source was assigned.",
  "If an item was meant (for example a station-linked item like the Sunstone Anvil, locale/client id 134615320, or Sunstone Forge, 1839029274), the pack needs to be re-issued with that item's name.",
  "The wiki Fry/Kallie/Broheim vendor rows are in repo:prototype/osfr-tools/data/content/npcs/sunstone_valley.json (lines around 2883-3034) and are unresolved; they are not item sources for this location."
 ]}
