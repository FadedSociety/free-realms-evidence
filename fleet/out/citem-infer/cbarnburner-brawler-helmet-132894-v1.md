<!-- fleet job=citem-infer id=cbarnburner-brawler-helmet-132894-v1 status=done turns=2 usd=0.0034 tokens(read,write,in,out)=[3691, 16566, 6, 2586] model=claude-haiku-5-5 -->
# Barnburner Brawler Helmet

{"item": {"name": "Barnburner Brawler Helmet", "locale_id": 132894, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Evander, Brawler Job merchant (introduced 6 August 2013, replaced Ned); sells the six-piece Barnburner Brawler set, including the Helmet", "where": "Mire's Edge campfire near Donovan Shadeweaver's home, Blackspore Swamp", "price": "752 coins (purchase); 676 coins for members (10% member discount)", "currency": "coins", "source": "repo:data/content/stores.json item 75886 (purchase_price_coins 752, member_price_coins 676); repo:prototype/osfr-tools/data/content/vendors.json:1818-1832 (Evander stock incl. 75886); wiki page Evander; repo:notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md:88"},
  {"type": "prize_wheel", "detail": "[Brawler] Prize Wheel, a dungeon prize wheel (one Brawler-specific head piece per dungeon wheel); listed on the Vale of the Ancients wiki page", "where": "Vale of the Ancients (dungeon)", "price": "202-304 coins per wheel spin as listed on the dungeon pages (price of the Helmet itself not stated)", "currency": "coins", "source": "wiki page Vale of the Ancients (\"[Brawler] Prize Wheel: [Barnburner] [Brawler] Helmet\"); repo:prototype/osfr-tools/data/content/dungeons/vale_of_the_ancients.json:1024, 2328"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client definition: name 'Barnburner Brawler Helmet', locale 132894, definition 75886, slot 1 (head), class 25, model brawler_<race>_<gender>_head_footballhelmetspiked.adr", "source": "locale:132894; FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:1222425-1222426"},
  {"claim": "Coin store row for item 75886 at 752 coins, member price 676, sell price 75, source tags present", "source": "repo:data/content/stores.json:15643 (item 75886)"},
  {"claim": "Evander sells exclusively Brawler job items, including the Barnburner Brawler Helmet", "source": "wiki page Evander; repo:prototype/osfr-tools/data/content/vendors.json:1818-1832"},
  {"claim": "Brawler Prize Wheel at Vale of the Ancients lists the Barnburner Brawler Helmet", "source": "wiki page Vale of the Ancients"},
  {"claim": "Barnburner set is the Brawler bonus clothing set for dungeon wheels/rewards (Croaking Vale video shows Barnburner Brawler Shoulderpads won from the Battle Item Mystery Pack/minigame)", "source": "video:dOauCv91EFw/00246; repo:notes/Build Guides/Content/Dungeons/Croaking Vale.md:59"},
  {"claim": "Other pieces of this set (Jacket, Boots, Gloves, Pants, Shoulderpads) are also sold by Evander and appear on dungeon Brawler wheels, consistent with the helmet", "source": "wiki pages Evander, Treeleaf's Retreat, Prince of Low Tide!, Stealthy Despoilers"}
 ],
 "confidence": 0.8,
 "open": ["The pack's 752 coin price is confirmed in stores.json, but no wiki page gives a price for Evander's helmet specifically; the Evander wiki entry was cut off before any price list.",
  "Retired status is not stated by any source. Evander is listed as a live merchant and the store row exists, so live is marked yes, but a later removal date was not checked.",
  "Vale of the Ancients wheel prices (202/238 coins) are wheel-spin costs, not the helmet's price; the helmet's own wheel odds were not found.",
  "The Evander wiki page and the Blackspore notes both say Evander 'replaced Ned'; the 6 August 2013 date is from the repo notes only, not a wiki or article source.",
  "Video evidence for this helmet specifically was not found; only the shoulderpads and jacket appear in video frames."]}
