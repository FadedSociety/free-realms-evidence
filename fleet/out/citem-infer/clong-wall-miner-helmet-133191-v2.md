<!-- fleet job=citem-infer id=clong-wall-miner-helmet-133191-v2 status=done turns=3 usd=0.0020 tokens(read,write,in,out)=[12034, 7611, 8, 1843] model=claude-haiku-5-5 -->
# Long Wall Miner Helmet

{"item": {"name": "Long Wall Miner Helmet", "locale_id": 133191, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Boddington (pixie NPC merchant, Miner Job items; Miner Job update 15 October 2013 per the pack's notes, not re-verified)", "where": "Blackspore Crafting Station near the Haunted Mines, Blackspore Swamp", "price": "unknown (no captured NPC quote; the wiki Sells list gives no price in the pack)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Boddington (Sells section, revision 2025-03-14, listed as Long Wall Miner Helmet); repo:prototype/osfr-tools/data/content/vendors.json lines 1128-1152 (stock_source)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 76183, name locale 133191 'Long Wall Miner Helmet', slot 1, class 12.", "source": "client definition in pack; locale:133191"},
  {"claim": "Wiki Boddington page (pixie merchant at Blackspore Crafting Station, sells Miner Job items) lists Long Wall Miner Helmet in its Sells section.", "source": "https://freerealms.fandom.com/wiki/Boddington"},
  {"claim": "Repo vendor record for item 76183 cites the wiki Sells listing but says its price is a stores.json reference price, not a captured NPC quote.", "source": "repo:prototype/osfr-tools/data/content/vendors.json lines 1137, 1144-1152, 1163-1167"},
  {"claim": "Coin catalogue entry: purchase 902 coins, member 811 (10% discount), sell 90, category 101, tint group 1, source tags L1,L2,L4,R2,T633,R1.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 15879 (item 76183)"},
  {"claim": "Item 76183 also appears in vendors_unresolved.json line 672, so the vendor link is not fully resolved in the repo.", "source": "repo:prototype/osfr-tools/data/content/vendors_unresolved.json:672"}
 ],
 "confidence": 0.6,
 "open": [
  "The 902 coin price is a stores.json catalogue reference, not a Boddington quote. It is not listed as a vendor price; a Coin Shop or store listing for this item is not evidenced by any wiki or article source in the pack. Verify whether category 101 is the coin store before citing it as a coin_shop source.",
  "Boddington's actual coin price for the helmet is not evidenced; check the wiki Boddington table or an NPC capture.",
  "Retirement is unconfirmed: the Sells listing is dated 2025-03-14 (wiki revision) but no source says whether it is still sold now or was removed later. live is 'unsure', not the first-pass 'yes'.",
  "The 15 October 2013 Miner Job date cited in the prior answer was not re-verified here; the earlier pointer to Miner.md line 72 was not confirmed.",
  "No evidence of drops, quest rewards, or event sources for this helmet; vendors_unresolved.json lists the item, so the vendor mapping needs review.",
  "The prior answer's citation of 'NPCs - Blackspore Swamp.md row 89' was not checked in this pass."
 ]}
