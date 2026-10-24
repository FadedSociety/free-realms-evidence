<!-- fleet job=item-infer id=itwin-crescent-axe-v2 status=done turns=2 usd=0.0018 tokens(read,write,in,out)=[6865, 7848, 6, 1579] model=claude-haiku-5-5 -->
# Twin Crescent Axe

{"item": {"name": "Twin Crescent Axe (New School, Warrior weapon)", "locale_id": null, "kind": "weapon"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace listing for the New School Twin Crescent Axe. Wiki station_cash field lists 299 and 269; 269 is the Members 10% discount on the same listing, not a second offer.", "where": "Station Cash Marketplace (SC Marketplace)", "price": "299 Station Cash (regular); 269 Station Cash for Members (10% discount)", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Twin_Crescent_Axe (New School section; station_cash field [299, 269] — field order and the prose price are unverified; the prose price was stripped)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "The wiki page says Twin Crescent Axe names two Warrior weapons: a New School weapon sold through the SC shop and an Old School weapon previously sold through the SC shop.", "source": "https://freerealms.fandom.com/wiki/Twin_Crescent_Axe"},
  {"claim": "The New School version is described as acquired from the Station Cash Marketplace, with Members receiving a 10% discount.", "source": "https://freerealms.fandom.com/wiki/Twin_Crescent_Axe (New School section)"},
  {"claim": "Station cash values 299 and 269 appear in the wiki station_cash field; 269 equals 299 minus 10%.", "source": "https://freerealms.fandom.com/wiki/Twin_Crescent_Axe (station_cash field)"},
  {"claim": "Tooltip for the New School item shows Power 5, Resell Value 352, Required Warrior, Cannot Sell, Cannot Trade.", "source": "image:item_tooltip, File:New School Twin Crescent Axe item.jpg"},
  {"claim": "Ember Strike 254 at Level 1 and Ignite 3x 506 are wiki-prose effect values for the New School version.", "source": "https://freerealms.fandom.com/wiki/Twin_Crescent_Axe (New School effects)"},
  {"claim": "Client text 'Twin Crescent Axe' exists under locale ids 13092 and 386600; both read the same, and nothing in the pack maps either id to a specific version.", "source": "locale:13092, locale:386600"}
 ],
 "confidence": 0.6,
 "open": [
  "locale_id left null: 13092 and 386600 both read 'Twin Crescent Axe' and no id-to-version mapping was found.",
  "The 299 regular and 269 Members prices come from the station_cash field; the sentence price was stripped, so the pairing is inferred. Confirm against a live SC Marketplace listing.",
  "Retirement status of the New School version is unknown: the 'Retired Weapons' and 'Unobtainable Weapons' categories are page-wide and cover both versions. The New School text is in present tense, which suggests current sale, but this is unconfirmed.",
  "No coin vendor, quest reward, enemy drop, or event source found for the New School version in the pack.",
  "The Old School Twin Crescent Axe (Sweeping Slash 3391, Spinning Attack 6143) is a separate item and needs its own answer; the wiki says it was previously sold on the SC Marketplace and can no longer be acquired.",
  "Tooltip image text is truncated; the Ignite figure is supported only by the wiki prose."
 ]}
