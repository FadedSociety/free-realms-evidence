<!-- fleet job=item-infer id=isimple-dress-v2 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[16909, 12029, 8, 2330] model=claude-haiku-5-5 -->
# Simple Dress

{"item": {"name": "Simple Dress", "locale_id": 442549, "kind": "clothing"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace, sold to everyone as a Girls Only dress; Members get a 10% discount on the same listing", "where": "Station Cash Marketplace", "price": "349 Station Cash base price, UNVERIFIED (the wiki price text is blank in the pack; 349 is one of two SC values in the wiki's station_cash list, and the 10% Members price of 314 fits 349 x 0.9). Members price 314 Station Cash is also UNVERIFIED.", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Simple_Dress (Category:SC Marketplace, Category:SC Marketplace Clothing; text: 'available to everyone in the Station Cash Marketplace ... Members at the %10 discount'); repo:FreeRealms-Legacy/src/Resources/StoreBundles.json:30156 (Comment 'Simple Dress', Id 5600, NameId 442549, CurrencyType 1, StoreId 1, CategoryGroupId 51, MemberDiscount 10, Status 1, GameItemId 5591); the same row also exists in repo:Lxzxrus-Free-Realms-Server/src/Resources/StoreBundles.json:30362"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Simple Dress is a Girls only clothing item sold in the Station Cash Marketplace, with a 10% Members discount.", "source": "https://freerealms.fandom.com/wiki/Simple_Dress"},
  {"claim": "Client name for the item is 'Simple Dress', locale 442549.", "source": "locale:442549"},
  {"claim": "Store record: StoreBundles Id 5600 for Simple Dress, Station Cash (CurrencyType 1), MemberDiscount 10, Status 1, LaunchTime 2013-04-24, ExpireTime 2040-08-15. Its Price and AltCurrencyPrice fields are both 1, which are placeholders, so this row does not confirm 349 or 314.", "source": "repo:FreeRealms-Legacy/src/Resources/StoreBundles.json:30156-30185"},
  {"claim": "Simple Dress was introduced as one of three new dresses (with Pockets Dress and Skulls Dress) in a freerealms.com 'What is New?' post. The post gives no date.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2922"},
  {"claim": "A wiki user blog shows the Simple Dress in game (Pink), so it existed in play.", "source": "https://freerealms.fandom.com/wiki/User_blog:Soe_amnerys/Dresses_Are_Here"}
 ],
 "confidence": 0.5,
 "open": [
  "The wiki price text is blank in both the pack and the live lookup. The 349 base and 314 Members prices are unverified. Do not treat them as confirmed until a revision with the price text is found.",
  "The earlier draft listed the 314 Members price as a second marketplace source. It is one listing with a member discount, so it is merged into one source here.",
  "The StoreBundles row gives a launch date of 2013-04-24 and an expiry of 2040-08-15. It was found in the FreeRealms-Legacy and Lxzxrus repos, not in a Sanctuary PC2009 file. The launch date is the store-record introduction date. The article's own post date is still unknown.",
  "The 2040 expiry looks like a far-future placeholder, so it does not prove the item is still sold. No source in the pack gives a retirement date or a current listing, so retired is null and live is 'unsure'.",
  "The user blog's in-game screenshot claim was not checked against the blog text beyond the lookup excerpt, which does show the Pink Simple Dress caption.",
  "No vendor, quest, drop, event, crafting, or prize-wheel source for Simple Dress appears in the pack or repo searches. Only the Station Cash Marketplace source is evidenced."
 ],
 "critic_fixes": "Evidence critic: prices marked unverified, and the blog claim is noted as existence only. World critic: single marketplace source, store row cited with its real repo path, placeholder price fields noted, launch date added, and the 2040 expiry is flagged as a likely placeholder.",
 "id_check": "locale 442549 confirmed as Simple Dress; StoreBundles NameId 442549 matches."}
