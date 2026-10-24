<!-- fleet job=citem-infer id=ckitty-viking-tunic-79662-v4 status=done turns=2 usd=0.0024 tokens(read,write,in,out)=[6100, 10074, 6, 2061] model=claude-haiku-5-5 -->
# Kitty Viking Tunic

{"item": {"name": "Kitty Viking Tunic", "locale_id": 79662, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Coin store sale, seller/store unknown: stores.json has a coin purchase row for item 24699 (category_id 6). No NPC or named shop is mapped to category 6 in the repo, and no wiki, article, video or other answer names an NPC for this item.", "where": null, "price": "270 coins (member price 243 coins, 10% member discount); sell-back 27 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 7522 (item 24699; verified by read)"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Kitty Viking Tunic' is locale 79662; description 'This is a Kitty Viking Tunic item.' is locale 150263; costume line 'The tunic for the kitty viking costume.' is locale 150616", "source": "locale:79662; locale:150263; locale:150616"},
  {"claim": "Store row for item 24699, category 6: purchase 270 coins, member 243 (10%), sell 27, no_sale false", "source": "repo:prototype/osfr-tools/data/content/stores.json line 7522"},
  {"claim": "Item 24704 has the same 270/243 purchase/member prices but no_sale true and sell_price null, so it cannot be sold back. Its purchase price is still listed", "source": "repo:prototype/osfr-tools/data/content/stores.json line 7527"},
  {"claim": "Items 24692-24717 (including 24699-24710 and 24711-24717) all share the same category-6 row shape at 270 coins, so the row shows a price for this definition but does not place it in a specific shop", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 7515-7540"},
  {"claim": "Set-mates Kitty Viking Leggings 80187, Outfit 72348, Helmet 80782 and Collar 81377 exist as client items with matching costume lines (locale 150278, 150294, 150311, 150632, 150648, 150666); no store check was done for them", "source": "locale:80187; locale:72348; locale:80782; locale:81377; locale:150278; locale:150294; locale:150311; locale:150632; locale:150648; locale:150666"},
  {"claim": "No wiki page, article or video names the Kitty Viking Tunic or costume", "source": "lookup (wiki, articles, video) for 'Kitty Viking'; no matches"}
 ],
 "confidence": 0.4,
 "open": [
  "Store category 6 is not mapped to a named shop, NPC or vendor in the repo. The 'coin vendor' type rests only on the coin price field (client coin_store_prices 270) and stores.json row 7522, so the vendor and location are unknown.",
  "Category 6 is shared by many items at the same 270-coin price (e.g. item 82 at stores.json line 79, and items 76, 2661, 2662, 2680, 2681), so the row does not prove this item sold in any particular store.",
  "Item 24704 is marked no_sale true with a 270 purchase price. The tag pattern L3,L3 on that row is unresolved.",
  "The 35 definitions were not all checked. Definitions 24699-24710 are the ones tied to this name in the pack; 24692-24698 and 24711-24717 are in the same category-6 block but were not confirmed as Kitty Viking variants.",
  "Set-mates' store rows were not checked, so it is unknown whether the tunic was sold as a set or in a promotion.",
  "Sale window, availability dates, and retirement are not stated by any source. retired is null.",
  "Source tags (L1, L2, L4, R2, T633, R1, L3) are unresolved codes.",
  "The previous answer's claim of a 24692-24703 block and the critique's 'vendor' label are corrected here: the source is typed as a vendor only in the sense of a coin-store price with an unknown seller."
 ]}
