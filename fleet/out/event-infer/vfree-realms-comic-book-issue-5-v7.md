<!-- fleet job=event-infer id=vfree-realms-comic-book-issue-5-v7 status=done turns=2 usd=0.0028 tokens(read,write,in,out)=[7701, 12334, 6, 2320] model=claude-haiku-5-5 -->
# Free Realms comic book issue #5

{"event": {"name": "Free Realms comic book issue code promotion (in-game code redemption for the comic issues)", "aliases": ["Free Realms Comic #5 Is On Sale Now!", "Free Realms comic issue codes"]},
 "kind": "promotion",
 "live": "unsure",
 "occurrences": [],
 "recurring": null,
 "zones": [],
 "npcs": ["Darkthorne"],
 "quests": [],
 "activities": ["Read the comic issues", "Enter the unique code found in an issue to redeem its in-game item"],
 "items": [
  {"name": "Spelunker's Shard", "price": null, "currency": "reward", "source": "wiki page: Spelunker's Shard (code from comic #9)"},
  {"name": "Flute of Slumber", "price": null, "currency": "reward", "source": "wiki page: Flute of Slumber (code from comic #10)"}
 ],
 "rewards": ["Spelunker's Shard (comic #9 code)", "Flute of Slumber (comic #10 code)"],
 "evidence": [
  {"claim": "Issue #5 of the Free Realms comic book is on sale; each of the 12 issues carries a unique code redeemable for a special in-game item.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=936 (article is undated in the pack; re-checked in articles.json)"},
  {"claim": "Issue #5 reveals a dangerous secret from Darkthorne and asks whether there is a spy in Queen Valerian's court.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=936 (fact quote: \"Darkthorne reveals a dangerous secret. Could there be a spy in Queen Valerian's court?\")"},
  {"claim": "A code can be found inside each issue and redeemed for exclusive items. This wording comes from a 2009-07-23 pre-launch preview, so it is plan-stage evidence only.", "source": "wiki page: Free Realms (comic); cited Joystiq preview http://www.joystiq.com/2009/07/23/free-realms-comic-coming-july-29-includes-in-game-bonuses/"},
  {"claim": "Spelunker's Shard is acquired by entering the code from comic #9.", "source": "wiki page: Spelunker's Shard"},
  {"claim": "Flute of Slumber is acquired by entering the code from comic #10.", "source": "wiki page: Flute of Slumber"}
 ],
 "confidence": 0.3,
 "open": [
  "MERGE, unresolved in this record: the 2009 WildStorm/DC print comic (issue #1 published July 29, 2009; $4.99 per issue; wiki: Free Realms, Free Realms Issue 1) is a separate thing from the in-game code promotion. Split it into its own record. The Joystiq 2009-07-23 item is a pre-launch preview ('coming July 29') and is not a live event.",
  "articleId=936 has no date in any source checked, so no year, month or window can be assigned. occurrences is empty and live is 'unsure'. A dated source is needed before this can be scheduled.",
  "Redemption window (when codes started and stopped working) is unsourced.",
  "Per-issue release dates for issues 2-12 are unsourced.",
  "Wiki-only per-issue items were NOT listed as rewards because they were not re-verified against their item pages: Spider Bite (issue 1), Mushroom Pizza (2), Team Rockabilly Nitrous System (3), Cloak of Shadows (4), Lightning Elixir (5), Darkthorne's Embrace (6), Bravery Biscuit (7), Stink Bombs (8), Floral Flair Shard (11), Masher Mask (12). Verify each before wiring.",
  "Collection items Eerie Gi (issues 1-4), Nightmarish Gloves (5-8) and Sinister Cowl (9-12) rest on wiki category lists only and are unverified.",
  "Creepy Construct is removed: its only source is a wiki page title, with no content tying it to the promotion.",
  "Quests are empty. The 'Comic Book Issues' and 'Certificate of Authenticity' locale titles (locale 416366-416387) show titles only; their in-game function is unsourced. locale:3952 is a flagged fragment and is not cited.",
  "Queen Valerian is named in the issue #5 article and in the wiki page 'Free Realms Issue 5' (plot text), but has no client NPC record in this pack. She is left out of npcs and is noted here instead.",
  "Item prices are null: the codes are rewards, not sales.",
  "Zones are unsourced for the comic and for code entry.",
  "Excluded: Ten Ton Hammer San Diego Comic-Con 2009 and 2011 PSN hits; Purple Triceratops (Fun! Online Games promotion, articleId=853)."
 ]}
