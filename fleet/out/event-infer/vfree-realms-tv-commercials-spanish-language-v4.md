<!-- fleet job=event-infer id=vfree-realms-tv-commercials-spanish-language-v4 status=done turns=2 usd=0.0032 tokens(read,write,in,out)=[8840, 12792, 6, 3080] model=claude-haiku-5-5 -->
# Free Realms TV commercials (Spanish-language)

{
 "event": {"name": "Free Realms television commercials (series; not one event)", "aliases": ["Free Realms TV Spot", "Free Realms [TV] Commercial", "Free Realms Commercial"]},
 "kind": "promotion",
 "live": "unsure",
 "occurrences": [],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": [
  "Watch the TV commercial on freerealms.com or the official YouTube channel (2147, 2148, 2149; 2151 for the Portuguese post)"
 ],
 "items": [],
 "rewards": [],
 "evidence": [
  {"claim": "The pack's name 'Free Realms TV commercials (Spanish-language)' merges several separate commercials in English, Spanish, French and Portuguese. It is a series, not one live event. Split it into one entry per commercial.", "source": "http://www.freerealms.com/article/detail.action?articleId=752 ; articles index (fact:release/event/housing entries below)"},
  {"claim": "Second TV commercial featuring the Yeti: freerealms.com posted that a second television commercial was available to watch. Undated.", "source": "http://www.freerealms.com/article/detail.action?articleId=746 ; http://www.freerealms.com/article/detail.action?articleId=756&request_locale=en_US ; http://www.freerealms.com/article/detail.action?articleId=757"},
  {"claim": "Third TV commercial, themed on housing (Viviendas): Spanish news post announcing it. 822 and 823 carry the same quote, so they may be one post under two URLs. Undated.", "source": "http://www.freerealms.com/article/detail.action?articleId=822&request_locale=en_US ; http://www.freerealms.com/article/detail.action?articleId=823&request_locale=en_US"},
  {"claim": "Activities TV commercial (biking, creating houses, showing outfits, farming). 2147 is an English-language post; 2148 and 2149 are Spanish posts with the same text. Undated, and 2148 was captured June 2011 per its summary, which is a capture date, not a post date.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2147 ; http://www.freerealms.com/article/detail.action?articleId=2148 ; http://www.freerealms.com/article/detail.action?articleId=2149"},
  {"claim": "'Tiger Ride [TV] Spot' news item announcing a new TV commercial. Relative timestamp only ('Posted 2 days, 2 hours ago'); no absolute date.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1747"},
  {"claim": "'Party Time' TV commercial: a PRE-LAUNCH PREVIEW on the What's New page, not a confirmed live run. Captured April 2010, but that is a capture date. A French-language preview of the same spot is article 1203 ('Temps de Faire la Fête!').", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1199 ; http://www.freerealms.com/article/detail.action?articleId=1203"},
  {"claim": "New-adventures TV commercial, viewable on the official YouTube channel. Portuguese-language post, undated.", "source": "http://www.freerealms.com/article/detail.action?articleId=2151"},
  {"claim": "Halloween Super Spooktacular TV commercial: Spanish news post ('Un Espacio en la TV - Halloween Super Spooktacular'). Relative timestamp only ('7 months, 1 week ago'). Tied to the Halloween holiday, so keep it separate from the generic series.", "source": "http://www.freerealms.com/article/detail.action?articleId=1876"},
  {"claim": "Wiki appearance pages list a 'Halloween [TV] Spot 2010' and a 'Spooktacular [Commercial]' (Pumpkin Prince), and 'Ninja Prank [Commercial]', 'Super Ego [Commercial]', 'Holiday [TV] Spot', 'Snow Days [Commercial]', 'Yeti [TV] Spot' and 'New Adventures TV Commercial' pages exist. These show that the commercials exist; they do not give a post date.", "source": "wiki: Pumpkin Prince; Chatty; Abominable Snowman; File:Free Realms New Adventures TV Commercial"}
 ],
 "confidence": 0.25,
 "open": [
  "Name: the Spanish-language label was wrong. Sources are English (746, 757 text, 1747, 1199, 2147), Spanish (752, 756, 757, 822, 823, 1876, 2148, 2149), Portuguese (2151) and French (1203). Rename to a neutral series name and split into per-commercial entries, as above.",
  "No absolute dates exist in the pack for any commercial. The only dated hints are relative timestamps (1747, 1876) and capture dates (1199 April 2010, 2148 June 2011, 82 2009-05-17), which are not post dates. Occurrences stay empty until a dated article is found.",
  "Halloween Super Spooktacular (1876) may be 2010 per the wiki title 'Halloween [TV] Spot 2010', but that is a wiki title, not an article date. Unsure until dated.",
  "Ninja Prank [Commercial] (article 82) and Super Ego [Commercial] (article 95): only wiki appearance pages and URL entries support them. No article text or date was found, and the earlier 'confirmed by lookup' claim was not borne out. Not included as entries.",
  "Possible duplicates: 746/756/757 (second Yeti commercial), 822/823 (third housing commercial), 2147/2148/2149 (activities). Counted once each here.",
  "Locale-id checks from the earlier answer are dropped: locale ids are a separate table from article ids and do not confirm or deny articles.",
  "752 is a series-level Spanish post (new TV commercials shown, with a new video). It names no commercial and gives no date. The earlier headline alias 'Un Espacio en la TV: Free Realms y las Festividades' is not supported by the captured text and is dropped.",
  "No prices, currencies, zones, NPCs, quests or rewards are sourced for any of these commercials, so those fields are empty.",
  "Recommendation: do not log this as a live event. Log each commercial separately as kind 'promotion', live 'unsure', until dated sources are found."
 ]
}
