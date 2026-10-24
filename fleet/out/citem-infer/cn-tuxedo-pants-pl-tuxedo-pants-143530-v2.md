<!-- fleet job=citem-infer id=cn-tuxedo-pants-pl-tuxedo-pants-143530-v2 status=done turns=3 usd=0.0027 tokens(read,write,in,out)=[15669, 11486, 8, 2310] model=claude-haiku-5-5 -->
# {n}Tuxedo Pants{pl="Tuxedo Pants"}

{"item": {"name": "Tuxedo Pants", "locale_id": 143530, "kind": "clothing"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace, regular listing (legs slot, All Jobs, available to everyone)", "where": "SC Marketplace", "price": "99 (regular); 89 for Members (10% member discount)", "currency": "station_cash", "source": "freerealms-wiki/wikitext/10623-37221-e901fc9c162e.wiki line 2 ({{SC|99}} regular, {{SC|89}} Members); categories at lines 5 and 9 (Category:SC Marketplace, Category:SC Marketplace Clothing); FreeRealms-Legacy/src/Resources/StoreBundles.json line 14003 (Comment 'Tuxedo Pants', MemberDiscount 10)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Wiki page 'Tuxedo Pants' says it is an All Jobs legs-slot clothing item sold in the SC Marketplace to everyone at SC 99, and to Members at the 10% discount price of SC 89", "source": "freerealms-wiki/wikitext/10623-37221-e901fc9c162e.wiki line 2"},
  {"claim": "Wiki page is in Category:SC Marketplace and Category:SC Marketplace Clothing", "source": "freerealms-wiki/wikitext/10623-37221-e901fc9c162e.wiki lines 5, 9"},
  {"claim": "Client name string is locale:143530 '{n}Tuxedo Pants{pl=\"Tuxedo Pants\"}'; client name locale:151349 reads 'Tuxedo Pants'; the item has 36 client variants sharing the name", "source": "locale:143530; locale:151349; client definition pack"},
  {"claim": "A StoreBundles entry with Comment 'Tuxedo Pants' (NameId 143530, MemberDiscount 10) exists, launched 2009-12-06 and expiring 2040-08-15; its Price field (1) is not usable as a price", "source": "FreeRealms-Legacy/src/Resources/StoreBundles.json line 14003 ff."},
  {"claim": "Wiki page is tagged Category:Mysterious Merchant (lead only; no Cragara stock row found)", "source": "freerealms-wiki/wikitext/10623-37221-e901fc9c162e.wiki line 8; quest-lines/items.json (Cragara link unverified)"}
 ],
 "confidence": 0.7,
 "open": [
  "Price: wiki gives SC 99 regular and SC 89 for Members. Treat 89 as the sale/member price per the page's wording; the 10% discount is consistent with StoreBundles MemberDiscount 10.",
  "The wiki page carries {{Sunset Sale}} (line 11), so the marketplace sale window may be time-limited; the sale dates were not found, so current availability is unsure.",
  "Retired status not established: no source says it was removed. The Sunset Sale template and the 2040 ExpireTime in StoreBundles conflict as signals; live is unsure.",
  "Category:Mysterious Merchant is only a category tag. No Cragara stock row was found, so no Mysterious Merchant / Cragara source is listed.",
  "The 270 coin_store_prices value in the client definition is not tied to item id 143530 in any checked source; it is not listed as a coin vendor source.",
  "The client has 36 definitions (variants). Only the marketplace listing is evidenced; I did not verify that every variant is sold, and a second StoreBundles entry with Comment 'Tuxedo Pants' (line 34755) was not checked.",
  "No vendor stock, quest reward, enemy drop, or event evidence was found."
 ]}
