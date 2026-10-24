<!-- fleet job=citem-infer id=cmother-s-day-bouquet-3074-v7 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[18088, 10489, 8, 2657] model=claude-haiku-5-5 -->
# Mother's Day Bouquet

{"item": {"name": "Mother's Day Bouquet", "locale_id": 3074, "kind": "weapon"},
 "sources": [
  {"type": "promotion", "detail": "Mother's Day redeem code ROSESFORMOM: a free bouquet of roses for all players, claimed through the Station Cash store's Claim window and placed in the weapon slot. One per account, no-trade.", "where": "Station Cash store, Claim window (redeem-a-code)", "price": "free with code", "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=80 (code and May 10-17, 2009 window confirmed by articles lookup, fact:event); wiki code table lines 64-65 per prior pack"},
  {"type": "marketplace", "detail": "Station Cash Marketplace listing of a Mother's Day bouquet variation (article 1370, May 6, 2010 update). Name-only candidate: the frame shows the name, not a definition id, so it is not confirmed as locale 3074.", "where": "Station Cash Marketplace", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=1370; video:Hu1ys1nYQRs/00742.jpg (reads 44 station_cash); video:Hu1ys1nYQRs/00778.jpg (reads 44 coins). Price 44 and currency are unresolved."}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Item name Mother's Day Bouquet is locale 3074.", "source": "locale:3074"},
  {"claim": "ROSESFORMOM code was redeemable between Sunday May 10 and Sunday May 17, 2009 for a bouquet of roses claimed in the Station Cash Claim window. The promotion is closed.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=80"},
  {"claim": "Article 1370 says four Mother's Day bouquet variations were added to the Marketplace with the May 6, 2010 update, with no price given.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1370"},
  {"claim": "Marketplace frames conflict on currency: 00742 reads 44 station_cash, 00778 reads 44 coins.", "source": "video:Hu1ys1nYQRs/00742.jpg; video:Hu1ys1nYQRs/00778.jpg"},
  {"claim": "Store data row: item 7307, category 12, purchase 25000 coins, member 22500, sell-back 2500, sale allowed. No vendor or store frame in the pack names where it is sold. Items 7308-7311 are no_sale at 540 coins.", "source": "repo:data/content/stores.json lines 1952-1956"},
  {"claim": "Client definition: slot 7 (weapon), class 1, model misc_ar_ag_weapon_roses.adr, six definitions (494, 7307-7311), name locale 3074.", "source": "client definition"},
  {"claim": "Inventory frame shows Mother's Day Bouquet owned and equippable in the weapon category. It confirms the item exists in play, not how it was acquired.", "source": "video:Qg7_4br2H80/00432.jpg"}
 ],
 "confidence": 0.5,
 "open": [
  "Retired status is split. The ROSESFORMOM promotion is closed (May 17, 2009). The Marketplace variations have no end date in any source, so the item-level retired flag stays null and live stays unsure.",
  "Marketplace currency is unresolved (station_cash vs coins across two frames), and the price 44 is not tied to a definition id. Article 1370 gives no price. A clearer store frame is needed.",
  "The 2009 code gift and the 2010 Marketplace bouquets may be separate items that share locale 3074. The schedule pack already excludes the Marketplace bouquets from the roses event (quest-lines/schedule-packs.json:42904).",
  "Store data row 7307 (25000 coins, category 12, stores.json line 1952) is an unverified data row, not a confirmed acquisition. No vendor, store frame or NPC in the pack sells it. It is tied to locale 3074 only through the client definition's name locale. It does not match the 44 Marketplace figure. Definitions 7308-7311 (540 coins) are no_sale and are not sources.",
  "No vendor or NPC in the pack stocks this item. Merry Vale Bouquet is a different item.",
  "Description locale 3075 is flagged dev_note and is not used as evidence.",
  "Kind is weapon because it is a weapon-slot cosmetic wieldable, not a combat weapon. 'other' is an acceptable alternative."
 ]}
