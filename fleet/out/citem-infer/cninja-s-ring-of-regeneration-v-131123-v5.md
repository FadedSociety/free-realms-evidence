<!-- fleet job=citem-infer id=cninja-s-ring-of-regeneration-v-131123-v5 status=done turns=4 usd=0.0026 tokens(read,write,in,out)=[21840, 9088, 10, 2460] model=claude-haiku-5-5 -->
# Ninja's Ring of Regeneration V

{"item": {"name": "Ninja's Ring of Regeneration V", "locale_id": 131123, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Hidden Dragon (Ninja job-item merchant, 'Sells' section, Soke Ninja row); wiki lists it by exact name", "where": "Shrouded Glade (top of mountain near Cooking Table)", "price": null, "currency": null, "source": "wiki page: Hidden Dragon (https://freerealms.fandom.com/wiki/Hidden_Dragon, Sells section, revision 2013-10-02); repo:prototype/osfr-tools/data/content/vendors.json:30156-30197"},
  {"type": "prize_wheel", "detail": "Ninja [Prize] Wheel (Ninja row), listed beside Ninja's Power Shard of Regeneration V and Battle Item Mystery Pack. Spin cost not stated on the wiki.", "where": "Mudshell dungeon", "price": null, "currency": null, "source": "wiki page: Mudshell (Ninja [Prize] [Wheel] section); repo:notes/Build Guides/Content/Dungeons/Mudshell.md:66"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 131123 is exactly \"Ninja's Ring of Regeneration V\", part of the Ring I-V family (131119-131123).", "source": "locale:131123"},
  {"claim": "Hidden Dragon wiki page is a Ninja job-item merchant introduced August 27, 2013, with a Sells section.", "source": "wiki page: Hidden Dragon"},
  {"claim": "Hidden Dragon Sells lists \"Ninja's Ring of Regeneration V\" (item 75379, name_id 131123), wiki revision 2013-10-02.", "source": "repo:prototype/osfr-tools/data/content/vendors.json:30156-30197 (stock_source = wiki Hidden Dragon)"},
  {"claim": "Mudshell wiki page has a Ninja [Prize] Wheel listing Ninja's Ring of Regeneration V beside Power Shard of Regeneration V and Battle Item Mystery Pack.", "source": "wiki page: Mudshell; repo:notes/Build Guides/Content/Dungeons/Mudshell.md:66"},
  {"claim": "Repo reference store row for item 75379: purchase 216 coins, member 194, sell 21, but price_provenance is 'reconstructed' with no captured NPC quote.", "source": "repo:prototype/osfr-tools/data/content/stores.json:17347"}
 ],
 "confidence": 0.5,
 "open": [
  "Coin price of 216 (member 194) is only a reconstructed repo reference (stores.json:17347; vendors.json price_basis says 'not captured NPC quote'). Not used as a sourced price; the vendor entry has price null until a live capture or wiki price confirms it.",
  "Mudshell wheel spin cost: the wiki's '10 Coins' figure under the Ninja wheel is unlabelled and was not used as a price. Confirm the spin cost before recording a price.",
  "Mudshell wheel and Hidden Dragon listing are both from 2013-era wiki revisions. No dated source confirms they are still live or that the item was retired, so live stays 'unsure' and retired is null.",
  "Hidden Dragon wiki excerpt did not show a price for this ring in the retrieved text; the full Sells table was not pulled.",
  "Client description is empty and no model files were listed, so tint variants and the slot 8 / class 2 kind were not verified; kind kept as 'other'.",
  "Prior answer's 'Crouching Tiger (Bristlewood)' stock claim was not re-verified and is not listed."
 ]}
