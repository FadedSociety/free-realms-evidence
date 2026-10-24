<!-- fleet job=item-infer id=iballoon-bow-v1 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[4680, 5846, 6, 2710] model=claude-haiku-5-5 -->
# Balloon Bow

{"item": {"name": "Balloon Bow", "locale_id": 17871, "kind": "weapon"},
 "sources": [
  {"type": "prize_wheel", "detail": "Prize wheel reward from the Cakenstein Attacks! combat encounter during the annual Birthday Bash (Reward Version, level 16 Archer, Power 5)", "where": "Cakenstein Attacks! encounter (Birthday Bash)", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Balloon_Bow (wiki page text, Reward Version section; category Prize Wheel Weapons)"},
  {"type": "coin_shop", "detail": "Coin Shop version (Membership required, level 16 Archer; Cannot Trade); sold during the annual Birthday Bash; buyer must already own the Balloon Wand/Bow from the Cakenstein Attacks! encounter", "where": "Coin Shop", "price": "1936 coins (wiki coins field; the price sentence in the page text is blank, so verify)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Balloon_Bow (wiki page, Coin Shop Version section; categories Coin Shop Weapons, Coin Shop, Members Only)"},
  {"type": "other", "detail": "Gifting Piñata version (level 16 Archer, no effects listed); the Gifting Piñata was available during the 2011 Birthday Bash and can no longer be acquired", "where": null, "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Balloon_Bow (wiki page text, Gifting Piñata Version section)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Balloon Bow is a level 16 Archer weapon with three versions: prize wheel reward, Coin Shop, and Gifting Piñata.", "source": "https://freerealms.fandom.com/wiki/Balloon_Bow"},
  {"claim": "Name 'Balloon Bow' is client text id 17871.", "source": "locale:17871"},
  {"claim": "Coin Shop version costs 1936 coins per the wiki coins field.", "source": "https://freerealms.fandom.com/wiki/Balloon_Bow (coins field)"},
  {"claim": "Client tooltip text for the Coin Shop version says it requires owning the Balloon Bow from the Cakenstein Attacks! encounter.", "source": "locale:6792"},
  {"claim": "Reward version resell value 100; Coin Shop version resell value 193 (image tooltips).", "source": "https://freerealms.fandom.com/wiki/Balloon_Bow (images)"},
  {"claim": "Coin Shop version is marked Members Only and Cannot Trade.", "source": "https://freerealms.fandom.com/wiki/Balloon_Bow (image tooltip and page text)"},
  {"claim": "Reward version is also obtainable through trade (player-to-player, not a listed source).", "source": "https://freerealms.fandom.com/wiki/Balloon_Bow"}
 ],
 "confidence": 0.7,
 "open": [
  "Coin Shop price: the wiki coins field says 1936 but the page sentence giving the price is blank; confirm the price against another source.",
  "Contradiction: the wiki page's Coin Shop section and its item description say the buyer must own the 'Balloon Wand' from Cakenstein Attacks!, while the client text (locale:6792) says 'Balloon Bow'. Unresolved; the client text was used for the name here.",
  "Trade: the page says the reward version and Gifting Piñata version can be obtained through trade. Trade is player-to-player, so it is not listed as a source.",
  "Availability: the Coin Shop and prize wheel sources are tied to the annual Birthday Bash. The page does not say they were removed, so retired is left null and live is unsure. The Gifting Piñata source is marked as no longer obtainable.",
  "Gifting Piñata source has no price, and its detail says only the 2011 Birthday Bash, so the revival team must confirm its exact details.",
  "Event links from other answers (Birthday Bash entries) were not used as sources; they only give context for the prize wheel and Coin Shop sources."
 ]}
