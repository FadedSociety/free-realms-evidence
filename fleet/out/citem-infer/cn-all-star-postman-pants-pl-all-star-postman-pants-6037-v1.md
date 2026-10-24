<!-- fleet job=citem-infer id=cn-all-star-postman-pants-pl-all-star-postman-pants-6037-v1 status=done turns=11 usd=0.0103 tokens(read,write,in,out)=[249200, 39097, 24, 5916] model=claude-haiku-5-5 -->
# {n}All-Star Postman Pants{pl="All-Star Postman Pants"}

{"item": {"name": "All-Star Postman Pants", "locale_id": 6037, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Unidentified Postman gear merchant (coin store entry for item 1767, store category 104; no NPC named in any source)", "where": null, "price": "715 coins (member price 643 coins; sell-back 71 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 1767 (line 524); client definition Cost 715 in refs FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json Id 1767"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item 1767 is 'All-Star Postman Pants', NameId 6037, slot 4 (legs), class 3, model courier_<race>_m_legs_pants.adr, dyetint tintable, MinProfileRank 15, NoTrade true", "source": "locale:6037; refs FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json lines 34426-34440"},
  {"claim": "Our store data lists item 1767 in category 104 at 715 coins, member 643 coins, sell 71 coins, with source tags L1, L2, L4, R2, T633, R1", "source": "repo:prototype/osfr-tools/data/content/stores.json item 1767 (line 524)"},
  {"claim": "Sibling Amateur Postman Pants (item 1766, NameId 6036) is in the same store category 104 at 291 coins; the Same Day Postman Pants (76014) is a reference price of 1076 coins at Kwan", "source": "repo:prototype/osfr-tools/data/content/stores.json line 523; repo:prototype/osfr-tools/data/content/vendors.json lines 11436-11470"},
  {"claim": "All-Star Postman set (pants, hat, jacket, skirt, gloves, shoes, shards) exists as a client set with no merchant recorded in the wiki-derived build notes", "source": "repo:notes/Build Guides/Content/Jobs/Postman.md lines 221-228 (section 'Other client armour sets with no merchant in the wiki'; All-Star Postman pants listed as 2760120177)"},
  {"claim": "Kwan (Briarwood) sells only the Same Day Postman set (added 1 Oct 2013), not the All-Star set, so Kwan is not a source for this item", "source": "wiki page Kwan (Sells list); repo:prototype/osfr-tools/data/content/vendors.json line 11301"},
  {"claim": "Wiki Postman merchants (Tipper, Newman, Clavin, Kwan, Reba, Walt, Wake, Arel, Ferd, Cliff) are each tied to one set; none is recorded selling All-Star pants", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md:98, NPCs - Stillwater Crossing.md:68, NPCs - Shrouded Glade.md:111, NPCs - Briarwood.md:209, NPCs - Snowhill.md:107, NPCs - Seaside.md:129, NPCs - Sanctuary.md:91, NPCs - Merry Vale.md:140, NPCs - Greenwood Forest.md:202"}
 ],
 "confidence": 0.4,
 "open": [
  "No NPC or wiki page names a seller for All-Star Postman Pants. The only source is the coin store price (715 coins) in stores.json, which the rules count as a coin vendor sale, but the seller is unknown.",
  "Price conflict risk: the wiki-derived Postman.md lists All-Star Postman Pants as definition 2760120177 and other wiki ids; the client definition here is 1767. Confirm the id mapping before crediting the 715-coin price to this exact item.",
  "Whether the All-Star set was ever sold at Kwan, Newman, Clavin or another merchant is unverified; the pack's 'Postman' merchant list does not include it.",
  "Live status: store data carries live-era source tags (L1, L2, L4, R2, T633, R1), but no dated wiki or article evidence confirms sale, retirement, or the Oct 2013 Postman launch for this piece. Retired status is unknown.",
  "Sell-back (71 coins) and member price (643 coins) come from stores.json only; no wiki price confirms them.",
  "Quest rewards, drops, events, prize wheel, and collections were not found for this item. The Postman job quest line (quests/postman.json) was not checked for All-Star rewards."
 ]}
