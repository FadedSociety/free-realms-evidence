<!-- fleet job=citem-infer id=cbig-time-tournament-winnings-3293-v2 status=nothing_found turns=2 usd=0.0016 tokens(read,write,in,out)=[5477, 6987, 6, 1367] model=claude-haiku-5-5 -->
# Big Time Tournament Winnings

{"item": {"name": "Big Time Tournament Winnings", "locale_id": 3293, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 3293 is 'Big Time Tournament Winnings', one of eight sibling 'Tournament Winnings' item names (3288 Tiny, 3289 Extra Large, 3290 Small, 3291 Grand, 3292 Medium, 3294 Large, 3295 Champion's).", "source": "locale:3293; locale:3288-3295; lookup client hits for 'Tournament Winnings'"},
  {"claim": "Client definition 36994 has no coin store price; repo stores data has no entry for it. The description 'Worth 200 coins!' is the item's stated worth, not a sale price.", "source": "client definition (definition_ids [36994], coin_store_prices []); repo search for '36994' returned no store entry"},
  {"claim": "The only repo or video reference to the claim family names 'Extra Large Tournament Winnings', not Big Time. Frames show 'Extra Large [Tournament] [Winnings] Chatty Backpack' with 'Worth 200 coins!' (00042) and 'Worth 500 Coins REDEEMED' (00032), in a Claim / 'Redeem a Code!' window (00044).", "source": "video:jfcerhMCY6g/00042, video:jfcerhMCY6g/00032, video:jfcerhMCY6g/00044; repo:notes/Build Guides/Gameplay/Rewards and Collections.md:104"},
  {"claim": "The previous answer's source (promotion via code claim) is an inference from sibling names in the Extra Large frames. No record names Big Time Tournament Winnings as a code reward.", "source": "critique of previous answer; no wiki, article, or vendor record found"}
 ],
 "confidence": 0.1,
 "open": [
  "No source found. Big Time Tournament Winnings appears only as a client name; no wiki page, article, video frame, vendor, quest, drop, or repo record names it.",
  "The 'promotion / code claim' source was dropped. The claim window frames show Extra Large Tournament Winnings, not Big Time, so they do not evidence this item.",
  "The 'ugdt'/'ucdt' locale-file citation from the previous answer was not verifiable and is removed.",
  "The 'Worth 200 coins!' text is a description, not a price; the Extra Large frames show 200 and 500 coins, so the stated worth varies and is not a price.",
  "Possible sources to check: the Claim window (code redemption) for the Big Time name specifically, or TCG tournament prizes. Neither is verified."
 ]}
