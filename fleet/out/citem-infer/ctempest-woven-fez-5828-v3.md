<!-- fleet job=citem-infer id=ctempest-woven-fez-5828-v3 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[6263, 9156, 6, 2248] model=claude-haiku-5-5 -->
# Tempest Woven Fez

{"item": {"name": "Tempest Woven Fez", "locale_id": 5828, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store listing for item definition 1612 (tint group 1). Stocking NPC not named in our data; store category 101 is not named in stores.json", "where": "coin store (category 101)", "price": "715 coins purchase (member price 643 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 482 (item_id 1612, category_id 101, purchase_price_coins 715, member_price_coins 643)"},
  {"type": "coin_shop", "detail": "Coin store listing for item definition 12099 (tint group 3). Stocking NPC not named in our data; store category 101 is not named in stores.json", "where": "coin store (category 101)", "price": "715 coins purchase (member price 643 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 3403 (item_id 12099, category_id 101, purchase_price_coins 715, member_price_coins 643)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Tempest Woven Fez' is locale 5828; item class 8, head slot 1, model caster_<race>_<gender>_head_fez.adr, 15 definitions", "source": "locale:5828; client definition in pack"},
  {"claim": "stores.json item 1612 (tint group 1, category 101) is listed at 715 coins purchase, 643 member price; source_tags L1,L2,L4,R2,T633,R1", "source": "repo:prototype/osfr-tools/data/content/stores.json line 482 (re-read and confirmed)"},
  {"claim": "stores.json item 12099 (tint group 3, category 101) is listed at 715 coins purchase, 643 member price", "source": "repo:prototype/osfr-tools/data/content/stores.json line 3403 (re-read and confirmed)"},
  {"claim": "Item 1614 (tint group 2) shows 9453 coins purchase / 8507 member, the same price as untinted listings 1609, 12067, 12096, 12126 (tint_group null). It is a shared price, not evidence of this fez's price, so it is dropped from sources and listed under open.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 479, 483, 3399, 3402, 3405"},
  {"claim": "Lookup of wiki, articles, video and client finds no page, facts or video for Tempest Woven Fez; only locale 5828 and sibling locale 25996 'Elite Black Tempest Woven Fez' match", "source": "lookup (wiki, articles, video, client)"}
 ],
 "confidence": 0.4,
 "open": [
  "No vendor NPC, zone or vendor_stock row names who sells definitions 1612 or 12099. The sources are coin store rows only; 'coin_shop' is used as the closest type and the 'Coin Shop' wiki category is not confirmed for category 101.",
  "Item 1614 (tint group 2) is a possible listing for this fez, but its 9453-coin price is shared with untinted listings and is unverified. Not used as a source.",
  "The other definitions (1614 and the rest of the 15 in definition_ids, including 12100-12108, 12111, 12114, 12115) do not appear in the checked store rows with a verified link to this fez. Their sources are unknown.",
  "No wiki, article, video or quest/drop/event/prize-wheel/crafting source found. Quest, drop, event, prize-wheel and crafting sources are unknown.",
  "Retired status is unconfirmed. Store rows carry live source tags with no retirement date or removal shown, so live is 'unsure' rather than 'yes'.",
  "The collection catalogue claim (ids 1612/1614 as collection entries) was not re-verified and is not used as a source.",
  "Client description is empty."
 ]}
