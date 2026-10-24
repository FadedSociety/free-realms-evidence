<!-- fleet job=quest-critic id=wchef-craving-something-tasty-v2-evidence-r3 status=no_submit turns=4 usd=0.0023 tokens(read,write,in,out)=[16949, 7654, 10, 2310] model=claude-haiku-5-5 -->
# Chef: Craving Something Tasty

{"lens": "evidence", "pass": true, "score": 4, "problems": [{"field": "objectives[1]", "issue": "The talk objective's target 'Diggy' has no locale id. Text 101056 checks out, so the target name is just unlinked, not wrong.", "fix": "Optionally set target_locale_id for Diggy from the NPC data (wiki Diggy, Ocean Treasures Cafe) so the builder can link the NPC by name."}, {"field": "line", "issue": "The line position is left empty with no previous or next, and the answer says Hasty Food Delivery's ordering is unknown. This is an honest gap, not a fabricated link.", "fix": "Leave as is unless a chain source establishes order. The wiki lists Hasty Food Delivery as a Seaspray appearance only."}, {"field": "rewards", "issue": "Rewards are empty and the answer says they are unknown. No client text was found for them, so this is acceptable.", "fix": "None from the evidence available."}]}

Checks I ran against the client text:
- 101053 is "Craving Something Tasty" (title).
- 101061 is the offer text, which asks the player to bring something special to eat from the Ocean Treasures Cafe.
- 101063 is "Get a meal for Seaspray from the Ocean Treasures Cafe."
- 101058 is the cooking-minigame objective, with Diggy named.
- 101056 is "Speak with Diggy…".
- 101060 is the deliver objective, with the "Seapsray" typo kept as shipped.
- 101064 is the completion line.
- 101065 is the cooking hint.
- 101070 is the progress line.
- 93476 is Ocean Treasures Cafe.
- 21301 is Seaspray.
- The repo's Seaside NPC index and Chef.md both list Craving Something Tasty under Diggy/Seaspray. The wiki's Seaspray page lists it as a quest, and its Diggy page lists it as an appearance.

I found no flagged or placeholder line used as live, and no wrong id. The answer's own caveats (no record id, unverified repo title id 811105456, unknown reward) are stated openly.
