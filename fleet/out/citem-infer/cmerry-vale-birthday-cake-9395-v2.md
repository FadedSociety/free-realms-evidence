<!-- fleet job=citem-infer id=cmerry-vale-birthday-cake-9395-v2 status=done turns=2 usd=0.0029 tokens(read,write,in,out)=[6685, 13638, 6, 2322] model=claude-haiku-5-5 -->
# Merry Vale Birthday Cake

{"item": {"name": "Merry Vale Birthday Cake", "locale_id": 9395, "kind": "consumable"},
 "sources": [
  {"type": "marketplace", "detail": "One of eight zone-themed Birthday Cake items (Shrouded Glade, Seaside, Snowhill, Merry Vale, Sanctuary, Wugachug, Blackspore Swamp, Briarwood) sold for the Birthday Bash event; buying all eight unlocks the bonus Boss Cake", "where": "SC Marketplace (Birthday Bash event)", "price": "unverified (no per-item price found)", "currency": "station_cash", "source": "wiki page 'Cake' (\"eight cakes available from the SC Marketplace during the Birthday Bash event... When the player collects all of the cakes, they unlock the Boss Cake\"); articles summary articleId=2107 (\"party items sold on the Marketplace, and eight zone-specific birthday cakes plus a bonus Boss Cake for buying all eight\"); locale:9391 category 'Birthday Cake Samples'"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 9395 'Merry Vale Birthday Cake', one definition (7969), class 168, slot 0, no models, no coin store price; no entry in repo stores data", "source": "locale:9395; repo:prototype/osfr-tools/data/content/stores.json (no match)"},
  {"claim": "Wiki 'Cake' page: eight cakes sold on the SC Marketplace during the Birthday Bash; collecting all eight unlocks the Boss Cake", "source": "wiki page 'Cake'"},
  {"claim": "Article 2107 summary: party items sold on the Marketplace; eight zone-specific birthday cakes plus a bonus Boss Cake for buying all eight", "source": "http://www.freerealms.com/article/detail.action?articleId=2107"},
  {"claim": "Collect-all-eight objective text confirms the set and Boss Cake reward", "source": "locale:14419"},
  {"claim": "Birthday Bash also had a Cakenstein boss event and the Birthday Cake Bake-off (Diggy, Camellia); the cake is event context, not a per-item drop", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Seaside.md:179; repo:notes/Build Guides/Content/NPCs/NPCs - Sanctuary.md:132; wiki page 'Events'"},
  {"claim": "Wiki Boss Cake pages (Cakenstein, Abominable Snowman, Stone Heart, Pumpkin Prince) describe Boss Cake as a Birthday Bash Station Cash Marketplace item", "source": "wiki pages 'Cakenstein', 'Abominable Snowman', 'Stone Heart', 'Pumpkin Prince'"}
 ],
 "confidence": 0.5,
 "open": [
  "Station Cash price for the single Merry Vale cake not found; the wiki gives no per-cake price. Only the Boss Cake and cakes as a set were checked.",
  "Which Birthday Bash year sold this set is unconfirmed (2010, 2011 or 2012). Article 2107's post date was not verified, and the wiki's cake-hat and bake-off notes point to the 2012 (third anniversary) party. Article 1267 and 2100 were not checked.",
  "Whether the cake was sold for Station Cash only or also as a bundle/other currency was not verified.",
  "Retired/unobtainable status is not stated by any source checked; the Birthday Bash is a past limited event, so live is marked unsure rather than no.",
  "No source says the cake was handed out as a party item; the earlier 'event handed out' source was removed as unsupported.",
  "Locale 17806 'Merry Vale Birthday Cake Sample' is flagged placeholder and is excluded as evidence; the 17803-17810 Sample strings are not treated as this item.",
  "Identity of 9395 with the collectible set is inferred from the 'Birthday Cake Samples' category (locale:9391) and the locale:14419 objective, not from a per-item source.",
  "No drop, quest reward, crafting or vendor source found for this cake."
 ]}
