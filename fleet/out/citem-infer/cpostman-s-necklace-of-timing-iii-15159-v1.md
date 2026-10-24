<!-- fleet job=citem-infer id=cpostman-s-necklace-of-timing-iii-15159-v1 status=done turns=5 usd=0.0049 tokens(read,write,in,out)=[47372, 20040, 12, 3898] model=claude-haiku-5-5 -->
# Postman's Necklace of Timing III

{"item": {"name": "Postman's Necklace of Timing III", "locale_id": 15159, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Reba, Postman gear merchant (ucdt 2169332063), sells the Certified Postman set plus Postman's Power Shard of Timing III, Necklace of Timing III and Ring of Talent III", "where": "Snowhill, near the Post Office", "price": "1055 coins (reference price; member price 949 coins, 10% member discount)", "currency": "coins", "source": "wiki page Reba (https://freerealms.fandom.com/wiki/Reba, 'Sells' section, revision 2013-10-09); repo:prototype/osfr-tools/data/content/vendors.json line 34544-34585 (stock_source Reba); repo:data/content/stores.json item 76512 (purchase_price_coins 1055); repo:notes/Build Guides/Content/NPCs/NPCs - Snowhill.md:107 (introduced 1 Oct 2013)"},
  {"type": "vendor", "detail": "Cliff, Postman gear merchant (ucdt 796158054), listed as selling the Postman's Necklace of Timing III alongside Priority Postman gear", "where": "near the Wugachug Postbox (Wugachug)", "price": "not stated by the wiki; store reference price 1055 coins (repo:stores.json item 76512)", "currency": "coins", "source": "wiki page Cliff ('Sells' list); wiki page Merchants; repo:notes/Build Guides/Content/NPCs/NPCs - Wugachug.md:81 (introduced 1 Oct 2013)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client defines the item as 'Postman's Necklace of Timing III', locale 15159, in the Postman Timing/Talent family (15154-15173), slot 8, class 3, definition id 76512", "source": "locale:15159; client definition in pack; locale 15154-15173 listing"},
  {"claim": "Reba sells Postman's Necklace of Timing III (wiki Reba 'Sells' list); Reba introduced in game with the 1 October 2013 update", "source": "wiki page Reba; lookup wiki page:ns0 Reba"},
  {"claim": "Cliff also lists the Necklace of Timing III in his sells list", "source": "wiki page Cliff; wiki page Merchants (Cliff found near Wugachug Postbox)"},
  {"claim": "Coin store price 1055 coins, member price 949, sell price 105; the store row is keyed by item id 76512", "source": "repo:data/content/stores.json item 76512 (line 17426); repo:prototype/osfr-tools/data/content/vendors.json line 34549"},
  {"claim": "Sibling items from the same Reba/Cliff/Newman/Clavin merchant sets are dated 1 Oct 2013, so the item is from the 2013 update, inside the 2009-2014 revival window", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Snowhill.md:107; NPCs - Wugachug.md:81"}
 ],
 "confidence": 0.7,
 "open": [
  "The 1055-coin price is a reconstructed reference (stores.json price_provenance kind 'reconstructed', from the legacy reference Cost and MemberDiscount), not a captured retail quote. The wiki gives no coin price for Reba or Cliff. Treat 1055 coins as unverified.",
  "The pack's coin_store_prices value 1055 is the price, not the store item id; the store row is item 76512.",
  "No wiki or article states when (or whether) Reba and Cliff stopped selling this necklace, so the retirement date is unknown. retired is null.",
  "Cliff's listing of this item is from the wiki only; no client or price source confirms it.",
  "No drop, quest reward, crafting, collection or prize-wheel source was found for this item in the pack's evidence.",
  "Clavin (Shrouded Glade, Global Postman set) sells Timing V, and Newman (Stillwater) sells Timing IV, not Timing III, so they are not sources for this item."
 ]}
