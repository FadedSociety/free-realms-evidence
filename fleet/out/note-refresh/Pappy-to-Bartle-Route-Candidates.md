<!-- fleet job=note-refresh id=Pappy-to-Bartle-Route-Candidates status=done turns=8 usd=0.0113 tokens(read,write,in,out)=[127781, 39577, 18, 10233] model=claude-haiku-5-5 -->
# notes/Research/Pappy to Bartle Route Candidates.md

**Verdict:** minor drift. The code-side claims hold at the tip: Pappy and Bartle coordinates match the content and tests, the 12 m interaction radius matches `npc_interaction.rs:52`, and the cited follow-up and Stage7 notes exist. Two statements are superseded by the Pappy→Bartle follow-up note written after this one. Everything else in the note is lab artifacts outside the repo and cannot be checked here.

**Corrections:**

1. `old:` Native reverse rocky descent and onward walking still require inspection; this supersedes the rejected cliff route as the next candidate.
   `new:` A retained run 193318 navigation/input proof records the reverse rocky gap (recorded A/D/W only) and the subsequent points up to the climb foot. That descent is still unaccepted, and onward walking still requires inspection; this supersedes the rejected cliff route as the next candidate ([[Pappy to Bartle Main Road Detour]]).
   `why:` `notes/Research/Pappy to Bartle Main Road Detour.md:3` and `:5` (the 193318 reverse gap reached `[-2163.7058,-50.537003,300.99753]` and the climb foot; "initial reverse rocky descent is separately unaccepted"). The candidates note omits this native evidence.

2. `old:` but their full bounds were not recovered or silently treated as known.
   `new:` but their full bounds were not recovered in that search rectangle. [[Pappy to Bartle Main Road Detour]] later resolves the billboard and roses to their original base ADRs for its corridor, and states that no appearances are unresolved there.
   `why:` `notes/Research/Pappy to Bartle Main Road Detour.md:50` ("Literal single-Actor XML ActorSets resolve the billboard and roses to their original base ADRs … No appearances are unresolved in this corridor.").

**Unsure:**
- The line-36 claim that the 151602 climb reached Pappy "farther east" than the candidate's west cliff path. `notes/Research/Stage7 Native Return Routes.md:59-72` confirms the climb path (X −2141 to −2183, Z 299 to 327) and its Pappy interaction at 1.60 m. I did not settle the east/west comparison against the candidate's path, which runs at Z 278 to 300.
- Lab-only counts and hashes: 95 DME meshes for 528 objects, 2,019-node MAP export, 303/307 source bindings, and "No source, content, saves or native input changed". These cite `C:/Users/Bryce/Documents/Projects/CartoonMMO/lab/...` outside the repo, so I could not verify them. The corridor counts in the follow-up (130 DME / 873 objects) use a different scope and do not contradict them.
- The Bartle relaxed endpoint distance (8.32 m) recomputes to about 8.33 m from the stated coordinates, which is within rounding.
