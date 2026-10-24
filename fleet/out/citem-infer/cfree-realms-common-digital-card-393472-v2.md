<!-- fleet job=citem-infer id=cfree-realms-common-digital-card-393472-v2 status=nothing_found turns=2 usd=0.0018 tokens(read,write,in,out)=[5391, 7476, 6, 1582] model=claude-haiku-5-5 -->
# Free Realms Common Digital Card

{"item": {"name": "Free Realms Common Digital Card", "locale_id": 393472, "kind": "card"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 393472 is 'Free Realms Common Digital Card' with sibling 393474 'Free Realms Foil Digital Card', so it is a rarity tier of a Trading Card Game card.", "source": "locale:393472; locale:393474"},
  {"claim": "Digital booster packs contain 10 game cards plus 1 virtual reward card that redeems for an in-game item. The text does not name the Common card or any rarity.", "source": "locale:150026; locale:5188; locale:4997 (Shattered Past says 8 game cards in one variant)"},
  {"claim": "The Free Realms [Digital] Booster Bundle (25 packs) lists 250 game cards and 25 virtual reward cards. It is a pack product, not a source named for this card.", "source": "locale:7968; locale:442422; wiki Items page"},
  {"claim": "No wiki page, article, video frame or coin vendor names 'Free Realms Common Digital Card'. The client definition 65834 has no coin store price, slots or models.", "source": "lookup (wiki/client/video) returned no direct hit; client definition in pack"},
  {"claim": "Locale 393470 is flagged as an internal dev name (BombSpawn01) and was removed as evidence.", "source": "id_check flag on locale:393470"}
 ],
 "confidence": 0.2,
 "open": [
  "Acquisition path unconfirmed. The likely route is as a game card inside TCG digital booster packs (Free Realms Digital Booster Pack, locale:150025/150026), but no source names this card, so it is not listed as a source.",
  "The Free Realms [Digital] Booster Bundle (25 packs, 5399 Station Cash per video:9NOkMosko1E/00024) is a related product only. It is not an evidenced acquisition source for this card.",
  "The price conflict is unresolved. articles/facts.json gives 200 SC for TCG booster packs, while video:1LjCvhboCkQ/00188 shows Heroes [Booster] Pack at 224 station_cash. I did not re-verify either figure, so no price is recorded.",
  "Drop rate of Common vs Foil cards per pack is unknown, and it is unknown whether the card was sold individually.",
  "Retired or unobtainable status of the digital packs is not established by any source here, so retired is null and live is unsure.",
  "Which TCG set (Free Realms, Shattered Past, Heroes, Baron von Darkcheat, fifth set) contains this card is unknown.",
  "Jev first-pass tag (live yes, source unknown) is only a hint and is not used as evidence."
 ],
 "critique_response": "Fixed: removed locale:393470 as evidence; moved the pack link and bundle from sources into open; removed the unverified 200 SC price claim as a source; flagged the 200 vs 224 SC discrepancy; kept live unsure and retired null.",
 "note": "Not wireable. Needs a source that names this card before any source is recorded."}
