<!-- fleet job=event-infer id=vshrouded-glade-gloam-invasion-v7 status=done turns=2 usd=0.0034 tokens(read,write,in,out)=[7688, 11896, 6, 3687] model=claude-haiku-5-5 -->
# Shrouded Glade Gloam Invasion

```json
{
 "event": {
  "name": "Gloam Invasion (Shrouded Glade)",
  "aliases": ["Gloam Invasion", "Shrouded Gloam (wiki page title)", "Shrouded Glade gloam invasion (client string prefix)"]
 },
 "kind": "update",
 "live": "unsure",
 "occurrences": [
  {"year": 2012, "when": "start June 15, 2012 per wiki only; end unknown", "source": "wiki page: Shrouded Gloam (only source for the start date; no article gives a day)"},
  {"year": 2012, "when": "undated article announcing the invasion (captured June 2012, posted about 3 days 22 hours before capture)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2614"}
 ],
 "recurring": null,
 "zones": ["Shrouded Glade"],
 "npcs": ["General Drahk", "Queen Valerian", "Marius Shadetree", "Brickface", "Gloamtooth", "Arch Druid Camellia", "Gus Geargrinder"],
 "quests": ["This Glade is Ours!"],
 "activities": [
  "Fighting Gloam-corrupted monsters (Corrupted Viper, Corrupted Bird, Corrupted Wolf, Corrupted Druid) and Gloam Constructs in Shrouded Glade (wiki page: Shrouded Gloam; wiki page: Wolves)",
  "Defeating Gloam Constructs in the final battle (locale:438262 'Defeat Gloam constructs')",
  "Escorting to the third escort point in the final battle (locale:438259/438252 per prior pack, objective text; wiki page: Shrouded Gloam)",
  "Choosing to aid the Druids or the Dwarves (wiki page: Druids)"
 ],
 "items": [
  {"name": "Archer's Power Bow", "price": null, "currency": null, "source": "wiki page: Archer's Power Bow (category Gloam Invasion Weapons; SC Marketplace category). Price not stated in the source read."},
  {"name": "Medic's Power Fist", "price": null, "currency": null, "source": "wiki page: Medic's Power Fist (category Gloam Invasion Weapons; SC Marketplace category)"},
  {"name": "Warrior's Nature Claw", "price": null, "currency": null, "source": "wiki page: Warrior's Nature Claw (category Gloam Invasion Weapons; SC Marketplace category)"},
  {"name": "Wizard's Nature Wand", "price": null, "currency": null, "source": "wiki page: Wizard's Nature Wand (category Gloam Invasion Weapons; SC Marketplace category)"},
  {"name": "Brawler's Power Fist", "price": null, "currency": null, "source": "wiki category: Category:Gloam Invasion Weapons (page not re-read)"},
  {"name": "Ninja's Nature Claw", "price": null, "currency": null, "source": "wiki category: Category:Gloam Invasion Weapons (page not re-read)"}
 ],
 "rewards": [],
 "evidence": [
  {"claim": "Shrouded Glade was under siege by the Gloam, whose influence poured down from the Dawn Cascade and Daybreak Falls; Sunstone Dwarves and Shrouded Glade Druids were fighting it.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2614"},
  {"claim": "Shrouded Gloam is described as the main questline event from June 15th, 2012 to an unknown time, with Shrouded Glade under siege by the Gloam Invasion.", "source": "wiki page: Shrouded Gloam"},
  {"claim": "Client dialog names the event: 'General Drahk is summoning Elite Gloam Constructs to invade Shrouded Glade!'", "source": "locale:439"},
  {"claim": "Final-battle objective 'Defeat Gloam constructs' exists in the client.", "source": "locale:438262"},
  {"claim": "Category:Gloam Invasion Weapons lists six weapons 'released with the launch of Gloam Invasion'; each weapon page carries the Gloam Invasion Weapons category.", "source": "wiki category: Category:Gloam Invasion Weapons; wiki pages Archer's Power Bow, Medic's Power Fist, Warrior's Nature Claw, Wizard's Nature Wand"},
  {"claim": "Wiki says Druid-job pets Arcadius and Harley were tied to the invasion, but acquisition details were not confirmed in the pack.", "source": "wiki pages: Arcadius, Harley"},
  {"claim": "Pre-launch Twitch webcast planned Thursday June 14, 2012 (4pm US Pacific). A plan, not an occurrence, and not counted.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2622"}
 ],
 "confidence": 0.4,
 "open": [
  "Start date June 15, 2012 rests only on one wiki line. Article 2614 is undated (captured June 2012) and does not give June 15. End date unknown.",
  "Live status unsure: the client and wiki show an in-game run in 2012, but no source gives an end date or says it runs on the revival.",
  "Name is composed by us. No source gives the title 'Shrouded Glade Gloam Invasion'; the wiki page is 'Shrouded Gloam' and the wiki text says 'Gloam Invasion'.",
  "Sunstone Valley follow-on ('Sunstone Valley Trapped and Alone', locale:438476, wiki Quest:Trapped and Alone, 'Aiding our Allies') is EXCLUDED from this event. Articles 2781 and 2782 say Sunstone Valley begins where the Gloam Invasion story ends. Treat as a separate candidate, or a merged pack entry.",
  "Weapons: category membership is confirmed by wiki pages, but no price, currency or acquisition text was read. Marketplace category suggests station_cash but this is not stated in the source read; left null.",
  "Arcadius and Harley: wiki says acquired during the invasion (Arcadius via Druid jobs; Harley via the boss NPC in Shrouded Glade, also sold by Cragara with a blank price). Not listed as rewards until the acquisition is verified.",
  "'The Invasion of Shrouded Glade' comic (wiki) is a consumable from the limited-time 'Defending the Glade' quest. The link to this event is by the comic's content; the quest is not verified as part of this event, so it is not listed.",
  "Client strings locale:437148, 437267, 437783, 437789 dropped: flagged as internal dev notes or ability labels, not player-facing evidence.",
  "Exclusions from the prior pack (Pirate Party / Invasion in Seaside, Aug 18, 2009; Robgoblin, Ninjawug and Abominable invasions; locale:5101922 Halt the Invasion!) are not re-verified here; treat as unchecked.",
  "'Report to Sunspark' quest has no source tying it to the Glade invasion; not listed. 'Defend Shrouded Glade!' (locale:817) may equal wiki 'Defending the Glade'; unconfirmed, not listed.",
  "Gus Geargrinder is shown in the wiki as having died to defeat the Gloam during the invasion; debut and first appearance claims are dropped as unsourced.",
  "Video frames (wSb4fTZcnJE/00400.jpg, 00424.jpg) show the comic with Queen Valerian captioned; not re-read here."
 ]
}
```
