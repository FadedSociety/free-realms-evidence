<!-- fleet job=event-infer id=vfree-realms-comic-book-issue-5-v8 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[6477, 7041, 6, 2640] model=claude-haiku-5-5 -->
# Free Realms comic book issue #5

```json
{
 "event": {
  "name": "Free Realms comic book issue code promotion (in-game code redemption for comic issues)",
  "aliases": ["Free Realms Comic #5 Is On Sale Now!", "Free Realms comic issue codes"]
 },
 "kind": "promotion",
 "live": "unsure",
 "occurrences": [],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": [
  "Read the comic issues",
  "Find the unique code in an issue and enter it in game to receive that issue's item"
 ],
 "items": [
  {"name": "Flute of Slumber", "price": null, "currency": "reward", "source": "locale:5513 (item name); wiki page 'Flute of Slumber' says it is the comic #10 code reward. Tooltip text in locale:5514 ('Causes nearby opponents to fall asleep.') was not re-read in this pass."},
  {"name": "Spelunker's Shard", "price": null, "currency": "reward", "source": "locale:6957 (item name); wiki page 'Spelunker's Shard' says it is the comic #9 code reward. Code-to-item link not re-confirmed against the article."}
 ],
 "rewards": [
  "Flute of Slumber (comic #10 code, wiki)",
  "Spelunker's Shard (comic #9 code, wiki)"
 ],
 "evidence": [
  {"claim": "Issue #5 of the Free Realms comic book is on sale, and each of the 12 comic issues carries a unique code redeemable for a special in-game item.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=936 (article is undated in every source checked)"},
  {"claim": "Issue #5 reveals a dangerous secret from Darkthorne and asks whether there is a spy in Queen Valerian's court.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=936 (quote: \"Darkthorne reveals a dangerous secret. Could there be a spy in Queen Valerian's court?\")"},
  {"claim": "Queen Valerian is also named in the plot text of the wiki page 'Free Realms Issue 5'. No client NPC record was found for her.", "source": "wiki page: Free Realms Issue 5; articleId=936"},
  {"claim": "A code inside each issue redeems an exclusive item. This wording is from a 2009-07-23 Joystiq pre-launch preview, so it is plan-stage evidence only and does not prove a live window.", "source": "wiki page: Free Realms (comic), citing http://www.joystiq.com/2009/07/23/free-realms-comic-coming-july-29-includes-in-game-bonuses/"},
  {"claim": "Spelunker's Shard exists as a client item name.", "source": "locale:6957"},
  {"claim": "Flute of Slumber exists as a client item name.", "source": "locale:5513"},
  {"claim": "Spelunker's Shard is linked to the comic #9 code, and Flute of Slumber to the comic #10 code.", "source": "wiki pages: Spelunker's Shard; Flute of Slumber (not confirmed against a dated article)"}
 ],
 "confidence": 0.3,
 "open": [
  "MERGE / SPLIT: the 2009 WildStorm/DC print comic (issue #1 on sale July 29, 2009; about $4.99 per issue; wiki: Free Realms, Free Realms Issue 1) is a different thing from this in-game code promotion. It needs its own record, which is not built here. Joystiq 2009-07-23 is a pre-launch preview ('coming July 29') and not a live event.",
  "Dating: articleId=936 has no date in any source checked, so no year, month or window can be assigned. occurrences is empty and live is 'unsure'. A dated source is needed. The wiki's issue #10 cover text reads 2010; this is print-cover evidence only and is not a code window.",
  "Redemption window (when codes started and stopped working) is unsourced.",
  "Per-issue release dates for issues 2-12 are unsourced.",
  "Unverified wiki per-issue items, NOT listed as rewards: Spider Bite (1), Mushroom Pizza (2), Team Rockabilly Nitrous System (3), Cloak of Shadows (4), Lightning Elixir (5), Darkthorne's Embrace (6), Bravery Biscuit (7), Stink Bombs (8), Floral Flair Shard (11), Masher Mask (12). Each needs its wiki/client check before wiring.",
  "Collection items Eerie Gi (issues 1-4), Nightmarish Gloves (5-8) and Sinister Cowl (9-12) rest only on wiki category lists and are unverified. Not listed.",
  "Creepy Construct REMOVED: its only source is a wiki page title with no content tying it to the promotion.",
  "Darkthorne: named in the article 936 quote as a plot figure only. No client NPC record was cited, so he is not in npcs.",
  "Queen Valerian: no client NPC record in this pack, so she is not in npcs. She is sourced to articleId=936 and wiki 'Free Realms Issue 5'.",
  "Quests are empty. The 'Comic Book Issues' and 'Certificate of Authenticity' locale titles (locale 416366-416387) show titles only; their in-game function is unsourced. locale:3952 is a flagged fragment and is not cited.",
  "Item prices are null: the codes are rewards, not sales.",
  "Zones are unsourced for the comic and for code entry.",
  "Excluded: Ten Ton Hammer San Diego Comic-Con 2009 and 2011 PSN hits; Purple Triceratops (Fun! Online Games promotion, articleId=853)."
 ]
}
```
