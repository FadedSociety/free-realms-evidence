<!-- fleet job=note-refresh id=Queen-to-Mae-Main-Road-Return status=nothing_found turns=7 usd=0.0102 tokens(read,write,in,out)=[107619, 42523, 16, 7613] model=claude-haiku-5-5 -->
# notes/Research/Queen to Mae Main Road Return.md

**Verdict:** current. I found no claim in this note that is now false, and no citation that moved. The note cites lab artifacts (`C:/Users/.../lab/reports/*.json`) and no repo code, so most of its numbers cannot be checked from the tip. The claims I could check agree with the notes they link to and with the later native review.

**Checked and consistent:**
- Both wiki links resolve: `notes/Research/Bartle to Queen Main Road Route.md` and `notes/Research/Pappy to Bartle Main Road Detour.md` exist.
- Reverse order 804→803→802→763→762→761→760→755 and the 755→753→bend(-1399,311)→751→…→747→bend(-1582,346)→748…→741→713 chain match the forward waypoints in `Bartle to Queen Main Road Route.md` (lines 19–27).
- The 713 fence jump is a "normal Space+W" input in run 193318. `Pappy to Bartle Main Road Detour.md` line 3 records a separate 19:51:18 Space+W 850 ms press crossing the low roadside fence near 713. That agrees with this note.
- "Route candidate ... 44 waypoints, 1316.78 m, `native_route_accepted=false`" matches `notes/Reviews/Native Return and Click Movement 235041.md` line 25.
- Reverse gates (lilypad support, ≈28° climb, fences) remain open. The 235041 review (lines 27–29, 45) says the reverse bridge and ramp still need original-support observation, and that the whole 44-point route is not accepted.

**Unsure (not corrections):**
- **Forward versus reverse status.** Lines 3 and 7 say the lilypad support, uphill descent and fences "remain gates". That is true for the reverse direction. `Bartle to Queen Main Road Route.md` lines 53–65 record a native forward traversal (run 203139, final receipt) through the climb and both lilypad bridges to a safe Queen endpoint, and `Tasks.md:113` agrees. The note does not say that the forward direction is already natively traversed, so a reader could take the gates as applying to both directions. I did not make this an edit because the note is not false as written. It could be clarified by adding "(forward direction natively traversed per [[Bartle to Queen Main Road Route]]; reverse remains gated)".
- **Missing reverse-walk result.** `Native Return and Click Movement 235041.md` lines 25–31 and 43–45 record a native reverse walk that reached index 24 of 43, stopped before Mae, and never delivered index 25. This note does not mention that attempt. It is an omission, not a falsehood, since the note already says no whole-route native acceptance is claimed.
- **Unverifiable numbers.** The SHA256 hashes, the 1,772 and 1,316.78 m figures, the 141.43 m connector grades and clearances, the −56.666724 ending floor, and the Mae/Cooking Table/fruit distances all sit in lab files outside the repo, so I could not check them.
