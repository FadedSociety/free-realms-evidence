<!-- fleet job=citem-infer id=ctalon-speedster-engine-117425-v1 status=nothing_found turns=4 usd=0.0039 tokens(read,write,in,out)=[32924, 18641, 10, 2469] model=claude-haiku-5-5 -->
# Talon Speedster Engine

{"item": {"name": "Talon Speedster Engine", "locale_id": 117425, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines 'Talon Speedster Engine' (locale 117425, description 'The customized engine for the Talon Speedster.', slot 1, class 98, definition 60900) with no coin store price in repo:data/content/stores.json.", "source": "locale:117425; client definition in evidence pack"},
  {"claim": "It is one part of the kart parts set for the Talon Speedster kart (Engine, Turbo 117426, Steering Column 117427, Tires 117428, Mod 117429), alongside the Burster, Privateer and other Speedster part sets.", "source": "locale:117420-117430 (client cluster)"},
  {"claim": "Kart parts are a Kart Racing progression item: the parts window has Engine, Boost, Steering, Traction, Slot A and Slot B tabs with a Power Rating.", "source": "notes/Build Guides/Gameplay/Kart Racing.md:24; video:FkCPRbskFVU/00000"},
  {"claim": "The kart named 'Talon Speedster' exists in the client (name locale 39224; chassis description locale 114643), but no wiki page, video frame, article fact or repo source names the Talon Speedster or its parts with a source, price, vendor, quest or drop.", "source": "lookup client/wiki/articles/video for 'Talon Speedster' and 'Speedster Engine'; repo and refs searches"},
  {"claim": "Only confirmed Speedster kart sources are unrelated: Blast Speedster from Sandstorm's Grand Opening quest reward, and Spooky Speedster as a Halloween kart (Seasonal, Super Spooktacular).", "source": "notes/Build Guides/Content/Jobs/Kart Driver.md:25; wiki page Spooky Speedster (Category:Seasonal, Category:Super Spooktacular)"}
 ],
 "confidence": 0.15,
 "open": [
  "No source for how the Talon Speedster Engine is obtained: no vendor, Station Cash Marketplace, Coin Shop, quest, drop, event, prize wheel or crafting evidence found.",
  "Live status not confirmed. The first-pass 'live: yes' is a hint only and no evidence supports it; the client defines the item but no in-game sighting is recorded.",
  "Client text 117538 and 117539 also name 'Talon Speedster' with description 'The customized engine/turbo for the Talon Speedster' (ids 117538/117539 are a second set of Talon parts). Unclear whether they are duplicates of 117425/117426 or a different tier; not resolved.",
  "Kart Driver's Clack (Kart Driver Equipment vendor, Tangletrack, Briarwood) is the only kart-parts vendor noted; stock and prices were never seen (Kart Driver.md:36). Checking Clack's stock for Talon parts is the next step.",
  "Power rating, price and whether the Talon kart is in the live race roster are unknown."
 ]}
