<!-- fleet job=citem-infer id=cchef-s-eggbeater-of-timing-ii-29522-v2 status=done turns=2 usd=0.0024 tokens(read,write,in,out)=[5840, 9361, 6, 2286] model=claude-haiku-5-5 -->
# Chef's Eggbeater of Timing II

{"item": {"name": "Chef's Eggbeater of Timing II", "locale_id": 29522, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Gaston (Chef job merchant). Wiki Gaston 'Sells' list includes Chef's [Eggbeater] [of] [Timing] [II]. No price on the wiki; the captured price is unknown.", "where": "Highroad Junction", "price": "unknown (store reference only: 850 coins, 765 member price)", "currency": "coins", "source": "wiki page Gaston (Sells, https://freerealms.fandom.com/wiki/Gaston, revision 2013-10-20); repo:prototype/osfr-tools/data/content/npcs/highroad_junction.json:4545 ('Prices unknown'); repo:prototype/osfr-tools/data/content/vendors.json:17790-17828 (price_basis: stores.json reference price, no captured NPC quote)"},
  {"type": "vendor", "detail": "Zamzani (pixie Chef merchant). Wiki Zamzani 'Sells' list includes Chef's [Eggbeater] [of] [Timing] [II]. No price on the wiki.", "where": "Wugachug", "price": "unknown", "currency": null, "source": "wiki page Zamzani (Sells; trivia: introduced in-game 1 Oct 2013); repo:prototype/osfr-tools/data/content/npcs/wugachug.json:19184"},
  {"type": "coin_shop", "detail": "Coin store data entry for item 75589 (category 107). Reference price only; the store/NPC it was sold at is not captured.", "where": null, "price": "850 coins (member price 765, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:15407 (item 75589 purchase_price_coins 850, member_price_coins 765)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name for locale 29522 is Chef's Eggbeater of Timing II, in the Chef tool family 29517-29527", "source": "locale:29522"},
  {"claim": "Wiki Gaston Sells list includes Chef's [Eggbeater] [of] [Timing] [II]", "source": "wiki page Gaston"},
  {"claim": "Wiki Zamzani Sells list includes Chef's [Eggbeater] [of] [Timing] [II]; Zamzani introduced 1 Oct 2013", "source": "wiki page Zamzani"},
  {"claim": "Gaston stock row says 'Prices unknown'; vendors.json labels 850/765 as a stores.json reference price with no captured NPC quote", "source": "repo:prototype/osfr-tools/data/content/npcs/highroad_junction.json:4545; repo:prototype/osfr-tools/data/content/vendors.json:17798"},
  {"claim": "Store data for item 75589: 850 coins, 765 member, sell 85", "source": "repo:prototype/osfr-tools/data/content/stores.json:15407"}
 ],
 "confidence": 0.5,
 "open": [
  "Price not captured from either NPC. The 850 coin (765 member) figure is a stores.json reference price, not attributed to Gaston or Zamzani; do not treat it as their sale price without a captured quote.",
  "Gaston and Zamzani both list the item on the wiki; the wiki gives no price for either. Which vendor(s) actually sold it, and whether both did, is not resolved.",
  "Retirement not documented in any source; live status unsure. Wiki vendor listings date to about the 1 Oct 2013 Chef update (Gaston revision 2013-10-20), so it was probably available then.",
  "Kind: client gives slot 7, class 21 and a tool model (tool_ar_ag_weapon_eggbeater.adr); it is a Chef job tool, so 'other'.",
  "No Station Cash, quest, drop, event, or crafting source found in the pack; not checked beyond the wiki vendor pages. The earlier citation of notes/Build Guides/Content/Jobs/Chef.md:331 was not re-verified and is not used here.",
  "The earlier citation 'repo:data/content/stores.json' was corrected to prototype/osfr-tools/data/content/stores.json:15407."
 ]}
