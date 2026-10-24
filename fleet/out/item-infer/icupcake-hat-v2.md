<!-- fleet job=item-infer id=icupcake-hat-v2 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[6338, 6827, 6, 2230] model=claude-haiku-5-5 -->
# Cupcake Hat

{"item": {"name": "Cupcake Hat", "locale_id": 5167, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop version, members only, nontradable, sold during the Birthday Bash event (three color variations)", "where": "Coin Shop", "price": "333", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Cupcake_Hat (vendor_or_shop image caption 'Cupcake Hat 333 You take frosted tips to the extreme.' and infobox coins field, rev 47742; the wiki prose price is blank). Note: the same image also lists a 337-coin Hen Feather Archer Tunic, so the 333 mapping rests on the caption."},
  {"type": "quest_reward", "detail": "Quest 'Perfecting the Batter' (client locale 428059, exact title; the wiki names it as the Birthday Bash quest, and the video title 'Origin Of Cakenstein' is not the quest name). Blue-text version, one color, members only, nontradable.", "where": "Birthday Bash event", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Cupcake_Hat (Quest Version section); locale:428059. Reward not verified in repo quest tables."},
  {"type": "event", "detail": "Gifting Piñata, 2011 Birthday Bash. Tradable, wearable by non-members, several colors. Can no longer be acquired.", "where": "Birthday Bash event (2011)", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Cupcake_Hat (Gifting Piñata Version section)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name 'Cupcake Hat' is client text id 5167", "source": "locale:5167"},
  {"claim": "Coin Shop price 333 coins, from the vendor_or_shop image caption and infobox coins field", "source": "https://freerealms.fandom.com/wiki/Cupcake_Hat (image:vendor_or_shop; rev 47742)"},
  {"claim": "Quest title 'Perfecting the Batter' exists in client text as locale 428059", "source": "locale:428059"},
  {"claim": "Quest version is earned by completing 'Perfecting the Batter' during Birthday Bash", "source": "https://freerealms.fandom.com/wiki/Cupcake_Hat (Quest Version)"},
  {"claim": "Gifting Piñata version came from the 2011 Birthday Bash and can no longer be acquired", "source": "https://freerealms.fandom.com/wiki/Cupcake_Hat (Gifting Piñata Version)"},
  {"claim": "Coin Shop and quest versions are members-only and nontradable; the Piñata version is tradable and usable by non-members", "source": "https://freerealms.fandom.com/wiki/Cupcake_Hat"},
  {"claim": "Item tooltip (Freestyle Jobs, level 1, resell value 100; resell is not a purchase price) belongs to the Gifting Piñata version image 'Cupcake hat gifting pinata item.jpg'", "source": "image:item_tooltip on https://freerealms.fandom.com/wiki/Cupcake_Hat"},
  {"claim": "Birthday Bash event is the availability context", "source": "https://freerealms.fandom.com/wiki/Cupcake_Hat; another answer: event 'Birthday Bash' (open)"}
 ],
 "confidence": 0.5,
 "open": [
  "Retired is left null at item level: the wiki says only the Gifting Piñata (2011) can no longer be acquired. The Coin Shop and quest versions have no end date in the wiki, so their status is unknown.",
  "Live is 'unsure': no source confirms whether the Birthday Bash Coin Shop listing or the quest is still offered.",
  "The quest 'Perfecting the Batter' (428059) is confirmed as a client title only. The reward link, and the objective text ('Help Glerga at the Robgoblin Camp perfect her batter', locale 428060, cited in critique but not re-checked here), are not verified against repo quest tables.",
  "The Coin Shop price 333 is from an image caption, not the prose (which is blank). It is not verified against a repo vendor or Coin Shop table.",
  "Whether the Gifting Piñata version shares locale 5167 or has a separate item id is not verified. Its price is unknown; the wiki gives none.",
  "The 2011 Gifting Piñata drop is not checked against repo drop tables."
 ]}
