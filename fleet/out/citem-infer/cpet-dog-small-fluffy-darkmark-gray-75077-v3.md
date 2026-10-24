<!-- fleet job=citem-infer id=cpet-dog-small-fluffy-darkmark-gray-75077-v3 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[19148, 13029, 8, 1918] model=claude-haiku-5-5 -->
# Pet: Dog: Small Fluffy: darkmark-gray

{"item": {"name": "Pet: Dog: Small Fluffy: darkmark-gray", "locale_id": 75077, "kind": "pet"},
 "sources": [
  {"type": "vendor", "detail": "Unidentified. Coin store price row only; no vendor file or wiki page names who sells this tint", "where": null, "price": "540 coins (member 486 coins, sell-back 54 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 23927 (line 6804, category_id null, tint_group_id 3, no price_provenance); client definition 23927 coin_store_prices [540]"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition 23927 is named 'Pet: Dog: Small Fluffy: darkmark-gray' (locale 75077), a dog pet on dog_small_fluffy.adr, with one coin store price of 540.", "source": "locale:75077; client definition 23927"},
  {"claim": "stores.json row for 23927 carries a plain 540-coin price with no price_provenance, so it was not reconstructed and no vendor is recorded.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 6804"},
  {"claim": "The 23903-23928 family is mixed. Most rows carry the plain 540 coin price, but siblings 23902 (Summer, 400 SC), 23906 (Barkley, 225 SC), 23912 (Taz, 225 SC), 23913 (Pavel, 225 SC), 23924 (Allie, 400 SC), 23929 (Dashes, 400 SC) and 23930 (York, 225 SC) are no_sale rows with null coin prices. Their provenance says no coin vendor stocks them, so the legacy 540 cost was cleared and they were reconstructed as Station Cash items from wiki pages.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 6779-6807"},
  {"claim": "Sibling dog tints 75067-75071 (solid-gold, solid-charcoal, solid-tan, solid-sand, solid-rusty) and 75072-75082 share this 'Pet: Dog: Small Fluffy' naming.", "source": "lookup client: locale:75067-75076; locale:75077 and cluster in pack"},
  {"claim": "Lookup for the exact name \"darkmark-gray\" and for 'Small Fluffy dog pet' found no wiki page, article or video frame naming this tint.", "source": "lookup wiki/articles/video, no matches"}
 ],
 "confidence": 0.35,
 "open": [
  "The 540-coin price is a bare store row with no vendor, category or wiki provenance. Treat it as an unvetted coin store price, not a confirmed coin vendor sale. The vendor and location are unknown.",
  "Because sibling dog-pet rows in the same block were reconstructed as Station Cash items (225 or 400 SC) with the 540 cost cleared, this row may be a legacy leftover. Whether 23927 is a coin item or a Station Cash item cannot be settled from the repo alone.",
  "Live status and retirement are unconfirmed. No dated source covers a sale or retirement for this tint.",
  "Quest rewards, enemy drops, events, promotions, membership, prize wheel and collection sources are not evidenced and are not listed.",
  "Wiki search for this tint's name returned nothing. A wiki page under the pet's own name (for example an SC Marketplace page) might exist for this tint and would settle the price and channel."
 ]}
