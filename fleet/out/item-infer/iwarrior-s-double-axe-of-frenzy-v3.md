<!-- fleet job=item-infer id=iwarrior-s-double-axe-of-frenzy-v3 status=done turns=3 usd=0.0027 tokens(read,write,in,out)=[15343, 9749, 8, 2562] model=claude-haiku-5-5 -->
# Warrior’s Double Axe of Frenzy

{"item": {"name": "Warrior's Double Axe of Frenzy", "locale_id": 132023, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Marius, 'Sells' section (wiki stock row; repo stock_source is the Marius wiki page, rev 2013-10-08)", "where": "Marius (NPC vendor); wiki category 'Coin Shop' is the label on the item page", "price": "1504 coins (wiki coins field; repo stores.json reference price, not a captured NPC quote)", "currency": "coins", "source": "wiki page Marius (lookup hit lists the axe under Sells); repo:prototype/osfr-tools/data/content/vendors.json:12349-12390 (item_id 75139, stock_source Marius, price_basis '(R) stores.json reference price'); wiki page Warrior’s Double Axe of Frenzy (coins field [1504], categories Coin Shop, Coin Shop Weapons)"},
  {"type": "prize_wheel", "detail": "Warrior Prize Wheel (spin reward)", "where": "Moldy Shamblers!", "price": null, "currency": null, "source": "wiki page Moldy Shamblers! (lookup hit lists 'Warrior Prize Wheel' with the axe); wiki page Warrior’s Double Axe of Frenzy ('prize wheels at Moldy Shamblers!'); wiki category Prize Wheel Weapons"},
  {"type": "prize_wheel", "detail": "Warrior Prize Wheel (spin reward)", "where": "Vale of the Ancients", "price": null, "currency": null, "source": "wiki page Vale of the Ancients (lookup hit lists 'Warrior Prize Wheel' with the axe); wiki page Warrior’s Double Axe of Frenzy ('prize wheels at ... Vale of the Ancients'); wiki category Prize Wheel Weapons"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Level 12 Warrior weapon, Power 4, Crushing Blow and Frenzy effects, resell value 150", "source": "wiki item tooltip image: Warrior’s Double Axe of Frenzy item.jpg; wiki page Warrior’s Double Axe of Frenzy"},
  {"claim": "Name matches client text", "source": "locale:132023"},
  {"claim": "Axe is listed in the Marius page's Sells section", "source": "wiki page Marius (lookup snippet, Sells list)"},
  {"claim": "Marius stock row: purchase 1504, member 1353, sell 752, but price basis is a stores.json reference, not a captured NPC quote", "source": "repo:prototype/osfr-tools/data/content/vendors.json:12349-12390"},
  {"claim": "Wiki coins field 1504; the wiki price sentence is blank in the page text", "source": "wiki page Warrior’s Double Axe of Frenzy (rev 34619)"},
  {"claim": "'68 Coins' (Moldy Shamblers!) and '202 Coins' (Vale of the Ancients) sit beside the Warrior Prize Wheel heading; these are wheel spin costs, not the axe's price", "source": "wiki pages Moldy Shamblers! and Vale of the Ancients (lookup snippets)"}
 ],
 "confidence": 0.6,
 "open": [
  "The 1504 price is an unverified reference value: the wiki coins field and repo stores.json reference agree, but no captured in-game NPC quote supports it. The member price 1353 and sell price 752 are repo-only reference values and are omitted from the source price.",
  "The wiki 'Coin Shop' label is not tied to Marius by any source beyond the Marius Sells listing (2013-10-08 revision); the Marius link is the best-supported coin source, and the Coin Shop label is treated as the wiki's category name.",
  "Current availability is unconfirmed: no source states whether Marius still sells the axe, whether the Coin Shop listing is current, or whether the prize wheels still include it. Retired is null for that reason.",
  "Wiki category 'Marketplace Items' is present, but there is no SC Marketplace category or Station Cash price, so no Station Cash source is recorded.",
  "Prize wheel per-spin cost and per-wheel odds are not in the pack; price is null for both wheel sources. The 68 and 202 Coins figures are wheel spin costs, not item prices.",
  "The repo moldy_shamblers.json and vale_of_the_ancients.json entries derive from the same wiki build guide, so they are not independent confirmation of the wheel sources."
 ]}
