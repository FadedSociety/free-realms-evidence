<!-- fleet job=citem-infer id=cpristine-bottle-cap-20759-v3 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[18859, 13164, 8, 1849] model=claude-haiku-5-5 -->
# Pristine Bottle Cap

{"item": {"name": "Pristine Bottle Cap", "locale_id": 20759, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Old Bottle Caps collection (membership only; the item is a set member, not an acquisition source)", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:241-244 (name_id 20759 -> item_definition_id 11067); locale:20778 'Old Bottle Caps'; locale:132283; wiki List of Collections rev 27852, https://freerealms.fandom.com/wiki/List_of_Collections"},
  {"type": "drop", "detail": "Robgoblin Junk piles (Common tier, 'Various Robgoblin Junk' grouping, which lists Old Bottle Caps). Per-item drop chance and exact pile locations not documented; this is a grouping, not a confirmed item-level drop table", "where": "unknown (no zone named in any source)", "price": null, "currency": null, "source": "freerealms-wiki/wikitext/2038-27852-f0e36d086ea8.wiki lines 200-219 (wiki List of Collections rev 27852, 2013-07-13); articles fact:mechanic http://www.freerealms.com:80/article/detail.action?articleId=1757 (2010 Treasure Hunting Week: treasure can be found in Robgoblin Junk Piles)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Pristine Bottle Cap is client locale:20759 and maps to item_definition_id 11067 in the collection catalogue; definition 3977 is the other client id and is unresolved.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:241-244; locale:20759"},
  {"claim": "It is one of eight condition variants of the bottle-cap set (locale:20757-20764).", "source": "locale:20757-20764"},
  {"claim": "The Old Bottle Caps collection exists and is listed under Various Robgoblin Junk / Common on the wiki.", "source": "locale:20778, locale:20779, locale:132283; freerealms-wiki/wikitext/2038-27852-f0e36d086ea8.wiki lines 200-219"},
  {"claim": "Robgoblin Junk piles were a 2010 Treasure Hunting Week treasure source.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1757"},
  {"claim": "No coin store price, vendor stock, quest reward, enemy drop, event or prize-wheel source was found. Client coin_store_prices is empty.", "source": "client definition; repo search for 11067/20759 finds only the collection catalogue"}
 ],
 "confidence": 0.4,
 "open": [
  "Definition 3977 is unresolved; only 11067 is mapped to name_id 20759.",
  "The junk-pile source rests on a wiki grouping and a 2010 news post. Per-cap drop rate and exact pile locations are unknown.",
  "Latest dated evidence is the 2013-07-13 wiki snapshot. Live status and any later retirement are unknown; live is 'unsure' and retired is null. No retired or SC Marketplace listing was found in the sources checked.",
  "The 'Sunstone Valley' zone claim from the earlier answer is removed; no source names a zone."
 ]}
