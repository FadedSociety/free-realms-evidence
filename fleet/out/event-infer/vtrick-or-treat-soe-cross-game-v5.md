<!-- fleet job=event-infer id=vtrick-or-treat-soe-cross-game-v5 status=done turns=3 usd=0.0035 tokens(read,write,in,out)=[19803, 12783, 8, 3449] model=claude-haiku-5-5 -->
# Trick-or-Treat (SOE cross-game event, 2011)

{
 "event": {
  "name": "Trick or Treat party, Sanctuary (2nd Annual Super Spooktacular, 2010)",
  "aliases": ["Super Spooktacular Trick or Treat (2010)", "Truco o Trato (Spanish text, article 1870)", "Friandise ou un Sort (French, article 1857)"]
 },
 "kind": "community",
 "live": "no",
 "occurrences": [
  {"year": 2010, "when": "Thursday 21 October 2010, 3pm Pacific (US/Latin America, Server 1); Friday 22 October 2010, 9am Pacific / 4pm GMT (UK/Europe, Server 1)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1864 ; http://www.freerealms.com/article/detail.action?articleId=1870 (dates quoted in an earlier pass; the article text was not re-read here, see open)"}
 ],
 "recurring": null,
 "zones": ["Sanctuary"],
 "npcs": ["Halloween Harry"],
 "quests": ["Trick-or-Treat", "Trick-or-Treat around Sanctuary"],
 "activities": [
  "Talk to Halloween Harry to start Trick or Treat and return daily for more candy (http://www.freerealms.com/article/detail.action?articleId=1857 ; locale:415052 says you can trick-or-treat every day in Sanctuary during the Halloween celebration)",
  "Travel around Sanctuary collecting candy from people in costume, then show Halloween Harry your candy (locale:415821 quest title; locale:415370 'Trick-or-treat around Sanctuary, collecting sweet treats from those in costume!')",
  "Use /scare on people to make them give candy (locale:415049 npc_dialog; article 1854 describes the same mechanic in Pixiewood, so the Sanctuary use is only shown by the client text)"
 ],
 "items": [],
 "rewards": [],
 "evidence": [
  {"claim": "A Trick or Treat party in Sanctuary celebrated the second anniversary of the Super Spooktacular edition, with Server 1 sessions in October 2010.", "source": "http://www.freerealms.com/article/detail.action?articleId=1870 (summary, verified)"},
  {"claim": "Super Spooktacular was the Free Realms Halloween festival; its second annual run returned in 2010 with the previous year's fun.", "source": "http://www.freerealms.com/article/detail.action?articleId=1861 (summary, verified: 'The second annual Super Spooktacular Halloween festival returned')"},
  {"claim": "Super Spooktacular first ran in 2009, scheduled October 14 to November 11, 2009.", "source": "http://www.tentonhammer.com:80/node/75739 (summary, verified)"},
  {"claim": "Halloween Harry gives daily Trick or Treat quests (client text).", "source": "locale:436401"},
  {"claim": "Quest title 'Trick-or-Treat' and 'Trick-or-Treat around Sanctuary' exist in the client.", "source": "locale:415050 ; locale:415821 (verified)"},
  {"claim": "Sanctuary party is a Halloween event with candy and costumes near the Sanctuary Warpstone.", "source": "locale:14567 ; locale:432174 (verified)"}
 ],
 "confidence": 0.5,
 "open": [
  "SPLIT: the 2011 SOE cross-game Trick-or-Treat promotion is a different event and is not in this record. Source: http://www.freerealms.com:80/article/detail.action?articleId=2322 ('Today through October 31, 2011, get treats and tricks when you visit your participating games each day'). Free Realms is listed as a participating game. No Free Realms items, quests or mechanics are in the source, and soe.com/trickortreat is not captured. Do not merge it with this record.",
  "The Super Spooktacular itself was live in 2011 too: article 2304 says it ran October 13 to November 23, 2011; article 2291 and 2301 cover an October 6, 2011 webcast. Those are the 2011 Spooktacular, not this Trick-or-Treat party, and the 2011 Trick-or-Treat quests were not checked.",
  "Dates for the 2010 party (21-22 Oct 2010, times) are from earlier-pass quotes of articles 1864 and 1870. Article 1870 summary confirms the October 2010 party; the exact days and times were not re-read in full and should be checked before use.",
  "Recurrence: Super Spooktacular recurs yearly (2009, 2010, 2011 per articles 1861, 2304, and TTH 75739). The Trick-or-Treat party itself is evidenced only for 2010, so recurring is null for this record.",
  "Pixiewood: earlier pass placed Harry and decorations there; article 1870 summary does not show that. Left out. The wiki puts Harry in Sanctuary.",
  "Quests not included: Bag Snatchers, Candy Gram, A Formal Report, Halloween Fanatic (Halloween Harry wiki page, Super Spooktacular questline; no source ties them to this party). 'Delicious Goo'd Candy' is excluded. 'Trick or Treat in Sanctuary' (locale:14563) and objective ids 415822-415824 and dialog 415052 were not re-verified as this party's quests; 415052 is quoted above only as client dialog.",
  "Duplicate quest titles (415050, 14563, 415821) are unresolved: some may be later reuse rather than the 2010 quests.",
  "Items: none tied to this event in any source. Price and currency unknown.",
  "Live: 'no' for the 2010 party (past). No source shows a current or scheduled Trick-or-Treat party. Do not wire as current.",
  "Video variants 'Trick-or-Treat Mystery Gift' and 'Trick-or-Treat Time?' (video:yWuHe_jYyc4/00272.jpg, /00274.jpg) are not merged; dates unknown.",
  "Aliases: bare 'Trick or Treat' / 'Trick-or-Treat' dropped because they overlap the 2011 SOE promotion."
 ]
}
