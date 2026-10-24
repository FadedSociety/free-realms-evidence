<!-- fleet job=citem-infer id=cbucket-of-bouncing-bait-17037-v1 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[3733, 9885, 6, 1653] model=claude-haiku-5-5 -->
# Bucket of Bouncing Bait

{"item": {"name": "Bucket of Bouncing Bait", "locale_id": 17037, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Bucket of Bouncing Bait' is locale 17037 (item, Seaside), with description 'Something smells fishy...' and definition id 9295, class 1, slot 0, no coin store price.", "source": "locale:17037; client definition in pack"},
  {"claim": "Item belongs to the Seaside Cray Castle quest cluster: quest objective \"Place Bucket o' Bait\" (locale:17036), quest title 'Cray Castle' (locale:17039), quest dialog 'Something smells fishy...' (locale:17038), and 'Place Sandcastle' (locale:17035). The item is placed as a quest objective, not sold.", "source": "locale:17035-17040"},
  {"claim": "Free Realms update notes of June 10, 2010 say the Bucket of Bouncing Bait was added and that it turns players who click it into a fish. No price, vendor or acquisition method is given.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1521"},
  {"claim": "The Darvon / Otis Pixie Woods strings (locale 17032-17034) sit in the same ID block but are a different quest; they do not name this item.", "source": "locale:17032-17034"},
  {"claim": "Repo search for 9295 / Bouncing Bait / Cray Castle found no vendor stock, store price (stores.json has no entry for this item), quest reward, drop or recipe for it.", "source": "repo search of notes/ and prototype/osfr-tools/data/content/"}
 ],
 "confidence": 0.3,
 "open": [
  "No acquisition source found. The item looks like a Cray Castle sandcastle quest/event item (placed via 'Place Bucket o' Bait') and was given out with the June 2010 Seaside update, but no quest reward, vendor, or drop naming it was found. Check the Cray Castle quest script in the repo for a reward or a grant step.",
  "The first-pass 'source_guess: unknown' is not confirmed. The sales and drops tags are empty.",
  "Retirement status is unknown. The article only shows the June 2010 addition; nothing says it was removed.",
  "Kind is set to consumable from the click-to-use behaviour and the first-pass tag. It is a quest or event trick item, so 'other' may be more accurate.",
  "No wiki page, images or video frames cover this item. No coin store price exists in our data."
 ]}
