<!-- fleet job=citem-infer id=calpine-winterwear-gloves-4971-v2 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[5353, 10134, 6, 2280] model=claude-haiku-5-5 -->
# Alpine Winterwear Gloves

{"item": {"name": "Alpine Winterwear Gloves", "locale_id": 4971, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store vendor, NPC not named in our data (coin store price row for item 76604, tint group 1; sibling rows 79223 and 79224 for tint groups 2 and 3 are in the same store data)", "where": null, "price": "750 coins purchase (675 coins with 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 76604 (line 16227); item 79223 (line 16987); item 79224 (line 16988)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Alpine Winterwear Gloves' (locale 4971) with description 'Great for snowcapped mountains.' (locale 4972)", "source": "locale:4971; locale:4972"},
  {"claim": "Three client definitions (76604, 79223, 79224) share the name, glove model freestyle_<race>_f_hands_snowhillgloves.adr, slot 2", "source": "client definition pack (definition_ids 76604, 79223, 79224)"},
  {"claim": "Store data gives item 76604 a purchase price of 750 coins, 10% member discount (675 coins), sell price 75 coins, category 102, not marked no_sale", "source": "repo:prototype/osfr-tools/data/content/stores.json:16227"},
  {"claim": "Store row tags (L1, L2, L4, R2, T633, R1) are raw data only; the same tag set appears on rows with a different category and no sale price (76607, 76608 carry L3 tags), so they do not identify a vendor", "source": "repo:prototype/osfr-tools/data/content/stores.json:16220-16235"},
  {"claim": "Alpine Winterwear Gloves appears in the in-game gloves inventory list in a video frame, so it existed in play; the frame does not show a source", "source": "video:piWfe7lXZ9I/00108"},
  {"claim": "Sibling Winterwear gloves Subarctic is a Freestyle Jobs Hands item obtained from the Snow Days quest 'Silversnow's Sapling' or trade; this does not confirm the Alpine source", "source": "wiki: Subarctic Winterwear Gloves"},
  {"claim": "No wiki page, article, or other answer names Alpine Winterwear Gloves as a vendor, quest, drop, or promotion; the pack's vendor stock list is empty. The locale cluster (4966-4976) only groups names and gives no tier ordering, so no 'top of the set' claim is made", "source": "lookup wiki/articles/client; locale:4966-4976"}
 ],
 "confidence": 0.5,
 "open": [
  "The coin vendor NPC and zone are not named in our data; the vendor source rests only on the coin store price row, as the store data is the only price source. Needs the NPC and zone.",
  "No wiki price, sale price, or dated source confirms the 750-coin price is current.",
  "Not evidenced: Station Cash Marketplace, membership pack, prize wheel, or quest reward sources for Alpine. Not checked against the Snow Days quest reward list beyond the Subarctic page.",
  "Live status is unsure: the store row is undated and the video frame is undated.",
  "The first-pass 'vendor' guess is only a hint; the vendor claim rests on the price row alone.",
  "The 'top of the set' tier claim from the first answer was dropped as unsupported."
 ]}
