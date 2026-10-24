<!-- fleet job=citem-infer id=chasty-trot-skirt-5989-v2 status=nothing_found turns=5 usd=0.0039 tokens(read,write,in,out)=[36904, 15258, 12, 3233] model=claude-haiku-5-5 -->
# Hasty Trot Skirt

{"item": {"name": "Hasty Trot Skirt", "locale_id": 5989, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale:5989 'Hasty Trot Skirt'. Client definition: slot 4 (legs), class 3, model courier_<race>_f_legs_skirt.adr, 18 variant definitions, no coin store price in the pack.", "source": "locale:5989; client definition in pack"},
  {"claim": "The Hasty Trot set names exist in the client text (Skirt 5989, Shirt 6005, Hat 6024, Shorts 6045, Gloves 6015, Shoes 143 and 2969). This shows the names exist in the client locale, not that the items were obtainable.", "source": "locale:5989, locale:6005, locale:6024, locale:6045, locale:6015, locale:143, locale:2969"},
  {"claim": "The Postman-line neighbours (Amateur Postman Skirt 5985, Breakneck Mailing Skirt 5986, All-Star Postman Skirt 5988) are client names only. The wiki Postman vendor pages (Tipper, Cliff, Reba, Newman, Clavin, Kwan) list Express, Priority, Certified, Special, Global and Same Day Postman gear, not Hasty Trot.", "source": "locale:5985, locale:5986, locale:5988; wiki pages Tipper, Cliff, Reba, Newman, Clavin, Kwan"},
  {"claim": "repo stores.json holds a row {item_id 5989, category 6, purchase 270 coins, member 243, sell 27, tags L1 L2 L4 R2 T633 R1} at line 1530. It sits in an identical block of rows for item_id 5974 to 5990 (all 270 coins). The R1 tag marks unknown or defaulted values in the Coin Shop research note.", "source": "repo:prototype/osfr-tools/data/content/stores.json:1515-1531; repo:notes/Research/Coin Shop.md:33"},
  {"claim": "The stores row is treated as a defaulted placeholder, not a sale. The uniform block of 17 ids all at the same price and the R1 default tag do not give a sourced vendor. The 5989 match is also unproven because the definition ids in the client (2791 to 13377) do not include 5989 and the stores.json item_id space is not confirmed as locale ids.", "source": "repo:stores.json lines 1515-1531; repo:notes/Research/Coin Shop.md:33"},
  {"claim": "No wiki page, article, video frame, vendor stock row, quest reward, drop or event names Hasty Trot Skirt or any Hasty Trot piece. lookup for 'Hasty Trot' returns client locale hits only.", "source": "lookup 'Hasty Trot' (client, wiki, articles)"}
 ],
 "confidence": 0.1,
 "open": [
  "No sourced acquisition path. The stores.json row for item_id 5989 (270 coins) looks like a defaulted block (R1 tag, uniform 5974-5990 run). It should be confirmed as a placeholder or as a real vendor sale before any coin-vendor source is assigned. If the stores item_id space is the locale id space and the row is real, it would be a coin vendor candidate at 270 coins (member 243, sell 27), but this is unverified.",
  "The first-pass tag (live yes, source vendor) is a model guess with no evidence; it is discarded.",
  "Set membership and tier are not established. The Postman-line neighbours have no sourced vendor here either. Check the Postman job pages and the Postman minigame rewards for any Hasty Trot mention, and check a forum or wiki source for the set.",
  "Live status and retirement are unknown. The client defining the item shows it shipped in the client, not that it was obtainable.",
  "The earlier claim that 'Biggs Breakneck' is a Sunstone Valley Freewheeler was not re-checked and is dropped; it does not bear on the sources."
 ]}
