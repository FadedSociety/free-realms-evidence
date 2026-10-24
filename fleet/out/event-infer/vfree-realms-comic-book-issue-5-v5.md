<!-- fleet job=event-infer id=vfree-realms-comic-book-issue-5-v5 status=done turns=2 usd=0.0032 tokens(read,write,in,out)=[8943, 10120, 6, 3710] model=claude-haiku-5-5 -->
# Free Realms comic book issue #5

```json
{
 "event": {
  "name": "Free Realms comic book issue codes (in-game code redemption for the 12-issue comic)",
  "aliases": ["Free Realms comic", "Free Realms comic book", "Free Realms Comic Book Series 1", "Free Realms Comic Book Issues 1-4 / 5-8 / 9-12", "Free Realms Issue 1", "Free Realms Comic #5"]
 },
 "kind": "promotion",
 "live": "unsure",
 "occurrences": [
  {"year": 2009, "when": "July 29, 2009 (print issue #1 publication by WildStorm/DC; wiki only, no article)", "source": "wiki page: Free Realms Issue 1"},
  {"year": null, "when": "Undated (issue #5 'on sale now' post; article has no date)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=936"}
 ],
 "recurring": null,
 "zones": [],
 "npcs": ["Darkthorne", "Queen Valerian"],
 "quests": ["Free Realms Comic Book Series 1", "Free Realms Comic Book Issues 9-12", "Comic Book Issues 1-4", "Comic Book Issues 5-8", "Comic Book Issues 9-12"],
 "activities": ["Read the comic book issues (print/web)", "Enter the unique code from each issue to redeem its in-game item"],
 "items": [
  {"name": "Spider Bite", "price": null, "currency": "reward", "source": "wiki page: Free Realms (comic), Exclusive Items list (Issue 1)"},
  {"name": "Mushroom Pizza", "price": null, "currency": "reward", "source": "wiki page: Free Realms (comic), Exclusive Items list (Issue 2)"},
  {"name": "Team Rockabilly Nitrous System", "price": null, "currency": "reward", "source": "wiki page: Free Realms (comic), Exclusive Items list (Issue 3)"},
  {"name": "Cloak of Shadows", "price": null, "currency": "reward", "source": "wiki page: Free Realms (comic), Exclusive Items list (Issue 4)"},
  {"name": "Lightning Elixir", "price": null, "currency": "reward", "source": "wiki page: Free Realms (comic), Exclusive Items list (Issue 5)"},
  {"name": "Darkthorne's Embrace", "price": null, "currency": "reward", "source": "wiki page: Free Realms (comic), Exclusive Items list (Issue 6)"},
  {"name": "Bravery Biscuit", "price": null, "currency": "reward", "source": "wiki page: Free Realms (comic), Exclusive Items list (Issue 7)"},
  {"name": "Stink Bombs", "price": null, "currency": "reward", "source": "wiki page: Free Realms (comic), Exclusive Items list (Issue 8)"},
  {"name": "Spelunker's Shard", "price": null, "currency": "reward", "source": "wiki page: Free Realms (comic), Exclusive Items list (Issue 9)"},
  {"name": "Flute of Slumber", "price": null, "currency": "reward", "source": "wiki page: Flute of Slumber (code from comic #10); locale:5513"},
  {"name": "Floral Flair Shard", "price": null, "currency": "reward", "source": "wiki page: Free Realms (comic), Exclusive Items list (Issue 11)"},
  {"name": "Masher Mask", "price": null, "currency": "reward", "source": "wiki page: Free Realms (comic), Exclusive Items list (Issue 12)"},
  {"name": "Eerie Gi", "price": null, "currency": "reward", "source": "wiki page: Free Realms (comic), Collection Rewards (issues 1-4); locale:3952 (resolves to 'Eerie Gi')"},
  {"name": "Nightmarish Gloves", "price": null, "currency": "reward", "source": "wiki page: Free Realms (comic), Collection Rewards (issues 5-8); wiki page: Nightmarish Gloves (codes for issues 5-8)"},
  {"name": "Sinister Cowl", "price": null, "currency": "reward", "source": "wiki page: Free Realms (comic), Collection Rewards (issues 9-12)"},
  {"name": "Creepy Construct", "price": null, "currency": "reward", "source": "wiki page: Creepy Construct (codes from all twelve comic books); wiki-only, unverified"}
 ],
 "rewards": ["Per-issue in-game items listed above", "Collection items: Eerie Gi (1-4), Nightmarish Gloves (5-8), Sinister Cowl (9-12)", "Creepy Construct (all twelve codes; wiki-only)"],
 "evidence": [
  {"claim": "Issue #5 of the Free Realms comic book is on sale now (undated post).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=936"},
  {"claim": "The comic has 12 issues; each issue's unique code redeems a special in-game item.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=936"},
  {"claim": "Issue #5 reveals a secret from Darkthorne and hints at a spy in Queen Valerian's court.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=936"},
  {"claim": "Free Realms #1 published July 29, 2009 by WildStorm (DC). Print publication; wiki statement only.", "source": "wiki page: Free Realms Issue 1"},
  {"claim": "Pre-launch plan only: a July 23, 2009 Joystiq preview said the series would arrive July 29, 2009. Plan, not a live event.", "source": "wiki page: Free Realms (comic), citing joystiq 2009/07/23 article"},
  {"claim": "Exclusive item list per issue 1-12.", "source": "wiki page: Free Realms (comic)"},
  {"claim": "Flute of Slumber is acquired by entering the code from comic #10.", "source": "wiki page: Flute of Slumber; locale:5513"},
  {"claim": "Eerie Gi is a valid locale name (locale:3952 = 'Eerie Gi'); the automatic FLAG was a fragment artifact, the name itself resolves.", "source": "locale:3952"},
  {"claim": "Certificate of Authenticity quests exist for issues 1-12 and the collection titles exist in client.", "source": "locale:416366-416387"}
 ],
 "confidence": 0.4,
 "open": [
  "MERGE NOT RESOLVED: The pack combines two things. (a) The 2009 print comic series (WildStorm/DC; issue #1 dated July 29, 2009 by wiki only). (b) The in-game code redemption. Only (b) has article support (articleId=936), and that article is undated. Recommend splitting into two records before wiring; this record is written as (b) with (a) kept as a dated, wiki-only occurrence.",
  "Issue #5 article (articleId=936) is undated, so no year or month can be assigned to the in-game promotion. live is 'unsure' until a dated article is found.",
  "Per-issue release dates for issues 2-12 are not in any source.",
  "Redemption window (when codes stopped working) is unsourced.",
  "Zones are empty: no zone is sourced for the comic or for code entry.",
  "Certificate of Authenticity quests (issues 1-12): linked by title only; their in-game function is not sourced.",
  "Item prices are null: items are reward-by-code, not sold.",
  "Creepy Construct, Nightmarish Gloves, Sinister Cowl, Floral Flair Shard, Masher Mask, Eerie Gi and Stink Bombs rely on wiki pages not in the pack; verify before wiring.",
  "Queen Valerian is named only in the issue #5 article; no client or wiki NPC record.",
  "Joystiq 2009-07-23 preview is cited only via the wiki; the article is not in the pack.",
  "Excluded: Ten Ton Hammer San Diego Comic-Con 2009 and 2011 PSN hits (not about this comic); Purple Triceratops (Fun! Online Games promotion, articleId=853)."
 ]
}
```
