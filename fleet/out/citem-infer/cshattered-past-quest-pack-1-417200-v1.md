<!-- fleet job=citem-infer id=cshattered-past-quest-pack-1-417200-v1 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[3499, 10195, 6, 1840] model=claude-haiku-5-5 -->
# Shattered Past - Quest Pack 1

{"item": {"name": "Shattered Past - Quest Pack 1", "locale_id": 417200, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition 62539 is a quest-pack item (slot 0, class 1, no models, no coin store price), so no coin vendor sale is recorded for it in our store data.", "source": "client definition in pack; repo:data/content/stores.json has no entry for it"},
  {"claim": "Item text says Card duelists challenge Sir Wellington and friends to win Shattered Past cards, found outside the Vale of the Ancients in Bristlewood, and that the pack is also included in the Shattered Past - Quest Bundle.", "source": "locale:417200, locale:417203"},
  {"claim": "Sibling pack texts say each pack must be purchased and completed in order: Pack 2 requires Pack 1 (locale:417204 for Dominic, which says to have purchased and completed Pack 1), and Pack 3 requires Pack 2 (locale:156878, locale:417205).", "source": "locale:417204, locale:417205, locale:156878"},
  {"claim": "Our notes place Sir Wellington and Dominic outside the Vale of the Ancients in Bristlewood, matching the pack text.", "source": "repo:notes/Build Guides/Content/Dungeons/Vale of the Ancients.md:95; repo:notes/Build Guides/Content/NPCs/NPCs - Briarwood.md:115"},
  {"claim": "Quest-line notes for the Shattered Past quest packs (TCG Series 2) list quests but name no giver or purchase source for the packs; the wiki has no article for this item.", "source": "repo:notes/Build Guides/Content/Jobs/Card Duelist.md:117, :278"}
 ],
 "confidence": 0.3,
 "open": [
  "No source for how a player buys Quest Pack 1: no coin store price in the client definition, no wiki category (SC Marketplace, Coin Shop, etc.), no vendor stock, and no article fact name it. Sources must be confirmed before this item is given a price or source.",
  "Price and currency unknown. The 'also included in the Shattered Past - Quest Bundle' text implies a bundle sale, but the bundle's own item and price were not found in the evidence pack.",
  "Live status is unsure: the client defines the item unflagged, but the pack-2 text (locale:417201) is flagged placeholder and no wiki or article confirms the pack is still sold or was retired.",
  "Whether the pack is delivered as a quest-unlock item (consumed on completion) or stays in inventory is not shown in the evidence.",
  "The client text for Pack 1 (locale:417200) carries no quest_dialog or quest_objective line naming an NPC for the pack; the NPC and location come only from locale:417203 and locale:417204."
 ]}
