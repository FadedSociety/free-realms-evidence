<!-- fleet job=citem-infer id=cmutton-mash-242-v2 status=done turns=4 usd=0.0033 tokens(read,write,in,out)=[31007, 14286, 10, 2484] model=claude-haiku-5-5 -->
# Mutton Mash

{"item": {"name": "Mutton Mash", "locale_id": 242, "kind": "consumable"},
 "sources": [{"type": "marketplace", "detail": "Station Cash store bundle 'Mutton Mash' (StoreBundles Id 2219): 3 x GameItemId 581 via MarketingItemId 3006; the bundle's DescriptionId is 3153 (thirty-minute wolf text)", "where": "Station Cash store (Station Cash marketplace, StoreId 1)", "price": "180 Station Cash (wiki Items page; the bundle's own Price field is 1 and AltCurrencyPrice 1, which look like placeholders, so the 180 figure rests on the wiki)", "currency": "station_cash", "source": "repo:Sanctuary/src/Resources/StoreBundles.json:604-625 (Id 2219); freerealms-wiki/wikitext/2242-43382-0a935accf24e.wiki:604 ('Mutton Mash - {{SC|180}}')"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item name locale 242 is 'Mutton Mash'; the item has two client definitions (2947, 3006) sharing that name, slot 0, class 9.", "source": "locale:242; client definition ids 2947, 3006"},
  {"claim": "Store bundle Id 2219 has Comment 'Mutton Mash', NameId 242, DescriptionId 3153, StoreId 1, CurrencyType 1, Status 1, LaunchTime 2009-04-22, ExpireTime 2040-08-15, and grants 3 x GameItemId 581 via MarketingItemId 3006.", "source": "repo:Sanctuary/src/Resources/StoreBundles.json:604-625"},
  {"claim": "Locale 3153 reads 'Eating this food will change the player into a wolf for thirty minutes.' This is the bundle's description, so the duration is thirty minutes. Locale 3152 ('temporarily ... into a Wolf', no duration) is a different string and should not be used as the description.", "source": "locale:3153; locale:3152; repo:Sanctuary/src/Resources/StoreBundles.json:619"},
  {"claim": "The wiki Items page wikitext lists 'Mutton Mash - SC 180' in its food list.", "source": "freerealms-wiki/wikitext/2242-43382-0a935accf24e.wiki:604"},
  {"claim": "'Mutton Mash' appears as a Comment in ClientItemDefinitions in several community data sets, which confirms the item definitions, but these carry no price or acquisition source.", "source": "refs: Sanctuary/src/Resources/ClientItemDefinitions.json:54815, 56066"},
  {"claim": "The earlier pack's claim that no source names Mutton Mash was wrong: the store bundle and wiki price were missed.", "source": "critique of previous answer; repo:Sanctuary/src/Resources/StoreBundles.json:604"}
 ],
 "confidence": 0.6,
 "open": [
  "Live status is unverified. The bundle has Status 1 and a 2040 expiry, but the 2040 expiry looks like an open-ended placeholder. No retirement or delisting source was found, so retired is null and live is unsure.",
  "The 180 SC price comes only from the wiki. The bundle's Price field is 1 with AltCurrencyPrice 1, which conflicts. Treat the price as unconfirmed until a second source is found.",
  "Whether the wiki line sits under a 'Food and Drink' heading was not checked directly; only line 604 of the wikitext was confirmed.",
  "Which of the two definitions (2947 or 3006) is the one sold in the bundle is not established. MarketingItemId 3006 matches a definition id but may be a coincidence.",
  "The duration of the transform is given by the description (thirty minutes); the actual in-game effect was not checked against video or articles.",
  "Sanctuary's pack-style store entry also appears in the other community copies (Lxzxrus, Legacy, TCG-Files), but only the Sanctuary copy was read in full here."
 ]}
