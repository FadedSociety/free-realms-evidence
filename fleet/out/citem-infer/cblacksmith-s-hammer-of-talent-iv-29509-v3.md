<!-- fleet job=citem-infer id=cblacksmith-s-hammer-of-talent-iv-29509-v3 status=done turns=3 usd=0.0023 tokens(read,write,in,out)=[15245, 9483, 8, 1998] model=claude-haiku-5-5 -->
# Blacksmith's Hammer of Talent IV

{"item": {"name": "Blacksmith's Hammer of Talent IV", "locale_id": 29509, "kind": "tool"},
 "sources": [{"type": "vendor", "detail": "Coin store sale; selling Blacksmith merchant not named. No wiki merchant row lists this hammer (Hess lists Talent IV tongs/ring and Timing IV tongs, not this hammer; Estus sells Hammer of Talent I, Keller sells Hammer of Talent V).", "where": null, "price": "1504 coins (purchase); member price 1353 coins (10% member discount); sell price 150 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75576 (line 15394); Blacksmith merchant table repo:notes/Build Guides/Content/Jobs/Blacksmith.md:188-194"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name for locale 29509 is Blacksmith's Hammer of Talent IV; definition 75576, slot 7, class 14, model tool_ar_ag_weapon_hammer.adr, one variant", "source": "locale:29509; client definition pack"},
  {"claim": "Coin store row for item 75576: category 107, purchase 1504 coins, member discount 10%, member price 1353, sell price 150, tags L1,L2,L4,R2,T633,R1 (re-verified in stores.json line 15394)", "source": "repo:prototype/osfr-tools/data/content/stores.json:15394"},
  {"claim": "Blacksmith merchant table lists Hammer of Talent I at Estus and Hammer of Talent V at Keller; no merchant lists Hammer of Talent IV", "source": "repo:notes/Build Guides/Content/Jobs/Blacksmith.md:188,194"},
  {"claim": "Wiki Hess page does not list the Hammer of Talent IV (lists Power Shard of Talen IV, Necklace of Timing IV, Ring of Talent IV, Tongs of Timing IV and Talent IV)", "source": "wiki page Hess (via Blacksmith.md:193)"},
  {"claim": "The 270-coin store row under item_id 29509 is a different definition sharing the locale id and is not attributed here", "source": "pack open note"},
  {"claim": "Wiki and video lookups for the exact name returned no page or frame; only the client text matched", "source": "lookup (client, wiki, video), quoted search"}
 ],
 "confidence": 0.4,
 "open": [
  "Selling merchant not identified: the coin store row is the only evidence, and the Blacksmith table does not name a seller for this hammer. Check Blacksmith merchant stock in-game before naming a vendor or zone.",
  "Live status unsure: the store row is present with tags L1,L2,L4,R2,T633,R1, but their meaning is not documented.",
  "Retirement unknown; no dated source.",
  "Level requirement for the Talent IV tier is not stated in any source.",
  "Earlier claim that Keller sells the Talent V hammer and Estus/Samune sell other hammers is only partly confirmed: Blacksmith.md confirms Estus (Hammer of Talent I) and Keller (Hammer of Talent V) and Samune (Hammer of Timing I)."
 ],
 "wireable": true}
