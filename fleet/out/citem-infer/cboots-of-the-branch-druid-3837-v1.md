<!-- fleet job=citem-infer id=cboots-of-the-branch-druid-3837-v1 status=done turns=4 usd=0.0030 tokens(read,write,in,out)=[21112, 10168, 10, 3091] model=claude-haiku-5-5 -->
# Boots of the Branch Druid

{"item": {"name": "Boots of the Branch Druid", "locale_id": 3837, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale (Mysterious Merchant category, sold for coins; wiki sibling pages Pants/Tunic of the Branch Druid list the Mysterious Merchant as their sale channel). Boots themselves have no wiki page confirming the vendor.", "where": "Coin store (category 105)", "price": "450 coins (members 405 coins, 10% member discount)", "currency": "coins", "source": "repo:data/content/stores.json item 79322 (also 79323, 79324 for the other tints; purchase_price_coins 450, member_price_coins 405, sell_price_coins 45); wiki category [Mysterious] [Merchant] on Pants of the Branch Druid and Tunic of the Branch Druid pages"},
  {"type": "drop", "detail": "Item drop during the Shrouded Glade Invasion community event (sibling-set evidence: Hood, Glove, Tunic, Pants of the Branch Druid pages all say so; no Boots-specific page)", "where": "Shrouded Glade", "price": null, "currency": null, "source": "wiki: Pants of the Branch Druid; wiki: Tunic of the Branch Druid; wiki: Glove of the Branch Druid; repo:notes/Build Guides/Content/NPCs/NPCs - Shrouded Glade.md line 236"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Boots of the Branch Druid' is locale 3837; flavour text sits in the Branch Druid set (3832-3842).", "source": "locale:3837"},
  {"claim": "Three tint definitions (79322-79324) are in the coin store category 105 at 450 coins, member price 405 coins, sell price 45 coins, with source tags L1, L2, L4, R2, T633, R1.", "source": "repo:data/content/stores.json item 79322"},
  {"claim": "Sibling Branch Druid pieces (Pants, Tunic) are sold by the Mysterious Merchant and dropped during the Shrouded Glade Invasion.", "source": "wiki: Pants of the Branch Druid; wiki: Tunic of the Branch Druid"},
  {"claim": "Glove and Hood of the Branch Druid are Members Only items dropped during the Shrouded Glade Invasion.", "source": "wiki: Glove of the Branch Druid; wiki: Hood of the Branch Druid"},
  {"claim": "Shrouded Glade Invasion is a community event; the Branch Druid set is tied to it.", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Shrouded Glade.md line 236"}
 ],
 "confidence": 0.5,
 "open": [
  "No wiki page or article names Boots of the Branch Druid specifically; the drop and Mysterious Merchant sources are inferred from the sibling pieces of the same set.",
  "The stores.json entry does not name a vendor; the 'Mysterious Merchant' label comes from wiki category pages of sibling items, and its link to category 105 is not verified.",
  "Coin store price is 450 coins for the base; the wiki's sibling pages show a blank price, so no second wiki price confirms it.",
  "Retired status and the event date window are unknown; the event dates are not in the sources.",
  "Client lines 3834, 3836, 3838, 3840 are flagged as duplicates by flavour text; 3838 is tagged to this name, but the definitions count (3) is from 79322-79324, so the string-to-definition link is not confirmed.",
  "The Members Only status for Boots is not stated in any source; the Glove and Hood pages say Members Only, the Pants and Tunic pages do not."
 ]}
