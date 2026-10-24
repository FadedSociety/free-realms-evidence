<!-- fleet job=item-infer id=idomo-hat-v3 status=done turns=2 usd=0.0018 tokens(read,write,in,out)=[5543, 7419, 6, 1616] model=claude-haiku-5-5 -->
# Domo Hat

{"item": {"name": "Domo Hat", "locale_id": 8428, "kind": "clothing"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace, All Jobs Head-slot clothing. Sold to everyone at one Station Cash price; Members get a 10% discount on the same listing (folded into this single source, not a separate path).", "where": "Station Cash Marketplace (SC Marketplace)", "price": "Two tiers, 89 and 99 Station Cash (standard vs. Members 10% off). Which figure is standard is unconfirmed: the wiki price sentence is blank; the station_cash field lists [99, 89]. Likely 99 standard / 89 Members, but unverified.", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Domo_Hat (station_cash field [99, 89]; text 'available to everyone in the Station Cash Marketplace ... to Members at the 10% discount price'; categories SC Marketplace, SC Marketplace Clothing, Marketplace Items)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Domo Hat is an All Jobs Head-slot clothing item sold in the Station Cash Marketplace, with a Members 10% discount", "source": "https://freerealms.fandom.com/wiki/Domo_Hat"},
  {"claim": "Client name string for the Domo Hat is locale 8428", "source": "locale:8428"},
  {"claim": "A Domo hat was added as Domo-themed clothing in a 2010 update (article dated August 2010 in the pack; the exact day is not checked)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1730"},
  {"claim": "A Domo hat was released as clothing in the same update (German and French article notes)", "source": "http://www.freerealms.com/article/detail.action?articleId=1734"},
  {"claim": "Re-check: the wiki page text in the live lookup still has the prices blank, so the price order cannot be confirmed from the wiki; repo search found no Domo hat vendor, recipe, or drop entry (only a Domo NPC and poster models)", "source": "lookup wiki page:ns0 Domo Hat; repo search 'Domo'"}
 ],
 "confidence": 0.4,
 "open": [
  "Price order unverified: 89 vs 99 Station Cash as the standard price rests only on the station_cash field order. Confirm against an archived or live SC Marketplace listing before treating 99 as standard.",
  "No coin vendor, quest, drop, crafting, or prize-wheel source found. The 2010 update articles name the hat but not the shop; no vendor_stock or quest data in the pack.",
  "The 'Promotional' wiki category is unexplained; the item may have been limited-time. Retired is null: no sale window or removal notice in evidence.",
  "Whether the Domo Hat is still sold on the Station Cash Marketplace today is unverified (live: unsure).",
  "Critique 1 and 2 concerns addressed: price no longer asserted as 99 for everyone; member price folded into one marketplace source; article date softened to 'August 2010 update'."
 ]}
