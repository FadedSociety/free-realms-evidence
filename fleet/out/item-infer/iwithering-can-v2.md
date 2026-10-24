<!-- fleet job=item-infer id=iwithering-can-v2 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[5054, 9174, 6, 2554] model=claude-haiku-5-5 -->
# Withering Can

{"item": {"name": "Withering Can", "locale_id": 436253, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Vending Machine on a player's farm (Freestyle Jobs Weapon slot item). This is a player-lot machine, not a town coin vendor; the buyer must own a Rank 1 Farm.", "where": "Player farm lot (Wilds Farm Vending Machine), not a town zone", "price": "2000 coins regular; 1800 coins member price (10% off), per the wiki coins field. Prose price fields are blank and the Vending Machine price table is an untranscribed image, so unverified.", "currency": "coins", "source": "wiki Withering Can (https://freerealms.fandom.com/wiki/Withering_Can, rev 47551: 'available for purchase through the Vending Machine'; coins field [2000,1800]); wiki Vending Machine (Equipment list includes Withering Can; price table is an image); locale:436278 ('*Must own a Rank 1 Farm to buy.')"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Name is locale 436253 'Withering Can'; description is locale 436278, which states the Rank 1 Farm purchase requirement.", "source": "locale:436253; locale:436278"},
  {"claim": "Item is a Freestyle Jobs, Level 1, weapon-slot item sold through the Vending Machine; the wiki lists it under Freestyle Jobs and Level 1 Weapons.", "source": "wiki Withering Can (categories and prose); image:item_tooltip (Required: Level 1, Freestyle Jobs)"},
  {"claim": "Item tooltip shows Resell Value 200 and states it cannot be traded.", "source": "image:item_tooltip for Withering Can (lookup [wiki] image 'Withering can item.jpg')"},
  {"claim": "Effects: Withering Spray shrinks another player; Withering Rain shrinks the user.", "source": "wiki Withering Can Effects section; locale:436235 ('Withering Spray'); locale:436973 ('Withering Rain')"},
  {"claim": "The item was part of the farming update that added Mega Growth Sprayer, Box of Bunnies, Cage of Crows, Vending Machine, Withering Can, Spider Sprayer, Fungal Sprayer, Wilds Tractor and Necrowart Zombie Buff. The update date is not given in the archive text.", "source": "wiki Template:News/Archive (update note)"},
  {"claim": "Farm unlocks promotion says the vending machine on the farm sells farmer items, including silly tools and farmer outfit.", "source": "wiki image:art_or_promo 'Rotator farm.png' (Farm Unlocks Are Here!)"},
  {"claim": "Sibling farm sprayers (Fungal Sprayer, Mega Growth Sprayer, Spider Sprayer) use the same Vending Machine, Freestyle Jobs, cannot-trade wording, which supports the sale mechanism.", "source": "wiki Fungal Sprayer; wiki Mega Growth Sprayer; wiki Spider Sprayer"}
 ],
 "confidence": 0.5,
 "open": [
  "Retirement is unknown. The pack cites only the add-news entry, with no removal evidence and no 'retired' category. Do not treat it as confirmed live or retired.",
  "Live status is unsure: no current listing, Coin Shop or SC Marketplace evidence was found.",
  "The 2000/1800 coin prices rest only on the wiki coins metadata field. The prose price is blank and the Vending Machine price table is an image that was not transcribed. Verify against that image or client data before relying on them.",
  "No update date is in the pack. The News/Archive entry gives the update contents without a date.",
  "The prior answer cited repo notes 'NPCs - Farnum Farmstead.md' (lines 27, 201) for the Wilds Farm vending machine. I could not re-verify that file in this pass, so treat that citation as unchecked.",
  "No quest reward, enemy drop, prize wheel or crafting source was found for this item in the pack. Those lines are not confirmed as absent."
 ]}
