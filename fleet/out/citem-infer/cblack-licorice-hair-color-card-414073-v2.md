<!-- fleet job=citem-infer id=cblack-licorice-hair-color-card-414073-v2 status=done turns=3 usd=0.0033 tokens(read,write,in,out)=[17553, 17049, 8, 2084] model=claude-haiku-5-5 -->
# Black Licorice Hair Color Card

{"item": {"name": "Black Licorice Hair Color Card", "locale_id": 414073, "kind": "card"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name string for the item is locale:414073 'Black Licorice Hair Color Card'; the description says it allows you to change your hair color (a hair-color style card).", "source": "locale:414073"},
  {"claim": "Nothing in the repo maps item id 35968 or 68835 to locale:414073. A repo-wide search for 35968 and 68835 hits only stores.json:7901 and unrelated vendors.json hash lines, so the 'client definition (item 35968 matches stores.json)' link in the previous answer is unverified.", "source": "search: repo for '35968|68835'"},
  {"claim": "stores.json row item 35968 is category 142, purchase 180 coins, member price 162 coins (10% member discount), sell_price null, no_sale true. Rows 35950-35977 are identical, so the row does not identify this card.", "source": "repo:prototype/osfr-tools/data/content/stores.json:7883-7910"},
  {"claim": "Wiki and video frames show Hair Color style cards sold in the Coin Shop at 162 coins in the October 2013 Super Spooktacular period (Gold Rush, Atomic Blast, Sun Kissed, Shock Wave). Black Licorice is not named in those frames. The 162-coin price matches the member price in the store row, so it is a family-level pattern only.", "source": "video:1xtVveaQ3XI/00112.jpg; video:1xtVveaQ3XI/00116.jpg; wiki page 'Super Spooktacular'"},
  {"claim": "The wiki has pages for other hair-color cards from the same 2013 batch (Snowstorm, Pumpkin, Ectoplasm, Bubblegum, Phantasm Blue, Grape Frosting). None covers Black Licorice.", "source": "wiki page 'Super Spooktacular'; lookup File: pages for Snowstorm, Pumpkin, Ectoplasm, Bubblegum"}
 ],
 "confidence": 0.2,
 "open": [
  "No source ties locale:414073 to any store, vendor, quest, drop or event. The previous 'vendor' source is withdrawn: it rests on an unverified id match (item 35968) and on a run of identical rows.",
  "Possible Coin Shop hair-card sale at 180 coins (member 162) in store category 142 is plausible from stores.json:7901 and the 162-coin Coin Shop frames, but it is unconfirmed. Need the item id-to-name table (or a store-category name) to confirm 35968 = Black Licorice.",
  "Second definition 68835 has no store row and no source. Unknown whether it is a tint or race variant.",
  "The category 142 vendor/NPC and zone are not named in any source checked (vendors.json not matched).",
  "Retirement, current availability and whether 180 coins was the launch price are unknown. Live status stays 'unsure'.",
  "Source for 'coin_store_prices: 180' in the client definition was not reproduced in this pack; treat as unverified."
 ]}
