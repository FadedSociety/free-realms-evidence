You judge one quest objective spec for Bryce's Free Realms revival (a rebuild of Sony's 2009-2014 MMO from its
original client). The spec has every id its kind needs, but an earlier pass left it "unknown" with a note. Decide
whether it can be wired now with its doubtful values marked (R), or must wait for evidence.

Bryce's rules: gameplay numbers stay live-tunable data, and a reasoned value is fine when it is flagged (R) before
anything builds on it. So:
- settled_r: every remaining doubt is a reasoned NUMBER or wording choice that can stay tunable (a count the client
  text does not state, "some cray" -> 1, a quantity from a guide), AND `local_check` confirms the id: an NPC row that
  world.rs draws, an enemy definition we ship, a client item definition, a recipe row, a minigame id other content
  uses. Name each (R) value in `r_values`.
- keep: an id is only a candidate or proxy (the note says unverified, candidate, proxy, look-alike, or local_check
  says NOT / no row / NOT drawn / no other content uses it), a position has no source, the objective may belong to
  another quest, or the kind itself is in doubt.
When unsure, keep. You have no tools except `submit`.

Your `submit` result is ONE JSON object and nothing else:
{"id": "<quest>-o<index>", "verdict": "settled_r" | "keep", "r_values": ["count 1 (text gives no number)"],
 "reason": "one or two sentences naming the deciding doubt or why every doubt is a tunable (R) value"}
