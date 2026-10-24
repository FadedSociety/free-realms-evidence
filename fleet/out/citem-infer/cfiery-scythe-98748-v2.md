<!-- fleet job=citem-infer id=cfiery-scythe-98748-v2 status=done turns=2 usd=0.0024 tokens(read,write,in,out)=[5140, 12227, 6, 1690] model=claude-haiku-5-5 -->
# Fiery Scythe

{"item": {"name": "Fiery Scythe", "locale_id": 98748, "kind": "weapon"},
 "sources": [],
 "retired": true,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Fiery Scythe' is locale 98748; single definition 38187; item class 30; slot 7; model axe_ar_ag_weapon_jaggedscythe.adr", "source": "locale:98748"},
  {"claim": "Wiki: Fiery Scythe is a level 16 Ninja Blue Text weapon that 'can only be acquired through trade'", "source": "wiki page: Fiery Scythe"},
  {"claim": "Wiki page Fiery Scythe is in Category:Retired Weapons", "source": "wiki page: Fiery Scythe (categories)"},
  {"claim": "stores.json row for item 38187 (category 207) shows 1913 coins / member 1721 / sell 191, but the identical tuple appears on at least 9 other category 207 rows (37238, 37537, 37933, 38213, 38502, 38693, 38694, 38696, 38700, 38704) and on category 107 rows (35545, 35597, 35649). It is a shared price template, not an item-specific sale, so it is not used as a source.", "source": "repo:prototype/osfr-tools/data/content/stores.json items 38187 and the rows listed"},
  {"claim": "Wiki 'Blue Text weapon' list includes [Fiery] Scythe; no wiki page names a vendor, store, quest, drop or event that sells or gives Fiery Scythe", "source": "wiki page: Blue Text weapon"}
 ],
 "confidence": 0.35,
 "open": [
  "No evidenced acquisition source. The only wiki statement is 'can only be acquired through trade' (player-to-player), which is not one of the source types; recorded here rather than as a source.",
  "The coin-shop row (1913 coins) is a shared category price template and is rejected; the previous answer's coin_shop source is withdrawn. Confirm with a store listing or screenshot if one surfaces.",
  "Wiki 'Ninja' page lists '[Fiery] [Scythe]' under a 'Level 20' heading, while the Fiery Scythe page says level 16. Unresolved level conflict; the Ninja page text is not cited as a source.",
  "Retirement date unknown; 'Retired Weapons' category is the only retirement evidence. Live status unsure.",
  "Level/power/damage (level 16; Flame Flash 2372; Dragonstrike 10674) not cross-checked against the client definition.",
  "'Fighting Tiger Scythe' (98752) is a different item and was not merged.",
  "No vendor stock, quest reward, drop, event, or video evidence found for this item."
 ],
 "critique_fixes": "Evidence critique applied: removed coin_shop source; removed the unsupported 'Level 20' Ninja-page claim from evidence (kept as open conflict); sources empty; retired=true kept from wiki category."}
