<!-- fleet job=citem-infer id=cbriarwood-collector-s-card-413964-v1 status=done turns=4 usd=0.0040 tokens(read,write,in,out)=[30637, 18733, 10, 2700] model=claude-haiku-5-5 -->
# Briarwood Collector's Card

{"item": {"name": "Briarwood Collector's Card", "locale_id": 413964, "kind": "collection"},
 "sources": [
  {"type": "other", "detail": "TCG Virtual Reward card from a Trading Card Game booster pack (Virtual Rewards are cards that hold an item; each booster pack gives one). Exact TCG set for this card not confirmed; the Briarheart Bandage Square Shard, which sits next to it in the client and in the video collection list, is a TCG series 2 virtual reward.", "where": null, "price": null, "currency": null, "source": "wiki Virtual Reward; wiki File:Briarheart bandage square shard tcg.png; video:eS3bRs9fR5k/00038.jpg and /00020.jpg (card shown in the Collection > Virtual Rewards window beside TCG cards)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name and description: 'Briarwood Collector's Card', 'This card gives you access to a unique collection!' (locale 413964 item; 413963 npc_dialog text).", "source": "locale:413964; locale:413963"},
  {"claim": "Item is defined in the client with item class 1, slot 0, no models, and no coin store price, so no coin vendor sells it.", "source": "client definition (definition_ids 68808); repo search found no store entry"},
  {"claim": "Virtual Rewards are TCG cards that contain virtual reward items, obtained through Trading Card Game Booster Packs, one reward per pack.", "source": "wiki page 'Virtual Reward'"},
  {"claim": "The card appears in the in-game Collection window under Virtual Rewards, next to TCG cards (Fly, Chuck a Mug, Snaggletooth) and other rewards such as Doggy Island Sunglasses and Doberman Whistle.", "source": "video:eS3bRs9fR5k/00038.jpg; video:eS3bRs9fR5k/00020.jpg"},
  {"claim": "The Virtual Rewards window says players can redeem virtual rewards on their character and open packs from the Collection.", "source": "video:jfcerhMCY6g/00024.jpg; video:eS3bRs9fR5k/00016.jpg"},
  {"claim": "Physical TCG packs are no longer produced, so virtual-reward TCG items are unobtainable in new packs.", "source": "wiki Rocker Pants (wording: 'physical TCG packs, which are no longer produced')"},
  {"claim": "The Doggy Vinegolem Chest, Legs, Hat and Collar sit in the same client id block (413965-413968), which suggests they are a set tied to this card. This is only an id-order guess.", "source": "client_cluster locale:413965-413968"}
 ],
 "confidence": 0.35,
 "open": [
  "The first-pass guess 'quest_reward' is not supported. No quest, enemy drop or vendor was found that gives this card.",
  "No wiki page exists for this card. The TCG set, the pack it came from, and its release window are not confirmed.",
  "The 'unique collection' it unlocks is not identified. The Doggy Vinegolem pieces are the likely set, but no source ties them to the card.",
  "Retired status is unknown. Physical TCG packs stopped, which suggests the virtual rewards are no longer obtainable, but no source names this card's end date.",
  "No price is known: no coin store entry and no Station Cash listing was found.",
  "The Collection video frames show the card in a player's collection; they do not show where it came from.",
  "The 'live: yes' tag is only a first-pass hint. It is 'unsure' here because the card appears in video but no dated source confirms it is still obtainable."
 ]}
